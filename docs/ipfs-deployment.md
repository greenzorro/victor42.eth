# victor42.eth 博客部署备忘录

> 最后更新：2026-06-04

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
→ 4EVER Pin
```

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
scripts/build_ipfs_car.sh
scripts/filebase_pin_car.py
scripts/filebase_update_ipns.py
scripts/filebase_retention.py
scripts/foureverland_client.py
scripts/foureverland_pin.py
scripts/foureverland_retention.py
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
托管 IPNS name
将 IPNS 指向 ROOT_CID
保留最近 20 个 release CAR
```

4EVER Pin：

```text
消费 GitHub Actions 生成的 ROOT_CID
pin 同一个 CID
作为第二 pin 服务提供内容冗余
只清理 workflow 自己创建的 pins
保留最近 20 个 workflow pins
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

验证 Filebase IPNS：

```bash
curl --noproxy '*' -I -L --max-time 80 \
  https://ipfs.io/ipns/k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud/
```

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

1. 看 GitHub Actions：`Publish IPFS Site` 是否成功。
2. 看 Filebase：IPNS name 是否指向最新 CID。
3. 看公共网关：`https://ipfs.io/ipfs/<CID>/` 是否可访问。
4. 看 IPNS：`https://ipfs.io/ipns/<network_key>/` 是否可解析。
5. 看 ENS / eth.limo：ENS contenthash 是否仍指向当前 Filebase IPNS。
6. 看 4EVER Pin：对应 CID 是否已被 pin；4EVER Pin 异常通常不影响主站即时访问。
7. 看 GitHub Pages：`Deploy to GitHub Pages` 是否成功；只影响备用域名。

## 应急原则

Filebase IPNS 异常但 CID 可访问时，可以临时把 ENS contenthash 改为：

```text
ipfs://<latest CID>
```

Filebase 内容不可取时，优先查看 4EVER Pin 是否已保存同一 CID，再重新运行 `Publish IPFS Site`，必要时使用上一版可访问 CID 兜底。

eth.limo 异常但 IPNS 正常时，可以临时使用公共网关链接或备用域名：

```text
https://ipfs.io/ipns/k51qzi5uqu5dmj5vlxt752kv8ptx9jb1j9hyrrplftwcrcb4l7u1ik7yw18hud/
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
- IPFS Gateway：https://ipfs.io/
- Filebase Console：https://console.filebase.com/
- 4EVERLAND Console：https://dashboard.4everland.org/
- GitHub Actions：https://github.com/greenzorro/victor42.eth/actions
