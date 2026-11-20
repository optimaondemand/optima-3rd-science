#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/29-01/lesson.json, how-lines.json, scripts.json, credits.json (29.01: no voices recorded; scripts only)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "Why can some animals thrive in the Everglades while others cannot survive there at all?"

film = {
  "id": "g3sci-29-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 29.01 · What Makes the Everglades Special?",
  "title": "Grass on Water",
  "bigQuestion": BQ,
  "poster": "f_prairie", "endPoster": "f_sunset", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    ph(3.4, 6.2, "f_prairie", "Tall sawgrass and a winding stream under a blue sky, with trees far away", "Everglades National Park, Florida",
       frm=(1.7, .5, .8), to=(1.0, .5, .5), fade=1.0, sfxAt=[{"at": 0.6, "name": "whoosh"}]),
    {"t": 9.6, "d": 5.8, "type": "reveal", "img": "f_water", "alt": "Sawgrass growing up out of shallow, shining water",
     "from": [1.0, .5, .5], "to": [1.08, .5, .55], "revealAt": 0.6, "revealDur": 4.2, "place": "Shark River Slough · Everglades National Park", "fade": 0.6,
     "cover": ["#b7a45e", "#8f7f3e"], "chip": "196,178,104"},
    {"t": 15.4, "d": 3.0, "type": "flash", "lines": ["A river?", "Of grass?"], "beats": [0.15, 1.2], "fade": 0.15},
    ph(18.4, 6.0, "f_river", "A wide marsh of grass and shining water at sunset, with one bare cypress tree", "The river of grass · Everglades National Park",
       frm=(1.0, .5, .5), to=(1.12, .6, .5), fx=["sweep"]),
    ph(24.4, 5.6, "f_spoon", "A pink roseate spoonbill sweeping its flat bill through shallow water", "A roseate spoonbill · Everglades National Park",
       frm=(1.0, .5, .5), to=(1.06, .5, .5), contain=True),
    ph(30.0, 5.6, "f_gator", "An alligator swimming with only its head above the water, among lily pads", "An alligator near the Anhinga Trail · Everglades National Park",
       frm=(1.12, .4, .55), to=(1.0, .5, .5), sfxAt=[{"at": 0.4, "name": "bubbles"}]),
    ph(35.6, 7.0, "f_sunset", "The sun setting over a flat marsh of sawgrass, with a line of trees far away", "Everglades National Park · Sunset",
       frm=(1.0, .5, .5), to=(1.08, .5, .5), fade=0.9),
    {"t": 42.6, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.4, "text": "South Florida. A sea of grass, as far as you can see.", "voice": "opti-1"},
    {"t": 10.0, "d": 5.0, "text": "But look closer. Under the grass, there's water.", "voice": "opti-2"},
    {"t": 15.5, "d": 2.8, "text": "A river? Of grass?", "voice": "opti-3"},
    {"t": 18.8, "d": 5.2, "text": "The water flows south, slowly, only inches deep.", "voice": "opti-4"},
    {"t": 24.8, "d": 4.8, "text": "Spoonbills sweep the shallow water for food.", "voice": "opti-5"},
    {"t": 30.4, "d": 4.8, "text": "Alligators wait in the warm water.", "voice": "opti-6"},
    {"t": 36.0, "d": 6.2, "text": BQ, "voice": "opti-7"}
  ]
}

specimen = {
  "img": "spec", "aspect": "3/4", "radius": 0.07,
  "hotspots": [
    {"name": "Tiny brown flowers", "x": 0.47, "y": 0.13},
    {"name": "Thin, branching stems", "x": 0.26, "y": 0.36},
    {"name": "One tall center stalk", "x": 0.34, "y": 0.62},
    {"name": "A long, thin leaf", "x": 0.86, "y": 0.52},
    {"name": "Seeds getting ready", "x": 0.66, "y": 0.83}
  ],
  "kicker": "🔎 Mystery specimen", "title": "What is this golden plant?",
  "alt": "A tall plant with thin green stems and hundreds of tiny golden-brown flowers, against a blurry green background",
  "look": "A close-up photo of one real plant, taller than a grown-up. Look at its parts: the tiny brown flowers, the stems, and the long leaves. A specimen is one real thing that scientists study. It grows by the millions in one Florida place. What is it? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the plant, then tap 3 things you notice.",
  "number": "No. 29.01-A",
  "card": ["<b>Specimen A</b>", "Found: on the Pa-hay-okee Trail, Everglades National Park", "Grows in: shallow water", "What is it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["💧", "wetland", "A place where water covers or soaks the soil much of the year. Special plants and animals live here."],
  ["🌾", "sawgrass", "A tall plant with sharp, saw-toothed edges that grows in thick mats across the Everglades' shallow water."],
  ["🏠", "habitat", "The place where a living thing lives and finds food, water, and shelter to survive."],
  ["🔄", "ecosystem", "All the living things in an area, and the water, air, and soil they all depend on."],
  ["🌊", "water flow", "The slow movement of water across flat land, like a shallow river hidden in a field of grass."],
  ["🎯", "adapted", "Having features that help a living thing survive in its home, like webbed feet for swimming."],
  ["📅", "season", "A part of the year with its own weather. South Florida has a wet season in summer and a dry season in winter."]
]

parts = [
  {"kicker": "🌱 Part 1", "title": "A River of Grass",
   "html": "<p>The Everglades isn't a lake or a pond. Scientists call it a river of grass. Water moves slowly south through miles of sawgrass, just a few inches deep. The land is almost flat and almost always wet, so it is a wetland.</p><p>South Florida has two seasons. In the wet season, summer storms fill the marsh. In the dry season, the water shrinks, and animals change what they do.</p>"},
  {"kicker": "🌤 Part 2", "title": "Who Fits In Here?",
   "html": "<p>Animals adapted to warm, shallow water live here. Alligators wait in pools. Herons and spoonbills catch fish. They fit this habitat like a key in a lock.</p><p>Not every animal fits. A polar bear, built for ice and freezing cold, could not survive here.</p>"},
  {"kicker": "🌍 Part 3", "title": "Water, Floods, and Protection",
   "html": "<p>When big storms hit South Florida, the Everglades soaks up rain like a giant sponge. That slows flooding and protects nearby farms and cities.</p><p>Engineers are working on the largest wetland restoration in the United States, so the water can flow south again.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Fit or Not? Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the summer storms.",
  "kicker": "🎞️ Put the scenes in order", "title": "What happens in the Everglades in one year?",
  "look": "Four real photos show one year in the Everglades, from the rainy summer to the dry spring. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "A dark storm cloud pouring rain over a wide marsh of sawgrass", "text": "Summer storms bring heavy rain to the marsh.", "play": "Summer rains.",
     "miss": ["", "The year starts with the summer rains. Try frame 1.", "The year starts with the summer rains. Try frame 1.", "The year starts with the summer rains. Try frame 1."]},
    {"img": "o2", "alt": "Sawgrass and small trees standing in wide, shallow water", "text": "Water spreads across the sawgrass. Fish spread out too.", "play": "Water everywhere.",
     "miss": ["The rain has to fall first. Try a later frame.", "", "The water spreads before it shrinks. Try an earlier frame.", "The water spreads before it shrinks. Try an earlier frame."]},
    {"img": "o3", "alt": "An alligator lying beside a small pond of water, with lily pads and grass around it", "text": "In the dry season, the water shrinks. An alligator's pond still holds water.", "play": "The water shrinks.",
     "miss": ["The marsh has to fill before it can dry. Try a later frame.", "The marsh has to fill before it can dry. Try a later frame.", "", "The water shrinks before the birds gather. Try an earlier frame."]},
    {"img": "o4", "alt": "Wood storks and pink spoonbills gathered in the bushes at the edge of a pond", "text": "Fish crowd into the last pools. Wading birds feast and raise their chicks.", "play": "Birds feast.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Max says, \"The Everglades is just a still swamp. The water never moves.\" What do you think?",
    "options": [
      {"t": "Max is right. The water just sits there.", "miss": "Look at the movie again. Does the water stay the same all year?"},
      {"t": "The water flows slowly south, and it rises and shrinks with the seasons.", "ok": "Yes! It's a slow river, only inches deep, and it changes with the wet and dry seasons."}
    ]
  }
}

movie = {
  "model": "glades-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🌦️",
  "real": "real", "realAlt": "A wood stork standing over its fluffy white chicks in a nest of sticks",
  "stamp": "NESTING TIME!", "endCap": "Real wood storks and chicks.",
  "beats": [
    {"at": 0, "cap": "1 · Summer rains.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["June"], "sfx": "bubbles"},
    {"at": 2600, "cap": "2 · Water everywhere.", "model": {"show": "s2"}, "counter": ["September"]},
    {"at": 5200, "cap": "3 · The water shrinks.", "model": {"show": "s3"}, "counter": ["February"]},
    {"at": 7800, "cap": "4 · Birds feast.", "model": {"show": "s4"}, "counter": ["April"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Fit Test", "title": "Which home fits which body?",
  "look": "Two real animals, each on a lit tray. Specimen A is an American alligator. Specimen B is a polar bear. Under the trays are two model homes: a tub of warm, shallow water, and a block of sea ice.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "An American alligator walking on green grass", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A polar bear on the edge of sea ice, looking into blue water", "label": "Specimen B"}
  ],
  "materials": [{"key": "water", "label": "Tub of warm, shallow water", "swatch": "water"}, {"key": "ice", "label": "Block of sea ice", "swatch": "ice"}],
  "ask": [
    {"q": "Which animal has scaly skin and a long tail?", "ans": "A", "ok": "Yes. Specimen A is the alligator, covered in tough scales.", "miss": "Look closely. Which one has scales?"},
    {"q": "Which animal has thick white fur?", "ans": "B", "ok": "Yes. Specimen B is the polar bear, with thick fur.", "miss": "Look again. Which one is furry?"}
  ],
  "press": "🎯 Run the test",
  "testDo": "Put the warm water under one tray and the sea ice under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. No real animals are tested.",
  "results": {
    "Awater": {"text": "The alligator slides in and floats with just its eyes and nose above the water. This home fits its body!", "fx": "float"},
    "Aice": {"text": "The alligator gets cold and very slow. Its body warms up from the air and water around it, so ice is no home for it.", "fx": "frost"},
    "Bwater": {"text": "The polar bear pants and looks for shade. Its thick fur and fat are made for freezing cold, so warm water is far too hot.", "fx": "warm"},
    "Bice": {"text": "The polar bear walks out onto the ice, right at home. Its thick fur and fat keep it warm.", "fx": "none"}
  },
  "best": ["Awater", "Bice"],
  "frame": "This animal's body is built for ___, so it fits ___.", "claimLead": "This animal's body is built for", "claimMid": "so it fits",
  "claim": {
    "A": {"feat": ["warm, shallow water", "ice and freezing cold"], "featOk": 0, "eat": ["the Everglades", "the Arctic"], "eatOk": 0},
    "B": {"feat": ["warm, shallow water", "ice and freezing cold"], "featOk": 1, "eat": ["the Everglades", "the Arctic"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Built for warm water.</b> An alligator's eyes and nose sit on top of its head, so it can hide in the water and still see and breathe.",
    "B": "<b>Built for ice.</b> A polar bear's thick fur and fat hold in heat. In Florida's heat, that same coat would make it far too hot."
  },
  "missFeat": "Look at your tests for {label} again. Which home made it comfortable?",
  "missClaim": "Think about your tests. Which place has that kind of home?",
  "done": "An animal survives where its body fits the habitat. The alligator fits warm, shallow water. The polar bear fits ice and cold.",
  "after": {"kicker": "🎬 Behind the scenes · A road becomes a bridge", "img": "after", "alt": "Workers and machines building a bridge beside a canal at the edge of the Everglades",
            "html": "For many years, a road called the Tamiami Trail blocked water flowing south into the Everglades. Workers are raising parts of it onto bridges, so the water can pass underneath. The first one-mile bridge opened in 2013."}
}

wall = {
  "kicker": "🥾 The Glades Walk", "title": "Walk south from high ground to the salty sea",
  "look": "A model trail with four stops, from a tree island on higher ground down to the coast. Each stop has a real photo from Everglades National Park. The brass dial on the left shows where you are.",
  "do": "First, make a prediction. Then brush the glowing step: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "Is the Everglades the same everywhere, or does it change as you walk south?",
              "options": [["changes", "It changes from place to place"], ["same", "It's the same grass everywhere"]], "answer": "changes",
              "mine": "Your prediction: <b>{p}</b>. Let's walk and find out.",
              "confirm": "You predicted it changes. You were right: each stop has its own water and its own living things.",
              "change": "You predicted it's the same everywhere. The walk changed that idea: each stop has its own water and its own living things."},
  "sky": "sky", "skyAlt": "The sun setting over a flat marsh of sawgrass", "skyCap": "Sunset over the sawgrass · Everglades National Park",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Walk", "Tree island", "Sawgrass", "Slough", "Mangroves"],
  "line": ["HIGHER, DRIER GROUND", "SALTY SEA"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We go one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Keep going. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the walk. The Everglades isn't the same everywhere. Each stop has its own water, and its own plants and animals.",
  "rule": "<b>Each zone is a different habitat.</b> Small changes in height, water depth, and salt decide which plants and animals can live there.",
  "choices": ["🌳 Trees on drier ground", "🌾 Sawgrass in shallow water", "🐢 Deeper, slow-moving water", "🦀 Salty water at the coast"],
  "layers": [
    {"name": "Stop 1 · Tree island", "rock": "leafshade", "img": "l1", "alt": "A rounded clump of trees rising out of a flat sea of sawgrass",
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "A tree island sits a little higher than the marsh, so its soil stays dry enough for trees. Deer, snakes, and birds rest and nest here.",
     "ans": 0, "ok": "Yes! Trees grow on the higher, drier ground of a tree island.", "tag": "🌳 Tree island · drier ground",
     "miss": {"1": "Look at the photo. What grows on the island?", "2": "Not yet. Is this deep water?", "3": "Not yet. Is this the salty coast?"},
     "env": "e1", "envAlt": "A boardwalk winding under palms and tall trees", "envCap": "Inside a tree island: Mahogany Hammock · Everglades National Park"},
    {"name": "Stop 2 · Sawgrass prairie", "rock": "leafsun", "img": "l2", "alt": "A flat, golden prairie of sawgrass under a sky full of white clouds",
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "Miles of sawgrass grow in water only a few inches deep. Frogs, insects, and small fish hide among the stalks.",
     "ans": 1, "ok": "Yes! Sawgrass grows in shallow water across most of the Everglades.", "tag": "🌾 Sawgrass · shallow water",
     "miss": {"0": "Look again. Are there trees here?", "2": "Close! There is water, but read the clue: how deep is it?", "3": "Not yet. Is this the salty coast?"},
     "env": "e2", "envAlt": "Sawgrass and small, thin cypress trees under white clouds", "envCap": "Pa-hay-okee: sawgrass as far as you can see · Everglades National Park"},
    {"name": "Stop 3 · Slough", "rock": "water1", "img": "l3", "alt": "Shallow water winding through a marsh of grass and small trees",
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "A slough (say \"slew\") is a deeper channel where water flows slowly south. Fish, turtles, and alligators stay here, even in the dry season.",
     "ans": 2, "ok": "Yes! A slough holds deeper water that flows slowly south.", "tag": "🐢 Slough · deeper water",
     "miss": {"0": "Not this one. Is this a dry island?", "1": "Close! Read the clue: is this water deeper than the sawgrass marsh?", "3": "Not yet. Is the water salty here?"},
     "env": "e3", "envAlt": "A wooden boardwalk crossing a green marsh under a bright sun", "envCap": "The Anhinga Trail crosses Taylor Slough · Everglades National Park"},
    {"name": "Stop 4 · Mangrove coast", "rock": "gulf", "img": "l4", "alt": "Red mangrove trees with tangled roots standing in brown water",
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "At the coast, fresh water meets the salty sea. Mangrove trees can live in salty water. Their tangled roots shelter baby fish.",
     "ans": 3, "ok": "Yes! Mangroves grow where fresh water meets the salty sea.", "tag": "🦀 Mangroves · salty coast",
     "miss": {"0": "Look again. Is this dry ground?", "1": "Not quite. Is this sawgrass?", "2": "Close! Read the clue: what's special about this water?"},
     "env": "e4", "envAlt": "Small mangrove trees standing in shining water under a golden sky", "envCap": "Mangroves where the river of grass meets the coast · Everglades National Park"}
  ],
  "mix": {
    "q": "Ava says, \"If a polar bear moved to the Everglades, it would just get used to the heat.\" What do you think?",
    "options": [
      {"t": "Ava is right. Any animal can get used to any place.", "miss": "Think about the Fit Test. What is a polar bear's body built for?"},
      {"t": "No. Its body is built for ice and cold, so it could not survive the Everglades heat.", "ok": "Yes! An animal can't just change its body to fit a new place. It survives where its features match the habitat."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Alligators and Crocodiles, Side by Side",
  "img": "wow", "alt": "A big gray crocodile resting on a muddy bank among mangrove roots",
  "caption": "An American crocodile near Flamingo, Everglades National Park",
  "html": "<p style=\"margin:0 0 8px\">The Everglades is the only place in the world where alligators and crocodiles live side by side.</p><p style=\"margin:0\">Alligators like fresh water. Crocodiles like the salty edges of the coast. The Everglades has both, so it has both!</p>",
  "inset": "inset", "insetCap": "An American alligator swimming · Everglades National Park."}

keyIdea = "Whether an animal survives in the Everglades depends on how well it fits the warm, wet, flat habitat. Animals that need dry ground or freezing cold struggle, while animals adapted to shallow water thrive. The water rises in the wet season and shrinks in the dry season, and animals change what they do. The same water soaks up storm rain like a giant sponge, slowing floods."

M = ["💧 Warm water", "🌳 Dry forest ground", "🧊 Ice and freezing cold"]
SHORT = ["warm water", "dry forest ground", "ice and freezing cold"]
SOL = [["well", "✅ Survives well"], ["less", "🤏 Survives less well"], ["not", "🚫 Cannot survive"]]


def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}


det = {
  "look": "Five real animals. Each card shows what scientists saw. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap a clue, then name what the animal needs. Predict how well it survives in the Everglades, and watch its home appear.",
  "noun": "Card", "need": 3, "inferQ": "What does it need?", "inferDone": "It needs", "chartSo": "so it",
  "predict": {"q": "How well do you predict it survives in the Everglades?", "options": SOL},
  "kicker": "Its real home", "enough": "You already solved 3 animal cards. Nice work, scientist!",
  "cols": ["Card", "My observation", "What it needs", "In the Everglades", "My evidence"],
  "write": {"label": "Card __ shows ___. It ___ in the Everglades, because ___.", "starter": "Start with: \"Card __ shows…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["need", "Names what it needs"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "An alligator swimming low in dark water, with only its back and head showing",
         [{"t": "A big reptile with tough, scaly skin", "ok": True}, {"t": "Thick white fur", "miss": "Look again. Does it have fur?"}, {"t": "A pink, spoon-shaped bill", "miss": "Look again. Does it have a bill?"}],
         0, "Alligators hunt fish and turtles in warm, shallow water. Which choice is that? Try again.",
         "well", "Warm, shallow water is everywhere in the Everglades. How well would it survive? Try again.",
         "d1h", "A clump of trees rising out of a flat sea of sawgrass", "Pa-hay-okee, Everglades National Park",
         "Alligators live all across the Everglades, in sloughs, marshes, and the ponds they keep open in the dry season.", "glades",
         "Many other animals use an alligator's pond when the dry season comes."),
    card("B", "d2", "A pink roseate spoonbill flying across a blue sky",
         [{"t": "A pink bird with a flat, spoon-shaped bill", "ok": True}, {"t": "Scaly skin", "miss": "Look again. Is it covered in scales?"}, {"t": "Black fur", "miss": "Look again. Does it have fur?"}],
         0, "A spoonbill sweeps its bill through shallow water for tiny fish. Which choice is that? Try again.",
         "well", "Shallow water full of tiny fish is exactly what the Everglades has. How well would it survive? Try again.",
         "d2h", "Small green islands in bright blue-green water, seen from the air", "North Nest Key, Florida Bay · Everglades National Park",
         "Roseate spoonbills feed in shallow Everglades water and nest on small mangrove islands in Florida Bay.", "bay",
         "Spoonbills are pink because of the colors in the tiny shrimp and fish they eat."),
    card("C", "d3", "A Florida black bear standing among palmetto plants in a pine forest",
         [{"t": "A big animal with black fur and a long snout", "ok": True}, {"t": "A spoon-shaped bill", "miss": "Look again. Does it have a bill?"}, {"t": "Tough scales", "miss": "Look again. Is it scaly?"}],
         1, "Black bears travel, find berries, and make dens on dry forest ground. Which choice is that? Try again.",
         "less", "Most of the Everglades is wet, but there are some drier edges and tree islands. How well would it survive? Try again.",
         "d3h", "Cypress trees and plants standing in dark water", "Big Cypress National Preserve, next to the Everglades",
         "Florida black bears live near the Everglades, in places like Big Cypress, where there is more dry ground. In the wet marsh, they use only drier edges and tree islands.", "bigcyp",
         "A black bear can live near the Everglades, but not out in the wide, wet sawgrass."),
    card("D", "d4", "A polar bear on the edge of sea ice, looking into blue water",
         [{"t": "Thick white fur on a big body", "ok": True}, {"t": "A spoon-shaped bill", "miss": "Look again. Does it have a bill?"}, {"t": "Tough scales", "miss": "Look again. Is it scaly?"}],
         2, "A polar bear hunts seals from the sea ice. Which choice is that? Try again.",
         "not", "The Everglades has no ice at all, and it's warm all year. How well would it survive? Try again.",
         "d4h", "Wide, rough sea ice under a pale sky", "Sea ice at the North Pole · April 1990",
         "Polar bears hunt seals from sea ice in the Arctic. Their thick fur and fat are made for freezing cold, so the Everglades would be far too hot.", "arctic",
         "Polar bears need sea ice to hunt, and the Everglades has none."),
    card("E", "d5", "A crocodile with a long, narrow snout and pointed teeth, resting at the edge of a road",
         [{"t": "A long, narrow snout with teeth showing", "ok": True}, {"t": "Thick white fur", "miss": "Look again. Does it have fur?"}, {"t": "A pink bill", "miss": "Look again. Does it have a bill?"}],
         0, "Crocodiles live in warm water along the coast. Which choice is that? Try again.",
         "well", "The Everglades coast has warm, salty water and mangroves. How well would it survive? Try again.",
         "d5h", "Green mangrove islands and winding water, seen from the air", "Mangrove backcountry near Hells Bay · Everglades National Park",
         "American crocodiles live in the warm, salty water along the Everglades coast. Park scientists count their nests near Flamingo each year.", "coast",
         "This crocodile was photographed during a nest survey by park scientists.")
  ]
}

rebuild = {"title": "Use your evidence to rebuild the scene", "missPrefix": "Hmm. Look at your animal card again. ", "kicker": "🌍 Rebuild the scene", "whyStart": "I chose this because the animal needs…",
  "envs": [
    {"key": "glades", "name": "🌾 The sawgrass marsh", "img": "d1h", "cap": "Warm, shallow water…"},
    {"key": "bay", "name": "🏝️ Florida Bay islands", "img": "d2h", "cap": "Mangrove islands…"},
    {"key": "bigcyp", "name": "🌲 Big Cypress", "img": "d3h", "cap": "Drier edges…"},
    {"key": "arctic", "name": "🧊 The Arctic", "img": "d4h", "cap": "Ice and freezing cold…"},
    {"key": "coast", "name": "🌊 The salty coast", "img": "d5h", "cap": "Mangroves and salt water…"}
  ],
  "life": [
    {"name": "🐊 An alligator", "img": "d1", "env": "glades", "miss": "The alligator belongs in the sawgrass marsh."},
    {"name": "🦩 A spoonbill", "img": "d2", "env": "bay", "miss": "The spoonbill nests on the Florida Bay islands."},
    {"name": "🐻 A black bear", "img": "d3", "env": "bigcyp", "miss": "The black bear belongs in Big Cypress."},
    {"name": "🐻‍❄️ A polar bear", "img": "d4", "env": "arctic", "miss": "The polar bear belongs in the Arctic."},
    {"name": "🐊 A crocodile", "img": "d5", "env": "coast", "miss": "The crocodile belongs on the salty coast."}
  ]}

quiz = [
  {"q": "What do scientists call the Everglades because water moves slowly through a vast field of grass?", "options": [
    {"t": "A frozen tundra", "miss": "Think about how water moves through the Everglades, slowly south through thick sawgrass. Scientists gave this a special name describing what they saw."},
    {"t": "A river of grass", "ok": "🌲 That's right! The Everglades is called a \"river of grass\": water flows slowly south through miles of sawgrass, just inches deep."},
    {"t": "A saltwater marsh", "miss": "Think about how water moves through the Everglades, slowly south through thick sawgrass. Scientists gave this a special name describing what they saw."}]},
  {"q": "An animal that needs dry land, cool temperatures, and thick forest would most likely _____ in the Everglades.", "options": [
    {"t": "Thrive and become the top predator", "miss": "Think about what the Everglades is like: warm, wet, and mostly grass and water. Does that match what this animal needs?"},
    {"t": "Adapt quickly and do fine", "miss": "Think about what the Everglades is like: warm, wet, and mostly grass and water. Does that match what this animal needs?"},
    {"t": "Struggle to survive because the habitat doesn't match its needs", "ok": "🌲 Exactly! The Everglades is warm, flat, and wet. An animal that needs dry, cool, forested land won't find a matching habitat here."}]},
  {"q": "How does the Everglades help protect nearby communities when big storms bring heavy rain?", "options": [
    {"t": "It absorbs water like a giant sponge, slowing down flooding", "ok": "⭐ Yes! The Everglades soaks up huge amounts of rainwater, slowing floods and protecting farms and cities nearby."},
    {"t": "It creates strong winds that push storms away from cities", "miss": "Remember: the Everglades acts a lot like a sponge. What does a sponge do when you pour water on it?"},
    {"t": "It freezes the rain before it reaches the ground", "miss": "Remember: the Everglades acts a lot like a sponge. What does a sponge do when you pour water on it?"}]}
]

CH = ["Survives well", "Survives less well", "Cannot survive"]


def sortq(n, q, ans, ok, miss):
    return {"n": n, "q": q, "type": "choice", "options": [{"t": c, "ok": ok} if i == ans else {"t": c, "miss": miss} for i, c in enumerate(CH)]}


partA = {"title": "Sort and identify", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  sortq(1, "An alligator that loves warm, shallow, slow-moving fresh water and can hold its breath underwater for a long time.", 0,
        "Yes. Warm, shallow water is exactly what the Everglades has.", "Think about what the Everglades has: warm, shallow water. Does that fit this animal?"),
  sortq(2, "A black bear that needs dry forest ground, berries, and places to den and raise cubs.", 1,
        "Yes. It can live at the drier edges, like Big Cypress, but not out in the wet sawgrass.", "The Everglades is mostly wet, with only a few drier edges and tree islands. How well would it do?"),
  sortq(3, "A roseate spoonbill that catches tiny fish by sweeping its bill through warm, shallow water.", 0,
        "Yes. Its bill is built for the Everglades' shallow water.", "Where does it find its food? Does the Everglades have that?"),
  sortq(4, "A polar bear that needs sea ice and freezing temperatures to hunt and stay cool.", 2,
        "Yes. The Everglades has no ice and is warm all year.", "Does the Everglades have any sea ice or freezing cold?")
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Name two features of the Everglades that make it a unique habitat. Why does each one matter for the animals that live there?", "type": "text", "min": 12, "chips": [["feat", "Names a feature"], ["because", "Says why it matters (because, so)"]]},
    {"n": 2, "q": "Why does it matter that water flows slowly through the Everglades, rather than drying up completely? What would change for the animals?", "type": "text", "min": 12, "chips": [["water", "Talks about the water"], ["animal", "Says what changes for animals"]]}
  ]},
  "write": {"title": BQ.replace("thrive in", "survive well in") + " Use evidence from your investigation.", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["habitat", "adapted", "ecosystem"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think that some animals survive in the Everglades because…\""],
                ["What did you learn that supports your thinking?", "Start with: \"I know this because the lesson showed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because…\""]]},
  "partC": {"do": "Draw one animal that survives well in the Everglades, in its Everglades home. Show the water and plants around it. Then write two labels.",
            "labels": ["One feature of the animal that helps it survive here", "One thing in the Everglades it needs"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 animal cards and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all four animals sorted.", "req": {"choice": ["a1", "a2", "a3", "a4"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my Everglades story", "thinkLabel": "What the animal needs", "director": "JUNIOR WETLAND SCIENTIST", "storyKicker": "My Everglades story",
  "frames": [
    {"k": "formation", "label": "A year in the Glades", "img": "o2", "cap": "A year in the Glades: rains, water, dry season, birds."},
    {"k": "compare", "label": "The Fit Test", "img": "ta", "cap": "The Fit Test: each body fits its own home."},
    {"k": "wall", "label": "The Glades Walk", "img": "l2", "cap": "The Glades Walk: tree island, sawgrass, slough, mangroves."},
    {"k": "det", "label": "Fit or not?", "img": "d2", "cap": "Fit or not? Who survives in the Everglades."}]}

nxt = {"title": "Coming up next: 29.02", "text": "Investigation: Everglades Food Web. Next time, build a food web and follow the energy from sawgrass to alligators."}

chips = {
  "part": {"any": ["flower", "flowers", "brown", "golden", "gold", "orange", "tiny", "stem", "stems", "branch", "branches", "branching", "stalk", "leaf", "leaves", "long", "thin", "seed", "seeds", "green", "tall", "grass", "plant"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["scales", "scaly", "fur", "furry", "white", "black", "pink", "bill", "spoon", "snout", "teeth", "tail", "reptile", "bird", "bear", "big", "skin", "alligator", "crocodile", "spoonbill", "polar"]},
  "need": {"any": ["water", "warm", "shallow", "ice", "cold", "freezing", "dry", "forest", "ground", "salty", "fish", "needs", "need"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "feat": {"any": ["water", "warm", "flat", "wet", "shallow", "sawgrass", "grass", "wetland", "slow", "flows", "flow", "seasons", "season"]},
  "water": {"any": ["water", "flow", "flows", "flowing", "dry", "drying", "wet"]},
  "animal": {"any": ["animal", "animals", "fish", "birds", "alligator", "alligators", "die", "survive", "food", "move", "leave"]}
}

L = {"id": "g3sci-29-01", "lesson": "29.01", "title": "What Makes the Everglades Special?", "emoji": "🐊",
  "details": ["📅 Q4 · Unit 10 · Florida Ecosystems", "📖 Week 29 · Lesson 29.01", "🌎 CPALMS SC.3.L.17.1", "⏱ About 35 minutes"],
  "icans": ["describe what makes the Everglades a unique habitat.", "use evidence to explain why some organisms survive in the Everglades and others cannot.", "make a claim about how the Everglades protects nearby communities from flooding."],
  "opti": {"warm": "Our film starts in a sea of grass in South Florida. First, inspect a golden plant that grows there by the millions.",
           "lesson": "Today you're a wetland scientist. Follow one year in the Everglades, test which homes fit which bodies, then walk the Glades to the sea.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Sort the animals, then draw one that fits right in."},
  "film": film, "scientist": "wetland scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Water Music, Suite No. 2, Alla hornpipe (George Frideric Handel), United States Marine Band Chamber Orchestra, public domain recording (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The year-in-the-Glades movie, the Fit Test, and the Glades Walk are models; every place photo is real. The Fit Test is a model: no animals are tested."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-29-01-compare": {"page": "Put the warm water under one tray and the sea ice under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the warm water under one tray and the sea ice under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-29-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-29-01-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap a clue, then name what the animal needs. Predict how well it survives in the Everglades, and watch its home appear."},
  "how-29-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"29-01-welcome": L["opti"]["warm"], "29-01-lesson": L["opti"]["lesson"], "29-01-check": L["opti"]["check"], "29-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
