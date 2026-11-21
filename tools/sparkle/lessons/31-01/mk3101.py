#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/31-01/lesson.json, how-lines.json, scripts.json, credits.json (31.01: no voices recorded; scripts only).
Images come from prep.py (run it first)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "What is threatening Florida's wild places, and what can people do about it?"

film = {
  "id": "g3sci-31-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 31.01 · What Threatens Florida Ecosystems?",
  "title": "Uninvited Guest",
  "bigQuestion": BQ,
  "poster": "f_py", "endPoster": "f_marsh", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 3.0, "type": "black", "sfxAt": [{"at": 0.4, "name": "bubbles"}, {"at": 1.8, "name": "bubbles"}], "fade": 0.5},
    ph(6.4, 5.4, "f_trail", "A wooden boardwalk winding through green marsh plants under a bright sun", "Anhinga Trail · Everglades National Park",
       frm=(1.12, .5, .6), to=(1.0, .5, .5), fade=1.0),
    ph(11.8, 5.4, "f_egret", "A white great egret standing in still water, its reflection below it", "A great egret · Everglades National Park",
       frm=(1.0, .5, .5), to=(1.06, .5, .45), contain=True),
    ph(17.2, 6.0, "f_py", "A large Burmese python with a brown and tan pattern coiled in the grass", "A Burmese python · Everglades, Florida",
       frm=(1.0, .5, .5), to=(1.22, .45, .45), sfxAt=[{"at": 0.4, "name": "rumble"}]),
    ph(23.2, 6.4, "f_rac", "A raccoon with a striped tail walking on sandy ground", "A raccoon · Everglades National Park",
       frm=(1.0, .5, .5), to=(1.1, .55, .5), fade=0.6, count={"to": 99, "label": "% fewer raccoons seen", "dur": 2.6}, **{"in": "ripple"}),
    ph(29.6, 6.0, "f_measure", "A young python stretched next to a ruler on a blue background", "A young python measured by park scientists · Everglades National Park",
       frm=(1.0, .5, .5), to=(1.08, .5, .5)),
    ph(35.6, 7.2, "f_marsh", "A wide marsh of golden sawgrass with a great blue heron standing in it", "Shark Valley · Everglades National Park",
       frm=(1.0, .5, .5), to=(1.08, .5, .5), fade=0.9),
    {"t": 42.8, "d": 5.6, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 6.8, "d": 4.8, "text": "Early morning in the Everglades.", "voice": "opti-1"},
    {"t": 12.2, "d": 4.8, "text": "Wading birds hunt in the shallow marsh.", "voice": "opti-2"},
    {"t": 17.6, "d": 5.4, "text": "But something new is hiding in the grass.", "voice": "opti-3"},
    {"t": 23.6, "d": 5.8, "text": "Where pythons spread, scientists saw far fewer raccoons and rabbits.", "voice": "opti-4"},
    {"t": 30.0, "d": 5.4, "text": "Now scientists catch and measure pythons to learn how to stop them.", "voice": "opti-5"},
    {"t": 36.0, "d": 6.4, "text": BQ, "voice": "opti-6"}
  ]
}

specimen = {
  "img": "spec", "aspect": "4/3", "radius": 0.07,
  "hotspots": [
    {"name": "Long, sharp spines on its back", "x": 0.33, "y": 0.11},
    {"name": "Bold red-and-white stripes", "x": 0.34, "y": 0.44},
    {"name": "Wide, feathery side fins, like fans", "x": 0.55, "y": 0.64},
    {"name": "A big eye", "x": 0.17, "y": 0.68},
    {"name": "A wide mouth for gulping small fish", "x": 0.11, "y": 0.81},
    {"name": "A see-through tail fin", "x": 0.84, "y": 0.56}
  ],
  "kicker": "🔎 Mystery specimen", "title": "Who is this spiny fish?",
  "alt": "A striped red-and-white fish with long spines and wide, feathery fins on a black background",
  "look": "A real fish, photographed up close. Look at its spines, its stripes, and its wide fins. A specimen is one real thing that scientists study. This fish now lives on Florida's reefs, but it didn't always. Why might scientists be worried about it? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the fish, then tap 3 things you notice.",
  "number": "No. 31.01-A",
  "card": ["<b>Specimen A</b>", "Length: about 30 cm (12 inches)", "Found on: Florida coral reefs", "Should it be here? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🌿", "ecosystem", "All the living things in a place and the non-living things they depend on, like water, soil, and sunlight."],
  ["💧", "pollution", "Harmful materials that get into the air, water, or soil and make it hard for living things to survive."],
  ["🐍", "invasive species", "A plant or animal from somewhere else that spreads in a new place and harms the living things that belong there."],
  ["🏗️", "habitat loss", "When the natural home of plants and animals is destroyed or changed so much that they can't live there anymore."],
  ["🌧️", "runoff", "Rainwater that flows over the land, picking up things like fertilizer and carrying them into rivers, lakes, and wetlands."],
  ["🌱", "conservation", "The work of protecting and restoring nature so ecosystems stay healthy now and in the future."]
]

parts = [
  {"kicker": "🌿 Part 1", "title": "Florida's Wild Places Are Changing",
   "html": "<p>Florida's ecosystems, like the Everglades, mangrove coasts, and dry scrub, are home to hundreds of kinds of plants and animals. But scientists are watching these places change. Some lakes are turning green. Some animals are losing their homes. Scientists study these places closely to find out what is causing the changes.</p>"},
  {"kicker": "⚠️ Part 2", "title": "Three Big Threats",
   "html": "<p><b>Pollution:</b> rain washes fertilizer off farms and lawns. This runoff makes algae grow out of control, blocking sunlight and using up oxygen fish need.</p><p><b>Invasive species:</b> Burmese pythons came as pets, and some got loose. Now they spread and eat native animals.</p><p><b>Habitat loss:</b> when a wetland is drained or a forest is cleared, the animals there have nowhere to go.</p>"},
  {"kicker": "🔬 Part 3", "title": "How Scientists Know, and How People Help",
   "html": "<p>Scientists use evidence: observations and data. In places where pythons spread, they counted far fewer raccoons, opossums, and rabbits. Satellites show where algae covers a lake.</p><p>People are working on fixes. Engineers build filter marshes to clean water. Divers and trappers remove invaders. Parks and preserves protect wild land.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Threat Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the rain on the farm.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does fertilizer turn a lake green?",
  "look": "Four real photos show how runoff travels, from a farm field to a lake. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "Muddy rainwater pouring off a farm field into a ditch", "text": "Rain washes fertilizer off a farm field.", "play": "Rain washes it off.",
     "miss": ["", "It starts on the farm when it rains. Try frame 1.", "It starts on the farm when it rains. Try frame 1.", "It starts on the farm when it rains. Try frame 1."]},
    {"img": "o2", "alt": "A long, straight canal cutting across a wide marsh", "text": "The runoff flows into canals and rivers.", "play": "It flows downstream.",
     "miss": ["The rain has to wash it off first. Try a later frame.", "", "It travels before it reaches the lake. Try an earlier frame.", "It travels before it reaches the lake. Try an earlier frame."]},
    {"img": "o3", "alt": "Lake Okeechobee seen from space, with swirls of green algae", "text": "Algae spreads across the lake.", "play": "Algae spreads.",
     "miss": ["The runoff has to reach the lake first. Try a later frame.", "The runoff has to reach the lake first. Try a later frame.", "", "Algae spreads before it gets this thick. Try an earlier frame."]},
    {"img": "o4", "alt": "Bright green algae covering the water of a marina between buildings", "text": "Thick algae blocks sunlight, and fish run short of oxygen.", "play": "Fish run short of oxygen.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Ava says, \"Pollution is only trash you can see, like bottles and bags.\" What do you think?",
    "options": [
      {"t": "Ava is right. If you can't see it, it isn't pollution.", "miss": "Think about the movie. Could you see the fertilizer in the rainwater? What did it do to the lake?"},
      {"t": "Some pollution is hard to see, like fertilizer in runoff. It can still turn a lake green.", "ok": "Yes! Fertilizer melts into rainwater, so you can't see it. But it makes algae grow out of control."}
    ]
  }
}

movie = {
  "model": "runoff-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🌧️",
  "real": "o3", "realAlt": "Lake Okeechobee seen from space in July 2016, with green swirls of algae",
  "stamp": "TOO MUCH FERTILIZER!", "endCap": "Real algae on Lake Okeechobee, seen from space (2016).",
  "beats": [
    {"at": 0, "cap": "1 · Rain washes it off.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Rainy day"], "sfx": "whoosh"},
    {"at": 2600, "cap": "2 · It flows downstream.", "model": {"show": "s2"}, "counter": ["Same day"]},
    {"at": 5200, "cap": "3 · Algae spreads.", "model": {"show": "s3"}, "counter": ["Days later"]},
    {"at": 7800, "cap": "4 · Fish run short of oxygen.", "model": {"show": "s4"}, "counter": ["Weeks later"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Buffer Test", "title": "Which edge keeps the water clean?",
  "look": "Two real places where land meets water, each on a lit tray. Shore A is a lawn that runs right down to a pond. Shore B is a farm field after a rainstorm. Under the trays are two model edges: a strip of native plants, and bare dirt.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A grassy lawn sloping down to a murky pond", "label": "Shore A"},
    {"id": "B", "img": "tb", "alt": "Muddy rainwater pouring off a farm field", "label": "Shore B"}
  ],
  "materials": [{"key": "plants", "label": "A strip of native plants", "img": "m_plants"}, {"key": "bare", "label": "A bare dirt edge", "swatch": "mud"}],
  "ask": [
    {"q": "Which shore is a lawn by a pond?", "ans": "A", "ok": "Yes. Shore A is the lawn.", "miss": "Look closely. Which one has a pond and grass?"},
    {"q": "Which shore is a farm field?", "ans": "B", "ok": "Yes. Shore B is the farm field.", "miss": "Look again. Which one shows a field and muddy water?"}
  ],
  "press": "🌧️ Make it rain",
  "testDo": "Put the plant strip on one shore and the bare dirt on the other: drag them, or tap one, then a tray. Press <b>Make it rain</b>. Then swap.",
  "disclaimer": "This is a model. No real ponds are changed.",
  "results": {
    "Aplants": {"text": "The plant strip catches the runoff. The pond stays clearer!", "fx": "shade"},
    "Abare": {"text": "Fertilizer from the lawn washes straight into the pond. Algae will grow.", "fx": "glow"},
    "Bplants": {"text": "The plants slow the muddy water and soak up fertilizer before it reaches the water!", "fx": "shade"},
    "Bbare": {"text": "Muddy, fertilizer-filled runoff pours right into the water.", "fx": "glow"}
  },
  "best": ["Aplants", "Bplants"],
  "frame": "This shore's water stayed cleanest with ___, so the runoff was caught by ___.", "claimLead": "This shore's water stayed cleanest with", "claimMid": "so the runoff was caught by",
  "claim": {
    "A": {"feat": ["a strip of native plants", "a bare dirt edge"], "featOk": 0, "eat": ["the plants' roots and stems", "the pond water"], "eatOk": 0},
    "B": {"feat": ["a strip of native plants", "a bare dirt edge"], "featOk": 0, "eat": ["the plants' roots and stems", "the pond water"], "eatOk": 0}
  },
  "curator": {
    "A": "<b>A buffer strip.</b> A row of native plants along a pond slows rainwater down. Roots soak up fertilizer before it reaches the water.",
    "B": "<b>Farm buffers.</b> Many farms leave strips of grass or plants along ditches and streams to catch soil and fertilizer."
  },
  "missFeat": "Look at your tests for {label} again. Which edge kept the water cleaner?",
  "missClaim": "Think about your tests. What soaked up the runoff?",
  "done": "On both shores, the plant strip caught the runoff. Plants are a simple way people protect water.",
  "after": {"kicker": "🎬 Behind the scenes · Trail camera", "img": "bob", "alt": "A bobcat on a trail camera standing near a pile of white python eggs in the brush",
            "html": "Scientists put hidden trail cameras near python nests. This camera caught a bobcat visiting a nest of python eggs. Photos like this are evidence that help scientists learn how pythons fit into the Everglades."}
}

wall = {
  "kicker": "🗺️ The Threat Map", "title": "Take a road trip across South Florida, one stop at a time",
  "look": "A model map of South Florida with four stops. Each stop holds a clue and a real photo. The dial on the left shows which stop you're at.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "Do you predict every stop on the map shows people harming nature?",
              "options": [["no", "No, some stops show people helping"], ["yes", "Yes, people only cause harm"]], "answer": "no",
              "mine": "Your prediction: <b>{p}</b>. Let's hit the road and find out.",
              "confirm": "You predicted some stops show people helping. You were right: at Big Cypress, people built underpasses for panthers.",
              "change": "You predicted people only cause harm. The map changed that idea: at Big Cypress, people built underpasses to help panthers."},
  "sky": "sky", "skyAlt": "South Florida seen from space, with Lake Okeechobee and the Everglades", "skyCap": "South Florida from space (NASA)",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Map", "Lake O", "Everglades", "City edge", "Big Cypress"],
  "line": ["WHERE THREATS HIT", "WHERE PEOPLE HELP"],
  "lockTag": "🔒 Open the stop above first", "locked": "Open the stop above first. We go one stop at a time.",
  "first": "Brush the glowing first stop. Drag across it (or tap it again and again).", "next": "Keep going. Brush Stop {n}.",
  "endTitle": "All 4 stops visited",
  "endText": "Look at the map. Three stops show threats. One shows people fixing a problem.",
  "rule": "<b>Three big threats, one big job.</b> Pollution, invasive species, and habitat loss all harm Florida's ecosystems. Conservation is the work people do to protect and restore them.",
  "choices": ["💧 Pollution: harmful stuff in water or soil", "🐍 Invasive species: an outsider that spreads", "🏗️ Habitat loss: wild land cleared or cut up", "🌿 Conservation: people protecting nature"],
  "layers": [
    {"name": "Stop 1 · Lake Okeechobee", "rock": "water1", "img": "o3", "alt": "Lake Okeechobee seen from space, with swirls of green algae",
     "ask": "Look at Stop 1. Read the clue AND the photo. What is happening here?",
     "clue": "Runoff full of fertilizer flows into Florida's biggest lake. In the summer of 2016, a huge bloom of algae covered much of it.",
     "ans": 0, "ok": "Yes! Fertilizer in runoff is pollution.", "tag": "💧 Lake O · pollution",
     "miss": {"1": "Look again. Is something moving in from another place?", "2": "Not quite. Is land being cleared here?", "3": "Not yet. Is this people fixing a problem?"},
     "env": "o4", "envAlt": "Bright green algae covering the water of a marina between buildings", "envCap": "Algae in a marina on the Caloosahatchee River, which flows out of Lake Okeechobee · 2005"},
    {"name": "Stop 2 · The Everglades", "rock": "water2", "img": "l2", "alt": "A large Burmese python coiled on green grass",
     "ask": "Look at Stop 2. Read the clue AND the photo. What is happening here?",
     "clue": "Burmese pythons come from Asia. Some pets got loose in the Everglades. Now there are many, and they eat birds and small mammals.",
     "ans": 1, "ok": "Yes! An animal from far away that spreads and harms native animals is an invasive species.", "tag": "🐍 Everglades · invasive species",
     "miss": {"0": "Not quite. Is something harmful washing into the water?", "2": "Close! But read the clue: is land being cleared, or is an outsider spreading?", "3": "Not yet. Is this people fixing a problem?"},
     "env": "e2", "envAlt": "A small brown marsh rabbit sitting in green grass", "envCap": "A marsh rabbit, one of the animals that is hard to find where pythons live · Green Cay Wetlands, Florida"},
    {"name": "Stop 3 · The city edge", "rock": "soil", "img": "l3", "alt": "An old aerial photo of a new neighborhood being built next to wild wetland",
     "ask": "Look at Stop 3. Read the clue AND the photo. What is happening here?",
     "clue": "In the 1970s, new neighborhoods were built right up to the edge of the Everglades. Wet prairie was filled and paved.",
     "ans": 2, "ok": "Yes! When wild land is filled and paved, animals lose their homes. That's habitat loss.", "tag": "🏗️ City edge · habitat loss",
     "miss": {"0": "Not quite. Is something harmful washing into the water?", "1": "Not yet. Is an animal spreading here?", "3": "Close! People are working here, but are they protecting the land or clearing it?"},
     "env": "e3", "envAlt": "An old aerial photo of cleared land marked with new roads", "envCap": "Land cleared for a new development · South Florida, 1970s"},
    {"name": "Stop 4 · Big Cypress", "rock": "leafsun", "img": "l4", "alt": "A wide concrete bridge over a dirt path, making a tunnel for animals under a highway",
     "ask": "Look at Stop 4. Read the clue AND the photo. What is happening here?",
     "clue": "Roads cut through panther land. Engineers built underpasses and fences so panthers can cross under the highway safely.",
     "ans": 3, "ok": "Yes! Building safe crossings for panthers is conservation: people protecting nature.", "tag": "🌿 Big Cypress · conservation",
     "miss": {"0": "Not this one. Is something washing into the water?", "1": "Not quite. Is an outsider spreading?", "2": "Close! The road caused habitat loss, but read the clue: what are people doing now?"},
     "env": "e4", "envAlt": "A yellow panther crossing sign at sunset by a marsh", "envCap": "A panther crossing sign · Everglades National Park"}
  ],
  "mix": {
    "q": "Kai says, \"People are always harmful to ecosystems.\" What do you think?",
    "options": [
      {"t": "Kai is right. People only cause problems.", "miss": "Think about Stop 4. What did engineers build for panthers?"},
      {"t": "People cause some problems, but people also fix them, like building underpasses and cleaning water.", "ok": "Yes! People caused many of these threats, and people are also working to fix them."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Fixing the River of Grass",
  "img": "wow", "alt": "A wide, shallow marsh of grass and water stretching to the horizon",
  "caption": "The Everglades' River of Grass · Everglades National Park",
  "html": "<p style=\"margin:0 0 8px\">Long ago, people dug canals to drain water from the Everglades for farms and cities. Today, engineers are working to send clean water back.</p><p style=\"margin:0\">It is one of the biggest repair jobs on Earth, and it will take many years. Nature doesn't heal overnight.</p>",
  "inset": "inset", "insetCap": "A steam dredge digging an Everglades canal, long ago."}

keyIdea = "Florida's ecosystems face three big threats: pollution, invasive species, and habitat loss. Runoff carries fertilizer into lakes and makes algae grow. Invasive species like pythons and lionfish spread and eat native animals. Habitat loss happens when wild land is cleared. Scientists use observations and data as evidence, and people are working on fixes: cleaning water, removing invaders, and protecting land."

THR = ["💧 Pollution", "🐍 Invasive species", "🏗️ Habitat loss"]
SHORT = ["pollution", "an invasive species", "habitat loss"]
SOL = [["clean", "🌿 Clean the water"], ["remove", "🎣 Remove the invaders"], ["protect", "🛡️ Protect the land"]]


def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": THR, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": envAns, "bts": bts}


det = {
  "look": "Five Florida threat files. Each card tells what happened in one place. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap the clue that shows the problem, then name the threat. Predict what could help, and see how people are fixing it.",
  "noun": "Card", "need": 3, "inferQ": "Which threat is it?", "inferDone": "It's", "chartSo": "and people can",
  "predict": {"q": "What could help fix it?", "options": SOL},
  "kicker": "How people help", "enough": "You already solved 3 threat files. Nice work, ecologist!",
  "cols": ["Card", "My evidence", "Threat", "How people help", "My explanation"],
  "write": {"label": "Card __ shows ___. This threat harms living things because ___. People can help by ___.", "starter": "Start with: \"Card __ shows…\"", "min": 15,
            "chips": [["trait", "Names the evidence"], ["hab", "Says how people help"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "o4", "Bright green algae covering the water of a marina between buildings",
         [{"t": "Thick green algae on the water after rain washed fertilizer in", "ok": True}, {"t": "A snake moving in", "miss": "Look again. Do you see a snake?"}, {"t": "Trees cut down", "miss": "Look again. Is land being cleared?"}],
         0, "Rain washed fertilizer into the water. Which threat is that? Try again.",
         "clean", "The problem is in the water. What would fix dirty water? Try again.",
         "sta", "Huge square ponds of plants and water seen from the air, next to green farm fields", "Filter marshes built to clean farm water · Everglades Stormwater Treatment Areas",
         "Engineers built huge filter marshes. Plants in them soak up fertilizer before the water flows into the Everglades.",
         "From high above, the filter marshes look like giant green squares."),
    card("B", "d2", "A green iguana with a long striped tail walking on white rocks",
         [{"t": "Pet iguanas let go, now spreading across South Florida", "ok": True}, {"t": "Fertilizer in a river", "miss": "Look again. Is this about water?"}, {"t": "A road through a forest", "miss": "Look again. Is there a road?"}],
         1, "An animal from far away that spreads and harms native plants. Which threat is that? Try again.",
         "remove", "The problem is too many outsiders. What would fix that? Try again.",
         "d2h", "A long, straight canal at the edge of a wide marsh", "A canal at the edge of the Everglades, where iguanas often dig into the banks",
         "Green iguanas are not from Florida. Some pet owners let them go. Now trappers remove iguanas, and Florida asks pet owners never to release a pet.",
         "Green iguanas mostly eat plants, like flowers and leaves from people's gardens."),
    card("C", "d3", "A city with hundreds of canals, seen from the air",
         [{"t": "A swamp filled with soil to build a mall", "ok": True}, {"t": "Algae in a lake", "miss": "Look again. Is this about algae?"}, {"t": "A spiny fish on a reef", "miss": "Look again. Is there a fish?"}],
         2, "Wild land was filled and built on. Which threat is that? Try again.",
         "protect", "The problem is losing wild land. What would keep land wild? Try again.",
         "d3h", "A wooden boardwalk winding through protected marsh", "Protected land · Everglades National Park",
         "When a swamp is filled, the wood storks and otters that lived there lose their home. Protecting wild land in parks and preserves keeps habitats safe.",
         "Cape Coral, in the photo, has hundreds of miles of canals."),
    card("D", "d4", "A highway stretching ahead with a sign warning of panther crossings for the next 6 miles",
         [{"t": "A highway built through panther land", "ok": True}, {"t": "An iguana let go", "miss": "Look again. Is there an iguana?"}, {"t": "Green algae", "miss": "Look again. Is there algae?"}],
         2, "A road cut the panthers' home into pieces. Which threat is that? Try again.",
         "protect", "Panthers need to cross safely. What would protect them? Try again.",
         "d4h", "A grassy path running under a highway bridge built for wildlife", "A wildlife underpass under a Florida highway",
         "Roads cut panther land into pieces, and some panthers are hit by cars. Engineers built underpasses and fences so panthers can cross under the road safely.",
         "Trail cameras show panthers, bobcats, and bears using these underpasses."),
    card("E", "d5", "A striped lionfish with long spines swimming near a coral reef",
         [{"t": "A fish from far away spreading on Florida reefs", "ok": True}, {"t": "A swamp filled with soil", "miss": "Look again. Is this on land?"}, {"t": "Fertilizer runoff", "miss": "Look again. Is this about fertilizer?"}],
         1, "A fish from another ocean that spreads and eats native fish. Which threat is that? Try again.",
         "remove", "The problem is too many outsiders. What would fix that? Try again.",
         "d5h", "A scuba diver with a spear and net catching a lionfish near a reef", "A diver removes a lionfish · Flower Garden Banks, Gulf of Mexico",
         "Lionfish come from the Pacific and Indian Oceans. In Florida, they eat many small reef fish. Divers catch them, and people hold lionfish contests to remove as many as they can.",
         "Lionfish have venomous spines, so divers handle them carefully.")
  ]
}

rebuild = {"title": "Use your evidence to match each threat to a fix", "missPrefix": "Hmm. Look at your threat file again. ", "kicker": "🛠️ Match the fix", "whyStart": "I chose this fix because the threat…",
  "envs": [
    {"key": "clean", "name": "🌿 Clean the water", "img": "sta", "cap": "Filter marshes…"},
    {"key": "remove", "name": "🎣 Remove the invaders", "img": "d5h", "cap": "Catch them…"},
    {"key": "protect", "name": "🛡️ Protect the land", "img": "l4", "cap": "Keep it wild…"}
  ],
  "life": [
    {"name": "💧 Algae from runoff", "img": "o4", "env": "clean", "miss": "Algae from runoff is fixed by cleaning the water."},
    {"name": "🦎 Released iguanas", "img": "d2", "env": "remove", "miss": "Iguanas are invaders. People remove them."},
    {"name": "🏗️ A filled swamp", "img": "d3", "env": "protect", "miss": "Habitat loss is slowed by protecting wild land."},
    {"name": "🛣️ A panther highway", "img": "d4", "env": "protect", "miss": "Underpasses protect panthers' land and paths."},
    {"name": "🐟 Lionfish on reefs", "img": "d5", "env": "remove", "miss": "Lionfish are invaders. Divers remove them."}
  ]}

quiz = [
  {"q": "What is an invasive species?", "options": [
    {"t": "A native Florida animal that migrates south for winter", "miss": "Invasive species is a key word for this lesson. Think about the pythons and lionfish: where did they come from, and what do they do?"},
    {"t": "A plant or animal that spreads into a new place and harms the ecosystem", "ok": "🌊 Exactly right! An invasive species moves into a new place where it doesn't belong, often crowding out native species."},
    {"t": "A type of water pollution caused by farm chemicals", "miss": "Invasive species is a key word for this lesson. Think about the pythons and lionfish: where did they come from, and what do they do?"}]},
  {"q": "What most likely happens when too much fertilizer washes into a Florida lake?", "options": [
    {"t": "More fish grow because there are extra nutrients in the water", "miss": "Think about what algae does when it grows out of control. What does it block? What does it use up?"},
    {"t": "The water gets cleaner as plants filter the nutrients", "miss": "Think about what algae does when it grows out of control. What does it block? What does it use up?"},
    {"t": "Algae grows out of control, blocking sunlight and reducing oxygen", "ok": "🌿 Yes! Too much fertilizer causes an algae bloom that blocks sunlight and uses up oxygen, making the lake harmful to fish and other animals."}]},
  {"q": "Which of these is an example of habitat loss?", "options": [
    {"t": "A cypress swamp is drained and filled to build a shopping center", "ok": "⭐ That's it! Draining a swamp to build a shopping center destroys the habitat. The animals that lived there have nowhere to go."},
    {"t": "A scientist removes invasive plants from a protected wetland", "miss": "Habitat loss means the natural home is destroyed. Which choice describes something being destroyed or taken away?"},
    {"t": "A rainstorm washes dirt and leaves into a river", "miss": "Habitat loss means the natural home is destroyed. Which choice describes something being destroyed or taken away?"}]}
]


def matchq(n, q, ans, ok, miss):
    opts = ["Pollution", "Invasive species", "Habitat loss"]
    return {"n": n, "q": q, "type": "choice", "options": [{"t": c, "ok": ok} if i == ans else {"t": c, "miss": miss} for i, c in enumerate(opts)]}


partA = {"title": "Match the threat", "do": "Read each one. Pick the type of threat.", "items": [
  matchq(1, "Farm fertilizer washes into a Florida lake during a rainstorm.", 0, "Yes. Fertilizer in runoff is pollution.", "Is something harmful getting into the water?"),
  matchq(2, "A Burmese python spreads through the Everglades, eating native mammals.", 1, "Yes. The python is an invasive species.", "Is this an animal from somewhere else that spreads?"),
  matchq(3, "A forest near Tampa is cleared to build a housing development.", 2, "Yes. Clearing a forest is habitat loss.", "Is wild land being destroyed?"),
  matchq(4, "Lionfish from the Pacific Ocean spread across Florida's reefs.", 1, "Yes. Lionfish are an invasive species.", "Are these fish from somewhere else?"),
  matchq(5, "A highway is built through the middle of panther land.", 2, "Yes. A road that cuts up wild land causes habitat loss.", "Is the panthers' home being cut up?")
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Explain how runoff can harm a Florida ecosystem. Use the word pollution in your answer.", "type": "text", "min": 12, "chips": [["pollw", "Uses the word pollution"], ["harm", "Says how it harms living things"]]},
    {"n": 2, "q": "Why is an invasive species dangerous even if it looks harmless at first?", "type": "text", "min": 12, "chips": [["invw", "Names an invasive species"], ["harm", "Says how it harms living things"]]}
  ]},
  "write": {"title": "Which of the three threats, pollution, invasive species, or habitat loss, do you think is the most serious danger to Florida's ecosystems?", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["ecosystem", "pollution", "invasive species", "habitat loss", "conservation"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think the most serious threat is…\""],
                ["What did you learn that supports your thinking?", "Start with: \"I know this because the lesson showed…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because…\""]]},
  "partC": {"do": "Draw a Florida wetland ecosystem. Show one threat happening in your drawing. Label at least 4 things: at least one plant, one animal, and the source of the threat.",
            "labels": ["Labels 1 and 2: a plant and an animal", "Labels 3 and 4: the threat and where it comes from"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 threat files and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all five matched.", "req": {"choice": ["a1", "a2", "a3", "a4", "a5"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and all my labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my Florida threat report", "thinkLabel": "Its threat", "director": "JUNIOR ECOLOGIST", "storyKicker": "My Florida threat report",
  "frames": [
    {"k": "formation", "label": "Runoff day", "img": "o3", "cap": "Runoff day: rain carries fertilizer into the lake, and algae spreads."},
    {"k": "compare", "label": "The Buffer Test", "img": "m_plants", "cap": "The Buffer Test: a plant strip keeps the water cleaner."},
    {"k": "wall", "label": "The Threat Map", "img": "l2", "cap": "The Threat Map: three threats and one fix across South Florida."},
    {"k": "det", "label": "Threat files", "img": "d5", "cap": "Threat files: every threat has people working on a fix."}]}

nxt = {"title": "Coming up next: 31.02", "text": "Engineering Challenge: Protect Florida Habitats. Next time, you're the engineer. Design a fix for one of Florida's habitat problems."}

chips = {
  "part": {"any": ["spines", "spine", "spiky", "fins", "fin", "stripes", "striped", "eye", "eyes", "mouth", "tail", "red", "white", "orange", "fish", "sharp", "long", "fan", "feathery", "lion", "lionfish"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["algae", "green", "pet", "pets", "iguana", "iguanas", "filled", "swamp", "road", "highway", "cars", "lionfish", "reef", "fertilizer", "runoff", "spread", "spreading", "python", "mall"]},
  "hab": {"any": ["clean", "remove", "removing", "protect", "protecting", "underpass", "underpasses", "filter", "plants", "trap", "trappers", "divers", "park", "parks", "help", "fix"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "pollw": {"any": ["pollution", "pollute", "polluted"]},
  "harm": {"any": ["harm", "harms", "hurt", "hurts", "kill", "kills", "eat", "eats", "crowd", "crowds", "die", "dies", "oxygen", "sunlight", "push", "algae", "lose", "loses"]},
  "invw": {"any": ["python", "pythons", "iguana", "iguanas", "lionfish", "pepper", "invasive"]}
}

L = {"id": "g3sci-31-01", "lesson": "31.01", "title": "What Threatens Florida Ecosystems?", "emoji": "🌊",
  "details": ["📅 Q4 · Unit 10 · Florida Ecosystems", "📖 Week 31 · Lesson 31.01", "🌎 CPALMS SC.3.N.1.7", "⏱ About 35 minutes"],
  "icans": ["name three major threats to Florida's ecosystems.", "explain how each threat affects plants and animals.", "describe ways people are working to protect Florida ecosystems."],
  "opti": {"warm": "Our film starts on a quiet morning in the Everglades, but something new is hiding there. First, inspect a mystery fish.",
           "lesson": "Today you're an ecologist. Follow runoff from a farm to a lake, run the Buffer Test, then take a road trip on the Threat Map.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Match each threat, then draw a Florida wetland with one threat in it."},
  "film": film, "scientist": "ecologist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Vltava (The Moldau), from Má vlast (Bedřich Smetana), Musopen, public domain recording (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The runoff movie, the Buffer Test, and the Threat Map are models; every place photo is real. The raccoon count in the film comes from a 2012 study that counted animals on Everglades roads where pythons had spread."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-31-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the fish, then tap three things you notice."},
  "how-31-01-compare": {"page": "Put the plant strip on one shore and the bare dirt on the other: drag them, or tap one, then a tray. Press Make it rain. Then swap.",
                        "say": "Put the plant strip on one shore and the bare dirt on the other: drag them, or tap one, then a tray. Press Make it rain. Then swap."},
  "how-31-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-31-01-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap the clue that shows the problem, then name the threat. Predict what could help, and see how people are fixing it."},
  "how-31-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"31-01-welcome": L["opti"]["warm"], "31-01-lesson": L["opti"]["lesson"], "31-01-check": L["opti"]["check"], "31-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
