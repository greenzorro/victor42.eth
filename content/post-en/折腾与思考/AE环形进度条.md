---
title: Creating a Circular Progress Bar in AE
description:
image:
date: 2015-02-10 15:16:00
categories: 折腾与思考-Geek
url: /post-en/3424
translationKey: '3424'
---

[Update: Simpler methods exist (see the end of the post). However, the techniques here are still valuable practice.]

I've been using After Effects for about a year. It's fun, useful, and easy to learn, especially with prior Flash experience. Complex UI animations are combinations of basic movements, rotations, scaling, opacity, and color changes. Online resources abound; I learned from this [video series](http://v.youku.com/v_show/id_XMjMyNzk0NjQ4.html?f=5405564).

This circular progress bar requires a bit more thought.

![The final animated circular progress bar created in After Effects](https://cdn.victor42.work/posts/2015-02/02-09/1.gif)

## The Idea

Circular progress bars are unique. They rotate while selectively revealing parts of the circle, which isn't immediately straightforward.

I drew inspiration from a [CSS3 circular progress bar](http://greenzorro.github.io/demo/css/%E7%8E%AF%E5%BD%A2%E8%BF%9B%E5%BA%A6%E6%9D%A1.html) I created earlier. The core concept involves splitting the circle in half. The dark green (progress) is the background and remains static. Two light green semicircles cover it, rotating sequentially to reveal the progress.

To create a ring, add a smaller circle on top. AE layer masks achieve a similar effect (explained later).

AE can create a truly transparent circular progress bar, but the core principle remains: rotating two semicircles independently. See the diagram below:

![Demonstration gif of the rotation principle using red, blue, and purple semicircles](https://cdn.victor42.work/posts/2015-02/02-09/2.gif)

Divide the circle into left (red) and right (blue) semicircles, restricting their visibility to their respective halves. Add a static right semicircle (purple) underneath. Let's break it down step by step.

## Left, Right, and Background Semicircles

First, prepare the three semicircles.

![Three static semicircle layers prepared in the After Effects timeline](https://cdn.victor42.work/posts/2015-02/02-09/1.png)

Create a 720p composition.

![Composition Settings panel in AE set to 1280x720 resolution](https://cdn.victor42.work/posts/2015-02/02-09/2.png)

Draw a 400x400 circle.

![Setting the ellipse path size to 400x400 in AE shape layer](https://cdn.victor42.work/posts/2015-02/02-09/3.png)

Set the circle's position (not the shape layer's) to 0, 0 for perfect centering.

![Centering the ellipse path by setting its position to 0,0 in AE](https://cdn.victor42.work/posts/2015-02/02-09/4.png)

In the same shape layer, draw a 200x400 rectangle (half the circle's size).

![Creating a 200x400 rectangle path in the same shape layer](https://cdn.victor42.work/posts/2015-02/02-09/5.png)

Set the rectangle's position to -100, 0 to cover the circle's left half. This rectangle will cut out the semicircle.

![Positioning the rectangle at -100,0 to cover the left half of the circle](https://cdn.victor42.work/posts/2015-02/02-09/6.png)

Click "Add" and choose "Merge Paths".

![Selecting Merge Paths option from the Add menu in AE shape layer](https://cdn.victor42.work/posts/2015-02/02-09/7.png)

Set the mode to "Intersect" (like path operations in PS/AI).

![Setting the Merge Paths mode to Intersect in After Effects](https://cdn.victor42.work/posts/2015-02/02-09/8.png)

Group (Command/Ctrl + G) the circle, rectangle, and Merge Paths. This is our semicircle.

![Grouping the ellipse, rectangle, and Merge Paths inside Group 1](https://cdn.victor42.work/posts/2015-02/02-09/9.png)

Expand the group, copy the inner rectangle, and paste it outside the group.

This new rectangle acts as a vector mask. AE's built-in masks rotate with the layer, which we don't want. We need a stationary mask and a rotating semicircle. So, we use "Merge Paths" again.

![Adding a second rectangle and Merge Paths outside Group 1 for masking](https://cdn.victor42.work/posts/2015-02/02-09/10.png)

Add -> Merge Paths, setting the mode to "Intersect". This creates the intersection of the new rectangle and the group.

![Rotating Group 1 in AE, with parts outside the mask hidden](https://cdn.victor42.work/posts/2015-02/02-09/11.png)

Rotating the group now shows that the area outside the rectangle is hidden.

![Adding a keyframe to the rotation property of Group 1](https://cdn.victor42.work/posts/2015-02/02-09/12.png)

Reset the rotation and add a keyframe to the group's rotation (for later use). Press "u" to quickly access keyframed properties.

![Renaming the shape layer to Left Semicircle in the timeline](https://cdn.victor42.work/posts/2015-02/02-09/13.png)

Name this layer "Left Semicircle".

![Setting the outer mask rectangle position of Right Semicircle layer to 100,0](https://cdn.victor42.work/posts/2015-02/02-09/14.png)

Duplicate the layer (Command/Ctrl + D) for the right semicircle. Set the *outer* rectangle's position to 100, 0 (covering the right half). Nothing appears because the semicircle is still on the left.

To clarify: the inner circle and rectangle form the rotating semicircle. The outer rectangle is the mask. The left semicircle's mask covers the left; the right semicircle's mask covers the right. Together, they form a full circle.

![Left, Right, and Background Semicircle layers ordered in the AE timeline](https://cdn.victor42.work/posts/2015-02/02-09/15.png)

Duplicate the right semicircle, rename it "Background Semicircle," and move it to the bottom. Set the *inner* rectangle's position to 100, 0. The circle becomes whole again.

The static assets are now ready.

## Creating the Rotation Animation

Let's animate the semicircles.

![AE timeline showing only rotation properties with keyframes](https://cdn.victor42.work/posts/2015-02/02-09/16.png)

Press "u" to show only the rotation property with the keyframe. This is the *group's* rotation, not the layer's.

Remove keyframes from the right and background semicircles' rotation. Keep the right semicircle's rotation property visible.

![Enabling the Solo switch for Left Semicircle layer in AE](https://cdn.victor42.work/posts/2015-02/02-09/17.png)

Click the dot on the left semicircle layer to solo it (like Alt + clicking the layer eye in PS).

![Creating a 360-degree rotation animation keyframe for Left Semicircle](https://cdn.victor42.work/posts/2015-02/02-09/18.png)

Create a simple animation: one full rotation.

![Activating expression input on Right Semicircle's rotation by Alt-clicking](https://cdn.victor42.work/posts/2015-02/02-09/19.png)

Important: Alt + click the right semicircle's rotation property. An expression appears in the timeline.

![Linking Right Semicircle's rotation to Left Semicircle using Pick Whip](https://cdn.victor42.work/posts/2015-02/02-09/20.png)

Drag the right semicircle's rotation property's pick whip (spiral icon) to the left semicircle's rotation property. The expression updates.

Alt + clicking activated the expression. Dragging the pick whip links the right semicircle's rotation to the left's. Now, the right semicircle always follows the left.

![Disabling Solo switch on Left Semicircle layer to restore view](https://cdn.victor42.work/posts/2015-02/02-09/21.png)

Turn off solo display for the left semicircle.

![Red, blue, and purple colored semicircles visible in the AE canvas](https://cdn.victor42.work/posts/2015-02/02-09/22.png)

For clarity, fill the semicircles with different colors (for demonstration only).

Use red for the left, blue for the right, and purple for the background semicircle, matching the "Idea" section's diagram.

## Finding the Critical Frame

Play the animation. It's incorrect: the left semicircle is visible initially. It should appear only after the right semicircle rotates halfway. The same applies to the background semicircle.

We need a specific frame where the left and background semicircles are hidden.

![Locating the playback head at the critical 180-degree rotation frame](https://cdn.victor42.work/posts/2015-02/02-09/23.png)

This critical frame is when the right semicircle reaches 180 degrees (or slightly more).

![Trimming the in-points of Left and Background Semicircles to the critical frame](https://cdn.victor42.work/posts/2015-02/02-09/24.png)

Select the left and background semicircles and trim their timelines' left ends to this frame. They won't appear too early now.

![Clicking the Graph Editor button to adjust motion curves in AE](https://cdn.victor42.work/posts/2015-02/02-09/25.png)

Playback is now correct!

The constant-speed rotation is unnatural.  Open the Graph Editor (graph icon). Select the left semicircle's rotation to see a straight line.

![Converting linear keyframes to Bezier curves in Graph Editor](https://cdn.victor42.work/posts/2015-02/02-09/26.png)

Select the line and click the two-handled icon. The line curves, and handles appear.

The Graph Editor is simple: the horizontal axis is time; the vertical is value change. A flat curve means slow change; a steep curve means fast change.

![Adjusting the Bezier handle to create an ease-out speed curve](https://cdn.victor42.work/posts/2015-02/02-09/27.png)

For a fast-start, slow-end animation, adjust the curve like this:

![Re-aligning layer in-points based on the newly adjusted ease curve](https://cdn.victor42.work/posts/2015-02/02-09/28.png)

Find the critical frame again (right semicircle at 180 degrees or slightly beyond).

## Adding a Mask

The circular progress bar is done; let's make it a ring.

![Right-clicking the selected layers to choose Pre-compose in AE](https://cdn.victor42.work/posts/2015-02/02-09/29.png)

Select all layers and Pre-compose (right-click).

![Confirming settings in the Pre-compose options dialog in AE](https://cdn.victor42.work/posts/2015-02/02-09/30.png)

The three layers merge (like a Smart Object in PS or Movie Clip in Flash).

Create a mask (Command/Ctrl + Shift + N) - AE's built-in layer mask.

![Adding a full-size rectangular mask to the new pre-composition layer](https://cdn.victor42.work/posts/2015-02/02-09/31.png)

The mask is a rectangle. Expand the mask menu and click "Mask Path".

![Opening the Mask Shape settings dialog to redefine the mask bounds](https://cdn.victor42.work/posts/2015-02/02-09/32.png)

Set the four values (top, left, bottom, right) as shown, and check the box to make it a circle.

![Setting the mask coordinates and checking Reset to Ellipse option](https://cdn.victor42.work/posts/2015-02/02-09/33.png)

These numbers ensure the circular mask matches the progress bar's size and position.

![Checking the Inverted option on the mask to hide the inner circle](https://cdn.victor42.work/posts/2015-02/02-09/34.png)

Check "Inverted". The circle disappears because the mask now shows the area *outside* it.

![Scaling down the inverted circular mask from center to form the ring](https://cdn.victor42.work/posts/2015-02/02-09/35.png)

Select the mask and press Command/Ctrl + T.

Hold Command/Ctrl + Shift to scale from the center, making it slightly smaller. The ring appears.

![The final animated circular progress bar created in After Effects](https://cdn.victor42.work/posts/2015-02/02-09/1.gif)

Done! That's the progress bar I wanted.

## Conclusion

This tutorial is lengthy, focusing on the concepts. The actual process is simple and takes about 5 minutes with practice.

For the lazy, here's the source file: [Here's the source file](http://pan.baidu.com/s/1eQxSE6A)

I'm a beginner, so this might not be the *best* method, just *a* method. Path animations might offer a simpler solution.

Share if you have a better method!

[Update: I received immediate feedback. "Radial Wipe" and "Trim Paths" are easier. "Radial Wipe" is a one-step solution. See the "Growing Circle" section in [this article](http://www.zcool.com.cn/article/ZNDkzNDg=.html).]
