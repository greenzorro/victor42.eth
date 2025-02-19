---
title: 乐观派UI：真实的谎言
description: 
image: 
date: 2016-11-27 16:08:31
categories: 设计译文 Design
url: /post/3531
---

**[国外设计第155期]**

想象3个用户界面（UI）一起去了酒吧。第1个点了一杯酒，然后又再点了几杯。几小时后，它买了单，醉醺醺的走了。第2个界面点了一杯酒，直接把钱付了，然后又点了一杯酒，又马上买了单，几小时后也醉醺醺的离开了酒吧。第3个界面刚走进酒吧，马上就已经醉醺醺的离开了——它知道酒吧是干什么的，它非常讲求效率，一点时间也不浪费。你听说过这第3种界面吗？它就叫做“乐观派UI”。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui-large-opt-1.png)

*乐观派UI设计并非乐观地看待页面——至少不**仅限于此**。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui-large-opt-1.png)）*

我最近参加了许多关于前端开发和用户体验的会议，讨论了[心理表现最佳化](https://vimeo.com/184659742)，我很惊讶，乐观派UI设计是业界一个如此微不足道的话题。坦白说，这个术语本身都没有清晰的定义。本文中，我们来探讨它的基本概念，寻找一些案例，并回顾它的心理学背景。然后，我们讨论掌握这项用户体验技巧的关键。

开始之前，我得说，没有任何一个单独的界面能被称作“乐观派UI”。其实它是界面实现背后的心智模型。乐观派UI设计有它自己的历史和逻辑。

## 很久以前

很久以前——那时候“tweet”一词还只有鸟鸣的意思、苹果公司濒临破产、人们还会把传真号码印在名片上——网页界面相当单调。其中绝大多数没有一丝一毫的乐观意味。比如一个按钮的交互，可以遵循下面类似剧本来进行：

1. 用户点击一个按钮。
2. 按触发进入禁用状态。
3. 一条请求发送到服务器。
4. 服务器返回信息到页面。
5. 页面刷新，反映出返回的状态。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/old-ui-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/old-ui-large-opt-1.png)

*那个年代，界面与乐观派扯不上什么关系。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/old-ui-large-opt-1.png)）*

站在2016年回顾这些，我们会觉得效率低下；但是相当惊人的是，同样的剧本仍然在许多网页和应用中上演，它仍然是许多产品的交互流程。原因在于它可以预测，而且或多或少总会出点错误：用户知道这项操作已经请求了服务器（禁用状态的按钮表明了这一点），当服务器有响应，更新后的页面清晰表明这种客户端——服务器——客户端的交互结果。这种交互方式的问题很明显：

- 用户必须等待。如今我们都知道，即使是最短的服务器响应延迟，也会对整个品牌，而非这个单独页面产生[负面的用户感知](https://blog.radware.com/applicationdelivery/applicationaccelerationoptimization/2013/12/mobile-web-stress-the-impact-of-network-speed-on-emotional-engagement-and-brand-perception-report/)。
- 每一次用户的操作得到响应，都会以一种相当破坏性方式呈现（整页刷新，而不是更新现有部分），会打断用户的任务流程，可能影响他们的[思维轨迹](https://en.wikipedia.org/wiki/Train_of_thought)。 我们甚至还没说到[多任务](http://www.apa.org/research/action/multitask.aspx)，心理环境的任何变化都令人不愉快。那么，如果某个操作本意不是改变环境（在线支付就是个需要改变环境的好例子），那么这种改变会在用户与系统的交流中创造不友善的氛围。

## 不久以前

然后，所谓Web 2.0出现了，提供了新的页面交互模式。它的核心是XMLHttpRequest和AJAX。一种最简单的进度条形式：“菊花”，补足了这些新交互模式，它的基本目的就是告诉用户，系统正忙着处理事情。现在，服务器返回信息后，我们不必刷新页面了；我们只需要对已经渲染的页面进行局部更新。这使得网站更加动态化，为用户创造了更加顺畅和亲切的体验。一个按钮的典型交互如今是这样的：

1. 用户点击按钮。
2. 按钮触发变为禁用状态，按钮上显示出某种菊花图形，表明系统正在运转。
3. 请求发送到服务器。
4. 服务器返回信息到页面。
5. 根据返回的状态更新按钮和页面的视觉状态。

这种新的交互模型解决了旧交互方式存在的一个问题：页面的刷新不会导致破坏性操作，保持用户所处环境不变。相比之前，这种交互亲切多了。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/spinner-ui-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/spinner-ui-large-opt-1.png)

*XMLHttpRequest和菊花解决了旧交互方式的一个问题：服务器响应会导致破坏性的刷新，改变整个环境。([查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/spinner-ui-large-opt-1.png))*

这种交互模式已经广泛应用于数字媒介。但还有一个问题：用户仍然需要等待服务器反馈。当然，我们有办法加快服务器响应速度，但无论我们如何努力优化基础设备，用户仍然要等待。比如，[研究表明](http://www.techradar.com/news/world-of-tech/roundup/consumers-dump-slow-websites-1080742)78%的用户对于缓慢或不稳定的网站产生负面情绪。更有甚者，Harris Interactive为Tealeaf做的一份[调查显示](http://www.marketwired.com/press-release/tealeaf-announces-new-mobile-transaction-research-conducted-harris-interactive-shows-1419058.htm)，23%的用户承认咒骂过自己的手机，11%冲自己手机大喊过，而且4%的用户在网络出问题时扔过手机。延迟就属于这类问题之一。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/cursing-phone-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/cursing-phone-large-opt.png)

*大约78%的用户面对缓慢或不稳定的网站时，会产生负面情绪。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/cursing-phone-large-opt.png)）*

即使在用户等待时展示某种进度条，如今也于事无补，除非[进度条非常有创意](https://dribbble.com/shots/1901531-Loading)。多数情况下，人们已经习惯性把菊花进度条当作系统缓慢的表现。菊花如今已经是一种[纯粹的被动等待](https://www.smashingmagazine.com/2015/11/why-performance-matters-part-2-perception-management/)，用户毫无选择，要么等待服务器响应，要么关闭标签页或整个应用。那么，我们再进一步，改善这种交互；我们来看看乐观派UI的概念。

## 乐观派UI

正如前文所说，乐观派UI仅仅是处理人机交互的一种方式。要理解它背后的核心观念，我们还是要回到“用户点击按钮”这个场景。不过它的原则用在任何乐观派交互上都一样。[牛津英文词典的解释如下](https://books.google.com/books?id=mYicAQAAQBAJ&lpg=PA503&dq=%22hopeful+and+confident+about+the+future%22&pg=PA503&redir_esc=y#v=onepage&q=%22hopeful%20and%20confident%20about%20the%20future%22&f=false)：

> **乐观主义**，*形容词*，对于未来充满希望和信心。


我们从“对未来充满信心”这部分说起。

想一想：用户操作引发服务器错误的频率高么？比如说，用户点击按钮时，你的API经常出错吗？或者用户点击某个链接时经常会出错？说实话我觉得不会。当然，API、服务器载荷、错误处理等级不同，表现也不一样。还有一些其他因素，作为前端开发或者用户体验专家，你可能不会考虑。但只要API稳定可靠，前端以适当方式反馈正确的UI操作，那么由用户触发导致的问题会特别少。以目前状况来看，我敢说不会超过1%到3%。这就意味着97%到99%的状况下，用户点击网站的某个按钮，服务器的响应应该是成功的，没有错误。应该从一个更好的角度来看待这个问题。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/failure-success-man-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/failure-success-man-large-opt.png)

*乐观派UI基于一个假设，用户点击按钮，服务器在97%到99%以上的状况下返回成功。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/failure-success-man-large-opt.png)）*

仔细想一想：如果97%到99%以上肯定是成功的响应，我们对于反馈就有充足信心——嗯，至少比薛定谔的猫有信心多了。我们就可以写出一个全新的按钮交互剧本：

1. 用户点击按钮。
2. 按钮的视觉状态立刻变为成功。

就是这样！至少从用户的角度来看，仅此而已——不用等待，不用盯着禁用状态的按钮，也没有烦人的菊花转。交互流畅无缝，系统不会粗暴地现身，提醒用户注意它的存在。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui1-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui1-large-opt.png)

*乐观派UI交互里根本没有禁用状态按钮和菊花。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui1-large-opt.png)）*

从开发者的角度来看，完整的流程是这样的：

1. 用户点击按钮。
2. 按钮的视觉状态立刻变为成功。
3. 请求发送到服务器。
4. 服务器响应发回页面。
5. 在97%到99%的状况下，我们知道响应会成功，所以不用再给用户添麻烦。
6. 系统只会在请求错误的情况下现身。暂时不用担心这块——我们会在后文中讲到。

我们来看一些乐观派交互的案例。你可能很熟悉“点赞”按钮，Facebook和Twitter上就有。我们来看看Twitter的。

很明显，从点击按钮开始。但是请注意用户松开并移开鼠标时按钮的状态。它立刻变成了成功状态！

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter1-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter1-preview-opt.png)

*点了赞之后，Twitter立刻把它更新为成功状态。*

此时，我们用浏览器开发人员工具，看看里面的“网络”标签栏发生了什么。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter2-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter2-large-opt.png)

*按钮的视觉状态改变，独立于服务器请求存在，此时服务器请求正在进行中。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter2-large-opt.png)）*

“网络”标签表明，服务器请求已经发送，但正在处理中。“赞”计数器还没有增加，但由于颜色变了，界面上已经清晰表明了点赞成功，甚至服务器都还没有给出反馈。

服务器返回成功的响应后，计数器增加，但这个变化比色彩改变微弱得多。这就给用户提供了一种流畅连贯的体验，感觉不到任何等待。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter3-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter3-large-opt.png)

*尽管赞按钮在视觉上已经变为成功状态，计数器只在服务器响应确认成功后才变化。*

在Facebook可以看到另一个乐观派交互的例子，也是点赞按钮。场景非常相似，不过Facebook是连着计数器一起直接变为了成功状态，完全没有等待服务器响应。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/fb-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/fb-preview-opt.png)

*Facebook用了和Twitter一样乐观派交互，但它连着计数器一起更新了视觉状态。*

但有一点要注意。如果我们观察服务器响应时间，会发现它大约在**1秒多**。考虑到[RAIL模型建议](https://developers.google.com/web/fundamentals/performance/rail?hl%3Den%23response_respond_in_under_100ms)采用**100毫秒**作为简单交互的最佳响应时间，相比之下1秒显得太长了。但是，用户感知不到任何等待，因为这种交互天然的乐观属性。非常棒！这是[**心理**表现最佳化](https://www.smashingmagazine.com/2015/11/why-performance-matters-part-2-perception-management/)的又一个例子。

但我们要面对现实：仍然有1%-3%的可能服务器会返回错误。或者有可能用户断线了。又或者一种更有可能的情况，服务器在技术上返回了成功状态响应，但是这个响应仍然需要客户端进一步处理。因此，用户看到的不是失败提示，但我们也不能认为响应是成功状态。要了解如何处理这种状况，我们首先要了解乐观派UI在心理学上为何能起作用。

## 乐观派UI背后的心理学

目前为止，我还没有听谁抱怨过主流社交媒体上的乐观派交互，就是我们之前提到的那种。那么，我们可以说这些例子已经证明，乐观派UI是有用的。但为什么它们有用？这仅仅是因为人们讨厌等待。仅此而已啊，亲！你可以直接跳到下个章节了。

不过如果你继续往下读，说明你对深层原因感兴趣。那么，我们稍微深入一点，了解这种方式的心理学基础。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/psychology-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/psychology-large-opt.png)

*大脑研究帮助我们理解乐观派UI起作用的心理学成因。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/psychology-large-opt.png)）*

乐观派UI有两个值得心理学分析的要素：

- 用户行为的快速响应；
- 服务器对于潜在错误的处理，无论是网络还是其他方面。

### 用户行为的快速响应

我们谈论乐观派UI设计时，我们谈的其实是人机交互中的最佳响应时间。早在1968年，这类交互就有了相关建议。当时，Robert B. Miller发表了他的开创性研究“[人机对话的响应时间](https://www.computer.org/csdl/proceedings/afips/1968/5072/00/50720267.pdf)”（PDF），他在其中定义了不同类型的响应，用户可能从计算机得到的反馈多达17种。Miller将其中一种称为“控件操作响应”——按下按钮到得到视觉反馈的时间。甚至早在1968年，就规定了它不应该超过0.1-0.2秒。是的，这并不是[RAIL模式](https://developers.google.com/web/fundamentals/performance/rail)首创——这个建议大约已经存在了50年。但是，Miller注明了，对于熟练的用户而言，这么短的延迟都可能太慢了。这就意味着，理想情况下，用户应当在**100毫秒**内获得操作的反馈。这就接近人体最快的潜意识动作——眨眼。因此，100毫秒的间隔给人感觉通常就是瞬间。“多数人每分钟眨眼大约15次，一次眨眼平均持续100到150毫秒”，伦敦城市学院神经学创立者[Davina Bristow说](http://www.ucl.ac.uk/media/library/blinking)，他还补充说：“这意味着我们每年有9天花在眨眼睛上。”

正由于瞬间的**视觉**响应（甚至在实际请求完成之前），乐观派UI在心理表现最佳化中，是一种[已经完善](https://www.smashingmagazine.com/2015/11/why-performance-matters-part-2-perception-management/)的技巧。但事实上，那些人们喜爱的能在眨眼间响应的界面，对我们而言应该不算惊喜，真不算。而且这也不难做到。即使在很早以前，我们在用户点击按钮后，会将它变为禁用状态，这通常就足以表明用户的输入了。只不过，界面中的禁用状态意味着[被动等待](https://www.smashingmagazine.com/2015/11/why-performance-matters-part-2-perception-management/)：用户什么也做不了，无法掌控整个过程。这对用户而言很令人扫兴。这就是为什么我们在乐观派UI中直接跳过了禁用状态——我们不让用户等待，直接给他积极的反馈。

### 处理潜在错误

现在我们进入乐观派UI设计中的第二个有趣的心理学问题——处理潜在错误。一般来说，有大量信息和文章讲述如何以最恰当的方式处理UI错误。但是，本文中讨论的错误处理，在乐观派UI中，最重要的不是如何处理错误，而是什么时候处理。

人们天生会把行为聚类处理，以主观定义的目标或者小目标达成为结束。有时候我们把这些聚类称作“[思维轨迹](https://en.wikipedia.org/wiki/Train_of_thought)”、“[思维涌动](http://www.unco.edu/cebs/psychology/kevinpugh/motivation_project/resources/flow6.pdf)” (PDF)，或者就简单称作“[心流](https://en.wikipedia.org/wiki/Mihaly_Csikszentmihalyi%23Flow)”。心流状态的特征包括乐趣达到巅峰、精力集中、创造力爆发。在心流状态中，用户完全被这项活动吸引。[Tammy Everts的一条推特](https://twitter.com/tameverts/status/783800032436695040)准确描绘了这点：

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/tammy-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/tammy-large-opt.png)

【图注：我喜欢心流状态的一切，除了一点，我会连续几个小时忘记眨眼。我的眼睛现在是这样的。】

*有时候，辨认出一个人是否处于心流状态非常简单。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/tammy-large-opt.png)）*

在网络中，这些活动聚类的持续时间短得多。我们回顾一下Robert B. Miller的作品。他指出，响应类型包括：

- 粗略浏览列表信息的响应；
- 仔细浏览图表信息的响应；
- “系统，你明白我要什么吗？”的响应。

他把这几类都归为**2秒**延迟的类型，用户会获得相应类型的响应。如果不继续深究，我们应该注意，这些延迟也取决于一个人的[记忆运转](http://www.simplypsychology.org/working%20memory.html)（这是指一个人记住一定量信息所需的时间，更重要的是，不仅记住，还要能运用）。我们作为开发者和用户体验专家，这意味着在操作了某个元素的2秒内，用户会短暂进入心流状态，专注于他们期待的响应。如果服务器在这个时间内返回错误状态，用户仍然处于与界面的“对话”中，这是个比喻。类似于两个人对话，比如你说了一句话，对方委婉地反驳你。想像一下，如果对方花了很长时间点头表示同意（等同于我们UI中的成功状态），但然后最终对你说“不”。这多尴尬啊？所以，乐观派UI必须在心流状态的2秒内传达出错误信息。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui2-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui2-large-opt.png)

*乐观派UI必须清楚表达错误状态给用户。最重要的是，它要在用户进入心流状态的2秒内发生。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/optimistic-ui2-large-opt.png)）*

现在我们掌握了这项心理原则，用来处理乐观派UI中的错误，下面我们就开始面对那1%-3%的失败请求吧。

## 乐观派UI的悲观一面

目前为止，我听到最多的言辞，是说乐观派UI是一种黑魔法——作弊，如果你这么想也对。也就是说，运用这种方式，我们就是在对用户撒谎，编造他们操作的结果。从法律上说，每个法庭可能都会认同这一点。但我仍然把这种技巧当作一种预期或是希望。（记得“乐观”的定义吗？我们在这里允许某些“希望”存在。）“撒谎”与“预期”的区别在于你如何对待那1%-3%的失败请求。我们来看看Twitter的乐观派“点赞”按钮在离线状态下的表现。

首先，点击按钮后它立刻变为成功状态，这符合乐观派UI模式——当用户松开并移开鼠标，它的表现和用户处于在线状态时一样。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline1-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline1-large-opt.png)

*离线状态下，Twitter的点赞按钮仍然在点击后产生视觉变化。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline1-large-opt.png)）*

但由于用户离线，请求失败了。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline2-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline2-large-opt.png)

*（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline2-large-opt.png)）*

那么，在用户进入心流状态后，错误信息要尽快给出。2秒通常是心流的持续时间。Twitter以一种非常微妙的方式表达这一点，把按钮的状态还原回去了。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline3-preview-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline3-large-opt.png)

*请求失败后，Twitter以一种低调的方式还原了按钮的视觉状态，没有在视觉上小题大做。（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/twitter-offline3-large-opt.png)）*

认真的读者会说，失败处理还能更进一步，准确告知用户请求没有发送出去，由于发生了某个错误。这就让系统尽可能保持隐形。但还有一系列问题：

- 屏幕上忽然出现的任何形式的通知，会改变用户的环境，刺激他们去分析失败背后的原因，但这个原因在错误信息中可能已经说明了。
- 就像所有错误信息或通知一样，它应该也要引导用户进入新的环境，提供相应的操作信息。
- 操作信息又会进入一个新的环境。

好吧，可能大家都觉得这开始有点复杂了。因为这样的错误处理对于网站的大型表单有意义，但对于像点击按钮这么简单的事情，它就杀鸡用牛刀了——对于所需的技术开发，还有用户的记忆运转，都太过了。

所以，没错，我们对乐观派UI中的失败要有开放心态。我们要尽快告知用户，保证乐观主义不会发展成谎言。但它应当与环境相称。对于点赞失败，还原按钮状态这样的微小提示足够了——也就是说，除非用户点击的是其他极其重要的状态，需要保证它时刻运转正常。

### 极端悲观

这就产生了另一个问题：如果用户获得成功的反馈，但是在服务器响应之前就关闭了浏览器标签页，怎么办？最讨厌的情况是，用户在请求发送到服务器之前就关闭了标签页。但除非用户极其敏捷，或者有本事减慢时间，这种情况很难发生。

如果乐观派UI运用得当，所有对于各元素的操作都在2秒内得到服务器反馈，那么用户就得在2秒内关闭浏览器标签页。这对于快捷键而言并不难；但是我们知道，97%-99%情况下，请求是成功的，无论标签页是否激活（只是响应没有发送回客户端而已）。

所以，只有对于那1%-3%的服务器错误，这才算一个问题。然后，有多少人在2秒内匆匆关闭页面？除非他们在比赛关闭标签页，我觉得这个数量没有什么意义。但如果你认为这个关系到特定的项目，可能会导致糟糕的后果，那就应该用一些工具来分析用户行为；如果这种场景存在的可能性足够高，就把乐观派交互限定在非重要元素上。

我有意没有提及那些故意延迟的请求；这些不在乐观派UI设计的范畴内。而且，我们在悲观方面讨论得已经够多了，现在我们来总结一下运用乐观派UI的核心要点。

## 经验法则

我真诚地希望，这篇文章能帮助你理解乐观派UI设计背后的核心观念。可能你很希望在下一个项目中运用这种方法。那么，开始前请牢记这些：

- 我们所有这些讨论的前提：你所依靠的API足够稳定，能够返回可预期的结果。这点无需多言。
- 界面要在向服务器发送请求*之前*，找出可能的错误和问题。最好能够完全去除可能会导致API返回错误的因素。UI元素越简单，越容易运用乐观派UI。
- 在简单的是非选项上运用乐观派模式，只有成功与失败两种响应的元素。例如一个按钮的服务器返回状态包含“是”、“否”、“有可能”（每一种都代表了不同程度的成功），这种按钮就不适合用乐观派模式。
- 了解API的响应时间。这点至关重要。如果你知道某个特定请求的响应时间一定在2秒以上，首先应该优化API到最佳性能。之前提到，服务器响应时间在2秒以内，乐观派UI才有最佳表现。超过2秒会导致难以预期的结果，用户会更加挫败。千万注意。
- 乐观派UI不仅仅是点击按钮。这种方式可以运用于页面中的各种不同交互，包括页面的加载。例如[框架页面](http://www.lukew.com/ff/entry.asp?1797)就运用了相同的观念：你预期服务器能成功返回信息，所以直接向用户先展示占位符。

[![](https://www.smashingmagazine.com/wp-content/uploads/2016/11/finish-650-opt.png)](https://www.smashingmagazine.com/wp-content/uploads/2016/11/finish-large-opt.png)

*（[查看大图](https://www.smashingmagazine.com/wp-content/uploads/2016/11/finish-large-opt.png)）*

看得出来，乐观派UI设计并不是网页中的新奇事物，也不是什么先进技巧。这只是另一种方式，另一种心智模型，帮助你掌控产品的[预期表现](https://www.smashingmagazine.com/2015/09/why-performance-matters-the-perception-of-time/)。乐观派UI设计基于人机交互的心理学基础，聪明地运用它，能够帮你的网站树立更好更流畅的体验，同时，需要做的其实很少。但是，为确保这种模式真正有效，避免产品向用户撒谎，我们必须理解乐观派UI设计的原理。

### 资源

- “[人机对话的响应时间](http://theixdlibrary.com/pdf/Miller1968.pdf)” (PDF), Robert B. Miller, Fall Joint Computer Conference, 1968
- “[RAIL简介：以用户为中心的表现模型](https://www.smashingmagazine.com/2015/10/rail-user-centric-model-performance/),” Paul Irish, Paul Lewis, Smashing Magazine, 2015
- “[移动端网页的压力：网速对于情绪与品牌认知的影响](https://blog.radware.com/applicationdelivery/applicationaccelerationoptimization/2013/12/mobile-web-stress-the-impact-of-network-speed-on-emotional-engagement-and-brand-perception-report/),” Tammy Everts, Radware Blog, 2013
- [*心流在人类发展与教育中的应用*](http://www.springer.com/gp/book/9789401790932), Mihaly Csikszentmihalyi, 2014
- “[移动端设计细节：避免转菊花](http://www.lukew.com/ff/entry.asp?1797),” Luke Wroblewski, 2013
- “[性能的重要性，第2部分：感知的掌控](https://www.smashingmagazine.com/2015/11/why-performance-matters-part-2-perception-management/),” Denys Mishunov, Smashing Magazine, 2015

---

原文链接：[https://www.smashingmagazine.com/2016/11/true-lies-of-optimistic-user-interfaces/](https://www.smashingmagazine.com/2016/11/true-lies-of-optimistic-user-interfaces/)

作者信息：[Denys Mishunov](https://www.smashingmagazine.com/author/denysmishunov/?rel=author)
Denys is a frontend developer living and working in Norway while advocating psychological optimizations around the world. Since the beginning of 00's he has gained experience with a wide range of frontend tasks. Being originally on "CSS side" of development, for the last years Denys has been building javascript applications, continuing breaking CSS, abusing HTML and working with optimization of pretty much all aspects of the frontend at Digital Garden AS ([fastname.no](https://www.fastname.no/) and [uniweb.no](https://www.uniweb.no/)). Passionate about science, history, psychology, in his day-to-day job Denys enjoys getting to the heart of the matter of things and processes. Cycling, photography, impressionist paintings and many more can trigger his attention.