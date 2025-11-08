# 4EVERLAND 自动GitHub集成配置指南

## 前提条件
- ✅ GitHub Actions工作流已运行 (https://github.com/greenzorro/victor42.eth/actions)
- ✅ Hugo构建成功
- ✅ Artifact已上传
- ✅ 4EVERLAND账号已创建

## 在4EVERLAND中配置GitHub自动部署

### 步骤1: 创建4EVERLAND项目
1. 登录 [4EVERLAND Dashboard](https://dashboard.4everland.org/hosting)
2. 点击 **"Create New Project"**
3. 选择 **"Static Web Hosting"**
4. 配置项目:
   - **Name**: `victor42.eth`
   - **Platform**: `IPFS`
   - **Framework**: `Hugo` (会自动检测)
   - **Build Command**: `hugo --gc --minify`
   - **Output Directory**: `publish`
   - **Root Directory**: `/` (默认)

### 步骤2: 连接GitHub仓库
1. 在项目中点击 **"Connect GitHub"**
2. 授权4EVERLAND访问您的GitHub账号
3. 选择仓库: `greenzorro/victor42.eth`
4. 选择分支: `main`
5. 点击 **"Connect"**

### 步骤3: 配置自动部署
1. 在项目设置中启用 **"Auto Deploy"**
2. 选择触发方式:
   - **GitHub Webhook** (推荐) - 每次push到main分支自动部署
   - **定期检查** - 每小时检查一次
3. 确保Webhook URL已配置

### 步骤4: 绑定ENS域名
1. 在项目页面点击 **"Domains"**
2. 点击 **"Decentralized Domains"**
3. 选择 **"ENS"**
4. 点击 **"Add Domain"**
5. 输入: `victor42.eth.limo`
6. 点击 **"Add"**
7. 点击 **"Set Content Hash"** (自动设置IPNS)
8. 点击 **"Bind"**
9. 在MetaMask中确认交易 (~$0.3)
10. 等待1-3分钟，状态变为 **"✅ Active"**

### 步骤5: 验证部署
1. 访问: `https://victor42.eth.limo`
2. 检查:
   - ✅ 首页正常加载
   - ✅ 文章列表显示
   - ✅ 文章详情可访问
   - ✅ 图片正常显示
   - ✅ 多语言切换正常
   - ✅ Sitemap正确生成

## 验证自动部署流程

### 完整流程测试
1. 在本地修改一篇博客文章
2. 提交并推送到GitHub:
   ```bash
   git add .
   git commit -m "Test: Update blog post"
   git push origin main
   ```
3. 查看GitHub Actions: 看到Hugo构建运行
4. 查看4EVERLAND Dashboard: 看到自动部署开始
5. 访问博客验证更新

## 故障排除

### 问题1: GitHub连接失败
- 检查4EVERLAND是否已授权GitHub
- 确认仓库名称和分支正确
- 尝试重新连接

### 问题2: 自动部署不触发
- 确认 "Auto Deploy" 已启用
- 检查Webhook配置
- 手动触发一次部署测试

### 问题3: 构建失败
- 查看GitHub Actions日志
- 检查Hugo版本和配置
- 确认主题依赖正常

### 问题4: 域名不解析
- 确认ENS记录设置正确
- 等待3-5分钟DNS传播
- 通过 [ENS App](https://app.ens.domains/) 验证

## 重要提示

⚠️ **当前GitHub Secrets**:
- `TOKEN_4EVERLAND` - 现在不需要了！可以删除
- GitHub不再需要4EVERLAND的token

✅ **工作流状态**:
- GitHub只负责构建
- 4EVERLAND负责部署
- 两者完全解耦

---

**配置完成后，您的博客将实现完全自动化部署！** 🚀
