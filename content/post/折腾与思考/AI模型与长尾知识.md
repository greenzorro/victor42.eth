---
title: AI模型与长尾知识
description: 一个自身能力极强的AI，并不是灵丹妙药。
image: 
date: 2023-10-10 23:38:00
categories: 折腾与思考
url: /post/3643
---

不能过于迷信依靠AI模型自身能力解决问题。几个顶流AI水平高是高，但主要体现在语言与思维能力。它们掌握的世界知识，其实仅仅是人类文明史里极少数意义重大的知识。还有浩如烟海的长尾知识，散落在世界世界的各个角落。这些知识既难以规整成数据集，AI也无法跟上它指数级增长的生产速度。

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/5e373f07e0f1d6cc445ff23440d48175.png)

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/bf76e92ffc1f62a8367a991ba92892d3.png)

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/f15d29bfa9fed427105aaaeb120ba45b.png)

以这个芒果胚根的问题为例，这是典型的长尾知识。我分别测了Claude、GPT-3.5、Bard。其中由于Bard有联网能力，表现反而优于模型自身能力更强的Claude和GPT-3.5。这里的关键在于，我指定让Bard“搜索网络后回答”，它从网络中得到了正确的长尾知识。

那如果让Claude和GPT-3.5采用同样策略，放弃用自己有限的知识猜测推理，转而总结人类生产的长尾知识，表现会不会有提升呢？目前Claude和GPT-3.5官方并没有联网的能力，但办法也是有的。就是这个浏览器插件：Maxai。

[https://chrome.google.com/webstore/detail/maxaime-use-chatgpt-ai-an/mhnlakgilnojmhinhkckjpncpbhabphi](https://chrome.google.com/webstore/detail/maxaime-use-chatgpt-ai-an/mhnlakgilnojmhinhkckjpncpbhabphi)

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/950c8f6bb194b893948fdcff805155c9.png)

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/b9e98c0cae51320fc9fa0592ea298956.png)

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/455533792011ed2dc9098e4418a67f78.png)

![](https://storage.fleek-internal.com/0a3a8890-e65e-47ce-93d7-0442b9209d38-bucket/blog/posts/2023-10/8af37c7c84ade486477a4f61c7c11f11.png)

它自己实现了搜索的部分，然后把搜索得来的几条结果让AI总结，现在结果大致令人满意了。只是我不太清楚这个插件挑选搜索结果的逻辑，它的准确度不如专业的搜索引擎（我在后来的几项其他测试中验证了这一点），Claude和GPT-3.5被一些无关信息干扰或误导，产生的结果仍然比不上Bard。确实，Bard在搜索能力上的优势无可比拟。

AI模型的立足之本是对语言的理解，当然，这里的语言是广义的，不仅仅限于人类的自然语言。它通过语言理解一切，与生物的多种立体感官系统感知世界的方式截然不同。从这个角度看，AI对世界的理解能达到今天的高度，是令人惊叹的。

然而，不能指望AI自身能力能解决一切问题，不，出到GPT-500都不可能。这是我看到的许多对AI不甚了解又满怀期待的老板们的认知误区。作为人，想要用好AI，让它真正成为人类的好帮手，正确的方向是，积极地让AI与真实世界连接起来。训练数据总会有截止时间，但它感知世界的渠道和方式可以无尽扩展。连接网络是极其重要的一步，但实际上只是第一步，后面的路，尽管放开胆想象。目前能看到的是，多模态能力的大发展，正在为未来铺路。
