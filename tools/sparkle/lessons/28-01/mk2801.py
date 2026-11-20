#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/28-01/lesson.json, how-lines.json, scripts.json, credits.json (28.01: no voices recorded; scripts only)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


film = {
  "id": "g3sci-28-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 28.01 · How Does Energy Cause Change?",
  "title": "Lightning Capital",
  "bigQuestion": "How does energy cause things to change and move?",
  "poster": "f_satbeach", "endPoster": "f_sunrise", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 3.6, "type": "black", "sfxAt": [{"at": 0.3, "name": "rumble"}, {"at": 2.2, "name": "rumble"}], "fade": 0.4},
    ph(7.0, 5.8, "f_vab", "Dark storm clouds roll in over a giant building marked NASA", "Kennedy Space Center, Florida · A storm rolls in",
       frm=(1.0, .5, .5), to=(1.12, .5, .45), fade=1.0, sfxAt=[{"at": 0.4, "name": "rumble"}]),
    ph(12.8, 6.2, "f_satbeach", "Many bolts of lightning flash down from tall storm clouds over wide, calm water", "Lightning over the Indian River · Satellite Beach, Florida",
       frm=(1.12, .5, .55), to=(1.0, .5, .5), sfx="thump"),
    ph(19.0, 8.0, "f_artemis", "A bright bolt of lightning hits a tall tower next to a rocket on its launch pad", "Launch Pad 39B, Kennedy Space Center · August 27, 2022",
       frm=(1.0, .7, .3), to=(1.25, .78, .3), count={"to": 50000, "label": "°F · the air around the bolt", "dur": 4.0}),
    ph(27.0, 6.0, "f_indian", "Lightning bolts light up the night sky over a dark river and the lights of a town", "Lightning over the Indian River at night · Merritt Island, Florida",
       frm=(1.0, .5, .5), to=(1.1, .5, .55), sfxAt=[{"at": 0.8, "name": "rumble"}]),
    ph(33.0, 8.0, "f_sunrise", "The Sun rises orange over the ocean at a Florida beach, under dark clouds", "Cocoa Beach, Florida · Sunrise",
       frm=(1.0, .5, .5), to=(1.1, .5, .55), fade=1.0, fx=["rays"], sfx="shimmer"),
    {"t": 41.0, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.6, "d": 3.2, "text": "Listen. A storm is coming.", "voice": "opti-1"},
    {"t": 7.4, "d": 5.2, "text": "Florida gets more lightning than any other state.", "voice": "opti-2"},
    {"t": 13.2, "d": 5.6, "text": "Each bolt is a giant spark of electrical energy.", "voice": "opti-3"},
    {"t": 19.4, "d": 4.0, "text": "In a flash, it heats the air to 50,000 °F.", "voice": "opti-4"},
    {"t": 23.6, "d": 3.2, "text": "Hotter than the Sun's surface?", "voice": "opti-5"},
    {"t": 27.4, "d": 5.4, "text": "The hot air bursts outward. Boom! That's thunder.", "voice": "opti-6"},
    {"t": 33.4, "d": 4.0, "text": "By morning, our closest star rises.", "voice": "opti-7"},
    {"t": 37.6, "d": 3.2, "text": "How does energy cause things to change and move?", "voice": "opti-8"}
  ]
}

specimen = {
  "img": "spec", "aspect": "4/3", "radius": 0.07,
  "hotspots": [
    {"name": "A shiny, glassy inside", "x": 0.56, "y": 0.60},
    {"name": "A rough, sandy outside", "x": 0.62, "y": 0.32},
    {"name": "Little round bubble holes", "x": 0.22, "y": 0.70},
    {"name": "A long groove down the middle", "x": 0.72, "y": 0.58},
    {"name": "A thin white edge", "x": 0.86, "y": 0.42}
  ],
  "kicker": "🔎 Mystery specimen", "title": "What made this strange tube?",
  "alt": "A broken tube of rock with a rough, sandy outside and a shiny, gray, glassy inside full of little holes",
  "look": "A real object found in the sand, broken open so you can see inside. Look at its parts: the outside, the inside, the little holes, and the edges. A specimen is one real thing that scientists study. Something very hot made it. What? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the tube, then tap 3 things you notice.",
  "number": "No. 28.01-A",
  "card": ["<b>Specimen A</b>", "Found: in desert sand, Sahara", "Feels: rough outside, smooth inside", "What made it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["⚡", "energy", "The ability to cause change. Energy makes things move, heat up, light up, or make sound."],
  ["☀️", "light energy", "Energy you can see. The Sun, light bulbs, and fire all give off light energy."],
  ["🔥", "heat energy", "Energy that makes things warmer. Rubbing your hands together changes motion energy into heat energy."],
  ["🔊", "sound energy", "Energy you can hear. Sound is made when something vibrates, like a guitar string or a drum."],
  ["🏃", "motion energy", "The energy of moving things. A rolling ball and a spinning top have motion energy. Scientists also call it mechanical energy."],
  ["🔌", "electrical energy", "Energy that flows through wires to power lights, fans, and other devices. Lightning is electrical energy too."]
]

parts = [
  {"kicker": "🌱 Part 1", "title": "What Is Energy?",
   "html": "<p>In science, energy is the ability to cause change. Energy makes things move, light up, warm up, or make sound. You can't always see energy, but you can see what it does.</p><p>Watch out: in everyday talk, \"energy\" can mean feeling peppy. Science words can have their own special meaning.</p>"},
  {"kicker": "🌤 Part 2", "title": "Forms of Energy",
   "html": "<p>Energy comes in many forms. Light energy lets us see. Heat energy makes things warmer. Sound energy is what we hear. Motion energy is the energy of moving things. Electrical energy flows through wires.</p><p>Things that give off light often give off heat too, like a light bulb, a candle, or the Sun. When you rub your hands together, motion energy changes into heat energy.</p>"},
  {"kicker": "🌍 Part 3", "title": "Our Sun Is a Star",
   "html": "<p>The Sun is a star: a huge ball of hot, glowing gas that gives off light and heat. Other stars are so far away that they look like tiny points of light. The Sun looks big and bright because it is the closest star to Earth.</p><p>Stars are not all the same size, color, or brightness. A telescope shows many more stars than your eyes can see. Never look straight at the Sun.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Energy Change Files"}
]

order = {
  "mix": [3, 1, 0, 2], "hint": "Start with the storm cloud.",
  "kicker": "🎞️ Put the scenes in order", "title": "What happens in one lightning strike?",
  "look": "Four real photos show what happens in a lightning strike, from a growing storm cloud to the boom of thunder. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "A tall white storm cloud towers over a calm marsh and its reflection", "text": "A tall storm cloud grows. Electric charge builds up inside it.", "play": "Charge builds.",
     "miss": ["", "The storm cloud comes first. Try frame 1.", "The storm cloud comes first. Try frame 1.", "The storm cloud comes first. Try frame 1."]},
    {"img": "o2", "alt": "A bright, branching bolt of lightning hits the ground near a launch pad at night", "text": "Crack! A bolt of lightning: electrical energy.", "play": "The bolt.",
     "miss": ["The cloud has to build up charge first. Try a later frame.", "", "The bolt comes before the flash lights the sky. Try an earlier frame.", "The bolt comes before the thunder. Try an earlier frame."]},
    {"img": "o3", "alt": "Purple lightning lights up the clouds and the trees below at night", "text": "The flash lights up the sky and heats the air.", "play": "Light and heat.",
     "miss": ["The storm has to build first. Try a later frame.", "The bolt has to strike first. Try a later frame.", "", "You see the flash before you hear the boom. Try an earlier frame."]},
    {"img": "o4", "alt": "A long strip of bark blasted off the trunk of a live oak tree, showing bright orange wood", "text": "Boom! Thunder rolls. The bolt's heat even blasted bark off this tree.", "play": "Sound and motion.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "In a storm, you see the flash first and hear the boom a few seconds later. Why?",
    "options": [
      {"t": "Light travels much faster than sound.", "ok": "Yes! The light reaches you almost at once. The sound of thunder takes about 5 seconds to travel 1 mile."},
      {"t": "The thunder comes from a different storm.", "miss": "Look at the movie again. The flash and the boom come from the same bolt."}
    ]
  }
}

movie = {
  "model": "bolt-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "⏱️",
  "real": "real", "realAlt": "The end of a hollow tube of glassy sand made by a lightning strike",
  "stamp": "FROZEN LIGHTNING!", "endCap": "Real lightning glass.",
  "beats": [
    {"at": 0, "cap": "1 · Charge builds.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Storm grows"], "sfx": "rumble"},
    {"at": 2600, "cap": "2 · The bolt.", "model": {"show": "s2"}, "counter": ["0 seconds"]},
    {"at": 5200, "cap": "3 · Flash and heat.", "model": {"show": "s3"}, "counter": ["0 seconds"], "sfx": "shimmer"},
    {"at": 7800, "cap": "4 · Boom! 1 mile away.", "model": {"show": "s4"}, "counter": ["5 seconds"], "sfx": "rumble"},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Glow Test", "title": "Does everything that glows get hot?",
  "look": "Two real specimens, each on a lit tray. Specimen A is a candle flame. Specimen B is a set of glow sticks. Both give off light. Under the trays are two tools: a thermometer that measures heat, and a dark box to check for light.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A bright yellow candle flame on a cream candle", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "Five glowing glow sticks in pink, yellow, green, and orange", "label": "Specimen B"}
  ],
  "materials": [{"key": "thermo", "label": "Thermometer (measures heat)", "swatch": "thermo"}, {"key": "box", "label": "Dark box (checks for light)", "swatch": "box"}],
  "ask": [
    {"q": "Which specimen has a real flame?", "ans": "A", "ok": "Yes. Specimen A is a candle with a flame.", "miss": "Look closely. Which one is burning?"},
    {"q": "Which specimen glows with no flame at all?", "ans": "B", "ok": "Yes. Specimen B is glow sticks. Nothing is burning.", "miss": "Look again. Which one glows without fire?"}
  ],
  "press": "🎯 Run the test",
  "testDo": "Put the thermometer under one tray and the dark box under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. Never touch a flame or put a thermometer in one; an adult does that test.",
  "results": {
    "Athermo": {"text": "The thermometer climbs fast! The flame gives off lots of heat.", "fx": "warm"},
    "Abox": {"text": "In the dark box, the flame lights everything up. It gives off light.", "fx": "glow"},
    "Bthermo": {"text": "The thermometer hardly moves. The glow sticks give off almost no heat.", "fx": "none"},
    "Bbox": {"text": "In the dark box, the glow sticks shine. They give off light.", "fx": "glow"}
  },
  "best": ["Athermo", "Bthermo"],
  "frame": "When I held the thermometer near it, the temperature ___, so it gives off ___.", "claimLead": "When I held the thermometer near it, the temperature", "claimMid": "so it gives off",
  "claim": {
    "A": {"feat": ["went way up", "hardly changed"], "featOk": 0, "eat": ["light and heat", "light but almost no heat"], "eatOk": 0},
    "B": {"feat": ["went way up", "hardly changed"], "featOk": 1, "eat": ["light and heat", "light but almost no heat"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Light and heat.</b> A flame gives off light and lots of heat, like a light bulb or the Sun.",
    "B": "<b>Cold light.</b> Glow sticks make light from a chemical change, with almost no heat."
  },
  "missFeat": "Look at your thermometer test for {label} again. Did the temperature go up?",
  "missClaim": "Think about your test. Did it give off heat, or only light?",
  "done": "Things that give off light often give off heat too, but not always. The thermometer tells us for sure.",
  "after": {"kicker": "🎬 Behind the scenes · Living lights", "img": "aft", "alt": "A firefly in flight with its tail glowing bright yellow-green",
            "html": "Fireflies make light inside their bodies, with almost no heat. Scientists call it \"cold light.\" On summer nights in Florida, you can watch them blink."}
}

wall = {
  "kicker": "🔭 The Star Elevator", "title": "From our closest star out to the far stars",
  "look": "A model elevator with four stops, from the Sun, our closest star, out to stars far away. Each stop has a real photo. The brass dial on the left shows how far out each stop is.",
  "do": "First, make a prediction. Then brush the glowing step: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "Is the Sun a star?",
              "options": [["yes", "Yes, the Sun is a star"], ["no", "No, the Sun is something different"]], "answer": "yes",
              "mine": "Your prediction: <b>{p}</b>. Let's ride the elevator and find out.",
              "confirm": "You predicted the Sun is a star. You were right: it is the closest star to Earth.",
              "change": "You predicted the Sun is something different. The elevator changed that idea: the Sun is a star, the closest one to Earth."},
  "sky": "sky", "skyAlt": "The Milky Way stretches over a dark road and grassland at night", "skyCap": "The Milky Way over Everglades National Park, Florida",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Distance", "Closest", "Night sky", "Telescope", "Far stars"],
  "line": ["OUR CLOSEST STAR", "FAR-AWAY STARS"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We go one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Keep going. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the elevator. The Sun is one star among many. It looks biggest and brightest only because it is the closest.",
  "rule": "<b>The Sun is a star, and the closest one to Earth.</b> Other stars are so far away they look like tiny points of light. Stars come in different sizes, colors, and brightness, and telescopes show many more of them.",
  "choices": ["☀️ The closest star, so it looks big and bright", "✨ Stars that look like tiny points of light", "🔭 Many more stars, seen through a telescope", "🎨 Stars of different colors"],
  "layers": [
    {"name": "Stop 1 · The Sun", "rock": "haze", "img": "l1", "alt": "The Sun as a glowing orange ball with bright, swirling spots, photographed by a space telescope",
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "The Sun is a star: a huge ball of hot, glowing gas. It is about 150 million kilometers away. That's close for a star, so it looks big and bright.",
     "ans": 0, "ok": "Yes! The Sun is the closest star, so it looks big and bright.", "tag": "☀️ Closest star",
     "miss": {"1": "Not quite. Does the Sun look like a tiny point of light?", "2": "Not yet. You don't need a telescope to see the Sun.", "3": "Close! But read the clue: why does the Sun look so big?"},
     "env": "e1", "envAlt": "Sunshine on a wide white beach and a long wooden pier", "envCap": "The Sun's light and heat at Clearwater Beach, Florida"},
    {"name": "Stop 2 · The night sky", "rock": "night", "img": "l2", "alt": "The stars of Orion in a dark sky, with three stars in a row in the middle",
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "At night, with just your eyes, stars look like tiny points of light. Many are bigger than the Sun, but they are so far away that they look small.",
     "ans": 1, "ok": "Yes! Far-away stars look like tiny points of light.", "tag": "✨ Night sky · tiny points",
     "miss": {"0": "Not this one. These stars are far, far away.", "2": "Not yet. This photo is how the sky looks to your eyes.", "3": "Close! But read the clue: how do these stars look to your eyes?"},
     "env": "e2", "envAlt": "The Milky Way glows over dark water and a lone tree", "envCap": "Stars over Flamingo, Everglades National Park, Florida"},
    {"name": "Stop 3 · Through a telescope", "rock": "space", "img": "l3", "alt": "A cluster of bright blue stars wrapped in glowing blue haze, with hundreds of smaller stars around it",
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "With your eyes, this star group looks like about 6 stars. A telescope gathers more light, and the 6 turn into hundreds!",
     "ans": 2, "ok": "Yes! A telescope shows many more stars than your eyes can see.", "tag": "🔭 Telescope · many more stars",
     "miss": {"0": "Not this one. The Sun isn't in this photo.", "1": "Close! But read the clue: what did the telescope show?", "3": "Not yet. Read the clue: is it about colors, or about how many?"},
     "env": "e3", "envAlt": "A white telescope dome lit red at night under a starry sky", "envCap": "Custer Astronomical Observatory · Southold, New York"},
    {"name": "Stop 4 · Star colors", "rock": "space", "img": "l4", "alt": "Two stars side by side in a telescope: one gold and one blue",
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "Stars are not all the same. Through a telescope, this pair of stars looks gold and blue. Some stars are bigger than the Sun, and some are smaller.",
     "ans": 3, "ok": "Yes! Stars come in different colors and sizes.", "tag": "🎨 Far stars · different colors",
     "miss": {"0": "Not this one. These stars are far away.", "1": "Close! But read the clue: what is different about these two?", "2": "Close! A telescope took it, but the clue is about the colors."},
     "env": "e4", "envAlt": "The Hubble Space Telescope floating in space above Earth", "envCap": "The Hubble Space Telescope · in orbit above Earth, 2009"}
  ],
  "mix": {
    "q": "Zoe says, \"The Sun can't be a star. Stars are tiny dots, and the Sun is huge.\" Is Zoe right?",
    "options": [
      {"t": "Yes. The Sun is too big to be a star.", "miss": "Think about Stop 2. Why do other stars look like tiny dots?"},
      {"t": "No. The Sun is a star. It only looks bigger because it is much closer to us.", "ok": "Yes! Other stars look tiny because they are so far away. Many of them are even bigger than the Sun."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Lightning Towers at the Launch Pad",
  "img": "wow", "alt": "A bolt of lightning hits the top of a tall tower beside a rocket launch pad",
  "caption": "Lightning hits a tower at Launch Pad 39B, Kennedy Space Center, Florida (2019)",
  "html": "<p style=\"margin:0 0 8px\">Kennedy Space Center sits in the lightning capital of the United States. So its launch pads have tall lightning towers.</p><p style=\"margin:0\">When lightning strikes, a tower catches the bolt and sends its electrical energy safely down into the ground, away from the rocket.</p>",
  "inset": "inset", "insetCap": "Lightning strikes beside the Artemis I rocket at Pad 39B, April 2022."}

keyIdea = "Energy is the ability to cause change. It comes in forms like light, heat, sound, motion, and electrical energy, and it can change from one form to another. Things that give off light often give off heat too, and rubbing things together changes motion energy into heat. The Sun is a star; it looks big and bright because it is the closest star to Earth."

IN = [["light", "☀️ Light energy goes in"], ["electrical", "🔌 Electrical energy goes in"], ["motion", "🏃 Motion energy goes in"], ["heat", "🔥 Heat from burning fuel goes in"]]


def card(id_, img, alt, clues, org, orgAns, orgShort, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": org, "orgAns": orgAns, "orgShort": orgShort, "orgMiss": orgMiss,
            "env": dict(IN)[envAns].split(" ", 1)[1].replace(" goes in", ""), "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}


det = {
  "look": "Five real places where energy changes from one form to another. Each card shows what scientists saw. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 files, one at a time. Tap a clue, then name the energy that comes out. Predict the energy that goes in, and watch the place appear.",
  "noun": "File", "need": 3, "inferQ": "What energy comes out?", "inferDone": "Out comes", "chartSo": "so out comes",
  "predict": {"q": "Which energy do you predict goes in?", "options": IN},
  "kicker": "The place today", "enough": "You already solved 3 energy change files. Nice work, scientist!",
  "cols": ["File", "My observation", "Energy out", "Energy in", "My evidence"],
  "write": {"label": "File __ shows ___. Energy changes from ___ to ___, because ___.", "starter": "Start with: \"File __ shows…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["form", "Names a form of energy"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "Rows of dark blue solar panels tilted toward the sky",
         [{"t": "Rows of solar panels soaking up sunshine", "ok": True}, {"t": "A rocket blasting off", "miss": "Look again. Is anything moving?"}, {"t": "People playing drums", "miss": "Look again. Do you see any people?"}],
         ["🔌 Electrical energy", "🔊 Sound energy", "❄️ Cold"], 0, "electrical energy",
         "Solar panels send power through wires to homes. Which form of energy flows through wires? Try again.",
         "light", "The panels face the sky to catch sunshine. Which energy goes in? Try again.",
         "d1h", "A huge solar farm seen from the air, with rows of panels beside ponds and forest", "A solar farm at Kennedy Space Center, Florida",
         "This solar farm changes the Sun's light energy into electrical energy. Wires carry it to homes and businesses in Florida.", "solar",
         "Solar panels work best in sunny places. That's one reason Florida is called the Sunshine State."),
    card("B", "d2", "A space shuttle lifting off its launch pad in a giant cloud of smoke and fire",
         [{"t": "A space shuttle rising up off the pad", "ok": True}, {"t": "Solar panels in a field", "miss": "Look again. Is it sitting still?"}, {"t": "Wind turbines turning", "miss": "Look again. What is moving up?"}],
         ["🏃 Motion energy", "🔌 Electrical energy from a plug", "❄️ Cold"], 0, "motion energy",
         "The shuttle zooms up into the sky. Which form of energy is moving energy? Try again.",
         "heat", "The engines burn fuel and make super-hot gas. Which energy goes in? Try again.",
         "d2h", "Two launch pads by the ocean, each with a space shuttle standing on it", "Launch pads at Kennedy Space Center, Florida, 2009",
         "Burning fuel makes hot gas that rushes out of the engines and pushes the shuttle up. The launch also makes lots of light, heat, and sound!", "launch",
         "This shuttle, Atlantis, flew in May 2009 to fix the Hubble Space Telescope."),
    card("C", "d3", "Two old light bulbs: one with a glowing orange wire inside, one turned off",
         [{"t": "A thin wire glowing orange inside the bulb", "ok": True}, {"t": "Metal drums being played", "miss": "Look again. Do you see any drums?"}, {"t": "Wind turbines", "miss": "Look again. What is glowing?"}],
         ["☀️🔥 Light and heat", "🔊 Sound only", "🏃 Motion only"], 0, "light and heat",
         "The wire glows, and the bulb gets very hot. Which choice has both? Try again.",
         "electrical", "The bulb is plugged into wires. Which energy goes in? Try again.",
         "d3h", "Wooden shelves full of glass jars and old tools in a long workshop", "Thomas Edison's laboratory · Fort Myers, Florida, today",
         "Old light bulbs change electrical energy into light, and most of it into heat. Thomas Edison worked on bulbs like these and had a lab in Fort Myers, Florida.", "lab",
         "Edison spent his winters in Fort Myers. You can visit his lab there today."),
    card("D", "d4", "Musicians in yellow shirts playing shiny steel drums",
         [{"t": "Players hitting shiny steel drums with sticks", "ok": True}, {"t": "A glowing bulb", "miss": "Look again. Is anything glowing?"}, {"t": "Solar panels", "miss": "Look again. Who is playing?"}],
         ["🔊 Sound energy", "☀️ Light energy", "🔌 Electrical energy"], 0, "sound energy",
         "When the sticks hit the drums, the metal vibrates. What do you hear? Try again.",
         "motion", "The players swing their sticks and hit the drums. Which energy goes in? Try again.",
         "d4h", "A city of houses around a big green park, with hills behind it", "Port of Spain, Trinidad and Tobago",
         "Hitting a steel drum changes motion energy into sound energy. The steel drum was invented in Trinidad and Tobago.", "carnival",
         "Steel drums are made from big metal barrels, hammered into shape."),
    card("E", "d5", "A long line of tall white wind turbines in a green field",
         [{"t": "Tall wind turbines with spinning blades", "ok": True}, {"t": "A rocket blasting off", "miss": "Look again. Is anything blasting off?"}, {"t": "A candle flame", "miss": "Look again. Is anything burning?"}],
         ["🔌 Electrical energy", "🔥 Heat only", "🔊 Sound only"], 0, "electrical energy",
         "Wind turbines send power down wires to homes. Which energy flows through wires? Try again.",
         "motion", "Moving air spins the blades. Which energy goes in? Try again.",
         "d5h", "Wind turbines and an old farm windmill beside a green field", "Roscoe Wind Farm · West Texas",
         "Moving air pushes the blades around. A machine inside changes that motion energy into electrical energy.", "windfarm",
         "Long ago, farm windmills used wind to pump water. Today's turbines make electricity.")
  ]
}

rebuild = {"title": "Use your evidence to rebuild the scene", "missPrefix": "Hmm. Look at your energy file again. ", "kicker": "🌍 Rebuild the scene", "whyStart": "I chose this because the energy…",
  "envs": [
    {"key": "solar", "name": "☀️ A Florida solar farm", "img": "d1h", "cap": "Sunshine to power…"},
    {"key": "launch", "name": "🚀 A launch pad", "img": "d2h", "cap": "Fuel to motion…"},
    {"key": "lab", "name": "💡 Edison's lab", "img": "d3h", "cap": "Wires to glow…"},
    {"key": "carnival", "name": "🥁 A steel drum band", "img": "d4h", "cap": "Sticks to music…"},
    {"key": "windfarm", "name": "🌬️ A wind farm", "img": "d5h", "cap": "Wind to power…"}
  ],
  "life": [
    {"name": "☀️ Solar panels making power", "img": "d1", "env": "solar", "miss": "Solar panels belong at the solar farm."},
    {"name": "🚀 A shuttle lifting off", "img": "d2", "env": "launch", "miss": "The shuttle lifts off from the launch pad."},
    {"name": "💡 A glowing bulb", "img": "d3", "env": "lab", "miss": "The glowing bulb belongs in Edison's lab."},
    {"name": "🥁 Ringing steel drums", "img": "d4", "env": "carnival", "miss": "The drums belong with the band."},
    {"name": "🌬️ Spinning turbines", "img": "d5", "env": "windfarm", "miss": "The turbines belong at the wind farm."}
  ]}

quiz = [
  {"q": "Which of these is a form of energy?", "options": [
    {"t": "Weight", "miss": "Think about what makes things move, warm up, or glow. Which option describes something that causes change?"},
    {"t": "Heat", "ok": "🌲 Correct! Heat is a form of energy. Other forms include light, sound, motion, and electrical energy."},
    {"t": "Color", "miss": "Think about what makes things move, warm up, or glow. Which option describes something that causes change?"}]},
  {"q": "What energy change happens when you turn on a flashlight?", "options": [
    {"t": "Electrical energy changes to light energy", "ok": "🌲 Yes! A flashlight uses electrical energy from batteries and changes it into light energy."},
    {"t": "Sound energy changes to heat energy", "miss": "A flashlight uses batteries. What form of energy do batteries have? What does the flashlight produce?"},
    {"t": "Light energy changes to motion energy", "miss": "A flashlight uses batteries. What form of energy do batteries have? What does the flashlight produce?"}]},
  {"q": "A student rubs her hands together quickly and they feel warm. What happened?", "options": [
    {"t": "Sound energy was created", "miss": "Rubbing is a type of movement. What form of energy is movement? What form of energy is warmth?"},
    {"t": "Light energy changed to heat energy", "miss": "Rubbing is a type of movement. What form of energy is movement? What form of energy is warmth?"},
    {"t": "Motion energy changed to heat energy", "ok": "🌲 Exactly! Rubbing your hands is motion, and that motion energy changes into heat energy through friction (the rubbing of two things together)."}]}
]

partA = {"title": "Energy forms chart", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  {"n": 1, "q": "The Sun: which forms of energy does it give off, warming Earth and lighting the day?", "type": "choice", "options": [
    {"t": "Sound energy only", "miss": "Can we hear the Sun? What do we feel and see from it?"},
    {"t": "Light and heat energy", "ok": "Yes. The Sun gives off light and heat. It lights our days and warms Earth."},
    {"t": "Electrical energy only", "miss": "The Sun isn't plugged into wires. What do we feel and see from it?"}]},
  {"n": 2, "q": "A guitar: when you strum the strings, which form of energy comes out?", "type": "choice", "options": [
    {"t": "Light energy", "miss": "Does a guitar glow? What do you hear?"},
    {"t": "Electrical energy", "miss": "A plain guitar has no wires. What do you hear?"},
    {"t": "Sound energy", "ok": "Yes. Strumming makes the strings vibrate, and motion energy changes into sound energy."}]},
  {"n": 3, "q": "A toaster: electrical energy goes in. Which form of energy comes out to toast the bread?", "type": "choice", "options": [
    {"t": "Heat energy", "ok": "Yes. A toaster changes electrical energy into heat energy, and the bread turns brown."},
    {"t": "Sound energy", "miss": "What makes bread turn brown and crispy?"},
    {"t": "Motion energy", "miss": "The toaster doesn't move the bread around. What makes it brown and crispy?"}]}
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "Describe one example of energy changing from one form to another.", "type": "text", "min": 12, "chips": [["form", "Names two forms of energy"], ["chg", "Says how it changes (changes into, becomes)"]]},
    {"n": 2, "q": "The Sun is the closest star to Earth. Why does that make it look bigger and brighter than the stars you see at night?", "type": "text", "min": 12, "chips": [["close", "Says the Sun is close"], ["far", "Says other stars are far away"]]}
  ]},
  "write": {"title": "How does energy cause things to change and move? Use examples from your energy files.", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["energy", "heat energy", "motion energy"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think energy causes change because…\""],
                ["What did you observe or learn that supports your thinking?", "Start with: \"I know this because in my energy files I found…\""],
                ["Why does that make sense?", "Start with: \"One example of energy causing change is…\""]]},
  "partC": {"do": "Draw a scene from your home or school that shows at least three forms of energy in action. Label each form of energy and draw arrows showing any energy changes.",
            "labels": ["One form of energy in my scene and what it does", "One energy change in my scene, from what to what"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 energy change files and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: my energy forms chart.", "req": {"choice": ["a1", "a2", "a3"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my energy story", "thinkLabel": "The energy that came out was", "director": "JUNIOR ENERGY SCIENTIST", "storyKicker": "My energy story",
  "frames": [
    {"k": "formation", "label": "Bolt to Boom", "img": "o2", "cap": "Bolt to Boom: charge, bolt, flash, thunder."},
    {"k": "compare", "label": "The Glow Test", "img": "ta", "cap": "The Glow Test: light often brings heat, but not always."},
    {"k": "wall", "label": "The Star Elevator", "img": "l1", "cap": "The Star Elevator: the Sun is our closest star."},
    {"k": "det", "label": "Energy change files", "img": "d1", "cap": "Energy change files: what goes in, what comes out?"}]}

nxt = {"title": "Coming up next: 28.02", "text": "Investigation: Light, Reflection, Absorption, and Heat. Next time, test how light travels, bounces, and gets soaked up, and how rubbing makes heat."}

chips = {
  "part": {"any": ["glass", "glassy", "shiny", "smooth", "rough", "sand", "sandy", "holes", "bubbles", "hole", "tube", "groove", "gray", "grey", "white", "edge", "inside", "outside", "rock", "melted", "hollow", "black", "broken"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["solar", "panel", "panels", "sun", "sunshine", "rocket", "shuttle", "fire", "smoke", "bulb", "wire", "glow", "glowing", "drum", "drums", "steel", "sticks", "wind", "turbine", "turbines", "blades", "spinning", "launch"]},
  "form": {"any": ["light", "heat", "sound", "motion", "electrical", "electric", "electricity", "mechanical", "energy"]},
  "chg": {"any": ["changes", "change", "changed", "becomes", "become", "turns", "turned", "into", "makes", "made"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "close": {"any": ["close", "closer", "closest", "near", "nearer", "nearest"]},
  "far": {"any": ["far", "farther", "further", "away", "distant", "tiny", "small", "dots", "points"]}
}

L = {"id": "g3sci-28-01", "lesson": "28.01", "title": "How Does Energy Cause Change?", "emoji": "⚡",
  "details": ["📅 Q4 · Unit 9 · Matter &amp; Energy", "📖 Week 28 · Lesson 28.01", "🌎 CPALMS SC.3.P.10.1, SC.3.P.10.2, SC.3.P.11.1, SC.3.P.11.2, SC.3.N.3.1, SC.3.E.5.1, SC.3.E.5.2, SC.3.E.5.3, SC.3.E.5.5", "⏱ About 35 minutes"],
  "icans": ["name different forms of energy such as light, heat, sound, and motion.", "explain how energy causes objects to move or change.", "give examples of energy at work in everyday life."],
  "opti": {"warm": "Our film starts in a Florida thunderstorm. First, inspect a strange tube of glass found in the sand.",
           "lesson": "Today you're an energy scientist. Follow a lightning bolt, test two glowing things, then ride up to the stars.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Match each energy, then draw energy at work in your own home."},
  "film": film, "scientist": "energy scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: A Night on the Bare Mountain (Modest Mussorgsky), public domain recording (Musopen, via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The lightning movie, the Glow Test, and the Star Elevator are models; every place photo is real."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-28-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the tube, then tap three things you notice."},
  "how-28-01-compare": {"page": "Put the thermometer under one tray and the dark box under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the thermometer under one tray and the dark box under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-28-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-28-01-det": {"page": det["do"], "say": "Pick three files, one at a time. Tap a clue, then name the energy that comes out. Predict the energy that goes in, and watch the place appear."},
  "how-28-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"28-01-welcome": L["opti"]["warm"], "28-01-lesson": L["opti"]["lesson"], "28-01-check": L["opti"]["check"], "28-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/meta.json'))
json.dump([dict(key=k, **meta[k]) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
