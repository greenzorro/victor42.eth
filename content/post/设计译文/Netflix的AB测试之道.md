---
title: Netflix的AB测试之道
description: 
image: 
date: 2016-08-28 00:53:10
categories: 设计译文-Design
url: /post/3519
---

**[国外设计第145期]**

![](https://cdn.victor42.work/posts/2016-08/08-27/netab-hero.jpg)

几周前，我在旧金山的[Yelp](http://blog.invisionapp.com/inside-design-yelp/)总部参加了一场[设计师与极客们的活动](http://www.eventbrite.com/e/designers-geeks-art-vs-science-ab-test-to-inform-design-tickets-26089495383#)Anna Blaylock和Navin Iyengar两位都是[Netflix](http://blog.invisionapp.com/inside-design-netflix/)的产品设计师，他们分享了自己多年在千万级用户群中做A/B测试的经验。他们也展示了相关的产品案例，帮助与会者思考自己的设计。

下面是我关于他们演讲做的记录，其中包含我最喜欢的一些精华。

[![Photo from the presentation.](https://cdn.victor42.work/posts/2016-08/08-27/netab-1.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netab-1.jpeg "How Netflix does A/B testing")

*演讲的照片*

## 实验

我非常喜欢PPT的第一页——*绝命毒师*里的这张图用得很聪明，能表现[实验](http://blog.invisionapp.com/genius-designer-mindset-experimentation/)的概念。

[![netab-2](https://cdn.victor42.work/posts/2016-08/08-27/netab-2.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netab-2.jpeg "How Netflix does A/B testing")

## 科学的方法

[![netab-03](https://cdn.victor42.work/posts/2016-08/08-27/netab-03.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netab-03.jpeg "How Netflix does A/B testing")

## 假设

在科学中，假设是指一个想法或一套解释，需要通过研究和实验来验证。在设计里，一套理论或猜想同样可以被称为假设。

[![netab-4](https://cdn.victor42.work/posts/2016-08/08-27/netab-4.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netab-4.jpeg "How Netflix does A/B testing")

假设的基本概念，是没有确定结果的。它经得起检验，这些测试也可以被重现。

*“[A/B测试](http://blog.invisionapp.com/ab-testing-beginners-guide/)背后的总体概念，是创造一套实验，有对照组和一个或更多实验组（在Netflix中这被称作‘单元’），对他们进行区别对待。在实验中，每个用户都属于唯一的单元，其中一个单元会被设计成‘默认单元’。这个单元代表着对照组，使用体验与所有没有加入实验的Netflix用户相同。”*——[Netflix技术博客](http://techblog.netflix.com/)

Netflix的A/B测试是这样进行的：随着测试启动，它们会记录特定的重要指标。例如播放时间和留存率之类的因素。一旦测试者得出足够有意义的结论，他们就会进一步观察每组实验的效果，定义出各个版本中的优胜者。

> [“A/B测试是研究用户行为最可靠的方式。”](https://twitter.com/intent/tweet?text=%22A%2FB+testing+is+the+most+reliable+way+to+learn+user+behaviors.%22+http%3A%2F%2Fblog.invisionapp.com%2Fhow-netflix-does-ab-testing%2F+-+%40lovejessiecat+via+%40InVisionApp)

[![netab-5](https://cdn.victor42.work/posts/2016-08/08-27/netab-5.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netab-5.jpeg "How Netflix does A/B testing")

[![netab-6](https://cdn.victor42.work/posts/2016-08/08-27/netab-6.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netab-6.jpeg "How Netflix does A/B testing")

## 实验

许多像Netflix这样的公司通过实验保障用户数据。同样重要的是，投入时间和精力合理安排实验，确保数据的种类和数量足以有效地阐明他们感兴趣的问题。

你可能会注意到，[Netflix首页](https://www.netflix.com/)的焦点区域似乎随着登录状态改变。它们都是Netflix复杂实验的一部分，让你观看他们的节目。

[![Homepage when I logged in the first time.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-7.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-7.png "How Netflix does A/B testing")

*我首次登录看到的首页。*

[![Image from the presentation: The House of Cards page as seen by a signed-out user.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-8.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-8.jpeg "How Netflix does A/B testing")

*PPT中的图片：用户注销后会看到纸牌屋的页面。*

[![Homepage when I logged in the second time.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-9.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-9.png "How Netflix does A/B testing")

*我第二次登录时看到的页面。*

[![Homepage when I switch to a different user name.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-10.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-10.png "How Netflix does A/B testing")

*我换了另一个账号登录看到的页面。*

[![Homepage when I switch the user to "kids."](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-11.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-11.png "How Netflix does A/B testing")

*我换了一个“儿童”账号登录看到的页面。*

[![Homepage when I’m not signed in.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-12.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-12.png "How Netflix does A/B testing")

*我未登录时看到的页面。*

A/B测试的概念，是向不同用户群呈现不同内容，收集他们的反应，通过结果来建立未来的策略。Netflix工程师[Gopal Krishnan](https://twitter.com/sgkrishnan)写的[这篇文章](http://techblog.netflix.com/2016/05/selecting-best-artwork-for-videos.html)里提到：“如果不在90秒内吸引一个用户的注意力，这个用户就很可能失去兴趣，去做其他的事情。这些失败的情况，往往是因为我们没有呈现正确的内容，或者我们呈现了正确的内容但没有提供足够的观赏理由。”

Netflix早在2013年做过一个实验，用来研究是否可以通过创造一些不同版本的作品，来提高某个标题的收视率。结果如下：

[![Image from the Netflix blog.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-13.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-13.png "How Netflix does A/B testing")

*图片来自[Netflix技术博客](http://techblog.netflix.com/2016/05/selecting-best-artwork-for-videos.html)*

Krishnan补充道：“这个信号很早提示我们，用户对于封面变化的敏感。这个信号也表明，还有更好的方式，可以通过Netflix的用户体验，帮助用户找到他们要的那一类故事。”

Netflix后来打造了一套[系统](http://techblog.netflix.com/2016/03/extracting-image-metadata-at-scale.html)，能自动根据纵横比、裁剪、润色和不同语言的同一张背景图为作品分组。他们在TV节目上也重复这个实验，用来追踪相关作品的表现。例子如下：

[![Image from the Netflix blog. The 2 marked images significantly outperformed all others.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-14.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-14.png "How Netflix does A/B testing")

*图片来自[Netflix技术博客](http://techblog.netflix.com/2016/05/selecting-best-artwork-for-videos.html)。两张带有标记的图片明显胜过其他版本。*

[![Image from the Netflix blog. The last marked images significantly outperformed all others.](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-15.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-15.png "How Netflix does A/B testing")

*图片来自[Netflix技术博客](http://techblog.netflix.com/2016/05/selecting-best-artwork-for-videos.html)。最后一张带标记的图片明显胜过其他版本。*

请看两篇博客文章，可以了解更多关于Netflix的A/B测试：

- [Netflix如何通过A/B测试选择最佳的视频封面](http://techblog.netflix.com/2016/05/selecting-best-artwork-for-videos.html)
- [Netflix实验平台](http://techblog.netflix.com/2016/04/its-all-about-testing-netflix.html)，一项由专门工程师团队支持的服务，使每一个Netflix工程师团队都能够进行A/B测试。

## 我的收获

A/B测试是研究用户行为的最可靠的方式。作为设计师，[我们应该通过实验的角度，思考自己的项目](https://twitter.com/intent/tweet?text=%22we+should+think+about+our+work+through+the+lens+of+experimentation.%22+http%3A%2F%2Fblog.invisionapp.com%2Fhow-netflix-does-ab-testing%2F+-+%40lovejessiecat+via+%40InVisionApp)。

[![Image from the presentation: Your instinct isn](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-16.jpeg?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-16.jpeg "How Netflix does A/B testing")

*PPT中的图片：你的直觉未必正确。*

[![netflixab-17](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-17.png?ver=1)](https://cdn.victor42.work/posts/2016-08/08-27/netflixab-17.png "How Netflix does A/B testing")

2. **何时以及为何进行A/B测试？**设计完工后，运用A/B测试调整设计细节，追求2项指标：留存率和收入。通过A/B测试，全产品全天候追踪用户，可以发你的改变是否提升了留存率或者增加了收入。如果没有，则采用默认方案。用这种方式，A/B测试可以持续用来提升业务指标。
3. **用户的需求和行为，是你希望的那样吗？**我的经验是，[通常，用户并不能像你期望的那样迅速完成一个任务](https://twitter.com/intent/tweet?text=%22often%2C+users+cannot+always+complete+a+task+as+fast+as+you+expect%22+http%3A%2F%2Fblog.invisionapp.com%2Fhow-netflix-does-ab-testing%2F+-+%40lovejessiecat+via+%40InVisionApp)。而且有时候，他们甚至找不到你放在页面上的某个特定的按钮。原因可能有很多种：设计不够直观；颜色不够鲜明；用户对技术陌生；他们不知道如何做决定，页面上太多选项；其他等等。
3. **你的直觉正确吗？**遗憾的是，涉及到用户行为时，我们的直觉可能是错的——唯一的证明方法就是通过A/B测试。A/B测试是检验哪种用户体验设计更加有效的最佳方案。在工作中，我们的用户产品团队，就通过A/B测试在我们的房地产网站上得到了验证。比如，他们想了解是否可以通过设计改进，来提高用户点击Google广告的注册率。他们创造了几个不同的实验性设计，对它们进行测试。他们认为那些去掉了房产图片的设计会胜出，但最终发现去掉房产图片和价格信息的转化率最高。
    > [“了解用户是设计过程中最令人兴奋的部分。”](https://twitter.com/intent/tweet?text=%22Knowing+your+user+is+the+most+exciting+part+of+the+design+process.%22+http%3A%2F%2Fblog.invisionapp.com%2Fhow-netflix-does-ab-testing%2F+-+%40lovejessiecat+via+%40InVisionApp)
5. **探索边界。**最佳创意来自任何的创意探索。在工作中，我们的产品团队[协作](http://blog.invisionapp.com/collaboration-and-great-products/)进行许多项目。由于牵扯到太多方面（从设计师到产品经理，再到[开发者](http://blog.invisionapp.com/design-with-developers-in-mind/)），我们必须一起探索边界。测试了我们的原型之后，有些最佳创意来自开发者或产品经理。
6. **观察人们的行为，忽略他们的言辞。**与用户交谈时，牢记一点：*他们总是言行不一。*我这周发起了一些[用户测试](http://blog.invisionapp.com/user-testing-guide/)，有充分的理由告诉你为什么。我让一个用户试用联系人列表界面的原型，我问他会不会经常排序和过滤联系人。他说不会，因为他不需要。但是当他发现新的下拉筛选菜单，他感到很惊奇，原来同时排序和筛选多个选项如此方便——然后他马上问产品什么时候上线这个功能。
7. **用数据来估计机会大小。**一切都在于*为什么*。[数据可以支撑创意成型。](https://twitter.com/intent/tweet?text=%22Data+can+help+shape+ideas.%22+http%3A%2F%2Fblog.invisionapp.com%2Fhow-netflix-does-ab-testing%2F+-+%40lovejessiecat+via+%40InVisionApp)

了解用户是设计过程中最令人兴奋的部分。设计没有成品，许多的改版和迭代可以改进设计，给用户带来尽可能好的体验。

*本文最初发布在[Medium](https://uxdesign.cc/how-netflix-does-a-b-testing-87df9f9bf57c#.iha9zwglj)。*

## 相关文章

- [内在设计: Netflix](http://blog.invisionapp.com/inside-design-netflix/)
- [通过A/B测试提升转化率](http://blog.invisionapp.com/improving-conversion-rates-ab-tests/)

---

原文链接：[http://blog.invisionapp.com/how-netflix-does-ab-testing/](http://blog.invisionapp.com/how-netflix-does-ab-testing/)

作者信息：[Jessie Chen, UI/UX Designer](http://blog.invisionapp.com/author/jessie-chen-uiux-designer/)
Jessie Chen currently works at [ZapLabs](http://zaplabs.com/), where she designs a CRM for real estate professionals. She enjoys gathering user feedback through user testing, and iterating on design ideas to solve usability issues. In her spare time, she shares ideas on [Medium](https://medium.com/@lovejessiecat) about how design impacts businesses. 
[Follow me on Twitter](https://twitter.com/lovejessiecat)