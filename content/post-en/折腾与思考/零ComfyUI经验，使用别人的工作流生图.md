---
title: Using Liblib ComfyUI Workflows with Zero Experience
description: It's as easy as using a mini-app. No experience needed.
image: https://cdn.victor42.work/posts/2025-02/65e10ec43957abff3dbb183248e33bd3.webp
date: 2025-02-27 12:15:00
categories: 折腾与思考-Geek
url: /post/en/comfyui-workflow-tutorial-for-newbies
translationKey: comfyui-workflow-tutorial-for-newbies
---

[LiblibAI](https://www.liblib.art/workflows)

Liblib offers many free workflows for tasks regular image generators can't handle, like **face-swapping, dressing up models, adding lighting and backgrounds to product photos, and creating memes**. You get free generations daily, and you can pay for more if needed.

ComfyUI is essentially an image generation program. Don't worry about the details now:

![](https://cdn.victor42.work/posts/2025-02/65e10ec43957abff3dbb183248e33bd3.webp)

Liblib's workflows are based on ComfyUI. You don't need to know how to create them, but you should know how to use them. There are three common scenarios:

## 1️⃣ The workflow is packaged as an app (you'll see a specific button)

![](https://cdn.victor42.work/posts/2025-02/46c26df9a8577c9cdf77aae4af49f1f1.webp)

Click it, and you're set. It's straightforward, and you won't see the underlying program.

![](https://cdn.victor42.work/posts/2025-02/caefee5ee6854594b0e273f148ddbc46.webp)

## 2️⃣ It's not an app, and you see a light blue "Run" button

![](https://cdn.victor42.work/posts/2025-02/421edc7a9ebe6cf69aa23245d5d0ea01.webp)

Clicking this takes you to the ComfyUI interface, a black screen that might take a moment to load. It can look complex, like a circuit board.

However, creators usually include instructions. These vary, so find and read them carefully. Here's an example:

![](https://cdn.victor42.work/posts/2025-02/7d652a7e19399a3c53683aa792a38bb7.webp)

## 3️⃣ You see a light blue "View Workflow" button, but no instructions

![](https://cdn.victor42.work/posts/2025-02/b78bb6863e56b1c86be4bfd3feb0a5d5.webp)

This likely means the creator didn't add instructions. Check if the workflow is overly complex.

**Tip: Zoom with the mouse wheel, and drag by holding the spacebar.**

1.  If it seems simple, with few components, there's hope. Find these two key node types:

    -   Image upload node: (look for the "choose file to upload" button): ![](https://cdn.victor42.work/posts/2025-02/88465060dc6397b6e62a5bfca4b1d89f.webp)
    -   Text input node: (look for a black input box for prompts): ![](https://cdn.victor42.work/posts/2025-02/09dbc0f7779d7896470f8ffc876d936d.webp)

    Upload images, write text, and click "Run." It should work.

2.  If it's too complicated, with many image and text nodes, find a similar workflow with instructions.

---

## ⚠️ Troubleshooting Errors

You might encounter errors:

![](https://cdn.victor42.work/posts/2025-02/1ae88573acbc157fb7bf1443a68dcb25.webp)

Don't worry! Close the error; the program will highlight the problem node in red:

![](https://cdn.victor42.work/posts/2025-02/c024ed1135e6e390d941dfa607010b77.webp)

Zoom in. It's usually a node for loading an AI model:

![](https://cdn.victor42.work/posts/2025-02/53f255d839ade35227ea9c02e782517b.webp)

The creator likely used their local file names for models. On Liblib, the names might differ, causing the node to fail.

Here's the fix: Note the names of each option, especially the part before the decimal (the model name). Click on each model and select the closest match from the dropdown (exact matches are best):

![](https://cdn.victor42.work/posts/2025-02/c460eab80d6db0ff96dac59993a8ca9e.webp)

Reselect models for all faulty nodes, then run it again.

If you can't find a match, search on [Liblib's Model Plaza](https://www.liblib.art/), add it to your library, and it'll appear in the dropdown.

This solves most errors.