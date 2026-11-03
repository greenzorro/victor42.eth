# victor42.eth 博客部署备忘录

> 文档定位：这是 `victor42.eth` 博客当前部署方案的长期备忘。本文只记录稳定架构、职责边界、验证入口和排障顺序；具体实现以博客仓库中的 workflow 和脚本为准。本文不记录 Filebase Access Key、Secret Key、4EVER Pin token、GitHub Secrets 具体值、钱包私钥等敏感信息。

## 当前架构

主站：

```text
victor42.eth
→ ENS contenthash
→ Filebase IPNS
→ GitHub Actions 生成的 latest IPFS CID
→ Hugo 静态站点
```

内容冗余：

```text
GitHub Actions 生成 ROOT_CID
→ Filebase pin
→ 4EVER Pin（非阻塞）
→ Filebase IPNS
```

依赖原则：

```text
Pin = 内容可用性的前提
IPNS = 可变指针优化
ENS = 最终入口指针
```

发布时必须先确保 ROOT_CID 至少已被 Filebase pin。4EVER Pin 是非阻塞的第二保存点，应该在更新 IPNS 前尽量执行，但不阻塞发布。IPNS 只是让 ENS 可以长期指向一个稳定名称；如果 IPNS 异常，只要 CID 已可靠 pin，ENS 可以直接指向 `ipfs://<ROOT_CID>`。

备用站：

```text
blog.victor42.work
→ GitHub Pages
→ gh-pages 分支
→ Hugo 静态站点
```

日常发布流程保持不变：

```text
改内容
git commit
git push origin main
```

push 后由 GitHub Actions 自动完成主站和备用站发布。

## 背景

这个架构的直接背景是：之前依赖的第三方托管 IPNS 曾出现“ENS 记录可读到 IPNS key，但公共网关无法解析该 IPNS 记录”的故障。当前方案把生产 IPNS 交给 Filebase 托管，并用 Filebase Pin 和 4EVER Pin 保存同一个 GitHub Actions 产出的 CID，目标是在不维护 24/7 自有节点的前提下，保留 IPFS/IPNS 工作流并增加内容冗余。

## 公共网关现状（2026-11）

ipfs.io 与 dweb.link 已于 2026 年 9 月日落，不再接受程序化流量：

```text
2026-08-24  Shipyard 宣布停止 IPFS 相关维护，最后工作日 2026-09-30
2026-08-25  IPFS 官方博客宣布公共网关转向浏览器端 service worker 模式
2026-09-01  ipfs.io 开始按小时递增拒绝程序化流量
2026-09-21  最后一天接受程序化请求（响应头 sunset: Mon, 21 Sep 2026）
```

后果：`https://ipfs.io/ipfs/<CID>/` 与 `https://ipfs.io/ipns/<name>/` 一律返回 429（`retry-after: 900`），不能再作为验证入口；`dist.ipfs.tech`、`trustless-gateway.link` 等同步下线。

本仓库的发布链路不依赖上述任何一项：打包用 `@ipld/car` + `ipfs-unixfs-importer`（依赖锁定在 `package-lock.json`），pin 与 IPNS 由 Filebase / 4EVERLAND 的商业 API 完成。公共网关只出现在人工验证环节，用的是 `ipfs.filebase.io`。

## CAR 打包工具链

`scripts/build_car.mjs` 把 Hugo 的 `public/` 打成单文件 CAR 并算出 root CID。依赖锁定在仓库根 `package.json` / `package-lock.json`，CI 用 Node 18 + `npm ci --omit=dev` 安装：

```text
@ipld/car@5.4.7
ipfs-unixfs-importer@17.1.1
```

打包参数取 UnixFS v1 的常规组合，即 `ipfs-unixfs-importer` 的 `unixfs-v1-2025` profile：

```text
CIDv1 + raw leaves + 1 MiB 定长分块 + 每层最多 1024 个链接
```

由此得到两条可依赖的性质：同一份 `public/` 必然产出同一个 root CID；换个时间、换台机器、换个 Node 版本都不改变 CID。

脚本的行为边界：

- 包含隐藏文件（如 `.well-known/`），站点里有就会发布
- 遇到符号链接直接失败，不把不确定的 DAG 结构发出去
- 源目录不存在或缺 `public/index.html` 时退出码 1
- 输出 `ROOT_CID=`、`CAR_PATH=`、`CAR_BYTES=`、`FILES=`、`BLOCKS=`，同时写入根 CID 文件与 `GITHUB_OUTPUT`

`tests/test_build_car.py` 锁住上述合同：目录根 CID、同输入同 CID、跨分块文件、隐藏文件、两种失败路径、`GITHUB_OUTPUT` 契约。

## 关键入口

博客仓库：

```text
本仓库
greenzorro/victor42.eth
```

主 IPFS 发布 workflow：

```text
.github/workflows/publish-ipfs.yml
```

GitHub Pages 备用站 workflow：

```text
.github/workflows/deploy-github-pages.yml
```

发布脚本：

```text
scripts/build_car.mjs          # Hugo 输出 → CAR + root CID
scripts/filebase_pin_car.py
scripts/filebase_update_ipns.py
scripts/foureverland_client.py
scripts/foureverland_pin.py
```

GitHub Secrets 名称：

```text
FILEBASE_ACCESS_KEY
FILEBASE_SECRET_KEY
FILEBASE_BUCKET
FILEBASE_IPNS_NAME
FOUREVERLAND_TOKEN
```

## 服务职责

Filebase：

```text
消费 GitHub Actions 生成的 ROOT_CID
上传并 pin 同一个 CAR
Filebase pin 成功后清理旧 release CAR
托管 IPNS name
在 Filebase pin 成功、4EVER Pin 尝试完成后将 IPNS 指向 ROOT_CID
保留最近 10 个 release CAR
```

4EVER Pin：

```text
消费 GitHub Actions 生成的 ROOT_CID
pin 同一个 CID
4EVER Pin 成功或确认已存在后清理旧 workflow pins
作为第二 pin 服务提供内容冗余
失败不阻塞 Filebase IPNS 更新
只清理 workflow 自己创建的 pins
保留最近 10 个 workflow pins
```

GitHub Pages：

```text
服务中心化备用域名 blog.victor42.work
不参与 ENS / IPNS / IPFS 主链路
```

## 公开标识

主站：

```text
https://victor42.eth.limo/
```

备用站：

```text
https://blog.victor42.work/
```

Filebase IPNS：

```text
label: victor42-eth
network_key: k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud
```

ENS contenthash 应指向：

```text
ipns://k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud
```

## 验证命令

验证主站：

```bash
curl --noproxy '*' -I -L --max-time 80 https://victor42.eth.limo/
```

期望看到：

```text
HTTP/2 200
x-ipfs-path: /ipns/k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud/
x-ipfs-roots: <当前 CID>
```

验证 Filebase IPNS（走 Filebase 自己的共享网关，不依赖任何公共网关）：

```bash
curl -I -L --max-time 80 \
  https://ipfs.filebase.io/ipns/k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud/
```

期望看到 `HTTP/2 200`，且 `content-length` 与主站页面一致（说明 IPNS 指向的就是当前发布的 CID）。

注意两点：

1. 不加 `--noproxy '*'`。直连经常连不通，而走系统代理反而能通；和主站那条命令的行为相反。
2. `ipfs.filebase.io` 是共享网关，域名在国内网络会被间歇性 DNS 污染（解析到无关 IP，表现为连接超时或 TLS 握手失败）。这只是本地解析问题，不代表发布失败。生产验证建议在 Filebase 控制台开通专用网关，用 `https://<gateway-name>.myfilebase.com` 代替：独立域名不会被污染，也不与共享网关争带宽。

验证 ENS / eth.limo 解析：

```bash
curl --noproxy '*' -sS \
  'https://dns.eth.limo/dns-query?name=victor42.eth&type=TXT'
```

验证备用站：

```bash
curl --noproxy '*' -I -L --max-time 30 https://blog.victor42.work/
```

期望备用站响应来自 GitHub Pages：

```text
HTTP/2 200
server: GitHub.com
```

## 排障顺序

1. 看 GitHub Actions：`Publish IPFS Site` 是否成功，注意 `Install CAR Build Dependencies`（`npm ci`）与 `Pack site as CAR` 两步。
2. 看 Filebase pin：CAR 上传是否成功，Filebase 返回 CID 是否等于 ROOT_CID。
3. 看网关：`https://ipfs.filebase.io/ipfs/<CID>/` 是否可访问（不要用 ipfs.io）。连不上时先排除本地 DNS 污染，或用专用网关。
4. 看 4EVER Pin：对应 CID 是否已被 pin；4EVER Pin 异常不应阻塞 Filebase IPNS 更新。
5. 看 Filebase IPNS：`https://ipfs.filebase.io/ipns/<IPNS name>/` 是否指向最新 CID。
6. 看 ENS / eth.limo：ENS contenthash 是否仍指向当前 Filebase IPNS，或是否需要临时改为 `ipfs://<CID>`。
7. 看 GitHub Pages：`Deploy to GitHub Pages` 是否成功；只影响备用域名。

## 应急原则

Filebase IPNS 异常但 CID 可访问时，可以临时把 ENS contenthash 改为：

```text
ipfs://<latest CID>
```

Filebase 内容不可取时，优先查看 4EVER Pin 是否已保存同一 CID，再重新运行 `Publish IPFS Site`，必要时使用上一版可访问 CID 兜底。没有可靠 pin 的 CID 不应作为 ENS 或 IPNS 的生产目标。

eth.limo 异常但 IPNS 正常时，可以临时使用 Filebase 共享网关链接或备用域名：

```text
https://ipfs.filebase.io/ipns/k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud/
https://blog.victor42.work/
```

## 安全边界

可以公开记录：

```text
IPNS network key
CID
bucket 名
GitHub Secrets 名称
workflow 文件路径
公开 GitHub Actions run 链接
ENS owner 地址
```

不要公开记录：

```text
Filebase Access Key
Filebase Secret Key
4EVER Pin token
GitHub Secrets 具体值
钱包私钥 / seed phrase
任何可写 API token
```

## 参考入口

- ENS App：https://app.ens.domains/victor42.eth
- eth.limo：https://eth.limo/
- IPFS 网关（Filebase 共享）：https://ipfs.filebase.io/
- IPFS 项目站（非网关）：https://ipfs.tech/
- Filebase Console：https://console.filebase.com/
- 4EVERLAND Console：https://dashboard.4everland.org/
- GitHub Actions：https://github.com/greenzorro/victor42.eth/actions
