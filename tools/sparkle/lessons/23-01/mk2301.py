#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/23-01/lesson.json, how-lines.json, credits.json, scripts.json."""
import json
D = '/home/claude/optima-3rd-science/tools/sparkle/lessons/23-01'

def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s

def arc(t, d, img, alt, note, **kw):
    s = {"t": t, "d": d, "type": "archive", "img": img, "alt": alt, "note": note, "fade": 0.8}
    s.update(kw); return s

film = {
  "id": "g3sci-23-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 23.01 · Pollution",
  "title": "Then & Now",
  "bigQuestion": "What happens to the plants and animals in an ecosystem when the air, water, and land around them get polluted?",
  "poster": "f_smog", "endPoster": "f_birds", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.6},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    arc(3.4, 5.8, "f_smog", "Tall buildings of Manhattan half hidden in thick, yellow-gray smog", "New York City, May 1973 · EPA photo", sfx="whoosh", sfxArg=0.6),
    arc(9.2, 5.2, "f_river", "A shiny slick of oil spreading on a river beside a floating boom", "An oil slick on the San Juan River, Utah, 1972 · EPA photo"),
    arc(14.4, 5.0, "f_dump", "Paper, cans and trash scattered across an open dump", "An open dump near Denver, Colorado, 1972 · EPA photo"),
    {"t": 19.4, "d": 3.4, "type": "flash", "lines": ["A brown sky?", "Over a city?"], "beats": [0.15, 1.3], "fade": 0.15},
    {"t": 22.8, "d": 7.0, "type": "reveal", "img": "f_clear", "alt": "The Manhattan skyline and the Brooklyn Bridge glowing at dusk under a clear sky",
     "from": [1.0, .5, .5], "to": [1.08, .5, .5], "revealAt": 0.6, "revealDur": 4.6, "place": "The same city today · New York City", "fade": 0.6},
    ph(29.8, 5.4, "man", "A gray Florida manatee gliding through clear water with small fish around it", "A manatee in clear spring water · Crystal River, Florida", frm=(1.12, .5, .5), to=(1.0, .5, .5), fx=["caustics"]),
    ph(35.2, 6.6, "f_birds", "A wood stork and a glossy ibis standing in green wetland grass", "A wood stork and a glossy ibis · Green Cay Wetlands, Florida", frm=(1.0, .5, .5), to=(1.06, .5, .5), fade=0.9, sfx="shimmer", contain=True),
    {"t": 41.8, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.0, "text": "In 1973, a whole city disappears into smog.", "voice": "opti-1"},
    {"t": 9.5, "d": 4.5, "text": "A river shines with spilled oil.", "voice": "opti-2"},
    {"t": 14.7, "d": 4.4, "text": "Trash blows across the land.", "voice": "opti-3"},
    {"t": 19.5, "d": 3.1, "text": "A brown sky? Over a city?", "voice": "opti-4"},
    {"t": 24.2, "d": 5.2, "text": "Today, the same city stands under a clearer sky.", "voice": "opti-5"},
    {"t": 30.2, "d": 4.8, "text": "And in a clear Florida spring, a manatee glides by.", "voice": "opti-6"},
    {"t": 35.6, "d": 5.8, "text": "So what happens to living things when air, water, and land get polluted?", "voice": "opti-7"}
  ]
}

specimen = {
  "img": "spec", "aspect": "1400/1867", "radius": 0.07,
  "hotspots": [
    {"name": "A pink and white crust: the lichen", "x": 0.45, "y": 0.6},
    {"name": "A bright red rim at its edge", "x": 0.76, "y": 0.37},
    {"name": "A thin twig lying across it", "x": 0.35, "y": 0.25},
    {"name": "A different lichen, pale green and leafy", "x": 0.78, "y": 0.93},
    {"name": "Dark, rough tree bark", "x": 0.86, "y": 0.5},
    {"name": "A curly vine tendril", "x": 0.16, "y": 0.75}
  ],
  "kicker": "🔎 Mystery specimen", "title": "What is growing on this tree?",
  "alt": "A pink and white crusty lichen with a red rim growing on dark tree bark, with a twig, a curly vine and a small pale green leafy lichen",
  "look": "A real photo of a tree trunk, seen very close up. Something pink and white is growing right on the bark. A specimen is one real thing that scientists study. Is it a plant? A paint spill? Something else? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the tree bark, then tap 3 things you notice.",
  "number": "No. 23.01-A",
  "card": ["<b>Specimen A</b>", "Found: on a tree at Lake Louisa State Park, Florida", "Size: patches like this are often a few inches across", "What is it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the bark)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🏭", "pollution", "Harmful materials that get into the air, water, or land and hurt living things."],
  ["🌿", "ecosystem", "All the living things in a place, like plants, animals, and insects, plus their surroundings."],
  ["🌲", "habitat", "The natural place where a plant or animal lives and finds everything it needs to survive."],
  ["🗑️", "land pollution", "Trash, chemicals, or waste left on the ground that harms soil and the creatures living in it."],
  ["💧", "water pollution", "Harmful materials, like oil, plastic, or chemicals, that get into rivers, lakes, or oceans."],
  ["💨", "air pollution", "Smoke, dust, or gases in the air, often from cars and factories, that make it unhealthy to breathe."]
]

parts = [
  {"kicker": "🌱 Part 1", "title": "What Is Pollution?",
   "html": "<p>Pollution happens when harmful stuff ends up somewhere it doesn't belong. There are three main types.</p><p><b>Land pollution</b> is trash and chemicals left on the ground. <b>Water pollution</b> is oil, plastic, or waste in rivers and oceans. <b>Air pollution</b> is smoke and gases that make the air unhealthy to breathe. Each type can damage the living things nearby.</p>"},
  {"kicker": "🌤 Part 2", "title": "How Does Pollution Hurt Living Things?",
   "html": "<p>Every living thing needs clean water, clean air, and healthy soil to survive. When pollution gets into an ecosystem, it can make animals sick and destroy habitats.</p><p>Fish die in rivers full of chemicals. Birds get tangled in floating plastic. Trees weaken when acid from smoky air soaks into the soil. Even small amounts of pollution can cause big problems over time.</p>"},
  {"kicker": "🌍 Part 3", "title": "Why Do Ecosystems Need Our Help?",
   "html": "<p>Humans cause most pollution, from factories, cars, farming, and trash. But humans can fix it, too. Laws set limits on how much pollution factories can release. More than 400 national park sites protect wild places. Scientists clean up oil spills, plant trees, and restore rivers.</p><p>In the Chesapeake Bay, decades of teamwork by scientists, governments, and everyday people cut water pollution and helped bring back striped bass. The work is still going.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Pollution Detective: Then & Now"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start where the fertilizer goes on.",
  "kicker": "🎞️ Put the scenes in order", "title": "How can a farm field turn a lake green?",
  "look": "Four real photos, from different places. Each one shows one step of the same trip, but they are mixed up. Fertilizer is plant food that farmers spread on fields. Algae are tiny green living things that grow in water. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "A tractor with long arms spreading fertilizer across a brown field", "text": "A farmer spreads fertilizer on a field.", "play": "Fertilizer on the field.",
     "miss": ["", "The fertilizer has to go on the field first. Try frame 1.", "Nothing can wash away yet. Try frame 1.", "The field comes first. Try frame 1."]},
    {"img": "o2", "alt": "Muddy rainwater rushing off the edge of a farm field into a ditch", "text": "Rain washes the extra fertilizer off the field.", "play": "Rain washes it away.",
     "miss": ["The fertilizer has to be spread before rain can wash it. Try a later frame.", "", "The rain carries it to the lake. Try an earlier frame.", "The rain comes before the fish. Try an earlier frame."]},
    {"img": "o3", "alt": "Lake Okeechobee seen from space, with swirls of bright green algae across the water", "text": "In the lake, the fertilizer feeds algae, and the water turns green.", "play": "The lake turns green.",
     "miss": ["The lake turns green after the fertilizer gets there. Try a later frame.", "The rain has to carry the fertilizer first. Try a later frame.", "", "The lake turns green before the fish die. Try an earlier frame."]},
    {"img": "o4", "alt": "Hundreds of dead fish lying along a sandy shoreline", "text": "The algae use up the water's oxygen, and fish die.", "play": "Fish can't breathe.",
     "miss": ["This is where the trip ends. Try frame 4.", "This is where the trip ends. Try frame 4.", "This is where the trip ends. Try frame 4.", ""]}
  ],
  "check": {
    "q": "The fertilizer was spread on a farm field, miles from the lake. Can it really harm the fish in that lake?",
    "options": [
      {"t": "No. Pollution only harms the spot where it starts.", "miss": "Think about the movie. What carried the fertilizer, and where did it end up?"},
      {"t": "Yes. Rain can carry it into streams and lakes far away.", "ok": "Yes! Pollution travels. Rain carried the fertilizer from the field all the way to the lake, where it harmed the fish."}
    ]
  }
}

movie = {
  "model": "algae-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "water",
  "real": "real", "realAlt": "Bright green swirls of algae spreading across a lake, seen from an airplane",
  "stamp": "POLLUTION TRAVELS", "endCap": "A real algae bloom on Lake Erie.",
  "beats": [
    {"at": 0, "cap": "1 · Fertilizer goes on a farm field.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Day 1"]},
    {"at": 2600, "cap": "2 · Rain washes it into a canal.", "model": {"show": "s2"}, "counter": ["Day 2"]},
    {"at": 5200, "cap": "3 · Algae grow, and the lake turns green.", "model": {"show": "s3"}, "counter": ["Day 10"]},
    {"at": 7800, "cap": "4 · The fish run out of oxygen.", "model": {"show": "s4"}, "counter": ["Day 20"], "sfx": "bubbles"},
    {"at": 10400, "cap": "The real thing: a lake turned green.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🔦 The Light Test", "title": "Can sunlight reach the bottom?",
  "look": "Two real kinds of water, each on a lit specimen tray. Specimen A is a clear Florida spring. Specimen B is a lake thick with green algae. Seagrass and other water plants grow on the bottom, and they need sunlight. Under the trays are two things for a test: a flashlight that stands in for the sun, and a clear cup for scooping water.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "Clear blue-green spring water with a sandy bottom you can see", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "Thick bright green algae floating on a lake near the shore", "label": "Specimen B"}
  ],
  "materials": [{"key": "torch", "label": "Flashlight", "swatch": "torch"}, {"key": "cup", "label": "Clear cup", "swatch": "cup"}],
  "ask": [
    {"q": "Which water is so clear you can see the bottom?", "ans": "A", "ok": "Yes. Specimen A, the spring, is clear all the way down.", "miss": "Look closely. In which one can you see sand on the bottom?"},
    {"q": "Which water is thick with tiny green algae?", "ans": "B", "ok": "Yes. Specimen B is full of green algae.", "miss": "Look again. Which one is bright green?"}
  ],
  "press": "🔦 Shine the light",
  "testDo": "Put the flashlight under one tray and the cup under the other: drag them, or tap one, then a tray. Press <b>Shine the light</b>. Then swap and try again.",
  "disclaimer": "This is a model. A flashlight stands in for the sun.",
  "results": {
    "Atorch": {"text": "The light shines all the way to the bottom. Seagrass down there gets the sunlight it needs.", "fx": "glow"},
    "Acup": {"text": "The cup just fills with clear water. Try the flashlight to test the light.", "fx": "none"},
    "Btorch": {"text": "The green algae block the light. Almost none reaches the bottom, so seagrass there can't grow.", "fx": "shade"},
    "Bcup": {"text": "The cup fills with green water. Try the flashlight to see what the algae do to light.", "fx": "none"}
  },
  "best": ["Atorch", "Btorch"],
  "frame": "This one has ___, so it ___.", "claimLead": "This one has", "claimMid": "so it",
  "claim": {
    "A": {"feat": ["clear water", "water thick with green algae"], "featOk": 0, "eat": ["lets sunlight reach the bottom", "blocks the sunlight"], "eatOk": 0},
    "B": {"feat": ["clear water", "water thick with green algae"], "featOk": 1, "eat": ["lets sunlight reach the bottom", "blocks the sunlight"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Clear water → light reaches the bottom.</b> Seagrass grows, and animals that eat it have food.",
    "B": "<b>Algae → the light is blocked.</b> Seagrass on the bottom dies in the dark."
  },
  "missFeat": "Look at {label} again. Is the water clear, or thick and green?",
  "missClaim": "Think about your test. Which water let the light through, and which one blocked it?",
  "done": "Algae blooms block sunlight. Without light, seagrass dies, and the animals that eat it go hungry.",
  "after": {"kicker": "🎬 Behind the scenes · Hungry manatees", "img": "man", "alt": "A gray Florida manatee swimming in clear water with small fish around it",
            "html": "Manatees eat seagrass. In 2021, algae blooms in Florida's Indian River Lagoon blocked the sunlight, and much of the seagrass there died. Many manatees went hungry. Scientists say cutting the pollution that feeds algae is the way to bring the seagrass back. (Photo: a manatee at Crystal River, Florida.)"}
}

wall = {
  "kicker": "🕰️ One river, then and now", "title": "Travel through time on the Androscoggin River",
  "look": "A model of one real river's story, like a timeline turned on its side. The Androscoggin River runs through Maine and New Hampshire. Each stop has a real photo from its past or present. The brass dial on the left shows where you are in its story.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the place shows.",
  "predict": {"q": "Once a river is badly polluted, can it ever get clean again?",
              "options": [["yes", "Yes, if people work to fix it"], ["no", "No, it stays polluted forever"]], "answer": "yes",
              "mine": "Your prediction: <b>{p}</b>. Let's travel through the river's story and find out.",
              "confirm": "You predicted it can get clean again. The evidence agrees: new laws and cleanup brought people back to fish and boat on the river.",
              "change": "You predicted it stays polluted forever. The evidence changed that idea: new laws and cleanup brought people back to fish and boat on the river."},
  "sky": "sky", "skyAlt": "White water rushing over the Great Falls of the Androscoggin River beside old brick mill buildings", "skyCap": "The Great Falls of the Androscoggin River today · Lewiston, Maine",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Start", "Foam", "Trash", "New laws", "Today"],
  "line": ["THEN: THE 1970s", "NOW: TODAY"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We travel through time one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Moving forward in time. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the line. In the 1970s the river was full of foam and trash. After new laws and years of cleanup, people fish and boat on it today.",
  "rule": "<b>Pollution can be fixed.</b> When people make rules and work together, a damaged ecosystem can get healthier again. Some parts of this river still need help, so the work goes on.",
  "choices": ["🫧 Foam and chemicals in the water", "🔥 Trash burned right by the river", "📜 A new law to clean the water", "🎣 People fishing on a cleaner river"],
  "layers": [
    {"name": "Stop 1 · Foam on the river", "rock": "redbed", "img": "l1", "alt": "Thick foam floating on a dark river below a bridge, in an old faded photo",
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "In the 1960s and 1970s, paper mills and towns dumped waste into this river. Foam drifted on the water, and there was so little oxygen that fish couldn't live.",
     "ans": 0, "ok": "Yes! Foam and chemicals filled the water.", "tag": "🫧 Foam",
     "miss": {"1": "Look at the water. What is floating on it?", "2": "Not yet. This is before the new law.", "3": "Look again. Could fish live in this water?"},
     "env": "e1", "envAlt": "The Androscoggin River flowing past Lewiston Falls on a cloudy day", "envCap": "The same river today · Lewiston, Maine (photo 1973 above)"},
    {"name": "Stop 2 · A dump on the bank", "rock": "mudstone", "img": "l2", "alt": "Smoke rising from burning trash at a dump, in an old faded photo",
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "In 1973, a town dump on the river's bank burned its trash. Smoke went into the air, and trash could wash into the water.",
     "ans": 1, "ok": "Yes! Trash was dumped and burned right by the river.", "tag": "🔥 Trash",
     "miss": {"0": "Look at the photo. Is this water or land?", "2": "Not yet. Look at what is burning.", "3": "Look again. Is anyone fishing here?"},
     "env": "e2", "envAlt": "A town and green hills along the Androscoggin River, seen from above", "envCap": "The river valley today · Berlin, New Hampshire (photo 1973 above, nearby Gorham)"},
    {"name": "Stop 3 · New laws", "rock": "sandstone", "img": "l3", "alt": "Two photos side by side of the same city by a river, one from 1973 and one from 2012",
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "In 1972, Senator Edmund Muskie, who grew up by this river, led Congress to pass the Clean Water Act. Now factories need permission before they put anything into a river.",
     "ans": 2, "ok": "Yes! A new law to clean the water.", "tag": "📜 New laws",
     "miss": {"0": "Look at both photos. What changed between them?", "1": "There's no dump here. Read the clue.", "3": "Close! But read the clue: what happened in 1972?"},
     "env": "e3", "envAlt": "A wide, calm river with bare trees and blue mountains behind it", "envCap": "The river in early spring · Bethel, Maine (the photo above shows Lewiston-Auburn in 1973 and 2012)"},
    {"name": "Stop 4 · Today", "rock": "water1", "img": "l4", "alt": "People fishing from a small drift boat on a calm river edged with green trees",
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "Today people boat and fish on the river, and some places are clean enough to swim. Some parts still need extra help, so people keep working on it.",
     "ans": 3, "ok": "Yes! People fish on a cleaner river.", "tag": "🎣 Today",
     "miss": {"0": "Look at the water. Is there foam?", "1": "No trash here. What are the people doing?", "2": "This is after the law. What are people doing now?"},
     "env": "e4", "envAlt": "A calm, dark blue river lined with green trees under a blue sky", "envCap": "The Androscoggin River today · near Berlin, New Hampshire"}
  ],
  "mix": {
    "q": "A stream looks clear and clean. Could it still be polluted?",
    "options": [
      {"t": "No. If I can't see any pollution, it isn't there.", "miss": "Think about the fertilizer in the movie. Could you see it in the water before the algae grew?"},
      {"t": "Yes. Some pollution, like fertilizer, is invisible, so scientists test the water.",
       "ok": "Yes! You can't always see pollution. Scientists test water and air to find what our eyes miss."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Parks that watch the air",
  "img": "wow", "alt": "Rows of forested blue mountains under a clear sky with a grassy field in front",
  "caption": "Great Smoky Mountains National Park, Tennessee and North Carolina",
  "html": "<p style=\"margin:0 0 8px\">The United States has more than 400 national park sites, and scientists check the air in many of them every day. At stations like Look Rock in Great Smoky Mountains National Park, machines measure smoke, haze, and acid in the rain.</p><p style=\"margin:0\">After new clean-air laws in 1990, power plants and cars put out much less of the gases that make haze and acid rain. Mountains in the Smokies that haze used to hide are now easier to see.</p>",
  "inset": "inset", "insetCap": "The Look Rock air quality station."}

keyIdea = "Pollution harms ecosystems by making the air, water, and land unsafe for living things. When the environment is polluted, plants and animals can't get what they need to survive. A single pollution source can affect many parts of an ecosystem at once, but people can take action to reduce the harm."

ORG = None
def card(id_, img, alt, clues, org, orgAns, orgShort, orgMiss, env, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": org, "orgAns": orgAns, "orgShort": orgShort, "orgMiss": orgMiss,
            "env": env, "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}

det = {
  "look": "Five real pollution scenes from the past. Each one matches a scenario a pollution detective would study. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 scenes, one at a time. Tap a clue, then pick who is harmed. Predict land, water, or air, and watch the place today appear.",
  "noun": "Scene", "need": 3, "inferQ": "Who or what is harmed?", "inferDone": "Harmed", "chartSo": "so it harms",
  "predict": {"q": "Is this land, water, or air pollution?", "options": [["land", "🗑️ Land pollution"], ["water", "💧 Water pollution"], ["air", "💨 Air pollution"]]},
  "kicker": "The place today", "enough": "You already solved 3 scenes. Nice work, pollution detective!",
  "cols": ["Scene", "My observation", "Who is harmed", "Type", "My evidence"],
  "write": {"label": "Scene __ shows ___. It is ___ pollution because ___.", "starter": "Start with: \"Scene __ shows…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["because", "Gives a reason (because)"], ["type", "Says land, water, or air"]]},
  "items": [
    card("A", "d1", "Cars on a highway in front of a steel plant whose tall chimneys pour smoke into a hazy sky",
         [{"t": "Smoke pouring from tall chimneys", "ok": True}, {"t": "Oil floating on water", "miss": "Look again. Is there water in this photo?"}, {"t": "Tires dumped in a field", "miss": "Look again. What is coming out of the chimneys?"}],
         ["Trees, birds, and people who breathe this air", "Fish in the deep ocean", "Worms in a farm field far away"], 0, "trees, birds, and people who breathe it",
         "Smoke spreads through the air. Who breathes that air? Try again.",
         "Air", "air", "The smoke rises into the sky, so it pollutes the air. Try again.",
         "d1h", "Tall city buildings and a green park under a clear blue sky", "Today: the same city under a clearer sky · Birmingham, Alabama, 2016 (smoke photo 1972)",
         "This clearer sky is evidence that cleaner factories and clean-air laws can clear the air.", "city",
         "Scenario 1 asks about a factory pouring smoke over a forest and a town. This 1972 photo shows steel mills in Birmingham, Alabama. The Clean Air Act of 1970 set limits on smoke, and mills got cleaner or closed."),
    card("B", "d2", "Yellow, white and red plastic bottle caps tangled in dark dried seaweed on a beach",
         [{"t": "Plastic caps in the seaweed", "ok": True}, {"t": "Smoke in the sky", "miss": "Look again. There's no smoke. What is in the seaweed?"}, {"t": "Fresh sea shells", "miss": "Look again. Are those shells, or plastic?"}],
         ["Seabirds and sea turtles that swallow plastic", "Cows on a farm", "Trees on a mountain"], 0, "seabirds and sea turtles",
         "Animals that live at sea can mistake plastic for food. Try again.",
         "Water", "water", "The plastic floats in the ocean, so it pollutes the water. Try again.",
         "d2h", "A green sea turtle swimming at the surface of blue ocean water", "Today: a green sea turtle swimming free · Cape Canaveral, Florida",
         "This healthy turtle is evidence that keeping plastic out of the sea protects ocean animals.", "ocean",
         "Scenario 2 asks about plastic washing out to sea. Scientists estimated in 2015 that about 8 million tons of plastic reach the ocean each year, like a garbage truck full of plastic every minute. Beach cleanups and less plastic trash help. (Photo: caps on a beach in France.)"),
    card("C", "d3", "A pile of old black tires dumped beside a road in dry, brushy land",
         [{"t": "Old tires dumped on the ground", "ok": True}, {"t": "Foam on a river", "miss": "Look again. Is there a river here?"}, {"t": "Smoke from chimneys", "miss": "Look again. What is lying on the ground?"}],
         ["Soil and the small animals that live in it", "Fish in the ocean", "Birds high in the clouds"], 0, "soil and the small animals in it",
         "Rain soaks through dumped trash into the soil. Who lives there? Try again.",
         "Land", "land", "The tires sit on the ground, so they pollute the land. Try again.",
         "d3h", "Sagebrush and green hills on open public land with a few tires left to pick up", "Today: volunteers pulled 200 tires off public land · eastern Oregon, 2019",
         "This cleaner land is evidence that a cleanup can take land pollution away.", "public",
         "Scenario 3 asks about old tires dumped near a meadow. This tire dump sat near the Oregon Badlands Wilderness. On Earth Day 2019, volunteers removed 200 tires from public land in eastern Oregon."),
    card("D", "d4", "Brown pelicans coated in dark oil, sitting on rocks at the water's edge",
         [{"t": "Birds coated in dark oil", "ok": True}, {"t": "Trash in a field", "miss": "Look again. What is on the birds' feathers?"}, {"t": "A smoky sky", "miss": "Look again. Look at the birds' feathers."}],
         ["Seabirds like pelicans", "Deer in a forest", "Cactus in a desert"], 0, "seabirds like pelicans",
         "Oil coats the feathers of birds that live by the sea. Try again.",
         "Water", "water", "The oil spilled into the sea, so it pollutes the water. Try again.",
         "d4h", "A clean brown pelican standing in a pen after being washed", "After cleaning: a brown pelican, ready to return to the wild (2010)",
         "This clean pelican is evidence that people can help animals recover from an oil spill.", "gulf",
         "Scenario 4 asks about oil leaking into the ocean. In 2010, an oil well blew out in the Gulf of Mexico. Wildlife workers caught oiled pelicans on Queen Bess Island, Louisiana, washed them, and let them go."),
    card("E", "d5", "A city under a thick brown haze of smog with mountains barely showing behind it",
         [{"t": "Brown haze hiding the city", "ok": True}, {"t": "Plastic on a beach", "miss": "Look again. There's no beach. What is in the air?"}, {"t": "Oil on the water", "miss": "Look again. What is hiding the buildings?"}],
         ["People and animals who breathe the city air", "Coral in the sea", "Fish in a lake far away"], 0, "people and animals who breathe it",
         "Smog hangs in the air over the city. Who breathes it? Try again.",
         "Air", "air", "Smog is in the sky, so it pollutes the air. Try again.",
         "d5h", "A wide city spread out under clear skies with snowy mountains behind", "Today: on a clear winter day · Salt Lake City, Utah, 2011 (smog photo 1972)",
         "This clear view is evidence that cleaner cars and clean-air laws can cut smog.", "valley",
         "Scenario 5 asks about car exhaust and smog. This 1972 photo shows Salt Lake City under smog. Cars today put out much less pollution than cars did then, though this valley still gets smoggy days in winter.")
  ]
}

rebuild = {"title": "Use your evidence to rebuild the place", "missPrefix": "Hmm. Look at your scene again. ", "kicker": "🌍 Rebuild the place", "whyStart": "I chose this because the scene…",
  "envs": [
    {"key": "city", "name": "🏙️ A city with cleaner air", "img": "d1h", "cap": "Blue sky, green park…"},
    {"key": "ocean", "name": "🌊 Open ocean", "img": "d2h", "cap": "Clear blue water…"},
    {"key": "public", "name": "🏜️ Open public land", "img": "d3h", "cap": "Sagebrush and hills…"},
    {"key": "gulf", "name": "🏝️ A Gulf coast island", "img": "d4h", "cap": "Pelicans and salt water…"},
    {"key": "valley", "name": "🏔️ A mountain valley city", "img": "d5h", "cap": "Snowy peaks, clear air…"}
  ],
  "life": [
    {"name": "🌳 City park trees", "img": "d1h", "env": "city", "miss": "City park trees grow in the city."},
    {"name": "🐢 Green sea turtle", "img": "d2h", "env": "ocean", "miss": "Sea turtles swim in the ocean."},
    {"name": "🌿 Sagebrush", "img": "d3h", "env": "public", "miss": "Sagebrush grows on dry open land."},
    {"name": "🐦 Brown pelican", "img": "d4h", "env": "gulf", "miss": "Brown pelicans nest on Gulf coast islands."},
    {"name": "🧍 People breathing clean air", "img": "d5h", "env": "valley", "miss": "These people live in the valley city."}
  ]}

quiz = [
  {"q": "What does the word pollution mean?", "options": [
    {"t": "The place where an animal or plant lives", "miss": "Think back to the word cards. Which word means where an animal lives? And which one is about harmful materials? They're two different words."},
    {"t": "Harmful materials that get into air, water, or land", "ok": "🌿 Exactly! Pollution is harmful material that ends up where it doesn't belong: in the air, water, or land around us."},
    {"t": "All the living things in a place and their surroundings", "miss": "Think back to the word cards. Which word means all the living things in a place? And which one is about harmful materials? They're two different words."}]},
  {"q": "A factory spills chemicals into a nearby river. What is most likely to happen next?", "options": [
    {"t": "Fish and other water animals get sick or die", "ok": "🌊 Right! Water pollution makes the river unsafe for the fish, frogs, and insects that live in it."},
    {"t": "The river water gets cleaner over time", "miss": "Think about cause and effect. Chemicals in water hurt the animals that live there."},
    {"t": "Plants near the river begin to grow faster", "miss": "Think about cause and effect. Chemicals in water hurt the animals that live there."}]},
  {"q": "Which of these is an example of land pollution?", "options": [
    {"t": "Car exhaust fumes rising into the sky over a city", "miss": "Look at the three types again: which happens on the ground? Fumes go into the air, oil goes into water. What's left is land."},
    {"t": "Old tires and trash dumped in a forest clearing", "ok": "🌲 Yes! Trash and waste dumped on the ground is land pollution. It harms the soil and the creatures that live in it."},
    {"t": "An oil spill spreading across the surface of the ocean", "miss": "Look at the three types again: which happens on the ground? Fumes go into the air, oil goes into water. What's left is land."}]}
]

def lwa(n, q, ans):
    names = {"land": "Land", "water": "Water", "air": "Air"}
    tips = {"land": "Is it on the ground?", "water": "Is it in a river, lake, or ocean?", "air": "Is it floating in the sky?"}
    return {"n": n, "q": q, "type": "choice", "options": [
        ({"t": names[k], "ok": "Yes. That's " + k + " pollution."} if k == ans else {"t": names[k], "miss": "Where does the pollution end up: on the ground, in the water, or in the air?"}) for k in ("land", "water", "air")]}

assign = {
  "partA": {"title": "Classify the pollution", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
    lwa(1, "Thick smog covers a city after a week with no wind. Birds and insects are struggling to fly.", "air"),
    lwa(2, "Bags of old pesticides (bug poison) are buried behind a warehouse near a field where deer graze.", "land"),
    lwa(3, "A gray, foamy substance floats on the surface of a river near a paper mill.", "water"),
    lwa(4, "Smoke from burning crop fields drifts over a wetland where birds stop to rest.", "air"),
    lwa(5, "Broken glass and rusted metal are left at the edge of a forest trail after a camping trip.", "land"),
    {"n": 6, "q": "Pick one of the five examples. Write one living thing that could be harmed, and how.", "type": "text", "min": 10, "chips": [["living", "Names a living thing"], ["because", "Says how (because, so)"]]}
  ]},
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Explain why water pollution is dangerous even for animals that don't live in the water, like deer or birds that drink from a river.", "type": "text", "min": 12, "chips": [["living", "Names an animal"], ["because", "Gives a reason (because, so)"]]},
    {"n": 2, "q": "How is air pollution different from land pollution? Give one example of each in your answer.", "type": "text", "min": 15, "chips": [["type", "Names air and land"], ["two", "Gives a second example (and, also)"]]}
  ]},
  "write": {"title": "Choose one type of pollution. How does it harm living things, and what can people do?", "do": "Pick one from your evidence chart. Answer the three questions. Use at least two of the science words under the boxes.",
    "vocab": ["pollution", "ecosystem", "habitat", "water pollution", "land pollution", "air pollution"], "need": 2,
    "prompts": [["What do you think?", "Start with: \"I think [land / water / air] pollution is especially harmful because…\""],
                ["What did you learn that supports your thinking?", "Start with: \"I know this because the lesson showed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because…\""]]},
  "partC": {"do": "Draw an outdoor place with one type of pollution getting into it. Label where it comes from, and one living thing it harms.",
            "labels": ["Where the pollution comes from, and its type", "One living thing it harms, and how"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 scenes and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all six questions.", "req": {"choice": ["a1", "a2", "a3", "a4", "a5"], "text": {"in-a6": 10}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 15}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least two science words.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 2}}
  ]
}

premiere = {"title": "Premiere my pollution story", "thinkLabel": "Harmed", "director": "JUNIOR ECOLOGIST", "storyKicker": "My pollution story",
  "frames": [
    {"k": "formation", "label": "Field to lake", "img": "o3", "cap": "Field to lake: rain carried fertilizer that turned a lake green."},
    {"k": "compare", "label": "The Light Test", "img": "tb", "cap": "The Light Test: green algae block the sunlight seagrass needs."},
    {"k": "wall", "label": "One river, then and now", "img": "l4", "cap": "Then and now: laws and cleanup brought a river back."},
    {"k": "det", "label": "Pollution detective", "img": "d4", "cap": "Pollution detective: land, water, or air, and who gets harmed."}]}

nxt = {"title": "23.02 · Pollution Cleanup", "text": "Next time, test ways to clean up pollution and decide which cleanup works best."}

chips = {
  "part": {"any": ["pink", "white", "red", "rim", "edge", "twig", "stick", "bark", "tree", "green", "leafy", "vine", "curly", "crust", "lichen", "gray", "brown", "moss"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["smoke", "chimney", "chimneys", "plastic", "caps", "cap", "tires", "tire", "oil", "pelican", "pelicans", "smog", "haze", "seaweed", "factory", "city"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "type": {"any": ["land", "water", "air"]},
  "living": {"any": ["fish", "bird", "birds", "deer", "turtle", "plant", "plants", "tree", "trees", "insect", "insects", "frog", "animal", "animals", "people", "worm", "worms", "pelican", "rabbit"]},
  "two": {"re": "\\b(and|also|another|second|too)\\b"}
}

L = {"id": "g3sci-23-01", "lesson": "23.01", "title": "What Types of Pollution Harm Ecosystems?", "emoji": "🏭",
  "details": ["📅 Q3 · Unit 8 · Human Impact &amp; Conservation", "📖 Week 23 · Lesson 23.01", "🌎 CPALMS SC.3.N.1.7 · NGSS 3-LS4-4", "⏱ About 35 minutes"],
  "icans": ["name three types of pollution and describe what causes each one.", "explain how pollution harms living things and the places they call home.", "describe actions people take to reduce pollution and protect wild ecosystems."],
  "opti": {"warm": "Our film starts with old photos from the 1970s. First, look closely at something growing on a tree.",
           "lesson": "Today you're a pollution detective. Follow the fertilizer, test the light, then travel through one river's story.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you found. Sort land, water, and air pollution, then explain how people can help."},
  "film": film, "scientist": "ecologist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Gustav Holst, <i>Jupiter</i> from <i>The Planets</i>, played by the U.S. Air Force Heritage of America Band, public domain (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The film's then-and-now is a story told with real photos from different places; the 1970s photos are from the EPA's DOCUMERICA project (U.S. National Archives). The algae movie, the Light Test and the river timeline are models; every place photo is real. The four order photos come from different places."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-23-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the tree bark, then tap three things you notice."},
  "how-23-01-compare": {"page": "Put the flashlight under one tray and the cup under the other: drag them, or tap one, then a tray. Press Shine the light. Then swap and try again.",
                        "say": "Put the flashlight under one tray and the cup under the other: drag them, or tap one, then a tray. Press Shine the light. Then swap and try again."},
  "how-23-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-23-01-det": {"page": det["do"], "say": "Pick three scenes, one at a time. Tap a clue, then pick who is harmed. Predict land, water, or air, and watch the place today appear."},
  "how-23-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"23-01-welcome": L["opti"]["warm"], "23-01-lesson": L["opti"]["lesson"], "23-01-check": L["opti"]["check"], "23-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
