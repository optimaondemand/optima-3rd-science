#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/25-01/lesson.json, how-lines.json, scripts.json (25.01: no voices recorded; scripts only)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
HS = json.load(open(f'{D}/hotspots.json')) if os.path.exists(f'{D}/hotspots.json') else None

def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s

film = {
  "id": "g3sci-25-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 25.01 · Why Do We Protect National Parks?",
  "title": "The First Park",
  "bigQuestion": "Why do people work hard to protect certain pieces of wild land?",
  "poster": "f_canyon", "endPoster": "f_today", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 6.0, "type": "archive", "img": "f_moran", "alt": "An old painting of a deep yellow and orange canyon with a tall waterfall and a river far below",
     "note": "Thomas Moran painted Yellowstone's canyon in 1872.", "fade": 0.8, "sfx": "whoosh", "sfxArg": 1.0},
    ph(9.4, 5.6, "f_canyon", "A rainbow in the mist below a huge waterfall in a yellow rock canyon", "Grand Canyon of the Yellowstone · Wyoming · Today",
       frm=(1.12, .5, .4), to=(1.0, .5, .5), fade=1.0),
    ph(15.0, 6.0, "f_bison", "A herd of bison standing in green grass with low mountains behind them", "Bison in Lamar Valley · Yellowstone National Park",
       frm=(1.0, .5, .5), to=(1.12, .55, .55)),
    {"t": 21.0, "d": 3.2, "type": "flash", "lines": ["A whole park?", "Just for nature?"], "beats": [0.15, 1.2], "fade": 0.15},
    ph(24.2, 5.0, "f_bird", "A pink roseate spoonbill flying with its wings spread against a blue sky", "A roseate spoonbill · Everglades National Park, Florida",
       frm=(1.5, .5, .5), to=(1.0, .5, .5), fade=0.6, sfx="whoosh", sfxArg=1.6),
    ph(29.2, 5.0, "f_glades", "Wide, flat sawgrass marsh dotted with dark tree islands, seen from an airplane", "The Everglades from the air · Florida",
       frm=(1.4, .5, .5), to=(1.0, .5, .5), fade=0.6),
    ph(34.2, 6.0, "f_space", "The southern tip of Florida seen from space, green and brown land wrapped in blue water", "South Florida from space · NASA satellite, 2023",
       frm=(1.35, .55, .62), to=(1.0, .5, .5), fade=0.6, count={"to": 60, "label": "miles wide", "dur": 3.0}, sfx="shimmer"),
    ph(40.2, 7.0, "f_today", "The sun sets in an orange sky over a flat, grassy marsh", "Shark Valley, Everglades National Park · Today",
       frm=(1.0, .5, .5), to=(1.08, .5, .55), fade=0.9, fx=["rays"]),
    {"t": 47.2, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.4, "text": "In 1872, an artist painted a wild canyon in Yellowstone.", "voice": "opti-1"},
    {"t": 9.8, "d": 5.0, "text": "That year, Yellowstone became the world's first national park.", "voice": "opti-2"},
    {"t": 15.3, "d": 5.4, "text": "Bison had almost disappeared. Inside the park, they were safe.", "voice": "opti-3"},
    {"t": 21.1, "d": 2.8, "text": "A whole park? Just for nature?", "voice": "opti-4"},
    {"t": 24.5, "d": 4.4, "text": "Far away in Florida, a spoonbill flies over the Everglades.", "voice": "opti-5"},
    {"t": 29.5, "d": 10.4, "text": "Zoom out. It lives in a river of grass, up to 60 miles wide.", "voice": "opti-6"},
    {"t": 40.6, "d": 6.2, "text": "So why do people work so hard to protect wild places like this?", "voice": "opti-7"}
  ]
}

spec_hs = HS or [{"name": "A pointed tip", "x": 0.5, "y": 0.2}, {"name": "Brown stripes", "x": 0.5, "y": 0.5}, {"name": "The round opening", "x": 0.5, "y": 0.8}, {"name": "A pale shell", "x": 0.2, "y": 0.5}]
specimen = {
  "img": "spec", "aspect": "1920/1141", "radius": 0.07, "hotspots": spec_hs,
  "kicker": "🔎 Mystery specimen", "title": "What are these striped shells?",
  "alt": "Three cone-shaped shells, cream colored with brown and pink stripes, lying on dark green cloth",
  "look": "A real photo of shells in a museum. Each one is about as long as your thumb. A specimen is one real thing that scientists study. Did these come from the sea? From a pond? Or from somewhere surprising? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the shells, then tap 3 things you notice.",
  "number": "No. 25.01-A",
  "card": ["<b>Specimen A</b>", "Found: in South Florida (now in a shell museum)", "Size: about 2 inches long", "Where did it live? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the shells)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🛡️", "protected land", "Land the government sets aside to keep wild and safe from harmful building."],
  ["🦋", "biodiversity", "The variety of different plants and animals living together in one place."],
  ["🏠", "habitat", "The natural home where a plant or animal finds food, water, and shelter."],
  ["🌱", "conservation", "Working to protect and care for nature so it stays healthy over time."],
  ["🕸️", "ecosystem", "All the living things in a place, plus the soil, water, and air they share."],
  ["⏳", "preserve", "To keep something safe and unchanged so it lasts for future generations."]
]

parts = [
  {"kicker": "🛡️ Part 1", "title": "What Is Protected Land?",
   "html": "<p>Some land in the United States is set aside by law. Nobody can build houses, factories, or farms there. These are protected lands.</p><p>National parks are one kind of protected land. People can visit and explore them, but the plants, animals, and water inside are kept safe from the kind of damage people can cause.</p>"},
  {"kicker": "🦋 Part 2", "title": "Why Biodiversity Matters",
   "html": "<p>A healthy ecosystem has many different kinds of living things. That variety is called biodiversity. Each species plays a role. Bees pollinate flowers. Owls eat mice. Decomposers break down dead leaves.</p><p>When one species disappears, others can be affected. A place with many kinds of living things is steadier and harder to break.</p>"},
  {"kicker": "🌱 Part 3", "title": "How Conservation Works",
   "html": "<p>Rangers and scientists work inside national parks. They count animals, pull out invasive plants, and reduce pollution. About half of the original Everglades was drained for farms and cities. Today much of what's left is protected, and scientists are slowly helping it recover.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Park Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start when the marsh is full of water.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does a gator hole save lives in the dry season?",
  "look": "Four real photos from the Everglades show how one alligator helps many animals, but they are mixed up. The wet season is the rainy part of the year. The dry season is when it hardly rains. A gator hole is a pond an alligator clears out. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "Tall grass standing in shallow water that shines orange under a setting sun", "text": "In the wet season, water covers the whole marsh.", "play": "Water everywhere.",
     "miss": ["", "The marsh is full of water first. Try frame 1.", "The alligator has nothing to clear yet. Try frame 1.", "This is where the story starts. Try frame 1."]},
    {"img": "o2", "alt": "A small pond surrounded by tall green grass and bushes in the Everglades", "text": "In the dry season, the water shrinks into a few low spots.", "play": "The water shrinks.",
     "miss": ["The marsh has to be full before it dries. Try a later frame.", "", "The water shrinks before the gator clears its hole. Try an earlier frame.", "The water shrinks first. Try an earlier frame."]},
    {"img": "o3", "alt": "A big alligator rests on the bank next to a small baby alligator", "text": "An alligator clears out a low spot, keeping a pond of water.", "play": "A gator keeps a pond.",
     "miss": ["The marsh has to dry out first. Try a later frame.", "The water shrinks before the gator clears its hole. Try a later frame.", "", "The gator makes the pond before animals crowd in. Try an earlier frame."]},
    {"img": "o4", "alt": "A great blue heron stands on a mangrove root while an alligator swims in the pond below", "text": "Fish, turtles, and birds crowd into the gator hole to survive.", "play": "Animals crowd in.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "A friend says, \"National parks are just for people to visit.\" What does the gator hole show?",
    "options": [
      {"t": "Parks are only for people to look around.", "miss": "Think about the gator hole. Who needs that water in the dry season?"},
      {"t": "Parks protect whole ecosystems, where animals depend on each other.", "ok": "Yes! People can visit, but the park protects the gators, fish, turtles, and birds that need each other to survive."}
    ]
  }
}

movie = {
  "model": "gator-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "swamp",
  "real": "real", "realAlt": "A round pond of water in a marsh seen from the air, with a trail of flattened grass leading to it",
  "stamp": "ONE GATOR HELPS", "endCap": "A real gator hole from the air.",
  "beats": [
    {"at": 0, "cap": "1 · Wet season: water everywhere.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["July"]},
    {"at": 2600, "cap": "2 · Dry season: water shrinks.", "model": {"show": "s2"}, "counter": ["January"]},
    {"at": 5200, "cap": "3 · A gator keeps a pond.", "model": {"show": "s3"}, "counter": ["March"]},
    {"at": 7800, "cap": "4 · Animals crowd in.", "model": {"show": "s4"}, "counter": ["April"], "sfx": "bubbles"},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Web Test", "title": "Which place can lose a species and stay healthy?",
  "look": "Two real places, each on a lit specimen tray. Specimen A is a Florida wetland where many kinds of birds feed together. Specimen B is a giant farm field where one kind of plant grows. A food web is a map of who eats whom. Under the trays are two model tests: scissors to snip one species out of the web, and a fence to keep people out.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "Pink spoonbills, white egrets, and wood storks feeding together in shallow water", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "Long, straight rows of green sugarcane fields stretching to the horizon, seen from an airplane", "label": "Specimen B"}
  ],
  "materials": [{"key": "snip", "label": "Scissors (snip one species)", "swatch": "scissors"}, {"key": "fence", "label": "Fence (keep people out)", "swatch": "fence"}],
  "ask": [
    {"q": "Which place has many kinds of living things?", "ans": "A", "ok": "Yes. Specimen A has spoonbills, egrets, storks, fish, and more.", "miss": "Look closely. Which one has lots of different birds?"},
    {"q": "Which place has mostly one kind of plant?", "ans": "B", "ok": "Yes. Specimen B is row after row of sugarcane.", "miss": "Look again. Which one has the same plant everywhere?"}
  ],
  "press": "✂️ Run the test",
  "testDo": "Put the scissors under one tray and the fence under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. Real food webs have thousands of links.",
  "results": {
    "Asnip": {"text": "One bird is snipped out. The web wobbles, but other animals still have food. The web holds.", "fx": "bend"},
    "Afence": {"text": "The fence keeps people out. The busy web stays busy.", "fx": "none"},
    "Bsnip": {"text": "One species is snipped out. With so few kinds, nothing fills its place, and the web falls apart.", "fx": "crush"},
    "Bfence": {"text": "A fence can't add missing species. The thin web stays thin.", "fx": "none"}
  },
  "best": ["Asnip", "Bsnip"],
  "frame": "This place has ___, so when one species is lost, its web ___.", "claimLead": "This place has", "claimMid": "so when one species is lost, its web",
  "claim": {
    "A": {"feat": ["many kinds of living things", "only a few kinds"], "featOk": 0, "eat": ["still holds", "falls apart"], "eatOk": 0},
    "B": {"feat": ["many kinds of living things", "only a few kinds"], "featOk": 1, "eat": ["still holds", "falls apart"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>High biodiversity → a strong web.</b> When one species is lost, others fill in.",
    "B": "<b>Low biodiversity → a weak web.</b> Losing one species can break it."
  },
  "missFeat": "Look at {label} again. Many kinds of living things, or just a few?",
  "missClaim": "Think about your test. Which web held when you snipped one species?",
  "done": "A place with many kinds of living things is steadier. That's one big reason people protect wild places with high biodiversity.",
  "after": {"kicker": "🎬 Behind the scenes · Only in South Florida", "img": "aft", "alt": "An American crocodile with a long, narrow snout resting on a gray rock by the water",
            "html": "South Florida is the only place in the world where American alligators and American crocodiles live side by side in the wild. Everglades and Biscayne National Parks protect both. Crocodiles like salty water near the coast; alligators like fresh water."}
}

wall = {
  "kicker": "🐠 The Reef Dive", "title": "Dive down through a protected ocean park",
  "look": "A model of one dive in Florida's ocean parks, from the surface down to a deep reef. Each stop has a real photo. A coral reef is a hard underwater structure built by tiny animals called corals. The brass dial on the left shows how deep you are.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the place shows.",
  "predict": {"q": "Is a protected ocean park home to just a few kinds of animals, or many?",
              "options": [["few", "Just a few kinds"], ["many", "Many kinds at every depth"]], "answer": "many",
              "mine": "Your prediction: <b>{p}</b>. Let's dive down and find out.",
              "confirm": "You predicted many kinds. The evidence agrees: different animals live at every depth, from the surface to the deep reef.",
              "change": "You predicted just a few kinds. The evidence changed that idea: different animals live at every depth, from the surface to the deep reef."},
  "sky": "sky", "skyAlt": "A six-sided brick fort on a small island ringed by bright blue-green water", "skyCap": "Fort Jefferson · Dry Tortugas National Park, Florida",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Above", "The<br>surface", "Seagrass", "Coral<br>reef", "Deep<br>reef"],
  "line": ["SURFACE", "DEEP REEF"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We dive down one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Dive deeper. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the line. Every depth has its own animals: snorkelers at the top, turtles in the seagrass, fish on the coral, and giant groupers in the deep. Protect the park, and you protect them all.",
  "rule": "<b>More kinds, more connections.</b> A protected ocean park keeps many habitats safe at once, from shallow seagrass to deep reefs. Fishing limits and no-anchor zones help the reef keep its biodiversity.",
  "choices": ["🤿 Clear, shallow water near the shore", "🐢 Seagrass meadows where turtles graze", "🪸 Corals that build a reef", "🐟 Giant fish on the deep reef"],
  "layers": [
    {"name": "Stop 1 · The surface", "rock": "water1", "img": "l1", "alt": "Calm, flat water of a bay reflecting a cloudy sky",
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "Biscayne National Park is almost all water. Its bay is shallow and clear, so sunlight reaches the bottom.",
     "ans": 0, "ok": "Yes! Clear, shallow water near the shore.", "tag": "🤿 Surface",
     "miss": {"1": "Not yet. We haven't dived down to the seagrass.", "2": "Not yet. The coral is deeper.", "3": "Not yet. The deep reef is far below."},
     "env": "e1", "envAlt": "A snorkeler in a mask and fins jumps into deep blue water", "envCap": "A snorkeler · Biscayne National Park, Florida"},
    {"name": "Stop 2 · Seagrass", "rock": "water2", "img": "l2", "alt": "A green sea turtle swims over a meadow of long, thin seagrass",
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "Seagrass grows in underwater meadows. Green sea turtles and manatees graze on it, and baby fish hide in it.",
     "ans": 1, "ok": "Yes! Seagrass meadows where turtles graze.", "tag": "🐢 Seagrass",
     "miss": {"0": "Look at the photo. What is the turtle swimming over?", "2": "Close! But is that coral, or grass?", "3": "Not yet. The deep reef is farther down."},
     "env": "e2", "envAlt": "A green sea turtle munching seagrass on a sandy bottom", "envCap": "A green sea turtle grazing · Akumal Bay, Mexico (stop photo: Bahamas)"},
    {"name": "Stop 3 · The coral reef", "rock": "water3", "img": "l3", "alt": "Branching tan elkhorn coral with small blue fish swimming over it",
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "Corals are tiny animals that build hard reefs. Elkhorn coral is shaped like antlers. Hundreds of kinds of fish live on Florida's reefs.",
     "ans": 2, "ok": "Yes! Corals that build a reef.", "tag": "🪸 Coral reef",
     "miss": {"0": "This is underwater now. Read the clue: what built this?", "1": "Close! But this isn't grass. Read the clue.", "3": "Not yet. Dive one more stop."},
     "env": "e3", "envAlt": "A school of big, bright blue parrotfish swimming over sand", "envCap": "Midnight blue parrotfish · Florida Keys National Marine Sanctuary"},
    {"name": "Stop 4 · The deep reef", "rock": "water4", "img": "l4", "alt": "A huge spotted goliath grouper swimming near the sea floor",
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "Goliath groupers can grow up to 8 feet long. So many were caught that catching them has been against the law since 1990. Now they are coming back.",
     "ans": 3, "ok": "Yes! Giant fish on the deep reef.", "tag": "🐟 Deep reef",
     "miss": {"0": "We're deep now. Read the clue: what lives down here?", "1": "Not a turtle. Look at the photo.", "2": "Close! But look at that giant fish."},
     "env": "e4", "envAlt": "Several huge goliath groupers gathered around a shipwreck on the sea floor", "envCap": "Goliath groupers · off Jupiter, Florida"}
  ],
  "mix": {
    "q": "A friend says, \"Losing one kind of fish from the reef doesn't matter.\" Is that right?",
    "options": [
      {"t": "Right. There are lots of other fish.", "miss": "Think about the Web Test. What happened when one species was snipped from a web?"},
      {"t": "No. Every species has a job, and losing one can affect others.", "ok": "Yes! Parrotfish keep algae off the coral, groupers eat other fish, and turtles trim the seagrass. Each one matters."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "The bison came back",
  "img": "wow", "alt": "A herd of bison grazing in a green valley with fog drifting over the dark forest behind them",
  "caption": "A bison herd on a foggy morning · Lamar Valley, Yellowstone National Park",
  "html": "<p style=\"margin:0 0 8px\">Millions of bison once roamed North America. Hunters killed so many that by the early 1900s, only about two dozen wild bison were left in Yellowstone.</p><p style=\"margin:0\">The park protected them and brought in more. Today thousands of bison roam Yellowstone. They're the only place in the United States where wild bison have lived since prehistoric times.</p>",
  "inset": "inset", "insetCap": "Bison grazing in Lamar Valley, Yellowstone."}

keyIdea = "Protecting land protects the whole ecosystem: the soil, water, plants, and animals that all depend on each other. Places with high biodiversity are steadier, so when people protect wild land, they help many species at once. Human choices can harm wild habitats, and human choices can protect them."

M = ["🌾 A wetland or swamp", "🌲 A forest or grassland", "🌊 An ocean or reef"]
SHORT = ["a wetland or swamp", "a forest or grassland", "an ocean or reef"]
def card(id_, img, alt, clues, orgAns, orgMiss, predict, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "predict": predict, "env": dict(predict["options"])[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss,
            "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}
Q = "Which living thing do you predict you'll find here?"
ALL = [["spoonbill", "🦩 A roseate spoonbill"], ["bison", "🦬 A herd of bison"], ["salamander", "🦎 A red-cheeked salamander"], ["reef", "🐠 Reef fish over coral"], ["panther", "🐆 A Florida panther"]]
def pr(*keys): return {"q": Q, "options": [o for o in ALL if o[0] in keys]}

det = {
  "look": "Five real national parks and preserves. Each card shows the land or water the park protects. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 parks, one at a time. Tap a clue, then pick its habitat. Predict a living thing you'll find, and watch it appear.",
  "noun": "Park", "need": 3, "inferQ": "What kind of habitat does it protect?", "inferDone": "Habitat", "chartSo": "where you'll find",
  "predict": {"q": Q, "options": ALL},
  "kicker": "Who lives here", "enough": "You already explored 3 parks. Nice work, park scientist!",
  "cols": ["Park", "My observation", "Habitat", "Living thing", "My evidence"],
  "write": {"label": "Park __ protects ___. I found ___, which needs this habitat because ___.", "starter": "Start with: \"Park __ protects…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["hab", "Names the habitat"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "A wooden boardwalk crosses a wet, grassy marsh under a bright sky",
         [{"t": "A boardwalk over shallow water and sawgrass", "ok": True}, {"t": "Snowy mountain peaks", "miss": "Look again. Is this land high and dry, or low and wet?"}, {"t": "Waves on a coral reef", "miss": "Look again. This is grass growing in water."}],
         0, "Shallow water and grass everywhere. Which habitat is that? Try again.",
         pr("spoonbill", "bison", "panther"), "spoonbill", "This wet, open marsh is full of wading birds. Try again.",
         "d1h", "A pink roseate spoonbill perched in green marsh plants", "Everglades National Park, Florida",
         "This spoonbill is evidence that the Everglades protects wading birds. More than 360 kinds of birds have been seen in the park.", "glades",
         "Everglades National Park opened in 1947. It protects the biggest subtropical wilderness in the United States."),
    card("B", "d2", "A wide green valley with a brown, winding river and mountains, seen from above",
         [{"t": "Open grassy valley between mountains", "ok": True}, {"t": "A coral reef", "miss": "Look again. This is dry land with a river."}, {"t": "A cypress swamp", "miss": "Look again. Are there swamp trees in water?"}],
         1, "Wide open grass between mountains. Which habitat is that? Try again.",
         pr("bison", "spoonbill", "reef"), "bison", "Big grazing animals need wide grasslands like this. Try again.",
         "d2h", "A herd of bison grazing on golden hills", "Lamar Valley, Yellowstone National Park, Wyoming",
         "These bison are evidence that Yellowstone protects big grazers. The park helped wild bison survive when they were nearly gone.", "valley",
         "Yellowstone became the world's first national park in 1872. Its valleys are home to bison, elk, wolves, and grizzly bears."),
    card("C", "d3", "Rows of misty mountain ridges covered in thick green forest",
         [{"t": "Mountains covered in thick, damp forest", "ok": True}, {"t": "Flat sawgrass", "miss": "Look again. Is this flat or full of mountains?"}, {"t": "Salt water", "miss": "Look again. These are tree-covered mountains."}],
         1, "Mountains covered in trees. Which habitat is that? Try again.",
         pr("salamander", "reef", "spoonbill"), "salamander", "Cool, damp forest floors are perfect for small animals that like moisture. Try again.",
         "d3h", "A small black salamander with red cheeks resting on a mossy log", "A red-cheeked salamander · Great Smoky Mountains National Park, Tennessee",
         "This salamander is evidence that the Smokies protect amazing biodiversity: about 30 kinds of salamanders live there.", "smokies",
         "The Great Smoky Mountains are called the Salamander Capital of the World. Red-cheeked salamanders live nowhere else on Earth."),
    card("D", "d4", "A small dark island on calm water under a glowing sunset sky",
         [{"t": "Calm salt water and a tiny island", "ok": True}, {"t": "A grassy valley", "miss": "Look again. Is this land or water?"}, {"t": "Tall pine trees", "miss": "Look again. Almost everything here is water."}],
         2, "Almost all water. Which habitat is that? Try again.",
         pr("reef", "panther", "bison"), "reef", "Under this water are coral reefs full of fish. Try again.",
         "d4h", "A snorkeler swims over branching elkhorn coral with fish", "Biscayne National Park, Florida",
         "This reef is evidence that Biscayne protects ocean life. About 95 percent of the park is water.", "reef",
         "Biscayne National Park sits right next to Miami. It protects mangrove shores, a shallow bay, and the start of Florida's coral reef."),
    card("E", "d5", "Tall, pale cypress trees standing in dark, still swamp water",
         [{"t": "Cypress trees growing in swamp water", "ok": True}, {"t": "A coral reef", "miss": "Look again. These are trees, not coral."}, {"t": "Snowy peaks", "miss": "Look again. This is warm and wet."}],
         0, "Trees growing in water. Which habitat is that? Try again.",
         pr("panther", "salamander", "bison"), "panther", "This big swamp is home to one of Florida's rarest cats. Try again.",
         "d5h", "A tan Florida panther sitting among green palmetto leaves", "A Florida panther (swamp photo: Big Cypress National Preserve, Florida)",
         "This panther is evidence that big protected places matter. Panthers need huge areas to hunt, and Big Cypress gives them room.", "cypress",
         "In 1974, Big Cypress became one of the first two national preserves. Only a couple hundred Florida panthers are left, and many live in and around it."),
  ]
}

rebuild = {"title": "Use your evidence to rebuild the place", "missPrefix": "Hmm. Look at your park again. ", "kicker": "🌍 Rebuild the place", "whyStart": "I chose this because the park…",
  "envs": [
    {"key": "glades", "name": "🌾 A sawgrass marsh", "img": "d1h", "cap": "Flat, wet, and wide…"},
    {"key": "valley", "name": "🏞️ A mountain valley", "img": "d2h", "cap": "Grass and rivers…"},
    {"key": "smokies", "name": "🌲 A misty mountain forest", "img": "d3h", "cap": "Damp and green…"},
    {"key": "reef", "name": "🪸 A coral reef", "img": "d4h", "cap": "Clear salt water…"},
    {"key": "cypress", "name": "🌳 A cypress swamp", "img": "d5h", "cap": "Tall trees in water…"}
  ],
  "life": [
    {"name": "🐊 Alligators", "img": "d1h", "env": "glades", "miss": "Alligators live in the Everglades marsh."},
    {"name": "🐺 Gray wolves", "img": "d2h", "env": "valley", "miss": "Gray wolves hunt in Yellowstone's valleys."},
    {"name": "🐻 Black bears", "img": "d3h", "env": "smokies", "miss": "Black bears live in the Smokies' forests."},
    {"name": "🐢 Sea turtles", "img": "d4h", "env": "reef", "miss": "Sea turtles swim over the reef and seagrass."},
    {"name": "🦉 Barred owls", "img": "d5h", "env": "cypress", "miss": "Barred owls call from the cypress swamp."}
  ]}

quiz = [
  {"q": "What is biodiversity?", "options": [
    {"t": "The number of people who visit a national park each year", "miss": "Biodiversity is about how many different kinds of living things share a space."},
    {"t": "The variety of different plants and animals living in one place", "ok": "🌿 That's it! Biodiversity means variety: many different kinds of living things sharing the same place."},
    {"t": "The amount of rainfall a forest receives each year", "miss": "Biodiversity is about how many different kinds of living things share a space."}]},
  {"q": "What most likely happens when a wild habitat is destroyed?", "options": [
    {"t": "Animals find more food because there's more open space", "miss": "Think about what animals need from their habitat: food, water, and shelter. What happens when those are gone?"},
    {"t": "Biodiversity in that area increases", "miss": "Think about what animals need from their habitat: food, water, and shelter. What happens when those are gone?"},
    {"t": "Animals lose shelter and food, so some species may disappear", "ok": "🌲 Exactly right. When habitat is destroyed, animals lose the things they need, and some can't survive without them."}]},
  {"q": "Which of these is the best example of conservation?", "options": [
    {"t": "Rangers monitoring and protecting a wetland from pollution", "ok": "⭐ Yes! Conservation means working to protect and care for nature. Monitoring a wetland is exactly that kind of work."},
    {"t": "Cutting down trees to build a new road through a forest", "miss": "Conservation means protecting nature and keeping it healthy. Which choice does that, instead of changing or removing the wild place?"},
    {"t": "Draining a swamp to create more farmland", "miss": "Conservation means protecting nature and keeping it healthy. Which choice does that, instead of changing or removing the wild place?"}]}
]

def hh(n, q, helps, ok, miss):
    o = [{"t": "Helps the ecosystem"}, {"t": "Harms the ecosystem"}]
    o[0 if helps else 1]["ok"] = ok; o[1 if helps else 0]["miss"] = miss
    return {"n": n, "q": q, "type": "choice", "options": o}

partA = {"title": "Sort the actions", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  hh(1, "A ranger removes invasive plants that are crowding out native wildflowers.", True, "Yes. Native wildflowers get their space back.", "Look again. Does removing invasive plants help or harm the native ones?"),
  hh(2, "A developer drains a wetland to build a shopping center.", False, "Right. Draining a wetland destroys a habitat.", "Look again. What happens to the animals when the wetland is drained?"),
  hh(3, "Scientists track wolf populations to make sure the forest ecosystem stays balanced.", True, "Yes. Tracking helps people protect the whole ecosystem.", "Look again. Does watching over wolves help or harm the forest?"),
  hh(4, "A logging company cuts down a large section of old-growth trees.", False, "Right. Cutting old forest removes homes for many animals.", "Look again. What happens to animals that live in those old trees?"),
  {"n": 5, "q": "Pick your most important choice above. In one sentence, explain why.", "type": "text", "min": 8, "chips": [["because", "Gives a reason (because, so)"]]}
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Explain what a national park is and name one reason why protected land matters for animals.", "type": "text", "min": 12, "chips": [["park", "Says what a national park is"], ["because", "Gives a reason (because, so)"]]},
    {"n": 2, "q": "Why is high biodiversity a sign of a healthy ecosystem? Give one example from what you learned today.", "type": "text", "min": 12, "chips": [["bio", "Uses biodiversity or many kinds"], ["because", "Gives a reason (because, so)"]]}
  ]},
  "write": {"title": "Is it worth protecting wild land, even if people can't build or farm there?", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["biodiversity", "ecosystem", "conservation", "protected land", "habitat", "preserve"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think protecting wild land is important because…\""],
                ["What did you learn that supports your thinking?", "Start with: \"I know this because the lesson showed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because…\""]]},
  "partC": {"do": "Draw a national park scene with at least 2 zones, like a marsh and a forest. Label a living thing in one zone, and one action that protects it.",
            "labels": ["A zone and a living thing that lives there", "One action that protects that zone"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 parks and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all five answers.", "req": {"choice": ["a1", "a2", "a3", "a4"], "text": {"in-a5": 8}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my park story", "thinkLabel": "It protects", "director": "JUNIOR PARK SCIENTIST", "storyKicker": "My park story",
  "frames": [
    {"k": "formation", "label": "The gator hole", "img": "o3", "cap": "The gator hole: one alligator keeps water for many animals."},
    {"k": "compare", "label": "The Web Test", "img": "ta", "cap": "The Web Test: many kinds of living things make a strong web."},
    {"k": "wall", "label": "The Reef Dive", "img": "l3", "cap": "The Reef Dive: different animals at every depth."},
    {"k": "det", "label": "Park files", "img": "d1h", "cap": "Park files: each park protects its own habitat."}]}

nxt = {"title": "25.02 · Investigation: Protect a Park Proposal", "text": "Next time, find a real threat to a park habitat and write a plan to protect it."}

chips = {
  "part": {"any": ["stripe", "stripes", "striped", "brown", "pink", "cream", "white", "tip", "point", "pointy", "pointed", "opening", "hole", "shell", "shells", "spiral", "swirl", "shiny", "cone", "lines"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["boardwalk", "water", "grass", "sawgrass", "marsh", "valley", "river", "mountains", "forest", "trees", "island", "sunset", "cypress", "swamp", "misty", "green"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "hab": {"any": ["wetland", "swamp", "marsh", "forest", "grassland", "ocean", "reef", "habitat"]},
  "park": {"any": ["protected", "protect", "protects", "land", "law", "safe", "nature", "wild"]},
  "bio": {"any": ["biodiversity", "many", "kinds", "variety", "species", "different"]}
}

L = {"id": "g3sci-25-01", "lesson": "25.01", "title": "Why Do We Protect National Parks?", "emoji": "🏞️",
  "details": ["📅 Q3 · Unit 8 · Human Impact &amp; Conservation", "📖 Week 25 · Lesson 25.01", "🌎 CPALMS SC.3.N.1.7 · NGSS 3-LS4-4", "⏱ About 35 minutes"],
  "icans": ["explain what protected land is and give an example.", "describe how biodiversity helps a habitat stay healthy.", "explain how human choices can harm or help wild habitats."],
  "opti": {"warm": "Our film starts with a painting from 1872 and ends in a river of grass. First, inspect some striped shells.",
           "lesson": "Today you're a park scientist. Watch a gator save the day, test two food webs, then dive down a reef.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Sort some actions, then tell us whether wild land is worth protecting."},
  "film": film, "scientist": "park scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: \"America the Beautiful\" (Samuel A. Ward), played by \"The President's Own\" United States Marine Band in the 1950s, public domain (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The gator-hole movie, the Web Test, and the Reef Dive are models; every place photo is real."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-25-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the shells, then tap three things you notice."},
  "how-25-01-compare": {"page": "Put the scissors under one tray and the fence under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the scissors under one tray and the fence under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-25-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-25-01-det": {"page": det["do"], "say": "Pick three parks, one at a time. Tap a clue, then pick its habitat. Predict a living thing you'll find, and watch it appear."},
  "how-25-01-partc": {"page": assign["partC"]["do"], "say": "Draw a national park scene with at least two zones, like a marsh and a forest. Label a living thing in one zone, and one action that protects it."}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"25-01-welcome": L["opti"]["warm"], "25-01-lesson": L["opti"]["lesson"], "25-01-check": L["opti"]["check"], "25-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
