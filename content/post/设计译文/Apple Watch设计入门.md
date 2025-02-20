---
title: Apple Watch设计入门
description: 
image: 
date: 2015-04-05 12:32:00
categories: 设计译文-Design
url: /post/3433
---

**[国外设计第81期]**

这个月晚些时候，众望所归的[Apple Watch](http://www.apple.com/watch/)会带来成千上万的手表应用，冲击应用市场，吸引你的注意。由于屏幕尺寸更小，又始终戴在手腕上，交互方式也有所不同。要在Apple Watch上创造一个美观、舒适的体验，需要新的设计方式。本文将带你入门。

本文中，你将学习如何通过一些基础理论和准则，**为Apple Watch设计应用**，借此初探可穿戴设备设计。

## 应用结构

Apple Watch应用有3部分：**WatchKit App**、**Glance**界面和**通知**。每种都有不同的目的，面临不同的设计挑战。

### WatchKit App

![Design for Apple Watch](http://designmodo.com/wp-content/uploads/2015/03/1-watchkit-app.jpg)

WatchKit App是查看应用数据或与之交互的主要手段。它通常从手表主屏进入，但也可以从Glance或通知进入。

很重要的一点，要知道WatchKit App**只有**两种类型的导航——**层级式**和**页面式**。虽然iOS应用可以编写出自定义导航，但WatchKit App限制很严格，目前并不支持。

![Hierarchical](http://designmodo.com/wp-content/uploads/2015/03/2-hierarchical.jpg)

**层级式**非常适合相对复杂的应用，类似很多现存iPhone应用，用户在其中需要进行一系列的选择，然后到达结束界面。牢记Apple预期用户在10秒内突击使用手表，所以别在手表上照搬现成应用，应该将它升华。

![Page based](http://designmodo.com/wp-content/uploads/2015/03/3-page-based.jpg)

**页面式**通过横向滑动，让用户在多个页面间穿梭。如果各页数据并不依赖其他页面，这种导航方式更佳。

开始设计时，想清楚什么数据对用户最重要，相互关系如何，然后选择最适于体现数据的导航结构。

### Glance

![Glance](http://designmodo.com/wp-content/uploads/2015/03/4-glance.jpg)

**Glance**是一系列可浏览的内容，基于时间或环境，穿戴者从最喜欢的应用中挑选而出。在Apple Watch上上滑可以触发Glance，然后可以水平滑动。Glance不是必须的，所以并非所有应用都具有，或者需要。

Glance被限制在无法滚动的一屏中，所以你得把最有用、最重要的信息展现在屏幕上，可以通过颜色、不同字号和图片来在视觉上区别你的Glance。在Glance上点击任何地方，会打开手表应用。所以要避免在其中包含按钮、滑块和菜单这样的操作项。

![Glance templates](http://designmodo.com/wp-content/uploads/2015/03/5-glance-templates.jpg)

最后，Glance基于一些模版。所以你的设计要选择一种最能体现数据意义的形式。Apple提供了一系列模版，适用于上半屏和下半屏。

### 通知

![Notifications](http://designmodo.com/wp-content/uploads/2015/03/6-notifications.jpg)

Apple Watch应用有**两种通知状态**，分别叫做short-look和long-look界面。用户首次收到通知时，short-look通知会出现，持续较短一段时间。用户可以降低手腕忽略通知，也可以抬起手腕或点击short-look通知，进入long-look查看详细信息和功能。

由于手表始终戴在手腕上，你得对通知有所限制，只推送最有用的信息。如果你持续被不重要的消息打断，那是很令人厌烦的。最好的通知会使用用户的环境信息——比如位置、时间或活动——来提供实时、相关的信息。

![Short look](http://designmodo.com/wp-content/uploads/2015/03/7-short-look.jpg)

short-look界面包含应用图标、应用名称和通知的标题。由于标题是你唯一能控制的东西，它需要为通知的内容提供简短的提示。

![Long look](http://designmodo.com/wp-content/uploads/2015/03/8-long-look.jpg)

所有应用的long-look界面结构都是一样的。顶部显示应用图标和名称（也可以自定义这一条的颜色），底部是忽略按钮。中间是定制内容，至多4个自定义操作按钮。

## 交互方式


除了手机上那些我们熟悉的日常手势——点击和滑动，Apple Watch提供了两种新的交互方式：

### 滚轮

![Digital crown](http://designmodo.com/wp-content/uploads/2015/03/9-digital-crown.jpg)

应用可以通过滚轮来滚动，不会像手指滑动那样挡住屏幕。滚轮尤其适用于长页面的滚动。

### 按压

![Force touch](http://designmodo.com/wp-content/uploads/2015/03/10-force-touch.jpg)

Apple Watch的屏幕可以区分点击和按压。就像鼠标的右键单击一样，按下可以显示当前界面的菜单，其中包含至多4项相关内容。

双指缩放这样的多点触控手势在手表上是没有的。

## 布局

![Layout](http://designmodo.com/wp-content/uploads/2015/03/11-layout.jpg)

Apple Watch有两种尺寸——33mm和43mm。小屏幕尺寸是340x272像素，大屏幕是390x312像素。手表的一大特点是retina屏，就像iPhone那样，你要提供两倍分辨率大小的图片。

你不必提供不同尺寸的图片（虽然可以这么做），也不必设计两套不同的布局。因为Apple使用相对尺寸和距离，图片和组件会缩放充满可用空间。

![Full width](http://designmodo.com/wp-content/uploads/2015/03/12-full-width.jpg)

设计应用时，Apple建议用黑色背景来配合外框。相比浅色，深色与亮色的搭配更好。由于外框提供了额外的边距，占满可用空间、按满屏宽度设计非常重要。

至于按钮，Apple也建议满屏宽。不过，如果你有并列按钮，应该用图标代替文字。一行中不建议包含3个及以上按钮，因为屏幕太小。同一屏中的按钮应该高度相同，以保持视觉一致性。

## 颜色

由于是在深色背景上设计，你得在应用中使用明亮、高对比度的颜色。颜色也可以作为你应用品牌的一部分。

![Key color](http://designmodo.com/wp-content/uploads/2015/03/13-key-color.jpg)

每个应用可以定义一个“主色”，它会显示在状态栏的标题和通知的应用名称上。还可以自定义long-look通知的顶栏颜色。

## 动画

![Zoom](http://designmodo.com/wp-content/uploads/2015/03/14-dm-zoom.gif)

美观、细致的动画可以提升用户体验，使应用更迷人、更具诱惑力，令人过目不忘。设计手表上的动画时，要确保它足够迅速，而且确有其目的。如果动画阻滞了用户获取他们所需的信息，则会损害用户体验。

在Apple Watch上创作动画时，你可不能给工程师一张GIF图，然后让他动态实现。你得提供每一帧的独立静态图片，来制作更快速和流畅的动画集成。最佳方式是将你的动画文件导入After Effects或Photoshop，提取出独立的每一帧。

## Context menu

![Context menu](http://designmodo.com/wp-content/uploads/2015/03/15-context-menu.jpg)

Context menu至多显示4个操作项，它表现为一个带有标签的圆形图片。点击某个操作项或屏幕上的任意位置，菜单收起。设计Context menu时无需考虑颜色。就像iOS应用的标签栏图标一样，Context menu的图标是模版内置图片，颜色仅仅定义了图标的形状。

![Menu image sizes](http://designmodo.com/wp-content/uploads/2015/03/16-menu-image-sizes.jpg)

对于Context menu，你得给每个图标提供两种大小的图片。在42mm的手表上，图标的线宽通常比38mm版多1像素。

## 字体

![Font](http://designmodo.com/wp-content/uploads/2015/03/17-font.jpg)

Apple开发了一套无衬线字体，叫做**San Francisco**，为Apple Watch的易读性做过专门处理，包含23种变化。虽然你也可以用自定义字体，Apple建议使用内置文字样式，因为它们是专为小屏幕设计的。

使用Apple系统字体的另一项好处，是标签过长时文字会自动缩放。随着字号增大，字间距会减少。如果要指定字号，那么San Francisco字体建议使用19点或更小字号。San Francisco的Display字体应该用于20点或更大的字号。

## 应用图标

![Home icons](http://designmodo.com/wp-content/uploads/2015/03/18-home-icons.jpg)

像iOS主屏图标一样，Apple Watch也需要一个应用图标。和iPhone不同，iPhone以方形显示应用图标和名称，Apple Watch是圆的，不包含标签。这就使你的图标必须比iOS应用图标更容易辨识和熟悉，同时表达出它的作用。

为这么小的屏幕设计应用图标时，简洁为先。在炫目的应用图标海洋中，图标是用户打开应用前首先看到的东西，所以你得通过优美的图标设计留下良好的第一印象。

![App icon size](http://designmodo.com/wp-content/uploads/2015/03/19-app-icon-size.jpg)

设计不同尺寸的图标，来适配两种手表尺寸和各个展现图标的界面。系统会自动为图标加上圆形蒙版，所以图标应该依据Apple提供的指南做成方形图片。

可以下载这个好用的[Apple Watch图标模版](http://appicontemplate.com/watch)来生成图标。

## 基础之外

Apple Watch为用户提供了一种不唐突的数据获取方式，这对他们至关重要。通过理解一款应用的结构、交互方式和最佳设计原则，我们可以在Apple Watch上打造更加美观、讨人喜爱的体验。

要深入学习入门，请看[Apple Watch人机交互指南](https://developer.apple.com/library/prerelease/ios/documentation/UserExperience/Conceptual/WatchHumanInterfaceGuidelines/index.html)，并且下载[Apple Watch设计资源](https://developer.apple.com/watchkit/)，里面有一系列模型、参考、模版和字体。

关于讨人喜爱的可穿戴设备体验设计，更多细节、窍门和资源请看[为可穿戴设备而设计](http://www.designforwearables.com/)。这是一门免费课程，让你一步一步经历Apple Watch的应用设计。

---

[原文链接](http://designmodo.com/design-apple-watch/)

作者信息：
[Kenny Chen](http://designmodo.com/author/kenny/)
Kenny Chen is a UX Designer from Los Angeles passionate about creating better experiences through thoughtful design. He curates [UX Design Weekly](http://www.uxdesignweekly.com/), a hand-picked list of the best user experience design links each week. Follow him on Twitter at [@kennycheny](https://twitter.com/kennycheny).