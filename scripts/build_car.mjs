#!/usr/bin/env node
/**
 * 把静态站点目录打包成 IPFS CAR，并输出 root CID。
 *
 * 用法：node scripts/build_car.mjs <source-dir> <car-path> <cid-path>
 *
 * 合同（由 tests/test_build_car.py 锁定）：
 *   - root 是 dag-pb 目录节点，站点根目录即 DAG 根
 *   - 同一份输入必然得到同一个 root CID（内容寻址，不掺时间戳）
 *   - 包含隐藏文件；遇到符号链接直接失败
 *   - 成功时输出 ROOT_CID= / CAR_PATH= / CAR_BYTES= / FILES= / BLOCKS=，
 *     并写根 CID 文件与 GITHUB_OUTPUT
 *   - 失败时退出码 1，原因写 stderr
 *
 * 依赖：@ipld/car + ipfs-unixfs-importer（版本锁定在 package.json）。
 * 两者已覆盖打包所需的全部能力，不需要额外的包装层。
 *
 * 打包参数取 `unixfs-v1-2025` profile：CIDv1 + raw leaves + 1 MiB 定长分块 +
 * 每层最多 1024 个链接。参数属于对外合同的一部分——改动会改变 root CID。
 */
import fs from 'node:fs'
import fsp from 'node:fs/promises'
import path from 'node:path'
import { Readable } from 'node:stream'
import { pipeline } from 'node:stream/promises'
import { CarWriter } from '@ipld/car/writer'
import { importer } from 'ipfs-unixfs-importer'
import { CID } from 'multiformats/cid'

/** CAR 头部先写占位根，全部块写完后回填真实根。 */
const PLACEHOLDER_ROOT = CID.parse('bafybeigdyrzt5sfp7udm7hu76uh7y26nf3efuylqabf3oclgtqy55fbzdi')

/** 打包参数：CIDv1 / raw leaves / 1 MiB 分块 / 每层最多 1024 个链接。 */
const IMPORT_PROFILE = 'unixfs-v1-2025'

function fail(message) {
  console.error(message)
  process.exit(1)
}

function walk(rootDir) {
  const files = []
  const stack = [{ abs: rootDir, rel: '' }]
  while (stack.length > 0) {
    const current = stack.pop()
    for (const name of fs.readdirSync(current.abs)) {
      const abs = path.join(current.abs, name)
      const rel = current.rel ? `${current.rel}/${name}` : name
      const stat = fs.lstatSync(abs)
      if (stat.isDirectory()) {
        stack.push({ abs, rel })
      } else if (stat.isSymbolicLink() || stat.isFile()) {
        // 符号链接按内容地址化会把目标位置写进 DAG，站点构建不会产出软链，直接拒绝。
        if (stat.isSymbolicLink()) fail(`Refusing to pack symbolic link: ${abs}`)
        files.push({ abs, rel })
      }
    }
  }
  // 排序只为让 CAR 的块顺序稳定，便于比对产物；DAG 结构与顺序无关。
  files.sort((a, b) => (a.rel < b.rel ? -1 : a.rel > b.rel ? 1 : 0))
  return files
}

function parseArgs(argv) {
  if (argv.length !== 3) {
    fail('Usage: build_car.mjs <source-dir> <car-path> <cid-path>')
  }
  const [sourceDir, carPath, cidPath] = argv
  if (!fs.existsSync(sourceDir) || !fs.statSync(sourceDir).isDirectory()) {
    fail(`Source directory does not exist: ${sourceDir}`)
  }
  if (!fs.existsSync(path.join(sourceDir, 'index.html'))) {
    fail(`Source directory is missing index.html: ${sourceDir}`)
  }
  fs.mkdirSync(path.dirname(path.resolve(carPath)), { recursive: true })
  fs.mkdirSync(path.dirname(path.resolve(cidPath)), { recursive: true })
  return { sourceDir, carPath, cidPath }
}

async function buildCar({ sourceDir, carPath }) {
  const files = walk(sourceDir)
  if (files.length === 0) fail(`Source directory is empty: ${sourceDir}`)

  const { writer, out } = await CarWriter.create([PLACEHOLDER_ROOT])
  const carWritten = pipeline(Readable.from(out), fs.createWriteStream(carPath))

  let blocks = 0
  let blockBytes = 0
  const blockstore = {
    // ipfs-unixfs-importer 的 blockstore 约定是 put(cid, bytes, options)。
    async put(cid, bytes) {
      blocks += 1
      blockBytes += bytes.length
      await writer.put({ cid, bytes })
    },
  }

  async function* source() {
    for (const file of files) {
      yield { path: file.rel, content: fs.createReadStream(file.abs) }
    }
  }

  let root
  for await (const entry of importer(source(), blockstore, {
    profile: IMPORT_PROFILE,
    wrapWithDirectory: true,
  })) {
    if (entry.path === '') root = entry.cid
  }
  if (root == null) fail('Importer did not produce a root CID')

  await writer.close()
  await carWritten

  const fd = await fsp.open(carPath, 'r+')
  await CarWriter.updateRootsInFile(fd, [root])
  await fd.close()

  return { root, files: files.length, blocks, blockBytes }
}

const args = parseArgs(process.argv.slice(2))
const { root, files, blocks, blockBytes } = await buildCar(args)

await fsp.writeFile(args.cidPath, `${root}\n`)

const carSize = fs.statSync(args.carPath).size
console.log(`ROOT_CID=${root}`)
console.log(`CAR_PATH=${args.carPath}`)
console.log(`CAR_BYTES=${carSize}`)
console.log(`FILES=${files}`)
console.log(`BLOCKS=${blocks}`)
console.log(`BLOCK_BYTES=${blockBytes}`)

if (process.env.GITHUB_OUTPUT) {
  await fsp.appendFile(process.env.GITHUB_OUTPUT, `ROOT_CID=${root}\n`)
}
