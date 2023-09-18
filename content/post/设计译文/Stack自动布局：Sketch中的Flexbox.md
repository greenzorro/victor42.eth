---
title: Stack自动布局：Sketch中的Flexbox
description: 
image: 
date: 2017-02-26 00:57:13
categories: 设计译文
url: /post/3541
---

**[国外设计第164期]**

*Skacks会彻底改变你对Sketch布局方式的理解。*

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-IjqstHVq3OGLQtqYACVgNA.gif)

就像[CSS中的Flex Box](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)、iOS中的[UIStackView](https://www.raywenderlich.com/114552/uistackview-tutorial-introducing-stack-views)和Android中的[FlexboxLayout](https://github.com/google/flexbox-layout)——**Stack**的自动布局可以再次改变整个局面。

> Sketch用户终于可以在不用CSS的情况下，直接使用Flexbox的排版技术。

我们相信，推动设计生态前进的关键在于，创造出强大的设计概念。

Flexbox已经彻底改变了局面，它出现已有好几年了。但要使用它，你得在浏览器中使用CSS来设计，因此对于多数设计师可望不可及。

Stack是另一种形式的Flexbox，它更直观，但能力丝毫不减。它能使设计师以列、行、网格的思维来思考设计——使设计更加一致。

## **Stack**是什么？

**Stack**是一种特殊的*组*，定义了其内部*图层*的布局方式。

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-uHeThlg0lB65kTcUkrSJQg.png)

*Stack组的图标是一种特殊的蓝色，上面还有图标来表示方向。*

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-7NbmCjfNNEwSnh0gTD7vnQ.png)

*要使图层变为Stack模式，在Auto-Layout面板中点击Stack按钮。*

> 小提示：
> - **Stacks**能产生**一致性**。
> - **一致性**使设计**清晰**。
> - **Stacks**能使设计**清晰**。

一个Stack组有3个属性：

- *方向*：定义其内部图层按照*水平*还是*垂直*方式排列。
    ![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-sAimwEhMxx2WwM1Ah76-AA.gif)
    *方向*
- *对齐*：包括顶对齐、中央对齐、底对齐、伸展。
    ![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-rzprFGD1zbB2PpCwJnQ-vg.gif)
    *对齐*
- *间距*：定义其中每个元素的间距。
    ![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-gEkN2HgGCHq8fCXfCFbJ6Q.gif)

> *Stack可以嵌套使用！*

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-bkdGZNtR8MeedhcouuLHSw.gif)

## 来解这道题！

**90%的设计师第一次都会理解错！**

下图由多少个*Stack组*构成：

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-uQTR5Fw0VMrmVrF9EeHL9w.png)

正确答案是：3。

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-1zBHWsMzI011GOTQSk8SxA.png)

*Stack组的图标是一种特殊的蓝色，上面还有图标来表示方向。*

1. 最里层*横向排列*的红色线框Stack组，其中有2个元素：星星和评论数。
2. 中间层*纵向排列*的蓝色线框Stack组，其中有4个元素：应用名称、作者、分类、红色Stack组。
3. 最外层*横向排列*的绿色线框Stack组，其中有2个元素：应用图标和蓝色Stack组。

## Stack的实用诀窍：

- Stack很适合用于定义**同级**图层间的排列规则。
- 在Stack组里增加或删除元素，会重新排列其中图层。
    ![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-Wl2bIzICvEbiNIm_WTDPtg.gif)
- 文字图层的伸展会移动相邻图层。
    ![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-3KNYU1p478jpCVlz-6joTA.gif)
- 拖拽可以轻松地重新排列子图层。
    ![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2017-02/02-24/1-V4_Axkl8r8JXcpuhBn6obw.gif)

## 使用Stack实现Flex网格

[Alan Roy](https://medium.com/@alanontheweb)，我们产品内测小组的一位多产的成员，用Stack创造出了[Flex网格](https://medium.com/@alanontheweb/responsive-flex-grid-in-sketch-using-autolayout-and-stacked-groups-ec8cfdf5df3f#.i40fnkdo8)系统。

他写了一篇详细解释，并且附带一段10分钟的视频。我们强烈建议阅读和观看这组教程。让人脑洞大开。【译者注：需科学上网】

[https://www.youtube.com/watch?time_continue=2&v=g--AD_Yp5lk](https://www.youtube.com/watch?time_continue=2&v=g--AD_Yp5lk)

[**使用AutoLayout和嵌套组，在Sketch中实现响应式Flex网格**](https://medium.com/@alanontheweb/responsive-flex-grid-in-sketch-using-autolayout-and-stacked-groups-ec8cfdf5df3f)

改善设计体系，便于缩放和统一。

> 我们Anima的使命是让设计师能掌控自己的设计。我们正在打造一款设计工具，让设计师定义和构建UI与UX设计中所有零零碎碎的元素，并且最终能自动生成本地代码，1:1还原设计。这就使设计师**不依赖**团队的其他部分，比如开发人员的优先关注点就与设计团队不同。

自动布局插件下载：[https://animaapp.github.io/Auto-Layout/](https://animaapp.github.io/Auto-Layout/)

指南与文档：[https://animaapp.github.io/docs/v1/guide/12-stacks-flexbox.html](https://animaapp.github.io/docs/v1/guide/12-stacks-flexbox.html)

---

原文链接：[https://medium.com/sketch-app-sources/auto-layout-introducing-stacks-flexbox-for-sketch-c8a11422c7b5#.jyyxfm90k](https://medium.com/sketch-app-sources/auto-layout-introducing-stacks-flexbox-for-sketch-c8a11422c7b5#.jyyxfm90k)

作者信息：[Anima App](https://medium.com/@AnimaApp)
Empowering designers to own their design.