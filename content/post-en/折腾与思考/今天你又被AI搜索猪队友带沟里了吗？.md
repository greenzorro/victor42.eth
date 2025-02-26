---
title: AI Search Got You Stuck?
description: Read this, and you might just pull yourself (and the AI) out of the ditch.
image: https://cdn.victor42.work/posts/2025-02/84O7u4RISVmTo0al7fmLUA.jpg
date: 2025-02-26 12:14:00
categories: 折腾与思考-Geek
url: /post/en/ai-search
translationKey: ai-search
---

I've been looking for a truly reliable AI search tool. I figured I'd just test it with some representative questions. Turns out, I was in over my head.

## Starting with Real-Life Problems

I've used some real-world questions as test cases, and most AI search tools fall short.

It's not that the questions are hard. The trick is how the AI goes about searching and pulling out the answer.

### What kind of fish is "Guyanyu"?

It's a type of edible flatfish. This is a trick question – "Guyanyu" is a colloquial, shortened name used in fish markets, not the scientific one.

AI finds useful info, but also noise:

- Some only consider "Guyanyu," ignoring homophones, leading to wrong answers like "spotted shad."
- Others consider the homophone "Guyanyu," but mistake it for the spotted shad.

Reasoning models see they're different, but can't tell which one you're asking about, so they list both.

Sometimes, because there's so much more info on "Guyanyu" (the flatfish), the AI jumps to a conclusion and gets it right, accidentally.

### What's the relationship between Liu Chuanzhi and bike-sharing?

There's not much of a direct link, but there's a two-step indirect one: his daughter, Liu Qing, and Didi (which she leads), which owns Qingju Bike.

I didn't know their relationship when I asked. I wanted the *most significant* chain of influence, not the most direct.

Non-reasoning models focus on Legend Capital's investment in ofo, mostly ignoring Liu Qing.

Reasoning models are smarter, recognizing Liu Qing's importance, but stop at Didi. They assume Didi is just ride-hailing and don't dig into Didi's connection with Qingju, often concluding: The Liu family has a big impact on transportation, but little direct connection to bike-sharing.

### Hangzhou was called Lin'an in ancient times. Why did this name get "given" to Lin'an District today?

This used to confuse me. It wasn't "given." I had it backwards. Lin'an County came first, *then* the Southern Song Lin'an Prefecture. The Southern Song might have been inspired by the county, but they were different places. The Southern Song capital was in downtown Hangzhou, not Lin'an. After the Song Dynasty fell, Lin'an Prefecture went back to being Hangzhou, while Lin'an County stayed Lin'an. Later, Lin'an became a district of Hangzhou.

Because the question itself is misleading, non-reasoning models mostly go with the incorrect assumption, talking about commemorating history or the glory of the Southern Song.

Reasoning models do well here, mostly getting it right. They spot the chronological order and point out the flawed "given to" phrasing.

### What was the highest throughput of Shanghai's port during the colonial period? How did it compare to the largest ports at the time?

I was just curious. I still don't know, but I found that most AI search tools can't answer this.

A somewhat reliable source is the Shanghai Port Chronicle on Baidu Baike, mentioning 14 million tons before the Second Sino-Japanese War, ranking 7th globally.

Data for other ports is either unavailable or made up by the AI. Some less intelligent AIs with big search volumes found *some* useful data (at least with references).

These are all real problems. I had tons of questions. I was a "walking encyclopedia" as a kid, and many quick searches turned up nothing. This made me doubt AI search.

## Not All Problems Are Created Equal

AI search is a mixed bag. Some do well on certain questions, others don't. I started looking for patterns: How can I tell which AI is good at what? And how should I pick an AI search product?

First, reasoning models are generally better, but not all are smart enough. Gemini 2.0 Flash and Kimi K1.5 aren't great. In my tests, Gemini 2.0 Flash couldn't answer these, but R1 could.

Search method matters, too.

Interestingly, Grok 3 has strong reasoning, even without "Think," but can't answer the "Guyanyu" question. Looking at its searches, I get why. It might be forcing a translation. With a weird Chinese name like "Guyanyu," it mistranslates, doesn't search for the shad or flatfish, and probably searches for things like "ancient" and "eye" separately. It finds nothing useful and makes stuff up.

Search volume is also key.

which country does Windsurf IDE come from?

It's from the US. I thought, "easy." Foreign AI search did great, even finding Mountain View, California. I tested domestic ones. Kimi and Yuewen can search English, so I asked in English. Finding the US was easy, but not the city.

But it's *not* that simple. Which article on Windsurf IDE would mention the city? At most, they'd say the country. To get the full answer, the AI needs to find Codium (the company behind it), then find the city from Codium's site, job postings, or Product Hunt. That takes reasoning and multi-step searching!

This made me realize: questions we find easy can be tough for AI. It's not that AI is dumb; we underestimate the complexity.

Even with a search engine, finding Windsurf IDE's country is easy, but the city isn't a one-search deal.

So, I came up with a rough way to evaluate AI search: four quadrants based on AI ability and search ability:

![](https://cdn.victor42.work/posts/2025-02/Snipaste_2025-02-26_12-52-46.png)

I underestimated the "Guyanyu," Liu Chuanzhi/bike-sharing, and Lin'an questions. I thought they were type D, but they're type B. The Shanghai port question is a trickier type A.

Mistaking type A for C, and B for D, leads to disappointment.

The biggest problem? We don't know the category when we ask, and we often underestimate the difficulty.

But AI search is a tool, and tools should serve us, right? It's not doing a great job yet, and that's not our fault; it's on them to improve.

To reliably answer type B, agents like Grok 3 Deep Search and OpenAI Deep Research are crucial. They need multi-step searches, deep dives into relationships, source reliability checks, and conflicting info evaluation.

## Making the Most of AI Search

Deep search for everything is too slow.

As someone in the AI community said: Since we can't make AI accommodate humans yet, let humans accommodate AI.

### Use Multiple Products Simultaneously

To save time and get decent answers, ditch the "one-tool-fits-all" idea. Think a bit about which quadrant a question likely falls into. Each has reliable AI search products; choose accordingly.

It takes more thought, but saves time. Your call.

Let's go backwards. Type D is easiest; any AI search tool works.

Type C needs a lot of searching, but no reasoning. If the webpage exists, the answer is there. Example:

which country does Windsurf IDE come from?

Kimi does well on these. Products with 50 search entries are also good. Consider long-tail knowledge as this type.

Type B has two scenarios:

1.  The answer's there, but with lots of conflicting noise.
2.  The answer's not in the core search results, but is abundant in incidentally searched terms. My earlier questions are examples.

These need strong reasoning models, like R1, Grok 3 Think, or O3 Mini. Search capability isn't as crucial; a dozen or two dozen sources are enough. Type B is easily mistaken for D. If answers are bad, realize this.

Finally, type A. I'm not sure any current AI search can handle these reliably. Info is scarce. You'll probably have to sift through search engines manually. If you want to try AI, use deep search/research.

### Give Up on One-Shot Answers

The goal is to solve problems. Don't expect a perfect answer in one go. Let that go, and you'll find more options.

Back to:

which country does Windsurf IDE come from?

If the first question doesn't give the city, ask:

which city?

For reasoning models, the odds of success go way up. Use multi-turn dialogue; you'd do the same with a search engine.

For tricky type A questions, like I said, accommodate the AI.

Ask in different ways, skim the sources, and judge usefulness by titles. Put useful ones in a knowledge base, and use AI to RAG it for the answer. Tools include NotebookLM, Tencent's iMa, Perplexity, and AI clients like Cherry Studio.

### Pay Attention to Language Differences

Language matters. An AI limited to Chinese can't answer English-world nuances; foreign AI can't answer questions about your local school's enrollment plan.

A test:

wildfire trends in CA in the last 10 years

Ask about something abroad in English. If most results are Chinese webpages, it can't search English well and is only good for Chinese topics.

Most domestic products have R1, so reasoning is good. Choosing a Chinese-world AI search is easy: find one with a large search volume.

If you need English and foreign info, foreign products are best. If that's inconvenient, test domestic products with English questions.

Finally, models and products mentioned are time-sensitive (February 2025). Conclusions might change, but the factors for understanding and evaluating AI search remain useful.