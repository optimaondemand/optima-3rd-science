#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/33-02/lesson.json, how-lines.json, scripts.json, credits.json (33.02: no voices recorded; scripts only).
Images come from prep.py (run it first). Season finale: premiere.finale turns on the scientist certificate."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "What have you learned to do as a scientist this year, and how can you prove it?"

film = {
  "id": "g3sci-33-02", "mount": "wf-film", "kicker": "Opti's Wonder Films · Season Finale", "lesson": "Lesson 33.02 · Your Final Science Investigation",
  "title": "From the Ashes",
  "bigQuestion": BQ,
  "poster": "f_air", "endPoster": "f_end", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.5},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    ph(3.4, 6.0, "f_air", "Rocky mountain peaks and green valleys seen from high in the air, with small white clouds", "Rocky Mountain National Park, from the air",
       frm=(1.25, .5, .5), to=(1.0, .5, .5), fade=1.0, sfxAt=[{"at": 0.4, "name": "whoosh"}]),
    ph(9.4, 5.4, "f_fire", "Tall orange flames and smoke rising from a burning pine forest", "The 1988 fires · Yellowstone National Park",
       frm=(1.0, .5, .5), to=(1.12, .5, .4), fx=["dust"], sfxAt=[{"at": 0.3, "name": "rumble"}]),
    ph(14.8, 4.6, "f_burn", "Black, burned tree trunks standing and lying across gray ash", "After the fire · Yellowstone, 1988",
       frm=(1.12, .5, .5), to=(1.0, .5, .5), fade=0.6),
    {"t": 19.4, "d": 2.6, "type": "flash", "lines": ["A forest?", "From ashes?"], "beats": [0.15, 1.2], "fade": 0.15},
    {"t": 22.0, "d": 7.0, "type": "reveal", "img": "f_regrow", "alt": "Hundreds of small green pine trees growing between tall, bare, burned trunks",
     "from": [1.0, .5, .5], "to": [1.08, .5, .55], "revealAt": 0.5, "revealDur": 4.4, "place": "The same burned forest, 10 years later · Yellowstone, 1998",
     "fade": 0.6, "cover": ["#2a2420", "#4a3d34"], "chip": "70,62,56"},
    ph(29.0, 5.6, "f_count", "A park scientist in a green cap bending over a square frame in tall grass, writing on a tablet", "A park scientist counts plants in a square · Yellowstone, 2020",
       frm=(1.0, .5, .5), to=(1.08, .5, .58)),
    ph(34.6, 5.0, "f_hatch", "A baby sea turtle crawling across the sand", "A loggerhead hatchling heads for the sea",
       frm=(1.08, .4, .5), to=(1.0, .5, .5), fx=["sweep"]),
    ph(39.6, 5.0, "f_pika", "A small, round, gray-brown pika sitting on a pink rock", "A pika · Rocky Mountain National Park",
       frm=(1.0, .5, .5), to=(1.1, .45, .55)),
    ph(44.6, 6.4, "f_end", "Yellow wildflowers on a high, rocky meadow with mountains and patches of snow behind", "A mountain meadow · Rocky Mountain National Park",
       frm=(1.0, .5, .5), to=(1.08, .5, .55), fade=0.9, fx=["rays"]),
    {"t": 51.0, "d": 5.4, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.4, "text": "High in the mountains, every park holds a mystery.", "voice": "opti-1"},
    {"t": 9.8, "d": 4.8, "text": "In 1988, giant fires burn across Yellowstone.", "voice": "opti-2"},
    {"t": 15.2, "d": 4.0, "text": "When the smoke clears, black trunks stand everywhere.", "voice": "opti-3"},
    {"t": 22.4, "d": 6.2, "text": "But look closer. Tiny pine trees are growing back.", "voice": "opti-4"},
    {"t": 29.4, "d": 5.0, "text": "Scientists count them, one small square at a time.", "voice": "opti-5"},
    {"t": 35.0, "d": 4.4, "text": "On beaches, scientists watch which way the hatchlings go.", "voice": "opti-6"},
    {"t": 40.0, "d": 4.4, "text": "Ask. Predict. Collect evidence. You've done it all year.", "voice": "opti-7"},
    {"t": 45.0, "d": 5.8, "text": BQ, "voice": "opti-8"}
  ]
}

specimen = {
  "img": "spec", "aspect": "1920/1677", "radius": 0.07,
  "hotspots": [
    {"name": "Pairs of long, narrow footprints", "x": 0.615, "y": 0.18},
    {"name": "A long line between the prints", "x": 0.83, "y": 0.6},
    {"name": "A date, written sideways", "x": 0.915, "y": 0.77},
    {"name": "Lines of handwriting, like a poem", "x": 0.3, "y": 0.36},
    {"name": "A name written under the tracks", "x": 0.68, "y": 0.92}
  ],
  "kicker": "🔎 Mystery specimen", "title": "Old pages, full of clues?",
  "alt": "Two yellowed, lined pages from a small old book: handwriting on the left, pencil drawings of pairs of footprints on the right",
  "look": "A real specimen from a museum. It is a small, old book open to two pages: handwriting on the left, drawings on the right. A specimen is one real thing that scientists study. Who made these pages, and what were they studying? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the page, then tap 3 things you notice.",
  "number": "No. 33.02-A",
  "card": ["<b>Specimen A</b>", "Found: in a museum archive", "Made of: paper, ink, and pencil", "Who made it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🔍", "evidence", "Information from observations or data that helps answer a science question."],
  ["🧪", "investigation", "A planned way to answer a science question by observing, testing, or collecting data."],
  ["📐", "model", "A drawing, diagram, or object that shows how something works in nature."],
  ["🔁", "pattern", "Something that repeats or happens in a regular, predictable way."],
  ["⚡", "cause and effect", "When one thing (the cause) makes another thing (the effect) happen."],
  ["💡", "conclusion", "An answer or idea you reach after looking at your evidence and thinking carefully."]
]

parts = [
  {"kicker": "🧠 Part 1", "title": "You Already Think Like a Scientist",
   "html": "<p>Remember the old pages? They come from the field book of Vernon Bailey, a scientist who studied animals. In 1890 in Nevada, he drew the tracks of a kind of kangaroo rat. It hops on two big back feet, so its prints come in pairs. He wrote the date, too. That's what scientists do: observe, record, and use evidence.</p><p><b>Scenario A · A Mountain Park.</b> In 1988, fires burned about a third of Yellowstone National Park. What grows back?</p>"},
  {"kicker": "🏖 Part 2", "title": "Scenario B · A New Parking Lot",
   "html": "<p>Sea turtles nest on Florida beaches every summer. At night, the hatchlings dig out and crawl toward the brightest light. On a natural beach, that's the moon and stars over the ocean. Now a new parking lot with bright lights is being built near the beach. What will the hatchlings do?</p>"},
  {"kicker": "🏔 Part 3", "title": "Scenario C · Shorter, Warmer Winters",
   "html": "<p>On a mountain, it gets colder the higher you go. Each plant and animal lives where the temperature fits it. In parks like Rocky Mountain National Park in Colorado, winters are getting shorter and warmer. Scientists check the same places year after year, looking for a pattern.</p>"},
  {"kicker": "🎞️ Part 4", "title": "Year in Review Files"}
]

order = {
  "mix": [2, 3, 0, 1], "hint": "Start with the fire.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does a forest come back after a fire?",
  "look": "Four real photos tell what happened after fire burned a pine forest in Yellowstone. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "Thick white smoke rising from a burning forest beside a river", "text": "A fire burns through the pine forest in the summer of 1988.", "play": "The fire burns.",
     "miss": ["", "The story starts with the fire. Try frame 1.", "The story starts with the fire. Try frame 1.", "The story starts with the fire. Try frame 1."]},
    {"img": "o2", "alt": "A gloved hand holding a pine cone whose scales have opened wide", "text": "The heat opens sealed pine cones, and seeds fall onto the ash.", "play": "Cones open.",
     "miss": ["The fire comes first. Try a later frame.", "", "The seeds must fall before they can sprout. Try an earlier frame.", "The seeds must fall before they can sprout. Try an earlier frame."]},
    {"img": "o3", "alt": "Two tiny pine seedlings growing out of black, burned ground next to a pine cone", "text": "The next spring, tiny pine seedlings sprout in the sunny, open ground.", "play": "Seedlings sprout.",
     "miss": ["The fire and the cones come first. Try a later frame.", "The cones have to open first. Try a later frame.", "", "Seedlings come before the forest. Try an earlier frame."]},
    {"img": "o4", "alt": "Green hills covered with thick young pine forest above a river", "text": "Years later, a young forest covers the hills again.", "play": "A young forest grows.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Mia says, \"After a big fire, a forest is gone for good.\" What do you think?",
    "options": [
      {"t": "Mia is right. Nothing grows back after a fire.", "miss": "Think about the movie. What fell out of the cones, and what grew?"},
      {"t": "The forest can grow back. The heat opens the cones, and new pines sprout from the seeds.", "ok": "Yes! Scientists counted the seedlings and watched the forest come back. Fire is part of this forest's life."}
    ]
  }
}

movie = {
  "model": "fire-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🌲",
  "real": "real", "realAlt": "A river winding through hills covered with thick, young pine forest",
  "stamp": "THE FOREST CAME BACK!", "endCap": "A real young forest.",
  "beats": [
    {"at": 0, "cap": "1 · The fire burns.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Summer 1988"], "sfx": "whoosh"},
    {"at": 2600, "cap": "2 · Cones open.", "model": {"show": "s2"}, "counter": ["Fall 1988"]},
    {"at": 5200, "cap": "3 · Seedlings sprout.", "model": {"show": "s3"}, "counter": ["Spring 1989"]},
    {"at": 7800, "cap": "4 · A young forest.", "model": {"show": "s4"}, "counter": ["2019"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Turtle Test", "title": "Which way will the hatchlings crawl?",
  "look": "Two real Florida beaches at night, each on a lit tray. Specimen A is a dark beach where the moon shines over the ocean. Specimen B is a beach below tall, brightly lit buildings. Under the trays are a model hatchling (a baby turtle that just hatched) and low, covered lights.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A dark beach at night with the moon shining on the ocean waves", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A beach at night below tall buildings with bright lights", "label": "Specimen B"}
  ],
  "materials": [{"key": "hatch", "label": "A hatchling", "img": "hatch"}, {"key": "low", "label": "Low, covered lights", "swatch": "lamp"}],
  "ask": [
    {"q": "Which beach is dark, with the moon shining over the ocean?", "ans": "A", "ok": "Yes. Specimen A is dark, and the brightest light is over the water.", "miss": "Look closely. Where is the moon shining on the waves?"},
    {"q": "Which beach has bright lights shining from the land?", "ans": "B", "ok": "Yes. Specimen B has bright buildings right beside the sand.", "miss": "Look again. Which one has tall, lit-up buildings?"}
  ],
  "press": "🌙 Let the hatchlings go",
  "testDo": "Put the hatchling under one beach and the low lights under the other: drag them, or tap one, then a beach. Press <b>Let the hatchlings go</b>. Then swap.",
  "disclaimer": "This is a model. A real nest holds about 100 eggs.",
  "results": {
    "Ahatch": {"text": "The hatchling crawls toward the moonlit ocean, the brightest way. It reaches the sea!", "fx": "glow"},
    "Alow": {"text": "This beach is already dark, so low lights change very little here.", "fx": "none"},
    "Bhatch": {"text": "The hatchling turns away from the sea and crawls toward the bright buildings. Danger!", "fx": "glow"},
    "Blow": {"text": "With low, covered lights, the ocean is the brightest way again. The hatchlings head for the sea!", "fx": "shade"}
  },
  "best": ["Ahatch", "Bhatch"],
  "frame": "On this beach, the hatchling crawls ___, because ___.", "claimLead": "On this beach, the hatchling crawls", "claimMid": "because",
  "claim": {
    "A": {"feat": ["toward the sea", "toward the buildings"], "featOk": 0, "eat": ["the brightest light is over the ocean", "the brightest lights are on land"], "eatOk": 0},
    "B": {"feat": ["toward the sea", "toward the buildings"], "featOk": 1, "eat": ["the brightest light is over the ocean", "the brightest lights are on land"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Follow the light.</b> On a natural beach, the sky over the ocean is brighter than the land, so hatchlings crawl toward the water.",
    "B": "<b>Lost in the lights.</b> Bright lights on land can pull hatchlings the wrong way, toward roads and parking lots. Many Florida beach towns have rules for turtle-safe lights during nesting season."
  },
  "missFeat": "Look at your hatchling test for {label} again. Which way did it crawl?",
  "missClaim": "Think about your tests. What made the difference between the two beaches?",
  "done": "Same hatchlings, two beaches. The brightest light decided which way they crawled, and people control the lights.",
  "after": {"kicker": "🎬 Behind the scenes · Counting hatchlings", "img": "after2", "alt": "A group of baby sea turtles crawling across wet sand",
            "html": "Every nesting season, trained teams walk Florida beaches at sunrise. They mark nests, count tracks, and check which way the hatchlings went. That evidence shows towns where their lights need to change."}
}

wall = {
  "kicker": "🏔 The Mountain Climb", "title": "Explore a mountain, one stop at a time",
  "look": "A model of a mountain in Rocky Mountain National Park, cut into four stops from the top down. Each stop holds a clue and a real photo. The dial on the left shows how high up you are, in feet.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "Leo says, \"If winters keep getting warmer, pikas will move down the mountain.\" What do you predict?",
              "options": [["up", "They will need to live higher up, where it stays cold"], ["down", "They will move lower down the mountain"]], "answer": "up",
              "mine": "Your prediction: <b>{p}</b>. Let's explore the mountain and find out.",
              "confirm": "You predicted pikas need to live higher up. You were right: pikas need cold, and the cold is at the top.",
              "change": "You predicted pikas would move lower. The mountain changed that idea: lower down is warmer, and pikas need cold."},
  "sky": "sky", "skyAlt": "Green tundra slopes and rocky peaks under a cloudy blue sky", "skyCap": "Alpine tundra · Rocky Mountain National Park",
  "unit": "Stop", "found": "Stop {n} explored",
  "elevator": ["Start", "12,000 ft", "11,000 ft", "9,500 ft", "8,000 ft"],
  "line": ["COLD UP HIGH", "WARMER DOWN LOW"],
  "lockTag": "🔒 Open the stop above first", "locked": "Open the stop above first. We explore the mountain one stop at a time.",
  "first": "Brush the glowing first stop. Drag across it (or tap it again and again).", "next": "Keep going. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "From the top down, the mountain gets warmer. Each living thing lives where the temperature fits it.",
  "rule": "<b>Living things live where the conditions fit them.</b> When winters get shorter and warmer, snow melts sooner, flowers bloom earlier, and animals that need cold, like pikas, can only live higher up. In some mountains, scientists now find pikas only higher up than where they lived long ago.",
  "choices": ["🪨 Pikas hide from the heat in cool rock piles", "🌲 Trees grow short and twisted, then stop", "❄️ Snow on the forest floor melts sooner", "🌼 Wildflowers bloom earlier in the year"],
  "layers": [
    {"name": "Stop 1 · The rocky top", "rock": "snowcap", "img": "l1", "alt": "Rocky tundra with long patches of snow on a high slope",
     "ask": "Look at Stop 1. Read the clue AND the photo. What happens here?",
     "clue": "Up here it's cold and windy, and snow lasts into summer. A pika can overheat on a day that feels only warm to us, so it stays cool under the rocks.",
     "ans": 0, "ok": "Yes! Pikas need cold, so they live in cool rock piles high up.", "tag": "🪨 The top · pikas",
     "miss": {"1": "Close! But are there trees up here? Read the clue.", "2": "Not quite. Read the clue: which animal lives here?", "3": "Not quite. Read the clue: which animal lives here?"},
     "env": "e1", "envAlt": "A small, round pika with grass in its mouth among pink rocks", "envCap": "A pika gathering grass for winter · Rocky Mountain National Park"},
    {"name": "Stop 2 · The treeline", "rock": "leafdark", "img": "l2", "alt": "Short, twisted spruce trees and bushes on a rocky slope high on a mountain",
     "ask": "Look at Stop 2. Read the clue AND the photo. What happens here?",
     "clue": "Trees here grow short and twisted. Any higher, it's too cold and windy for trees at all. This line is called the treeline.",
     "ans": 1, "ok": "Yes! The cold stops trees from growing any higher.", "tag": "🌲 Treeline · trees stop",
     "miss": {"0": "That was the stop above. Read the clue: what happens to the trees?", "2": "Not yet. Read the clue: what happens to the trees?", "3": "Not yet. Read the clue: what happens to the trees?"},
     "env": "e2", "envAlt": "Grassy tundra with a sign that says Area Closed, Tundra Protection, and snowy peaks behind", "envCap": "Tundra above the treeline · Rocky Mountain National Park"},
    {"name": "Stop 3 · The forest", "rock": "leafmid", "img": "l3", "alt": "Tall, dark pine and spruce trees with deep snow on the ground",
     "ask": "Look at Stop 3. Read the clue AND the photo. What happens here?",
     "clue": "Deep snow covers the forest floor all winter. When winters are warmer, the snow melts sooner, and the ground dries out earlier.",
     "ans": 2, "ok": "Yes! Warmer winters mean the snow melts sooner.", "tag": "❄️ Forest · melts sooner",
     "miss": {"0": "That was higher up. Read the clue: what is the snow doing?", "1": "That was higher up. Read the clue: what is the snow doing?", "3": "Close! The flowers come next. Read the clue: what is the snow doing?"},
     "env": "e3", "envAlt": "Pine cones on the forest floor, half buried in round grains of snow", "envCap": "Snow on the forest floor · Longs Peak Trailhead, Rocky Mountain National Park"},
    {"name": "Stop 4 · The meadow", "rock": "leafsun", "img": "l4", "alt": "A mountain meadow full of tall grass and small yellow flowers",
     "ask": "Look at Stop 4. Read the clue AND the photo. What happens here?",
     "clue": "Meadow flowers start growing when the snow melts. Scientists who write down bloom dates every year see many flowers blooming earlier than they used to.",
     "ans": 3, "ok": "Yes! When snow melts sooner, flowers bloom sooner.", "tag": "🌼 Meadow · earlier blooms",
     "miss": {"0": "That was way up top. Read the clue: what do the flowers do?", "1": "That was higher up. Read the clue: what do the flowers do?", "2": "That was the forest. Read the clue: what do the flowers do?"},
     "env": "e4", "envAlt": "Bright yellow mountain sunflowers and small purple daisies", "envCap": "Wildflowers · Rocky Mountain National Park"}
  ],
  "mix": {
    "q": "Ava says, \"One warm winter proves the mountain is changing.\" What do you think?",
    "options": [
      {"t": "Ava is right. One warm winter is enough proof.", "miss": "Think like a scientist. How many winters would you want to compare?"},
      {"t": "One winter isn't enough. Scientists compare records from many years to find a pattern.", "ok": "Yes! A pattern needs lots of evidence, collected over many years."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Old Faithful Kept Erupting",
  "img": "wow", "alt": "Old Faithful geyser shooting a tall plume of steam into a smoky sky, with burned forest behind",
  "caption": "Old Faithful erupts as smoke from the 1988 fires fills the sky · Yellowstone National Park",
  "html": "<p style=\"margin:0 0 8px\">On September 7, 1988, fire swept right up to the buildings at Old Faithful. Firefighters worked to save them, and the geyser kept erupting, just as it always had.</p><p style=\"margin:0\">The next summer, scientists walking the burned ground found tiny pine seedlings almost everywhere they looked. The forest was already starting over.</p>",
  "inset": "inset", "insetCap": "Lodgepole pine seedlings after the fires."}

keyIdea = "Scientists ask a question, make a prediction, collect evidence, look for patterns, and explain what they found. That's how you studied a burned forest, a bright beach, and a warming mountain today, and it's how you studied weather, forces, life cycles, plants, and ecosystems all year. Evidence is what makes a conclusion stronger than a guess."

PRED = [["past", "🕰️ What happened long ago"], ["pattern", "🔁 A pattern that helps us predict"], ["depend", "🔗 How living things depend on each other"]]


def card(id_, img, alt, clues, org, orgShort, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": org, "orgAns": 0, "orgShort": orgShort, "orgMiss": orgMiss,
            "env": dict(PRED)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap,
            "reveal": reveal, "rebuildEnv": envAns, "bts": bts}


det = {
  "look": "Five real things from this year's science lessons. Each card shows one. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap something you see, then name the science topic. Predict what scientists figured out, and see the evidence.",
  "noun": "Card", "need": 3, "inferQ": "Which science topic is it from?", "inferDone": "It's from", "chartSo": "and it shows",
  "predict": {"q": "What did scientists use this evidence to figure out?", "options": PRED},
  "kicker": "What scientists found", "enough": "You already solved 3 Year in Review files. Nice work, scientist!",
  "cols": ["Card", "What I saw", "Topic", "What it shows", "My evidence"],
  "write": {"label": "Card __ shows ___. It's from ___. It helped scientists figure out ___, because ___.", "starter": "Start with: \"Card __ shows…\"", "min": 15,
            "chips": [["thing", "Names what you saw"], ["topic", "Names a science topic"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "A fossil fish pressed flat in pale rock, with its bones and spiny fin showing",
         [{"t": "A fish's bones pressed into rock", "ok": True}, {"t": "A fresh fish from a market", "miss": "Look again. Is this fish soft and fresh, or turned to stone?"}, {"t": "A plastic toy", "miss": "Look again. Is this made by people?"}],
         ["🦴 Fossils and Earth's history", "🧲 Magnets and forces", "🌦 Weather"], "fossils",
         "Which topic studies living things from long ago that turned to stone? Try again.", "past",
         "This fish lived millions of years ago. Try again.",
         "d1h", "A dry, flat-topped hill above gray-green sagebrush", "Fossil Butte National Monument, Wyoming, today",
         "This fish lived in a lake about 50 million years ago. Today the place is dry land. The fossil is evidence that a big, warm lake was once here.",
         "You met this fish, Priscacara, in the fossils lessons."),
    card("B", "d2", "A huge spiral of white clouds over Florida, seen from space",
         [{"t": "A giant spiral of clouds over Florida", "ok": True}, {"t": "A snowy mountain", "miss": "Look again. Is this on the ground or in the sky?"}, {"t": "A forest fire", "miss": "Look again. Is that smoke, or clouds over the ocean?"}],
         ["🌦 Weather and climate", "🌱 Plant parts", "🐢 Animal life cycles"], "weather",
         "Which topic studies storms, clouds, and wind? Try again.", "pattern",
         "Hurricanes come in the same months, over the same warm water. Try again.",
         "d2h", "Clouds seen from the window of an airplane, with its propellers spinning", "NOAA Hurricane Hunters flying through Hurricane Irma, 2017",
         "This is Hurricane Frances over Florida in 2004. Hurricanes follow a pattern: they form over warm ocean water, mostly from June to November. Hurricane Hunter planes fly into storms to collect data, so forecasters can predict where they will go.",
         "NOAA's Hurricane Hunters are based in Lakeland, Florida."),
    card("C", "d3", "An orange monarch butterfly on tall purple flowers in a meadow",
         [{"t": "An orange-and-black butterfly on flowers", "ok": True}, {"t": "A bird's nest", "miss": "Look again. Does it have feathers, or wings with scales?"}, {"t": "A fish", "miss": "Look again. Is it in the water?"}],
         ["🐛 Life cycles and traits", "🧊 Matter and energy", "🪨 Rocks and fossils"], "life cycles",
         "Which topic studies how living things grow and change? Try again.", "pattern",
         "The monarch life cycle repeats every year. Try again.",
         "d3h", "A monarch butterfly with a small round sticker on its wing, resting in a person's hand", "A tagged monarch · Pipestone National Monument, Minnesota, 2019",
         "Monarchs follow patterns: egg, caterpillar, chrysalis, butterfly, again and again. Scientists put tiny stickers on their wings. When a tagged monarch is found far away, it's evidence of where monarchs travel each fall.",
         "Some monarchs fly all the way to Mexico for the winter."),
    card("D", "d4", "From the air: a small, round pool of water in a dry, grassy marsh",
         [{"t": "A round pool of water in a dry marsh", "ok": True}, {"t": "A snowy field", "miss": "Look again. Is this a cold place?"}, {"t": "A parking lot", "miss": "Look again. Do you see cars?"}],
         ["🐊 Florida ecosystems", "🧲 Magnets", "☁️ Clouds"], "Florida ecosystems",
         "Which topic studies the Everglades and its animals? Try again.", "depend",
         "Fish, turtles, and birds all crowd into this pool in the dry season. Try again.",
         "d4h", "A great blue heron standing at the edge of the water near an alligator", "A heron and an alligator share the water · Everglades National Park",
         "This is a gator hole. An alligator keeps it clear, and in the dry season fish, turtles, and birds depend on its water to survive. It's evidence that living things depend on each other.",
         "You studied gator holes in the Everglades lessons."),
    card("E", "d5", "A chunk of pale rock made of many tiny broken shells stuck together",
         [{"t": "Tiny shells stuck together into rock", "ok": True}, {"t": "Ice cubes", "miss": "Look again. Would ice look like broken shells?"}, {"t": "A pile of leaves", "miss": "Look again. Is it soft like leaves, or hard like rock?"}],
         ["🧱 Matter and its properties", "🌀 Weather", "🦋 Life cycles"], "matter",
         "Which topic studies what things are made of and how hard they are? Try again.", "past",
         "These shells piled up long ago, before they became rock. Try again.",
         "d5h", "The tall gray stone walls of an old fort beside a grassy moat", "Castillo de San Marcos, St. Augustine, Florida, today",
         "This rock is coquina. It formed long ago from shells that piled up and got pressed and cemented together. Builders used coquina for the Castillo de San Marcos, finished in 1695.",
         "Coquina is soft enough to cut, but cannonballs sank into it instead of smashing it.")
  ]
}

rebuild = {"title": "Use your evidence to sort the discoveries", "missPrefix": "Hmm. Look at your Year in Review files again. ", "kicker": "🗂️ Sort the discoveries", "whyStart": "I chose this because…",
  "words": {"do": "Pick one you solved. Pick the group it belongs in, then tap the other ones that belong in the same group.", "cap": "{card}: {org}. Which group does it belong in?",
            "pickPlace": "Pick the group it belongs in.", "pickItems": "Tap each one that belongs in this group too.", "why": "What evidence made you choose this group?", "done": "🗂️ Sorted with your evidence."},
  "envs": [
    {"key": "past", "name": "🕰️ Long ago", "img": "d1h", "cap": "Clues about the past…"},
    {"key": "pattern", "name": "🔁 A pattern", "img": "d2", "cap": "Things that happen again and again…"},
    {"key": "depend", "name": "🔗 Depend on each other", "img": "d4h", "cap": "Living things that need each other…"}
  ],
  "life": [
    {"name": "🦴 A fossil fish in desert rock", "img": "d1", "env": "past", "miss": "A fossil is a clue about long ago."},
    {"name": "🐢 Hatchlings crawl to the brightest light, night after night", "img": "hatch", "env": "pattern", "miss": "It happens again and again. That's a pattern."},
    {"name": "🌼 Snow melts, then flowers bloom, every spring", "img": "l4", "env": "pattern", "miss": "It repeats every year. That's a pattern."},
    {"name": "🐊 Fish and birds need the gator's pool", "img": "d4", "env": "depend", "miss": "The animals need the pool to survive."},
    {"name": "🪨 Shells pressed into coquina rock", "img": "d5", "env": "past", "miss": "Those shells piled up long ago."}
  ]}

quiz = [
  {"q": "A scientist notices that plants near a river grow taller than plants far from it. What should she do next?", "options": [
    {"t": "Decide the river causes tall plants and stop investigating.", "miss": "Scientists don't stop at one observation. They collect more data to find out if the pattern is real."},
    {"t": "Ignore the observation because it might be a coincidence.", "miss": "Scientists don't ignore what they see. They collect more data to find out if the pattern is real."},
    {"t": "Collect more data: measure the plants and the distance from the river to look for a pattern.", "ok": "🌈 Yes! One observation isn't enough. Real scientists collect more data and look for patterns before drawing conclusions."}]},
  {"q": "Which of these is the best example of using evidence to support an idea?", "options": [
    {"t": "\"I think magnets are cool because they stick to the fridge.\"", "miss": "Evidence means specific data or observations, not opinions or guesses. Look for the answer with a real measurement."},
    {"t": "\"The magnet attracted the paperclip from 2 cm away but not from 10 cm. Distance affects the force.\"", "ok": "⭐ That's evidence-based thinking: a specific observation that supports a clear idea."},
    {"t": "\"Magnets probably work because of electricity inside them.\"", "miss": "Evidence means specific data or observations, not opinions or guesses. Look for the answer with a real measurement."}]},
  {"q": "You studied weather, ecosystems, forces, and engineering this year. What do all of these have in common?", "options": [
    {"t": "Scientists study all of them by asking questions, collecting evidence, and looking for patterns.", "ok": "🌟 Exactly! The process is what connects all science: asking, observing, collecting evidence, and explaining."},
    {"t": "They are all about animals and plants.", "miss": "Think bigger than the topic. What steps did you follow in every investigation this year?"},
    {"t": "They all require the same kind of equipment to study.", "miss": "Think bigger than the topic. What steps did you follow in every investigation this year?"}]}
]

assign = {
  "partA": {"title": "Investigation report", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Which scenario did you choose: A (the burned forest), B (the turtle beach), or C (the warmer mountain)? What was your science question?", "type": "text", "min": 10,
     "chips": [["scen", "Names your scenario"], ["ask", "Asks a question"]]},
    {"n": 2, "q": "What prediction did you make? Was it correct? Explain.", "type": "text", "min": 10,
     "chips": [["pred", "Says what you predicted"], ["because", "Gives a reason (because, so)"]]},
    {"n": 3, "q": "Name two science topics from this year that connect to your scenario. How do they connect?", "type": "text", "min": 12,
     "chips": [["topic", "Names a science topic"], ["conn2", "Says how it connects"]]}
  ]},
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "What is the difference between a guess and a conclusion? Why does evidence matter?", "type": "text", "min": 12,
     "chips": [["concl", "Uses the word conclusion"], ["evid", "Uses the word evidence"]]},
    {"n": 2, "q": "Describe one cause and effect relationship from your scenario. What caused the change, and what happened because of it?", "type": "text", "min": 12,
     "chips": [["cause", "Names a cause"], ["effect", "Names an effect (so, then, because of)"]]}
  ]},
  "write": {"title": "You just finished your last science investigation of 3rd grade. What did you discover, and what does it tell you about how the natural world works?",
    "do": "Pick one from your evidence chart. Answer the three questions. Use at least two of the science words under the boxes.",
    "vocab": ["evidence", "investigation", "pattern", "cause and effect", "conclusion", "model"], "need": 2,
    "prompts": [["What did you find out?", "Start with: \"In my investigation, I discovered that…\""],
                ["What evidence supports your thinking?", "Start with: \"I know this because…\""],
                ["Why does this matter?", "Start with: \"This matters because…\""]]},
  "partC": {"do": "Make your \"My Year as a Scientist\" page. Draw a model of your scenario with at least 3 labels and arrows that show cause and effect.",
            "labels": ["My favorite science moment this year, and what made it special", "My advice to next year's 3rd graders about thinking like a scientist"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 Year in Review files and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all three answers.", "req": {"text": {"in-a1": 10, "in-a2": 10, "in-a3": 12}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least two science words.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 2}}
  ]
}

premiere = {"title": "Premiere my scientist story", "thinkLabel": "It's from", "director": "JUNIOR SCIENTIST", "storyKicker": "My year in science",
  "frames": [
    {"k": "formation", "label": "After the Fire", "img": "o4", "cap": "After the Fire: the forest came back."},
    {"k": "compare", "label": "The Turtle Test", "img": "tb", "cap": "The Turtle Test: the brightest light leads the way."},
    {"k": "wall", "label": "The Mountain Climb", "img": "l1", "cap": "The Mountain Climb: pikas need the cold up high."},
    {"k": "det", "label": "Year in Review", "img": "d2", "cap": "Year in Review: evidence from all year long."}],
  "finale": {"kicker": "Optima Academy Online · 3rd Grade Science", "title": "Official 3rd Grade Scientist", "certifies": "This certifies that",
             "noName": "A 3rd Grade Scientist", "sub": "finished a whole year of science and can:",
             "skills": ["ask questions, predict, and investigate", "collect evidence and look for patterns", "explain a conclusion with evidence"],
             "dateLabel": "Date", "signName": "Opti", "signed": "Opti the owl · Wonder Films guide", "seal": "Season Finale",
             "button": "Open my certificate", "saveLabel": "Save my certificate", "file": "my-scientist-certificate.png",
             "nameTip": "Type your first name in the Director's first name box, then open your certificate again to put your name on it."}}

nxt = {"title": "🎉 That's a wrap on 3rd grade science!", "text": "You finished every Wonder Film this year. Keep asking questions this summer: watch the clouds, flip over a rock, follow a bird. Every scientist starts by noticing. Get ready for 4th grade science!"}

chips = {
  "part": {"any": ["track", "tracks", "footprint", "footprints", "prints", "writing", "words", "date", "poem", "drawing", "drawings", "line", "lines", "paper", "page", "pages", "book", "handwriting", "pencil", "ink", "name"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "thing": {"any": ["fossil", "fish", "hurricane", "storm", "clouds", "spiral", "butterfly", "monarch", "pool", "hole", "gator", "alligator", "rock", "shells", "coquina", "bones"]},
  "topic": {"any": ["fossil", "fossils", "weather", "climate", "life", "cycle", "cycles", "ecosystem", "ecosystems", "matter", "energy", "forces", "plants", "florida", "everglades", "traits", "earth"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "scen": {"re": "\\b(a|b|c|scenario|fire|forest|turtles?|beach|parking|winters?|snow|mountain|pikas?)\\b"},
  "pred": {"any": ["predict", "predicted", "prediction", "thought", "guess", "guessed", "think", "expected"]},
  "conn2": {"any": ["because", "connects", "connect", "connected", "so", "when", "shows", "helps", "explains"]},
  "concl": {"re": "conclusions?"},
  "evid": {"re": "evidence"},
  "cause": {"any": ["fire", "fires", "light", "lights", "warm", "warmer", "snow", "heat", "parking", "winter", "winters", "melt", "melts", "burn", "burned"]},
  "effect": {"re": "\\b(so|then|because|caused|causes|made|makes|led|result)\\b"}
}

L = {"id": "g3sci-33-02", "lesson": "33.02", "title": "Your Final Science Investigation", "emoji": "🎓",
  "details": ["📅 Q4 · Unit 11 · National Park Capstone", "📖 Week 33 · Lesson 33.02", "🌎 CPALMS Integrated Review · NGSS Integrated Review", "⏱ About 35 minutes"],
  "icans": ["ask a science question and design a way to investigate it.", "use evidence to explain what I discovered.", "reflect on how I've grown as a scientist this year."],
  "opti": {"warm": "It's our season finale! First, inspect two old pages from a real scientist's field book.",
           "lesson": "Three scenarios, three investigations: a burned forest, a bright beach, and a mountain that's getting warmer.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Your last assignment of the year! Show your evidence, draw your year, then premiere your film."},
  "film": film, "scientist": "scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Academic Festival Overture (Johannes Brahms), Musopen public domain recording (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The fire movie, the Turtle Test, and the mountain are models; every place photo is real. The field book page is by Vernon Orlando Bailey, Nevada, 1890 (Smithsonian Institution Archives). The opened pine cone in scene 2 is from Yellowstone's 2016 Maple Fire; the twisted treeline trees at Stop 2 grow on Wheeler Peak, Great Basin National Park, Nevada."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-33-02-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the page, then tap three things you notice."},
  "how-33-02-compare": {"page": "Put the hatchling under one beach and the low lights under the other: drag them, or tap one, then a beach. Press Let the hatchlings go. Then swap.",
                        "say": "Put the hatchling under one beach and the low lights under the other: drag them, or tap one, then a beach. Press Let the hatchlings go. Then swap."},
  "how-33-02-wall": {"page": wall["do"], "say": wall["do"]},
  "how-33-02-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap something you see, then name the science topic. Predict what scientists figured out, and see the evidence."},
  "how-33-02-partc": {"page": assign["partC"]["do"], "say": "Make your My Year as a Scientist page. Draw a model of your scenario with at least three labels and arrows that show cause and effect."}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"33-02-welcome": L["opti"]["warm"], "33-02-lesson": L["opti"]["lesson"], "33-02-check": L["opti"]["check"], "33-02-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
