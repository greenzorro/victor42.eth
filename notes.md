# Victor42.eth 博客备忘录

## 1. 目的

本文档旨在详细记录 `projects/victor42.eth` 目录下的整个博客项目，为本项目的未来开发提供便利。

**重要提示：** 每次新增或修改功能后，请务必更新此备忘录，确保文档的准确性和时效性。

## 2. 项目概览

### 2.1 基本信息
- **GitHub**: https://github.com/greenzorro/victor42.eth
- **技术栈**: Hugo Extended 0.152.2 + Stack主题 v3.32.0

### 2.2 核心特性
- ✅ 自定义多语言实现（中文/英文）
- ✅ 自动SEO优化（Schema.org、OpenGraph、hreflang）
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
│   ├── partials/
│   └── _default/
├── scripts/                    # 项目脚本
├── static/                     # 静态资源
│   └── css/
├── config.toml                 # 站点配置
└── go.mod                      # Hugo Modules
```

### 4.2 关键文件说明

**配置**:
- `config.toml`: 站点主配置
- `go.mod`: Hugo Modules依赖
- `.github/workflows/`: GitHub Actions工作流配置
- `docs/ipfs-deployment.md`: 网站部署方案
- `scripts/`: 项目脚本

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

  <!-- 所有页面 -->
  {{ range .Site.Pages }}
  {{ if not .Params.sitemap_exclude }}
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
- 支持sitemap_exclude参数控制页面
- 动态priority计算
- 首页priority=1.0，其他页面默认0.5

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
baseURL = "https://victor42.eth.limo"  # 站点根地址
relativeURLs = true             # 使用相对URL
# 移除publishDir，使用默认的public目录
buildfuture = true              # 允许发布未来日期文章
```

**特点**:
- 使用相对URL提高资源路径可迁移性
- 使用默认 `public` 目录作为Hugo构建产物目录

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

#### 5.4.3 响应式设计
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
│   │       ├── lang-switcher.html  # 语言切换组件
│   │       └── related-content.html  # 关联内容组件
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
│   └── custom-override.css     # 5KB自定义样式+flexbox布局
├── icons/                      # SVG图标资源
└── robots.txt                  # 搜索引擎爬虫配置

assets/
└── scss/
    └── variables.scss          # Stack主题变量覆盖（主色调）
```

**自定义样式说明**:
- `static/css/custom-override.css` (5KB): Stack主题样式覆盖
- `assets/icons/`: SVG图标目录
- 主题资源通过Hugo Modules从Stack主题复制
