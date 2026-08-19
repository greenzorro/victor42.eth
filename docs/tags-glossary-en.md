# Tag Glossary (English)

The canonical **English** tag vocabulary. It governs tags on English articles (`content/post-en/`). The Chinese glossary (`tags-glossary.md`) governs Chinese articles (`content/post/`); the two files are maintained independently and do not mirror each other.

Each tag appears once. When different categories reuse the same tag, update the original entry's definition and scope — do not add a duplicate. Actual usage counts, article lists, and glossary gaps are generated into `docs/tags-stats.generated.md`.

## Entry format

    ### `tag`
    - **Definition**: what this tag covers
    - **Use**: which articles it fits
    - **Don't use**: common misuses to avoid
    - **Synonyms/retired**: retired synonyms, near-words, or over-fine words

## Maintenance rules

- Before adding any tag, check this file first; prefer reusing an existing canonical tag.
- Do not maintain usage counts here; counts come from `docs/tags-stats.generated.md`.
- One-shot tags must be judged as proper nouns worth keeping; otherwise roll up to a more general tag.
- When maintaining tags, run `scripts/generate_tags_report.py` from the repo root to refresh the generated report.
- Tags are maintained by the tag itself, not partitioned by category.
- The Chinese and English glossaries are independent. A tag used in both languages (e.g. `AI`, `Midjourney`) appears in both files.

---

### `AI`
- **Definition**: artificial intelligence topics, including AI art, AI agents, AI search, AI awakening, etc.
- **Use**: articles substantively discussing AI as a subject
- **Don't use**: articles that merely use an AI tool as a passing means
- **Synonyms/retired**: shared with Chinese glossary

### `AI Art`
- **Definition**: AI-generated visual art (Midjourney, Stable Diffusion, ComfyUI workflows, etc.)
- **Use**: articles about producing, selling, or critiquing AI-generated images
- **Don't use**: general AI discussions that are not about image generation
- **Synonyms/retired**: `AI Painting` (use `AI Art` instead)

### `AI Awakening`
- **Definition**: speculative theme of AI gaining consciousness or agency
- **Use**: fictional or philosophical pieces where AI awakening is central
- **Don't use**: routine AI capability articles
- **Synonyms/retired**:—

### `Adventure`
- **Definition**: adventure as a narrative or experiential theme
- **Use**: fiction or travelogues built around an adventure arc
- **Don't use**: any trip that happens to be fun
- **Synonyms/retired**: —

### `After Effects`
- **Definition**: Adobe After Effects motion-graphics software
- **Use**: tutorials or design breakdowns using After Effects
- **Don't use**: general animation topics not tied to the software
- **Synonyms/retired**: `AE` (use full product name in English)

### `Alien`
- **Definition**: extraterrestrial life as a sci-fi subject
- **Use**: fiction or speculation with first contact / alien civilization
- **Don't use**: metaphorical "alien" feelings
- **Synonyms/retired**: —

### `Animal`
- **Definition**: animal perspectives or animal-centered subject matter
- **Use**: fiction or essays told from or about a non-human animal's viewpoint
- **Don't use**: articles that simply mention animals in passing
- **Synonyms/retired**: —

### `Animation`
- **Definition**: animation craft and motion design
- **Use**: breakdowns or tutorials of animated work
- **Don't use**: static illustrations
- **Synonyms/retired**: —

### `Anthropology`
- **Definition**: anthropology as a lens for understanding humans
- **Use**: essays applying anthropological frameworks (e.g. *Sapiens*-style synthesis)
- **Don't use**: passing references to human evolution
- **Synonyms/retired**: —

### `Apocalypse`
- **Definition**: apocalyptic and post-apocalyptic scenarios
- **Use**: fiction or essays where civilizational collapse is central
- **Don't use**: metaphorical decay
- **Synonyms/retired**: —

### `Architecture`
- **Definition**: buildings, urban form, and architectural history
- **Use**: travel or culture writing where architecture is the main subject (e.g. Forbidden City, Suzhou gardens)
- **Don't use**: generic city-trip articles with no architectural focus
- **Synonyms/retired**: —

### `Automation`
- **Definition**: automating workflows, tasks, or pipelines
- **Use**: articles building or reflecting on automated systems (Port Mindset, Photoshop automation, etc.)
- **Don't use**: one-off scripts that are not about the idea of automation
- **Synonyms/retired**: —

### `Beijing`
- **Definition**: Beijing as a destination or setting
- **Use**: travelogues or cultural pieces centered on Beijing
- **Don't use**: articles that merely pass through Beijing
- **Synonyms/retired**: —

### `Biology`
- **Definition**: biological sciences — organisms, ecosystems, physiology
- **Use**: substantive biology explainers or experiments
- **Don't use**: science articles that are really physics or chemistry
- **Synonyms/retired**: —

### `Blockchain`
- **Definition**: blockchain technology and Web3 infrastructure
- **Use**: articles about on-chain identity (ENS), IPFS, decentralized hosting
- **Don't use**: general crypto-price commentary
- **Synonyms/retired**: `Web3` (use `Blockchain` for now)

### `Book Review`
- **Definition**: review or deep engagement with a specific book
- **Use**: structured reactions to a book's argument (e.g. *Sapiens*)
- **Don't use**: articles that merely quote a book
- **Synonyms/retired**: —

### `Business`
- **Definition**: business models, strategy, market behavior
- **Use**: articles analyzing how a business or market works
- **Don't use**: personal career anecdotes that are not about business logic
- **Synonyms/retired**: —

### `Career`
- **Definition**: career, workplace, and professional identity
- **Use**: essays on job paths, workplace dynamics, designer career growth
- **Don't use**: pure productivity tips unrelated to career arc
- **Synonyms/retired**: `Workplace` (use `Career`)

### `Chemistry`
- **Definition**: chemistry as the article's core science
- **Use**: explainers of chemical phenomena (e.g. how water extinguishes fire)
- **Don't use**: articles that use a chemistry fact as a side note
- **Synonyms/retired**: —

### `Coming of Age`
- **Definition**: coming-of-age or maturation theme
- **Use**: fiction or essays where growth from youth to adulthood is central
- **Don't use**: general `Growth` content not tied to life-stage transition
- **Synonyms/retired**: —

### `Cooking`
- **Definition**: cooking as a craft or reflective practice
- **Use**: pieces focused on the act of cooking or kitchen philosophy
- **Don't use**: food writing that is really about eating or travel
- **Synonyms/retired**: overlap with `Food`; prefer `Cooking` for technique/act, `Food` for ingredient/dish

### `Culture`
- **Definition**: cultural history, customs, and collective meaning
- **Use**: travel or essay writing unpacking a place's culture (Beijing, Xinjiang, Suzhou)
- **Don't use**: generic "cultural" observations with no specific tradition
- **Synonyms/retired**: —

### `Daily Life`
- **Definition**: ordinary daily life as the explicit subject
- **Use**: reflective essays on domestic objects, routines, social phenomena
- **Don't use**: any article that merely depicts daily life incidentally
- **Synonyms/retired**: `Life` (banned — too broad)

### `Data`
- **Definition**: data infrastructure, data systems, data thinking
- **Use**: articles on what a data system is or how data flows
- **Don't use**: articles that simply include numbers
- **Synonyms/retired**: —

### `Data Analysis`
- **Definition**: analytical methods applied to a specific dataset
- **Use**: articles whose core is a quantitative analysis (English stress, design value)
- **Don't use**: articles that merely cite a statistic
- **Synonyms/retired**: —

### `Data Visualization`
- **Definition**: designing visual representations of data
- **Use**: articles focused on chart construction or visual encoding (e.g. child growth charts)
- **Don't use**: any article that happens to contain a chart
- **Synonyms/retired**: —

### `Deemo`
- **Definition**: Deemo rhythm game
- **Use**: articles substantively about Deemo
- **Don't use**: rhythm games in general
- **Synonyms/retired**: shared with Chinese glossary

### `Desert`
- **Definition**: desert landscapes and desert travel
- **Use**: travelogues where the desert environment is central (Ningxia, Dunhuang fringes)
- **Don't use**: articles that cross a desert incidentally
- **Synonyms/retired**: —

### `Design`
- **Definition**: design as a profession and craft (UI, UX, visual, product)
- **Use**: substantive design pieces — process, principles, career
- **Don't use**: over-broad tag for anything visual; prefer a more specific design tag when possible
- **Synonyms/retired**: `设计` lives in the Chinese glossary

### `Development`
- **Definition**: software development as a craft
- **Use**: essays on what it means to build software (e.g. "Bricklaying and Trailblazing")
- **Don't use**: specific programming tutorials — use `Tutorial` + language tag
- **Synonyms/retired**:—

### `DIY`
- **Definition**: do-it-yourself physical or home projects
- **Use**: articles documenting a built object (rainproof shutters, interior fixes)
- **Don't use**: pure software tinkering
- **Synonyms/retired**: —

### `DOTA`
- **Definition**: DOTA game content
- **Use**: articles substantively about DOTA
- **Don't use**: general gaming
- **Synonyms/retired**: shared with Chinese glossary

### `Doraemon`
- **Definition**: Doraemon fan fiction or analysis
- **Use**: stories set in the Doraemon universe
- **Don't use**: passing references to the character
- **Synonyms/retired**:—

### `Dream`
- **Definition**: dreams and dream-logic as subject matter
- **Use**: fiction or essays where a dream is the structural device
- **Don't use**: metaphorical "dreams" meaning aspirations
- **Synonyms/retired**: —

### `Dunhuang`
- **Definition**: Dunhuang as a destination
- **Use**: travelogues of Dunhuang trips
- **Don't use**: articles that merely cite Dunhuang historically
- **Synonyms/retired**: —

### `Economy`
- **Definition**: macroeconomics — national or regional economies as subject
- **Use**: essays analyzing a country or region through its economy (Nigeria)
- **Don't use**: personal finance content
- **Synonyms/retired**: distinct from `Business` (firm-level) and `Finance` (instrument-level)

### `Education`
- **Definition**: education as a subject — how people learn, what should be taught
- **Use**: substantive essays on learning, pedagogy, knowledge transfer
- **Don't use**: any article from which a reader could "learn something"
- **Synonyms/retired**:—

### `Efficiency`
- **Definition**: efficiency and optimization as an explicit topic
- **Use**: essays on the philosophy or pathology of efficiency (e.g. efficiency obsession)
- **Don't use**: articles that simply happen to be efficient
- **Synonyms/retired**:—

### `Elf`
- **Definition**: elves as a fantasy race
- **Use**: fiction or worldbuilding centered on elves (e.g. Wood Elves)
- **Don't use**: generic fantasy
- **Synonyms/retired**: —

### `Energy`
- **Definition**: energy sources, energy policy, energy transition
- **Use**: substantive pieces on energy (e.g. why clean energy matters)
- **Don't use**: metaphorical uses of "energy"
- **Synonyms/retired**:—

### `ENS`
- **Definition**: Ethereum Name Service identifiers
- **Use**: articles about ENS or on-chain identity
- **Don't use**: general Ethereum content
- **Synonyms/retired**:—

### `Environment`
- **Definition**: environmental protection and ecological thinking
- **Use**: articles where conservation or ecology is a theme
- **Don't use**: articles that merely depict nature
- **Synonyms/retired**: —

### `Entrepreneurship`
- **Definition**: starting or building a venture
- **Use**: essays on the founder / startup journey (e.g. designer in a startup)
- **Don't use**: general career content
- **Synonyms/retired**: —

### `Essay`
- **Definition**: reflective non-fiction essay as the writing form
- **Use**: personal essays, perspective pieces, "thoughts on..." articles
- **Don't use**: tutorials or news
- **Synonyms/retired**: —

### `Excel`
- **Definition**: Microsoft Excel as the article's primary tool
- **Use**: articles whose core technique happens in Excel (child growth charts, Photoshop-machine-gun pipeline)
- **Don't use**: any article that touches a spreadsheet
- **Synonyms/retired**:—

### `Exploration`
- **Definition**: exploration as a theme — space, geography, idea-space
- **Use**: speculative or narrative pieces built around an exploration arc
- **Don't use**: travelogues that are about a destination rather than the act of exploring
- **Synonyms/retired**: —

### `Family`
- **Definition**: family as subject matter
- **Use**: fiction or essays where family relationships are central
- **Don't use**: passing mentions of a family member
- **Synonyms/retired**:—

### `Fan Fiction`
- **Definition**: derivative fiction set in an existing universe
- **Use**: stories built on a known property (Doraemon, World of Warcraft)
- **Don't use**: original fiction
- **Synonyms/retired**: —

### `Fantasy`
- **Definition**: fantasy genre — magic, mythical beings, secondary worlds
- **Use**: fiction or worldbuilding in a fantasy setting
- **Don't use**: metaphorical "fantasy"
- **Synonyms/retired**: —

### `Finance`
- **Definition**: finance as a domain — money mechanics, annualized returns, etc.
- **Use**: articles explaining how a financial instrument works
- **Don't use**: general investment commentary that is really `Investment`
- **Synonyms/retired**: —

### `Food`
- **Definition**: food, ingredients, dishes
- **Use**: articles about eating, ingredients, or specific dishes (crucian carp, aojiru)
- **Don't use**: cooking technique pieces — prefer `Cooking`
- **Synonyms/retired**:—

### `Forest`
- **Definition**: forests as setting or ecological subject
- **Use**: fiction or nature writing where a forest is central (e.g. Wood Elves)
- **Don't use**: articles that mention trees in passing
- **Synonyms/retired**: —

### `Future of Humanity`
- **Definition**: long-term future of the human species
- **Use**: speculative or philosophical pieces about humanity's trajectory
- **Don't use**: near-term trend pieces
- **Synonyms/retired**: —

### `Gaming`
- **Definition**: games and gaming culture (beyond a specific game)
- **Use**: articles about games as a medium or culture
- **Don't use**: content about one specific game — use that game's proper-noun tag instead
- **Synonyms/retired**:—

### `Geography`
- **Definition**: geography as a lens — landforms, climate, regional logic
- **Use**: essays that explain a place through its geography (Sikkim, monsoon logic)
- **Don't use**: travelogues with no geographic analysis
- **Synonyms/retired**: —

### `Growth`
- **Definition**: growth as personal or professional development
- **Use**: essays on leveling up, gaining competence, maturing as a designer
- **Don't use**: life-stage fiction — prefer `Coming of Age`
- **Synonyms/retired**:—

### `Hangzhou`
- **Definition**: Hangzhou as a destination
- **Use**: travelogues or museum pieces centered on Hangzhou
- **Don't use**: articles that merely stop in Hangzhou
- **Synonyms/retired**: —

### `History`
- **Definition**: history as substantive subject matter
- **Use**: essays or explainers that genuinely narrate the past (Middle East, *Sapiens*, Sikkim)
- **Don't use**: articles that cite a historical anecdote in passing
- **Synonyms/retired**: —

### `Home Improvement`
- **Definition**: home renovation, repair, and improvement
- **Use**: articles documenting changes to a living space
- **Don't use**: pure interior-design ideation — prefer `Design`
- **Synonyms/retired**:—

### `Horror`
- **Definition**: horror genre
- **Use**: fiction intended to frighten or unsettle
- **Don't use**: any dark-tinged essay
- **Synonyms/retired**: —

### `Human Nature`
- **Definition**: human nature as an explicit subject
- **Use**: essays or fiction interrogating what humans are fundamentally like
- **Don't use**: articles that depict human behavior without examining it
- **Synonyms/retired**:—

### `Humor`
- **Definition**: humor as the primary mode
- **Use**: jokes, parodies, comic anecdotes (the garage-gate tug-of-war)
- **Don't use**: any article with a funny line
- **Synonyms/retired**: —

### `Inner Mongolia`
- **Definition**: Inner Mongolia as a destination
- **Use**: travelogues centered on Inner Mongolia
- **Don't use**: generic grassland pieces that are not specifically about Inner Mongolia
- **Synonyms/retired**: —

### `Investment`
- **Definition**: investing as practice and theory
- **Use**: articles on return math, giving back, portfolio logic
- **Don't use**: pure finance explainers — prefer `Finance`
- **Synonyms/retired**:—

### `IPFS`
- **Definition**: InterPlanetary File System
- **Use**: articles using or explaining IPFS for hosting/pinning
- **Don't use**: general decentralized-web content
- **Synonyms/retired**:—

### `Japan`
- **Definition**: Japan as a geographical, cultural, and historical subject
- **Use**: articles substantively discussing Japanese society, culture, history, or travel
- **Don't use**: articles that merely mention Japanese products or names in passing
- **Synonyms/retired**: —

### `Language`
- **Definition**: language and linguistics as subject matter
- **Use**: essays on words, phonetics, translation (English stress, "ten thousand")
- **Don't use**: articles that merely happen to discuss language learning
- **Synonyms/retired**:—

### `Law`
- **Definition**: law, rights, and legal reasoning
- **Use**: articles substantively engaging a legal question (rights of robots)
- **Don't use**: passing legal anecdotes
- **Synonyms/retired**:—

### `Magic`
- **Definition**: magic as a fantasy device
- **Use**: fiction or worldbuilding where magic is a load-bearing element
- **Don't use**: metaphorical "magic"
- **Synonyms/retired**:—

### `Mathematics`
- **Definition**: math as the article's core
- **Use**: substantive math pieces (topology via a children's game)
- **Don't use**: articles that use arithmetic incidentally
- **Synonyms/retired**:—

### `Method`
- **Definition**: methodology as an explicit subject
- **Use**: articles proposing or critiquing a method (efficiency obsession, travel planning)
- **Don't use**: any article that has a method
- **Synonyms/retired**:—

### `Middle East`
- **Definition**: the Middle East as a regional subject
- **Use**: historical or political essays centered on the region
- **Don't use**: articles that touch the region in passing
- **Synonyms/retired**:—

### `Midjourney`
- **Definition**: Midjourney AI image-generation tool
- **Use**: articles substantively about Midjourney
- **Don't use**: general AI art not tied to Midjourney
- **Synonyms/retired**: shared with Chinese glossary

### `Mobile`
- **Definition**: mobile platform and mobile design dimensions
- **Use**: articles on mobile UI sizing, mobile conventions
- **Don't use**: general UI work not specific to mobile
- **Synonyms/retired**:—

### `Museum`
- **Definition**: museums as destinations
- **Use**: articles centered on a specific museum visit (Zhejiang museums)
- **Don't use**: articles that pass through a museum
- **Synonyms/retired**:—

### `Nature`
- **Definition**: the natural world as subject — ecology, landscape, phenomena
- **Use**: substantive nature writing (solstice physics, grassland, water-cycle)
- **Don't use**: articles that merely depict scenery
- **Synonyms/retired**:—

### `Ningxia`
- **Definition**: Ningxia as a destination
- **Use**: travelogues centered on Ningxia
- **Don't use**: generic northwest-China content
- **Synonyms/retired**:—

### `Parenting`
- **Definition**: parenting and raising children
- **Use**: essays on parenthood, kids' learning, family travel with children
- **Don't use**: any article featuring a child
- **Synonyms/retired**:—

### `Philosophy`
- **Definition**: philosophy as subject — meaning, ethics, mind, time
- **Use**: substantive philosophical essays (kitchenware, digital dark age, last work)
- **Don't use**: articles that gesture at a big idea without arguing it
- **Synonyms/retired**:—

### `Phone`
- **Definition**: phones as devices — hardware, optics, telephoto
- **Use**: articles substantively about the phone as a physical object
- **Don't use**: mobile-app UI — use `Mobile` or `UI`
- **Synonyms/retired**:—

### `Photography`
- **Definition**: photography as craft and phenomenon
- **Use**: articles on optical zoom, telephoto limits, photographic technique
- **Don't use**: articles that merely include photos
- **Synonyms/retired**:—

### `Physics`
- **Definition**: physics as the article's core science
- **Use**: explainers of physical phenomena (solstice, summer sun, water/ice)
- **Don't use**: science articles that are really biology or chemistry
- **Synonyms/retired**:—

### `Product`
- **Definition**: product thinking and product design
- **Use**: substantive product essays (AI agents, PPT automation, canvas sizing)
- **Don't use**: articles that mention a product in passing
- **Synonyms/retired**:—

### `Programming`
- **Definition**: writing code as a craft
- **Use**: articles substantively about the act or philosophy of programming
- **Don't use**: tutorials where the code is the means, not the subject
- **Synonyms/retired**:—

### `Prompt Engineering`
- **Definition**: crafting prompts for AI systems
- **Use**: articles whose core technique is prompt design
- **Don't use**: articles that merely include an example prompt
- **Synonyms/retired**:—

### `Psychology`
- **Definition**: psychology as subject matter
- **Use**: articles substantively applying psychology (icon psychology)
- **Don't use**: articles that gesture at "perception" without analysis
- **Synonyms/retired**:—

### `Religion`
- **Definition**: religion as subject matter
- **Use**: fiction or essays substantively engaging religion
- **Don't use**: passing religious imagery
- **Synonyms/retired**:—

### `Review`
- **Definition**: evaluative review of a product or capability
- **Use**: structured assessment (AI PPT, AI search)
- **Don't use**: casual opinions
- **Synonyms/retired**:—

### `Road Trip`
- **Definition**: self-driving / road-trip travel style
- **Use**: travelogues where the road-trip format is the point
- **Don't use**: any trip that involved a car
- **Synonyms/retired**:—

### `Robot`
- **Definition**: robots as subjects — fiction, ethics, embodiment
- **Use**: fiction or essays where robots are central (rights of robots)
- **Don't use**: industrial-automation content
- **Synonyms/retired**:—

### `Rural`
- **Definition**: rural life and countryside as setting or subject
- **Use**: fiction or essays set in and about the rural
- **Don't use**: articles that depict a village in passing
- **Synonyms/retired**:—

### `Savanna`
- **Definition**: the African savanna as ecological setting
- **Use**: nature or fiction pieces specifically about the savanna
- **Don't use**: generic grassland — use `Nature` or a more specific place tag
- **Synonyms/retired**:—

### `Sci-Fi`
- **Definition**: science fiction genre
- **Use**: fiction or speculation built on a science-fiction premise
- **Don't use**: any speculative essay
- **Synonyms/retired**:—

### `Science`
- **Definition**: natural sciences as popular-explanation subject
- **Use**: substantive science explainers (metacognition, long-tail knowledge, summer solstice)
- **Don't use**: articles that merely cite a scientific fact
- **Synonyms/retired**:—

### `Search`
- **Definition**: search as a domain — search engines, search behavior, AI search
- **Use**: articles substantively about how search works or fails
- **Don't use**: articles that mention "searching" for something
- **Synonyms/retired**: TBD — appears once, context narrow; revisit when a second article arrives

### `Short Story`
- **Definition**: fictional short story as the writing form
- **Use**: narrative fiction (42 Seconds, Nobita, Regular Day)
- **Don't use**: essays or personal anecdotes
- **Synonyms/retired**:—

### `Society`
- **Definition**: society as subject — collective phenomena, institutions, power
- **Use**: essays analyzing a social pattern (besieged customers, real-estate bubble, Nigeria)
- **Don't use**: personal anecdotes
- **Synonyms/retired**:—

### `Space`
- **Definition**: outer space as setting or subject
- **Use**: fiction or speculation centered on space (Space Hotel)
- **Don't use**: articles that mention astronomy in passing
- **Synonyms/retired**:—

### `Statistics`
- **Definition**: statistics as a method
- **Use**: articles whose technique is statistical (child growth charts)
- **Don't use**: articles that merely include a number
- **Synonyms/retired**:—

### `Suzhou`
- **Definition**: Suzhou as a destination
- **Use**: travelogues or garden pieces centered on Suzhou
- **Don't use**: articles that pass through Suzhou
- **Synonyms/retired**:—

### `Survival`
- **Definition**: survival as theme — staying alive in harsh conditions
- **Use**: fiction or essays where survival is central (divine era, grassland)
- **Don't use**: metaphorical "survival"
- **Synonyms/retired**:—

### `Technology`
- **Definition**: technology as subject — how tech works, where it's going
- **Use**: substantive tech essays (AI agents, AI metacognition, long-tail knowledge)
- **Don't use**: any article that uses a tool
- **Synonyms/retired**:—

### `Tool`
- **Definition**: a specific tool as the article's subject
- **Use**: articles substantively about a tool (canvas calculator, data system, last working device)
- **Don't use**: articles that merely use a tool
- **Synonyms/retired**:—

### `Travel`
- **Definition**: travel as topic — trip planning, destinations, travel style
- **Use**: travelogues and travel-method articles
- **Don't use**: articles that incidentally take place elsewhere
- **Synonyms/retired**:—

### `Tutorial`
- **Definition**: step-by-step how-to
- **Use**: instructional articles (circular progress bar, interior design, blockchain blogging)
- **Don't use**: reflective essays
- **Synonyms/retired**:—

### `UI`
- **Definition**: user-interface design specifics
- **Use**: articles on UI elements, sizing, icon design
- **Don't use**: general design — prefer `Design`
- **Synonyms/retired**:—

### `UX`
- **Definition**: user-experience design and reasoning
- **Use**: articles on UX logic (newbie perspective, texting experience, roommate's ride)
- **Don't use**: any design article — prefer `Design`
- **Synonyms/retired**:—

### `Vision`
- **Definition**: vision as a biological or technological capability
- **Use**: articles on visual perception or computer vision (distinguishing experiment)
- **Don't use**: metaphorical "vision"
- **Synonyms/retired**: TBD — appears once, context narrow; revisit when a second article arrives

### `World of Warcraft`
- **Definition**: World of Warcraft game and lore
- **Use**: articles substantively about WoW
- **Don't use**: general gaming
- **Synonyms/retired**:—

### `Writing`
- **Definition**: writing as a craft and practice
- **Use**: articles on how one writes (AI-assisted writing)
- **Don't use**: any article that is well-written
- **Synonyms/retired**:—

### `Xi'an`
- **Definition**: Xi'an as a destination
- **Use**: travelogues centered on Xi'an
- **Don't use**: articles that pass through Xi'an
- **Synonyms/retired**:—

### `Xinjiang`
- **Definition**: Xinjiang as a destination
- **Use**: travelogues centered on Xinjiang
- **Don't use**: generic northwest-China content
- **Synonyms/retired**:—

### `Xishuangbanna`
- **Definition**: Xishuangbanna as a destination
- **Use**: travelogues centered on Xishuangbanna
- **Don't use**: generic Yunnan content
- **Synonyms/retired**:—

### `Yunnan`
- **Definition**: Yunnan as a destination
- **Use**: travelogues centered on Yunnan
- **Don't use**: articles that merely pass through Yunnan
- **Synonyms/retired**:—
