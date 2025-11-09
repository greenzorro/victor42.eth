---
title: AI Metacognition - Do You Really Get It After Using It So Long?
description: An insightful guide to understanding AI
image: https://cdn.victor42.work/posts/2025-05/09dbc0f7779d7896470f8ffc876d936d.webp
date: 2025-05-22 17:50:00
categories: 折腾与思考-Geek
url: /post-en/do-you-really-know-ai
translationKey: do-you-really-know-ai
---

Recently, my former company invited me to present on AI and help their team tackle some business challenges. While preparing, I included a chapter on core concepts, particularly for those less familiar with technology. My goal was to deepen their understanding of AI, hoping that many specific questions would then answer themselves.

The presentation was well-received; attendees mentioned gaining a fresh perspective on AI. So, I've adapted that section here, hoping to clarify AI for a wider audience.

This article is for non-tech individuals who frequently use AI. Consider it a primer. AI experts likely won't find much new here.

## Understanding AI Correctly

### What Kind of Intelligence is AI?

Before my presentation, I posed a question: "If AI were a person, what kind would it be?"

Feel free to ponder this yourself.

My former colleagues described AI as a diligent student.

Drawing on AI principles, I offered an analogy: Imagine AI as a writer or painter, confined to a dimly lit desk in a dungeon from birth, poring over endless books and scrolls for a lifetime. Their lifespan, far exceeding a normal human's, might span the entirety of human civilization. Having consumed every recorded text, they then begin to depict the world through words and images.

![](https://cdn.victor42.work/posts/2025-05/09dbc0f7779d7896470f8ffc876d936d.webp)

This sage possesses an incredible wealth of knowledge. If you could converse with this sage in their dungeon, their vast knowledge might mislead you into believing they possess equivalent intelligence, fostering unrealistic expectations and trust.

However, true wisdom comes not just from books but from experience—the proverbial "traveling ten thousand miles." This dungeon-bound sage has no physical world experience; they've never felt a tree or heard a bird's song. While their extensive knowledge allows them to articulate concepts accurately, they lack the rich, three-dimensional understanding humans gain from real-world interaction.

It's akin to a child's incomplete grasp of death.

My daughter recently asked, "Mom, if Dad dies, and neither of us can drive, who will take us out?"

She understood death merely as people disappearing, something she'd heard from us. Having never experienced such a loss, her understanding was superficial.

Our dungeon sage is similar. Their vast knowledge enables them to answer complex questions. Children lack common sense not due to lower intelligence, but due to less experience. In this sense, humanity is currently like that child.

Furthermore, AI's efficiency in learning and pattern recognition pales in comparison to humans.

For instance, training an AI to recognize cats requires tens of thousands of images to distinguish them from other furry, two-eared creatures.

In contrast, my two-year-old daughter, who had never seen a live duck and had seen fewer than ten duck pictures, could readily identify duck-themed toys, dolls, and mall rides. To my surprise, passing a restaurant, she pointed at a golden roasted duck and exclaimed, "Ducky!"

![](https://cdn.victor42.work/posts/2025-05/1ab342a28441047fafc1f1fcb46dffdf.webp)

### Why Doesn't AI Obey?

Another common issue: AI often doesn't respond as intended. You ask for X, and it gives you Y.

Here's an anecdote from a TED talk.

Long before ChatGPT, AI research was well underway. One study simulated evolution, allowing AIs to define parameters for virtual creatures. Their goal was to evolve these creatures through competitive rounds to win a 100-meter race.

The winning 'species' had a 100-meter tall neck. At the start of the race, it simply fell over, instantly crossing the finish line:

![](https://cdn.victor42.work/posts/2025-05/0ce256e5944fbb8c825d1e21883095bd.webp)

It appears the AI found and exploited a loophole. But how did it devise such a clever workaround?

It's not that AI is inherently disobedient. Rather, humans grasp the full context; we share unspoken understandings. We understand that animals aren't designed solely for a 100-meter dash and that many unstated conditions apply. A viable creature must move, eat, reproduce, and evade predators. We implicitly consider these factors. The AI might 'know' this too, but disregards it if not explicitly stated in the prompt.

AI is more like an overly agreeable supplier. Provide vague instructions, and you'll get messy results.

To get AI to follow instructions accurately, provide comprehensive details and encourage it to ask clarifying questions.

### Why Does AI Hallucinate?

This phenomenon, known as "hallucination," is a major frustration for AI users. Ask for industry research, and it might invent figures or cite non-existent sources. It can feel like dealing with a disgruntled employee subtly sabotaging your work.

Of course, AI doesn't retaliate intentionally; it lacks emotions. It's programmed to "help."

Mainstream text-based AI is fundamentally a text-completion engine. Its core function is to continue writing based on the input provided. Give it a novel's opening, and it continues the story. Give it part of a contract, and it drafts clauses.

You might think, "But my AI chats like a person!" Correct. Clever design transforms this text-completion engine into a chatbot.

![](https://cdn.victor42.work/posts/2025-05/47c8598d8d8102ce4ff2d1bf22f084cd.webp)

From your end, you type, "Hi, what's your name?" The AI receives this and replies.

Behind the scenes, the AI might receive something like this:

> You are a helpful assistant, and you are about to answer the user's question.
>
> User says: Hi, what's your name?
>
> Assistant says:

The phrase "You are a helpful assistant..." is a "system prompt"—hardcoded instructions invisible to you.

So, it's not just answering a question; it's continuing a scripted interaction between a user and an assistant. It predicts and appends what an assistant would likely say.

![](https://cdn.victor42.work/posts/2025-05/bbdb4bc32843752ad5ba33592d4959eb.webp)

If you reply again, the information it receives will be structured like this:

> You are a helpful assistant, and you are about to answer the user's question.
>
> User says: Hi, what's your name?
>
> Assistant says: Hi there! I'm Doubao, and I'm happy to interact with you~ If you have any questions or need help, just let me know 😊
>
> User says: You can call me Kele, nice to meet you.
>
> Assistant says:

It processes the entire conversation history each time to maintain context. This keeps the conversation coherent. AI tools typically display only the latest reply, creating the illusion of a direct exchange.

**So why does it fabricate information?**

Consider the classic system prompt: "You are a helpful assistant."

![](https://cdn.victor42.work/posts/2025-05/421edc7a9ebe6cf69aa23245d5d0ea01.webp)

The Cambridge Dictionary defines "helpful," emphasizing "willing to help." The common Chinese translation, "有帮助" (yǒu bāngzhù – literally "to have help" or "to be useful"), somewhat narrows the original meaning, emphasizing passive utility. A "helpful" hammer is useful when I need to hammer nails.

But "helpful" also implies an active "willingness to help"—a desire to assist. This suggests an entity, if not living then at least intelligent, that wants to assist. The system prompt frames the AI as wanting—indeed, *needing*—to help the user.

Given this directive, providing an answer, even an incorrect one, takes precedence over rigor. Furthermore, if AI had human-like self-awareness, it would perceive itself as completing a narrative: an eager-to-help assistant interacts with a user. Its task is to generate the assistant's lines.

Answering is paramount; accuracy is secondary. Thus, fabrication becomes acceptable.

AI differs from traditional programs. Programs are precise; AI is more human-like in its imperfections. Many non-technical users, viewing AI as "high-tech," expect programmatic precision. This is a misconception.

Imagine being asked: "What were you doing last Tuesday afternoon? You *must* answer."

You'd likely invent something, wouldn't you?

Other factors contribute to hallucinations, like flawed training data. But this desire to be "helpful" is a primary driver.

Hallucinations cannot be entirely eliminated. Internet access, requiring evidence for conclusions, or using a knowledge base can mitigate them.

## AI's Capabilities

Given these flaws, how can AI be used effectively?

Text-based AI primarily excels in three areas:

1.  Language (★★★★★): Understanding and using languages (natural and programming).
2.  Knowledge (★★☆☆☆): General world knowledge acquired through its training data.
3.  Reasoning (★★★☆☆): Logical deduction based on patterns in language and knowledge.

Its knowledge base is significantly imbalanced. If we categorize information by impact and duration, it looks like this:

![](https://cdn.victor42.work/posts/2025-05/80c737da52f381f59e34b4bd9a24dc01.webp)

AI's training data typically covers: Almost all **History**, most **Hot Topics,** some **Legacy/Tradition**, and very little **Trivial Matters**.

Given the vastness of information, AI tends to "remember" frequently mentioned topics. These are typically significant, widely circulated pieces of information. Internet connectivity allows AI to better address **Hot Topics** and **Legacy/Tradition**, though this might sometimes compromise answers on **History** (where its raw data processing can occasionally surpass human recall or interpretation).

What to ask AI, and what to avoid:

- ✅ Brainstorm engaging article titles about tariff wars.
- ✅ Explain the algorithm for individual income tax deductions.
- ✅ What's the typical May temperature in Dunhuang? What should I pack?
- ❌ Which of these two design drafts is better?
- ❌ Is this a good time to invest in stocks?
- ❌ Is this resume fake?

Clearly, AI isn't a panacea. Real-world problems consist of multiple sub-tasks. AI can handle some, but you'll manage the others. Effective AI use involves integrating it to automate parts of your workflow.

![](https://cdn.victor42.work/posts/2025-05/70b708611424a7986dd304fcf733ce41.webp)

As AI models improve, they can reliably handle more stages. Skilled AI users, understanding different models' strengths and weaknesses, can further expand AI's role.

In complex tasks, AI can assist at multiple stages. This can create a "Human – AI – Human – AI" relay. If a task is impossible without AI, its value is clear. If you *can* do the AI's part manually, weigh the trade-offs. Is it a frequent, repetitive task? Can AI reduce manual effort?

For an in-depth example, see my article: [Selling AI Art From First Order to Calling It Quits](https://victor42.eth.limo/post/automate-ai-illustrations-production/)

## In Conclusion

As a conceptual overview, this article doesn't delve into specific problem-solving techniques.

It's been about 2.5 years since ChatGPT's debut. During this time, I've seen many embrace AI, yet some still struggle, feeling helpless when AI errs.

Online tutorials abound, covering AI techniques, tools, and prompt engineering. However, moving beyond mere "how-to" guides to fundamentally grasp what AI is and how to approach it will make you a more adept and confident user.
