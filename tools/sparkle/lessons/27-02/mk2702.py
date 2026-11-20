#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/27-02/lesson.json, how-lines.json, scripts.json, credits.json (27.02: no voices recorded; scripts only)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


film = {
  "id": "g3sci-27-02", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 27.02 · Investigation: Heating, Cooling, and Water Changes",
  "title": "Steaming Springs",
  "bigQuestion": "What happens to water when you heat it up or cool it down?",
  "poster": "f_glades", "endPoster": "f_run", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.6},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 4.0, "type": "black", "sfxAt": [{"at": 0.3, "name": "bubbles"}, {"at": 1.6, "name": "bubbles"}, {"at": 2.9, "name": "bubbles"}], "fade": 0.5},
    ph(7.4, 6.2, "f_glades", "A white egret stands in tall golden grass while a soft mist floats over the marsh behind it", "Everglades National Park, Florida · A November morning",
       frm=(1.12, .5, .5), to=(1.0, .5, .55), fade=1.0, fx=["rays"]),
    ph(13.6, 6.0, "f_woodruff", "Calm blue pond water with a thin white mist lying on it at sunrise", "Lake Woodruff, near DeLand, Florida · Early morning",
       frm=(1.0, .5, .5), to=(1.12, .55, .6)),
    {"t": 19.6, "d": 7.4, "type": "split", "img": "f_alicefog", "alt": "A white mist lying low over a still lake at dusk, with orange trees behind it",
     "img2": "f_alice", "alt2": "The same lake on a clear, sunny day, with no mist on the water",
     "splitAt": 3.6, "splitDur": 2.4, "lab1": "Lake Alice · a cold January evening", "lab2": "Lake Alice · a sunny day",
     "from": [1.0, .5, .5], "to": [1.06, .5, .5], "fade": 0.6, "sfxAt": [{"at": 3.6, "name": "whoosh"}]},
    ph(27.0, 6.2, "f_manatee", "Many gray manatees resting close together under clear spring water", "Blue Spring State Park, Florida · February",
       frm=(1.0, .5, .5), to=(1.1, .5, .5), fx=["caustics"]),
    ph(33.2, 5.8, "f_run", "Clear blue-green spring water flowing between trees hung with Spanish moss", "Blue Spring Run, Orange City, Florida",
       frm=(1.1, .5, .5), to=(1.0, .5, .5)),
    ph(39.0, 6.4, "f_wekiwa", "Swimmers float in a clear green spring surrounded by tall trees on a sunny summer day", "Wekiwa Springs State Park, Florida · A July afternoon",
       frm=(1.0, .5, .5), to=(1.08, .5, .5), fade=0.9),
    {"t": 45.4, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 3.4, "text": "Listen. Something is bubbling.", "voice": "opti-1"},
    {"t": 7.8, "d": 5.6, "text": "Dawn in the Everglades. A soft white mist floats over the grass.", "voice": "opti-2"},
    {"t": 14.0, "d": 5.4, "text": "At Lake Woodruff, mist curls up off the water.", "voice": "opti-3"},
    {"t": 20.0, "d": 3.4, "text": "Cold air, and a white cloud sits on the lake.", "voice": "opti-4"},
    {"t": 23.8, "d": 3.0, "text": "Sunny and warm? The cloud is gone.", "voice": "opti-5"},
    {"t": 27.4, "d": 5.6, "text": "In winter, manatees crowd into Blue Spring. Its water stays warm all year.", "voice": "opti-6"},
    {"t": 33.6, "d": 5.2, "text": "On cold mornings, mist rises off the spring, like steam from a pot.", "voice": "opti-7"},
    {"t": 39.4, "d": 2.6, "text": "Steam? From a Florida spring?", "voice": "opti-8"},
    {"t": 42.2, "d": 3.6, "text": "What happens to water when you heat it up or cool it down?", "voice": "opti-9"}
  ]
}

specimen = {
  "img": "spec", "aspect": "3/2", "radius": 0.07,
  "hotspots": [
    {"name": "A big ice cube poking out the top", "x": 0.64, "y": 0.30},
    {"name": "A yellow straw", "x": 0.26, "y": 0.24},
    {"name": "A round, clear rim", "x": 0.83, "y": 0.60},
    {"name": "A foggy, cloudy outside", "x": 0.40, "y": 0.90},
    {"name": "Ice under the water", "x": 0.70, "y": 0.82}
  ],
  "kicker": "🔎 Mystery specimen", "title": "What's on the outside of this cup?",
  "alt": "A clear plastic cup full of ice water and big ice cubes, with a yellow straw. The lower part of the cup looks foggy.",
  "look": "A close-up photo of one real thing: a cup of ice water on a warm day. Look at its parts: the ice, the straw, the rim, and the outside of the cup. A specimen is one real thing that scientists study. Something is happening on the outside. That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the cup, then tap 3 things you notice.",
  "number": "No. 27.02-A",
  "card": ["<b>Specimen A</b>", "Found: on a table outside, on a warm day", "Inside: ice and water", "The foggy outside? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🌡️", "temperature", "How hot or cold something is. A thermometer measures temperature."],
  ["🔥", "heat energy", "Energy that makes things warmer. Adding heat energy raises the temperature."],
  ["🫧", "boiling", "When a liquid gets so hot that bubbles of gas form all through it. Pure water boils at 100 °C."],
  ["💨", "water vapor", "Water as a gas. You can't see it, but it is in the air all around you."],
  ["💧", "condensation", "When a gas cools and turns back into a liquid. Water drops on a cold glass are condensation."],
  ["🔍", "observation", "Something you notice with your senses. Scientists make careful observations."],
  ["📊", "data", "Information you collect, like measurements and notes. Scientists record data to find patterns."]
]

parts = [
  {"kicker": "🌱 Part 1", "title": "Temperature and Water",
   "html": "<p>Water can be a solid (ice), a liquid, or a gas (water vapor). Temperature decides which one. A thermometer measures temperature in degrees. Pure water freezes at 0 °C and boils at 100 °C.</p><p>Scientists record data, like temperatures and what they see. Data helps them find patterns.</p>"},
  {"kicker": "🌤 Part 2", "title": "Heating Water",
   "html": "<p>When you add heat energy, water gets warmer. Ice melts into liquid water. Keep heating, and the water boils. Big bubbles form all through it. They are not air. They are water vapor.</p><p>Water vapor is invisible. The white cloud you see over a pot is tiny drops that formed when the vapor cooled. That's condensation!</p>"},
  {"kicker": "🌍 Part 3", "title": "Cooling Water",
   "html": "<p>Taking heat away works the other way. When water vapor touches something cold, like a lid or a cold glass, it condenses into drops. Water that gets cold enough freezes into ice.</p><p>The Sun heats the things it shines on, like the water in a puddle or a spring. When the Sun sets or hides behind a cloud, the water loses heat and cools down.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Thermometer Files"}
]

order = {
  "mix": [1, 3, 0, 2], "hint": "Start with the frozen ice.",
  "kicker": "🎞️ Put the scenes in order", "title": "What happens when you heat ice, then cool the steam?",
  "look": "Four real photos show water in the Pot Lab, from ice to drops on a lid. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "Two metal bowls full of crushed ice with metal scoops", "text": "Ice sits in a metal bowl. It is solid, at about 0 °C.", "play": "Solid ice.",
     "miss": ["", "The ice comes first. Try frame 1.", "The ice comes first. Try frame 1.", "The ice comes first. Try frame 1."]},
    {"img": "o2", "alt": "An ice cube melting into a flat puddle of water on a table", "text": "Heat is added, and the ice melts into liquid water.", "play": "It melts.",
     "miss": ["It has to be ice first. Try a later frame.", "", "It melts before it boils. Try an earlier frame.", "It melts before the steam. Try an earlier frame."]},
    {"img": "o3", "alt": "A pot of water boiling hard, seen from above", "text": "More heat. At 100 °C, the water boils.", "play": "It boils.",
     "miss": ["The ice must melt first. Try a later frame.", "The water melts first, then boils. Try a later frame.", "", "It boils before the drops form. Try an earlier frame."]},
    {"img": "o4", "alt": "Lots of small water drops on the underside of a clear glass lid", "text": "Steam hits a cool glass lid and condenses into drops.", "play": "Drops form.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Drops cover the inside of the lid. Max says, \"The lid is leaking water.\" What do you think?",
    "options": [
      {"t": "Max is right. The lid leaks.", "miss": "Look at the last frame of the movie again. Where did the drops come from?"},
      {"t": "Water vapor from the pot cooled on the lid and condensed into drops.", "ok": "Yes! The water left the pot as water vapor, then turned back into liquid on the cool lid."}
    ]
  }
}

movie = {
  "model": "pot-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🌡️",
  "real": "real", "realAlt": "Water boiling in a steel pot with a glass lid on an electric stove",
  "stamp": "WATER CAME BACK!", "endCap": "A real boiling pot.",
  "beats": [
    {"at": 0, "cap": "1 · Solid ice.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["0 °C"]},
    {"at": 2600, "cap": "2 · It melts.", "model": {"show": "s2"}, "counter": ["20 °C"]},
    {"at": 5200, "cap": "3 · It boils.", "model": {"show": "s3"}, "counter": ["100 °C"], "sfx": "bubbles"},
    {"at": 7800, "cap": "4 · Drops on the lid.", "model": {"show": "s4"}, "counter": ["100 °C"], "sfx": "shimmer"},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Drip Test", "title": "Where do the drops come from?",
  "look": "Two real specimens, each on a lit tray. Specimen A is a glass of ice water. Specimen B is a mug of a hot drink. Under the trays are two tools: a clear lid to hold on top, and a dry paper towel to wrap around the outside.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A glass of ice water with a cloudy, foggy outside", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A dark mug with steam curling up out of the top", "label": "Specimen B"}
  ],
  "materials": [{"key": "lid", "label": "Clear lid (held on top)", "swatch": "lid"}, {"key": "towel", "label": "Dry paper towel (wrapped around the outside)", "swatch": "towelstrip"}],
  "ask": [
    {"q": "Which specimen is colder than the air around it?", "ans": "A", "ok": "Yes. Specimen A is ice water. It is much colder than the air.", "miss": "Look closely. Which one has ice in it?"},
    {"q": "Which specimen has steam rising off it?", "ans": "B", "ok": "Yes. Specimen B is a hot drink. You can see steam rising.", "miss": "Look again. Which one has white steam curling up?"}
  ],
  "press": "🎯 Run the test",
  "testDo": "Put the lid on one specimen and the paper towel on the other: drag them, or tap one, then a specimen. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. In real life, the drops take a few minutes to form.",
  "results": {
    "Alid": {"text": "Almost nothing happens. Ice water gives off very little water vapor, so the lid stays dry.", "fx": "none"},
    "Atowel": {"text": "The towel gets damp on the outside! Water vapor in the air cooled on the cold glass and condensed.", "fx": "wet"},
    "Blid": {"text": "Drops form under the lid! Water vapor from the hot drink cooled on the lid and condensed.", "fx": "wet"},
    "Btowel": {"text": "The towel stays dry. The warm mug is not colder than the air, so no drops form on it.", "fx": "warm"}
  },
  "best": ["Atowel", "Blid"],
  "frame": "The drops came from ___, which ___.", "claimLead": "The drops came from", "claimMid": "which",
  "claim": {
    "A": {"feat": ["water leaking out of the glass", "water vapor in the air"], "featOk": 1, "eat": ["condensed on the cold glass", "melted out of the ice"], "eatOk": 0},
    "B": {"feat": ["water leaking out of the mug", "water vapor from the hot drink"], "featOk": 1, "eat": ["condensed under the cool lid", "froze on the lid"], "eatOk": 0}
  },
  "curator": {
    "A": "<b>Not a leak!</b> The towel got wet on the outside. Water vapor in the air touched the cold glass and condensed.",
    "B": "<b>Steam to drops.</b> Water vapor from the hot drink cooled on the lid and condensed into drops."
  },
  "missFeat": "Look at your test for {label} again. Where did the water come from?",
  "missClaim": "Think about your test. Did the water vapor cool into drops, or did something melt or freeze?",
  "done": "Condensation happens when water vapor cools. A cold glass and a cool lid both turn water vapor into drops.",
  "after": {"kicker": "🎬 Behind the scenes · Catching fog", "img": "aft", "alt": "People stand beside a big net stretched between two poles on a hilltop above a sea of white fog",
            "html": "Fog is a cloud of tiny drops that formed when water vapor cooled. In Chile's dry Atacama Desert, scientists hang big nets on foggy hills. The drops stick to the nets, run down into gutters, and give people water."}
}

wall = {
  "kicker": "♨️ The Steam Tower", "title": "From high in the air down to the bottom of a boiling pot",
  "look": "A model tower of four steps over a pot of boiling water, from high in the air at the top down to the bottom of the pot. Each step has a real photo. The brass dial on the left shows where each step is.",
  "do": "First, make a prediction. Then brush the glowing step: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "What do you predict is inside the big bubbles in boiling water?",
              "options": [["air", "Air"], ["vapor", "Water vapor, a gas"]], "answer": "vapor",
              "mine": "Your prediction: <b>{p}</b>. Let's climb down and find out.",
              "confirm": "You predicted water vapor. You were right: the big bubbles are water that turned into a gas.",
              "change": "You predicted air. The tower changed that idea: the big bubbles are water vapor, water that turned into a gas."},
  "sky": "sky", "skyAlt": "Steam rising from a hot spring pool at sunrise", "skyCap": "Crested Pool at sunrise · Yellowstone National Park",
  "unit": "Step", "found": "Clue found at Step {n}",
  "elevator": ["Height", "High up", "Just above", "Surface", "Pot bottom"],
  "line": ["HIGH IN THE AIR", "DEEP IN THE POT"],
  "lockTag": "🔒 Brush the step above first", "locked": "Brush the step above first. We go one step at a time.",
  "first": "Brush the glowing top step. Drag across it (or tap it again and again).", "next": "Keep going. Brush Step {n}.",
  "endTitle": "All 4 steps explored",
  "endText": "Look at the tower. Heat at the bottom turns water into water vapor. Up in the cooler air, the vapor condenses into a white cloud of drops.",
  "rule": "<b>Heating turns liquid water into water vapor. Cooling turns it back into liquid drops.</b> The bubbles in boiling water are water vapor, and the white steam cloud is tiny drops of liquid.",
  "choices": ["☁️ Tiny liquid drops (condensation)", "💨 Water vapor, a gas you can't see", "♨️ Water boiling at 100 °C", "🫧 Bubbles of water vapor"],
  "layers": [
    {"name": "Step 1 · The white cloud", "rock": "cloud", "img": "l4", "alt": "Thick white clouds of steam drifting through a dark kitchen",
     "ask": "Look at Step 1. Read the clue AND the photo. What do you find?",
     "clue": "This white cloud is made of billions of tiny drops of liquid water. Water vapor cooled in the air and condensed.",
     "ans": 0, "ok": "Yes! The white cloud is tiny drops of liquid water.", "tag": "☁️ High up · tiny drops",
     "miss": {"1": "Not quite. Can you see this cloud? Then it isn't the invisible gas.", "2": "Not yet. This step is up in the air, not in the pot.", "3": "Not yet. These are not bubbles in water."},
     "env": "e4", "envAlt": "A tall white cloud of steam rising from a geyser next to dark pine trees", "envCap": "Old Faithful Geyser's steam cloud · Yellowstone National Park"},
    {"name": "Step 2 · Just above the pot", "rock": "haze", "img": "l3", "alt": "A pressure cooker on a stove with jets of steam shooting out of its top",
     "ask": "Look at Step 2. Read the clue AND the photo. What do you find?",
     "clue": "Right where the steam leaves the pot, it is thin and hard to see. That part is water vapor, a gas. It turns white only after it cools.",
     "ans": 1, "ok": "Yes! Right at the pot, the water vapor is a gas you can't see.", "tag": "💨 Just above · water vapor",
     "miss": {"0": "Close! The white cloud is farther out. Read the clue: what is right at the pot?", "2": "Not yet. This step is above the water.", "3": "Not yet. These are not bubbles in water."},
     "env": "e3", "envAlt": "Calm blue-green Gulf water and a clear sky", "envCap": "Air over the Gulf, full of water vapor you can't see · Mexico Beach, Florida"},
    {"name": "Step 3 · The water's surface", "rock": "water1", "img": "l2", "alt": "A glass kettle full of water boiling hard, with steam at the top",
     "ask": "Look at Step 3. Read the clue AND the photo. What do you find?",
     "clue": "The thermometer reads 100 °C. The water is boiling: it turns into gas all through the kettle, not just on top.",
     "ans": 2, "ok": "Yes! At 100 °C, the water is boiling.", "tag": "♨️ Surface · boiling",
     "miss": {"0": "Not yet. Read the clue: how hot is the water?", "1": "Close! But this step is about the water itself.", "3": "Close! Bubbles are coming. This step is about the whole pot boiling."},
     "env": "e2", "envAlt": "A hot spring pool churning and splashing as it boils, with steam rising", "envCap": "Churning Caldron, a boiling hot spring · Yellowstone National Park"},
    {"name": "Step 4 · The bottom of the pot", "rock": "water3", "img": "l1", "alt": "Hundreds of round bubbles on the bottom of a pot of very hot water",
     "ask": "Look at Step 4. Read the clue AND the photo. What do you find?",
     "clue": "Big bubbles start where the hot bottom of the pot heats the water. They are not air. They are pockets of water vapor that rise and pop.",
     "ans": 3, "ok": "Yes! The big bubbles are water vapor.", "tag": "🫧 Pot bottom · vapor bubbles",
     "miss": {"0": "Not yet. These are under the water, not up in the air.", "1": "Close! It is water vapor, but here it is trapped in something. What?", "2": "Not quite. Look at the round shapes in the photo."},
     "env": "e1", "envAlt": "Boiling water bursting up in a hot spring pool", "envCap": "Boiling water in Crested Pool · Yellowstone National Park"}
  ],
  "mix": {
    "q": "Ava says, \"The bubbles in boiling water are air bubbles.\" Is Ava right?",
    "options": [
      {"t": "Yes. The bubbles are air.", "miss": "Think about Step 4. What did the clue say the big bubbles are?"},
      {"t": "No. The big bubbles are water vapor: water that turned into a gas.", "ok": "Yes! When water boils, some of it turns into water vapor, and that gas makes the bubbles."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Steam Trains to Key West",
  "img": "wow", "alt": "An old photo of a steam train puffing smoke and steam as it crosses a long bridge over the sea",
  "caption": "A steam train on the railroad to Key West, Florida (book photo, 1928)",
  "html": "<p style=\"margin:0 0 8px\">Long ago, many trains in Florida ran on steam! Inside the engine, a fire boiled water. The water vapor pushed hard on metal parts, and that turned the wheels.</p><p style=\"margin:0\">In 1912, steam trains began running all the way to Key West, on long bridges over the sea. People called it the railroad that went to sea.</p>",
  "inset": "inset", "insetCap": "A real steam locomotive on display in Boca Raton, Florida."}

keyIdea = "Temperature decides whether water is a solid, a liquid, or a gas. Adding heat energy melts ice and boils water into water vapor. Taking heat away condenses water vapor into drops and freezes water into ice. Scientists record temperatures and observations as data to find this pattern."

M = ["🔥 Melting (solid → liquid)", "❄️ Freezing (liquid → solid)", "☁️ Evaporation (liquid → gas, slowly, no bubbles)", "♨️ Boiling (liquid → gas, with big bubbles)", "💧 Condensation (gas → liquid)"]
SHORT = ["melting", "freezing", "evaporation", "boiling", "condensation"]
SOL = [["warm", "🌡️ Warming up (heat added)"], ["cool", "❄️ Cooling down (heat taken away)"]]


def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}


det = {
  "look": "Five real places where water changed state. Each file has a thermometer reading and an observation. That's data! Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 files, one at a time. Tap a clue, then name the change. Predict if it was warming up or cooling down, and watch the place appear.",
  "noun": "File", "need": 3, "inferQ": "Which change happened?", "inferDone": "Change", "chartSo": "so the change is",
  "predict": {"q": "Do you predict the water was warming up or cooling down?", "options": SOL},
  "kicker": "The place today", "enough": "You already solved 3 thermometer files. Nice work, scientist!",
  "cols": ["File", "My data", "Change", "Temperature", "My evidence"],
  "write": {"label": "File __ shows ___. It is ___, because ___.", "starter": "Start with: \"File __ shows…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["chg", "Names a change"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "A wide lake covered in white ice and snow under a deep blue sky",
         [{"t": "Thermometer: air −15 °C. The lake is hard, white ice.", "ok": True}, {"t": "Thermometer: 100 °C. Big bubbles everywhere.", "miss": "Look again. Is anything bubbling?"}, {"t": "Drops of water on a bottle", "miss": "Look again. Do you see any bottles?"}],
         1, "The lake water was liquid, and now it is solid ice. Which change is that? Try again.",
         "cool", "Ice forms when water gets very cold. Was it warming up or cooling down? Try again.",
         "d1h", "Blue lake water next to a dock and green grass on a summer day", "Lake Mendota · Madison, Wisconsin, in summer",
         "In winter, the air over Lake Mendota drops far below 0 °C. The lake water loses heat and freezes into a thick sheet of ice. In spring, it melts again.", "lake",
         "People in Madison have written down the days Lake Mendota freezes and thaws for more than 150 years. That's a lot of data!"),
    card("B", "d2", "Cold plastic bottles covered in tiny drops of water on the outside",
         [{"t": "Thermometer: bottle 4 °C, air 32 °C. Tiny drops cover the outside.", "ok": True}, {"t": "Thermometer: −15 °C. Thick ice.", "miss": "Look again. Is anything frozen solid?"}, {"t": "Hills of white salt", "miss": "Look again. What is on the bottles?"}],
         4, "The drops came from water vapor in the air. A gas turned into a liquid. Which change is that? Try again.",
         "cool", "The water vapor touched the cold bottle. Was it warming up or cooling down? Try again.",
         "d2h", "A white sand beach with a yellow lifeguard stand under a blue sky", "Siesta Key Beach · Sarasota, Florida",
         "On a hot Florida beach, the air is full of water vapor. When it touches a cold bottle from the cooler, it cools and condenses into drops. The bottle isn't leaking!", "beach",
         "These bottles were photographed in Seattle. The same thing happens on any warm, damp day."),
    card("C", "d3", "An old photo of two women stirring a big, steaming kettle of sugarcane juice under a shed",
         [{"t": "Thermometer: about 100 °C. The juice bubbles hard and steams.", "ok": True}, {"t": "Thermometer: 4 °C. Drops on a cold bottle.", "miss": "Look again. Is this hot or cold?"}, {"t": "Ice balls on green grass", "miss": "Look again. Do you see any ice?"}],
         3, "The juice is bubbling hard as its water turns into gas. Which change has big bubbles? Try again.",
         "warm", "A fire heats the kettle. Was it warming up or cooling down? Try again.",
         "d3h", "Wide green fields of sugarcane seen from the air", "Sugarcane fields · Canal Point, Florida, about 1968",
         "To make cane syrup, people boil sugarcane juice in a big kettle. The water boils away as water vapor, and thick, sweet syrup is left behind.", "kettle",
         "This photo was taken at the Seminole Indian Agency in Florida in 1941."),
    card("D", "d4", "Tall white hills of salt beside a shallow pink pond under a cloudy sky",
         [{"t": "Thermometer: air about 30 °C, sunny. White salt sits by shallow water.", "ok": True}, {"t": "Thermometer: −15 °C. Thick ice.", "miss": "Look again. Is anything frozen?"}, {"t": "A kettle bubbling hard", "miss": "Look again. Is anything boiling?"}],
         2, "The Sun slowly turns the pond water into gas. No bubbles! Which change is that? Try again.",
         "warm", "The Sun heats the pond day after day. Was it warming up or cooling down? Try again.",
         "d4h", "Long rows of white salt hills beside a pink salt pond", "Pekelmeer salt pans · Bonaire, in the Caribbean",
         "Workers let seawater into shallow ponds. The Sun heats it day after day, and the water evaporates into the air. The salt stays behind in white piles.", "saltpan",
         "The pink color comes from tiny living things that grow in very salty water."),
    card("E", "d5", "A green lawn covered with hundreds of little white balls of hail",
         [{"t": "Thermometer: air 28 °C. Little balls of ice cover the green grass.", "ok": True}, {"t": "Steam rising from a kettle", "miss": "Look again. Is anything steaming?"}, {"t": "Drops on a cold bottle", "miss": "Look again. Do you see any bottles?"}],
         0, "The hailstones are solid ice turning into liquid water. Which change is that? Try again.",
         "warm", "The warm air and ground heat the hail. Was it warming up or cooling down? Try again.",
         "d5h", "A tall storm cloud with sunbeams over the water", "A storm cloud over the Gulf · Florida",
         "Hail forms high up in tall storm clouds, where it is below freezing. When hailstones land on warm grass, heat from the air and ground melts them into water.", "storm",
         "Florida gets hail too, mostly from spring and summer thunderstorms.")
  ]
}

rebuild = {"title": "Use your evidence to rebuild the scene", "missPrefix": "Hmm. Look at your thermometer file again. ", "kicker": "🌍 Rebuild the scene", "whyStart": "I chose this because the water…",
  "envs": [
    {"key": "lake", "name": "🧊 A northern lake in winter", "img": "d1h", "cap": "Freezing cold…"},
    {"key": "beach", "name": "🏖️ A hot Florida beach", "img": "d2h", "cap": "Warm, damp air…"},
    {"key": "kettle", "name": "🌾 A cane syrup kettle", "img": "d3h", "cap": "Boiling juice…"},
    {"key": "saltpan", "name": "🧂 A sunny salt pond", "img": "d4h", "cap": "Water drying away…"},
    {"key": "storm", "name": "⛈️ A summer hailstorm", "img": "d5h", "cap": "Ice from the sky…"}
  ],
  "life": [
    {"name": "❄️ A lake freezing solid", "img": "d1", "env": "lake", "miss": "The lake freezes in the cold north."},
    {"name": "💧 Drops on a cold bottle", "img": "d2", "env": "beach", "miss": "Cold bottles get drops on the hot beach."},
    {"name": "♨️ Juice boiling into syrup", "img": "d3", "env": "kettle", "miss": "The juice boils in the syrup kettle."},
    {"name": "☁️ Seawater evaporating", "img": "d4", "env": "saltpan", "miss": "Seawater evaporates in the salt pond."},
    {"name": "🔥 Hail melting on grass", "img": "d5", "env": "storm", "miss": "Hail falls from the storm and melts."}
  ]}

quiz = [
  {"q": "What happens to ice when heat energy is added?", "options": [
    {"t": "It gets harder and colder", "miss": "Think about what happens to an ice cube sitting in a warm room. Does it stay frozen?"},
    {"t": "It melts into liquid water", "ok": "🌲 Yes! Adding heat energy causes ice to melt. It changes from a solid to a liquid."},
    {"t": "It disappears completely", "miss": "Think about what happens to an ice cube sitting in a warm room. Does it stay frozen?"}]},
  {"q": "What is condensation?", "options": [
    {"t": "When water vapor cools and turns back into liquid water", "ok": "🌲 Correct! Condensation is when water vapor (a gas) cools down and becomes liquid water again."},
    {"t": "When liquid water turns into ice", "miss": "Condensation involves a gas changing. Think about water drops on a cold glass."},
    {"t": "When a solid gets warmer and melts", "miss": "Condensation involves a gas changing. Think about water drops on a cold glass."}]},
  {"q": "A student records that ice melted at a warm temperature and water froze at a cold temperature. What pattern does this data show?", "options": [
    {"t": "Water always stays the same", "miss": "Look at the data. What is different between the two situations? Focus on the temperature."},
    {"t": "Cold temperatures make water evaporate", "miss": "Look at the data. What is different between the two situations? Focus on the temperature."},
    {"t": "Temperature determines the state of water", "ok": "🌲 Exactly! The data shows a pattern: temperature determines whether water is a solid, liquid, or gas."}]}
]

partA = {"title": "Investigation data table", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  {"n": 1, "q": "Stage 1 · Ice. Thermometer: 0 °C. It is hard and keeps its shape. What state is the water in?", "type": "choice", "options": [
    {"t": "Solid", "ok": "Yes. Ice keeps its own shape, so it is a solid."},
    {"t": "Liquid", "miss": "A liquid flows. Does this ice flow, or keep its shape?"},
    {"t": "Gas", "miss": "A gas spreads out and you can't see water vapor. Can you see this ice?"}]},
  {"n": 2, "q": "Stage 2 · Melted. Thermometer: 20 °C. It flows and fills the bottom of the pot. What state is the water in?", "type": "choice", "options": [
    {"t": "Solid", "miss": "A solid keeps its shape. This water flows."},
    {"t": "Liquid", "ok": "Yes. Water that flows and takes the shape of its container is a liquid."},
    {"t": "Gas", "miss": "You can see this water at the bottom of the pot. Water vapor is invisible."}]},
  {"n": 3, "q": "Stage 3 · Boiling. Thermometer: 100 °C. Big bubbles and steam. What is happening to the water?", "type": "choice", "options": [
    {"t": "Air is being added to the water", "miss": "The big bubbles are not air. What did the Steam Tower show?"},
    {"t": "The liquid is turning into a gas (water vapor)", "ok": "Yes. At 100 °C, liquid water boils and turns into water vapor."},
    {"t": "The water is turning into ice", "miss": "Ice forms when water gets cold. Is 100 °C hot or cold?"}]}
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "What happened to the water each time the temperature changed? Describe the pattern you observed.", "type": "text", "min": 12, "chips": [["heat", "Uses temperature or heat"], ["chg", "Names a change (melting, boiling…)"]]},
    {"n": 2, "q": "If you left a glass of ice water outside on a hot summer day, what would happen over time? Explain each change.", "type": "text", "min": 12, "chips": [["melt", "Tells what happens to the ice"], ["cond", "Tells about drops on the outside"]]}
  ]},
  "write": {"title": "What does your investigation data tell you about how temperature changes the state of water?", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["temperature", "condensation", "boiling"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"My investigation showed me that temperature…\""],
                ["What did you observe or learn that supports your thinking?", "Start with: \"I know this because when heat was added…\""],
                ["Why does that make sense?", "Start with: \"The pattern in my data tells me that…\""]]},
  "partC": {"do": "Draw a comic strip with four panels showing the Pot Lab: ice, melted water, boiling water with steam, and drops on a cool lid. In each panel, draw the water and label its state: solid, liquid, gas, liquid again.",
            "labels": ["What caused the ice to melt and boil", "What caused the drops on the lid"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 thermometer files and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: my investigation data table.", "req": {"choice": ["a1", "a2", "a3"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my water story", "thinkLabel": "The change I'll look for in my kitchen is", "director": "JUNIOR WATER SCIENTIST", "storyKicker": "My water story",
  "frames": [
    {"k": "formation", "label": "The Pot Lab", "img": "o3", "cap": "The Pot Lab: ice, water, boiling, drops."},
    {"k": "compare", "label": "The Drip Test", "img": "ta", "cap": "The Drip Test: cold glass and cool lid make drops."},
    {"k": "wall", "label": "The Steam Tower", "img": "l4", "cap": "The Steam Tower: a white cloud, vapor, boiling, bubbles."},
    {"k": "det", "label": "Thermometer files", "img": "d1", "cap": "Thermometer files: warming up or cooling down?"}]}

nxt = {"title": "Coming up next: 28.01", "text": "How Does Energy Cause Change? Next time, find light, heat, sound, and motion energy, and see how energy makes things move and change."}

chips = {
  "part": {"any": ["ice", "cube", "cubes", "straw", "yellow", "rim", "cup", "glass", "plastic", "foggy", "fog", "cloudy", "drops", "wet", "water", "cold", "clear", "outside", "melting", "melt", "frost", "frosty", "top"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["ice", "icy", "lake", "frozen", "white", "snow", "bottle", "bottles", "drops", "wet", "kettle", "juice", "bubbles", "bubbling", "steam", "steaming", "salt", "pond", "pink", "hail", "grass", "balls", "thermometer", "degrees", "°c", "hot", "cold"]},
  "chg": {"any": ["melt", "melts", "melted", "melting", "freeze", "freezes", "froze", "frozen", "freezing", "evaporate", "evaporates", "evaporated", "evaporating", "evaporation", "boil", "boils", "boiled", "boiling", "condense", "condenses", "condensed", "condensation"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "heat": {"any": ["heat", "heated", "heating", "temperature", "temperatures", "hot", "hotter", "warm", "warmer", "cold", "colder", "cool", "cooler", "cooled", "degrees"]},
  "melt": {"any": ["melt", "melts", "melted", "melting", "ice"]},
  "cond": {"any": ["condense", "condenses", "condensed", "condensation", "drops", "droplets", "wet", "outside", "vapor"]}
}

L = {"id": "g3sci-27-02", "lesson": "27.02", "title": "Investigation: Heating, Cooling, and Water Changes", "emoji": "💧",
  "details": ["📅 Q4 · Unit 9 · Properties &amp; Changes of Matter", "📖 Week 27 · Lesson 27.02", "🌎 CPALMS SC.3.P.9.1, SC.3.E.6.1, SC.3.N.1.3", "⏱ About 35 minutes"],
  "icans": ["describe what happens to water when it is heated and when it is cooled.", "record observations of water changing from one state to another.", "explain how temperature causes water to change state using evidence from my investigation."],
  "opti": {"warm": "Our film starts on a misty Florida morning. First, inspect a cold cup with a secret on the outside.",
           "lesson": "Today you're a water scientist. Heat a pot, test two drinks, then climb down a steam tower.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show your data. Fill in the table, then draw your Pot Lab comic."},
  "film": film, "scientist": "water scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Gymnopédie No. 1 (Erik Satie), public domain recording (Musopen, via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The Pot Lab movie, the Drip Test, and the Steam Tower are models; every place photo is real."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-27-02-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the cup, then tap three things you notice."},
  "how-27-02-compare": {"page": "Put the lid on one specimen and the paper towel on the other: drag them, or tap one, then a specimen. Press Run the test. Then swap.",
                        "say": "Put the lid on one specimen and the paper towel on the other: drag them, or tap one, then a specimen. Press Run the test. Then swap."},
  "how-27-02-wall": {"page": wall["do"], "say": wall["do"]},
  "how-27-02-det": {"page": det["do"], "say": "Pick three files, one at a time. Tap a clue, then name the change. Predict if it was warming up or cooling down, and watch the place appear."},
  "how-27-02-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"27-02-welcome": L["opti"]["warm"], "27-02-lesson": L["opti"]["lesson"], "27-02-check": L["opti"]["check"], "27-02-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/meta.json'))
cred = [dict(key=k, **meta[k]) for k in sorted(meta)] + [dict(key="l4", **meta["l3"])]
json.dump(cred, open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
