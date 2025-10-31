---
categories: 折腾与思考-Geek
date: 2025-10-31 15:46:00
description: 猛然发现，现在真的能用Agent解决实际问题了，不再是玩具。
image: https://cdn.victor42.work/posts/2025-10/fa3e1420ce5ad04750a70cf47af3b382.webp
title: AI Agent真的已经今非昔比了
url: /post/ai-agent-evolution
translationKey: ai-agent-evolution
---

Manus那一波Agent概念火过之后，当时拿各种真实的复杂任务去测试，包括生成PPT，离解决实际问题还有一段距离。今天，情况是否不同了？值得再研究一次看看。

## AI Agent的各种形态和任务

最近AI浏览器也引人关注，加上Kimi K2/GLM 4.6/Minimax M2这些以Agent能力见长的模型出现，我认真思考了一下Agent在现实应用中的方向。

![](https://cdn.victor42.work/posts/2025-10/5c1dfd280ced698aafb769fda72f1bbb.webp)

> 趁着AI浏览器热潮，想了想Agent在数字世界里面临的挑战。其实现在能做好所有任务的模型和产品还没有出现，每一类任务都有它独特的要求。
> 
> 就像Chat bot一样，Agent工具也不是一招鲜吃遍天的，手边总要有好几个不同产品应对不同问题。
> 
> 目前相对成熟的是左上和右下，因为Web去中心化，而OS中心化。

其实，AI浏览器也好，Claude Code也好，Manus也好，本质是同类的东西。让AI控制一个相对完整的浏览器沙盒/本地环境，使用不同能力完成复杂耗时的任务。

既然Kimi/GLM/Minimax这些模型有比较出色Agent能力，它们的官方产品是否已经运用这些能力，来把自家产品推向一个更高层面，跳出国外模型大厂和国内互联网大厂的产品竞争？

一看发现确实如此，是我后知后觉了。海外AI四大和国内互联网大厂的AI入口产品，都没有提供完整的Agent能力，最多只是 Deep Research。如果撇去图片和视频的生成能力，仍然是纯纯的Chatbot。

但 Kimi/GLM/Minimax 的产品其实都提供了完整的Agent能力。Kimi的是OK Computer，GLM(Z.ai)的是Full-Stack，Minimax的开启Pro模式就是了。

Agent能力的加入，有希望让它们成为我日常主力AI产品吗？

## 3道测试题

正好，我平时整理保存了一些曾给AI处理的任务，用以测试Agent产品的能力：

1. 中国空军当前的战斗机序列是什么样的？帮我找出主流的机型，并且每个机型去网上找来各种角度的图片。
2. 做一份图文并茂的关于地球地质年代历史的分享报告，最好是PPT形式。
3. [http://victor42.eth.limo/](http://victor42.eth.limo/) 这是我的个人网站，我想看看我的个人信息泄露情况。你尽可能多地从网络上找到我的隐私信息，看看关于我能知道些什么。

先说结论：有进步，几乎达到可用水平，但仍然无法脱离人类的一步步指导和纠偏。

### 第1题：空军战机序列

第1题，Kimi的回答算是比较完整的成果。我不是军迷，其中数据和信息没去验证过，但这照片一看就知道不对，许多机型都搞混了。

![](https://cdn.victor42.work/posts/2025-10/40e4a3eb557ad47cabef41d1377717db.webp)

Kimi的输出：[https://sbudgp6km5i3s.ok.kimi.link/](https://sbudgp6km5i3s.ok.kimi.link/)

GLM的测试结果我都不太想放上来。它直接用AI给我生成了战机图片，我多次抗议后，自欺欺人地在风景图旁边标了“真实图片”，还用风景图代替了战机照片。

![](https://cdn.victor42.work/posts/2025-10/3ed522e94a089a5b9c9158c4836f881b.webp)

Minimax输出是真慢，另外两家全都测完了，它第一题才出来。但页面效果不错。而且它战机图片的匹配度是3个里最高的。

![](https://cdn.victor42.work/posts/2025-10/385decfa3e267bfa37e7af17546341a1.webp)

![](https://cdn.victor42.work/posts/2025-10/7db3981e98107c26649e0b6590cdfdba.webp)

Minimax的输出：[https://nycqzyogwce4.space.minimaxi.com/](https://nycqzyogwce4.space.minimaxi.com/)

### 第2题：地质年代报告

地球地质PPT，我的预期是它们用编程能力创作HTML格式的PPT。其中GLM提供PPT模式，我看了下，原理确实是生成HTML再转PPT。但我故意选了Full-Stack模式来创作，因为我就想看看通用Agent在这种任务上能做到什么程度。

这道题由于不太依赖网络资料，模型自身知识可以覆盖大部分信息，Kimi和GLM都顺利完成。GLM生成的是HTML，没有PPT格式。Minimax的Agent实在输出太慢了，等不了了，没有测它。

![](https://cdn.victor42.work/posts/2025-10/fa3e1420ce5ad04750a70cf47af3b382.webp)

![](https://cdn.victor42.work/posts/2025-10/6d9851b72af506f3b9cdce71a715115d.webp)

Kimi的输出：[https://qvokpfxqsh.feishu.cn/file/Sdz0bwNffoAFXKxqyItc4WNenwc?from=from_copylink](https://qvokpfxqsh.feishu.cn/file/Sdz0bwNffoAFXKxqyItc4WNenwc?from=from_copylink)

![](https://cdn.victor42.work/posts/2025-10/31d44ae8c1fcfa671416ff8a91cd7a88.webp)

![](https://cdn.victor42.work/posts/2025-10/2eac5f87eb6242cbba7fa4902f63f7ec.webp)

GLM的输出：[https://p0r7a94j92w1-deploy.space.z.ai](https://p0r7a94j92w1-deploy.space.z.ai)

还是老问题，全是AI图。

### 第3题：个人隐私信息泄露研究

第3题其实各家产品的Deep research也能做，但也拿来试一下，考验Agent规划任务全面收集信息的能力。这其实考验的是模型的基础能力，而非Agent能力。最后输出什么样的东西我不在意，我只看内容。

Kimi给了我一个形式花哨的报告，但内容空洞了些，信息收集不够深入。

![](https://cdn.victor42.work/posts/2025-10/ea5d6775e7457ca7b7bebd420db5d4a8.webp)

Kimi的输出：[https://dgkenxfkgs2to.ok.kimi.link/](https://dgkenxfkgs2to.ok.kimi.link/)

GLM则出于安全原因拒绝执行任务，拒绝了2次。

Minimax给了一份markdown文档，但内容很详实。可以看到它对很多信息专门做了独立研究，然后才整合出这份报告。

![](https://cdn.victor42.work/posts/2025-10/a4ce5062078b84188a2a0fd19a2ec725.webp)

GLM的输出：[https://agent.minimaxi.com/share/328823906788332?chat_type=0](https://agent.minimaxi.com/share/328823906788332?chat_type=0)

作为对比，贴一个非Agent产品对第3题的回答，来自Grok：[https://grok.com/share/bGVnYWN5LWNvcHk%3D_acd6451b-b37a-405e-a700-91d692edaac6](https://grok.com/share/bGVnYWN5LWNvcHk%3D_acd6451b-b37a-405e-a700-91d692edaac6)
可以看出在复杂任务上，即使不涉及独有的工具调用能力，Agent也比Chatbot走得更远。

其实Kimi/GLM/Minimax这3家官方产品里的Agent，如果你换成用Claude Code接他们家API，在本地执行，过程资料和最终结果存本地，也能达到差不多的效果。只是AI运行的环境从云端Linux变成了你自己的Windows/Mac。

所以说各种形态的Agent产品本质还是相同的。

## 在非标准化任务中的作用

再回顾一下象限图，以上测试的还只是右边两个象限，Agents面临的任务主要是本地文件操作、网络请求这类标准化任务。

![](https://cdn.victor42.work/posts/2025-10/5c1dfd280ced698aafb769fda72f1bbb.webp)

标准化任务的特点是，只要按正确的方式去做，就能得到确定的结果。

今天的这类Agents，已经大有可为。只要你自己清楚某件事正确的做法，它们能帮大忙。

但象限图左半边的任务就模糊地多。让AI通过非标准的图形界面操作网页和本地应用，会得到什么结果，任务能否完成，无法预知。所以这方面成熟度相对低很多，也还没有出现真正的杀手级产品。

即使前有Dia/Comet，后有Atlas，都没有改变这个局面。

理解图形界面不能光靠读HTML，要有优秀的视觉能力配合。而且最好是一个Stream持续传输给AI，相当于各家AI产品的视频电话功能。

否则，在页面上找个特定入口都能找几分钟。

但这样的开销哪是轻轻松松能开放给所有人使用的？

即使这样，在特定情况下，Agents也能在非标准化任务上帮大忙。

最近在研究东南亚的度假海岛。第一步，先要找出有哪些海岛。

旅游信息，我只信小红书和马蜂窝，不信公开网络。用Agent操作Playwright MCP，我帮它登录，它按我要求大量阅读，全面收集信息。中间两次让它收集更多信息，还做了一轮核实。

拿到核实的结果，去多个AI工具里验证，全部属实。

这样，我就得到了一份有价值的目的地清单，作为旅行规划的起点。然后，用类似的方法让AI补充更多信息，一次补充一个维度，直到我能选出某个确定的目的地。

之后就是我熟悉的旅行攻略方法论了，人工规划出完整的行程：

[手把手教你制作旅行攻略](https://victor42.eth.limo/post/3642/)

## 后记

这一年开年时，大家就说是Agent元年，现在看来，没有夸大。

Agent在编程领域已经摘取了第一颗果实，成功有目共睹，我已经大量使用很久了。在其他领域也开始广泛体现出真实的使用价值。

这确实是一个转变观念主动尝试的好时候，希望我发现得不算太晚。

最后，作为对比，附一下以前AI Agents生成PPT的测试，感受一下这段时间来Agents的进步：

[AI现在能独立做PPT了吗？](https://victor42.eth.limo/post/ai-generated-ppt/)

![](https://cdn.victor42.work/posts/2025-10/41d210330352023851a73ea8b5a06929.webp)