#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/24-01/lesson.json, how-lines.json, scripts.json."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))

def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s

film = {
  "id": "g3sci-24-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 24.01 · What Is Conservation?",
  "title": "The Comeback",
  "bigQuestion": "How do people protect the natural world, and why does it matter?",
  "poster": "f_dawn", "endPoster": "f_today", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    ph(3.4, 6.6, "f_dawn", "Two bald eagles fly as dark shapes across a pink dawn sky above a line of bare trees", "Westmoreland State Park, Virginia · Dawn",
       frm=(1.0, .5, .55), to=(1.45, .47, .47), fade=1.2, sfx="whoosh", sfxArg=2.0),
    {"t": 10.0, "d": 5.6, "type": "archive", "img": "f_spray", "alt": "An old black-and-white photo of a small airplane spraying a long white cloud over a dark forest",
     "note": "An airplane sprays DDT over a forest in Oregon, 1955.", "fade": 0.8},
    ph(15.6, 6.4, "f_egg", "Two adult bald eagles in a big stick nest look down at one white egg", "An eagle nest with one egg · Big Bear Lake, California, 2019",
       frm=(1.12, .55, .6), to=(1.0, .5, .5)),
    {"t": 22.0, "d": 3.2, "type": "flash", "lines": ["Our national bird?", "Almost gone?"], "beats": [0.15, 1.2], "fade": 0.15},
    ph(25.2, 8.0, "f_chicks", "A mother bald eagle stands in a huge nest of sticks with two fuzzy gray chicks beside her", "A mother eagle and two chicks · Philadelphia, Pennsylvania",
       frm=(1.16, .45, .55), to=(1.0, .5, .5), fade=1.0, **{"in": "ripple"}, fx=["rays"], sfx="shimmer",
       tags=[{"text": "1963: 417 nesting pairs", "x": 6, "y": 40, "at": 0.8}, {"text": "2007: 9,789 nesting pairs", "x": 6, "y": 52, "at": 4.4}]),
    ph(33.2, 6.0, "f_soar", "A bald eagle with wide brown wings and a white head soars low over green bushes", "A bald eagle soars · Seedskadee National Wildlife Refuge, Wyoming",
       frm=(1.0, .4, .5), to=(1.12, .5, .45)),
    ph(39.2, 7.6, "f_today", "A bald eagle stands in its big stick nest high in a pine tree under a blue sky", "Kennedy Space Center, Florida · Today",
       frm=(1.0, .5, .5), to=(1.1, .55, .4), fade=0.9),
    {"t": 46.8, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.8, "text": "Dawn over a quiet lake. Two bald eagles ride the morning air.", "voice": "opti-1"},
    {"t": 10.3, "d": 5.0, "text": "Long ago, people sprayed a bug poison called DDT almost everywhere.", "voice": "opti-2"},
    {"t": 15.9, "d": 5.8, "text": "It washed into lakes and fish. Eagles ate the fish, and their eggshells grew thin.", "voice": "opti-3"},
    {"t": 22.1, "d": 2.8, "text": "Our national bird? Almost gone?", "voice": "opti-4"},
    {"t": 25.6, "d": 4.4, "text": "Then people chose to act. They banned DDT and protected eagle nests.", "voice": "opti-5"},
    {"t": 30.4, "d": 2.6, "text": "Year by year, the eagles came back.", "voice": "opti-6"},
    {"t": 33.5, "d": 5.4, "text": "Today, bald eagles nest in every state except Hawaii.", "voice": "opti-7"},
    {"t": 39.6, "d": 6.8, "text": "So how do people protect the natural world? And why does it matter?", "voice": "opti-8"}
  ]
}

specimen = {
  "img": "spec", "aspect": "1920/1285", "radius": 0.07,
  "hotspots": [
    {"name": "A long, pale scar across its back", "x": 0.61, "y": 0.41},
    {"name": "A second, shorter scar", "x": 0.44, "y": 0.36},
    {"name": "A flipper, like a paddle", "x": 0.25, "y": 0.57},
    {"name": "A round snout with whiskers", "x": 0.09, "y": 0.27},
    {"name": "Bumpy, spotted skin near the tail", "x": 0.87, "y": 0.62},
    {"name": "Sunlight rippling on the water above", "x": 0.42, "y": 0.06}
  ],
  "kicker": "🔎 Mystery specimen", "title": "What made these marks on a manatee's back?",
  "alt": "A big gray manatee swims just under the surface of blue-green water, with long pale stripes on its back",
  "look": "A real photo of a Florida manatee, a big, gentle animal that eats water plants. Look at the pale stripes on its back. A specimen is one real thing that scientists study. Are the stripes a pattern it was born with? Or marks from something that happened to it? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the manatee, then tap 3 things you notice.",
  "number": "No. 24.01-A",
  "card": ["<b>Specimen A</b>", "Found: in Florida waters", "Size: a grown manatee is about 10 feet long", "What made the marks? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the manatee)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🌱", "conservation", "Taking care of natural resources so they stay healthy and last for the future."],
  ["🏡", "habitat", "The place where a plant or animal lives and gets what it needs to survive."],
  ["🌊", "natural resource", "Something from nature that living things use, like water, soil, clean air, or trees."],
  ["🚫", "pollution", "Harmful materials that get into the air, water, or soil and damage the environment."],
  ["♻️", "reduce", "To use less of something, like less water, less plastic, or less energy, so resources aren't used up."],
  ["🛡️", "protect", "To keep something safe from harm, like making laws that stop people from destroying a habitat."]
]

parts = [
  {"kicker": "🌱 Part 1", "title": "What Conservation Means",
   "html": "<p>Every day, people use natural resources: water, soil, clean air, wood, and food from the land. They come from the Earth, and if we use them carelessly, they can run out or get damaged.</p><p>Conservation is protecting natural places, plants, animals, and resources so they stay healthy. It doesn't mean people can never use the land. It means making smart choices about how we use it.</p>"},
  {"kicker": "🏞️ Part 2", "title": "How People Protect Habitats",
   "html": "<p>One strong conservation tool is a park or refuge, where building and logging are not allowed and animals can live safely.</p><p>Conservation happens outside parks too. Communities plant trees and sea oats. Scientists bring back wetlands that were drained. Laws protect nesting beaches for sea turtles and birds. These are conservation solutions: actions people choose because evidence shows they work.</p>"},
  {"kicker": "🔍 Part 3", "title": "Making a Claim About Conservation",
   "html": "<p>Scientists don't just say \"we should protect this place.\" They gather evidence: they count animals, test the water, and measure how many trees are left. Then they make a claim: this solution will help, and here's why.</p><p>Anyone can say something would help. Evidence is what makes a claim convincing.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Comeback Cases"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start where the poison first gets into the water.",
  "kicker": "🎞️ Put the scenes in order", "title": "How did the bald eagle come back?",
  "look": "Four real photos tell the story of the bald eagle, but they are mixed up. DDT was a bug poison people once sprayed on farms, forests, and towns. A ban is a law that says to stop. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "An old black-and-white photo of a man spraying from a hose along the edge of a pond", "text": "People spray DDT, and it washes into lakes and rivers.", "play": "DDT washes into water.",
     "miss": ["", "The poison has to get into the water first. Try frame 1.", "Nothing has gone wrong yet to fix. Try frame 1.", "This is where the story starts. Try frame 1."]},
    {"img": "o2", "alt": "Two adult bald eagles in a stick nest look down at one white egg", "text": "Eagles eat fish with DDT in them. Their eggshells grow thin and break.", "play": "Thin eggs break.",
     "miss": ["The poison has to reach the fish first. Try a later frame.", "", "The eggs broke before people fixed the problem. Try an earlier frame.", "The eggs broke before the eagles came back. Try an earlier frame."]},
    {"img": "o3", "alt": "Four scientists kneel on the forest floor around a young eagle, checking it and fitting a small band", "text": "People ban DDT and protect eagles. Scientists check on young eagles.", "play": "Laws protect eagles.",
     "miss": ["People acted after the problem started. Try a later frame.", "People acted after the eggs broke. Try a later frame.", "", "The laws came before the eagles came back. Try an earlier frame."]},
    {"img": "o4", "alt": "Two young bald eagles with dark brown feathers stand in a big nest", "text": "Strong eggs hatch, and eagle numbers climb.", "play": "Eagles come back.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "A friend says, \"Conservation means people can never use nature at all.\" Is that right?",
    "options": [
      {"t": "Yes. To protect nature, people must stay away from it.", "miss": "Think about the eagles. Did people stop using lakes and land, or did they make a smarter choice about one poison?"},
      {"t": "No. It means using nature wisely so it lasts.", "ok": "Yes! People still fish, farm, and visit lakes. They stopped using DDT, a choice that let eagles come back."}
    ]
  }
}

movie = {
  "model": "eagle-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "water",
  "real": "real", "realAlt": "Two bald eagles in a big stick nest high in a pine tree under a pale sky",
  "stamp": "PROTECT IT", "endCap": "A real nest · Kennedy Space Center.",
  "beats": [
    {"at": 0, "cap": "1 · DDT gets into the water.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["1958"]},
    {"at": 2600, "cap": "2 · A ban. Strong eggs.", "model": {"show": "s2"}, "counter": ["1972"]},
    {"at": 5200, "cap": "3 · Chicks hatch.", "model": {"show": "s3"}, "counter": ["1980s"]},
    {"at": 7800, "cap": "4 · More eagles and nests.", "model": {"show": "s4"}, "counter": ["2007"], "sfx": "shimmer"},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Dune Test", "title": "Do plants protect a sand dune?",
  "look": "Two real sand dunes, each on a lit specimen tray. A dune is a hill of sand by a beach. Specimen A is a Florida dune covered with sea oats, a tall beach grass with long roots. Specimen B is a dune that lost its plants. Under the trays are two model tests: a fan for wind and a cup of water for waves.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A white sand dune covered with clumps of sea oats, with an old wooden sand fence half buried in the sand", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A bare, broken edge of a sand dune with fallen trees and no plants holding the sand", "label": "Specimen B"}
  ],
  "materials": [{"key": "wave", "label": "Cup of water (waves)", "swatch": "water"}, {"key": "fan", "label": "Fan (wind)", "swatch": "fan"}],
  "ask": [
    {"q": "Which dune has plants growing all over it?", "ans": "A", "ok": "Yes. Specimen A is covered with sea oats.", "miss": "Look closely. Which one has tall grass on the sand?"},
    {"q": "Which dune is bare sand with no plants holding it?", "ans": "B", "ok": "Yes. Specimen B lost its plants.", "miss": "Look again. Which one has a broken edge of bare sand?"}
  ],
  "press": "🌊 Run the test",
  "testDo": "Put the water under one tray and the fan under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. Real dunes face big storms, wind, and waves.",
  "results": {
    "Awave": {"text": "The water soaks in. The sea oat roots hold the sand together, so the dune stays in place.", "fx": "wet"},
    "Afan": {"text": "The sea oats sway in the wind, but their roots keep the sand from blowing away.", "fx": "sway"},
    "Bwave": {"text": "The wave washes the loose sand away, and the dune slumps down.", "fx": "slump"},
    "Bfan": {"text": "The wind blows loose sand off the top. With no roots, nothing holds it.", "fx": "slump"}
  },
  "best": ["Awave", "Bwave"],
  "frame": "This dune has ___, so when waves hit, it ___.", "claimLead": "This dune has", "claimMid": "so when waves hit, it",
  "claim": {
    "A": {"feat": ["sea oats with roots", "bare, loose sand"], "featOk": 0, "eat": ["stays in place", "washes away"], "eatOk": 0},
    "B": {"feat": ["sea oats with roots", "bare, loose sand"], "featOk": 1, "eat": ["stays in place", "washes away"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Roots → a strong dune.</b> Sea oat roots hold the sand like a net.",
    "B": "<b>No plants → a weak dune.</b> Loose sand washes and blows away."
  },
  "missFeat": "Look at {label} again. Does it have plants, or bare sand?",
  "missClaim": "Think about your test. Which dune stayed in place when the water hit?",
  "done": "Plants protect the dune, and the dune protects the beach and the animals behind it. That's why planting sea oats is a conservation solution.",
  "after": {"kicker": "🎬 Behind the scenes · Leave the sea oats", "img": "aft2", "alt": "Green sea oat dunes along a beach with tall city buildings in the distance",
            "html": "In Florida, it's against the law to pick or cut sea oats. Many beach towns build wooden walkovers so people can cross the dunes without stepping on the plants. After big storms, volunteers plant new sea oats to help the dunes grow back."}
}

wall = {
  "kicker": "🌲 The Eagle Tree", "title": "Climb down one tall longleaf pine",
  "look": "A model of one tall longleaf pine in a protected Florida forest, from the treetop down to the ground. Each stop has a real photo. A longleaf pine is a pine tree with very long needles. The brass dial on the left shows where you are on the tree.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the place shows.",
  "predict": {"q": "When people protect one pine forest, who does it help?",
              "options": [["eagles", "Just the eagles that nest there"], ["many", "Many kinds of animals at once"]], "answer": "many",
              "mine": "Your prediction: <b>{p}</b>. Let's climb down the tree and find out.",
              "confirm": "You predicted many kinds of animals. The evidence agrees: eagles, woodpeckers, squirrels, and tortoises all live on this one tree.",
              "change": "You predicted just the eagles. The evidence changed that idea: eagles, woodpeckers, squirrels, and tortoises all live on this one tree."},
  "sky": "sky", "skyAlt": "Tall, straight longleaf pines standing far apart over a floor of grass and small plants", "skyCap": "A longleaf pine forest · southeastern United States",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Sky", "Treetop", "Pine<br>crown", "Trunk", "Forest<br>floor"],
  "line": ["TREETOP", "FOREST FLOOR"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We climb down one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Climb down. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the line. One tree holds an eagle nest, food for squirrels, a woodpecker home, and a tortoise burrow at its roots. Protect the forest, and you protect them all.",
  "rule": "<b>Protect the habitat, protect them all.</b> Saving one forest helps many living things at once. People still have to care for it: longleaf forests need small, careful fires every few years, set by trained crews.",
  "choices": ["🦅 A bald eagle nest", "🌰 Pine seeds that feed animals", "🐦 A woodpecker home in a living pine", "🐢 A burrow many animals share"],
  "layers": [
    {"name": "Stop 1 · The treetop", "rock": "leafsun", "img": "l4", "alt": "A huge stick nest in the top of a pine tree, with a bald eagle sitting in it",
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "Bald eagles build huge stick nests near the tops of tall pines close to water. They use the same nest year after year and add new sticks each time.",
     "ans": 0, "ok": "Yes! A bald eagle nest.", "tag": "🦅 Treetop",
     "miss": {"1": "Look at the photo. Is that a pine cone, or a nest of sticks?", "2": "Not yet. That's lower on the trunk.", "3": "Not yet. We're at the very top of the tree."},
     "env": "e4", "envAlt": "A bald eagle perched on a pine branch beside its nest", "envCap": "A bald eagle by its nest · Merritt Island National Wildlife Refuge, Florida"},
    {"name": "Stop 2 · The pine crown", "rock": "leafmid", "img": "l3", "alt": "Long green pine needles around a bunch of small blue-gray pollen cones",
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "Longleaf pines grow big cones full of seeds. Fox squirrels, birds, and other animals eat the seeds.",
     "ans": 1, "ok": "Yes! Pine seeds that feed animals.", "tag": "🌰 Pine crown",
     "miss": {"0": "The nest is higher up. Read the clue: what do these cones hold?", "2": "Not yet. The woodpecker home is lower on the trunk.", "3": "Not yet. The ground is still far below."},
     "env": "e3", "envAlt": "A big gray fox squirrel with a bushy tail running over pine needles", "envCap": "A fox squirrel · central Florida"},
    {"name": "Stop 3 · The trunk", "rock": "bark", "img": "l2", "alt": "A small black-and-white woodpecker clings to a pine trunk at the round opening of a hole",
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "Red-cockaded woodpeckers carve their homes inside living longleaf pines. Digging one hole can take a year or more. When old forests were cut down, these woodpeckers lost their homes.",
     "ans": 2, "ok": "Yes! A woodpecker home in a living pine.", "tag": "🐦 Trunk",
     "miss": {"0": "This hole is in the trunk, not a nest of sticks.", "1": "Close! But read the clue: what lives in this hole?", "3": "Not yet. We're still on the trunk."},
     "env": "e2", "envAlt": "A red-cockaded woodpecker with a black cap and white cheek clinging to a pine trunk", "envCap": "A red-cockaded woodpecker · Georgia"},
    {"name": "Stop 4 · The forest floor", "rock": "soil", "img": "l1", "alt": "A sandy hole at the base of grass and young pines in an open forest",
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "Gopher tortoises dig long burrows in the sandy ground. Hundreds of other kinds of animals, like frogs, snakes, and mice, hide in them too.",
     "ans": 3, "ok": "Yes! A burrow many animals share.", "tag": "🐢 Forest floor",
     "miss": {"0": "Look at the photo. Is this up in the tree, or on the ground?", "1": "These aren't pine cones. Read the clue: who digs this hole?", "2": "This hole is in the ground, not in a tree."},
     "env": "e1", "envAlt": "A gopher tortoise with a domed shell crawls into a sandy burrow", "envCap": "A gopher tortoise at its burrow · Fort Pierce, Florida"}
  ],
  "mix": {
    "q": "A forest is now protected. A friend says, \"Great, the job is done!\" Is that right?",
    "options": [
      {"t": "Yes. Once a place is protected, nobody has to do anything else.", "miss": "Read the rule again. What do longleaf forests still need every few years?"},
      {"t": "No. People still have to care for it and keep checking on it.",
       "ok": "Yes! Protected places still need care, like careful fires in a longleaf forest, and scientists keep counting animals to see if it's working."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Scientists know manatees by their scars",
  "img": "wow", "alt": "Dozens of gray manatees rest close together in clear, shallow spring water",
  "caption": "Manatees crowd into warm spring water in winter · Three Sisters Springs, Crystal River, Florida",
  "html": "<p style=\"margin:0 0 8px\">Remember the marks on the mystery manatee? Most scars like those come from boat propellers. Each manatee's scars make a pattern, a little like a fingerprint. Florida scientists photograph the scars and keep a catalog, so they can tell one manatee from another year after year.</p><p style=\"margin:0\">That evidence shows how often boats hit manatees. It helped make the case for slow-speed zones, where boats must go slowly. In winter, manatees crowd into warm springs like these, which people protect as a refuge.</p>",
  "inset": "inset", "insetCap": "A manatee in Three Sisters Springs, Crystal River, Florida."}

keyIdea = "Conservation is the choice to protect natural resources and habitats before they are lost. When people take action, like making laws, protecting land, and stopping pollution, the evidence shows that habitats can recover and animals can come back. Human choices can cause harm, and human choices can also help."

M = ["🏗️ Habitat loss: its home was cleared or drained", "🧪 Pollution: poison got into its food or water", "🎯 Too much hunting: people killed too many"]
SHORT = ["habitat loss", "pollution", "too much hunting"]
SOL = {"land": "Protect the land it lives on", "clean": "Stop the pollution", "law": "Make laws against hunting it"}
def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": SOL[envAns], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}

det = {
  "look": "Five real Florida animals that were in trouble. Each card shows the animal and clues about what went wrong. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cases, one at a time. Tap a clue, then pick the problem. Predict the solution that helped, and watch the place today appear.",
  "noun": "Case", "need": 3, "inferQ": "What was the problem?", "inferDone": "Problem", "chartSo": "so people chose to",
  "predict": {"q": "Which conservation solution do you predict helped this animal?", "options": [["land", "🏞️ Protect the land it lives on"], ["clean", "🚫 Stop the pollution"], ["law", "⚖️ Make laws against hunting it"]]},
  "kicker": "The place today", "enough": "You already solved 3 cases. Nice work, conservation scientist!",
  "cols": ["Case", "My observation", "The problem", "The solution", "My evidence"],
  "write": {"label": "Case __ was in trouble because ___. People chose to ___, and today ___.", "starter": "Start with: \"Case __ was in trouble because…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["problem", "Names the problem"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "A tiny dark sea turtle hatchling crawling across white sand",
         [{"t": "Buildings and bright lights spread along its nesting beaches", "ok": True}, {"t": "A bug poison in its fish", "miss": "Look again. What happened to the beaches where turtles lay eggs?"}, {"t": "A boat hitting it", "miss": "Look again. This tiny turtle is on the sand, not in the water."}],
         0, "Read the clue again. Its beaches filled with buildings and lights. Which problem is that? Try again.",
         "land", "The problem was losing its nesting beach. Which solution protects the beach? Try again.",
         "d1h", "The sun rising over calm ocean water seen from a quiet, dark beach", "Today: sunrise at Archie Carr National Wildlife Refuge, Florida (hatchling photo also there)",
         "This protected beach is evidence that saving the land helps: green turtle nests on Florida's survey beaches went from fewer than 300 in some early years to more than 61,000 in 2023.", "beach",
         "Archie Carr National Wildlife Refuge was set aside in 1991 to protect one of the most important sea turtle nesting beaches in the world. Beach towns also use turtle-safe lights so hatchlings head for the sea."),
    card("B", "d2", "A brown pelican with long wings flying in a clear blue sky",
         [{"t": "Its eggs had thin shells from a bug poison in its fish", "ok": True}, {"t": "Its beach was turned into a parking lot", "miss": "Look again. What happened to its eggs?"}, {"t": "It has a long beak", "miss": "That's true, but it's not what went wrong. What happened to its eggs?"}],
         1, "A poison in its food made thin eggs. Which problem is that? Try again.",
         "clean", "The poison was the problem. Which solution stops it? Try again.",
         "d2h", "Brown pelicans perch on low mangroves at the edge of blue water, with buildings far away", "Today: brown pelicans at Pelican Island National Wildlife Refuge, Florida",
         "These pelicans are evidence that stopping the pollution helped. After DDT was banned in 1972, brown pelicans came back and were taken off the endangered list in 2009.", "island",
         "Pelican Island became the first national wildlife refuge in 1903, to protect pelicans from hunters. Years later, DDT made their eggshells thin, just like the eagles'. The ban helped both birds."),
    card("C", "d3", "A tall white wood stork with a bare gray head and long legs wading at a pond's edge",
         [{"t": "The wetlands where it finds fish were drained for farms and towns", "ok": True}, {"t": "People hunted it for its feathers", "miss": "Look again. What happened to the wet places where it eats?"}, {"t": "Oil on its feathers", "miss": "Look again. What happened to the wetlands?"}],
         0, "Its wet feeding places were drained. Which problem is that? Try again.",
         "land", "The problem was losing its wetlands. Which solution keeps them safe? Try again.",
         "d3h", "A long wooden boardwalk crosses a green marsh toward a tall cypress forest under a blue sky", "Today: Corkscrew Swamp Sanctuary, Florida (stork photo: Tampa, Florida)",
         "This protected swamp is evidence that saving wetlands helps. Wood storks did well enough that in 2014 they moved from endangered to threatened, but some years they still can't nest here.", "swamp",
         "Corkscrew Swamp has been protected since 1954, partly to save a big wood stork nesting area. Wood storks need shallow water full of fish at just the right time to feed their chicks, so people still watch the water closely."),
    card("D", "d4", "A big American alligator resting on rocks with its mouth open",
         [{"t": "People killed so many for their skins that few were left", "ok": True}, {"t": "Poison in the water", "miss": "Look again. What were people doing to alligators?"}, {"t": "Its swamp was paved", "miss": "Look again. What were people taking from alligators?"}],
         2, "People killed too many for their skins. Which problem is that? Try again.",
         "law", "The problem was hunting. Which solution stops people from killing too many? Try again.",
         "d4h", "A flat sawgrass marsh stretching to a line of trees under a pale sky", "Today: the Anhinga Trail, Everglades National Park, Florida (alligator photo: Fakahatchee Strand, Florida)",
         "This marsh is evidence that laws worked. Alligators were listed as endangered in 1967, and by 1987 they had recovered. Florida now has more than a million.", "glades",
         "Laws stopped most alligator hunting, and wildlife officers made sure people followed them. Today alligator hunting has strict rules and limits, so the population stays healthy."),
    card("E", "d5", "A blue and gray Florida scrub-jay perched on a twig in short scrub bushes",
         [{"t": "The dry, sandy scrub where it lives was cleared for homes and groves", "ok": True}, {"t": "A poison in its eggs", "miss": "Look again. What happened to the scrub where it lives?"}, {"t": "People hunted it", "miss": "Look again. What happened to its home?"}],
         0, "Its scrub home was cleared. Which problem is that? Try again.",
         "land", "The problem was losing its scrub. Which solution saves the scrub? Try again.",
         "d5h", "A sign reading Scrub Restoration Area in front of low green scrub bushes", "Today: a scrub restoration area · Merritt Island National Wildlife Refuge, Florida",
         "This sign is evidence that people are trying: they protect and restore scrub. But Florida scrub-jays are still threatened, so the work isn't done yet.", "scrub",
         "Florida scrub-jays live only in Florida. They need short, open scrub, so crews cut back and carefully burn overgrown scrub to keep it the right height."),
  ]
}

rebuild = {"title": "Use your evidence to rebuild the place", "missPrefix": "Hmm. Look at your case again. ", "kicker": "🌍 Rebuild the place", "whyStart": "I chose this because the case…",
  "envs": [
    {"key": "beach", "name": "🏖️ A turtle nesting beach", "img": "d1h", "cap": "Sand, surf, dark nights…"},
    {"key": "island", "name": "🐦 A pelican island", "img": "d2h", "cap": "Mangroves and salt water…"},
    {"key": "swamp", "name": "🌳 A cypress swamp", "img": "d3h", "cap": "Tall trees, shallow water…"},
    {"key": "glades", "name": "🌾 A sawgrass marsh", "img": "d4h", "cap": "Flat, wet, and wide…"},
    {"key": "scrub", "name": "🌵 Dry, sandy scrub", "img": "d5h", "cap": "Short bushes, white sand…"}
  ],
  "life": [
    {"name": "🦀 Ghost crabs", "img": "d1h", "env": "beach", "miss": "Ghost crabs dig burrows in beach sand."},
    {"name": "🐟 Mullet", "img": "d2h", "env": "island", "miss": "Mullet swim in the salty lagoon around the island."},
    {"name": "🦉 Barred owls", "img": "d3h", "env": "swamp", "miss": "Barred owls hoot from the tall swamp trees."},
    {"name": "🐦 Anhingas", "img": "d4h", "env": "glades", "miss": "Anhingas dive for fish in the sawgrass marsh."},
    {"name": "🐢 Gopher tortoises", "img": "d5h", "env": "scrub", "miss": "Gopher tortoises dig burrows in dry, sandy scrub."}
  ]}

quiz = [
  {"q": "What does conservation mean?", "options": [
    {"t": "Using as many natural resources as possible before they run out", "miss": "Conservation is about protecting, not using up. Which answer fits that idea?"},
    {"t": "Taking care of natural resources and habitats so they stay healthy for the future", "ok": "🌿 That's right! Conservation is about protecting what we have so it lasts, for animals, plants, and people."},
    {"t": "Studying weather patterns over many years", "miss": "That's about weather. Conservation is about protecting, not using up. Which answer fits that idea?"}]},
  {"q": "A beach where sea turtles nest is losing nests every year because of too many visitors and bright lights. Which conservation solution would help most?", "options": [
    {"t": "Build a parking lot so more visitors can come easily", "miss": "Think about what's causing the problem: lights and too many visitors. A good solution reduces the cause. Which answer does that?"},
    {"t": "Remove all the turtles and move them to an aquarium", "miss": "Think about what's causing the problem: lights and too many visitors. A good solution reduces the cause. Which answer does that?"},
    {"t": "Limit nighttime visitors, reduce bright lights, and protect the nesting area", "ok": "🌱 Yes! Good conservation targets the cause of the problem. The turtles need darker, quieter beaches, so the solution does exactly that."}]},
  {"q": "Why do scientists gather evidence when they argue for a conservation solution?", "options": [
    {"t": "Because a claim without evidence is just an opinion. Evidence is what makes it convincing.", "ok": "⭐ Exactly. Evidence turns an idea into an argument people can trust. That's true for scientists, and for you."},
    {"t": "Because scientists are required to collect evidence for school projects", "miss": "What makes a claim about conservation convincing? It's not just saying \"this would help.\" It's showing why."},
    {"t": "Because only scientists are allowed to talk about conservation", "miss": "Anyone can talk about conservation. What makes a claim convincing? It's showing why it would help."}]}
]

def sort_item(n, q, ok, why_ok, why_miss):
    yes = {"t": "Conservation action"}; no = {"t": "Not a conservation action"}
    (yes if ok else no).update({"ok": why_ok}); (no if ok else yes).update({"miss": why_miss})
    return {"n": n, "q": q, "type": "choice", "options": [yes, no]}

partA = {"title": "Sort and classify", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  sort_item(1, "A city plants 500 trees along a river to stop soil from washing into the water.", True, "Yes. The trees protect the river and the soil.", "Look again. Do the trees protect the river, or harm it?"),
  sort_item(2, "A company dumps old chemicals into a nearby wetland to save money.", False, "Right. Dumping chemicals is pollution. It harms the wetland.", "Look again. Does dumping chemicals protect the wetland, or harm it?"),
  sort_item(3, "Scientists set up a slow-speed boat zone in a Florida bay where manatees live.", True, "Yes. Slow boats are less likely to hurt manatees.", "Look again. Does a slow zone protect manatees, or harm them?"),
  sort_item(4, "A family fixes a leaky faucet and turns off sprinklers when it rains.", True, "Yes. Using less water saves a natural resource.", "Look again. Does saving water protect a natural resource?"),
  {"n": 5, "q": "Pick one action from above. In one sentence, tell why it is or isn't a conservation action.", "type": "text", "min": 8, "chips": [["because", "Gives a reason (because, so)"]]}
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "What is a natural resource? Give two examples and explain why they need to be protected.", "type": "text", "min": 12, "chips": [["resource", "Names two natural resources"], ["because", "Gives a reason (because, so)"]]},
    {"n": 2, "q": "Why is it important for scientists to collect evidence before claiming that a conservation solution will work?", "type": "text", "min": 12, "chips": [["evidence", "Uses the word evidence"], ["because", "Gives a reason (because, so)"]]}
  ]},
  "write": {"title": "What conservation solution would you argue for?", "do": "Think of a natural place near you. Answer the three questions. Use at least two of the science words under the boxes.",
    "vocab": ["conservation", "habitat", "natural resource", "pollution", "protect", "reduce"], "need": 2,
    "prompts": [["What do you think?", "Start with: \"I think the best conservation solution for this place would be…\""],
                ["What did you learn that supports your thinking?", "Start with: \"I know this would help because the lesson showed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because…\""]]},
  "partC": {"do": "Draw one habitat twice: damaged on the left, and helped by conservation on the right. Label what changed.",
            "labels": ["What changed in the habitat", "What conservation made possible"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 cases and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all five answers.", "req": {"choice": ["a1", "a2", "a3", "a4"], "text": {"in-a5": 8}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least two science words.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 2}}
  ]
}

premiere = {"title": "Premiere my comeback story", "thinkLabel": "The problem was", "director": "JUNIOR CONSERVATION SCIENTIST", "storyKicker": "My comeback story",
  "frames": [
    {"k": "formation", "label": "The eagle comeback", "img": "o4", "cap": "The eagle comeback: DDT thinned the eggs, people banned it, and eagles came back."},
    {"k": "compare", "label": "The Dune Test", "img": "ta", "cap": "The Dune Test: sea oat roots hold a dune in place."},
    {"k": "wall", "label": "The Eagle Tree", "img": "l4", "cap": "The Eagle Tree: one protected forest is home to many animals."},
    {"k": "det", "label": "Comeback cases", "img": "d1", "cap": "Comeback cases: real Florida animals, and the solutions that helped."}]}

nxt = {"title": "24.02 · How Can We Practice Conservation?", "text": "Next time, sort real conservation actions, from saving water to protecting habitats, and decide which ones help the most."}

chips = {
  "part": {"any": ["scar", "scars", "stripe", "stripes", "mark", "marks", "flipper", "flippers", "snout", "nose", "whiskers", "skin", "tail", "spots", "spotted", "water", "sunlight", "light", "back", "gray", "grey", "manatee"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["turtle", "hatchling", "sand", "pelican", "wings", "stork", "white", "alligator", "gator", "jay", "blue", "beach", "lights", "buildings", "eggs", "wetlands", "skins", "scrub", "bird", "feathers"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "problem": {"any": ["habitat", "loss", "lost", "cleared", "drained", "pollution", "poison", "ddt", "hunting", "hunted", "killed", "lights", "buildings"]},
  "resource": {"any": ["water", "soil", "air", "trees", "tree", "wood", "food", "fish", "plants", "land", "sunlight", "oil", "rocks", "sand"]},
  "evidence": {"any": ["evidence", "data", "count", "counts", "measure", "proof", "test", "tests"]}
}

L = {"id": "g3sci-24-01", "lesson": "24.01", "title": "What Is Conservation?", "emoji": "🌿",
  "details": ["📅 Q3 · Unit 8 · Human Impact &amp; Conservation", "📖 Week 24 · Lesson 24.01", "🌎 CPALMS SC.3.N.1.7 · NGSS 3-LS4-4", "⏱ About 35 minutes"],
  "icans": ["explain what conservation means and why people do it.", "describe ways people protect habitats and natural resources.", "give an example of a conservation solution and explain why it helps using evidence."],
  "opti": {"warm": "Our film starts at dawn with two bald eagles. First, inspect a manatee with some strange marks on its back.",
           "lesson": "Today you're a conservation scientist. Watch eagles come back, test two dunes, then climb a tree full of life.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Sort some real actions, then tell us how you'd protect a place you know."},
  "film": film, "scientist": "conservation scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Edward Elgar, <i>Pomp and Circumstance</i> March No. 1 (trio), played by \"The President's Own\" United States Marine Band, public domain (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The film tells the bald eagle's comeback with real photos from different places. The eagle movie, the Dune Test, and the Eagle Tree are models; every place photo is real."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-24-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the manatee, then tap three things you notice."},
  "how-24-01-compare": {"page": "Put the water under one tray and the fan under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the water under one tray and the fan under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-24-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-24-01-det": {"page": det["do"], "say": "Pick three cases, one at a time. Tap a clue, then pick the problem. Predict the solution that helped, and watch the place today appear."},
  "how-24-01-write": {"page": assign["write"]["do"], "say": "Think of a natural place near you. Answer the three questions. Use at least two of the science words under the boxes."},
  "how-24-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"24-01-welcome": L["opti"]["warm"], "24-01-lesson": L["opti"]["lesson"], "24-01-check": L["opti"]["check"], "24-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
