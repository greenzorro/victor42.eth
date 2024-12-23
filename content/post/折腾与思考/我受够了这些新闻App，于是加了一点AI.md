---
title: 我受够了这些新闻App，于是加了一点AI
description: 用手机编程，一不小心搞出了个市面上没有的东西。
image: https://cdn.victor42.work/posts/2024-08/90415a2f2e2fa7829fae2a10f117f392.jpg
date: 2024-08-13 13:31:00
categories: 折腾与思考
url: /post/3652
---

**阅读提示：本文涉及Tasker、AI、前端、自动化，有一定技术门槛。**

## 背景

我有个坚持，不想浪费宝贵时间在低价值信息上，所以会时常反思自己的信息来源。我感兴趣的领域，通常都能找到相应信息渠道，长期关注。但不能只盯着这些领域，也需要一扇小窗口，来偶尔了解其他领域的大事，防止画地为牢。

以往，我都是利用早晨送老婆孩子的时间，听听新闻电台，了解当天时事。这里面的信息也可以分为两类：

1. 肯定对我无价值。如体育新闻、娱乐新闻，我一点也不关心体育和八卦；又如军事新闻，军事信息披露少、难查证，各方报喜不报忧，单从新闻报道获得结论，完全不可靠。
2. 可能有价值，听了才知道。如社会新闻，近期消费趋势、科技发展导致的新社会现象等，有时能从中得到一些数据和洞察。当然，也有许多毫无价值，比如某豪车肇事逃逸这种，社会构成形形色色，单个个体的行为往往不值得关心。

近期巴黎奥运会，我的新闻时光几乎被奥运新闻淹没了。导致我开车时不时要瞄一眼大屏上的新闻标题，判断是不是该切下一条。有时候要连切7、8条，才能轮到一则我愿意听的。这样既不安全，又让人火大。

我试过许多可以听新闻的手机App。如果听头条频道，免不了混进这些不感兴趣的信息。如果订阅几个特定频道，又总会混入上千字的深度报道，敢情我一路就听你一条呢？更新频率的差异也是个问题，订阅的几个频道中，只要有一两个更新量极大，其他频道就相当于不存在了。

我就想，既然只瞄一眼标题就能判断要不要听，这事儿AI难道不能做吗？我可以继续听头条频道，只是让AI帮我滤掉一道，可不可行？

这个想法一冒出来，就完全停不下来了。

## 实现思路

仔细一想就发现，这事压根儿没什么技术含量。但就是找不到一款现成产品，可能是需求过于小众，那我就自己干吧！

首先，我要在哪实施我的构想？在电脑上写个程序当然可以，但既然听新闻绕不开手机，干脆整个流程都在手机上完成吧，摆脱对其他设备的依赖，否则我出去度个长假还听不了新闻了？所幸我长期使用Tasker，安卓手机上的一款编程软件，我知道它能实现我想要的效果。

整个过程不复杂，就这么几步：

1. 从新闻源获取当日的头条新闻
2. 把新闻标题交给AI，让它判断属于哪类新闻
3. 过滤掉我不要的几类新闻，剩余新闻以文字形式保存下来
4. 通过语音合成转成音频新闻，存到特定位置
5. 以上动作做成自动任务，每天深夜执行一遍
6. 在音乐播放器创建一个专门的歌单，读取音频新闻
7. 做另一个自动任务，手机连上车载蓝牙启动播放器，播放新闻
8. 再做个自动任务，每天把新闻清空，为下一轮做准备

## 准备轮子

以上步骤听起来像个大工程。但好在我不用自己发明轮子，其中许多能力都有现成的工具，把它们整合进来即可。现在，我得把可能用到的基础能力做成一个个小模块，也就是子任务，提前准备好，便于后续组装。

### Tasker简介

Tasker是这些子任务的载体。它是一个手机上的自动化工具，把硬件控制、数学运算、文件操作、网络请求、判断/循环等能力都打散成原子级别，让你自由组合，构建各种各样的自动化工作流。折腾过iPhone快捷指令的朋友应该熟悉这套玩法，只是Tasker远比快捷指令强大得多。把它归为自动化工具是低估了它，它实际上是个编程软件。

最基础的用法是根据条件来控制手机硬件，比如连上公司WIFI自动静音、连上车载蓝牙启动音乐播放器，这类效果做起来轻轻松松。高级一些的用法，涉及文件操作、网络请求，则需要有编程的思维，但并不需要真的写代码。

### 网络获取内容

第一个子任务需要具备上网的能力，才能浏览新闻源。

**输入：新闻源链接**  
**输出：包含新闻列表的代码**

![](https://cdn.victor42.work/posts/2024-08/7c717fff18ada6917cc6ddb9ab5acab4.jpg)

它用到了Tasker内置的HTTP请求，我没做任何额外处理，只把从新闻源获得的信息原封不动传递给外层任务。为什么要包这么一层，而不是直接用呢？这和子任务的执行优先级有关系，后面组装轮子的时候我会再讲。

### 解析XML

从RSS新闻源获得的不是直接能读的新闻，而是一堆XML代码，其中包含新闻列表。

![](https://cdn.victor42.work/posts/2024-08/d9b55eddd9d7d7e26b86fffe3dc56a1f.jpg)

RSS遵循一种通用的格式，无论哪个新闻源，一条新闻都对应一个item，它的标题、链接、描述分别对应title、link、description。标准的格式，就有标准的办法从中提取信息。

但在解析之前，我还加了另一个子任务，用来规整XML代码的格式。这里需要一点前端知识，因为网页里有时候会遇到代码被写成转义字符的情况，比如左尖括号`<`被写成`&lt;`、右尖括号`>`被写成`&gt;`。这个子任务可以把转义字符变回常规符号，便于统一处理。

**输入：包含转义字符的XML代码**  
**输出：标准的XML代码**

![](https://cdn.victor42.work/posts/2024-08/c117f68d572158b87dc54acd03427ad3.jpg)

下面该解析XML了。这个子任务可以从一堆XML中找到所有相邻的特定标签，提取出它们的内容，每个标签用`|||`分隔开。

**输入：完整XML代码、要提取内容的标签**  
**输出：所有该标签里的内容**

![](https://cdn.victor42.work/posts/2024-08/97c487fda93b7ef67d871a58ebd06721.jpg)

在我的程序里，我需要它找出所有item里的内容，也就是获取整个新闻列表。外层任务调用它时，把item作为第2参数（%par2）传给它，就能得到所有新闻条目的内容，并且以`|||`分隔开，便于外层任务进一步拆分处理。

### 从HTML提取内容

刚才的子任务能解析新闻列表，但其中只有标题和链接是真正有用的。RSS新闻源虽然格式统一，各家对于description却有不同理解。有的新闻源把全文都写在了description里，有的只在这写了摘要，正文藏在详情页里。

这个子任务就是为了干这个。给它一个页面的完整HTML代码，再告诉它要提取哪个标签的内容，它就能取出来，把不相干的菜单、评论、广告、页头页尾全撇掉。

**输入：完整HTML代码、要提取内容的标签**  
**输出：第一个该标签里的内容**

![](https://cdn.victor42.work/posts/2024-08/0f45bc228aba2af149ceeb0c69a67907.jpg)

这个子任务为何这么复杂？因为它要处理HTML标签层层嵌套的情况，这里涉及的前端知识不展开讲了。简单说就是它找到了标签的结尾在哪里，确定了提取内容的范围。整个过程都是靠字符串拆分、替换、拼接来完成的，实现了Javascript里innerHTML的能力。

取出来的正文内容仍然是HTML代码，这就需要另一个子任务来把HTML转成纯文本。这是Tasker自带的能力。

**输入：HTML代码**  
**输出：文本内容**

![](https://cdn.victor42.work/posts/2024-08/75b7ba16f35c56d3bb121026e9098eeb.jpg)

### AI判断新闻类型

前面的子任务是获取、加工内容的基础，但关键的筛选能力还得靠这个子任务，这是整个程序的脑子。

**输入：要发给AI的内容、AI模型名称**  
**输出：AI的回复**

![](https://cdn.victor42.work/posts/2024-08/05c6c50a2cba1cad021f550344301002.jpg)

[Groq的API](https://console.groq.com/playground)真的是个好东西，里面有许多好用的开源AI模型。查阅它的文档，调用这些AI模型非常简单。向它发一些文字，它再把生成的文字回给你。等待2秒是因为API有请求限制，一分钟内最多调用30次。

### 文本转语音

这个子任务把文本文件批量转成音频文件保存。

**输入：文本文件所在目录、音频文件保存目录**  
**输出：一批音频文件**

![](https://cdn.victor42.work/posts/2024-08/c1dabc63612d30a30e611297c14b6493.jpg)

关键步骤用到了Tasker自带的Say To File，文本存为音频文件。需要注意的是，Say To File只是提供了这种操作，合成过程需要的语音合成引擎，Tasker并没有内置。

![](https://cdn.victor42.work/posts/2024-08/995e0fb18649e334014f111ea8be2b8d.jpg)

我用了谷歌的本地语音合成引擎，Google Play下载这个App，就能在Tasker里调用。

![](https://cdn.victor42.work/posts/2024-08/07e0c2612c68af093e0a4e5c942ab102.jpg)

实测发现，本地免费语音合成引擎，效果大概只能达到地图软件默认语音包的水准。谷歌这个算其中比较优秀的了，甚至比讯飞的好，尽管还是很生硬。

## 组装轮子

几个轮子准备好了，大多难题都已解决，该组装了。

### 下载并筛选新闻

先组装出核心任务，它能从单个新闻源下载新闻，筛选后保存为文本文件，完成整个程序里绝大多数工序。

**输入：新闻源地址、详情页正文所在HTML标签**  
**输出：一批新闻文本文件**

我在输入的第2个参数上留了个小彩蛋。输入的如果是`<description>`，则不去新闻详情页获取正文，而是直接把XML里的description当做正文。这取决于每个新闻源的性质和数据质量，可以定义在它的外层任务上。

![](https://cdn.victor42.work/posts/2024-08/64acc1961ddd336d05f0b9aba63739ec.jpg)

从新闻源获得完整XML代码，把转义字符规整成标准XML，去掉一些特殊的内容标记。然后提取新闻列表。

![](https://cdn.victor42.work/posts/2024-08/b52349abcd5a92bb918c797c3043868a.jpg)

新闻列表根据分隔符分成数组，设定好AI提示词，设定正文长度上限（过滤掉太长的正文）。开始循环，每条新闻从XML里读出标题，标题转成纯文本，交给AI分类。

![](https://cdn.victor42.work/posts/2024-08/ba4c7edd6576c053b69d271d37f2bd88.jpg)

AI的提示词我是这么写的，没用到什么技巧，直白说出需求就行。由于这里处理的都是中文信息，Groq上的Gemma2 9b模型比较适合，比Llama3.1的中文能力强。这种简单需求，开源小模型足以胜任。实际使用效果很好，没出过错。

![](https://cdn.victor42.work/posts/2024-08/3e5a40b3c15e4e3661f026de131b45f0.jpg)

根据AI分的类型来判断，过滤掉体育/娱乐/军事新闻。再从XML得到新闻详情页链接，顺藤摸瓜取得详情页完整HTML，规整代码格式，根据正文所在HTML标签取出其内容。

把正文HTML代码转成文本，判断正文长度，太长的过滤掉，太短的可能是图片新闻也过滤掉。剩下的作为文本文件存到特定目录里。

### 优先级问题

调试核心任务的过程中，很多次出现取不到内容的情况，卡了很久。深入研究找到了原因：原来子任务的执行竟然是并行的！

Tasker的灵魂是它的Perform Task，作用是在当前任务里执行一个子任务。执行时可以把当前任务的信息传递给子任务，并获得子任务处理后的结果。

传入参数，获得返回值，这不就是编程里的函数吗？虽然Tasker有限制，最多只能往子任务里传2个参数，但如果把多个参数用特定分隔符拼接成字符串，传到子任务里再拆分开，理论上多少个参数都能传进来。用这种结构层层嵌套，什么复杂的逻辑做不出来？Perform Task的存在，使Tasker成为一款编程软件。

![](https://cdn.victor42.work/posts/2024-08/9fe1b7073ff0b94fab2859978f94ec9f.jpg)

仔细阅读了Perform Task的帮助文档，里面提到了执行顺序问题。触发子任务时，外层任务并不会等子任务执行完再继续（我一直这么以为），而是并行执行下去了。我的程序中，许多子任务要去网上获取内容，或对页面代码进行大量的循环处理，耗费时间很长。在子任务给出处理结果前，外层任务继续执行，当然就接不上了。

![](https://cdn.victor42.work/posts/2024-08/1091748819015f7296ec93d7500e5475.jpg)

按照帮助文档里建议的做法，把子任务Priority属性设为%priority+1，让子任务的优先级数值比外层任务多1，这样外层任务就会等子任务执行完才继续。

### 多渠道下载新闻

呼~ 好长一个任务写完了，现在来调用它。

![](https://cdn.victor42.work/posts/2024-08/a0a90a2ca998bca90156e3cfe59040b5.jpg)

把我选出的几个RSS新闻源传递给核心任务，从哪里取正文也告诉它。每个新闻源都执行一次。

![](https://cdn.victor42.work/posts/2024-08/d6d37dbe8a8195e2d6c7674104fc533f.jpg)

再单独做一个批量转语音的任务，把文本新闻的目录和音频新闻的目录都告诉它，让它往音频新闻目录里输出。

### 定时下载并转语音

上面都是任务，怎么启动它们呢？切换到Tasker的Profiles页面，这里可以为任务添加各种各样的触发条件。

![](https://cdn.victor42.work/posts/2024-08/bf1751cc5b2863826ff82d819e8b8859.jpg)

每天凌晨4点，把新闻都存成文本文件。这个过程要5-10分钟。

![](https://cdn.victor42.work/posts/2024-08/e1f5ef475b315060c9a3679f7a0e0603.jpg)

每天凌晨5点，把文本新闻转成音频。

## 最终效果

这样我一觉醒来，News目录下就有两个文件夹。

![](https://cdn.victor42.work/posts/2024-08/7add1606a97bddcc6fdee7af42f71cb1.jpg)

text保存了文字版新闻，如果有需要我还能二次分享出去。

![](https://cdn.victor42.work/posts/2024-08/4d00497b3a8e5554ff90aeccfe11dcbd.jpg)

audio文件夹里是音频新闻。虽然还有一些没什么意思的社会新闻混在其中，但这不能怪AI，至少我再也没有听到过体育新闻了。

![](https://cdn.victor42.work/posts/2024-08/fb2a13c2d652d15b0653f2e39be0beea.jpg)

手机上的音乐播放器里新建了一个叫每日新闻的歌单，专门读取audio文件夹。

![](https://cdn.victor42.work/posts/2024-08/90415a2f2e2fa7829fae2a10f117f392.jpg)

更新一下内容，当天新闻就都来了。这个更新过程仍然需要手动点一下，我还在找自动化的办法。

![](https://cdn.victor42.work/posts/2024-08/0023ce1bc26cb0c58b78cab5d834c033.jpg)

播新闻也是自动的。早晨连上车载蓝牙，播放器就自动打开了，而我用的[AIMP播放器](https://play.google.com/store/search?q=AIMP&c=apps)能设置打开自动播放，这下就完全不用动手了。

最后，我还有另一个自动任务，每天凌晨3点把新闻文件夹清空，为下一轮任务做准备。

## 后记

用了几天自制的新闻头条程序，这下舒坦了，开车不用分心了。除了语音比较生硬之外，其他毛病没有。语音嘛也许等哪天我受不了了，就再找个效果好的付费TTS API，把Say To File这一步替换掉就可以了。

一番操作下来，不仅解决了我生活中的问题，还积累了一些有用的子任务。我在制作网络获取内容、解析XML、从HTML提取内容、向AI提问这些子任务时，充分考虑了通用性。未来还能组装出其他程序，在手机上轻松实现各种网络爬虫，甚至AI agent。手机上的网络爬虫真的香，没有任何服务器费用，还能实现全天候运行，以后有具体需求再折腾吧。

## 资源下载

其中用到的比较复杂的Task已经公开分享，可随意取用。部分过于简单的Task就没有放上来，用内置的Task就能实现。

Bulk TTS:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3ABulk+TTS](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3ABulk+TTS)

Fix XML format:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AFix+XML+format](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AFix+XML+format)

API- Groq (enter your key):
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AAPI+-+Groq+%28enter+your+key%29](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AAPI+-+Groq+%28enter+your+key%29)

Fix file name:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AFix+file+name](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AFix+file+name)

Get inner XML(all siblings):
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AGet+inner+XML%28all+siblings%29](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AGet+inner+XML%28all+siblings%29)

Get inner XML(first match):
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AGet+inner+XML%28first+match%29](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3AGet+inner+XML%28first+match%29)

从RSS下载特定分类新闻:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E4%BB%8ERSS%E4%B8%8B%E8%BD%BD%E7%89%B9%E5%AE%9A%E5%88%86%E7%B1%BB%E6%96%B0%E9%97%BB](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E4%BB%8ERSS%E4%B8%8B%E8%BD%BD%E7%89%B9%E5%AE%9A%E5%88%86%E7%B1%BB%E6%96%B0%E9%97%BB)

多渠道下载新闻:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E5%A4%9A%E6%B8%A0%E9%81%93%E4%B8%8B%E8%BD%BD%E6%96%B0%E9%97%BB](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E5%A4%9A%E6%B8%A0%E9%81%93%E4%B8%8B%E8%BD%BD%E6%96%B0%E9%97%BB)
