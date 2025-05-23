---
title: 如何表达App的隐藏手势操作
description: 
image: 
date: 2017-01-22 22:03:37
categories: 设计译文-Design
url: /post/3538
---

**[国外设计第161期]**

![Nick Babich](https://cdn.victor42.work/posts/2017-01/01-18/1-raN6DpE52jAdYaEc-zsu3A.png)

手势操作，是通过手指轻微移动来让用户操作应用。触屏界面提供了许多自然的手势，比如点按、滑动、双指缩放。但这些交互方式不像UI控件，通常对于用户是不可见的。除非用户事先了解手势存在，否则他们并不会尝试使用。

如何加入隐藏手势呢？好在有许多视觉层面的交互设计技巧，可以让用户了解这些手势。

## 首次打开时的教程和引导页

在手势为主的应用中，教程和引导页相当常见。许多情况下，在应用中加入教程意味着向用户说明、解释界面。但是，UI教程并不是阐述应用核心功能的最简洁方式。这种方式存在两个问题：

- 如果你要给产品准备说明书，就说明与用户的沟通还不到位，因为他们可不希望使用前还要读说明书。
- 另一个问题在于，用户不得不记住所有这些新的用法。

举个例子，Clear应用一开始会展示7页教程，用户得耐心阅读所有信息，尝试记在脑海中。这个设计很糟糕，因为它需要用户在真正开始使用之前就付出精力。

![](https://cdn.victor42.work/posts/2017-01/01-18/1-2.png)

*Clear的教程*

避免使用强制性的多步引导，要试图在操作所处环境中教育用户（这时候用户真正需要相应功能）。几经迭代后，教程可以变成更加平缓的暗示。

> 关注单个操作，而不是试图在界面中解释每一个操作。

以Android版YouTube的手势操作指引为例：

![](https://cdn.victor42.work/posts/2017-01/01-18/2-2.png)

*Android版Youtube*

这个应用有用到手势操作，但并不是通过教程的方式教育用户。它反而是在新用户首次触发时进行了暗示，每次只介绍一处，而且只在用户进入相关功能时才触发。

## 如何在情境中教育用户

在情境中教育的技巧，能帮助用户以一种从未尝试过的方式操作某个元素或界面。这种技巧通常包含*轻微的视觉提示*和*微妙的动画*。

### 纯文本指令

这个技巧主要依靠纯文本指令，促使用户执行某个手势操作，并且简明地描述这个操作的结果。

**注意：**说明文字要非常简短——文字越短，用户越可能会阅读，然后才能遵照它的指引。

![](https://cdn.victor42.work/posts/2017-01/01-18/3-1.gif)

*图片来源：Material Design*

### 提示动效

提示动效（或者动画暗示）表现了执行操作时具体手势的效果预览。例如，Pudding Monsters游戏的诀窍就是完全依靠手势操作，但是用户不必过多猜测就能掌握基本玩法。动画传达了功能方面的信息——用动画来展现一个具体场景，用户立马明白该怎么做。

![](https://cdn.victor42.work/posts/2017-01/01-18/4-1.gif)

*提示动效展现了如何操作一个元素。来源：Pudding Monsters*

### 内容的暗示

内容暗示是一种微妙的视觉线索，表明了操作的可能。下面这个例子展示了卡片的内容暗示——当前卡片的下方还有其他卡片，这显然表明它是可以滑动的。

![](https://cdn.victor42.work/posts/2017-01/01-18/5-1.gif)

*展现出导航功能。来源：Barthelemy Chalvet*

## 结论

总之，在移动或网页应用中展现手势操作方式，并没有万能的方案。不过在教育用户操作界面时，我比较推崇通过内容暗示、[渐进式提示](http://babich.biz/design-patterns-progressive-disclosure-for-mobile-apps/)和微妙的动画，在具体情景中教育用户。教程和引导页应该只作为最后手段。

感谢阅读！

---

原文链接：[http://babich.biz/how-to-communicate-hidden-gestures-in-mobile-app/](http://babich.biz/how-to-communicate-hidden-gestures-in-mobile-app/)

作者信息：[Nick Babich](http://babich.biz/author/nick/)