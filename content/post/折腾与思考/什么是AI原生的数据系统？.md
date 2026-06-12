---
title: 什么是AI原生的数据系统？
description: 我的数据管理方式，随工具发展的几次变迁。
image: https://cdn.victor42.work/posts/2026-06/01a9a53be38ac38125ec5e439d0ee2d1.webp
date: 2026-06-09 16:12:00
categories: 折腾与思考-Geek
url: /post/ai-native-data-system
translationKey: ai-native-data-system
---

我Excel/Google Sheets用得很溜，[大量用它们管理工作和生活](https://qvokpfxqsh.feishu.cn/wiki/G8OywdlWji0H31kJ0KwciaJ8nAd)。

后来，我曾经把一部分较重的数据管理任务迁移到飞书多维表这样的产品里。这类东西长得很像Excel，但本质上是完全不同的东西，是可视化数据库。它们比Excel有着严格得多的数据规范，限制灵活性的同时，释放了数据库天然带来的强大能力。可以更轻松建立多表关联，构建出结构非常复杂的数据系统，支撑[一个小生意](https://victor42.eth.limo/post/automate-ai-illustrations-production/)都不在话下。

![多维表格中用于项目管理的排期日历界面](https://cdn.victor42.work/posts/2026-06/fc6b17ebd80b1127ef989c46c9ed412b.webp)

我用多维表构建过任务管理系统，每一项工作任务从接收到交付，完整生命周期全都在里面。从中再派生出周报、排期日历、年度数据报表等用途。这套系统至少3次被别人要了去，一次是同事个人，一次是主管拿去管理团队，还一次是被前司拿去全员推行。

但再强大，毕竟免不了亲自动手。

我信奉一个“洗碗机哲学”：老一辈瞧不上这玩意，总觉得你不还是得先冲洗下再放进去吗，有这时间我早就手洗完了。我的道理是，手洗15分钟，投入人工15分钟；人工冲洗5分钟+洗碗机洗40分钟，人工只投入5分钟，我给自己的人生赢回了10分钟。

科技，在我这，是用来赎回生活的。

多维表本身也带AI功能，或者也可以用本地的Agent通过CLI或API来操作多维表。但你试过就知道，那过程就像博尔特在海底跑步，束手束脚的。多维表并不是一种AI Native的产品，它的形态是围绕人类视觉和理解而设计的。目前的AI Agent都是文字生物，代码是他们和世界交互的方式，最AI Native的数据系统就是数据库。

花了1天时间完成了这套系统的AI化改造。返璞归真，彻底本地化。它现在不用再依赖任何云端产品或第三方应用了，一个轻量级本地SQLite数据库，完全由AI来读写和管理。根据其中数据自动产生日历、近期任务、历史任务、项目统计4个页面，作为我观察数据的窗口，和发号施令的依据。效果如下：

![新系统网页中干净清晰的排期日历页面](https://cdn.victor42.work/posts/2026-06/01a9a53be38ac38125ec5e439d0ee2d1.webp)

![新数据系统中展示进行中任务的近期任务页](https://cdn.victor42.work/posts/2026-06/1ef49a58e0fc77e16de145b8a8f10935.webp)

![新数据系统中展示已完成需求的历史任务页](https://cdn.victor42.work/posts/2026-06/4493b8709a24ae2c1a2ebd66f351e0de.webp)

![展示各项需求数量及页面统计的图表页面](https://cdn.victor42.work/posts/2026-06/6c11adfcc19725d0155524aae1eedf6f.webp)

插个临时需求？让AI把今天及以后的所有任务都延后一个工作日，跨天任务还能自动拆成两段避开周末。就一句话的事情。

有个任务完成了？AI自动去排期表里找，这个任务最后一次出现在哪一天，把那天作为交付日期，更新完成状态。如果缺了交付物链接、缩略图等信息，还主动提醒我补充。也是一句话的事情。

![系统控制台展示的部分已录入公共假期表](https://cdn.victor42.work/posts/2026-06/d89b73b5ca2469be465cc6c1e9ddbb4a.webp)

![系统界面展示的全部录入完成的假期表格](https://cdn.victor42.work/posts/2026-06/c865e3397af6f1488633198616b466ff.webp)

往日历里添加法定节假日，这种非标准用法，反正你用的是AI，它总有办法满足你。

不是说这种方法值得代替一切Excel或多维表，它们的优点也非常明显：所见即所得、跨平台、无环境依赖，我仍有许多数据是在Google sheets里管理的。

看着AI仔细但缓慢地读规范、写SQL、验证数据、更新页面，我一点也不嫌弃。如果是在Excel或多维表里，我可能十几秒就处理完了。但一天密集用下来，不知道AI又给我的人生赢回了多少个十几秒。

这套系统已经开源，欢迎取用。让你工作井井有条，又不用花太多时间在事务性任务上：

[https://github.com/greenzorro/project-manager](https://github.com/greenzorro/project-manager)
