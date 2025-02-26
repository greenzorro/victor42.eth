---
title: Fed Up with News Apps, I Added Some AI
description: I built a non-existent app, coding on my phone.
image: https://cdn.victor42.work/posts/2024-08/90415a2f2e2fa7829fae2a10f117f392.jpg
date: 2024-08-13 13:31:00
categories: 折腾与思考-Geek
url: /post/en/en/3652
translationKey: 3652
---

**Note: This article involves Tasker, AI, front-end development, and automation. It's a bit technical.**

## Background

I'm all about avoiding low-value information. I usually follow specific channels for my interests, but I also need a way to catch major events in other fields, to avoid getting stuck in an echo chamber.

I used to listen to the radio while driving my family around, to get the news. The info fell into two categories:

1.  Useless: Sports, entertainment, and military news (often unreliable or biased).
2.  Potentially useful, but I had to listen to find out: Social news, trends, and tech-related social phenomena. Of course, much of it was fluff, like a celebrity hit-and-run.

During the Paris Olympics, my news time was swamped with Olympics coverage. I had to keep glancing at my car's screen to skip stories, which was unsafe and annoying.

I've tried many news apps with audio. The headlines channels were full of uninteresting stuff. Subscribing to specific channels meant long, in-depth reports – not ideal for a short drive. Update frequencies also varied wildly; some channels would dominate, effectively silencing others.

Then it hit me: I can usually tell if a story is interesting just from the headline. Why not use AI for this? Could I filter out unwanted stories from a headlines channel?

The idea stuck.

## Implementation

It wasn't technically difficult, but I couldn't find anything like it. Maybe it's too niche, so I built it myself!

My phone was the obvious choice, since that's where I listen to news. This avoids relying on other devices. What if I'm on vacation? Luckily, I'm familiar with Tasker, an Android app that's essentially programming software.

Here's the process:

1.  Fetch the day's top news.
2.  Use AI to categorize headlines.
3.  Filter out unwanted categories, saving the rest as text.
4.  Convert the text to audio.
5.  Automate this to run nightly.
6.  Create a playlist for the audio news.
7.  Auto-start the player when connected to my car's Bluetooth.
8.  Clear old news daily.

## Building Blocks

This sounds complex, but I didn't have to reinvent the wheel. I just needed to integrate existing tools. I created small modules (subtasks) for the core functions, ready for assembly.

### Tasker Intro

Tasker is the backbone. It's an automation tool that lets you combine hardware control, math, file operations, network requests, and logic into workflows. Think iPhone Shortcuts, but much more powerful – it's programming software.

Basic usage is simple: mute the phone on company Wi-Fi, or start music on Bluetooth connection. More advanced uses, like file operations and network requests, require programming logic, but no actual coding.

### Fetching Content

The first subtask browses the news source.

**Input: News source link**  
**Output: Code with the news list**

![](https://cdn.victor42.work/posts/2024-08/7c717fff18ada6917cc6ddb9ab5acab4.jpg)

It uses Tasker's HTTP request. I just passed the info to the outer task. Wrapping it in a layer relates to subtask execution priority, which I'll explain later.

### Parsing XML

RSS news feeds provide XML, not directly readable news.

![](https://cdn.victor42.work/posts/2024-08/d9b55eddd9d7d7e26b86fffe3dc56a1f.jpg)

RSS is standardized. Each news item is an "item," with "title," "link," and "description" tags.

Before parsing, I standardized the XML. Webpages sometimes use escaped characters (e.g., `<` as `&lt;`). This subtask converts them back.

**Input: XML with escaped characters**  
**Output: Standard XML**

![](https://cdn.victor42.work/posts/2024-08/c117f68d572158b87dc54acd03427ad3.jpg)

Next, parsing. This subtask extracts content from specific XML tags, separating them with `|||`.

**Input: Full XML, tag to extract**  
**Output: All content within that tag**

![](https://cdn.victor42.work/posts/2024-08/97c487fda93b7ef67d871a58ebd06721.jpg)

I use it to find all "item" tags (the news list). The outer task passes "item" as %par2, getting all news items separated by `|||`.

### Extracting Content from HTML

The previous subtask gets the news list, but only the title and link are really useful. "Description" varies; some sources include the full text, others just a summary, with the full text on a details page.

This subtask extracts content from a page's HTML, removing menus, comments, ads, etc.

**Input: Full HTML, tag to extract**  
**Output: First content within that tag**

![](https://cdn.victor42.work/posts/2024-08/0f45bc228aba2af149ceeb0c69a67907.jpg)

It's complex because of nested HTML tags. It finds the tag's end to define the content range, using string manipulation to mimic Javascript's `innerHTML`.

The result is still HTML, so another subtask converts it to plain text – a built-in Tasker feature.

**Input: HTML code**  
**Output: Text content**

![](https://cdn.victor42.work/posts/2024-08/75b7ba16f35c56d3bb121026e9098eeb.jpg)

### AI Classification

This is the core: the program's brain.

**Input: Content for AI, AI model name**  
**Output: AI response**

![](https://cdn.victor42.work/posts/2024-08/05c6c50a2cba1cad021f550344301002.jpg)

[Groq's API](https://console.groq.com/playground) is great, offering many open-source AI models. It's simple: send text, get generated text back. The 2-second wait is due to the API's 30 calls/minute limit.

### Text to Speech

This subtask converts text files to audio in batches.

**Input: Text file directory, audio output directory**  
**Output: Batch of audio files**

![](https://cdn.victor42.work/posts/2024-08/c1dabc63612d30a30e611297c14b6493.jpg)

It uses Tasker's "Say To File," saving text as audio. "Say To File" is just the operation; the speech synthesis engine isn't built-in.

![](https://cdn.victor42.work/posts/2024-08/995e0fb18649e334014f111ea8be2b8d.jpg)

I used Google's local engine. Download the app from Google Play, and Tasker can use it.

![](https://cdn.victor42.work/posts/2024-08/07e0c2612c68af093e0a4e5c942ab102.jpg)

The local engine is comparable to map software's default voice. Google's is decent, better than iFlytek's, but still robotic.

## Putting the Pieces Together

Now that we have our tools, and most of the hard parts are solved, let's assemble everything.

### Downloading and Filtering News

First, we'll build the core task: downloading news from a single source, filtering it, and saving it as text files. This is the heart of the process.

**Input: News source URL, HTML tag containing the article body**  
**Output: News text files**

I added a shortcut for the second input. If you enter `<description>`, it uses the description from the XML instead of fetching the article's detail page.  This works best with high-quality news sources, and you can set it in the parent task.

![](https://cdn.victor42.work/posts/2024-08/64acc1961ddd336d05f0b9aba63739ec.jpg)

We fetch the full XML, clean up escaped characters, and remove some special content tags. Then, we extract the news list.

![](https://cdn.victor42.work/posts/2024-08/b52349abcd5a92bb918c797c3043868a.jpg)

The news list is split into an array. We set up the AI prompt and a maximum article length (to avoid overly long articles). Then, we loop through each news item, read and convert the title to plain text, and send it to the AI for categorization.

![](https://cdn.victor42.work/posts/2024-08/ba4c7edd6576c053b69d271d37f2bd88.jpg)

Here's the AI prompt. I kept it simple, just telling it what to do. Groq's Gemma2 9b model works well for Chinese text, better than Llama3. A small open-source model is perfect for this, and it hasn't made any mistakes.

![](https://cdn.victor42.work/posts/2024-08/3e5a40b3c15e4e3661f026de131b45f0.jpg)

We filter out sports, entertainment, and military news based on the AI's categorization.  Then, we get the news detail page link, fetch the full HTML, clean it up, and extract the content using the specified HTML tag.

We convert the article body from HTML to text, check its length, and filter out anything too long or short (likely image-based news). The remaining articles are saved as text files.

### Priority Issues

During debugging, I couldn't get content consistently. It took a while to realize the subtasks were running in parallel.

Tasker's core feature, "Perform Task," runs a subtask within the current task, passing data and receiving results.

It's like function calls in programming. Tasker limits you to two parameters, but you can combine multiple parameters into a string using a separator, then split them in the subtask. This allows for any number of parameters. This nesting lets you build complex logic, making "Perform Task" a key programming feature in Tasker.

![](https://cdn.victor42.work/posts/2024-08/9fe1b7073ff0b94fab2859978f94ec9f.jpg)

The "Perform Task" documentation mentions execution order. The parent task doesn't wait for a triggered subtask to finish before continuing.  Many of my subtasks fetch content or loop through page code, which takes time. If the parent task proceeds before the subtask returns a result, things break.

![](https://cdn.victor42.work/posts/2024-08/1091748819015f7296ec93d7500e5475.jpg)

Following the documentation, I set the subtask's Priority to %priority+1 (one higher than the parent). This forces the parent task to wait.

### Downloading News from Multiple Sources

That was a complex task! Now, let's use it.

![](https://cdn.victor42.work/posts/2024-08/a0a90a2ca998bca90156e3cfe59040b5.jpg)

I pass my RSS feeds and article body locations to the core task. It runs for each source.

![](https://cdn.victor42.work/posts/2024-08/d6d37dbe8a8195e2d6c7674104fc533f.jpg)

Then, I created a separate task for batch conversion to speech, specifying the input (text news) and output (audio news) directories.

### Scheduled Downloads and Conversion

These are the tasks, but how do they run?  On Tasker's Profiles page, you can add triggers for your tasks.

![](https://cdn.victor42.work/posts/2024-08/bf1751cc5b2863826ff82d819e8b8859.jpg)

Every day at 4 AM, save all news as text files (takes 5-10 minutes).

![](https://cdn.victor42.work/posts/2024-08/e1f5ef475b315060c9a3679f7a0e0603.jpg)

Every day at 5 AM, convert the text news to audio.

## The Final Result

When I wake up, there are two folders in the News directory.

![](https://cdn.victor42.work/posts/2024-08/7add1606a97bddcc6fdee7af42f71cb1.jpg)

`text` contains the text versions, which I can share.

![](https://cdn.victor42.work/posts/2024-08/4d00497b3a8e5554ff90aeccfe11dcbd.jpg)

`audio` contains the audio news. Some local news still gets in, but the AI is doing its job filtering out sports.

![](https://cdn.victor42.work/posts/2024-08/fb2a13c2d652d15b0653f2e39be0beea.jpg)

I created a "Daily News" playlist in my music player to read the `audio` folder.

![](https://cdn.victor42.work/posts/2024-08/90415a2f2e2fa7829fae2a10f117f392.jpg)

Updating the content brings in the day's news. I still have to update it manually, but I'm working on automating that.

![](https://cdn.victor42.work/posts/2024-08/0023ce1bc26cb0c58b78cab5d834c033.jpg)

Playback is automatic. My car's Bluetooth connection opens the player, and I use [AIMP player](https://play.google.com/store/search?q=AIMP&c=apps), which auto-plays on open. No interaction needed.

Finally, a task clears the news folders at 3 AM daily, preparing for the next cycle.

## Epilogue

My homemade news program has been working great for a few days. I can drive without distraction. The robotic voice is the only minor issue. I might replace "Say To File" with a better TTS API later.

This process solved a problem and gave me reusable subtasks. The subtasks for fetching content, parsing XML, extracting HTML, and querying AI are generic. I can now build other programs, create web scrapers, and even AI agents on my phone. Mobile scraping is great: no server costs, and it runs 24/7. I'll explore it further as needed.

## Resources

The more complex Tasks are shared publicly for free use. Simpler Tasks are omitted, as they can be built using Tasker's built-in features.

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

Download specific categories of news from RSS:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E4%BB%8ERSS%E4%B8%8B%E8%BD%BD%E7%89%B9%E5%AE%9A%E5%88%86%E7%B1%BB%E6%96%B0%E9%97%BB](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E4%BB%8ERSS%E4%B8%8B%E8%BD%BD%E7%89%B9%E5%AE%9A%E5%88%86%E7%B1%BB%E6%96%B0%E9%97%BB)

Download news from multiple channels:
[https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E5%A4%9A%E6%B8%A0%E9%81%93%E4%B8%8B%E8%BD%BD%E6%96%B0%E9%97%BB](https://taskernet.com/shares/?user=AS35m8mopd%2Bc1C7UhZNzgAc6Ld0oCTR8LzUJsfqb7SGyZq7NWeHANGDjDvTtBPSkNCjn3CrFQoI%3D&id=Task%3A%E5%A4%9A%E6%B8%A0%E9%81%93%E4%B8%8B%E8%BD%BD%E6%96%B0%E9%97%BB)
