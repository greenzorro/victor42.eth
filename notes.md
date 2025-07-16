# Hugo 站点配置备忘录

## 1. 目的

本文档旨在详细记录 `projects/victor42.eth` 目录下的整个博客项目，为本项目的未来开发提供便利。

**重要提示：** 每次新增或修改功能后，请务必更新此备忘录，确保文档的准确性和时效性。

## 2. Sitemap 配置

### 2.1 问题描述
多语言站点默认生成多个sitemap文件和一个sitemap索引，但我们希望所有内容都在一个sitemap中呈现。

### 2.2 配置修改
在`config.toml`中添加以下配置：

```toml
# Sitemap配置
[sitemap]
  changefreq = "weekly"
  filename = "sitemap.xml"
  priority = 0.5

# 禁用多语言sitemap索引
enableGitInfo = true

# 确保只生成一个sitemap
[params.sitemap]
  disable_multilingual = true

[outputs]
  home = ["HTML", "RSS", "Sitemap"]
  section = ["HTML", "RSS"]
  taxonomy = ["HTML", "RSS"]
  term = ["HTML", "RSS"]

[outputFormats]
  [outputFormats.Sitemap]
    mediaType = "application/xml"
    baseName = "sitemap"
    isHTML = false
```

### 2.3 自定义模板
创建以下自定义模板文件：

#### layouts/_default/sitemap.xml
自定义sitemap模板，实现以下功能：
- 添加首页条目
- 使用 `.Site.Pages` 包含所有页面类型
- 处理priority值的有效性
- 支持通过前置元数据排除特定页面

#### layouts/_default/sitemapindex.xml
生成单一的sitemap索引，指向主sitemap文件。

#### layouts/index.sitemap.xml
备用的sitemap生成模板，与 `_default/sitemap.xml` 功能类似。

具体实现可参考对应目录下的模板文件。

### 2.4 Sitemap生成优化

#### 问题背景
- 原始sitemap模板仅包含文章页面
- 首页和其他页面（如单页、分类页）未被包含在sitemap中
- Google Search Console报告了sitemap中的priority标签值问题

#### 模板修改要点

1. **首页处理**
   - 在sitemap中明确添加首页条目
   - 设置首页优先级为1.0
   - 设置首页更新频率为daily

2. **页面范围扩展**
   - 使用 `.Site.Pages` 替代原有的页面过滤逻辑
   - 包含所有类型的页面：
     * 首页
     * 文章页面
     * 单页（pages）
     * 分类页面
     * 标签页面
     * 列表页面（section）

3. **Priority值安全处理**
   - 添加priority值的有效性检查
   - 确保priority值始终在0.0到1.0之间
   - 默认priority值为0.5
   - 支持通过前置元数据自定义priority

#### 最佳实践

1. 使用 `sitemap_exclude: true` 可以排除不希望出现在sitemap中的页面
2. 可以根据页面类型自定义priority值，例如：
   ```go
   {{ $priority := "0.5" }}
   {{ if eq .Kind "home" }}
     {{ $priority = "1.0" }}
   {{ else if eq .Kind "page" }}
     {{ $priority = "0.8" }}
   {{ else if eq .Kind "section" }}
     {{ $priority = "0.6" }}
   {{ else if eq .Kind "taxonomy" }}
     {{ $priority = "0.4" }}
   {{ end }}
   ```

#### 注意事项

- 修改sitemap模板后，需要重新构建站点
- 建议使用 `hugo --cleanDestinationDir` 清理缓存
- 在Google Search Console中重新提交sitemap
- 定期检查sitemap生成是否符合预期

## 3. 多语言实现分析

### 3.1 目录结构与URL设计
本站使用了自定义的多语言实现方式，具有以下特点：

1. **目录结构**：
   - 中文内容：`content/post/[分类]/[文章].md`
   - 英文内容：`content/post-en/[分类]/[文章].md`

2. **URL结构**：
   - 中文文章URL: `/post/[slug]/`
   - 英文文章URL: `/post/en/[slug]/`

3. **关联机制**：
   - 通过`translationKey`参数关联不同语言版本的内容
   - 文件名可以相同，但URL和目录结构不同

### 3.2 前置元数据配置
文章通过前置元数据中的`url`和`translationKey`参数实现多语言关联：

中文版本（位于`content/post/[分类]/`目录）：
```yaml
---
title: 文章标题
description: 文章描述
date: 2025-01-27 12:15:00
categories: 分类名称
url: /post/article-slug
translationKey: article-slug
---
```

英文版本（位于`content/post-en/[分类]/`目录）：
```yaml
---
title: Article Title
description: Article description
date: 2025-01-27 12:15:00
categories: 分类名称
url: /post/en/article-slug
translationKey: article-slug
---
```

### 3.3 多语言链接关系
在`themes/stack/layouts/partials/head/head.html`中实现了多语言版本链接关系：

主要功能：
- 识别当前页面的语言（中文或英文）
- 自动生成对应的`hreflang`标签
- 为搜索引擎提供不同语言版本的对应关系
- 支持x-default语言标记

实现方式：
- 基于`translationKey`参数查找对应的翻译版本
- 只有当翻译版本真实存在时才生成hreflang标签
- **当前页面是英文版本时**：查找同样`translationKey`的中文版本（不在`/post/en/`路径）
- **当前页面是中文版本时**：查找同样`translationKey`的英文版本（在`/post/en/`路径）
- 确保每个页面都有正确的语言版本链接，避免404错误

### 3.4 与Hugo默认多语言机制的区别
本站的多语言实现与Hugo默认的多语言机制有以下区别：

1. **目录组织**：
   - Hugo默认：同一目录下，通过文件名前缀或子目录区分语言
   - 本站：完全独立的目录结构（post vs post-en）

2. **URL生成**：
   - Hugo默认：自动在URL中添加语言代码前缀（如`/en/post/...`）
   - 本站：通过前置元数据中的`url`参数手动控制URL结构

3. **内容关联**：
   - Hugo默认：通过文件名和目录结构自动关联
   - 本站：通过`translationKey`参数手动关联

4. **灵活性**：
   - 本站方案提供了更大的灵活性，可以为不同语言版本设计完全不同的URL结构
   - 便于SEO优化和用户体验定制

## 4. 内容组织与分类系统

### 4.1 分类目录结构
本站使用了自定义的分类目录结构，而非Hugo默认的taxonomies：

1. **物理目录结构**：
   - 按主题分类：`content/post/[分类名称]/`
   - 英文内容同样按主题分类：`content/post-en/[分类名称]/`

2. **分类参数**：
   - 使用`categories`前置参数指定文章分类
   - 分类名称可以包含子分类，如`折腾与思考-Geek`

3. **与默认taxonomies的区别**：
   - Hugo默认使用`taxonomies`配置定义分类系统
   - 本站在物理目录结构上也体现了分类，增强了内容组织的直观性

### 4.2 自定义URL结构
本站对内容URL进行了自定义，不使用Hugo默认的URL生成规则：

1. **文章URL**：
   - 通过前置元数据中的`url`参数手动指定
   - 格式为`/post/[slug]/`或`/post/en/[slug]/`
   - 不包含分类信息，保持URL简洁

2. **分类页URL**：
   - 使用默认的`/categories/[category-name]/`格式
   - 支持中英文分类页面

## 5. SEO优化分析

### 5.1 基础SEO元素
站点使用了以下SEO基础元素：

- 标题和描述：通过`partialCached "data/title"`和`partialCached "data/description"`生成
- 规范链接：`<link rel='canonical' href='{{ .Permalink }}'>`
- 多语言标记：通过`hreflang`属性实现

### 5.2 Open Graph协议支持
站点实现了完整的Open Graph协议支持，便于社交媒体分享：

- 基本属性：标题、描述、URL、站点名称、类型
- 文章特定属性：发布时间、修改时间、分类、标签
- 图片支持：通过`helper/image`部分实现

### 5.3 结构化数据
在`head/schema.html`中实现了结构化数据，帮助搜索引擎更好地理解内容。

### 5.4 图片处理与CDN
本站对图片处理有特殊处理：

1. **CDN使用**：
   - 图片URL使用CDN域名：`https://cdn.victor42.work/`
   - 在前置元数据中直接指定完整图片URL

2. **与Hugo默认图片处理的区别**：
   - Hugo默认使用本地图片和图片处理管道
   - 本站使用外部CDN，不依赖Hugo的图片处理功能

## 6. 主题定制与扩展

### 6.1 Stack主题定制
本站基于Stack主题进行了多处定制：

1. **头部模板修改**：
   - 修改了`head.html`添加多语言支持
   - 自定义了SEO相关元标签

2. **布局定制**：
   - 可能修改了文章列表和文章页面布局
   - 添加了自定义的页面组件

### 6.2 静态资源处理
本站对静态资源处理有特殊配置：

1. **相对URL**：
   - 启用了`relativeURLs = true`
   - 启用了`canonifyURLs = true`

2. **构建配置**：
   - 使用自定义发布目录：`publishDir = "publish"`
   - 启用了`buildfuture = true`允许发布未来日期的文章

## 7. 注意事项与最佳实践

### 7.1 多语言内容管理
- 使用`translationKey`关联不同语言版本的内容
- 保持目录结构一致性（post对应post-en）
- 确保`hreflang`标签正确设置
- 在创建新内容时，站长会选择性地为部分新内容创建对应的翻译版本

### 7.2 URL结构维护
- 保持URL结构一致性（中文`/post/slug/`，英文`/post/en/slug/`）
- 使用有意义的slug，便于SEO和用户记忆
- 避免更改已发布内容的URL，如需更改应设置301重定向

### 7.3 Sitemap维护
- 使用`hugo --cleanDestinationDir`清理缓存后重新构建
- 定期检查sitemap.xml是否正确生成
- 可以通过`sitemap_exclude: true`前置参数排除特定页面

### 7.4 SEO优化建议
- 确保每篇文章都有唯一的标题和描述
- 使用有意义的URL结构
- 提供高质量的特色图片
- 保持内容更新，利用`lastmod`属性

### 7.5 主题升级注意事项
- 升级Stack主题时注意保留自定义修改
- 特别关注`head.html`和多语言相关模板
- 使用版本控制跟踪主题修改，便于合并更新

## 8. hreflang标签修复记录

### 8.1 问题描述
**发现时间**: 2025-01-27

**问题现象**:
- 原始的hreflang标签生成逻辑假设每篇文章都有对应的翻译版本
- 使用简单的URL替换来生成对应语言的链接
- 对于只有单语言版本的文章，会生成指向不存在页面的hreflang链接
- 可能导致SEO问题和404错误

**具体问题**:
```html
<!-- 原始逻辑 - 有问题 -->
{{ $zhURL := replaceRE "/post/en/([^/]+)/" "/post/$1/" $currentURL }}
{{ $enURL := replaceRE "/post/([^/]+)/" "/post/en/$1/" $currentURL }}
```

### 8.2 修复方案
**修复思路**:
1. 基于`translationKey`参数而非URL模式来查找翻译版本
2. 遍历所有页面验证翻译版本是否真实存在
3. 只有当翻译版本存在时才生成hreflang标签

**修复实现**:
```html
<!-- 修复后的逻辑 -->
{{ $translationKey := .Params.translationKey }}
{{ if $translationKey }}
    {{ $hasTranslation := false }}
    {{ $translationURL := "" }}
    
    {{ range .Site.Pages }}
        {{ if and (eq .Params.translationKey $translationKey) (不同语言路径条件) }}
            {{ $hasTranslation = true }}
            {{ $translationURL = .Permalink }}
            {{ break }}
        {{ end }}
    {{ end }}
    
    {{ if $hasTranslation }}
        <!-- 生成hreflang标签 -->
    {{ end }}
{{ end }}
```

### 8.3 修复效果
**修复前**:
- 为不存在的翻译版本生成hreflang链接
- 搜索引擎可能访问到404页面
- SEO表现受到影响

**修复后**:
- 只为真实存在的翻译版本生成hreflang标签
- 避免404错误
- 改善SEO表现
- 对于像"灵感库的故事"这样只有中文版本的文章，不会生成英文版本的hreflang链接

### 8.4 验证方法
1. 检查有翻译版本的文章：hreflang标签正常生成
2. 检查只有单语言版本的文章：不生成指向不存在页面的hreflang标签
3. 验证生成的URL都能正常访问
4. 在Google Search Console中检查是否还有hreflang相关错误

## 9. 故障排查

如遇问题，可尝试以下方法：
- 检查模板语法错误
- 查看Hugo构建日志
- 清理缓存后重新构建
- 验证自定义模板是否被正确加载
- 检查`translationKey`是否正确设置
- 验证URL结构是否符合预期
- **hreflang相关问题**: 检查翻译版本是否真实存在，验证`translationKey`参数是否正确配置