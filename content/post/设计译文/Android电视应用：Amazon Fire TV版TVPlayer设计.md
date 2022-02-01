---
title: Android电视应用：Amazon Fire TV版TVPlayer设计
date: 2016-09-25 00:00:08
categories: 设计译文
url: /post/3523
---

**[国外设计第148期]**

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-F1yr5kRsBHZ2vNWK.jpg)

**设计**和研发、推广一道，是移动应用的成功要诀之一。定义用户操作应用的方式，与应用的功能和高效的盈利模式同等重要。而且，当涉及到**为电视这样的新交互模式设计界面**，许多在智能手机和平板上有效的模式，都需要重新思考，如何利用大屏幕和遥控带来的输入模式。

## Fire TV上的TVPlayer

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-C6I2Hu2HtWFTIPO7.png)

这个任务并没有吓到**TVPlayer**的开发者们，这是全英国在Fire TV和Fire TV Stick上最成功的电视应用之一。

**TVPlayer是一款Android原生流媒体应用，可以让你在Amazon和Android设备上免费观看电视直播**，它掌握了英国许多收视率最高的频道。TVPlayer在2014年作为Fire TV的一部分同时发布，它的成功一直延续至2015年、2016年。

**Simplestream**，TVPlayer背后的研发与设计团队，接受了打造电视优先体验的艰巨任务。

我们采访了运营总监**Lewis Arthur**和Simplestream的Android开发**Michael Jordan**，请他们分享Fire TV应用设计过程中的真知灼见，下面是他们的分享。

## 设计过程：从手机到电视

在登陆Fire TV前，TVPlayer已经可以在Fire Tablets和Android设备的Amazon Appstore中下载。移动端版本的设计师，将关注点聚焦于**可用性与内容的易达性**。他们在欢迎界面采用了**大胆醒目的图片**布局，主标签内有可滚动的直播电视频道列表。设计师决定坚持“浅色”主题，为了使内容突出，也保持各平台的主题一致。

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-AncB4Dlaqvw7nWvV.png)![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-WBoJB2UYacca0TzG.png)

当进行**平板端的支持**时，设计师需要重新思考，更好地利用大屏幕。**主体布局**有所改动，在主界面上直接为用户**呈现更多内容**。这是个很好的策略，既能吸引用户注意，并且为多种相关内容提供快捷入口。

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-s8YaswLN8cFMLkEi.png)

至于**第一版Fire TV应用**，主界面需要呈现新的面貌。电视的设计，与手机平板的界面和用户体验设计有两大不同，这都来源于TV自身的天性：它有**巨大的显示器**，也不提供**触摸式界面**，因为所有的操作都发生在遥控器上。

Simplestream在第一版Fire TV应用的主界面上，**尽数使用了大胆醒目的图片**。“主页”、“正在直播”和“频道”标签**都移到左边**，**字号成倍放大**，使得从远处看也清晰可辨。

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-uER5i3hZGQnhcnw4.png)

第一版Fire TV应用主界面，感觉像平板端那样清爽，栅格布局中承载各类主要频道。

## 为Fire TV开发简单而迅速：4周就从移动端迁移到电视

当我们询问Simplestream团队，从移动版到第一版Fire TV应用**花了多长时间**，他们告诉我们**大约4周**。由于Fire TV是一款完全成熟的Android设备，搭载了基于Android Lollipop的[Fire OS 5](https://developer.amazon.com/public/solutions/devices/fire-tv/overview/developing-apps-and-games-for-amazon-fire-tv)，改版迅速而流畅：**移动端和电视版的核心组件相同**，保持界面与应用底层结构分离，能让开发者**拥有足够的灵活性快速迭代**，在几周内成就完整的电视应用。

## Fire TV的界面革新

这款Fire TV应用发布一年多以后，从应用数据中收集了足够的用户操作反馈，TVPlayer开发者与设计师们决定，是时候为Fire TV应用创造一套**新界面**了。目的在于使应用更加高效，为电视用户提供最佳的内容呈现形式，同时在应用中加入新功能。


新的一版加入了按月订阅的应用内购——包含免费与付费内容，使应用更多样化。Simplestream的设计师进行了**深入的竞品分析，理解流媒体应用设计当前的趋势**，掌握了如何设计统一一致的界面，甚至是**跨越多平台与设备**。

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0--AkSc_NnXYNLbKrf.jpg)

## 选用合适的配色方案，确保应用对眼睛友好

首先，设计师决定探索Fire TV的**深色配色方案**。在设计上一版Fire TV应用时就做出了个决策，不过在这版界面更新中更进一步，把多数UI组件都加深了。**深色主题主要是为了防止浏览内容时眼睛疲劳**，因此能创造更轻松的用户体验。这对于应用的启动界面尤其重要，把它改成黑色，避免“亮瞎眼”。

> **让用户的眼睛免于疲劳。**

设计电视应用时，**浅色与亮色的主题需要慎重考虑**，因为多数可能的使用场景都发生在夜晚，没有自然光，因此**明亮的界面会损害用户体验**，久而久之导致应用被抛弃。通过色彩来**展现品牌**也非常重要。对于TVPlayer，**蓝色作为高亮色彩**，相比前一版，更有助于保持多平台的**品牌一致性**。蓝色表示免费内容，而粉色表示付费内容。

## 通过ViewPager进行内容翻页

TVPlayer的开发者们想要一套**极具表现力**的界面，但也希望保持**品牌辨识度**，并提供独一无二的用户体验。因此他们决定不遵循标准的[Android Leanback界面](http://developer.android.com/tools/support-library/features.html#v17-leanback)，他们建立了自己的**布局与导航系统**。

TVPlayer的**主体布局**对[ViewPager](http://developer.android.com/training/animation/screen-slide.html)组件进行了自定义。ViewPager是一种布局管理组件，可以在多页内容中轻松左右翻页。在TVPlayer中，通过**ViewPager的自定义运用**，实现了水平滚动翻页切换节目与频道，每一页都包含一系列自定义视图。

## 内容的快速入口增强粘性

上一版中创建的网格视图得到了改进，**每项有更大的间距**，并且**用水平滚动替代了垂直滚动**。同时也引入了快速内容导航：用户可以选中**翻页导航指示器**，在页面间快速滚动。翻页导航指示器与ViewPager相关联，决定了当前展现什么页面，下一页是什么。快速滚动意味着用户能更快触达更多内容，因此有助于增强用户粘性、加强记忆。

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-yEy2wOan57S_ShDy.PNG)

## 马赛克式界面：内容的快速入口，更加商业化

最终的结果是**马赛克式界面**，能快速到达各个频道。自定义Android视图和Adapter的使用，让开发者**能在一个界面中完全掌控和融合免费与付费内容**，改善了通向**应用内购**的高级内容入口，因此也创造了更多收入。TVPlayer从第一版完全免费的形式，变为**包含付费内容的新版本**。保持了干净的用户界面，将界面背后的逻辑与核心应用组件分离开，使得这次改版轻松而迅速，也保证了快速迭代来创造**优秀的用户体验**和**加强商业化**。

![](http://qiniu.colacdn.com/img/posts/2016-09/09-21/0-iHns9GwlNwn2BGyU.jpg)

## 马上开始创造Amazon Fire TV应用吧！

**Amazon Fire TV**和**Fire TV Stick**给你提供了绝佳的机会，让你的Android或HTML5应用能触达更多用户。只要遵循Amazon Appstore的开发者文档，把Android移动应用迁移到Fire TV上非常简单！这些链接会非常有用：

[Amazon Fire TV：把应用和游戏带到客厅，触达更多用户](https://developer.amazon.com/public/solutions/devices/fire-tv/overview/developing-apps-and-games-for-amazon-fire-tv)

[Amazon Fire TV应用与游戏开发入门](https://developer.amazon.com/public/solutions/devices/fire-tv/overview/getting-started-developing-apps-and-games-for-amazon-fire-tv)

[为Amazon Fire TV开发应用与游戏](https://developer.amazon.com/public/solutions/devices/fire-tv/overview/developing-apps-and-games-for-amazon-fire-tv)

---

原文链接：[https://medium.com/amazon-appstore/designing-native-android-apps-for-tv-how-tvplayer-designed-for-amazon-fire-tv-79c3801b60e7#.sinhtvmbx](https://medium.com/amazon-appstore/designing-native-android-apps-for-tv-how-tvplayer-designed-for-amazon-fire-tv-79c3801b60e7#.sinhtvmbx)

作者信息：[Mario Viviani](https://medium.com/@Mariuxtheone)
Technology Evangelist, Amazon Appstore