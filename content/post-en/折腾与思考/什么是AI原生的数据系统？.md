---
title: What is an AI Native Data System
description: How my data management evolved alongside tools
image: https://cdn.victor42.work/posts/2026-06/01a9a53be38ac38125ec5e439d0ee2d1.webp
date: 2026-06-09 16:12:00
categories: 折腾与思考-Geek
url: /post-en/ai-native-data-system
translationKey: ai-native-data-system
---

I am a power user of Excel and Google Sheets, [relying on them heavily to manage both work and life](https://qvokpfxqsh.feishu.cn/wiki/G8OywdlWji0H31kJ0KwciaJ8nAd).

Later, I migrated some of my heavier data management tasks to visual databases like Feishu Bitable. While they might look like Excel, they are fundamentally different beasts. With much stricter data rules than spreadsheets, they trade some flexibility for the raw power of a true database. You can easily link multiple tables and build highly complex data systems—more than capable of running [a small business](https://victor42.eth.limo/post-en/automate-ai-illustrations-production/).

![](https://cdn.victor42.work/posts/2026-06/fc6b17ebd80b1127ef989c46c9ed412b.webp)

I once built a full-cycle task management system in Bitable, tracking everything from assignment to delivery. It seamlessly spun out weekly reports, project calendars, and annual stats. People asked for this system at least three times: a colleague for personal use, a manager for their team, and my previous employer for a company-wide rollout.

But no matter how powerful the tool, you still have to do the heavy lifting yourself.

I believe in what I call the "dishwasher philosophy". The older generation often scoffs at dishwashers, arguing, "You still have to rinse the plates first. I could have just washed them by hand in that time!" Here is my take: washing by hand takes 15 minutes of pure human labor. Rinsing takes 5 minutes, and the machine runs for 40—but that is still only 5 minutes of *my* time. I just bought back 10 minutes of my life.

To me, technology is a tool to reclaim my life.

Bitable has built-in AI features, and you can also use local Agents to control it via CLI or API. But if you try it, it feels like Usain Bolt running underwater—completely constrained. Bitable is not an AI-native product; it is designed for human eyes and human logic. Current AI Agents are text-based creatures, interacting with the world through code. Therefore, the most AI-native data system is simply a database.

I spent a day overhauling this system with AI. I stripped it back to the basics and took it entirely local. It no longer relies on cloud services or third-party apps. Now, it is just a lightweight local SQLite database, entirely read, written, and managed by AI. It automatically generates four pages based on the data: a calendar, recent tasks, historical tasks, and project stats. These serve as my dashboard and command center. Here is how it looks:

![](https://cdn.victor42.work/posts/2026-06/01a9a53be38ac38125ec5e439d0ee2d1.webp)

![](https://cdn.victor42.work/posts/2026-06/1ef49a58e0fc77e16de145b8a8f10935.webp)

![](https://cdn.victor42.work/posts/2026-06/4493b8709a24ae2c1a2ebd66f351e0de.webp)

![](https://cdn.victor42.work/posts/2026-06/6c11adfcc19725d0155524aae1eedf6f.webp)

Need to squeeze in a last-minute request? I just tell the AI to push all tasks from today onwards back by one workday, and it even splits overnight tasks to skip the weekend. Just one sentence.

Finished a task? The AI automatically scans the schedule for the task's last appearance, sets that as the delivery date, and marks it done. If I forget to add deliverable links or thumbnails, it nudges me to provide them. Again, just one sentence.

![](https://cdn.victor42.work/posts/2026-06/d89b73b5ca2469be465cc6c1e9ddbb4a.webp)

![](https://cdn.victor42.work/posts/2026-06/c865e3397af6f1488633198616b466ff.webp)

Want to add public holidays to the calendar? It is a non-standard request, but since you are using AI, it always finds a way to make it happen.

I am not saying this replaces Excel or Bitable entirely. Their perks are undeniable: WYSIWYG interfaces, cross-platform access, and zero environment dependencies. I still manage plenty of data in Google Sheets.

Watching the AI carefully but slowly read specs, write SQL, verify data, and update pages does not bother me one bit. Sure, I could have done it in seconds in Excel or Bitable. But over a full day of intensive use, who knows how many of those seconds the AI has bought back for me.

This system is open-source, so feel free to grab it. It will keep your work perfectly organized without draining your time on administrative chores:
[https://github.com/greenzorro/project-manager](https://github.com/greenzorro/project-manager)