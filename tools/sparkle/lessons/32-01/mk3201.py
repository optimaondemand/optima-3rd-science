#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/32-01/lesson.json, how-lines.json, scripts.json, credits.json (32.01: no voices recorded; scripts only).
Images come from prep.py (run it first)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "How do scientists figure out which organisms belong in a habitat, and why does protecting that habitat matter?"

film = {
  "id": "g3sci-32-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 32.01 · Researching a National Park Ecosystem",
  "title": "See America",
  "bigQuestion": BQ,
  "poster": "f_see", "endPoster": "f_valley", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.5},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 6.0, "type": "archive", "img": "f_see", "alt": "An old travel poster of a waterfall in a canyon, with the words See America and Visit the National Parks", "note": "A travel poster from the 1930s.", "fade": 0.8, "sfx": "whoosh", "sfxArg": 0.8},
    {"t": 9.4, "d": 8.0, "type": "split", "img": "f_stamp", "alt": "A green 3-cent stamp showing a white heron and a map of Florida, with the words Everglades National Park",
     "img2": "f_ever", "alt2": "A wide, flat marsh of grass and water at sunset",
     "splitAt": 2.6, "splitDur": 2.4, "lab1": "A stamp from 1947", "lab2": "The Everglades today",
     "from": [1.0, .5, .5], "to": [1.05, .5, .5], "fade": 0.6, "sfxAt": [{"at": 2.6, "name": "whoosh"}]},
    {"t": 17.4, "d": 8.0, "type": "split", "img": "f_poster", "alt": "An old blue poster of a white geyser shooting up, with the words Yellowstone National Park",
     "img2": "f_old", "alt2": "Old Faithful geyser shooting a tall column of steam into a blue sky",
     "splitAt": 2.6, "splitDur": 2.4, "lab1": "A poster from 1938", "lab2": "Old Faithful today",
     "from": [1.0, .5, .5], "to": [1.05, .5, .5], "fade": 0.6, "sfxAt": [{"at": 2.6, "name": "whoosh"}]},
    ph(25.4, 5.6, "f_tunnel", "A deep green valley between giant granite cliffs, with a waterfall on the right", "Tunnel View · Yosemite National Park, California",
       frm=(1.12, .5, .5), to=(1.0, .5, .5)),
    ph(31.0, 5.6, "f_ranger", "A park ranger with a backpack and students holding a notepad", "A park ranger and students collecting data · Denali National Park, Alaska",
       frm=(1.0, .5, .45), to=(1.1, .5, .4)),
    ph(36.6, 6.8, "f_valley", "A green meadow and a calm river below the huge granite cliff El Capitan", "El Capitan · Yosemite National Park",
       frm=(1.0, .5, .5), to=(1.08, .5, .45), fade=0.9),
    {"t": 43.4, "d": 5.6, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.4, "text": "Long ago, posters invited people to see America's national parks.", "voice": "opti-1"},
    {"t": 9.8, "d": 7.4, "text": "In 1947, the Everglades became a national park.", "voice": "opti-2"},
    {"t": 17.8, "d": 7.4, "text": "Yellowstone was the very first, back in 1872.", "voice": "opti-3"},
    {"t": 25.8, "d": 5.0, "text": "Each park has its own weather, land, and living things.", "voice": "opti-4"},
    {"t": 31.4, "d": 5.0, "text": "Scientists study each park, then share what they find.", "voice": "opti-5"},
    {"t": 37.0, "d": 6.2, "text": BQ, "voice": "opti-6"}
  ]
}

specimen = {
  "img": "spec", "aspect": "3/4", "radius": 0.07,
  "hotspots": [
    {"name": "Small, tight scales at the top", "x": 0.50, "y": 0.10},
    {"name": "Woody scales with wrinkly edges", "x": 0.70, "y": 0.29},
    {"name": "Scales packed in a spiral, all the way around", "x": 0.25, "y": 0.46},
    {"name": "A rounded shape, about as big as a chicken egg", "x": 0.42, "y": 0.66},
    {"name": "A short stalk that held it to a branch", "x": 0.56, "y": 0.86}
  ],
  "kicker": "🔎 Mystery specimen", "title": "Small cone, big secret?",
  "alt": "A small, egg-shaped brown cone with wrinkly woody scales and a short stalk",
  "look": "A real cone from a tree, about as long as your thumb. Look at its scales, its shape, and its stalk. A specimen is one real thing that scientists study. This small cone comes from a tree that grows in a national park. How big do you think that tree gets? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the cone, then tap 3 things you notice.",
  "number": "No. 32.01-A",
  "card": ["<b>Specimen A</b>", "Length: about 5 to 7 cm (2 to 3 inches)", "Comes from: a tree in California's mountains", "How big is the tree? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🌍", "ecosystem", "All the living things and nonliving things in an area that interact with each other."],
  ["🏡", "habitat", "The place where an organism lives and finds everything it needs: food, water, shelter, and space."],
  ["🌡️", "environmental conditions", "The nonliving features of a place, like temperature, rainfall, and sunlight, that affect which organisms can live there."],
  ["🐾", "organism", "Any living thing, including plants, animals, fungi, and bacteria."],
  ["💪", "survive", "To stay alive by getting the food, water, shelter, and other conditions you need to live and grow."],
  ["🛡️", "conservation", "Protecting natural places and living things so that ecosystems can stay healthy over time."]
]

parts = [
  {"kicker": "🌿 Part 1", "title": "What Is an Ecosystem?",
   "html": "<p>Every national park is an ecosystem. It includes every plant, animal, and other organism that lives there, plus nonliving things like water, soil, temperature, and sunlight. These parts interact all the time. A tree shades the soil. A frog eats insects and gets eaten by a heron. Rain fills a pond. When scientists study a park, they look at the habitat, the organisms, and the environmental conditions together.</p>"},
  {"kicker": "🐊 Part 2", "title": "Who Can Survive Here?",
   "html": "<p>Not every organism can survive in every place. In any habitat, some organisms survive well, some survive less well, and some cannot survive at all. An alligator could not live in a snowy mountain forest, but in the warm, wet Everglades it does just fine. South Florida is the only place on Earth where alligators and crocodiles live side by side.</p>"},
  {"kicker": "📣 Part 3", "title": "Protecting Parks, and Sharing What We Learn",
   "html": "<p>Droughts, floods, wildfires, and hurricanes can change a park quickly. People change parks too, with pollution, building, and invasive species. That's why conservation matters.</p><p>Scientists and rangers collect evidence: observations and measurements of the organisms and conditions. Then they communicate. They share their findings in reports, talks, and maps, so other scientists can check the results and park managers can use them to protect the park.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Park Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the elk by the river.",
  "kicker": "🎞️ Put the scenes in order", "title": "What happened when wolves came home?",
  "look": "Four real photos tell the story of wolves returning to Yellowstone National Park. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "Elk standing in a winding river between snowy banks", "text": "Without wolves, elk gather by rivers and eat young willows.", "play": "Elk by the river.",
     "miss": ["", "The story starts before the wolves come back. Try frame 1.", "The story starts before the wolves come back. Try frame 1.", "The story starts before the wolves come back. Try frame 1."]},
    {"img": "o2", "alt": "Park workers carrying a metal crate through the snow", "text": "1995: wolves are carried back into Yellowstone.", "play": "Wolves come home.",
     "miss": ["The elk come first. Try a later frame.", "", "The wolves arrive before the elk change. Try an earlier frame.", "The wolves arrive before the elk change. Try an earlier frame."]},
    {"img": "o3", "alt": "An elk with big antlers on a snowy slope", "text": "Wolves hunt elk, and elk move around more.", "play": "Elk keep moving.",
     "miss": ["The wolves have to arrive first. Try a later frame.", "The wolves have to arrive first. Try a later frame.", "", "The elk change before the plants do. Try an earlier frame."]},
    {"img": "o4", "alt": "Tall reddish willow bushes poking up through snow in a valley", "text": "In some places, willows grow taller.", "play": "Some willows grow.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Ben says, \"One kind of animal doesn't matter to a whole park.\" What do you think?",
    "options": [
      {"t": "Ben is right. One kind of animal is too small to change anything.", "miss": "Think about the movie. What changed after the wolves came back?"},
      {"t": "One kind of animal can change others, like wolves changing how elk behave.", "ok": "Yes! Wolves changed what elk did, and that affected plants too. Scientists are still studying how big the change was."}
    ]
  }
}

movie = {
  "model": "wolf-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🐺",
  "real": "real", "realAlt": "A gray wolf with yellow eyes, wet fur, and a dark coat",
  "stamp": "EVERYTHING CONNECTS!", "endCap": "A real gray wolf in Yellowstone.",
  "beats": [
    {"at": 0, "cap": "1 · Elk by the river.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Before 1995"], "sfx": "whoosh"},
    {"at": 2600, "cap": "2 · Wolves come home.", "model": {"show": "s2"}, "counter": ["1995"]},
    {"at": 5200, "cap": "3 · Elk keep moving.", "model": {"show": "s3"}, "counter": ["A few years later"]},
    {"at": 7800, "cap": "4 · Some willows grow.", "model": {"show": "s4"}, "counter": ["Years later"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Winter Test", "title": "How does each animal get through winter?",
  "look": "Two real park animals, each on a lit tray. Specimen A is an American bison from Yellowstone. Specimen B is a mule deer from Yosemite. Under the trays are two model winter places: deep snow over the grass, and a lower valley with little snow.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A big brown bison walking through deep snow", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A mule deer with big ears eating plants in a grassy meadow", "label": "Specimen B"}
  ],
  "materials": [{"key": "snow", "label": "Deep snow over the grass", "img": "m_snow"}, {"key": "valley", "label": "A lower valley, little snow", "img": "m_valley"}],
  "ask": [
    {"q": "Which animal has a huge head and a big hump on its shoulders?", "ans": "A", "ok": "Yes. Specimen A is the bison.", "miss": "Look closely. Which one has a hump?"},
    {"q": "Which animal has thin legs and big ears?", "ans": "B", "ok": "Yes. Specimen B is the mule deer.", "miss": "Look again. Which one has big ears?"}
  ],
  "press": "❄️ Start winter",
  "testDo": "Put the deep snow under one tray and the lower valley under the other: drag them, or tap one, then a tray. Press <b>Start winter</b>. Then swap.",
  "disclaimer": "This is a model. No real animals are tested.",
  "results": {
    "Asnow": {"text": "The bison swings its huge head side to side, pushes the snow away, and eats the grass underneath!", "fx": "shade"},
    "Avalley": {"text": "The bison could eat here too, but it doesn't need to leave. It can dig through deep snow for food.", "fx": "glow"},
    "Bsnow": {"text": "The deer's thin legs sink in the deep snow, and it can't reach the plants below.", "fx": "glow"},
    "Bvalley": {"text": "The deer walks down to the lower valley, where it can find plants to eat!", "fx": "shade"}
  },
  "best": ["Asnow", "Bvalley"],
  "frame": "In winter, this animal ___, so it does best in ___.", "claimLead": "In winter, this animal", "claimMid": "so it does best in",
  "claim": {
    "A": {"feat": ["digs through snow with its big head", "walks downhill to find food"], "featOk": 0, "eat": ["deep snow up high", "a lower valley"], "eatOk": 0},
    "B": {"feat": ["digs through snow with its big head", "walks downhill to find food"], "featOk": 1, "eat": ["deep snow up high", "a lower valley"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Snow plow.</b> A bison's strong neck and hump muscles let it swing its head like a plow and clear snow off the grass.",
    "B": "<b>Moving downhill.</b> When snow covers their food, many mule deer in Yosemite move to lower places where it's easier to find plants."
  },
  "missFeat": "Look at your tests for {label} again. What did it do in winter?",
  "missClaim": "Think about your tests. Where did this animal find food?",
  "done": "Two animals, two ways to survive winter. Each one fits the conditions in its own park.",
  "after": {"kicker": "🎬 Behind the scenes · Sharing data", "img": "after", "alt": "Scientists at an outdoor table recording information on paper data sheets",
            "html": "In Glacier National Park, scientists catch birds in soft nets, record data, and let them go. They share their data with scientists across North America, so everyone can learn how birds are doing."}
}

wall = {
  "kicker": "🛂 The Park Passport", "title": "Collect four park stamps, one stop at a time",
  "look": "A model passport with four national park stamps. Each stamp holds a clue and a real photo. The dial on the left shows which park you're visiting.",
  "do": "First, make a prediction. Then brush the glowing stamp: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "Do you predict the same environmental condition matters most in every park?",
              "options": [["no", "No, each park is different"], ["yes", "Yes, it's the same everywhere"]], "answer": "no",
              "mine": "Your prediction: <b>{p}</b>. Let's stamp the passport and find out.",
              "confirm": "You predicted each park is different. You were right: water, cold, height, and rain each matter most in a different park.",
              "change": "You predicted it's the same everywhere. The passport changed that idea: a different condition matters most in each park."},
  "sky": "sky", "skyAlt": "A deep green valley between huge granite cliffs", "skyCap": "Yosemite Valley, California",
  "unit": "Stamp", "found": "Stamp {n} collected",
  "elevator": ["Passport", "Everglades", "Yosemite", "Yellowstone", "Smokies"],
  "line": ["WARM AND LOW", "COLD AND HIGH"],
  "lockTag": "🔒 Open the stamp above first", "locked": "Open the stamp above first. We go one park at a time.",
  "first": "Brush the glowing first stamp. Drag across it (or tap it again and again).", "next": "Keep going. Brush Stamp {n}.",
  "endTitle": "All 4 stamps collected",
  "endText": "Look at the passport. Each park has its own conditions, so each park has its own organisms.",
  "rule": "<b>Conditions decide who lives where.</b> Water, temperature, height, and rainfall shape each park. The organisms that live there are the ones that fit those conditions.",
  "choices": ["💧 Water: lots of warm, shallow water", "⛰️ Height: tall mountains and cliffs", "❄️ Cold: freezing winters and deep snow", "🌫️ Rain and mist: cool, wet forests"],
  "layers": [
    {"name": "Stamp 1 · Everglades, Florida", "rock": "water1", "img": "l1", "alt": "A wide, flat marsh of grass and water at sunset",
     "ask": "Look at Stamp 1. Read the clue AND the photo. Which condition matters most here?",
     "clue": "The Everglades is warm and flat. In the wet season, shallow water covers the land. Sawgrass, alligators, and spoonbills live here.",
     "ans": 0, "ok": "Yes! Warm, shallow water shapes life in the Everglades.", "tag": "💧 Everglades · water",
     "miss": {"1": "Look again. Are there tall mountains here?", "2": "Not quite. Is the Everglades freezing?", "3": "Close! It is wet, but read the clue: is it a cool forest, or warm, shallow water?"},
     "env": "e1", "envAlt": "An alligator swimming with its head above dark green water", "envCap": "An alligator near the Anhinga Trail · Everglades National Park"},
    {"name": "Stamp 2 · Yosemite, California", "rock": "limestone", "img": "l2", "alt": "A green valley between giant granite cliffs",
     "ask": "Look at Stamp 2. Read the clue AND the photo. Which condition matters most here?",
     "clue": "Granite cliffs rise high above the valley. Plants and animals change as you climb, and giant sequoias grow on the mountain slopes.",
     "ans": 1, "ok": "Yes! Height shapes life in Yosemite: different organisms live low and high.", "tag": "⛰️ Yosemite · height",
     "miss": {"0": "Not quite. Is this a flat marsh?", "2": "Close! It snows up high, but read the clue: what changes as you climb?", "3": "Not yet. Read the clue again: what rises above the valley?"},
     "env": "e2", "envAlt": "A giant sequoia trunk reaching up into a blue sky", "envCap": "A giant sequoia in the Mariposa Grove · Yosemite National Park"},
    {"name": "Stamp 3 · Yellowstone, Wyoming", "rock": "snowcap", "img": "l3", "alt": "Old Faithful geyser shooting steam into a blue sky",
     "ask": "Look at Stamp 3. Read the clue AND the photo. Which condition matters most here?",
     "clue": "Winters are long and freezing, with deep snow for months. Bison and elk must find food under the snow.",
     "ans": 2, "ok": "Yes! Cold and deep snow shape life in Yellowstone.", "tag": "❄️ Yellowstone · cold",
     "miss": {"0": "Not quite. Is it warm here?", "1": "Close! It is high up, but read the clue: what makes finding food hard?", "3": "Not yet. Is this a misty, rainy forest?"},
     "env": "e3", "envAlt": "A line of bison walking single file through deep snow", "envCap": "Bison walking through deep snow · Yellowstone National Park"},
    {"name": "Stamp 4 · Great Smoky Mountains", "rock": "haze", "img": "l4", "alt": "Foggy, forested mountains under gray clouds",
     "ask": "Look at Stamp 4. Read the clue AND the photo. Which condition matters most here?",
     "clue": "These cool mountain forests get lots of rain and mist. About 30 kinds of salamanders live here, more than almost anywhere on Earth.",
     "ans": 3, "ok": "Yes! Rain and mist keep these forests cool and wet, perfect for salamanders.", "tag": "🌫️ Smokies · rain and mist",
     "miss": {"0": "Not quite. Is this a warm, shallow marsh?", "1": "Close! There are mountains, but read the clue: what keeps the forest wet?", "2": "Not yet. Read the clue: is it freezing, or cool and misty?"},
     "env": "e4", "envAlt": "A bright red salamander with black spots on green moss", "envCap": "A black-chinned red salamander · Great Smoky Mountains National Park"}
  ],
  "mix": {
    "q": "Mia says, \"National parks are protected, so nothing ever changes there.\" What do you think?",
    "options": [
      {"t": "Mia is right. A park is safe forever.", "miss": "Think about the lesson. What can still happen in a park?"},
      {"t": "Parks still face droughts, fires, floods, and invaders, so scientists keep watching and sharing what they find.", "ok": "Yes! Protection helps a lot, but parks keep changing. That's why scientists study them every year."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "The Salamander Capital",
  "img": "wow", "alt": "A bright red salamander with black spots resting on green moss",
  "caption": "A black-chinned red salamander · Great Smoky Mountains National Park",
  "html": "<p style=\"margin:0 0 8px\">Great Smoky Mountains National Park is called the Salamander Capital of the World. About 30 kinds live in its cool, wet forests.</p><p style=\"margin:0\">Scientists and volunteers count salamanders year after year and share what they find, so everyone can see if the forest is staying healthy.</p>",
  "inset": "inset", "insetCap": "A black bear in the same forest."}

keyIdea = "Every national park is an ecosystem: living organisms and nonliving conditions like water, temperature, and sunlight, all interacting. In any habitat, some organisms survive well, some survive less well, and some cannot survive at all. Scientists collect evidence by observing and measuring, then share their findings so others can check them and use them to protect the park. Protecting a habitat protects all the organisms that depend on it."

PARKS = ["🐊 Everglades", "⛰️ Yosemite", "🦬 Yellowstone", "🌫️ Great Smoky Mountains"]
SHORT = ["the Everglades", "Yosemite", "Yellowstone", "the Great Smoky Mountains"]
SOL = [["well", "✅ It would survive well"], ["less", "⚠️ It would survive less well"], ["cannot", "❌ It could not survive"]]


def card(id_, img, alt, clues, orgAns, orgMiss, move, envAns, envMiss, envImg, envAlt, envCap, reveal, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": PARKS, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "predict": {"q": move, "options": SOL},
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": envAns, "bts": bts}


det = {
  "look": "Five real organisms from four national parks. Each card shows one organism. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap a feature that helps it survive, then name its home park. Predict if it could survive in a different park, and see the evidence.",
  "noun": "Card", "need": 3, "inferQ": "Which park is its home?", "inferDone": "It lives in", "chartSo": "and moved to another park, it",
  "predict": {"q": "Could it survive in a different park?", "options": SOL},
  "kicker": "The other park", "enough": "You already solved 3 park files. Nice work, ecologist!",
  "cols": ["Card", "Survival feature", "Home park", "In another park", "My evidence"],
  "write": {"label": "Card __ has ___. It survives in ___, but in another park it ___, because ___.", "starter": "Start with: \"Card __ has…\"", "min": 15,
            "chips": [["trait", "Names a feature"], ["hab", "Names a park or condition"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "An alligator swimming with its head above dark green water",
         [{"t": "Eyes and nostrils on top of its head", "ok": True}, {"t": "Thick fur for the cold", "miss": "Look again. Does an alligator have fur?"}, {"t": "Feathers", "miss": "Look again. Does it have feathers?"}],
         0, "Alligators need warm, shallow water. Which park has that? Try again.",
         "Could the alligator survive in Yellowstone?", "cannot", "Think about Yellowstone's winters. Can a cold-blooded reptile live through months of ice? Try again.",
         "d1h", "Three bison standing in blowing snow", "Winter in Yellowstone National Park",
         "Alligators need warm water. Yellowstone's lakes freeze, and winter lasts for months. An alligator could not survive there.",
         "Alligators can't make their own body heat, so they need warm places."),
    card("B", "d2", "A pink roseate spoonbill wading in shallow water, sweeping its flat bill",
         [{"t": "A flat, spoon-shaped bill for sweeping shallow water", "ok": True}, {"t": "A big hump for pushing snow", "miss": "Look again. Does a bird have a hump?"}, {"t": "Thick bark", "miss": "Look again. Is this a tree?"}],
         0, "Spoonbills feed in warm, shallow water. Which park has that? Try again.",
         "Could the spoonbill survive high in Yosemite's mountains?", "cannot", "High in the mountains, the water is cold, deep, or frozen. Where would it sweep for food? Try again.",
         "d2h", "Huge granite cliffs above a pine forest", "High granite cliffs · Yosemite National Park",
         "A spoonbill sweeps its bill through warm, shallow water to catch small fish and shrimp. High in Yosemite's mountains, there's no warm, shallow water like that.",
         "Spoonbills get their pink color from the food they eat."),
    card("C", "d3", "A giant sequoia trunk reaching up into a blue sky",
         [{"t": "Thick, spongy bark that protects it from fire", "ok": True}, {"t": "Eyes on top of its head", "miss": "Look again. Is this an animal?"}, {"t": "A spoon-shaped bill", "miss": "Look again. Is this a bird?"}],
         1, "Giant sequoias grow on mountain slopes in California. Which park is that? Try again.",
         "Could a giant sequoia survive in the Everglades?", "cannot", "Sequoias grow on cool mountain slopes. Would a hot, flooded marsh suit it? Try again.",
         "d3h", "A wide marsh of green sawgrass under a blue sky", "A sawgrass marsh · Everglades National Park",
         "Giant sequoias grow naturally only on the mountain slopes of California's Sierra Nevada. In the hot, flooded Everglades, a sequoia could not grow.",
         "The small cone from our mystery specimen grows on this tree, the biggest tree on Earth by volume."),
    card("D", "d4", "A big brown bison walking through deep snow",
         [{"t": "A huge head and hump that push snow aside", "ok": True}, {"t": "Sticky toe pads", "miss": "Look again. Does a bison have toe pads?"}, {"t": "Scales", "miss": "Look again. Does a bison have scales?"}],
         2, "Bison graze in cold meadows with deep winter snow. Which park is that? Try again.",
         "Could the bison survive in the Great Smoky Mountains?", "well", "Here's a surprise: think about where bison lived long ago. Try again.",
         "d4h", "Green forested mountains under a blue sky", "Great Smoky Mountains National Park",
         "Long ago, bison really did live in the Southeast, including the area around the Smoky Mountains, until people hunted them out. The land could still feed them.",
         "A grown bison can weigh as much as a small car."),
    card("E", "d5", "A dark gray wolf with yellow eyes",
         [{"t": "Hunts in a pack to catch big prey like elk", "ok": True}, {"t": "A flat bill", "miss": "Look again. Does a wolf have a bill?"}, {"t": "Thick, spongy bark", "miss": "Look again. Is this a tree?"}],
         2, "Gray wolves were brought back to this park in 1995. Which park is that? Try again.",
         "Could the gray wolf survive in Yosemite?", "well", "Yosemite has forests, mountains, and deer to hunt. Try again.",
         "d5h", "A mule deer with antlers walking on a road in Yosemite Valley", "A mule deer in Yosemite Valley",
         "Gray wolves once lived in California's mountains. Today, a few wolf packs live in northern California again, hunting deer.",
         "Wolves can travel many miles in one day to find food.")
  ]
}

rebuild = {"title": "Use your evidence to sort the moves", "missPrefix": "Hmm. Look at your park file again. ", "kicker": "🗂️ Sort the moves", "whyStart": "I chose this because the conditions…",
  "envs": [
    {"key": "well", "name": "✅ Would survive well", "img": "d4h", "cap": "A good fit…"},
    {"key": "cannot", "name": "❌ Could not survive", "img": "d1h", "cap": "The wrong conditions…"}
  ],
  "life": [
    {"name": "🐊 Alligator to Yellowstone", "img": "d1", "env": "cannot", "miss": "Freezing winters are the wrong conditions for an alligator."},
    {"name": "🦩 Spoonbill to the mountains", "img": "d2", "env": "cannot", "miss": "There's no warm, shallow water high in the mountains."},
    {"name": "🌲 Sequoia to the Everglades", "img": "d3", "env": "cannot", "miss": "A hot, flooded marsh is the wrong place for a sequoia."},
    {"name": "🦬 Bison to the Smokies", "img": "d4", "env": "well", "miss": "Bison lived in the Southeast long ago."},
    {"name": "🐺 Wolf to Yosemite", "img": "d5", "env": "well", "miss": "Wolves once lived in California's mountains, and some live there again."}
  ]}

quiz = [
  {"q": "What does an organism's habitat provide?", "options": [
    {"t": "Only the other animals it can eat", "miss": "If you moved to a new home, you'd need more than just food. A habitat provides food, water, shelter, and the right living conditions all at once."},
    {"t": "Food, water, shelter, and the conditions it needs to survive", "ok": "🌲 Exactly right! A habitat provides everything an organism needs, all together."},
    {"t": "Sunlight and temperature only", "miss": "If you moved to a new home, you'd need more than just food. A habitat provides food, water, shelter, and the right living conditions all at once."}]},
  {"q": "A polar bear is built for icy, cold environments. What would happen if a polar bear was placed in a hot, wet rainforest habitat?", "options": [
    {"t": "It would thrive, because animals can adapt to any environment", "miss": "Size and strength don't guarantee survival in the wrong habitat. What matters is whether the conditions match what the organism needs."},
    {"t": "It would survive well, because it's a large, strong predator", "miss": "Size and strength don't guarantee survival in the wrong habitat. What matters is whether the conditions match what the organism needs."},
    {"t": "It would struggle or not survive, because the environmental conditions don't match its needs", "ok": "🌿 Great thinking! A polar bear's thick fur and cold-water diet make it a poor fit for a hot rainforest."}]},
  {"q": "Scientists at Yellowstone brought wolves back after they had been gone for about 70 years. Why did this matter for the whole ecosystem?", "options": [
    {"t": "The wolves changed how elk behaved, and that affected plants and other animals too", "ok": "⭐ Excellent! One species can change others. Scientists are still studying just how big the changes were."},
    {"t": "Wolves are the only endangered species in Yellowstone, so they needed the most protection", "miss": "Think about the movie: wolves changed what the elk did, and that affected plants. One species touched others."},
    {"t": "Wolves only affected other wolves. They didn't change anything for other organisms.", "miss": "Think about the movie: wolves changed what the elk did, and that affected plants. One species touched others."}]}
]


def lq(n, item, ans):
    opts = ["A living thing", "A nonliving thing"]
    ok = f"Yes. {item[0].upper() + item[1:]} is {'living' if ans == 0 else 'nonliving'}."
    miss = "Ask: does it grow, need food, and make more of its own kind?"
    return {"n": n, "q": f"Is {item} living or nonliving?", "type": "choice", "options": [{"t": c, "ok": ok} if i == ans else {"t": c, "miss": miss} for i, c in enumerate(opts)]}


partA = {"title": "Living or nonliving?", "do": "Read each one. Pick the best answer.", "items": [
  lq(1, "an alligator", 0), lq(2, "sunlight", 1), lq(3, "sawgrass", 0), lq(4, "rainfall", 1), lq(5, "soil", 1)
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Pick one park from today: the Everglades, Yosemite, Yellowstone, or the Great Smoky Mountains. Answer in complete sentences.", "items": [
    {"n": 1, "q": "Describe your park. Name two organisms that live there and explain how the environmental conditions match their needs.", "type": "text", "min": 12, "chips": [["two", "Names two organisms"], ["condw", "Names a condition (water, cold, snow, heat, rain)"]]},
    {"n": 2, "q": "Why do scientists say that protecting one national park habitat helps many different organisms, not just one species?", "type": "text", "min": 12, "chips": [["habw", "Uses the word habitat"], ["because", "Gives a reason (because, so)"]]}
  ]},
  "write": {"title": "Pick one organism from a national park. Can it survive in a completely different habitat? Use what you learned to explain your thinking.", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["habitat", "environmental conditions", "survive", "ecosystem"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think that [organism's name] could / could not survive in [different habitat] because…\""],
                ["What did you observe or learn that supports your thinking?", "Start with: \"I know this because the lesson showed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because…\""]]},
  "partC": {"do": "Draw a simple ecosystem scene from the park you picked. Show at least four organisms in their habitat. Label each organism, and draw one arrow showing how one thing connects to another (like wolf → elk).",
            "labels": ["Labels: my four organisms", "My arrow: what connects to what"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 park files and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all five answered.", "req": {"choice": ["a1", "a2", "a3", "a4", "a5"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing, labels, and arrow.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my park report", "thinkLabel": "Its home park", "director": "JUNIOR ECOLOGIST", "storyKicker": "My national park report",
  "frames": [
    {"k": "formation", "label": "Wolves come home", "img": "o2", "cap": "Wolves come home: one species changes others."},
    {"k": "compare", "label": "The Winter Test", "img": "ta", "cap": "The Winter Test: each animal fits its own winter."},
    {"k": "wall", "label": "The Park Passport", "img": "l3", "cap": "The Park Passport: each park has its own conditions."},
    {"k": "det", "label": "Park files", "img": "d3", "cap": "Park files: who could survive where."}]}

nxt = {"title": "Coming up next: 32.02", "text": "Build a Park Ecosystem Presentation. Next time, you'll turn your park research into a presentation and share it, just like real scientists."}

chips = {
  "part": {"any": ["scales", "scale", "brown", "cone", "wrinkly", "woody", "stalk", "stem", "egg", "round", "small", "spiral", "pine", "seed", "seeds"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["eyes", "nostrils", "bill", "bark", "hump", "head", "pack", "hunts", "fur", "feathers", "thick", "flat"]},
  "hab": {"any": ["everglades", "yosemite", "yellowstone", "smoky", "smokies", "park", "water", "snow", "cold", "warm", "mountains", "marsh"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "two": {"re": "\\b(and|also)\\b"},
  "condw": {"any": ["water", "cold", "snow", "heat", "hot", "warm", "rain", "rainfall", "temperature", "mist", "freezing", "sunlight"]},
  "habw": {"any": ["habitat", "habitats"]}
}

L = {"id": "g3sci-32-01", "lesson": "32.01", "title": "Researching a National Park Ecosystem", "emoji": "🏞️",
  "details": ["📅 Q4 · Unit 11 · National Park Capstone", "📖 Week 32 · Lesson 32.01", "🌎 CPALMS SC.3.N.1.4, SC.3.N.1.7", "⏱ About 35 minutes"],
  "icans": ["describe an ecosystem by naming its organisms, habitat, and environmental conditions.", "explain why some organisms survive well in a habitat while others cannot survive there at all.", "explain one reason why protecting a national park ecosystem matters for the organisms that live there."],
  "opti": {"warm": "Our film starts with old national park posters and stamps. First, inspect a small mystery cone.",
           "lesson": "Today you're an ecologist. Watch wolves come home, run the Winter Test, then stamp your Park Passport.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Pick a park, then draw its ecosystem with one connection arrow."},
  "film": film, "scientist": "ecologist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: The Stars and Stripes Forever (John Philip Sousa), \"The President's Own\" United States Marine Band (2017), public domain recording (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The wolf movie, the Winter Test, and the Park Passport are models; every place photo is real. The cone photo was taken in Scotland, where giant sequoias are planted in gardens."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-32-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the cone, then tap three things you notice."},
  "how-32-01-compare": {"page": "Put the deep snow under one tray and the lower valley under the other: drag them, or tap one, then a tray. Press Start winter. Then swap.",
                        "say": "Put the deep snow under one tray and the lower valley under the other: drag them, or tap one, then a tray. Press Start winter. Then swap."},
  "how-32-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-32-01-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap a feature that helps it survive, then name its home park. Predict if it could survive in a different park, and see the evidence."},
  "how-32-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"32-01-welcome": L["opti"]["warm"], "32-01-lesson": L["opti"]["lesson"], "32-01-check": L["opti"]["check"], "32-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
