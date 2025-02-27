---
title: Using ComfyUI Workflows with Zero Experience
description: It's as easy as using a mini-app. No experience needed.
image: https://cdn.victor42.work/posts/2025-02/65e10ec43957abff3dbb183248e33bd3.webp
date: 2025-02-27 12:15:00
categories: 折腾与思考-Geek
url: /post/en/comfyui-workflow-tutorial-for-newbies
translationKey: comfyui-workflow-tutorial-for-newbies
---

[LiblibAI - A Leading AI Creation Platform in China](https://www.liblib.art/workflows)

Liblib offers many free workflows for advanced image generation tasks like **face swapping, model dressing, product photo lighting/backgrounds, and meme creation**. There's a daily free quota, with paid options for heavier use.

ComfyUI is the underlying image generation engine. Don't worry about the technical details right now:

![](https://cdn.victor42.work/posts/2025-02/65e10ec43957abff3dbb183248e33bd3.webp)

Liblib's workflows are essentially ComfyUI programs. You just need to know how to use them, not how to build them. Here are the three scenarios you'll encounter:

## 1️⃣ The Workflow Has a "Run" Button

![](https://cdn.victor42.work/posts/2025-02/46c26df9a8577c9cdf77aae4af49f1f1.webp)

This means the creator packaged the workflow as an app. Click, run, and you're good to go. You won't see the underlying complexity.

![](https://cdn.victor42.work/posts/2025-02/caefee5ee6854594b0e273f148ddbc46.webp)

## 2️⃣ No App, Just Light Blue Buttons

![](https://cdn.victor42.work/posts/2025-02/421edc7a9ebe6cf69aa23245d5d0ea01.webp)

![](https://cdn.victor42.work/posts/2025-02/b78bb6863e56b1c86be4bfd3feb0a5d5.webp)

These buttons open the ComfyUI interface. Expect a black screen and a bit of a wait. It'll look like a complex circuit board.

Creators usually include instructions. Find and read them—they'll vary. Example:

![](https://cdn.victor42.work/posts/2025-02/7d652a7e19399a3c53683aa792a38bb7.webp)

## 3️⃣ Light Blue Buttons, No Instructions

The creator skipped the instructions. First, check the workflow's complexity.

**Tip: Mouse wheel zooms, spacebar + drag moves the view.**

If it's simple (few nodes), you can probably still use it. Look for these two key node types:

-   Image uploads (look for the "choose file to upload" button): ![](https://cdn.victor42.work/posts/2025-02/88465060dc6397b6e62a5bfca4b1d89f.webp)
-   Text input (a black input box, usually for prompts): ![](https://cdn.victor42.work/posts/2025-02/09dbc0f7779d7896470f8ffc876d936d.webp)

Upload images, add prompts, and run. It should work.

If it's too complex, find a different workflow with instructions.

---

## ⚠️ Troubleshooting Errors

You might see errors pop up:

![](https://cdn.victor42.work/posts/2025-02/1ae88573acbc157fb7bf1443a68dcb25.webp)

Don't worry! Close the error. The program will highlight the problem node in red:

![](https://cdn.victor42.work/posts/2025-02/c024ed1135e6e390d941dfa607010b77.webp)

Zoom in. It's usually a node for loading an AI model:

![](https://cdn.victor42.work/posts/2025-02/53f255d839ade35227ea9c02e782517b.webp)

The creator likely used their local model file names. These might not match Liblib's. The node can't find the correct model.

Here's the fix: Note the names of each option, especially the part before the decimal (the model name). Click each model and choose the closest match from the dropdown (exact matches are best):

![](https://cdn.victor42.work/posts/2025-02/c460eab80d6db0ff96dac59993a8ca9e.webp)

Re-select models for all error nodes, then run again.

This fixes most errors.