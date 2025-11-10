# Victor42.eth 博客备忘录

## 1. 目的

本文档旨在详细记录 `projects/victor42.eth` 目录下的整个博客项目，为本项目的未来开发提供便利。

**重要提示：** 每次新增或修改功能后，请务必更新此备忘录，确保文档的准确性和时效性。

## 2. 项目概览

### 2.1 基本信息
- **部署地址**: https://victor42.eth.limo
- **GitHub**: https://github.com/greenzorro/victor42.eth
- **技术栈**: Hugo Extended 0.152.2 + Stack主题 v3.16.0

### 2.2 核心特性
- ✅ 自定义多语言实现（中文/英文）
- ✅ 自动SEO优化（Schema.org、OpenGraph、hreflang）
- ✅ 中文字符阅读时间计算
- ✅ 关联推荐自动语言分离
- ✅ GitHub Actions自动部署
- ✅ 4EVERLAND IPFS部署 + ENS域名

---

## 3. 整体架构

### 3.1 部署架构

```
┌─────────────────┐
│   开发者推送     │  (main分支)
└────────┬────────┘
         │
         ▼
┌────────────────────────────────────────┐
│         GitHub Actions                  │
│  - Hugo Extended构建                    │
│  - 推送到gh-pages分支                   │
└────────┬─────────┬──────────────────────┘
         │         │
         ▼         ▼
┌────────────────┐ ┌──────────────────┐
│   gh-pages     │ │  GitHub Pages   │  (预览)
│  (静态文件)    │ │  https://...    │
└────────┬───────┘ └──────────────────┘
         │
         ▼
┌────────────────────────────────────────┐
│          4EVERLAND                     │
│  - IPFS部署                             │
│  - ENS域名绑定                          │
│  - victor42.eth.limo                  │
└────────────────────────────────────────┘
```

### 3.2 分支策略
- **main分支**: 源代码
- **gh-pages分支**: 构建产物，GitHub Actions自动更新

---

## 4. 文件结构

### 4.1 完整目录结构

```
victor42.eth/
├── .github/
│   └── workflows/
│       └── deploy.yml          # GitHub Actions工作流
├── assets/                     # Hugo资源（编译）
│   └── scss/
│       └── variables.scss      # Stack主题变量
├── content/                    # 内容
│   ├── post/                   # 中文文章
│   │   ├── 菜谱/
│   │   ├── 梦境与幻想/
│   │   └── ...
│   └── post-en/                # 英文文章
│       ├── 菜谱/
│       ├── 苟且与远方/
│       └── ...
├── layouts/                    # 模板
│   ├── partials/
│   └── _default/
├── static/                     # 静态资源
│   └── css/
├── config.toml                 # 站点配置
└── go.mod                      # Hugo Modules
```

### 4.2 关键文件说明

**配置**:
- `config.toml`: 站点主配置
- `go.mod`: Hugo Modules依赖
- `.github/workflows/deploy.yml`: CI/CD配置

**模板**:
- `layouts/partials/head/head.html`: 主页，SEO和hreflang
- `layouts/partials/article/components/details.html`: 文章详情
- `layouts/index.html`: 首页

**资源**:
- `assets/scss/variables.scss`: 主题变量
- `static/css/custom-override.css`: 样式覆盖

---

## 5. 技术实现

### 5.1 多语言系统

#### 5.1.1 实现方案
自定义多语言实现（非Hugo默认多语言）

**目录结构**:
```
content/
├── post/分类/文章.md          # 中文文章
└── post-en/分类/文章.md       # 英文文章
```

**URL结构**:
- 中文: `/post/[slug]/`
- 英文: `/post-en/[slug]/`

#### 5.1.2 关联机制
通过 `translationKey` 参数关联中英文版本：

```yaml
# 中文版本
---
title: 熟练优雅地吃鲫鱼
url: /post/3618
translationKey: 3618
---

# 英文版本
---
title: How to Eat Crucian Carp Like a Pro
url: /post-en/3618
translationKey: 3618
---
```

#### 5.1.3 hreflang自动生成
文件: `layouts/partials/head/head.html`

```html
{{ $translationKey := .Params.translationKey }}
{{ if $translationKey }}
    {{ $hasTranslation := false }}
    {{ range .Site.Pages }}
        {{ if and (eq .Params.translationKey $translationKey) (条件检查) }}
            {{ $hasTranslation = true }}
            {{ break }}
        {{ end }}
    {{ end }}
    {{ if $hasTranslation }}
        <!-- 生成hreflang标签 -->
    {{ end }}
{{ end }}
```

**特点**: 只有当翻译版本真实存在时才生成标签，避免404错误

#### 5.1.4 关联推荐语言分离
文件: `config.toml`

```toml
[related]
  includeNewer = true
  threshold = 80
  toLower = true

  [[related.indices]]
  name = "section"      # 目录/章节
  weight = 80           # 最高权重

  [[related.indices]]
  name = "categories"   # 分类
  weight = 40           # 较低权重
```

**工作原理**:
- Hugo Related算法按权重匹配
- `section` 区分 `content/post/` 与 `content/post-en/`
- 中文文章只推荐中文，英文文章只推荐英文
- 无需自定义过滤逻辑

### 5.2 SEO优化

#### 5.2.1 Schema.org结构化数据
文件: `layouts/partials/head/schema.html`

```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "{{ .Title }}",
  "description": "{{ .Description }}",
  "author": {
    "@type": "Person",
    "name": "{{ .Site.Params.author }}"
  },
  "datePublished": "{{ .Date }}",
  "dateModified": "{{ .Lastmod }}",
  "wordCount": {{ partial "helper/word-count" . }},
  "timeRequired": "{{ partial "helper/reading-time" . }}"
}
</script>
```

#### 5.2.2 OpenGraph标签
文件: `layouts/partials/head/opengraph.html`

包含完整的社交媒体分享元数据：
- `og:url`, `og:site_name`, `og:type`
- `article:section`, `article:published_time`
- `article:author` (自定义修复)

#### 5.2.3 Sitemap配置
文件: `layouts/_default/sitemap.xml`

```xml
<url>
  <loc>{{ .Permalink }}</loc>
  <lastmod>{{ .Lastmod.Format "2006-01-02T15:04:05-07:00" }}</lastmod>
  <changefreq>weekly</changefreq>
  <priority>{{ if eq .Kind "home" }}1.0{{ else }}0.5{{ end }}</priority>
</url>
```

特点: 单一sitemap文件，包含所有页面类型

### 5.3 资源策略

#### 5.3.1 图片CDN配置
**CDN域名**: `https://cdn.victor42.work/`

**使用方式**:
- 在文章front matter中直接使用完整CDN URL
- 不依赖Hugo本地图片处理管道
- 所有图片资源独立管理

**优势**:
- 减轻Hugo构建负担
- 统一的CDN加速
- 便于图片管理和备份

#### 5.3.2 平台无关配置
文件: `config.toml`

```toml
baseURL = ""                    # 空URL，支持多平台部署
relativeURLs = true             # 使用相对URL
canonifyURLs = true             # 规范URL处理
publishDir = "publish"          # 自定义发布目录
buildfuture = true              # 允许发布未来日期文章
```

**特点**:
- 静态文件可在任意平台部署
- 避免平台特定的URL依赖
- 灵活切换部署方式

### 5.4 自定义功能

#### 5.4.1 中文字符阅读时间计算
问题: Hugo内置`.ReadingTime`对中文字符计算不准确

解决: 自定义helper函数

**文件**:
- `layouts/partials/helper/word-count.html` - 字符统计
- `layouts/partials/helper/reading-time.html` - 时间计算
- `layouts/partials/article/components/details.html` - 显示组件

**算法**:
```go
{{ $wordCount := partial "helper/word-count" . }}
{{ $readingTime := div $wordCount 200 }}  // 200字/分钟
```

**特点**:
- 中文字符 + 英文单词混合统计
- 自定义阅读速度（200字/分钟）
- 集成到Schema.org结构化数据

#### 5.4.2 Stack主题定制

**Hugo Modules配置**:
```go
// go.mod
module github.com/greenzorro/victor42.eth

go 1.18

require github.com/CaiJimmy/hugo-theme-stack/v3 v3.16.0
```

**config.toml**:
```toml
[module]
  [module.imports]
    path = "github.com/CaiJimmy/hugo-theme-stack/v3"
```

**版本选择**:
- Hugo: 0.152.2 Extended
- Stack: v3.16.0 (兼容Hugo 0.152.2)
- Go: 1.18+

**自定义样式**:
- 主色调: cola青绿色 (#2A9D8F)
- 文件: `assets/scss/variables.scss`
- CSS覆盖: `static/css/custom-override.css`

#### 5.4.3 响应式设计
移动端优化:
- 汉堡菜单深色模式切换按钮显示
- 嵌套菜单CSS规则覆盖
- 三列布局（宽屏）vs 单列（移动端）

### 5.5 CI/CD

#### 5.5.1 GitHub Actions工作流
文件: `.github/workflows/deploy.yml`

**核心流程**:
```yaml
1. 检出代码 (actions/checkout@v4)
2. 设置Hugo Extended (peaceiris/actions-hugo@v2)
3. 设置Node.js 18 (actions/setup-node@v4)
4. 安装Stack主题依赖 (npm ci)
5. 执行构建 (hugo --gc --minify)
6. 推送到gh-pages (peaceiris/actions-gh-pages@v3)
```

**权限配置**:
```yaml
permissions:
  contents: write       # 推送到gh-pages
  pull-requests: write  # PR评论
  statuses: write       # 更新commit状态
  pages: write          # GitHub Pages
```

---

## 6. 核心配置

### 6.1 config.toml 关键配置

```toml
# 基础配置
baseURL = ""                    # 空URL，支持多平台部署
relativeURLs = true             # 使用相对URL
languageCode = 'en-us'
defaultContentLanguage = "zh-cn"
hasCJKLanguage = true           # 支持中文

# 主题模块
[module]
  [module.imports]
    path = "github.com/CaiJimmy/hugo-theme-stack/v3"

# Related算法
[related]
  includeNewer = true
  threshold = 80
  toLower = true

  [[related.indices]]
  name = "section"
  weight = 80

  [[related.indices]]
  name = "categories"
  weight = 40

  [[related.indices]]
  name = "date"
  weight = 20

# 页脚
[params.footer]
  since = 2011

# 右边栏Widgets
[params.widgets]
  homepage = [
    { type = "archives", params = { limit = 5 } }
  ]
  page = [
    { type = "toc" }
  ]

# Google Analytics
GoogleAnalytics = "G-H0F3NJJ4RT"
```

### 6.2 go.mod 依赖

```go
module github.com/greenzorro/victor42.eth

go 1.18

require github.com/CaiJimmy/hugo-theme-stack/v3 v3.16.0
```

### 6.3 自定义模板文件清单

```
layouts/
├── partials/
│   ├── head/
│   │   ├── head.html           # 主页，hreflang实现
│   │   ├── schema.html         # Schema.org结构化数据
│   │   ├── analytics.html      # Google Analytics
│   │   ├── opengraph.html      # OpenGraph标签
│   │   ├── twitter.html        # Twitter Card
│   │   └── custom.html         # 自定义CSS加载
│   ├── helper/
│   │   ├── word-count.html     # 中文字符统计
│   │   └── reading-time.html   # 阅读时间计算
│   ├── article/
│   │   └── components/
│   │       └── details.html    # 双语切换+flexbox
│   ├── sidebar/
│   │   └── left.html           # 菜单去重
│   └── data/
│       ├── title.html          # 自定义标题
│       └── description.html    # 自定义描述
├── index.html                   # 首页，包含页脚和右边栏
└── _default/
    └── sitemap.xml             # 单sitemap文件
```

### 6.4 静态资源文件

```
static/
├── css/
│   └── custom-override.css     # 自定义样式+flexbox布局
└── robots.txt                  # 搜索引擎爬虫配置

assets/
└── scss/
    └── variables.scss          # Stack主题变量覆盖（主色调）
```

---

## 7. 部署方案

### 7.1 4EVERLAND配置

**项目创建**:
1. 选择 "Static Web Hosting"
2. 框架: Hugo (或其他)
3. 连接到GitHub
4. 仓库: `greenzorro/victor42.eth`
5. 分支: `gh-pages`
6. 根目录: `/` (gh-pages根目录)
7. 构建命令: 空（已构建）
8. 发布目录: 空（gh-pages就是发布目录）

**域名绑定**:
- ENS域名: `victor42.eth.limo`
- 绑定方式: Decentralized Domains → ENS
- 成本: ~$0.3 (MetaMask交易)

**特点**:
- 自动从GitHub获取构建产物
- IPFS pinning
- CDN加速
- SSL证书
- IPNS自动更新

### 7.2 部署流程

```
开发者push → GitHub Actions → gh-pages更新 → 4EVERLAND自动部署 → victor42.eth.limo
```

**时间线**:
- GitHub Actions: ~2分钟
- 4EVERLAND: 3-5分钟
- 总计: < 10分钟

### 7.3 多平台支持

**当前**: 4EVERLAND (生产)
**备选**:
- GitHub Pages: `greenzorro.github.io/victor42.eth`
- Netlify / Vercel (支持静态文件部署)

**优势**: 平台无关，静态文件可部署到任何平台
