#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/30-02/lesson.json, how-lines.json, scripts.json, credits.json (30.02: no voices recorded; scripts only).
Images come from prep.py (run it first)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "Could a small difference between two animals of the same kind change which one survives?"

film = {
  "id": "g3sci-30-02", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 30.02 · Investigation: Adaptation Comparison",
  "title": "Fire Day",
  "bigQuestion": BQ,
  "poster": "f_fire", "endPoster": "f_dune", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 3.0, "type": "black", "sfxAt": [{"at": 0.3, "name": "tick"}, {"at": 1.3, "name": "tick"}, {"at": 2.3, "name": "tick"}], "fade": 0.5},
    ph(6.4, 5.2, "f_smoke", "A tall plume of gray smoke rising over low, sandy scrub with saw palmettos", "A planned burn seen from Archbold Biological Station, Florida",
       frm=(1.0, .5, .5), to=(1.12, .55, .45), fade=1.0),
    ph(11.6, 5.2, "f_fire", "Orange flames and smoke sweeping through palmettos and bushes", "A planned burn · Merritt Island National Wildlife Refuge, Florida",
       frm=(1.15, .5, .55), to=(1.0, .5, .5), sfxAt=[{"at": 0.3, "name": "rumble"}]),
    ph(16.8, 5.6, "f_dig", "A gopher tortoise crawling toward the dark opening of its burrow in yellow sand", "A gopher tortoise at its burrow · Florida",
       frm=(1.0, .5, .5), to=(1.2, .4, .55)),
    ph(22.4, 5.0, "f_burnt", "Blackened ground and burned palm trunks after a fire", "After a planned burn · Florida Panther National Wildlife Refuge",
       frm=(1.08, .5, .5), to=(1.0, .5, .5), fade=0.9),
    ph(27.4, 5.2, "f_sprout", "The same pine forest later, full of new green plants", "The same spot, later · Florida Panther National Wildlife Refuge",
       frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=0.6, **{"in": "ripple"}),
    {"t": 32.6, "d": 8.4, "type": "split", "img": "f_pale", "alt": "A pale beach mouse with sandy fur and a white belly, sitting on white sand",
     "img2": "f_dark", "alt2": "A darker brown oldfield mouse in dry grass and dark soil",
     "splitAt": 2.6, "splitDur": 2.4, "lab1": "A beach mouse · white dunes", "lab2": "Same kind of mouse · inland fields",
     "from": [1.0, .5, .45], "to": [1.06, .5, .45], "fade": 0.6, "sfxAt": [{"at": 2.6, "name": "whoosh"}]},
    ph(41.0, 6.6, "f_dune", "Pale sand dunes with sea oats under a clear blue sky", "White sand dunes · Pensacola Beach, Florida",
       frm=(1.0, .5, .5), to=(1.08, .5, .5), fade=0.9),
    {"t": 47.6, "d": 5.6, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 6.8, "d": 4.6, "text": "Smoke rises over the Florida scrub.", "voice": "opti-1"},
    {"t": 12.0, "d": 4.6, "text": "Fire sweeps through here every few years.", "voice": "opti-2"},
    {"t": 17.2, "d": 5.0, "text": "A gopher tortoise heads down its burrow.", "voice": "opti-3"},
    {"t": 22.8, "d": 4.4, "text": "The fire passes. The ground turns black.", "voice": "opti-4"},
    {"t": 27.8, "d": 4.6, "text": "Soon, new green plants sprout.", "voice": "opti-5"},
    {"t": 33.0, "d": 7.6, "text": "Two mice of the same kind. One is pale. One is darker.", "voice": "opti-6"},
    {"t": 41.4, "d": 5.8, "text": BQ, "voice": "opti-7"}
  ]
}

specimen = {
  "img": "spec", "aspect": "3/2", "radius": 0.07,
  "hotspots": [
    {"name": "A tall, domed shell", "x": 0.50, "y": 0.13},
    {"name": "A blunt head with a hard beak", "x": 0.50, "y": 0.46},
    {"name": "A wide, flat front leg, shaped like a shovel", "x": 0.25, "y": 0.60},
    {"name": "Thick scales that protect the front legs", "x": 0.74, "y": 0.58},
    {"name": "The flat bottom shell under its chin", "x": 0.50, "y": 0.70}
  ],
  "kicker": "🔎 Mystery specimen", "title": "Who is hiding in this shell?",
  "alt": "A brown tortoise facing the camera with its head and wide, scaly front legs pulled close to its shell, on pale sand",
  "look": "A real Florida animal, photographed face to face. Look at its parts: the shell, the head, and the wide front legs. A specimen is one real thing that scientists study. What is it, and what could those front legs be for? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the animal, then tap 3 things you notice.",
  "number": "No. 30.02-A",
  "card": ["<b>Specimen A</b>", "Shell length: about 25 cm (10 inches)", "Found in: dry, sandy Florida land", "What are its legs for? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🔀", "variation", "A difference in a characteristic between individuals of the same species, like one mouse with paler fur than another."],
  ["🏆", "survival advantage", "When a variation makes one individual more likely to survive and have young than others of the same species."],
  ["🐭", "population", "A group of animals of the same kind living in the same area, like all the beach mice on one island."],
  ["🔍", "individual", "One single living thing in a population, with its own small differences."],
  ["🧬", "characteristic", "A feature of a living thing, like fur color, bill length, or claw size. It means the same as trait."],
  ["🐦", "behavior", "Something an animal does that helps it survive, like digging a burrow or keeping watch for hawks."]
]

parts = [
  {"kicker": "🔀 Part 1", "title": "Not Every Individual Is the Same",
   "html": "<p>In Lesson 30.01, you learned that adaptations help animals survive. Now look closely at a population of one kind of animal. No two individuals are exactly alike. One beach mouse is paler. One tortoise has wider front legs. These small differences are called variations.</p>"},
  {"kicker": "🏆 Part 2", "title": "When a Small Difference Matters",
   "html": "<p>Most variations don't change much. But some do. In Florida scrub, fires sweep through every few years. A tortoise that digs a deeper burrow stays cooler underground, so its variation is a survival advantage.</p><p>Survivors have young, and the young can inherit the helpful characteristic. Scientists think this is how, over many generations, a whole population changes.</p>"},
  {"kicker": "🔬 Part 3", "title": "Evidence and Animal Groups",
   "html": "<p>Scientists use evidence: observations and measurements, like a mouse's fur color or how deep a burrow goes. They also sort animals into groups. Mammals have fur, and most give birth to live young. Birds have feathers and lay eggs. Reptiles have dry scales. Amphibians have smooth, wet skin. Fish have gills. All of these are vertebrates, animals with a backbone. Insects have no backbone.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Variation Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the fire coming.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does a gopher tortoise survive a fire?",
  "look": "Four real photos show what happens on a fire day in Florida, from the first flames to the weeks after. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "f_fire", "alt": "Orange flames and smoke sweeping through palmettos and bushes", "text": "Fire moves through the scrub.", "play": "Fire comes.",
     "miss": ["", "The fire has to come first. Try frame 1.", "The fire has to come first. Try frame 1.", "The fire has to come first. Try frame 1."]},
    {"img": "f_dig", "alt": "A gopher tortoise crawling toward the opening of its burrow", "text": "The tortoise goes deep in its burrow.", "play": "It goes deep.",
     "miss": ["The fire comes first. Try a later frame.", "", "It hides before the fire passes. Try an earlier frame.", "It hides before the fire passes. Try an earlier frame."]},
    {"img": "f_burnt", "alt": "Blackened ground and burned palm trunks", "text": "The fire passes over. The ground is black.", "play": "The fire passes.",
     "miss": ["The tortoise has to hide first. Try a later frame.", "The tortoise has to hide first. Try a later frame.", "", "The ground burns before plants grow back. Try an earlier frame."]},
    {"img": "f_sprout", "alt": "A pine forest full of new green plants", "text": "New plants sprout, and animals come back out.", "play": "Plants grow back.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Lena says, \"Variation is only about how an animal looks.\" What do you think?",
    "options": [
      {"t": "Lena is right. Variation means a different color or size.", "miss": "Think about the tortoise. Could two tortoises differ in how deep they dig?"},
      {"t": "Behaviors can vary too, like how deep a tortoise digs its burrow.", "ok": "Yes! A variation can be in a body part or in a behavior. A tortoise that digs deeper stays safer when fire comes."}
    ]
  }
}

movie = {
  "model": "burrow-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🔥",
  "real": "real", "realAlt": "A gopher tortoise resting on the pale sand mound in front of its burrow",
  "stamp": "SAFE UNDERGROUND!", "endCap": "A real gopher tortoise at its burrow.",
  "beats": [
    {"at": 0, "cap": "1 · Fire comes.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Hour 1"], "sfx": "whoosh"},
    {"at": 2600, "cap": "2 · It goes deep.", "model": {"show": "s2"}, "counter": ["Hour 2"]},
    {"at": 5200, "cap": "3 · The fire passes.", "model": {"show": "s3"}, "counter": ["Hour 3"]},
    {"at": 7800, "cap": "4 · Plants grow back.", "model": {"show": "s4"}, "counter": ["Weeks later"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Owl Test", "title": "Which mouse can an owl spot?",
  "look": "Two real mice of the same species, each on a lit tray. Specimen A is a pale beach mouse from the white dunes. Specimen B is a darker mouse of the same kind from inland fields. Under the trays are two model grounds: white dune sand, and dark field soil.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A pale beach mouse with sandy fur and a white belly on white sand", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A darker brown mouse in dry grass and dark soil", "label": "Specimen B"}
  ],
  "materials": [{"key": "sand", "label": "White dune sand", "img": "m_sand"}, {"key": "soil", "label": "Dark field soil", "swatch": "mud"}],
  "ask": [
    {"q": "Which mouse is pale, like white sand?", "ans": "A", "ok": "Yes. Specimen A is the pale beach mouse.", "miss": "Look closely. Which one is pale?"},
    {"q": "Which mouse is darker brown?", "ans": "B", "ok": "Yes. Specimen B is the darker mouse.", "miss": "Look again. Which one is darker?"}
  ],
  "press": "🦉 Run the test",
  "testDo": "Put the white sand under one tray and the dark soil under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. No real animals are tested.",
  "results": {
    "Asand": {"text": "The pale mouse almost disappears on the white sand! An owl would have a hard time.", "fx": "shade"},
    "Asoil": {"text": "The pale mouse stands out on the dark soil. An owl could spot it.", "fx": "glow"},
    "Bsand": {"text": "The darker mouse stands out on the white sand. An owl could spot it.", "fx": "glow"},
    "Bsoil": {"text": "The darker mouse almost vanishes on the dark soil!", "fx": "shade"}
  },
  "best": ["Asand", "Bsoil"],
  "frame": "This mouse's fur matches ___, so it is safer from owls in ___.", "claimLead": "This mouse's fur matches", "claimMid": "so it is safer from owls in",
  "claim": {
    "A": {"feat": ["white dune sand", "dark field soil"], "featOk": 0, "eat": ["the white beach dunes", "the darker inland fields"], "eatOk": 0},
    "B": {"feat": ["white dune sand", "dark field soil"], "featOk": 1, "eat": ["the white beach dunes", "the darker inland fields"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>A pale variation.</b> Beach mice on Florida's white dunes have pale fur. On white sand, a pale mouse is harder for an owl to see.",
    "B": "<b>A darker variation.</b> Mice of the same species that live inland on darker soil have darker fur. There, dark fur is harder to see."
  },
  "missFeat": "Look at your tests for {label} again. Where did it almost disappear?",
  "missClaim": "Think about your tests. Which place has that color of ground?",
  "done": "Same species, two variations. Each fur color is a survival advantage on its own kind of ground.",
  "after": {"kicker": "🎬 Behind the scenes · Fishing feet", "img": "osprey", "alt": "An osprey with a brown back and white head perched on a bare branch",
            "html": "An osprey dives from high above the water and grabs fish with its feet. Its outer toe can turn backward, so it holds a slippery fish with two toes in front and two behind."}
}

wall = {
  "kicker": "🕳️ Under the Burrow", "title": "Follow the burrow down, one stop at a time",
  "look": "A model of a gopher tortoise burrow, cut open so you can see inside. Each stop holds one Florida animal that has been found using these burrows, and a real photo. The dial on the left shows how deep you are.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "A fire is coming. Do you predict the tortoise is the only animal that hides in its burrow?",
              "options": [["no", "No, other animals hide there too"], ["yes", "Yes, only the tortoise"]], "answer": "no",
              "mine": "Your prediction: <b>{p}</b>. Let's dig down and find out.",
              "confirm": "You predicted other animals hide there too. You were right: mice, snakes, and frogs all use tortoise burrows.",
              "change": "You predicted only the tortoise. The burrow changed that idea: many kinds of animals share it when fire comes."},
  "sky": "sky", "skyAlt": "A tortoise burrow opening in a grassy longleaf pine forest", "skyCap": "A gopher tortoise burrow · Florida",
  "unit": "Stop", "found": "Guest found at Stop {n}",
  "elevator": ["Burrow", "Mouth", "Tunnel", "Middle", "Deep end"],
  "line": ["SURFACE: HOT FIRE", "DEEP: COOL AND SAFE"],
  "lockTag": "🔒 Open the stop above first", "locked": "Open the stop above first. We go one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Keep going. Brush Stop {n}.",
  "endTitle": "All 4 stops opened",
  "endText": "Look at the burrow. A mammal, two reptiles, and an amphibian all use the same shelter.",
  "rule": "<b>One burrow, many guests.</b> Scientists have found more than 350 kinds of animals using gopher tortoise burrows. Deep underground, the soil stays cool even when fire burns above.",
  "choices": ["🐾 Mammal: fur, milk for babies", "🪶 Bird: feathers and wings", "🐍 Reptile: dry, tough scales", "🐸 Amphibian: smooth, wet skin"],
  "layers": [
    {"name": "Stop 1 · Florida mouse", "rock": "sandstone", "img": "l1", "alt": "A small gray-brown Florida mouse held gently in a person's sandy hand",
     "ask": "Look at Stop 1. Read the clue AND the photo. What group is it?",
     "clue": "The Florida mouse has soft fur. A mother mouse feeds her babies milk. It often digs a side tunnel off a tortoise burrow.",
     "ans": 0, "ok": "Yes! Fur and milk for babies: the Florida mouse is a mammal.", "tag": "🐾 Florida mouse · mammal",
     "miss": {"1": "Look again. Does a mouse have feathers?", "2": "Not quite. Is a mouse covered in scales?", "3": "Not yet. Does a mouse have smooth, wet skin?"},
     "env": "e1", "envAlt": "A round burrow opening in a mound of white sand", "envCap": "A gopher tortoise burrow mouth in white sand · Florida"},
    {"name": "Stop 2 · Eastern indigo snake", "rock": "soil", "img": "l2", "alt": "A long, shiny blue-black snake coiled on pale sand",
     "ask": "Look at Stop 2. Read the clue AND the photo. What group is it?",
     "clue": "The eastern indigo snake has dry, smooth scales. In winter it often rests inside tortoise burrows.",
     "ans": 2, "ok": "Yes! Dry scales: the indigo snake is a reptile.", "tag": "🐍 Indigo snake · reptile",
     "miss": {"0": "Not quite. Does a snake have fur?", "1": "Not yet. Does a snake have feathers?", "3": "Close! But read the clue: is its skin wet and smooth, or covered in dry scales?"},
     "env": "sky", "envAlt": "A tortoise burrow opening in a grassy longleaf pine forest", "envCap": "A tortoise burrow in a longleaf pine forest · Florida"},
    {"name": "Stop 3 · Gopher frog", "rock": "mudstone", "img": "l3", "alt": "A chubby, spotted brown frog sitting on sand",
     "ask": "Look at Stop 3. Read the clue AND the photo. What group is it?",
     "clue": "The gopher frog has smooth, wet skin. It lays its eggs in ponds, and it hides in tortoise burrows on dry land.",
     "ans": 3, "ok": "Yes! Smooth, wet skin and eggs in ponds: the gopher frog is an amphibian.", "tag": "🐸 Gopher frog · amphibian",
     "miss": {"0": "Not this one. Does a frog have fur?", "1": "Not quite. Does a frog have feathers?", "2": "Close! But read the clue: is its skin dry and scaly, or smooth and wet?"},
     "env": "e3", "envAlt": "A pine forest with saw palmettos and green plants", "envCap": "Pine forest where gopher frogs can live · Florida Panther National Wildlife Refuge"},
    {"name": "Stop 4 · Gopher tortoise", "rock": "shale", "img": "l4", "alt": "A gopher tortoise with a dark, domed shell walking through green grass",
     "ask": "Look at Stop 4. Read the clue AND the photo. What group is it?",
     "clue": "The gopher tortoise has dry, scaly legs and a hard shell. It lays eggs in the sand. It dug this whole burrow.",
     "ans": 2, "ok": "Yes! Dry scales and eggs on land: the gopher tortoise is a reptile.", "tag": "🐢 Gopher tortoise · reptile",
     "miss": {"0": "Not quite. Does a tortoise have fur?", "1": "Not yet. Does a tortoise have feathers?", "3": "Close! It lives in a hole, but read the clue: is its skin wet, or dry and scaly?"},
     "env": "e4", "envAlt": "A gopher tortoise at the dark opening of its burrow in pale sand", "envCap": "A gopher tortoise at its burrow · Florida"}
  ],
  "mix": {
    "q": "Sam says, \"Every difference between two animals is a survival advantage.\" What do you think?",
    "options": [
      {"t": "Sam is right. Any difference helps an animal.", "miss": "Think about two tortoises with shells of slightly different brown. Would that help one survive a fire?"},
      {"t": "Most differences don't matter much. A difference is an advantage only if it helps with a real challenge.", "ok": "Yes! A deeper burrow helps in a fire, and pale fur helps on white sand. A slightly different shell color probably doesn't change much."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Burrow City",
  "img": "wow", "alt": "A black racer snake lying at the mouth of a gopher tortoise burrow",
  "caption": "A black racer snake at the door of a gopher tortoise burrow",
  "html": "<p style=\"margin:0 0 8px\">A gopher tortoise burrow can be as long as a school bus. Deep inside, it stays cool in summer and safe during fires.</p><p style=\"margin:0\">Scientists have found more than 350 kinds of animals using these burrows: snakes, frogs, mice, insects, and more.</p>",
  "inset": "e1", "insetCap": "A fresh burrow mouth in white sand."}

keyIdea = "Individuals in a population are not all the same. These small differences are called variations. Most variations don't matter much, but some give an individual a survival advantage, like a deeper burrow during a fire or pale fur on white sand. Survivors have young, and the young can inherit the helpful characteristic. Scientists use evidence, like observations and measurements, to find out which variations matter."

M = ["🐾 Mammal", "🪶 Bird", "🐢 Reptile", "🐸 Amphibian"]
SHORT = ["a mammal", "a bird", "a reptile", "an amphibian"]
SOL = [["adv", "🏆 A survival advantage"], ["dis", "⚠️ A disadvantage"], ["none", "➖ No real difference"]]


def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": envAns, "bts": bts}


det = {
  "look": "Five Florida variation files. Each card shows two individuals of the same kind, or one behavior that varies. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap the variation you see, then name its animal group. Predict if the variation helps, hurts, or makes no real difference, and see the real place.",
  "noun": "Card", "need": 3, "inferQ": "What group is it in?", "inferDone": "It's", "chartSo": "and this variation is",
  "predict": {"q": "Does this variation help it survive?", "options": SOL},
  "kicker": "Where it lives", "enough": "You already solved 3 variation cards. Nice work, biologist!",
  "cols": ["Card", "My observation", "Animal group", "Does it help?", "My evidence"],
  "write": {"label": "Card __ shows ___. This variation is ___, because ___.", "starter": "Start with: \"Card __ shows…\"", "min": 15,
            "chips": [["trait", "Names the variation"], ["hab", "Says if it helps"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "Two alligators side by side: a white alligator on the left and a dark alligator in green water on the right",
         [{"t": "One alligator is white, one is dark", "ok": True}, {"t": "One has feathers", "miss": "Look again. Does either one have feathers?"}, {"t": "One has fur", "miss": "Look again. Does either one have fur?"}],
         2, "An alligator has dry, tough scales and lays eggs. Which group is that? Try again.",
         "dis", "Think about a white animal in dark swamp water. Would prey see it coming? Try again.",
         "d1h", "Dark, shady swamp water under tangled trees", "Dark swamp water, where alligators hunt · Corkscrew Swamp Sanctuary, Florida",
         "A white alligator stands out in dark water, so prey can see it coming, and strong sun can burn its pale skin. Very few white alligators survive in the wild.",
         "The white alligator in this photo lives in a zoo, where people keep it safe."),
    card("B", "d2", "Two deer side by side: a small Key deer in green grass on the left and a bigger white-tailed deer in tall grass on the right",
         [{"t": "One kind of deer is much smaller", "ok": True}, {"t": "One deer has scales", "miss": "Look again. Do deer have scales?"}, {"t": "One deer has wings", "miss": "Look again. Do deer have wings?"}],
         0, "A deer has fur, and a mother feeds her fawn milk. Which group is that? Try again.",
         "adv", "Small islands have less food. Would a smaller body that needs less food help or hurt? Try again.",
         "d2h", "A small Key deer standing among island plants", "A Key deer among island plants · Big Pine Key, Florida",
         "Key deer are a small kind of white-tailed deer that live only in the Florida Keys. Scientists think a smaller body, which needs less food, helps them on small islands.",
         "A grown Key deer is only about as tall as a big dog."),
    card("C", "d3", "A blue and gray Florida scrub-jay perched on a bare branch, keeping watch",
         [{"t": "Some families have more jays keeping watch", "ok": True}, {"t": "Its fur is pale", "miss": "Look again. Does a bird have fur?"}, {"t": "Its scales are dark", "miss": "Look again. Does it have scales?"}],
         1, "A scrub-jay has feathers and wings, and lays eggs. Which group is that? Try again.",
         "adv", "More lookouts can spot a hawk sooner. Does that help the family? Try again.",
         "d3h", "Two hikers on a sandy trail through low scrub bushes", "Florida scrub · Juniper Prairie Wilderness, Ocala National Forest",
         "Scrub-jay families take turns keeping watch for hawks. Some families have more helpers than others. More lookouts can spot danger sooner, so this behavior is a survival advantage.",
         "This variation is a behavior, not a body part. Behaviors can vary too."),
    card("D", "d4", "Two gopher tortoise shells side by side, one lighter orange-brown and one darker brown",
         [{"t": "One shell is a lighter brown", "ok": True}, {"t": "One has smooth, wet skin", "miss": "Look again. Is a tortoise's skin wet?"}, {"t": "One has feathers", "miss": "Look again. Does a tortoise have feathers?"}],
         2, "A tortoise has dry, scaly skin and lays eggs in sand. Which group is that? Try again.",
         "none", "Both tortoises hide underground when danger comes. Would a slightly different brown change much? Try again.",
         "sky", "A tortoise burrow in a grassy longleaf pine forest", "A tortoise burrow in a longleaf pine forest · Florida",
         "Gopher tortoise shells come in many shades of brown. Scientists have not found that a slightly lighter or darker shell changes which tortoise survives. Not every difference matters.",
         "A tortoise's shell is part of its skeleton, so it grows along with the tortoise."),
    card("E", "d5", "A pink roseate spoonbill wading in shallow water, sweeping its flat bill",
         [{"t": "Some spoonbills have slightly longer bills", "ok": True}, {"t": "Some have fur", "miss": "Look again. Does a bird have fur?"}, {"t": "Some have gills", "miss": "Look again. Does a bird have gills?"}],
         1, "A spoonbill has feathers and wings. Which group is that? Try again.",
         "adv", "In a dry spell, the food moves to deeper water. Which bill could still reach it? Try again.",
         "d5h", "A shallow marsh with grass and pools of water", "A shallow marsh, where spoonbills feed · Everglades National Park",
         "A spoonbill feels for food with its bill. If a dry spell leaves food only in deeper water, a bird with a slightly longer bill might still reach it. This is a model; scientists would test it with measurements.",
         "Spoonbills don't need to see their food. They feel it with their bills, even in muddy water.")
  ]
}

rebuild = {"title": "Use your evidence to sort the variations", "missPrefix": "Hmm. Look at your variation card again. ", "kicker": "🗂️ Sort the variations", "whyStart": "I chose this because the variation…",
  "envs": [
    {"key": "adv", "name": "🏆 A survival advantage", "img": "f_dune", "cap": "Helps it survive…"},
    {"key": "dis", "name": "⚠️ A disadvantage", "img": "d1h", "cap": "Makes life harder…"},
    {"key": "none", "name": "➖ No real difference", "img": "sky", "cap": "Doesn't change much…"}
  ],
  "life": [
    {"name": "🐊 A white alligator", "img": "d1", "env": "dis", "miss": "A white alligator stands out in dark water. That's a disadvantage."},
    {"name": "🦌 A small Key deer", "img": "d2", "env": "adv", "miss": "Scientists think a small body helps Key deer on islands with less food."},
    {"name": "🐦 A family with more lookouts", "img": "d3", "env": "adv", "miss": "More lookouts spot hawks sooner. That's an advantage."},
    {"name": "🐢 A lighter brown shell", "img": "d4", "env": "none", "miss": "A slightly different brown doesn't change much."},
    {"name": "🦩 A slightly longer bill", "img": "d5", "env": "adv", "miss": "In a dry spell, a longer bill might still reach food."}
  ]}

quiz = [
  {"q": "What is a variation?", "options": [
    {"t": "A body feature that every animal of a species shares in exactly the same form", "miss": "A variation isn't about being the same. It's a difference between individuals of the same species. Think about the pale mouse and the darker mouse."},
    {"t": "A difference in a characteristic between individuals of the same species", "ok": "🌿 Exactly right. A variation is a difference between individuals of the same kind, like a pale beach mouse and a darker mouse of the same species."},
    {"t": "A brand-new trait that appears when two different species breed together", "miss": "A variation isn't about different species. It's a difference between individuals of the same species. Think about the pale mouse and the darker mouse."}]},
  {"q": "A dry spell hits south Florida and the water drops. Spoonbill A has a slightly longer bill than Spoonbill B. What is the most likely outcome?", "options": [
    {"t": "Spoonbill A struggles more because its longer bill is harder to sweep through shallow water", "miss": "Think about what changes during a dry spell: the food moves to deeper water. Which bill can still reach it?"},
    {"t": "Both spoonbills are equally affected because bill length doesn't change how deep they can reach", "miss": "Think about what changes during a dry spell: the food moves to deeper water. Which bill can still reach it?"},
    {"t": "Spoonbill A can still reach food in slightly deeper water, giving it a survival advantage during the dry spell", "ok": "🌿 Right! The dry spell is what makes the variation matter. Spoonbill A's longer bill gives it an advantage because the water level dropped."}]},
  {"q": "Which statement best describes how a variation becomes a survival advantage?", "options": [
    {"t": "A variation becomes an advantage when it helps one individual survive a specific challenge in its environment better than others of the same kind", "ok": "⭐ Exactly! The environment and the challenge are what make the variation matter. Most variations don't help or hurt, but some, in the right situation, make a real difference."},
    {"t": "Every difference between animals is a survival advantage because any variation is better than none", "miss": "Think about the tortoises. A deeper burrow only mattered because of what happened: the fire. That's what turns a small difference into a survival advantage."},
    {"t": "A variation only becomes an advantage if it creates a completely new species over time", "miss": "Think about the tortoises. A deeper burrow only mattered because of what happened: the fire. That's what turns a small difference into a survival advantage."}]}
]


def matchq(n, q, opts, ans, ok, miss):
    return {"n": n, "q": q, "type": "choice", "options": [{"t": c, "ok": ok} if i == ans else {"t": c, "miss": miss} for i, c in enumerate(opts)]}


partA = {"title": "Name the science idea", "do": "Read each one. Pick the best answer.", "items": [
  matchq(1, "Two gopher tortoises in the same scrub: one has slightly wider front legs than the other.", ["A variation", "A new species", "A habitat"], 0, "Yes. A difference between two individuals of the same kind is a variation.", "Are these two different kinds of animals, or two of the same kind?"),
  matchq(2, "Wide, flat front legs that help every gopher tortoise dig a burrow.", ["A population", "An adaptation", "A variation"], 1, "Yes. A trait that helps the whole species survive is an adaptation.", "Do all gopher tortoises have this, or only some?"),
  matchq(3, "All the beach mice living on one Florida beach.", ["An individual", "A characteristic", "A population"], 2, "Yes. A group of the same kind of animal in one area is a population.", "Is this one mouse, or a whole group?"),
  matchq(4, "One single pale beach mouse.", ["An individual", "A population", "A habitat"], 0, "Yes. One single animal is an individual.", "Is this one mouse, or a whole group?"),
  matchq(5, "Scrub-jay family members taking turns keeping watch for hawks.", ["A body part", "A behavior", "A habitat"], 1, "Yes. Keeping watch is something the jays do, so it's a behavior.", "Is keeping watch a part of the body, or something the jays do?")
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Explain the difference between an adaptation and a variation. Use an example from today's investigation to make the difference clear.", "type": "text", "min": 12, "chips": [["adaptw", "Uses the word adaptation"], ["varw", "Uses the word variation"]]},
    {"n": 2, "q": "Spoonbill A (longer bill) survives a dry spell and raises young, and Spoonbill B does not. What might happen to the spoonbill population over many generations? Use the words population and characteristic.", "type": "text", "min": 12, "chips": [["popw", "Uses the word population"], ["charw", "Uses the word characteristic"]]}
  ]},
  "write": {"title": "Choose one variation pair from today. Does the variation give one individual a survival advantage? Use evidence to support your answer.", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["variation", "survival advantage", "population", "individual", "characteristic"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think the variation in [characteristic] gives one individual a survival advantage because…\""],
                ["What did you observe or learn that supports your thinking?", "Start with: \"I know this because when I compared the two individuals, I noticed…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because in this habitat, an individual without this variation would…\""]]},
  "partC": {"do": "Draw two individuals of the same Florida animal side by side. Show one variation between them, in a body part or a behavior. Label the variation on each one, and say which has the survival advantage.",
            "labels": ["Individual 1: its variation", "Individual 2: its variation, and which one has the advantage"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 variation cards and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all five answered.", "req": {"choice": ["a1", "a2", "a3", "a4", "a5"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my variation story", "thinkLabel": "Its animal group", "director": "JUNIOR BIOLOGIST", "storyKicker": "My variation story",
  "frames": [
    {"k": "formation", "label": "Fire day", "img": "f_burnt", "cap": "Fire day: the tortoise goes deep and stays safe."},
    {"k": "compare", "label": "The Owl Test", "img": "ta", "cap": "The Owl Test: each fur color hides best on its own ground."},
    {"k": "wall", "label": "Under the Burrow", "img": "l3", "cap": "Under the Burrow: many animal groups share one shelter."},
    {"k": "det", "label": "Variation files", "img": "d1", "cap": "Variation files: some differences help, some hurt, some don't matter."}]}

nxt = {"title": "Coming up next: 31.01", "text": "What Threatens Florida Ecosystems? Next time, find out what puts Florida's wild places and animals in danger, and what people can do to help."}

chips = {
  "part": {"any": ["shell", "legs", "leg", "scales", "scaly", "head", "eye", "eyes", "claws", "flat", "wide", "dome", "domed", "sand", "brown", "beak", "tortoise", "turtle", "feet"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["white", "pale", "dark", "darker", "smaller", "small", "bigger", "longer", "bill", "shell", "lookouts", "watch", "fur", "color", "variation", "brown", "lighter"]},
  "hab": {"any": ["advantage", "disadvantage", "helps", "help", "hurts", "survive", "difference", "matter", "safer", "harder"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "adaptw": {"any": ["adaptation", "adaptations"]},
  "varw": {"any": ["variation", "variations"]},
  "popw": {"any": ["population", "populations"]},
  "charw": {"any": ["characteristic", "characteristics"]}
}

L = {"id": "g3sci-30-02", "lesson": "30.02", "title": "Investigation: Adaptation Comparison", "emoji": "🔀",
  "details": ["📅 Q4 · Unit 10 · Florida Ecosystems", "📖 Week 30 · Lesson 30.02", "🌎 CPALMS SC.3.N.1.7, SC.3.L.15.1", "⏱ About 35 minutes"],
  "icans": ["explain what a variation is and give an example from a Florida animal.", "compare two individuals of the same species and identify which variation gives a survival advantage.", "use evidence to explain why survival advantages matter for a species over time."],
  "opti": {"warm": "Our film starts on a fire day in the Florida scrub. First, inspect a mystery animal hiding in its shell.",
           "lesson": "Today you're a biologist. Follow a tortoise through a fire, run the Owl Test, then dig down Under the Burrow.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Name the science ideas, then draw two animals of the same kind with one variation."},
  "film": film, "scientist": "biologist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: In the Hall of the Mountain King, from Peer Gynt (Edvard Grieg), Musopen Symphony Orchestra, public domain recording (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The burrow movie, the Owl Test, and the burrow cutaway are models; every place photo is real. Two-photo cards put two real photos side by side. The fire photos show planned burns set by wildlife workers."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-30-02-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the animal, then tap three things you notice."},
  "how-30-02-compare": {"page": "Put the white sand under one tray and the dark soil under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the white sand under one tray and the dark soil under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-30-02-wall": {"page": wall["do"], "say": wall["do"]},
  "how-30-02-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap the variation you see, then name its animal group. Predict if the variation helps, hurts, or makes no real difference, and see the real place."},
  "how-30-02-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"30-02-welcome": L["opti"]["warm"], "30-02-lesson": L["opti"]["lesson"], "30-02-check": L["opti"]["check"], "30-02-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
