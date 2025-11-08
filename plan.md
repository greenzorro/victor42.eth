# Victor42.eth 博客 GitHub Actions + 4EVERLAND 自动部署方案

---

## ⚠️ 架构更新 (2025-11-08)

**重要变更**: GitHub Actions与4EVERLAND已完全解耦！

- ✅ **GitHub Actions**: 仅负责Hugo构建，上传Artifact
- ✅ **4EVERLAND**: 自动从GitHub获取构建产物并部署
- ✅ **平台无关**: 静态文件可部署到任何平台

**当前状态**: 工作流已更新并推送，参考实际工作流文件: `.github/workflows/deploy.yml`

---

## 1. 项目概述

### 1.1 当前状态
- **仓库**: `greenzorro/victor42.eth`
- **当前部署**: fleek.xyz → IPFS → victor42.eth.limo
- **目标部署**: 4EVERLAND → IPFS → victor42.eth.limo
- **内容规模**: 82篇中文 + 419篇英文 = 501篇文章
- **技术栈**: Hugo Extended + Stack主题 + 自定义多语言

### 1.2 特殊配置
- **多语言实现**: 自定义 (非Hugo默认)
  - 中文: `content/post/分类/文章.md`
  - 英文: `content/post-en/分类/文章.md`
  - 通过 `translationKey` 关联
- **图片策略**: CDN存储 `https://cdn.victor42.work/`
- **发布目录**: `publish/` (非默认 `public/`)
- **主题**: Stack (Git Submodule)
- **主题依赖**: SCSS + TypeScript (需要Node.js构建)

### 1.3 之前尝试失败的原因 (推测)
根据git历史，之前的 `.github/workflows/deploy.yml` 可能在以下环节出现问题：
- 未安装Stack主题的Node依赖
- Hugo Extended版本未正确配置
- 4EVERLAND集成方式不明确
- 缺少必要的错误处理和日志

---

## 2. 架构决策: 方案A (解耦方案)

### 2.1 总体架构
```
GitHub Repo → GitHub Actions (Build) → Artifact → 4EVERLAND (Auto Deploy) → IPFS → ENS Domain
```

### 2.2 职责分工
- **GitHub Actions 负责**:
  - 代码检出
  - Node.js环境准备
  - Stack主题依赖安装
  - Hugo Extended构建
  - 产物质量验证
  - 上传构建产物 (Artifact)
  - **不涉及任何部署平台**

- **4EVERLAND 负责**:
  - 从GitHub自动拉取构建产物
  - IPFS pinning
  - CDN加速
  - SSL证书
  - ENS域名绑定
  - IPNS自动更新
  - 构建历史管理

### 2.3 为什么选择方案A (解耦)
1. ✅ **完整保留Stack主题功能** (SCSS/TS编译)
2. ✅ **4EVERLAND专注IPFS部署** (其强项)
3. ✅ **GitHub Actions灵活可控** (可添加测试、验证等)
4. ✅ **故障排除更易** (分离关注点)
5. ✅ **平台无关** (可切换到fleek/Netlify/Vercel)
6. ✅ **GitHub无需部署平台密钥** (更安全)
7. ✅ **符合最佳实践** (单一职责原则)
8. ✅ **未来可扩展** (支持复杂构建流程)

---

## 3. GitHub Actions 详细配置

### 3.1 工作流文件: `.github/workflows/deploy.yml`

```yaml
name: Build Hugo Site

# 触发条件
on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

# 权限配置
permissions:
  contents: read
  pull-requests: write

# 环境变量
env:
  HUGO_VERSION: '0.111.3'
  HUGO_EXTENDED: true
  NODE_VERSION: '18'

# 任务定义
jobs:
  # 构建任务
  build:
    name: Build Site
    runs-on: ubuntu-latest

    steps:
      # 步骤1: 检出代码
      - name: Checkout
        uses: actions/checkout@v4
        with:
          submodules: true          # 拉取Stack主题
          fetch-depth: 0            # 获取全部历史 (用于GitInfo)

      # 步骤2: 设置Hugo
      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: ${{ env.HUGO_VERSION }}
          extended: ${{ env.HUGO_EXTENDED }}

      # 步骤3: 设置Node.js
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: 'npm'              # 缓存npm依赖
          cache-dependency-path: |
            themes/stack/package-lock.json
            package-lock.json

      # 步骤4: 安装Stack主题依赖 ⭐ 关键步骤
      - name: Install Stack Theme Dependencies
        run: |
          echo "🔍 检查Stack主题是否有package.json..."
          if [ -f "themes/stack/package.json" ]; then
            echo "✅ 发现package.json，开始安装依赖..."
            cd themes/stack
            npm ci --silent
            echo "✅ 主题依赖安装完成"
            cd ../..
          else
            echo "ℹ️  Stack主题无package.json，跳过依赖安装"
          fi

      # 步骤5: 验证构建环境
      - name: Verify Build Environment
        run: |
          echo "🔍 环境验证..."
          echo "Hugo版本: $(hugo version)"
          echo "Node版本: $(node --version)"
          echo "npm版本: $(npm --version)"
          echo "主题目录: $(ls -la themes/stack/)"
          echo "主题assets: $(ls -la themes/stack/assets/ 2>/dev/null || echo '无assets目录')"

      # 步骤6: 执行构建
      - name: Build Hugo Site
        run: |
          echo "🔨 开始构建Hugo站点..."
          hugo --gc --minify --verbose
          echo "✅ 构建完成"

      # 步骤7: 验证构建产物
      - name: Verify Build Output
        run: |
          echo "🔍 验证构建产物..."
          if [ -d "publish" ]; then
            echo "✅ publish目录存在"
            echo "文件数量: $(find publish -type f | wc -l)"
            echo "目录大小: $(du -sh publish | cut -f1)"
            echo "首页检查: $(test -f publish/index.html && echo '存在' || echo '缺失')"
          else
            echo "❌ publish目录不存在!"
            exit 1
          fi

      # 步骤8: 上传构建产物 (用于调试)
      - name: Upload Build Artifacts
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: hugo-site-${{ github.sha }}
          path: publish/
          retention-days: 7

      # 步骤9: 部署到4EVERLAND ⭐ 核心步骤
      - name: Deploy to 4EVERLAND
        id: deploy
        uses: 4everland/pin-action@v1.1
        with:
          EVER_TOKEN: ${{ secrets.EVER_TOKEN }}
          BUILD_LOCATION: ./publish
          EVER_PROJECT_NAME: 'victor42.eth'
          EVER_PROJECT_PLAT: 'IPFS'
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}

      # 步骤10: 输出部署结果
      - name: Show Deployment Results
        if: always()
        run: |
          echo "🚀 部署结果:"
          echo "Hash: ${{ steps.deploy.outputs.hash }}"
          echo "URI: ${{ steps.deploy.outputs.uri }}"
          echo "Project Link: ${{ steps.deploy.outputs.projLink }}"

      # 步骤11: 添加PR评论 (仅PR时)
      - name: Comment PR with Deployment Link
        if: github.event_name == 'pull_request'
        uses: actions/github-script@v7
        with:
          script: |
            const { data: comments } = await github.rest.issues.listComments({
              owner: context.repo.owner,
              repo: context.repo.repo,
              issue_number: context.issue.number
            });

            const botComment = comments.find(comment =>
              comment.user.type === 'Bot' && comment.body.includes('4EVERLAND部署')
            );

            const deploymentLink = '${{ steps.deploy.outputs.projLink }}';
            const commentBody = `🚀 4EVERLAND部署成功!

            - **预览链接**: ${deploymentLink}
            - **Commit**: ${context.sha}
            - **构建者**: ${context.actor}
            - **时间**: ${new Date().toISOString()}
            `;

            if (botComment) {
              await github.rest.issues.updateComment({
                owner: context.repo.owner,
                repo: context.repo.repo,
                comment_id: botComment.id,
                body: commentBody
              });
            } else {
              await github.rest.issues.createComment({
                issue_number: context.issue.number,
                owner: context.repo.owner,
                repo: context.repo.repo,
                body: commentBody
              });
            }

      # 步骤12: 更新Commit状态 (仅push到main时)
      - name: Update Commit Status
        if: github.event_name == 'push' && github.ref == 'refs/heads/main'
        uses: actions/github-script@v7
        with:
          script: |
            const deploymentLink = '${{ steps.deploy.outputs.projLink }}';
            await github.rest.repos.createCommitStatus({
              owner: context.repo.owner,
              repo: context.repo.repo,
              sha: context.sha,
              state: 'success',
              target_url: deploymentLink,
              description: '4EVERLAND部署成功',
              context: '4EVERLAND Deployment'
            });

  # 部署状态检查
  deploy-status:
    name: Check Deployment Status
    runs-on: ubuntu-latest
    needs: build
    if: always()
    steps:
      - name: Verify Deployment
        run: |
          if [ "${{ needs.build.result }}" == "success" ]; then
            echo "✅ 部署成功"
            exit 0
          else
            echo "❌ 部署失败"
            exit 1
          fi
```

### 3.2 工作流特点

1. **详细的日志输出** - 每步都有说明，便于排查问题
2. **环境验证** - 提前发现问题
3. **产物验证** - 确保构建正确
4. **PR集成** - 自动添加部署链接到PR评论
5. **失败处理** - 保留构建产物用于调试
6. **缓存优化** - Node.js依赖缓存加速构建

---

## 4. 4EVERLAND 配置步骤

### 4.1 准备阶段

#### 步骤1: 创建4EVERLAND账号
1. 访问 [4EVERLAND官网](https://www.4everland.org/)
2. 注册账号
3. 完成邮箱验证

#### 步骤2: 创建Auth Token
1. 登录 [4EVERLAND Dashboard](https://dashboard.4everland.org/hosting)
2. 导航至: **Hosting → Auth Tokens**
3. 点击 **"Create New Token"**
4. 填写Token名称: `GitHub Actions - victor42.eth`
5. 点击 **"Create"**
6. **立即复制Token** (只显示一次)
7. 将Token保存为GitHub Secret: `EVER_TOKEN`

#### 步骤3: 创建IPFS项目
1. 在Dashboard中点击 **"Create New Project"**
2. 选择 **"Static Web Hosting"**
3. 项目配置:
   - **Name**: `victor42.eth`
   - **Platform**: `IPFS`
   - **Framework**: `Hugo` (4EVERLAND会检测)
4. **先不连接GitHub** (我们用GitHub Actions)

### 4.2 GitHub集成

#### 步骤4: 配置GitHub Secrets
在GitHub仓库 `greenzorro/victor42.eth` 中:

1. 导航至: **Settings → Secrets and variables → Actions**
2. 点击 **"New repository secret"**
3. 添加:
   - **Name**: `EVER_TOKEN`
   - **Secret**: `<粘贴4EVERLAND的Token>`
4. 点击 **"Add secret"**

#### 步骤5: 提交GitHub Actions配置
1. 在项目根目录创建 `.github/workflows/deploy.yml`
2. 复制上述工作流配置
3. 提交并推送:
   ```bash
   git add .github/workflows/deploy.yml
   git commit -m "Add GitHub Actions workflow for 4EVERLAND deployment

   - Build Hugo site with Stack theme
   - Handle SCSS/TS dependencies
   - Deploy to 4EVERLAND IPFS
   - Supports PR previews and deployment status"
   git push origin main
   ```

### 4.3 首次部署测试

#### 步骤6: 触发工作流
1. 访问GitHub仓库的 **Actions** 标签
2. 应该看到 "Build and Deploy to IPFS via 4EVERLAND" 工作流
3. 点击最新工作流查看进度
4. 观察各步骤执行情况

#### 步骤7: 检查工作流日志
重点检查:
- ✅ Checkout成功
- ✅ Hugo安装成功
- ✅ Node.js安装成功
- ✅ Stack主题依赖安装 (如果存在)
- ✅ Hugo构建成功
- ✅ publish目录生成
- ✅ 4EVERLAND部署成功
- ❌ 如果有错误，查看详细日志

#### 步骤8: 验证部署结果
1. 工作流完成后，查看步骤9的输出:
   - `hash`: IPFS哈希值
   - `uri`: IPFS链接
   - `projLink`: 4EVERLAND项目链接
2. 点击 `projLink` 访问站点
3. 检查功能:
   - 首页加载
   - 文章列表
   - 文章详情
   - 图片显示
   - 多语言切换
   - Sitemap生成

### 4.4 ENS域名绑定

#### 步骤9: 绑定ENS域名
1. 在4EVERLAND Dashboard中打开 `victor42.eth` 项目
2. 导航至: **Domains → Decentralized Domains → ENS**
3. 点击 **"Add Domain"**
4. 输入域名: `victor42.eth.limo`
5. 点击 **"Add"**
6. 点击 **"Set Content Hash"**
7. 确认自动检测到IPNS记录
8. 点击 **"Bind"**
9. 在MetaMask中确认交易 (~$0.3)
10. 等待1-3分钟，状态变为 **"✅ Active"**

#### 步骤10: 验证域名解析
1. 访问: `https://victor42.eth.limo`
2. 应该看到您的博客
3. 如果无法访问:
   - 检查ENS记录是否生效 ([ENS App](https://app.ens.domains/))
   - 尝试通过 [eth.limo](https://eth.limo/) 访问
   - 清除浏览器缓存

### 4.5 高级配置

#### 步骤11: 配置自定义域名 (可选)
如果已有传统域名:
1. 导航至: **Domains → Centralized Domains**
2. 点击 **"Add Custom Domain"**
3. 输入域名: `www.victor42.eth.limo`
4. 按照提示配置DNS记录:
   ```
   类型: CNAME
   名称: www
   值: cname.4everland.org
   ```
5. 保存并等待DNS传播

#### 步骤12: 设置部署钩子 (可选)
1. 在项目中导航至: **Settings → Webhooks**
2. 复制Webhook URL
3. 在GitHub中配置: **Settings → Webhooks**
4. 添加Webhook:
   - **Payload URL**: `<4EVERLAND Webhook URL>`
   - **Content type**: `application/json`
   - **Events**: `Push events`

---

## 5. 实施时间表

### Phase 1: 环境准备 (1天)
- [ ] 创建4EVERLAND账号
- [ ] 生成Auth Token
- [ ] 配置GitHub Secrets
- [ ] 了解工作流配置

### Phase 2: 工作流实现 (1天)
- [ ] 创建 `.github/workflows/deploy.yml`
- [ ] 提交并推送代码
- [ ] 观察首次构建
- [ ] 修复发现的问题

### Phase 3: 部署验证 (1天)
- [ ] 检查构建产物
- [ ] 验证站点功能
- [ ] 测试多语言
- [ ] 确认图片加载

### Phase 4: 域名迁移 (1天)
- [ ] 绑定ENS域名
- [ ] 验证域名解析
- [ ] 检查所有页面
- [ ] 更新DNS设置 (如需要)

### Phase 5: 切换和清理 (1天)
- [ ] 在4EVERLAND中删除fleek.xyz部署
- [ ] 更新书签和文档
- [ ] 监控24小时
- [ ] 记录问题和解决方案

**总计: 5天**

---

## 6. 测试和验证清单

### 6.1 构建测试
- [ ] `hugo --gc --minify` 成功执行
- [ ] `publish` 目录生成
- [ ] 静态资源完整
- [ ] 无404错误

### 6.2 功能测试
- [ ] 首页正常加载
- [ ] 文章列表显示
- [ ] 文章详情可访问
- [ ] 分类页面正常
- [ ] 搜索功能 (如存在)
- [ ] RSS生成
- [ ] Sitemap生成

### 6.3 多语言测试
- [ ] 中文文章可访问 (`/post/slug/`)
- [ ] 英文文章可访问 (`/post/en/slug/`)
- [ ] 语言切换按钮
- [ ] hreflang标签正确
- [ ] 翻译版本关联正确

### 6.4 性能测试
- [ ] 首页加载 < 3秒
- [ ] 图片优化正确
- [ ] CDN加速生效
- [ ] 缓存策略正确

### 6.5 移动端测试
- [ ] 响应式布局正常
- [ ] 移动端菜单可用
- [ ] 文字大小合适
- [ ] 图片缩放正确

### 6.6 SEO测试
- [ ] 标题和描述正确
- [ ] 规范链接设置
- [ ] Open Graph标签
- [ ] Twitter Card标签
- [ ] 结构化数据

---

## 7. 故障排除指南

### 7.1 构建失败

#### 问题: Hugo构建失败
**症状**: `hugo --gc --minify` 执行报错

**排查步骤**:
1. 检查Hugo版本是否符合要求 (≥ 0.87.0 Extended)
2. 查看错误日志定位问题
3. 常见原因:
   - Markdown语法错误
   - 缺失主题文件
   - 配置语法错误
   - 资源文件路径错误

**解决方案**:
```yaml
# 切换到debug模式
- name: Build Hugo Site
  run: |
    hugo --gc --minify --verbose --debug
    # 查看详细错误信息
```

#### 问题: Node依赖安装失败
**症状**: Stack主题依赖安装报错

**排查步骤**:
1. 确认主题存在 `package.json`
2. 检查npm缓存
3. 查看npm错误日志

**解决方案**:
```yaml
# 清理npm缓存
- name: Clean npm cache
  run: npm cache clean --force

# 升级npm版本
- name: Upgrade npm
  run: npm install -g npm@latest
```

#### 问题: SCSS编译失败
**症状**: 样式文件缺失或错误

**排查步骤**:
1. 确认使用Hugo Extended
2. 检查SCSS语法
3. 查看主题assets配置

**解决方案**:
```yaml
# 使用Hugo Extended构建
- name: Setup Hugo
  uses: peaceiris/actions-hugo@v2
  with:
    hugo-version: '0.111.3'
    extended: true  # 必须是true
```

### 7.2 部署失败

#### 问题: 4EVERLAND Token无效
**症状**: 部署时401/403错误

**解决方案**:
1. 确认Token在GitHub Secrets中配置
2. 重新生成Token
3. 检查Token权限

#### 问题: IPFS部署失败
**症状**: 部署步骤报错

**排查步骤**:
1. 检查BUILD_LOCATION路径
2. 确认publish目录存在
3. 查看4EVERLAND日志

**解决方案**:
```yaml
# 验证构建目录
- name: Verify build directory
  run: |
    ls -la publish/
    du -sh publish/

# 使用绝对路径
- name: Deploy to 4EVERLAND
  uses: 4everland/pin-action@v1.1
  with:
    BUILD_LOCATION: ${{ github.workspace }}/publish
```

#### 问题: ENS域名不解析
**症状**: 域名访问404

**排查步骤**:
1. 检查ENS记录状态
2. 验证IPNS绑定
3. 确认eth.limo网关

**解决方案**:
1. 在 [ENS App](https://app.ens.domains/) 检查记录
2. 重新执行Bind操作
3. 等待3-5分钟再测试

### 7.3 性能问题

#### 问题: 站点加载慢
**原因**: 未使用4EVERLAND CDN

**解决方案**:
1. 确认4EVERLAND项目已启用CDN
2. 检查图片URL是否使用CDN
3. 启用gzip压缩

#### 问题: 图片不显示
**原因**: CDN域名或路径错误

**解决方案**:
1. 确认图片使用完整URL: `https://cdn.victor42.work/`
2. 检查图片文件存在
3. 测试直接访问图片URL

---

## 8. 从 fleek.xyz 迁移指南

### 8.1 迁移前准备
1. **备份当前部署**:
   - 记录fleek的部署URL
   - 保存构建日志
   - 确认所有功能正常

2. **记录重要配置**:
   - ENS域名设置
   - DNS配置 (如使用自定义域名)
   - 资源链接

### 8.2 执行迁移
1. **并行部署**:
   - 在4EVERLAND创建新项目
   - 部署到4EVERLAND
   - 保持fleek.xyz部署不变

2. **功能对比**:
   - 比较两个站点的功能
   - 检查所有页面
   - 确认多语言正常

3. **域名切换**:
   - 在4EVERLAND中绑定ENS域名
   - 在fleek中删除域名绑定
   - 或配置DNS指向新部署

4. **清理fleek**:
   - 删除fleek项目
   - 取消订阅 (如付费)
   - 更新文档

### 8.3 迁移后检查
- [ ] 所有页面可访问
- [ ] 图片正常显示
- [ ] 多语言切换正常
- [ ] Sitemap正确更新
- [ ] 搜索功能正常
- [ ] RSS Feed正常
- [ ] 性能未下降
- [ ] 无404错误

---

## 9. 监控和维护

### 9.1 自动化监控
1. **GitHub Actions状态**: 每次部署自动通知
2. **4EVERLAND监控**: 设置邮件/Discord通知
3. **域名解析监控**: 定期检查ENS记录
4. **页面可用性监控**: 使用UptimeRobot等工具

### 9.2 定期维护
- **每周**: 检查构建日志
- **每月**: 更新Hugo版本
- **每季度**: 检查4EVERLAND使用量和费用
- **每年**: 评估新功能和优化

### 9.3 性能优化
1. **图片优化**:
   - 压缩大图片
   - 使用WebP格式
   - 添加懒加载

2. **缓存策略**:
   - 启用浏览器缓存
   - 使用CDN缓存
   - 设置合理的过期时间

3. **代码优化**:
   - 压缩CSS/JS
   - 移除未使用的代码
   - 优化模板

---

## 10. 成本分析

### 10.1 4EVERLAND费用
**免费套餐** (对于您的项目足够):
- 存储: 6GB/月 (您的站点约50-100MB)
- 构建: 250分钟/月
- 带宽: 10GB/月
- 费用: **$0/月**

**付费套餐** (如需要):
- 存储: $0.08/GB/月
- 带宽: $0.10/GB
- 预计月费用: <$2

### 10.2 预期收益
1. **更好性能**: 4EVERLAND CDN vs fleek
2. **更稳定**: ENS + IPNS自动更新
3. **更简单**: GitHub Actions自动化
4. **更灵活**: 自定义构建流程
5. **成本低**: 免费套餐足够使用

---

## 11. 风险评估

### 11.1 技术风险
| 风险 | 影响 | 概率 | 缓解措施 |
|------|------|------|----------|
| GitHub Actions失败 | 中 | 低 | 保留fleek备用部署 |
| 4EVERLAND服务中断 | 中 | 低 | 手动部署IPFS |
| ENS域名解析问题 | 中 | 中 | 备用人人可访问的IPFS URL |
| Hugo版本兼容问题 | 低 | 中 | 固定Hugo版本号 |

### 11.2 缓解策略
1. **保持多平台部署**: 4EVERLAND + fleek并行一段时间
2. **定期备份**: 每周导出站点源文件
3. **快速回滚**: 保留Git历史，可快速回滚
4. **监控告警**: 设置自动化监控

---

## 12. 成功标准

### 12.1 技术标准
- [ ] 每次push到main分支自动部署
- [ ] PR自动生成预览链接
- [ ] 部署时间 < 5分钟
- [ ] 构建成功率 > 99%
- [ ] 部署失败自动通知

### 12.2 功能标准
- [ ] 所有页面可访问
- [ ] 多语言功能完整
- [ ] 图片和静态资源正常
- [ ] Sitemap和RSS正确生成
- [ ] SEO元素完整

### 12.3 性能标准
- [ ] 首屏加载 < 3秒
- [ ] 页面交互流畅
- [ ] 移动端体验良好
- [ ] SEO评分 > 90

---

## 13. 附录

### 13.1 常用命令
```bash
# 本地测试构建
hugo --gc --minify

# 清理缓存
hugo --cleanDestinationDir

# 本地开发服务器
hugo server -D

# 检查Hugo版本
hugo version
```

### 13.2 有用链接
- [4EVERLAND文档](https://docs.4everland.org/)
- [4EVERLAND Dashboard](https://dashboard.4everland.org/)
- [ENS App](https://app.ens.domains/)
- [eth.limo网关](https://eth.limo/)
- [GitHub Actions文档](https://docs.github.com/actions)

### 13.3 紧急联系
- GitHub支持: [support.github.com](https://support.github.com)
- 4EVERLAND客服: [Discord](https://discord.gg/4everland)
- Hugo社区: [Discourse](https://discourse.gohugo.io/)

---

## 14. 实施计划

### 下一步行动
1. ✅ 阅读本plan.md
2. ⏳ 创建4EVERLAND账号
3. ⏳ 生成Auth Token
4. ⏳ 配置GitHub Secrets
5. ⏳ 创建GitHub Actions工作流
6. ⏳ 首次部署测试
7. ⏳ 绑定ENS域名
8. ⏳ 完整功能验证
9. ⏳ 从fleek迁移
10. ⏳ 清理和优化

### 预期时间
- **准备阶段**: 2小时
- **实现阶段**: 4小时
- **测试阶段**: 2小时
- **迁移阶段**: 1小时
- **总计**: ~1天

---

**文档版本**: v1.0
**创建日期**: 2025-11-08
**适用项目**: victor42.eth
**方案**: GitHub Actions + 4EVERLAND IPFS部署

---

*本计划基于对项目的深入分析和4EVERLAND平台特性的研究，提供了完整的实施指南。如有问题，请参考故障排除章节或相关文档。*