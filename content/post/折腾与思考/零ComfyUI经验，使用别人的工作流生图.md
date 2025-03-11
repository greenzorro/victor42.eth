---
title: 零ComfyUI经验，使用别人的工作流生图
description: 真的0基础，就像用微信小程序一样。
image: https://cdn.victor42.work/posts/2025-02/65e10ec43957abff3dbb183248e33bd3.webp
date: 2025-02-27 12:15:00
categories: 折腾与思考-Geek
url: /post/comfyui-workflow-tutorial-for-newbies
translationKey: comfyui-workflow-tutorial-for-newbies
---

[LiblibAI-哩布哩布AI - 中国领先的AI创作平台](https://www.liblib.art/workflows)

Liblib上有很多免费的工作流，一般生图产品实现不了的特殊能力，如：**换脸、模特穿衣、商品图打光加背景、生成表情包**，用Liblib上的工作流都可以实现。Liblib每天有一定的免费生成额度，如果用得好，用得多，充钱就是了。

至于ComfyUI，就是这样的东西，可以理解为一个生图程序，具体原理以后再学也不迟：

![](https://cdn.victor42.work/posts/2025-02/65e10ec43957abff3dbb183248e33bd3.webp)

Liblib的工作流本质上都是ComfyUI程序，虽然现在不必理解这程序怎么做出来的，但要会用别人的程序。用的过程中你会遇到3种情况。

## 1️⃣ 有这个按钮，作者已经把程序打包成应用了

![](https://cdn.victor42.work/posts/2025-02/46c26df9a8577c9cdf77aae4af49f1f1.webp)

你点进去就可以直接运行，操作很简单。看不到程序内部原理。

![](https://cdn.victor42.work/posts/2025-02/caefee5ee6854594b0e273f148ddbc46.webp)

## 2️⃣ 没有打包成应用，出现的是这种浅蓝色运行按钮

![](https://cdn.victor42.work/posts/2025-02/421edc7a9ebe6cf69aa23245d5d0ea01.webp)

点了打开就会进入ComfyUI界面，黑色的界面，打开比较慢，多等一会儿。里面跟接线板一样，很复杂。

但一般为了大家使用方便，作者会在程序里加上必要的操作说明。每个程序操作说明都不一样，说明的形式也不一样，要找到并认真阅读。比如这个就是作者加的说明：

![](https://cdn.victor42.work/posts/2025-02/7d652a7e19399a3c53683aa792a38bb7.webp)

## 3️⃣ 浅蓝色查看工作流按钮，但进去没有任何说明

![](https://cdn.victor42.work/posts/2025-02/b78bb6863e56b1c86be4bfd3feb0a5d5.webp)

这种一般是作者比较懒，连说明都不写。你可以大概看看整个程序是不是很复杂。

**操作提示：鼠标滚轮缩放界面，按住空格拖动可以移动视野。**

一、如果你判断程序比较简单，接线板卡片比较少，应该还有希望继续用，只需要找到2种关键的卡片：

- 上传图片的卡片长这样，未必一模一样，关键特征是带有这个 choose file to upload 按钮：![](https://cdn.victor42.work/posts/2025-02/88465060dc6397b6e62a5bfca4b1d89f.webp)
- 输入文字的卡片长这样，关键特征是这种黑色输入框，这一般是给你输入提示词用的：![](https://cdn.victor42.work/posts/2025-02/09dbc0f7779d7896470f8ffc876d936d.webp)

会用这两种卡片，往里面传图片、写文字，然后按运行，大概率就能成功。

二、如果程序实在很复杂，这种图片卡片和文字卡片很多，不知道该用哪个。那还是先放弃，找找其他有说明的同类工作流。

---

## ⚠️ 报错处理

另外，你还可能遇到程序报错，一堆英文出来：

![](https://cdn.victor42.work/posts/2025-02/1ae88573acbc157fb7bf1443a68dcb25.webp)

不要慌，你关掉这个报错弹窗，程序会把出错的卡片标红：

![](https://cdn.victor42.work/posts/2025-02/c024ed1135e6e390d941dfa607010b77.webp)

放大过去看看，出错的卡片通常是用来加载AI模型的：

![](https://cdn.victor42.work/posts/2025-02/53f255d839ade35227ea9c02e782517b.webp)

程序作者制作时可能是在自己电脑上做的，模型的名称是他自己电脑上的文件名。但是他把程序传到Liblib上来，模型的名称可能Liblib平台的不一样，所以卡片出错是因为找不到对应的模型。

这个好办，你记住里面每一个选项的名字，尤其是小数点前面的部分，那是模型的名称。然后点击每个模型，在下拉菜单里选名称和它最接近的（当然一模一样最好了）：

![](https://cdn.victor42.work/posts/2025-02/c460eab80d6db0ff96dac59993a8ca9e.webp)

把出错卡片的每一个模型都重新选一遍，再运行就可以了。

如果列表里找不到相应的，可以直接在 [Liblib模型广场](https://www.liblib.art/) 找，找到之后加入模型库，下拉菜单里就有了。

这样可以解决90%以上的错误。