# -*- coding: utf-8 -*-
"""Project data for the gallery and the detail pages.

Order here IS the order on the site: newest first. Move a dict to move the tile.

Dates come from the GitHub repo timestamps where a repo exists. The GADIG titles
carry no date because itch.io does not publish one in its markup - their relative
order is taken from the gadig.itch.io listing, which is newest-first. Inferred
semesters are noted in a comment on each so they can be filled in once confirmed.

The `rant` fields are drafts in Khalid's voice, meant to be rewritten by him.
"""

PROJECTS = [

 # ---------------- 2026 ----------------

 dict(slug='knowledge-assistant', title='Knowledge assistant', year='2026 &rarr; NOW', kind='AI &middot; SAP NS2',
   stack='REACT · FLASK · AWS GOVCLOUD · HYBRID RETRIEVAL',
   kao='⋆.˚🔍 ⊹',
   blurb='Sole engineer. 30+ delivery managers, 1,000+ queries a week, source-tracked citations. Cut lookup time from 15 minutes to under 30 seconds.',
   rant='This is the thing I am proudest of. I was the only engineer on it, and it is live inside real customer delivery workflows rather than sitting in a demo somewhere.\n\nThe problem was that finding one fact across a thousand-plus enterprise documents took about fifteen minutes. Pure vector search was not good enough on its own, so it runs hybrid keyword routing with structured retrieval grouping, and every answer carries source-tracked citations so people can check it. Lookup is now under thirty seconds.\n\nReact on the front, Flask behind it, deployed on AWS GovCloud. It serves 30+ customer delivery managers and over a thousand queries a week.',
   links=[]),

 dict(slug='flock-off', title='flock-off', year='SEP 2026', kind='TOOL',
   stack='PYTHON · OPENSTREETMAP · ROUTING',
   kao='[ ◉¯] ✧˖°',
   blurb='Navigation that routes around ALPR and speed cameras, then hands the trip to Google Maps. Names who runs each camera.',
   rant='Automatic licence plate readers are everywhere now and almost nobody knows where they are or who operates them. This maps the surveillance grid from public OpenStreetMap data, routes you around it, and then hands the finished trip off to Google Maps so you can actually drive it.\n\nIt also names who runs each camera, because "there is a camera here" is much less useful than "there is a camera here and this is the company collecting it".',
   links=[('GITHUB','https://github.com/grmpyktn11/flock-off')]),

 dict(slug='nibbler', title='Nibbler', year='2026', kind='AI',
   stack='PYTHON · LLM APIS · MCP · POSTGRESQL · VECTOR SEARCH',
   kao='‧₊˚ ⋅ 🍽️ ‧₊˚ ⋅',
   blurb='Pulls restaurant mentions out of Instagram, Discord, WhatsApp and SMS, then matches them against a preference profile built from your order history.',
   rant='Everyone I know has the same problem: a friend sends you a restaurant, you say "oh that looks good", and then it disappears into a group chat forever. Nibbler goes and finds those mentions across Instagram, Discord, WhatsApp and SMS, parses them with an LLM, and keeps them somewhere you will actually look.\n\nThe interesting half is the matching. It builds a preference profile out of your order history and spending patterns in Postgres with vector search, then uses MCP connectors and a calendar API to pull in real restaurant data and factor in when you are actually free. You get menu suggestions and a cost estimate per visit rather than a list of names.\n\nThere is also a sponsored-placement layer where restaurants can bid on recommendation visibility, which is the part that could pay for itself.',
   links=[('GITHUB','https://github.com/grmpyktn11')]),

 dict(slug='firstpick', title='FirstPick', year='AUG 2026', kind='TOOL',
   stack='MYSQL · SCRAPING · CLEVERCLOUD',
   kao='.✦ ݁˖🎮๋࣭₊ ⊹',
   blurb='Register the champions you play and it recommends picks for counter-matchups, using data scraped from op.gg.',
   rant='You register an account, tell it which champions you actually play, and it tells you what to pick into a given matchup based on scraped op.gg data rather than vibes.\n\nUser info lives in MySQL on CleverCloud hosting, so it follows you between machines instead of being stuck in one browser.',
   links=[('GITHUB','https://github.com/grmpyktn11/LastPick')]),

 # GADIG - inferred Spring 2026, newest title on the itch page
 dict(slug='king-fisher', title='King Fisher', year='GADIG', kind='GAME',
   stack='GADIG · WINDOWS · LINUX',
   kao='⋆.˚🎣 ₊˚⊹',
   blurb='A 2&ndash;4 player party game about catching the most fish, where you reel in your catch by playing along to the rhythm.',
   rant='Master anglers from every corner of existence gather for the Intergalactic Fish Bowl, all hoping to claim the title of Fish Whisperer. You reel your catch in by playing along to the rhythm, and you can trip your friends up while they are trying to do the same.\n\nA GADIG club title. <em>Add what you worked on here.</em>',
   links=[('ITCH.IO','https://gadig.itch.io/king-fisher')]),

 dict(slug='wkw-ify', title='wkw-ify', year='FEB 2026', kind='TOOL',
   stack='PYTHON · OPENCV · COLOUR SCIENCE',
   kao='. ₊ ⊹ . 🎞️.ᐟ',
   blurb='Colour-grades photographs like two favourite Wong Kar-wai films, using classical technique rather than a model.',
   rant='Final project for computational photography, and the one I had the most fun presenting. It grades your photos to look like two of my favourite Wong Kar-wai films.\n\nThe constraint I set myself was no model — everything is classical technique from the course, actual colour science rather than handing it to a network and hoping. Getting the greens and the reds to sit the way they do in those films took far longer than the code did.',
   links=[('GITHUB','https://github.com/grmpyktn11/wongkarwaify')]),

 dict(slug='cheet-sheet', title='Cheet Sheet', year='FEB 2026', kind='TOOL',
   stack='REACT · AWS AMPLIFY · FLASK · GPT',
   kao='✎ᝰ. ⋆.˚',
   blurb='Feed it a lecture presentation and it returns a summary PDF with notes.',
   rant='Drop in a lecture presentation, get back a summary PDF with notes you can actually revise from.\n\nReact front end hosted on AWS Amplify, with a Flask server doing the summarising. It was the first time I had to think about where each half of an app lives and how they talk to each other, rather than everything running on my laptop.',
   links=[('GITHUB','https://github.com/grmpyktn11/cheetsheetprogram')]),

 # ---------------- 2025 ----------------

 # GADIG - inferred Fall 2025
 dict(slug='deadshot', title='DEADSHOT', year='GADIG', kind='GAME',
   stack='GADIG · HTML5 · WINDOWS · LINUX',
   kao='⋆.˚🐴 ₊˚⊹',
   blurb='A 2.5D shooter about an exiled gunslinger who comes home to a cursed town overrun by monsters.',
   rant='An exiled gunslinger returns to town determined to clear their name and save their beloved horse. While they were away the place picked up a curse and a monster problem. You fight strange creatures, talk to the people still living there, and work out what happened in your absence.\n\nA GADIG club title. <em>Add what you worked on here.</em>',
   links=[('ITCH.IO','https://gadig.itch.io/deadshot')]),

 dict(slug='pptxt', title='pptxt', year='DEC 2025', kind='TOOL',
   stack='PYTHON',
   kao='⋆.˚🗒️ ₊˚',
   blurb='Converts PowerPoints into stripped plain text, so they are cheaper and cleaner to feed to a model than pasting slides one by one.',
   rant='Built during finals season out of pure irritation. I was copy-pasting slide after slide into a model, wasting tokens on layout junk nobody needed, and losing my place every time.\n\nSo: point it at a set of PowerPoints and it strips them down to plain text. Boring, small, and I still use it.',
   links=[('GITHUB','https://github.com/grmpyktn11/pptxtxt')]),

 dict(slug='steam-search', title='Steam Search', year='DEC 2025', kind='TOOL',
   stack='MYSQL · PYTHON · SCRAPING',
   kao='⋆.˚📈 ₊˚⊹',
   blurb='All-time lows, current versus base price, and the analytics needed to tell whether a Steam sale is actually a sale.',
   rant='Final project for our database class. The Steam store will happily tell you something is on sale without telling you it was cheaper three months ago.\n\nThis adds all-time lows, current versus base price, and enough analytics to tell whether a discount is real. Mostly it is a database project wearing a shopping tool as a disguise.',
   links=[('GITHUB','https://github.com/grmpyktn11/Cs450Project')]),

 dict(slug='catfe-au-lait', title='Catfe au Lait', year='JUN 2025', kind='GAME',
   stack='UNITY · C#',
   kao='⋆.˚☕︎',
   blurb='Diner Dash in a cat cafe. Final project for game development.',
   rant='Diner Dash, but you are a barista in a cat cafe. Final project for CS325, built in Unity with C#.\n\nOrder queues, timers, and a lot of tuning to find the line where it is stressful enough to be fun but not so stressful that you quit.',
   links=[('ITCH.IO','https://grumpykitten1.itch.io/catfe-au-lait')]),

 dict(slug='kpop-bot', title='Keeping Up With Kpop', year='2025', kind='BOT',
   stack='PYTHON · TWITTER API · GPT',
   kao='₊˚.🎧 ✩｡',
   blurb='Scrapes headlines from Soompi, writes the post, and publishes it.',
   rant='A bot that scrapes headlines off Soompi, has GPT write the post, and publishes it through the Twitter API. It ran on its own for a good while.\n\nThe first time I chained scraping, generation and posting into one unattended pipeline, which turned out to be the shape of a lot of things I built afterwards.',
   links=[('TWITTER','https://twitter.com/KeepingUpKpop1'),
          ('GITHUB','https://github.com/grmpyktn11/Keeping-Up-With-Kpop/tree/main')]),

 dict(slug='resource-monitor', title='Resource Monitor', year='MAY 2025', kind='TOOL',
   stack='ELECTRON · NODE',
   kao='๋࣭ ⭑💻 ⊹',
   blurb='A small desktop widget for CPU and RAM. Deliberately cute.',
   rant='A little Electron widget that sits on your desktop and tells you your CPU and RAM usage. That is the whole thing.\n\nI wanted something I could glance at without opening Task Manager, and I wanted it to be cute rather than a wall of graphs.',
   links=[('GITHUB','https://github.com/grmpyktn11/cool-performance-monitor')]),

 # GADIG - inferred Spring 2025
 dict(slug='bake-me-crazy', title='Bake Me Crazy', year='GADIG', kind='GAME',
   stack='GADIG · HTML5 · WINDOWS',
   kao='˚₊ʚ🧁ɞ₊˚',
   blurb='You are a baker at a new farmer&rsquo;s market, and flirting is not your strong suit &mdash; so you bake at people instead.',
   rant='You run a bakery in a small town that has just opened a farmer&rsquo;s market. On opening day you spot a few merchants you would like to talk to, discover that flirting is not among your skills, and fall back on what you are good at: handing people baked goods until they like you.\n\nA GADIG club title. <em>Add what you worked on here.</em>',
   links=[('ITCH.IO','https://gadig.itch.io/bake-me-crazy')]),

 dict(slug='chalets-explore', title='Chalet&rsquo;s Explore', year='FEB 2025', kind='HACK',
   stack='WICSHACKS 2025 · WEB · SOCIAL',
   kao='ᯓ ✈︎',
   blurb='A platform for posting and finding third places around Charlottesville.',
   rant='Submission for WICSHacks 2025. A social platform for posting and getting recommendations for third places — the cafes, parks and rooms that are neither home nor work — around Charlottesville.',
   links=[('GITHUB','https://github.com/grmpyktn11/WICS-hacks')]),

 # ---------------- 2024 ----------------

 dict(slug='fetch-quest', title='Fetch Quest', year='FALL 2024', kind='GAME',
   stack='GADIG · GODOT · GDSCRIPT',
   kao='૮ ˶• ﻌ •˶ ა',
   blurb='Imagine if Link were a dog. The semester we moved the club from Unity to Godot.',
   rant='A dog sets out to return a stick to its owner, finds a legendary sword along the way, and ends up saving a kingdom from a growing gloom. Puzzles, dungeons, the most grandiose fetch quest of our time.\n\nThis was the GADIG game for Fall 2024, and the semester we moved the whole club from Unity over to Godot. I took a more administrative role on this one, which mostly meant making sure eighty people with different schedules shipped the same game.',
   links=[('ITCH.IO','https://gadig.itch.io/fetch-quest')]),

 dict(slug='focusup', title='FocusUp!', year='NOV 2024', kind='TOOL',
   stack='VS EXTENSION',
   kao='⋆˙⟡ ꒰ 🔔 ꒱ ⟡˙⋆',
   blurb='Pings my phone whenever I wander off while Visual Studio is open.',
   rant='It notices when Visual Studio is open and I have wandered off, then pings my phone about it. Built entirely to police my own attention span.\n\nIt worked, which was mildly insulting.',
   links=[('GITHUB','https://github.com/grmpyktn11/FocusUp')]),

 dict(slug='worse-wiki', title='Worse Wiki', year='OCT 2024', kind='HACK',
   stack='PATRIOTHACKS 2024 · API DESIGN · WEB',
   kao='📖⋆. 𐙚 ˚',
   blurb='An evil Wikipedia that gets less accurate the longer you read. First time I wrote an API and consumed it in the same weekend.',
   rant='Submission for PatriotHacks 2024: an evil Wikipedia that gets progressively less accurate the further down the page you read.\n\nThis one was fun because I finally got to build with friends instead of alone, and because it was the first time I wrote an API and then had to consume my own API in the same weekend. Very clarifying about what makes an API annoying.',
   links=[('GITHUB','https://github.com/grmpyktn11/WorseWiki')]),

 dict(slug='card-counter', title='Card Counter', year='JUN 2024', kind='TOOL',
   stack='OPENCV · PYTESSERACT',
   kao='⋆⁺₊⋆🂲🃍🂶⋆⁺₊⋆',
   blurb='Photograph a card, OCR it, and see how many are left in the deck. Built for a professor&rsquo;s research.',
   rant='Built for a professor&rsquo;s research. Take a picture of a card, OpenCV finds and cleans it up, PyTesseract reads it, and the app tells you how many of that card are left in the deck.\n\nMy first real lesson in how much of computer vision is preprocessing rather than the clever bit at the end.',
   links=[('GITHUB','https://github.com/grmpyktn11/Pokemon-Card-Counter')]),

 # GADIG - inferred Spring 2024
 dict(slug='fruit-punch', title='Fruit Punch', year='GADIG', kind='GAME',
   stack='GADIG · HTML5 · WINDOWS · MACOS · LINUX',
   kao='⋆.˚🍉 ₊˚⊹',
   blurb='A beat-em-up in an overgrown urban wasteland. Four playable fruit, three stages, one question: who packs the biggest punch?',
   rant='An urban wasteland has been overrun with jungle, and the only reasonable response is a beat-em-up. Three stages, and four playable characters — Apple, Banana, Watermelon and Grapes-Sensei — each with their own action.\n\nA GADIG club title. <em>Add what you worked on here.</em>',
   links=[('ITCH.IO','https://gadig.itch.io/fruit-punch')]),

 dict(slug='dish-detective', title='Dish Detective', year='MAR 2024', kind='HACK',
   stack='VCU MEGAHACK 2024 · GOOGLE CLOUD VISION · GPT',
   kao='𓌉◯𓇋',
   blurb='Photograph the groceries you already have and it generates a recipe you can share. My first hackathon.',
   rant='My first hackathon, at VCU&rsquo;s Megahack in March 2024. You photograph whatever groceries you already have, Google Cloud Vision works out what they are, and GPT generates a recipe you can share.\n\nEverything I have built since started here.',
   links=[('DEVPOST','https://devpost.com/software/dish-detective-jhu81e')]),

 # ---------------- 2023 ----------------

 # GADIG - inferred Fall 2023, the oldest of the titles listed and most likely
 # the first game Khalid worked on after joining the club that September
 dict(slug='princess-starshine', title='Princess Starshine', year='GADIG', kind='GAME',
   stack='GADIG · UNITY · C#',
   kao='˗ˏˋ ★ ˎˊ˗',
   blurb='A bullet heaven built across a semester with separate art and sound teams. I wrote UI, enemy movement and player behaviour.',
   rant='Princess Starshine of the Sparkle Kingdom accidentally takes an elevator to hell, and fights her way out with rainbows, butterflies and unicorns. A bullet heaven, built over a full semester alongside separate art and sound teams. I wrote the UI, the enemy movement and the player behaviour.\n\nThe real lesson was not the code. It was learning to hand a build to an artist, get something back that does not match what you assumed, and keep the thing shipping anyway.',
   links=[('ITCH.IO','https://gadig.itch.io/princess-starshine-vs-the-demons'),
          ('GITHUB','https://github.com/gmuGADIG/Princess-Starshine')]),
]
