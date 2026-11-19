#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/24-02/lesson.json, how-lines.json, scripts.json."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
HS = json.load(open(f'{D}/hotspots.json')) if os.path.exists(f'{D}/hotspots.json') else None

def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s

film = {
  "id": "g3sci-24-02", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 24.02 · How Can We Practice Conservation?",
  "title": "Trash Mountain",
  "bigQuestion": "What can people do to take care of the natural world, and why does it matter which actions we choose?",
  "poster": "f_night", "endPoster": "f_bfly", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    ph(3.4, 6.4, "f_night", "Florida seen from space at night, its cities glowing gold along the dark coast", "Florida from the International Space Station · Night",
       frm=(1.0, .5, .5), to=(1.25, .55, .55), fade=1.2, sfx="whoosh", sfxArg=2.0),
    {"t": 9.8, "d": 5.8, "type": "archive", "img": "f_scows", "alt": "An old color photo of barges piled high with trash at a dock, with cranes and smoke behind them",
     "note": "Barges bring New York City's trash to a landfill, 1973.", "fade": 0.8},
    {"t": 15.6, "d": 3.2, "type": "flash", "lines": ["A mountain?", "Made of trash?"], "beats": [0.15, 1.2], "fade": 0.15},
    {"t": 18.8, "d": 12.8, "type": "split", "img": "f_lf2", "alt": "A big machine drives over a landfill piled with crushed trash under a blue sky", "img2": "f_park",
     "alt2": "A tall grassy hill with lamp posts and bushes under a pale sky", "splitAt": 5.4, "splitDur": 2.4,
     "lab1": "A landfill at work", "lab2": "Mount Trashmore Park · Virginia Beach", "from": [1.0, .5, .5], "to": [1.06, .5, .5], "fade": 0.6, "sfx": "shimmer"},
    ph(31.6, 6.0, "f_cans", "Huge stacked bales of crushed, colorful cans and bottles at a recycling plant", "Bales of crushed cans and bottles · Greenville, North Carolina",
       frm=(1.0, .5, .5), to=(1.14, .45, .5)),
    ph(37.6, 8.6, "f_bfly", "A butterfly with orange and brown wings rests on small white wildflowers", "A butterfly on wildflowers · Everglades, Florida",
       frm=(1.12, .5, .5), to=(1.0, .5, .5), fade=0.9, fx=["rays"]),
    {"t": 46.2, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.6, "text": "Night over Florida. Millions of homes glow below.", "voice": "opti-1"},
    {"t": 10.1, "d": 5.2, "text": "Every day, those homes throw things away. Where does it all go?", "voice": "opti-2"},
    {"t": 15.7, "d": 2.8, "text": "A mountain? Made of trash?", "voice": "opti-3"},
    {"t": 19.1, "d": 4.8, "text": "Much of it is buried in a landfill, layer after layer.", "voice": "opti-4"},
    {"t": 24.6, "d": 6.6, "text": "This grassy hill in Virginia is trash under soil. It opened as a park in 1974.", "voice": "opti-5"},
    {"t": 31.9, "d": 5.4, "text": "But some trash never has to be buried. These cans become new cans.", "voice": "opti-6"},
    {"t": 38.0, "d": 7.8, "text": "So what can we do to care for nature? And which actions matter most?", "voice": "opti-7"}
  ]
}

spec_hs = HS or [
  {"name": "A squashed red can", "x": 0.30, "y": 0.40}, {"name": "A shiny silver can", "x": 0.60, "y": 0.35},
  {"name": "A label you can still read", "x": 0.45, "y": 0.60}, {"name": "A bit of plastic mixed in", "x": 0.75, "y": 0.70},
  {"name": "A wire strap holding it together", "x": 0.15, "y": 0.80}]
specimen = {
  "img": "spec", "aspect": "1920/2880", "radius": 0.07, "hotspots": spec_hs,
  "kicker": "🔎 Mystery specimen", "title": "What is this giant block?",
  "alt": "A tall block made of hundreds of flattened, colorful drink cans pressed together, sitting on a wooden pallet, with another block behind it",
  "look": "A real photo of a giant block at a recycling plant. It is about as tall as a kitchen counter and weighs hundreds of pounds. A specimen is one real thing that scientists study. What is it made of? Why would anyone squash it like this? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the block, then tap 3 things you notice.",
  "number": "No. 24.02-A",
  "card": ["<b>Specimen A</b>", "Found: at a recycling center on a Marine Corps base", "Size: about as tall as a kitchen counter", "What is it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see in the block)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🛡️", "conservation", "Protecting natural resources, like water, land, and wildlife, so they aren't used up or destroyed."],
  ["♻️", "recycling", "Collecting used materials, like paper, plastic, or metal, and turning them into something new instead of throwing them away."],
  ["🏡", "habitat", "The natural home where a plant or animal finds food, water, and shelter."],
  ["💧", "water conservation", "Using water carefully and reducing waste, so there is enough clean water for people, animals, and plants."],
  ["📉", "reduce", "Using less of something, like electricity, plastic, or water, so fewer resources are used up or wasted."],
  ["🤝", "stewardship", "Taking responsibility for caring for the Earth. A steward looks after something that belongs to everyone."]
]

parts = [
  {"kicker": "♻️ Part 1", "title": "Reducing Waste",
   "html": "<p>Every day, people throw things away: packaging, paper, bottles. A lot of it doesn't have to be waste. Recycling turns old materials into new ones. Aluminum cans get melted and made into new cans.</p><p>Even smarter is to reduce: buy less, choose less packaging, and reuse things first. Less trash going in means less harm coming out.</p>"},
  {"kicker": "💧 Part 2", "title": "Water Conservation",
   "html": "<p>Most of Earth's water is salty. Only a small part is fresh water we can drink or use to grow food. Water conservation means making careful choices: turning off the tap while brushing your teeth, fixing leaks, and covering garden soil with mulch so it stays damp. A faucet that drips once every second can waste more than 3,000 gallons in a year.</p>"},
  {"kicker": "🌿 Part 3", "title": "Protecting Habitats",
   "html": "<p>When land is cleared for buildings or roads, animals lose their homes. Communities protect habitats by setting aside nature preserves, planting native plants, and keeping streams and wetlands clean.</p><p>Not every action works the same way. The best choice depends on the problem you're trying to solve.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Sort and Rate"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start where the can leaves your home.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does a can get a second life?",
  "look": "Four real photos show what happens to a drink can after you recycle it, but they are mixed up. A recycling plant is a big building where machines sort what people recycle. Melt means to heat something until it turns to liquid. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "Two soldiers smile as they toss empty cans into a big box full of cans", "text": "People put empty cans in the recycling.", "play": "Cans go in the bin.",
     "miss": ["", "The cans have to be collected first. Try frame 1.", "Nothing can be squashed until the cans are collected. Try frame 1.", "This is where the can's trip starts. Try frame 1."]},
    {"img": "o2", "alt": "Inside a recycling plant, piles of mixed recycling sit by machines and moving belts", "text": "At a recycling plant, machines sort cans from paper and plastic.", "play": "Machines sort them.",
     "miss": ["The cans have to reach the plant first. Try a later frame.", "", "Cans are sorted before they're squashed. Try an earlier frame.", "Sorting comes before melting. Try an earlier frame."]},
    {"img": "o3", "alt": "Big square bales of crushed cans stacked in rows", "text": "The cans are crushed into big, heavy bales.", "play": "Crushed into bales.",
     "miss": ["The cans have to be collected and sorted first. Try a later frame.", "They're sorted before they're crushed. Try a later frame.", "", "The bales are made before the metal is melted. Try an earlier frame."]},
    {"img": "o4", "alt": "Bright orange melted metal glows inside a metal pot at a factory", "text": "The metal is melted and made into new cans.", "play": "Melted into new cans.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Which is even better for the Earth than recycling a can?",
    "options": [
      {"t": "Recycling is always the very best choice.", "miss": "Recycling still uses trucks, machines, and heat to melt the metal. What uses even less?"},
      {"t": "Using less in the first place, like a refillable bottle.", "ok": "Yes! Reducing comes first. When you don't use a can at all, no energy is needed to collect, crush, and melt it."}
    ]
  }
}

movie = {
  "model": "can-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab",
  "real": "real", "realAlt": "Bales of crushed, colorful cans and bottles stacked at a recycling plant",
  "stamp": "NEW AGAIN", "endCap": "Real bales · Greenville, NC.",
  "beats": [
    {"at": 0, "cap": "1 · Into the bin.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Day 1"]},
    {"at": 2600, "cap": "2 · Sorted.", "model": {"show": "s2"}, "counter": ["Days later"]},
    {"at": 5200, "cap": "3 · Crushed into a bale.", "model": {"show": "s3"}, "counter": ["Weeks later"]},
    {"at": 7800, "cap": "4 · Melted. A new can!", "model": {"show": "s4"}, "counter": ["About 2 months"], "sfx": "shimmer"},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Mulch Test", "title": "Which garden bed saves water?",
  "look": "Two real garden beds, each on a lit specimen tray. Specimen A is bare soil with nothing covering it. Specimen B is covered with mulch, a blanket of wood chips or shredded bark on top of the soil. Under the trays are two model tests: a desk lamp for hot sun and a cup of water for rain.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "Dry, bare brown soil with deep cracks running across it", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A garden bed covered with a thick layer of brown wood chips around green plants", "label": "Specimen B"}
  ],
  "materials": [{"key": "lamp", "label": "Desk lamp (hot sun)", "swatch": "lamp"}, {"key": "rain", "label": "Cup of water (rain)", "swatch": "water"}],
  "ask": [
    {"q": "Which garden bed has bare soil?", "ans": "A", "ok": "Yes. Specimen A has nothing covering the soil.", "miss": "Look closely. Which one shows cracked, bare dirt?"},
    {"q": "Which garden bed is covered with mulch?", "ans": "B", "ok": "Yes. Specimen B has a thick blanket of wood chips.", "miss": "Look again. Which one has wood chips on top?"}
  ],
  "press": "☀️ Run the test",
  "testDo": "Put the lamp under one tray and the water under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. Real gardens get hot sun and heavy rain.",
  "results": {
    "Alamp": {"text": "The hot sun dries the bare soil fast. It cracks, and the water is gone.", "fx": "dry"},
    "Arain": {"text": "Some water soaks in, but a lot runs off the hard, dry crust.", "fx": "runoff"},
    "Blamp": {"text": "The mulch shades the soil like a blanket. Underneath, the soil stays damp.", "fx": "wet"},
    "Brain": {"text": "The water soaks through the wood chips into the soil and stays there.", "fx": "wick"}
  },
  "best": ["Alamp", "Blamp"],
  "frame": "This bed has ___, so in the hot sun its soil ___.", "claimLead": "This bed has", "claimMid": "so in the hot sun its soil",
  "claim": {
    "A": {"feat": ["bare soil", "a blanket of mulch"], "featOk": 0, "eat": ["dries out", "stays damp"], "eatOk": 0},
    "B": {"feat": ["bare soil", "a blanket of mulch"], "featOk": 1, "eat": ["dries out", "stays damp"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Bare soil → water lost.</b> Sun and wind dry it out, so it needs more watering.",
    "B": "<b>Mulch → water saved.</b> The blanket keeps the soil damp, so it needs less watering."
  },
  "missFeat": "Look at {label} again. Is the soil bare, or covered?",
  "missClaim": "Think about your test. Which soil stayed damp under the lamp?",
  "done": "A blanket of mulch keeps water in the soil, so gardeners can water less. That's a small action that saves a natural resource.",
  "after": {"kicker": "🎬 Behind the scenes · Florida-friendly yards", "img": "aft2", "alt": "A yard with green native plants and paths of mulch",
            "html": "Florida's gardening experts at the University of Florida say to keep 2 to 3 inches of mulch on plant beds. It holds water in the soil and keeps weeds from sprouting. Lots of Florida families also pick native plants, which need less watering once they're growing."}
}

wall = {
  "kicker": "🚜 The Landfill Dig", "title": "Dig down through a landfill",
  "look": "A model of one landfill, from the top down to the bottom. A landfill is a place where trash is buried in layers. Each stop has a real photo. The brass dial on the left shows how deep you have dug.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the place shows.",
  "predict": {"q": "Does trash buried in a landfill rot away quickly?",
              "options": [["fast", "Yes, it rots away in a few months"], ["slow", "No, a lot of it lasts for years"]], "answer": "slow",
              "mine": "Your prediction: <b>{p}</b>. Let's dig down and find out.",
              "confirm": "You predicted a lot of it lasts. The evidence agrees: scientists dug up newspapers from long ago that you could still read.",
              "change": "You predicted it rots away fast. The evidence changed that idea: scientists dug up newspapers from long ago that you could still read."},
  "sky": "sky", "skyAlt": "A wide landfill of bare, packed ground with machines far away under an evening sky", "skyCap": "A working landfill · Calvert, England",
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Top", "Today's<br>trash", "Cover<br>soil", "Old<br>trash", "The<br>bottom"],
  "line": ["NEW TRASH", "THE BOTTOM"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We dig down one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Dig deeper. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the line. New trash goes on top, soil covers it, old trash sits below for a very long time, and a liner at the bottom keeps the trash juice out of the ground.",
  "rule": "<b>Buried isn't gone.</b> A landfill keeps trash out of sight, but much of it lasts for many years. That's why reducing and recycling come first: less trash means smaller landfills.",
  "choices": ["🚜 New trash squashed flat", "🟫 A layer of soil on top", "📰 Old trash that hasn't rotted", "🧱 A liner that protects the ground"],
  "layers": [
    {"name": "Stop 1 · Today's trash", "rock": "redbed", "img": "l1", "alt": "A big machine with spiked wheels rolls over crushed trash",
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "Trucks dump trash on top. Heavy machines with spiked wheels drive over it to squash it flat, so more fits.",
     "ans": 0, "ok": "Yes! New trash squashed flat.", "tag": "🚜 Today's trash",
     "miss": {"1": "Not yet. Look at the photo: is that soil, or trash?", "2": "Not yet. This trash is brand new.", "3": "Not yet. We're still at the top."},
     "env": "e1", "envAlt": "A yellow landfill compactor parked on a dirt road", "envCap": "A landfill compactor · a working landfill"},
    {"name": "Stop 2 · Cover soil", "rock": "soil", "img": "l2", "alt": "A wide, bare hill of packed soil at a landfill, with a pond in front",
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "At the end of each day, workers spread a layer of soil over the trash. It keeps away birds, rats, and smells.",
     "ans": 1, "ok": "Yes! A layer of soil on top.", "tag": "🟫 Cover soil",
     "miss": {"0": "Close! But read the clue: what do workers spread over the trash?", "2": "Not yet. Old trash is deeper.", "3": "Not yet. The bottom is still far down."},
     "env": "e2", "envAlt": "An old photo of a wheat field with a long, low hill of soil-covered trash behind it", "envCap": "A soil-covered dump behind a wheat field · EPA photo, 1970s"},
    {"name": "Stop 3 · Old trash", "rock": "mudstone", "img": "l3", "alt": "An old black-and-white photo of shelves and stacks of old newspapers",
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "Scientists in the Garbage Project dug into old landfills. They found newspapers from decades before that you could still read, and food that hadn't rotted.",
     "ans": 2, "ok": "Yes! Old trash that hasn't rotted.", "tag": "📰 Old trash",
     "miss": {"0": "This trash isn't new. Read the clue: how old is it?", "1": "Close! But read the clue: what did scientists find inside?", "3": "Not yet. Dig one more stop."},
     "env": "e3", "envAlt": "An old color photo of barges stacked with trash at a dock", "envCap": "Trash barges at Fresh Kills landfill · New York, 1973"},
    {"name": "Stop 4 · The bottom", "rock": "shale", "img": "l4", "alt": "Workers lay huge black plastic sheets across the bottom of a new landfill",
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "Before any trash goes in, workers line the bottom with clay and thick plastic. The liner keeps rain that trickles through the trash from leaking into the ground water.",
     "ans": 3, "ok": "Yes! A liner that protects the ground.", "tag": "🧱 The bottom",
     "miss": {"0": "Not trash. Read the clue: what lines the bottom?", "1": "Close! But this is under all the trash.", "2": "Not trash. Read the clue: what goes in before the trash?"},
     "env": "e4", "envAlt": "A grassy hill with a path, trees, and blue sky", "envCap": "Mount Trashmore Park, a covered landfill · Virginia Beach"}
  ],
  "mix": {
    "q": "A friend says, \"Throwing away one cup a day doesn't matter.\" What does the evidence say?",
    "options": [
      {"t": "It doesn't matter. One cup is too small.", "miss": "Think about the landfill. How did it get so big? One bag at a time."},
      {"t": "Small actions add up, like trash adding up into a mountain.", "ok": "Yes! A cup a day is 365 cups a year, and many people add up to a mountain. Small actions add up the other way too."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "From the world's biggest landfill to a giant park",
  "img": "wow", "alt": "A wide, grassy landfill hill with roads and water around it, seen from the air",
  "caption": "Fresh Kills, seen from the air · Staten Island, New York, 2012",
  "html": "<p style=\"margin:0 0 8px\">For more than 50 years, Fresh Kills was one of the biggest landfills in the world. Barges brought New York City's trash here every day. It closed in 2001.</p><p style=\"margin:0\">Now workers are covering the trash hills with liners and soil and planting grass. It's becoming Freshkills Park, about three times the size of Central Park. Hawks, foxes, and grassland birds already live there.</p>",
  "inset": "inset", "insetCap": "Trash barges at Fresh Kills in 1973."}

keyIdea = "People can take real steps to reduce their impact on the environment. Reducing waste, conserving water, and protecting habitats all make a difference, but only if people actually do them. Reducing comes before recycling, and small actions add up when many people do them."

M = ["♻️ Reduce waste", "💧 Save water", "🌿 Protect habitat"]
SHORT = ["reduce waste", "save water", "protect habitat"]
WHO = {"family": "One family", "town": "A neighborhood", "eco": "A whole community or ecosystem"}
def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": WHO[envAns], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}

det = {
  "look": "Five real conservation actions. Each card shows people doing something to help. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 actions, one at a time. Tap a clue, then pick its kind. Predict who it helps most, and watch the place appear.",
  "noun": "Action", "need": 3, "inferQ": "What kind of action is it?", "inferDone": "Kind", "chartSo": "so it helps",
  "predict": {"q": "Who do you predict this action helps the most?", "options": [["family", "🏠 One family"], ["town", "🏘️ A neighborhood"], ["eco", "🌎 A whole community or ecosystem"]]},
  "kicker": "Where it helps", "enough": "You already rated 3 actions. Nice work, conservation scientist!",
  "cols": ["Action", "My observation", "Kind of action", "Who it helps", "My evidence"],
  "write": {"label": "Action __ shows ___. It is a ___ action, and it helps ___.", "starter": "Start with: \"Action __ shows…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["kind", "Names the kind (waste, water, habitat)"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "A red rain barrel sits under a downspout beside a house",
         [{"t": "A barrel catching rain from the roof", "ok": True}, {"t": "A bin full of cans", "miss": "Look again. What is coming down the pipe into the barrel?"}, {"t": "A butterfly on a flower", "miss": "Look again. What is the barrel collecting?"}],
         1, "The barrel catches rain to use in the garden instead of tap water. Which kind is that? Try again.",
         "family", "One barrel catches rain from one family's roof for their own garden. Try again.",
         "d1h", "A woman stands in a green home vegetable garden", "Where it helps: a family's vegetable garden",
         "This garden is evidence that one family can water plants with saved rain. About 600 gallons can run off a 1,000-square-foot roof in one inch of rain.", "garden",
         "A rain barrel usually holds 50 to 80 gallons. Many Florida counties teach families to build one. When lots of families use them, they save tap water together."),
    card("B", "d2", "A compost bin full of food scraps, leaves, and dark soil",
         [{"t": "Food scraps and leaves turning into soil", "ok": True}, {"t": "A dripping faucet", "miss": "Look again. What is inside the bin?"}, {"t": "Wildflowers in a field", "miss": "Look again. These are scraps in a bin."}],
         0, "Composting keeps food scraps out of the trash. Which kind is that? Try again.",
         "family", "A home compost bin turns one family's scraps into soil for their own yard. Try again.",
         "d2h", "A pile of dark, crumbly finished compost on a tarp", "Where it helps: finished compost for a family's garden",
         "This rich soil is evidence that one family's scraps can feed their garden instead of a landfill. Food and yard waste make up more than a quarter of what Americans throw away.", "garden",
         "Tiny living things like worms, fungi, and bacteria break down the scraps into compost in a few months. In a landfill, the same scraps can last for years."),
    card("C", "d3", "Sailors in gloves pick up trash on a sandy beach and put it in big bags",
         [{"t": "Volunteers picking up trash on a beach", "ok": True}, {"t": "A rain barrel", "miss": "Look again. What are the people picking up?"}, {"t": "Bales of cans", "miss": "Look again. Where are these people?"}],
         2, "Clearing trash keeps the beach safe for the animals that live there. Which kind is that? Try again.",
         "eco", "Trash on a beach can wash out to sea, so a cleanup helps birds, turtles, and fish far away. Try again.",
         "d3h", "A wide, sandy beach under a blue sky with a few volunteers far down the shore", "Where it helps: volunteers clean a wide beach · Cape Hatteras, North Carolina (cleanup photo: Souda Bay, Greece)",
         "This clean beach is evidence that a cleanup helps a whole ecosystem: sea turtles, shorebirds, and fish all share it.", "beach",
         "Every September, volunteers around the world join the International Coastal Cleanup. They count every piece they pick up, so scientists know what kinds of trash end up on beaches."),
    card("D", "d4", "A field of native yellow and purple wildflowers planted for bees and butterflies",
         [{"t": "Native wildflowers planted for bees and butterflies", "ok": True}, {"t": "A pile of trash", "miss": "Look again. What is growing here?"}, {"t": "A leaky pipe", "miss": "Look again. What is growing here?"}],
         2, "Native plants give insects and birds food and shelter. Which kind is that? Try again.",
         "town", "Bees and butterflies fly from yard to yard, so one garden helps the whole neighborhood. Try again.",
         "d4h", "A fuzzy bumblebee covered in pollen leaves a pale yellow flower", "Where it helps: a bumblebee carrying pollen (flower photo: native prairie, North Dakota)",
         "This bee is evidence that native flowers feed pollinators, and pollinators fly from yard to yard, so one garden helps a whole neighborhood.", "yard",
         "Native plants grow naturally in Florida. Local insects already know how to use them, and they usually need less water than a lawn."),
    card("E", "d5", "People sort piles of cans and bottles into crates at a busy recycling center",
         [{"t": "Sorting a whole neighborhood's cans and bottles", "ok": True}, {"t": "A family's garden", "miss": "Look again. How much recycling is there?"}, {"t": "Volunteers on a beach", "miss": "Look again. Is this a beach?"}],
         0, "Recycling keeps cans, paper, and plastic out of the landfill. Which kind is that? Try again.",
         "eco", "This center takes cans and bottles from thousands of people. Who does that help? Try again.",
         "d5h", "Stacked bales of flattened cardboard at a recycling plant", "Where it helps: bales ready to become new things · Greenville, North Carolina",
         "These bales are evidence that recycling helps a whole community: thousands of homes keep tons of material out of the landfill.", "plant",
         "A recycled aluminum can can become a new can in less than two months on average. Making cans from old ones uses much less energy than starting from new metal."),
  ]
}

rebuild = {"title": "Use your evidence to rebuild the place", "missPrefix": "Hmm. Look at your action again. ", "kicker": "🌍 Rebuild the place", "whyStart": "I chose this because the action…",
  "envs": [
    {"key": "garden", "name": "🥕 A home garden", "img": "d1h", "cap": "Rows of vegetables…"},
    {"key": "beach", "name": "🏖️ A Florida beach", "img": "d3h", "cap": "Sand and waves…"},
    {"key": "yard", "name": "🦋 A native-plant yard", "img": "d4h", "cap": "Flowers and buzzing…"},
    {"key": "plant", "name": "🏭 A recycling plant", "img": "d5h", "cap": "Bales and belts…"}
  ],
  "life": [
    {"name": "🪱 Earthworms", "img": "d2h", "env": "garden", "miss": "Earthworms help turn scraps into garden soil."},
    {"name": "🐢 Sea turtles", "img": "d3h", "env": "beach", "miss": "Sea turtles nest on Florida beaches."},
    {"name": "🐝 Native bees", "img": "d4h", "env": "yard", "miss": "Native bees visit the flowers in a native-plant yard."},
    {"name": "🥫 New cans", "img": "d5h", "env": "plant", "miss": "New cans start as bales at a recycling plant."}
  ]}

quiz = [
  {"q": "What does the word conservation mean?", "options": [
    {"t": "Throwing old materials into a landfill", "miss": "Conservation is about protecting resources, not getting rid of them."},
    {"t": "Protecting natural resources so they aren't used up or destroyed", "ok": "🌲 Exactly right! Conservation means taking care of resources, like land, water, and wildlife, so they last for future generations."},
    {"t": "Burning waste to reduce how much goes to the dump", "miss": "Conservation is about protecting resources, not getting rid of them."}]},
  {"q": "A community fixes a leaky pipe in a park fountain. What type of conservation practice is this?", "options": [
    {"t": "Habitat protection", "miss": "A leaky pipe is about water being wasted. Which kind is about using water carefully?"},
    {"t": "Reduce waste", "miss": "A leaky pipe is about water being wasted. Which kind is about using water carefully?"},
    {"t": "Water conservation", "ok": "🌿 Yes! Fixing a leak stops water from being wasted. Small fixes add up to a lot of water saved over time."}]},
  {"q": "A family plants native wildflowers along the edge of their yard and leaves a section unmowed. Which conservation practice does this best represent?", "options": [
    {"t": "Habitat protection", "ok": "⭐ Great thinking! Native plants and unmowed areas give insects, birds, and small animals food and shelter. That's habitat protection in a neighborhood."},
    {"t": "Recycling", "miss": "This is about giving animals a place to live. Which kind protects the homes of wildlife?"},
    {"t": "Water conservation", "miss": "This is about giving animals a place to live. Which kind protects the homes of wildlife?"}]}
]

def k3(n, q, ans, ok, miss):
    opts = [{"t": t} for t in ["Reduce waste", "Save water", "Protect habitat"]]
    for i, o in enumerate(opts):
        if i == ans: o["ok"] = ok
        else: o["miss"] = miss
    return {"n": n, "q": q, "type": "choice", "options": opts}

partA = {"title": "Sort and identify", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  k3(1, "Bring a reusable bag to the store. Which kind of action is it?", 0, "Yes. A reusable bag means fewer bags thrown away.", "Think about what ends up in the trash. Which kind keeps trash out?"),
  k3(2, "Install a rain barrel to collect water. Which kind of action is it?", 1, "Yes. Rain water from the barrel replaces tap water in the garden.", "Think about what the barrel collects. Which kind is about water?"),
  k3(3, "Leave a wild area of a yard unmowed. Which kind of action is it?", 2, "Yes. Tall plants give insects and small animals a home.", "Think about who lives in tall grass. Which kind is about homes for animals?"),
  {"n": 4, "q": "Pick one action from above. In one sentence, tell who or what benefits when people do it.", "type": "text", "min": 8, "chips": [["because", "Gives a reason (because, so)"]]}
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "What is the difference between reducing waste and recycling? Why do scientists say that reducing is actually more powerful than recycling?", "type": "text", "min": 12, "chips": [["reduce", "Uses the word reduce or reducing"], ["because", "Gives a reason (because, so)"]]},
    {"n": 2, "q": "Why is habitat protection important for animals? What happens when a habitat is destroyed or damaged?", "type": "text", "min": 12, "chips": [["habitat", "Uses the word habitat"], ["because", "Gives a reason (because, so)"]]}
  ]},
  "write": {"title": "Does your best action really reduce human impact?", "do": "Pick one from your evidence chart. Answer the three questions. Use at least two of the science words under the boxes.",
    "vocab": ["conservation", "recycling", "habitat", "water conservation", "reduce", "stewardship"], "need": 2,
    "prompts": [["What do you think?", "Start with: \"I think that [your chosen action] helps the environment because…\""],
                ["What did you observe or learn that supports your thinking?", "Start with: \"I know this because during the sort, I noticed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because when people [action], the result is that…\""]]},
  "partC": {"do": "Draw one conservation action and what it does for the environment. Label the action and the resource it protects, and one living thing that benefits.",
            "labels": ["The action and the resource it protects", "One living thing that benefits, and how"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 actions and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all four answers.", "req": {"choice": ["a1", "a2", "a3"], "text": {"in-a4": 8}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least two science words.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 2}}
  ]
}

premiere = {"title": "Premiere my conservation story", "thinkLabel": "It is a", "director": "JUNIOR CONSERVATION SCIENTIST", "storyKicker": "My conservation story",
  "frames": [
    {"k": "formation", "label": "A can's second life", "img": "o3", "cap": "A can's second life: sorted, crushed, melted, and made new."},
    {"k": "compare", "label": "The Mulch Test", "img": "tb", "cap": "The Mulch Test: a blanket of mulch keeps the soil damp."},
    {"k": "wall", "label": "The Landfill Dig", "img": "l4", "cap": "The Landfill Dig: buried trash lasts a long, long time."},
    {"k": "det", "label": "Sort and rate", "img": "d4", "cap": "Sort and rate: real actions, and who they help."}]}

nxt = {"title": "25.01 · Why Do We Protect National Parks?", "text": "Next time, find out why people work so hard to protect wild places like national parks."}

chips = {
  "part": {"any": ["can", "cans", "red", "silver", "blue", "label", "labels", "plastic", "wire", "strap", "squashed", "crushed", "flat", "metal", "shiny", "bottle", "bottles", "colors", "colorful", "block"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["barrel", "rain", "roof", "compost", "scraps", "soil", "volunteers", "beach", "trash", "flowers", "bees", "butterflies", "garden", "machines", "recycling", "cans", "bales", "plant"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "kind": {"any": ["waste", "water", "habitat", "reduce", "save", "protect", "recycle", "recycling"]},
  "reduce": {"any": ["reduce", "reducing", "reduces", "less"]},
  "habitat": {"any": ["habitat", "habitats", "home", "homes"]}
}

L = {"id": "g3sci-24-02", "lesson": "24.02", "title": "How Can We Practice Conservation?", "emoji": "♻️",
  "details": ["📅 Q3 · Unit 8 · Human Impact &amp; Conservation", "📖 Week 24 · Lesson 24.02", "🌎 CPALMS SC.3.N.1.7 · NGSS 3-LS4-4, 3-5-ETS1-2", "⏱ About 35 minutes"],
  "icans": ["name and explain real conservation practices people use to protect the environment.", "sort conservation actions by category and explain how each one reduces human impact.", "evaluate a conservation solution and make a claim about why it helps the environment."],
  "opti": {"warm": "Our film starts in space and lands on a mountain made of trash. First, inspect a giant block of something squashed.",
           "lesson": "Today you're a conservation scientist. Follow a can, test two garden beds, then dig down through a landfill.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Sort some actions, then tell us which one you'd choose and why."},
  "film": film, "scientist": "conservation scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Scott Joplin, \"Sunflower Slow Drag\", played by \"The President's Own\" United States Marine Band, public domain (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The can movie, the Mulch Test, and the Landfill Dig are models; every place photo is real."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-24-02-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the block, then tap three things you notice."},
  "how-24-02-compare": {"page": "Put the lamp under one tray and the water under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the lamp under one tray and the water under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-24-02-wall": {"page": wall["do"], "say": wall["do"]},
  "how-24-02-det": {"page": det["do"], "say": "Pick three actions, one at a time. Tap a clue, then pick its kind. Predict who it helps most, and watch the place appear."},
  "how-24-02-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"24-02-welcome": L["opti"]["warm"], "24-02-lesson": L["opti"]["lesson"], "24-02-check": L["opti"]["check"], "24-02-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
