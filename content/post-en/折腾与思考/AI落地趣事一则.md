---
categories: 折腾与思考-Geek
date: 2026-04-03 09:42:00
description: A glimpse into the absurdities of the current AI gold rush
image: https://cdn.victor42.work/posts/2026-04/5c4ba548b31db35137c4d2b685767ba3.webp
title: A funny story about AI implementation
url: /post-en/the-great-ai-ification
translationKey: the-great-ai-ification
---

The company churns out a ton of fixed-template images daily: course covers, promo banners, printed signs, desk nameplates, arm stickers, you name it. It mostly boils down to swapping out text and picking a background from a preset pool based on the category.

Having designers do this manually is a pipe dream. The ops team doesn't know Photoshop and refuses to learn. Outsourcing it costs 20 RMB a pop.

My day job is UI design, but this chore somehow became my gig. I built a personal project that bridges Excel and Photoshop. Ops fills out a spreadsheet, designers maintain the PSD templates, and my script automatically maps the data into the templates, spitting out images in bulk. Over the past two years, it has generated roughly 150k RMB worth of design assets—enough to hire a few interns just to do the manual labor.

[https://github.com/greenzorro/excel-ps-batch-export](https://github.com/greenzorro/excel-ps-batch-export)

This Python script isn’t tailor-made for the company; it’s highly versatile. Whatever PSD template you build, my script generates the matching Excel sheet. Ops fills it in, hands it back, and boom—instant image batch.

Recently, the big boss started waving the AI flag, aggressively pushing AI adoption to "cut costs and boost efficiency." He eyed my batch-export setup and decided to make it the flagship AI demo to set the standard for the whole company.

In terms of cutting costs and boosting efficiency, my project is already doing exactly that. There's nothing left to push. The catch? It’s not AI. It’s just a hardcoded script.

That’s a dealbreaker. Without AI, it won't pass the boss's vibe check. Traditional code is seen as an outdated productive force. It needs that "AI flavor"—an overwhelming, undeniable AI aesthetic.

On the flip side, since the script runs locally on my machine, the whole process bottlenecks at me. And honestly, what boss doesn’t dream of "distilling" their employees into modular digital skills?

No problem. Distill away. Deploying it to the cloud solves that. Technically, they’re appropriating my personal IP for free, but since I don't mind (and it's open-source anyway), whatever.

Deploying it on the company server and slapping a GUI on it would make it a complete product. Give the ops team a quick tutorial, and it’s undeniably a step up from running it locally.

But alas, still no AI. Too primitive. Middle management vetoed it. If it’s not AI, we have to dress it up as AI. The final master plan? Spin up an AI bot on the server, give it a DingTalk account, and drop it into the ops group chat. Now, ops just @s the bot every day to generate images—exactly how they used to @ me.

Perfect! Just like that, a piece of my soul has been digitized, permanently enshrined in the corporate mainframe. Honestly, if we swapped the bot's name and avatar to mine, it would probably be even more intimidating to the boss.

The only hiccup is that a zero-cost operation is now burning through LLM tokens daily.

But on second thought, the boss probably sees this as a massive win. Finally, someone in the company is burning tokens and actually producing tangible results! The dawn of his grand AI empire is here. Sound the charge! Who cares about unit economics? In the name of AI, cost is but an illusion.

My takeaway? AI isn't a bubble. The doomers can rest easy. Setting aside how many real-world problems it actually solves, its mere existence is a spiritual balm, offering astronomical emotional value. It’s the new tech-bro Hermès. Between economic value and emotional value, it guarantees at least one. What a magical industry!

So yeah, the corporate grind is actually pretty entertaining. If the ship is going crazy, you might as well grab an oar and enjoy the ride. At the end of the day, having fun is all that matters~