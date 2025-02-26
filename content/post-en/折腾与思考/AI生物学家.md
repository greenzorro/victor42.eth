---
title: My AI Biologist
description: I built an AI biologist, but it got stumped by the seafood market.
image: https://cdn.victor42.work/posts/2024-03/27b2a2b1d435b113.jpg
date: 2024-03-20 15:06:00
categories: 折腾与思考-Geek
url: /post/en/en/3649
translationKey: 3649
---

![](https://cdn.victor42.work/posts/2024-03/27b2a2b1d435b113.jpg)

Here's a funny thing that happened. My family sent me some seafood, labeled "Guyanyu," a Shandong specialty. It looked flat, obviously a flatfish, maybe a flounder. I asked several AIs about "Guyanyu," and they all invented some nonexistent species. I figured I'd be identifying species often, so I should create an AI biologist persona prompt for more professional answers. And so I did:

> Your task is to act as a knowledgeable biologist. I will ask you about some creatures. You will give me a brief introduction of this species, including bio taxonomy, species range, evolution history, noticeable feature and anything else you find important. Pay extra attention to the creature names I tell you since they may be far from accurate or academical, sometimes wrong due to misuses by non-biologists. Make sure to check some possible alternative names with similar pronunciation or spelling. If you have access to the Internet, you must search the web for answer. When you find no reliable answer, search for those alternative names instead. Answer in "Simplified Chinese" regardless of the language I use.
> The first creature I’m interested in is "orca".
This way, the AI can help me build a basic but comprehensive understanding of a creature, covering its taxonomy, distribution, evolutionary history, and notable features. My prompt asked about orcas, and all the AIs provided satisfactory answers.

The AIs initially hallucinated "Guyanyu" because, well, the name's misleading.  Colloquial names for species can be wildly inconsistent. My local grocery, for instance, caters to less savvy shoppers by using simplified characters on their signs: "里几肉" (lijirou) instead of "里脊肉" (lirou, pork tenderloin), and "卢鱼" (luyu) instead of "鲈鱼" (luyu, sea bass).  This isn't just a consumer-facing quirk; it likely happens throughout the supply chain. "Guyanyu" probably fell victim to the same issue. A quick Google search showed that in Shandong, it's called "Guyanyu" (鼓眼鱼, bulging-eye fish). This fits the flatfish description, and sure enough, further digging confirmed it was a type of flatfish.

I wanted my AI biologist to handle these curveballs. So, the prompt's second half stresses paying close attention to potentially inaccurate or misused names, checking for homophones and similar spellings, and using web searches to validate those possibilities.

I tested it again with "Guyanyu," and one AI nailed it. Prompt engineering for the win!

Google Gemini was the only one to get it right, actually connecting similar names and searching for alternatives.

> "Guyanyu" (Gǔ yǎn yú)
> There's no corresponding species for the name "Guyanyu" in biological taxonomy. However, based on its pronunciation and meaning, it could refer to two types of fish:
> *   "Guyanyu" (鼓眼鱼, Gǔ yǎn yú): This fish is closer to the literal meaning of "Guyanyu." They are a type of benthic fish in the order Pleuronectiformes (flatfish), with a flat body and asymmetrical features, with one eye on the upper side. "Guyanyu" are widely distributed in the coastal waters of all continents and are also common along the coast of China. They are especially popular in Qingdao. They are commonly fried or pan-fried, resulting in a crispy exterior and tender interior.
> *   "Gaoyandie" (高眼鲽, Gāo yǎn diè): This is another possibility, as "Gu" and "Gao" have similar pronunciations. "Gaoyandie" is also a member of the Pleuronectiformes order. Their eyes are located on the upper side of the body, but they don't protrude like those of "Guyanyu." "Gaoyandie" are mainly distributed in the deep sea areas of the North Pacific. They are larger than "Guyanyu" and have higher economic value.
> Both species are commonly consumed sea fish, and both have one eye on the upper side of their body. The specific type of fish depends on the context or local customs.

Perplexity (using Claude 3 Sonnet) and Poe's Web search (using GPT-3.5), both designed for web searching, missed the mark. They're optimized for search, so they ignored my instruction to look for similar names. When "Guyanyu" didn't turn up anything, they just started inventing facts – no better than before.

**Perplexity**

> ## Introduction to Guyanyu
>
> Guyanyu (Ophthalmolepis) is an extinct genus of fish belonging to the ancient order of lungfish. They lived during the Devonian and Carboniferous periods, from 560 to 360 million years ago.
>
> ## Taxonomy
>
> Guyanyu belongs to:
> Kingdom: Chordata
> Phylum: Fish
> Class: Sarcopterygii
> Order: Dipnoi
> Family: Ophthalmolepididae
>
> ## Distribution
>
> Guyanyu fossils are widely distributed in Europe, North America, Greenland, China, and other regions. Their habitats included marine and freshwater environments.
>
> ## Evolutionary History
>
> Guyanyu is one of the earliest lungfish groups and is considered an ancestor of modern amphibians and reptiles. They had a fish-like body but had developed primitive lungs, allowing them to survive briefly in anoxic environments. This feature enabled them to adapt to environments such as tidal zones, paving the way for later terrestrial life.
>
> ## Notable Features
>
> *   Large head with high and prominent eyes, hence the name "Guyanyu"
> *   Low mouth position, suitable for feeding on benthic organisms
> *   Flat body with elongated dorsal and anal fins
> *   Possessing both internal lungs and gills, with a respiratory method between fish and amphibians
>
> Guyanyu fossils are of great significance for studying the transition of vertebrates from aquatic to terrestrial life.

**Web search**

> Guyanyu (Konosirus punctatus), also known as yellowfin gizzard shad, flat gizzard shad, air bubble fish, oil fish, and gizzard shad, is a species of fish in the family Clupeidae. It feeds on plankton and is mainly distributed in the South China Sea, East China Sea, Yellow Sea, and Bohai Sea [[2]](https://baike.sogou.com/v101570476.htm). Here is some important information about Guyanyu:
>
> Taxonomy:
> - Kingdom: Animalia
> - Phylum: Chordata
> - Subphylum: Vertebrata
> - Class: Actinopterygii
> - Order: Clupeiformes
> - Family: Clupeidae
> - Genus: Konosirus
> - Species: Konosirus punctatus
>
> Characteristics:
> - Guyanyu has a laterally compressed, elongated oval body, generally 13-16 cm in length, and does not grow large [[2]](https://baike.sogou.com/v101570476.htm).
> - The dorsal side is blue-green, and the ventral side is silver-white.
> - It has one dorsal fin, and the last fin ray is elongated into a filament, like a long whisker.
> - The dorsal and caudal fins are yellow-green, the pectoral fins are light yellow-green, and the pelvic and anal fins are lighter in color.
>
> Evolutionary History:
> There is currently no reliable information on the evolutionary history of Guyanyu.
>
> Other Names:
> Guyanyu also has other common names, such as yellowfin gizzard shad, flat gizzard shad, air bubble fish, oil fish, and gizzard shad [[2]](https://baike.sogou.com/v101570476.htm).
>
> Learn more:
> 1. [The Unassuming Guyanyu Costs 30 Yuan per Jin, a Qingdao "Exclusive" Delicacy, Fragrant and Delicious When Fried](https://www.sohu.com/a/491048259_100022807)
> 2. [Guyanyu - Sogou Baike](https://baike.sogou.com/v101570476.htm)
> 3. [The Unassuming Guyanyu Costs 30 Yuan per Jin, a Qingdao "Exclusive" Delicacy, Fragrant and Delicious When Fried | Mackerel | Pomfret | Knife Fish_NetEase Subscription](https://www.163.com/dy/article/GKBO40CG0522UM59.html)

Finally, Claude 3 Sonnet, without web access, gave it a shot. It considered similar names, but not quite as I'd intended. And without the web, it couldn't possibly answer correctly for such niche knowledge.

> Okay, I will do my best to answer your question about the creature "Guyanyu" in Chinese.
>
> "Guyanyu" may refer to two different creatures:
>
> 1.  Brownie Glass Eyed
> This is a small tropical fish belonging to the family of glass-eyed fish. They are widely distributed and can be found along the coasts of the Western Pacific and Indian Oceans. This fish is famous for its large, laterally compressed body and large eyes, and is considered one of the most primitive species in the family of glass-eyed fish. They mostly live in shallow sea areas and feed on algae and small invertebrates.
>
> 2.  Lungfish
> This is an ancient lungfish animal that is considered to be a transitional link from fish to amphibians and reptiles. There are 6 existing species of lungfish, mostly distributed in Africa, South America, and Australia. They have some special structures and habits, such as being able to periodically curl up in mud pits to survive the dry season, and using lungs and skin to breathe. Lungfish are considered to have retained relatively primitive characteristics during evolution.
>
> If you are referring to other creatures, please provide more detailed information, and I will try my best to search and answer your questions.

For information-consulting AIs, reasoning and search are key. But are they enough? How they work *together* matters.

This example suggests that letting the AI decide *when* and *how* to search, based on its reasoning, is more adaptable. However, current search-focused AIs treat reasoning and searching as separate. They search once, then reason based on the results – a one-two punch that can't handle these tricky situations. Even Perplexity, a dedicated search AI, only adds a pre-search intent analysis. Either its analysis lacks the necessary logic, or it's limited to a single search per turn, leaving it stuck.

My AI biologist is still a work in progress, especially with edge cases, but it's getting there. The takeaway isn't the prompt itself, or which AI is best, but the sheer complexity of natural language. Truly understanding all its nuances and variations? That's a long road ahead for AI.
