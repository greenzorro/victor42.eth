---
title: Turning Photoshop into a Machine Gun with Excel
description: How a designer with Excel skills saved his company a bundle.
image: https://cdn.victor42.work/posts/2024-06/927f0f7ac6f154b4027673e30b629be2.jpg
date: 2024-06-13 14:05:00
categories: 折腾与思考-Geek
url: /post-en/3650
translationKey: 3650
---

I heard Marketing was tearing their hair out. The boss greenlit the new course cover design, and now they needed to update all 800+ existing covers. It wasn't a simple find-and-replace; there were tons of small differences.  Marketing has only one designer, and they were slammed. Doing it in-house? No way. Outsourcing would cost 20 RMB per image, totaling 16,000 RMB – a budget buster.

Bingo! 16,000 RMB? My ears perked up. I love automation. A data geek who knows Photoshop?  This was my moment. People talk about the "value of design." But what *is* your value? How do you put a number on it?  Saving the company a designer's monthly salary in half a day? That's real value.  Plus, it'd be great for my year-end review. I jumped on the task.

## The Challenge

![](https://cdn.victor42.work/posts/2024-06/d257445c788894aad2f9c9d25333d834.jpg)

This is the template the marketing designer created. No use criticizing – the boss wanted this style. Simple. The basic need was also simple: replace three text areas and generate 800+ images.

Most designers would think, "Piece of cake! Define some variables in Photoshop, create an Excel sheet, and batch export."

If you *don't* know how to batch output with Excel and Photoshop, check out this tutorial: [https://zhuanlan.zhihu.com/p/33725280](https://zhuanlan.zhihu.com/p/33725280)

Yeah... that's the gist. If it were *that* easy, you could just follow the tutorial, and this article would be done.

But, once I saw the template, I realized it was much trickier. The variations were crazy:

![](https://cdn.victor42.work/posts/2024-06/927f0f7ac6f154b4027673e30b629be2.jpg)

![](https://cdn.victor42.work/posts/2024-06/2f196e8210e1f43dae80cd978031cf36.jpg)

   ![](https://cdn.victor42.work/posts/2024-06/0a0c12d573ee7d0f2958cd0baee914fc.jpg)
   
![](https://cdn.victor42.work/posts/2024-06/f60e4590c7b4551a14e93c37b5396f8d.jpg)

1.  Over a dozen course categories, some with unique backgrounds, others sharing.
2.  The top category wasn't always text. Two (Taobao and Tmall) used logos – images.
3.  Course titles: one or two lines. Single-line titles needed vertical centering.
4.  Text color changed with the background – a tinted shade, not pure black.
5.  The bottom description text wasn't always there. If missing, its decorative box had to go too.
6.  The box's line color also changed, matching the text but brighter.

Think. Could you handle this with Photoshop variables? Sure, you could make a dozen PSDs. But I wanted just *one*.

Yes, it was possible.

But it needed a designer who was also an Excel expert.

## Designing the Excel Data Model

The complexity meant I needed to think about the data model first.

Programmers might laugh. "Data model? For a simple image?"

Don't @ me! I'm just using the idea. Look, if you just want to finish, anything goes. But for top efficiency, you need a data model mindset. What's that? The operations team fills in the least info, and I do the least work per export. This was ongoing, so I needed low marginal costs. The initial setup could be complex; that cost was less important.

So, what columns did we need?

-   Course Category
-   Course Title
-   Description
-   Background Image

Obvious ones. Adding the variations, the real list was:

![](https://cdn.victor42.work/posts/2024-06/3edc562bdfee2fb96d5271d682185f6b.jpg)

-   Filename: Controls the output filename, arranged logically.
-   categories: The dozen-ish categories, shown at the top, determining the template.
-   Title Line 1: Titles can be one or two lines, split for manual line breaks.
-   Title Line 2: Optional; if blank, it's a single-line title.
-   Description: The optional keywords, determining if the box below is shown.
-   Taobao: Yes/no, toggles the Taobao logo, based on Category.
-   Tmall: Yes/no, toggles the Tmall logo, based on Category.
-   Single Line: Yes/no, controls the single-line title layer, based on Title Line 2.
-   Two Lines: Yes/no, controls Title Line 1 and 2 layers, based on Title Line 2.
-   Has Description: Yes/no, controls the description box, based on Description.
-   Background Image: Path for the background image.
-   Foreground Color: Path for the color image, used for title text color.

![](https://cdn.victor42.work/posts/2024-06/f0990a616f2f602bcdd42a44bb01df9e.jpg)

Explanation: I had three title layers. One for single-line, two for two-line titles.

Giving this to operations would be brutal. Most could be calculated. Operations only needed: Category, Title Line 1, Title Line 2, and Description. I made an online spreadsheet with just those four and sent it out. We had 5-6 people working, each taking categories. They finished fast.

The hard part was mine: calculating the rest, all needed for Photoshop. None could be skipped. Category was key. It determined the logos, background, text color, and filename sorting. So, I made a separate Category table, a dimension table, where each category was like a product. The image content table was the fact table, like an order. Category name was the dimension table's primary key, a foreign key in the fact table, pulling in category info. One fact table (CSV) and one dimension table – a simple star schema, or maybe "Earth-Moon schema"?

![](https://cdn.victor42.work/posts/2024-06/6d4da5705eb81be2c0eee26a2cf600a7.jpg)

These concepts are from data modeling and databases. Simply, it's defining attributes on Category. Anything in a category would auto-read the background, color, etc., based on the name. This matched the requirements.

![](https://cdn.victor42.work/posts/2024-06/a536f153f4837dc8de1937558ca0482d.jpg)

All the operations data (4 columns) was now in my Excel. I referenced it, added the calculated columns, and formed a complete table. I updated, saved as CSV, and gave it to Photoshop.

![](https://cdn.victor42.work/posts/2024-06/3edc562bdfee2fb96d5271d682185f6b.jpg)

These calculated columns tested my Excel skills:

-   `vlookup` was crucial for looking up category attributes.
-   Filenames needed text concatenation. I could combine them freely, deciding the output order.
-   I used string replacement to remove spaces in titles, ensuring centering even with accidental spaces.
-   `IF` checked for empty values, preventing 0 on empty rows.

These are easy for Excel users, so I won't detail them.

## Merging Tables with Power Query

But, two questions remained:

1.  How did operations' data get into my Excel?
2.  How do I update it?

![](https://cdn.victor42.work/posts/2024-06/800867584af30783c478924a6db86fdd.jpg)

First: The online spreadsheet let people work independently and update in real-time. My table was local because I needed Excel's Power Query for merging, which most online spreadsheets lack.

![](https://cdn.victor42.work/posts/2024-06/521925ce776cc959e7698c66e0969042.jpg)

For each batch, I downloaded the online spreadsheet (`Course Cover Content Collection.xlsx`) to the same directory as my table (`Course Cover Content.xlsx`). The data link would stay as long as the location didn't change.

![](https://cdn.victor42.work/posts/2024-06/2878de8a5b1e67e4846803c6e585a9b3.jpg)

I used Power Query from the "Data" menu. Think of it as a visual SQL. It reads data from local tables, web pages, databases, and Azure, and cleans, transforms, and aggregates it. I used its local table reading.

![](https://cdn.victor42.work/posts/2024-06/be21ed673a8ff88073305b48f847fefd.jpg)

The Power Query interface is both familiar and strange to basic Excel users. Familiar: "Tables!" Strange: "What's all this?"

Understanding Power Query: It does three things:

1.  Specifies the data source.
2.  Sets rules and conditions.
3.  Executes and loads data, one request per sheet.

![](https://cdn.victor42.work/posts/2024-06/af1dc0620c1d62b971ac405eddbb55cc.jpg)

Step two is crucial. The left list is a series of requests, executed in order.

Each needs "Use First Row as Headers" and removal of empty values.

![](https://cdn.victor42.work/posts/2024-06/69054b9e157cd497d0ede7fa9d85a547.jpg)

It's not just filtering and sorting. I used its table merging. Operations' data was scattered. I couldn't copy-paste, right? I queried each sheet, then created an append request, combining tables with the same format, like SQL's `CROSS JOIN`.

![](https://cdn.victor42.work/posts/2024-06/137c056d4946b2367dc3259518c0e5dd.jpg)

Its merge query is also useful, like SQL's `JOIN` and `LEFT JOIN`.

![](https://cdn.victor42.work/posts/2024-06/66b4091f7dfc0ebf0448baf72b6509c0.jpg)

"Close" (actually save) made a bunch of sheets appear. I deleted unneeded ones. I added a sequence number for filename sorting.

All operations data was now in.

Second question: updating?

![](https://cdn.victor42.work/posts/2024-06/e56e2966a217111a4a10f15db546dd42.jpg)

New batch? Download, overwrite, open the data table, "Data" menu, "Refresh." Simple.

Why compare to SQL? It records query *conditions*, not results. Results are shown, but it's a preview. It records requests and re-queries on "Refresh."

After complex initial setup, the pipeline was set. Use was simple: download, overwrite, refresh, save as CSV – Photoshop's data file.

## Batch Image Generation in Photoshop

Photoshop had five steps:

1.  Organize/rename layers.
2.  Define variables.
3.  Import data.
4.  Batch export PSDs.
5.  Batch convert to JPGs.

### 1. Organize and Rename Layers

![](https://cdn.victor42.work/posts/2024-06/531b776b93a3a94233d9c2842edd7612.jpg)

Not hard. Merge, reorder. Name layers according to table headers for easier variable definition.

"Filename" is special; it's not visible. I created it manually. Style doesn't matter. Hide it.

"Foreground Color" needed special handling. Variables can't directly change text color. For background-based changes: group the text, create a solid color layer, and use a clipping mask. This gives unified control.

![](https://cdn.victor42.work/posts/2024-06/a9a688b8e6f7b88860fa0b00a4b79c1b.jpg)

The box's line color? Related to text, but not the same. Add a Hue/Saturation layer for the lines, increasing saturation and brightness. Brown becomes orange, dark green becomes grass green... This needs color theory and Photoshop knowledge.

### 2. Define Variables for Layers

No step-by-step; the linked tutorial covers it. I'll discuss tricky points.

![](https://cdn.victor42.work/posts/2024-06/ea2af0bf27f4c74c49db871f5c2b7296.jpg)

Common use: "Text Replacement." Non-text layers become "Pixel Replacement" – image change. Background is replaced this way.

![](https://cdn.victor42.work/posts/2024-06/5be7d1ed67cc798dc3a2925f3e07cc84.jpg)

Foreground color is similar. Prepare color images, define the clipping mask as a variable, select based on category.

![](https://cdn.victor42.work/posts/2024-06/46b0372dc8bd46ffed011eae85e6bb28.jpg)

Visibility variables are useful. TRUE/FALSE control display. Can be used with text/pixel replacement. Description text: text replacement changes content, visibility controls display.

![](https://cdn.victor42.work/posts/2024-06/a740f3312e02a860493537f9e78b80c0.jpg)

These first two steps, though tedious, are one-time.

### 3. Import Data Sets

![](https://cdn.victor42.work/posts/2024-06/e1fbcc63e3a13d31e181c8a1f12db265.jpg)

Import the CSV.

Two common errors: extra/mismatched columns, and empty cells. Photoshop doesn't support empty cells, so I used NULL, with visibility checks.

### 4. Batch Export PSDs

![](https://cdn.victor42.work/posts/2024-06/d92857c1843b212c5205b9d0582f88b2.jpg)

No trick; do it like this.

![](https://cdn.victor42.work/posts/2024-06/7dceeaca255670e1437a37b68e773e31.jpg)

Define filename format. "Data Set Name" is useful; it's the first column, "Filename," allowing customization.

### 5. Batch PSD to JPG Conversion

PSDs need conversion.

![](https://cdn.victor42.work/posts/2024-06/c36d844e7381a77f1c02718a560fe9f8.jpg)

Record a simple action: open, save as JPG, close. Batch process the PSD folder.

My action set has "Save as JPG"; link at the end.

## One More Table

Done? Task complete, but not the matter. One crucial table is missing.

These 800+ images (16,000 RMB) are just the first batch. More will come. Shouldn't I know the yearly savings? Even if I don't, the boss should.

![](https://cdn.victor42.work/posts/2024-06/fa9ce9f2b382b99c6cad7125d176799b.jpg)

So, a statistics table, a "bragging table." Let's call it "Rock and Roll Table."

I could even make a chart, showing monthly/quarterly/seasonal value. Subtract from my salary to show my cost – hiring me is a steal! Data is there; whether I do it is TBD.

## Epilogue

This was cost-effective. Half a day for initial setup. Negligible time after; I ran it during lunch.

This is my strength. I don't reinvent wheels, but I assemble them well.

After setup, I met with operations. Marketing explained the four columns. No one found it hard. Operations thought I used AI. For non-tech people, anything amazing is AI. AI is the silver bullet. It's funny; I'm used to it.

Finally, resources. Try it yourself:

-   [PS+Excel Batch Output Basic Tutorial](https://zhuanlan.zhihu.com/p/33725280)
-   [Workflow Files](https://qvokpfxqsh.feishu.cn/file/PGx8bMjyrohPp2x4DZ9ct0A9nIf)
-   [PS Action Set (click the table of contents to jump)](https://qvokpfxqsh.feishu.cn/docx/SK0UdUPphoFBZpxJpEJcbZIsnRf)
