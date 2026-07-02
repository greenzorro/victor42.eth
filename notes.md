# Victor42.eth 博客备忘录

## 1. 目的

本文档旨在详细记录 `projects/victor42.eth` 目录下的整个博客项目，为本项目的未来开发提供便利。

## 2. 项目概览

### 2.1 基本信息
- **GitHub**: https://github.com/greenzorro/victor42.eth
- **技术栈**: Hugo Extended 0.152.2 + Stack主题 v3.32.0

### 2.2 核心特性
- ✅ 自定义多语言实现（中文/英文）
- ✅ 自动SEO优化（Schema.org、OpenGraph、hreflang、sitemap、image sitemap）
- ✅ 分类与标签体系（categories + tags）
- ✅ 中文字符阅读时间计算
- ✅ 关联推荐自动语言分离

---

## 3. 整体架构

### 3.1 部署说明

网站部署方案见 `docs/ipfs-deployment.md`。

---

## 4. 文件结构

### 4.1 完整目录结构

```
victor42.eth/
├── .github/
│   └── workflows/
│       ├── deploy-github-pages.yml # GitHub Actions工作流配置
│       └── publish-ipfs.yml        # GitHub Actions工作流配置
├── assets/                     # Hugo资源（编译）
│   ├── icons/
│   └── scss/
│       └── variables.scss      # Stack主题变量
├── content/                    # 内容
│   ├── post/                   # 中文文章
│   │   ├── 苟且与远方/
│   │   ├── 梦境与幻想/
│   │   └── ...
│   └── post-en/                # 英文文章
│       ├── 苟且与远方/
│       └── ...
├── docs/                       # 项目文档
│   └── ipfs-deployment.md      # 网站部署方案
├── i18n/                       # 国际化文案
├── layouts/                    # 模板
│   ├── _default/
│   ├── page/
│   ├── partials/
│   ├── index.html
│   ├── index.imagesitemap.xml
│   └── index.sitemap.xml
├── scripts/                    # 项目脚本
├── static/                     # 静态资源
│   ├── css/
│   ├── favicon.ico
│   └── robots.txt
├── config.toml                 # 站点配置
├── .gitignore                  # Git忽略规则
└── go.mod                      # Hugo Modules
```

### 4.2 关键文件说明

**配置**:
- `config.toml`: 站点主配置
- `go.mod`: Hugo Modules依赖
- `.gitignore`: 忽略 Hugo 构建产物与本地生成文件
- `.github/workflows/`: GitHub Actions工作流配置
- `docs/ipfs-deployment.md`: 网站部署方案
- `scripts/`: 项目脚本

**模板**:
- `layouts/partials/head/head.html`: 页面 head、SEO和hreflang
- `layouts/partials/article/components/details.html`: 文章详情
- `layouts/partials/article/components/footer.html`: 文章页脚
- `layouts/index.html`: 首页
- `layouts/index.imagesitemap.xml`: 图片sitemap

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

### 5.2 内容组织

#### 5.2.1 分类与标签

文件: `config.toml`

```toml
[taxonomies]
category = "categories"
tag = "tags"
```

**职责边界**:
- `categories` 是一级内容分类，沿用 `苟且与远方-Life`、`折腾与思考-Geek`、`设计译文-Design` 等长期栏目。
- `tags` 是跨栏目主题索引，用于目的地、旅行方式、技术主题、设计主题等细粒度聚合。
- Stack主题自带 tags 展示和 taxonomy 列表能力；文章写入 `tags` 后会生成 `/tags/<tag>/` 页面。

**文章写法**:
```yaml
categories: 苟且与远方-Life
tags: ["舟山", "朱家尖", "亲子旅行", "自驾游", "海岛旅行", "浙江旅行"]
```

### 5.3 SEO优化

#### 5.3.1 Schema.org结构化数据
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

#### 5.3.2 OpenGraph标签
文件: `layouts/partials/head/opengraph.html`

包含完整的社交媒体分享元数据：
- `og:url`, `og:site_name`, `og:type`
- `article:section`, `article:published_time`
- `article:author` (自定义修复)

#### 5.3.3 Sitemap配置
文件: `layouts/_default/sitemap.xml`

```xml
{{ printf "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>" | safeHTML }}
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <!-- 首页 -->
  <url>
    <loc>{{ .Site.BaseURL }}</loc>
    {{ if not .Lastmod.IsZero }}
    <lastmod>{{ safeHTML ( .Lastmod.Format "2006-01-02T15:04:05-07:00" ) }}</lastmod>
    {{ end }}
    <changefreq>daily</changefreq>
    <priority>1.0</priority>
  </url>

  <!-- 所有页面，包括常规页面、单页和分类页面 -->
  {{ range .Site.Pages }}
  {{ if and (not .IsHome) (not .Params.sitemap_exclude) }}
  <url>
    <loc>{{ .Permalink }}</loc>
    {{ if not .Lastmod.IsZero }}
    <lastmod>{{ safeHTML ( .Lastmod.Format "2006-01-02T15:04:05-07:00" ) }}</lastmod>
    {{ end }}
    <changefreq>{{ if .Sitemap.ChangeFreq }}{{ .Sitemap.ChangeFreq }}{{ else }}weekly{{ end }}</changefreq>
    {{ $priority := "0.5" }}
    {{ if .Sitemap.Priority }}
      {{ if and (ge .Sitemap.Priority 0.0) (le .Sitemap.Priority 1.0) }}
        {{ $priority = .Sitemap.Priority }}
      {{ end }}
    {{ end }}
    <priority>{{ $priority }}</priority>
  </url>
  {{ end }}
  {{ end }}
</urlset>
```

特点:
- 单一sitemap文件，包含所有页面类型
- 自定义多语言通过 `/post/` 与 `/post-en/` 目录区分，中英文URL混合收录在同一个 `sitemap.xml`
- 支持sitemap_exclude参数控制页面
- 动态priority计算
- 首页priority=1.0，其他页面默认0.5

#### 5.3.4 Image Sitemap配置

文件: `layouts/index.imagesitemap.xml`

`image-sitemap.xml` 是独立的图片sitemap，由 Hugo 构建时自动生成。它覆盖 `post` 和 `post-en` 两个文章区，收录：

- 文章 front matter 的 `image`
- 正文渲染后的 `<img>` 图片
- 图片 alt 文本作为 `image:caption`
- 同一页面内重复图片自动去重

文件: `static/robots.txt`

```text
Sitemap: https://victor42.eth.limo/sitemap.xml
Sitemap: https://victor42.eth.limo/image-sitemap.xml
```

### 5.4 资源策略

#### 5.4.1 图片CDN配置
**CDN域名**: `https://cdn.victor42.work/`

**使用方式**:
- 在文章front matter中直接使用完整CDN URL
- 不依赖Hugo本地图片处理管道
- 所有图片资源独立管理

**优势**:
- 减轻Hugo构建负担
- 统一的CDN加速
- 便于图片管理和备份

#### 5.4.2 平台无关配置
文件: `config.toml`

```toml
baseURL = "https://victor42.eth.limo"  # 站点根地址
relativeURLs = true             # 使用相对URL
buildfuture = true              # 允许发布未来日期文章
```

**特点**:
- 使用相对URL提高资源路径可迁移性
- 使用默认 `public` 目录作为Hugo构建产物目录
- `public/`、`resources/`、`dist/` 是构建产物，不提交到仓库

### 5.5 自定义功能

#### 5.5.1 中文字符阅读时间计算
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

#### 5.5.2 Stack主题定制

**Hugo Modules配置**:
```go
// go.mod
module github.com/greenzorro/victor42.eth

go 1.18

require github.com/CaiJimmy/hugo-theme-stack/v3 v3.32.0
```

**config.toml**:
```toml
[module]
  [module.imports]
    path = "github.com/CaiJimmy/hugo-theme-stack/v3"
```

**版本选择**:
- Hugo: 0.152.2 Extended
- Stack: v3.32.0 (兼容Hugo 0.152.2)
- Go: 1.18+

**自定义样式**:
- 主色调: cola青绿色 (#2A9D8F)
- 文件: `assets/scss/variables.scss`
- CSS覆盖: `static/css/custom-override.css`

#### 5.5.3 文章页脚

文件: `layouts/partials/article/components/footer.html`

文章页脚只有在存在可展示内容时才输出。判断条件：

- 文章存在 tags
- 文章启用 license
- 文章 `Lastmod` 与 `Date` 不同

文件: `static/css/custom-override.css`

`article-footer` 上方有分隔线和上间距；无页脚内容的文章不会输出 `article-footer`，因此不会出现空分隔线。

#### 5.5.4 响应式设计
移动端优化:
- 汉堡菜单深色模式切换按钮显示
- 嵌套菜单CSS规则覆盖
- 三列布局（宽屏）vs 单列（移动端）

## 6. 核心配置

### 6.1 config.toml 关键配置

```toml
# 基础配置
baseURL = "https://victor42.eth.limo"  # 站点根地址
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

# 分类法
[taxonomies]
category = "categories"
tag = "tags"

# 输出格式
[outputs]
  home = ["HTML", "RSS", "Sitemap", "ImageSitemap"]
  section = ["HTML", "RSS"]
  taxonomy = ["HTML", "RSS"]
  term = ["HTML", "RSS"]

[outputFormats]
  [outputFormats.Sitemap]
    mediaType = "application/xml"
    baseName = "sitemap"
    isHTML = false

  [outputFormats.ImageSitemap]
    mediaType = "application/xml"
    baseName = "image-sitemap"
    isHTML = false
    notAlternative = true

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

require github.com/CaiJimmy/hugo-theme-stack/v3 v3.32.0
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
│   │   ├── reading-time.html   # 阅读时间计算
│   │   ├── icon.html           # 图标组件
│   │   └── hugo-reading-time-override.html  # Hugo阅读时间覆盖
│   ├── article/
│   │   └── components/
│   │       ├── details.html    # 文章详情
│   │       ├── footer.html     # 文章页脚条件渲染
│   │       ├── lang-switcher.html  # 语言切换组件
│   │       └── related-content.html  # 关联内容组件
│   ├── sidebar/
│   │   └── left.html           # 菜单去重
│   └── data/
│       ├── title.html          # 自定义标题
│       └── description.html    # 自定义描述
├── index.html                   # 首页，包含页脚和右边栏
├── index.imagesitemap.xml       # 图片sitemap
├── index.sitemap.xml            # 首页sitemap输出
└── _default/
    └── sitemap.xml             # 单sitemap文件
```

### 6.4 静态资源文件

```
static/
├── css/
│   └── custom-override.css     # 自定义样式、语言切换、标签、文章页脚
├── favicon.ico                 # 站点图标
└── robots.txt                  # 搜索引擎爬虫配置

assets/
├── icons/                      # SVG图标资源
└── scss/
    └── variables.scss          # Stack主题变量覆盖（主色调）
```

**自定义样式说明**:
- `static/css/custom-override.css`: Stack主题样式覆盖
- `assets/icons/`: SVG图标目录
- 主题资源通过Hugo Modules从Stack主题复制
