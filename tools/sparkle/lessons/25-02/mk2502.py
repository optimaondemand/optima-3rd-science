#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/25-02/lesson.json, how-lines.json, scripts.json (25.02: no voices recorded; scripts only)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))
HS = json.load(open(f'{D}/hotspots.json')) if os.path.exists(f'{D}/hotspots.json') else None
CFG = json.load(open(f'{D}/cfg.json')) if os.path.exists(f'{D}/cfg.json') else {}

def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s

XR = CFG.get("xray", {"win": [30, 30, 40], "y0": 0.1, "y1": 0.6})
film = {
  "id": "g3sci-25-02", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 25.02 · Protect a Park Proposal",
  "title": "The Invader",
  "bigQuestion": "If a park habitat is being damaged, how do you figure out what to do, and how do you convince others that your plan will actually help?",
  "poster": "f_marsh", "endPoster": "f_today", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.55},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 4.0, "type": "black", "fade": 0.4, "sfxAt": [{"at": 0.6, "name": "brush"}, {"at": 1.8, "name": "brush"}, {"at": 3.0, "name": "brush"}]},
    {"t": 7.4, "d": 10.0, "type": "xray", "img": "f_marsh", "alt": "A wide Everglades marsh of tall golden-green sawgrass at dawn", "img2": "f_python",
     "alt2": "A big patterned Burmese python stretched across the ground", "xlabel": "Look closer · a model", "from": [1.04, .5, .5], "to": [1.12, .5, .58],
     "win": XR["win"], "band": 0.18, "y0": XR["y0"], "y1": XR["y1"], "xrayAt": 2.0, "xrayDur": 6.0, "place": "Everglades National Park, Florida", "fade": 1.0},
    {"t": 17.4, "d": 3.2, "type": "flash", "lines": ["A python?", "In Florida?"], "beats": [0.15, 1.2], "fade": 0.15},
    ph(20.6, 6.2, "f_measure", "A trail camera photo of a bobcat finding a python curled on its nest", "A scientist's trail camera at a python nest · Florida",
       frm=(1.0, .5, .5), to=(1.08, .42, .62)),
    ph(26.8, 6.0, "f_track", "A Burmese python wrapped around a tree branch", "A Burmese python up a tree · Everglades National Park",
       frm=(1.12, .5, .55), to=(1.0, .5, .5)),
    ph(32.8, 6.2, "f_rabbit", "A small brown marsh rabbit sitting in green grass", "A marsh rabbit · Florida",
       frm=(1.0, .5, .5), to=(1.14, .5, .5), sfx="shimmer"),
    ph(39.0, 7.4, "f_today", "The sun rises over a quiet Everglades marsh with scattered trees", "Everglades National Park · Today",
       frm=(1.0, .5, .5), to=(1.08, .5, .55), fade=0.9, fx=["rays"]),
    {"t": 46.4, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 3.4, "text": "Morning in the Everglades. Something hides in the grass.", "voice": "opti-1"},
    {"t": 8.0, "d": 8.8, "text": "Look closer. Can you find what's hiding here?", "voice": "opti-2"},
    {"t": 17.5, "d": 2.8, "text": "A python? In Florida?", "voice": "opti-3"},
    {"t": 21.0, "d": 5.6, "text": "Pythons don't belong here. Scientists set cameras.", "voice": "opti-4"},
    {"t": 27.2, "d": 5.4, "text": "Pythons climb, swim, and hide, and they eat native animals.", "voice": "opti-5"},
    {"t": 33.2, "d": 5.6, "text": "With evidence, people write plans to protect animals like this rabbit.", "voice": "opti-6"},
    {"t": 39.4, "d": 6.6, "text": "How do you choose a plan to save a park, and prove it will work?", "voice": "opti-7"}
  ]
}

spec_hs = HS or [{"name": "Diamond-shaped scales", "x": .5, "y": .5}, {"name": "Dark brown blotches", "x": .3, "y": .4}, {"name": "A pale belly", "x": .7, "y": .6}, {"name": "A see-through edge", "x": .2, "y": .7}]
specimen = {
  "img": "spec", "aspect": CFG.get("specAspect", "16/9"), "radius": 0.07, "hotspots": spec_hs,
  "kicker": "🔎 Mystery specimen", "title": CFG.get("specTitle", "What left this behind?"),
  "alt": CFG.get("specAlt", "A long, thin, see-through sheet with a pattern of scales and blotches"),
  "look": CFG.get("specLook", "A real photo from South Florida. Look at the pattern of scales and dark blotches. A specimen is one real thing that scientists study. What animal does it come from? Does that animal belong in Florida? That's for you to figure out."),
  "do": "Press Inspect specimen. Move the magnifying lens over the specimen, then tap 3 things you notice.",
  "number": "No. 25.02-A",
  "card": ["<b>Specimen A</b>", CFG.get("specFound", "Found: in South Florida"), CFG.get("specSize", "Size: longer than a grown-up is tall"), "What is it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🏡", "habitat", "The place where a plant or animal lives and gets the food, water, and shelter it needs to survive."],
  ["⚠️", "threat", "A danger that could harm a living thing or damage the place where it lives."],
  ["🌿", "conservation", "Protecting nature so that plants, animals, and ecosystems stay healthy for the future."],
  ["📋", "proposal", "A written plan that describes a problem and explains a solution that could fix it."],
  ["✅", "criteria", "The list of things a solution needs to do to count as successful: what \"working\" looks like."],
  ["🔍", "evidence", "Facts, observations, or data that support an idea or show that something is true."]
]

parts = [
  {"kicker": "⚠️ Part 1", "title": "What Threatens a Habitat?",
   "html": "<p>Every habitat has things that could hurt it. Threats can come from pollution washing into a river, invasive species crowding out native ones, or too many visitors trampling a marsh. Some threats are slow, like roads and buildings creeping into wild land.</p><p>Scientists notice these problems by counting species, testing water, and tracking which plants are disappearing.</p>"},
  {"kicker": "📋 Part 2", "title": "The Four Parts of a Proposal",
   "html": "<p>A habitat protection proposal has four parts. <b>The problem:</b> what's happening and why it matters. <b>The evidence:</b> facts that show the problem is real. <b>The solution:</b> what should be done. <b>The criteria:</b> how you'll know it worked.</p><p>A proposal without evidence is just an opinion. With evidence, it becomes a case.</p>"},
  {"kicker": "🗺️ Part 3", "title": "Proposals Can Change a Place",
   "html": "<p>In 2000, Congress approved a giant plan to bring water back across the Everglades, a region of about 18,000 square miles. Scientists had gathered evidence for years first, and work on the plan still goes on today.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Threat Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the problem.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does a proposal come together?",
  "look": "Four real photos follow one real problem in the Everglades: Burmese pythons, big snakes from Asia that don't belong in Florida. Each photo shows one part of a proposal, but they are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": CFG.get("o1alt", "A large Burmese python coiled in the grass"), "text": "The problem: pythons are eating native animals.", "play": "The problem.",
     "miss": ["", "A proposal starts with the problem. Try frame 1.", "You need a problem before a solution. Try frame 1.", "Start with what's going wrong. Try frame 1."]},
    {"img": "o2", "alt": CFG.get("o2alt", "Scientists measuring a long python stretched on the ground"), "text": "The evidence: cameras and counts show what pythons do.", "play": "The evidence.",
     "miss": ["The problem comes first. Try a later frame.", "", "Gather evidence before you pick a solution. Try an earlier frame.", "Evidence comes before criteria. Try an earlier frame."]},
    {"img": "o3", "alt": CFG.get("o3alt", "A crew carrying a captured python out of the marsh"), "text": "The solution: crews find and remove pythons from the park.", "play": "The solution.",
     "miss": ["The problem comes first. Try a later frame.", "You need evidence before the solution. Try a later frame.", "", "The solution comes before you check it worked. Try an earlier frame."]},
    {"img": "o4", "alt": CFG.get("o4alt", "A small marsh rabbit sitting in the grass"), "text": "The criteria: count rabbits and other animals to see if it's working.", "play": "The criteria.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "A friend says, \"A good idea is enough. You don't need evidence.\" What does the python case show?",
    "options": [
      {"t": "Right. If the idea sounds good, everyone will agree.", "miss": "Think about the python case. How did scientists convince people the pythons were a real problem?"},
      {"t": "No. Evidence, like counts and measurements, is what convinces people.", "ok": "Yes! Scientists set cameras and counted animals. That evidence made the case for removing them."}
    ]
  }
}

movie = {
  "model": "plan-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "swamp",
  "real": "real", "realAlt": CFG.get("realAlt", "Scientists holding a very long python stretched out across their arms"),
  "stamp": "MAKE THE CASE", "endCap": "A real python hiding in the grass · Everglades.",
  "beats": [
    {"at": 0, "cap": "1 · The problem.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Step 1"]},
    {"at": 2600, "cap": "2 · The evidence.", "model": {"show": "s2"}, "counter": ["Step 2"]},
    {"at": 5200, "cap": "3 · The solution.", "model": {"show": "s3"}, "counter": ["Step 3"]},
    {"at": 7800, "cap": "4 · The criteria.", "model": {"show": "s4"}, "counter": ["Step 4"], "sfx": "shimmer"},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Footprint Test", "title": "Which trail protects the plants?",
  "look": "Two real trails, each on a lit specimen tray. Specimen A is a raised wooden boardwalk over a wetland. Specimen B is a dirt path that people made by walking straight across the plants. Under the trays are two model tests: hiking boots for lots of visitors, and a cup of water for rain.",
  "trays": [
    {"id": "A", "img": "ta", "alt": CFG.get("taAlt", "A wooden boardwalk raised above green wetland plants"), "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": CFG.get("tbAlt", "A bare dirt path worn through grass and plants"), "label": "Specimen B"}
  ],
  "materials": [{"key": "boots", "label": "Hiking boots (visitors)", "swatch": "boots"}, {"key": "rain", "label": "Cup of water (rain)", "swatch": "water"}],
  "ask": [
    {"q": "Which trail keeps people up off the plants?", "ans": "A", "ok": "Yes. Specimen A is a raised boardwalk.", "miss": "Look closely. Which one is made of boards above the ground?"},
    {"q": "Which trail is bare dirt where plants used to grow?", "ans": "B", "ok": "Yes. Specimen B is a worn dirt path.", "miss": "Look again. Which one is bare dirt?"}
  ],
  "press": "🥾 Run the test",
  "testDo": "Put the boots under one tray and the water under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. Real parks get thousands of visitors.",
  "results": {
    "Aboots": {"text": "The boots stay on the boards. The plants underneath stay safe.", "fx": "none"},
    "Arain": {"text": "Rain falls between the boards onto the plants, just like in the wild.", "fx": "wet"},
    "Bboots": {"text": "Boots squash the plants and pack down the mud. Footprints everywhere.", "fx": "print"},
    "Brain": {"text": "Rain washes the loose, bare mud off the path.", "fx": "slump"}
  },
  "best": ["Aboots", "Bboots"],
  "frame": "This trail has ___, so when visitors walk, the plants ___.", "claimLead": "This trail has", "claimMid": "so when visitors walk, the plants",
  "claim": {
    "A": {"feat": ["a raised boardwalk", "no boardwalk"], "featOk": 0, "eat": ["stay safe", "get trampled"], "eatOk": 0},
    "B": {"feat": ["a raised boardwalk", "no boardwalk"], "featOk": 1, "eat": ["stay safe", "get trampled"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Boardwalk → plants protected.</b> Visitors can still enjoy the park.",
    "B": "<b>No boardwalk → plants trampled.</b> Bare mud washes away in the rain."
  },
  "missFeat": "Look at {label} again. Boards above the plants, or bare dirt?",
  "missClaim": "Think about your test. Where did the boots leave footprints?",
  "done": "A boardwalk is a solution with criteria you can check: are the plants beside it still growing? That's how a good proposal works.",
  "after": {"kicker": "🎬 Behind the scenes · Letting the water flow", "img": "aft", "alt": CFG.get("aftAlt", "A long, low bridge carrying a highway over a wide Everglades marsh"),
            "html": "For years, a highway called the Tamiami Trail blocked water from flowing south into Everglades National Park. Scientists and park staff made the case with evidence. Here, leaders dig the first shovels of dirt for a long bridge. Now bridges carry the road, so water can flow under it again."}
}

wall = {
  "kicker": "🌊 The River Comeback", "title": "Follow one Florida river through time",
  "look": "A model of one real river, the Kissimmee River in central Florida, from long ago to today. Each stop has a real photo. A canal is a straight ditch people dig to move water. The brass dial on the left shows the years.",
  "do": "First, make a prediction. Then brush the glowing stop: drag across it (or tap it again and again) until the place shows.",
  "predict": {"q": "Once people change a river, can a good plan bring it back?",
              "options": [["no", "No, once it's changed it's gone"], ["yes", "Yes, with a plan and hard work"]], "answer": "yes",
              "mine": "Your prediction: <b>{p}</b>. Let's follow the river and find out.",
              "confirm": "You predicted a plan can help. The evidence agrees: about 40 miles of the river curve again, and birds came back.",
              "change": "You predicted it's gone for good. The evidence changed that idea: about 40 miles of the river curve again, and birds came back."},
  "sky": "sky", "skyAlt": CFG.get("skyAlt", "A winding river curving through green marsh, seen from the air"), "skyCap": CFG.get("skyCap", "The Kissimmee River, Florida · Today"),
  "unit": "Stop", "found": "Clue found at Stop {n}",
  "elevator": ["Long ago", "1940s", "1960s", "1990s", "Today"],
  "line": ["LONG AGO", "TODAY"],
  "lockTag": "🔒 Brush the stop above first", "locked": "Brush the stop above first. We travel through time one stop at a time.",
  "first": "Brush the glowing top stop. Drag across it (or tap it again and again).", "next": "Move ahead in time. Brush Stop {n}.",
  "endTitle": "All 4 stops explored",
  "endText": "Look at the line. A winding river was turned into a straight canal. Scientists showed the harm, people approved a plan, and the river curves again.",
  "rule": "<b>A plan with evidence can bring a place back.</b> The Kissimmee River proposal had a problem, evidence, a solution, and criteria: count the birds and fish. It took almost 30 years, and the counts show it's working.",
  "choices": ["🐍 A winding river full of life", "📏 A straight canal that drained the wetlands", "🚜 Filling in the canal", "🦆 A curving river with birds again"],
  "layers": [
    {"name": "Stop 1 · Long ago", "rock": "water2", "img": "l1", "alt": CFG.get("l1alt", "A river making big loops through a wide, wet floodplain"),
     "ask": "Look at Stop 1. Read the clue AND the photo. What do you find?",
     "clue": "The Kissimmee River used to wind for about 103 miles, spilling over its banks into wide wetlands full of fish and wading birds.",
     "ans": 0, "ok": "Yes! A winding river full of life.", "tag": "🐍 Winding river",
     "miss": {"1": "Not yet. This river still curves.", "2": "Not yet. No machines yet.", "3": "Not yet. We're at the start."},
     "env": "e1", "envAlt": CFG.get("e1alt", "Wading birds feeding in a shallow Florida wetland"), "envCap": CFG.get("e1cap", "Wading birds in a Florida wetland")},
    {"name": "Stop 2 · The canal", "rock": "shale", "img": "l2", "alt": CFG.get("l2alt", "A long, straight canal cutting across flat land"),
     "ask": "Look at Stop 2. Read the clue AND the photo. What do you find?",
     "clue": "From 1962 to 1971, engineers dug a straight canal 56 miles long to stop floods. The wetlands dried up, and many birds left.",
     "ans": 1, "ok": "Yes! A straight canal that drained the wetlands.", "tag": "📏 Canal",
     "miss": {"0": "Look at the photo. Does it curve, or go straight?", "2": "Not yet. Read the clue: what did engineers dig?", "3": "Not yet. The birds haven't come back."},
     "env": "e2", "envAlt": CFG.get("e2alt", "Dry, brown land where a wetland used to be"), "envCap": CFG.get("e2cap", "Drained land in central Florida")},
    {"name": "Stop 3 · The plan", "rock": "soil", "img": "l3", "alt": CFG.get("l3alt", "Heavy machines pushing dirt to fill in a canal"),
     "ask": "Look at Stop 3. Read the clue AND the photo. What do you find?",
     "clue": "Scientists showed the evidence: fewer birds, fewer fish, dry wetlands. In 1992, Congress approved a plan to fill in parts of the canal.",
     "ans": 2, "ok": "Yes! Filling in the canal.", "tag": "🚜 The plan",
     "miss": {"0": "Not the old river. Read the clue: what happened to the canal?", "1": "Close! But this is the plan to fix the canal.", "3": "Not yet. The work isn't finished."},
     "env": "e3", "envAlt": CFG.get("e3alt", "Workers and machines on a muddy riverbank"), "envCap": CFG.get("e3cap", "Restoration work on the Kissimmee River")},
    {"name": "Stop 4 · Today", "rock": "leafsun", "img": "l4", "alt": CFG.get("l4alt", "A curving river through green marsh under a blue sky"),
     "ask": "Look at Stop 4. Read the clue AND the photo. What do you find?",
     "clue": "The work finished in 2021. About 40 miles of river curve again. Scientists counted at least 159 kinds of birds using the restored river.",
     "ans": 3, "ok": "Yes! A curving river with birds again.", "tag": "🦆 Today",
     "miss": {"0": "Close! But this is today, after the plan.", "1": "This isn't straight anymore. Look again.", "2": "The canal work is done. Read the clue."},
     "env": "e4", "envAlt": CFG.get("e4alt", "A wading bird standing in a green marsh"), "envCap": CFG.get("e4cap", "Wildlife on the restored river")}
  ],
  "mix": {
    "q": "A student's plan says, \"Success means the river is nice.\" Is that a good criterion?",
    "options": [
      {"t": "Yes. Everyone knows what nice means.", "miss": "Can you count or measure \"nice\"? Think about how scientists checked the Kissimmee River."},
      {"t": "No. A criterion should be something you can count or measure, like birds.", "ok": "Yes! \"At least 159 kinds of birds\" is something you can count. \"Nice\" is a goal, not a criterion."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": CFG.get("wowTitle", "36,000 lionfish in one summer"),
  "img": "wow", "alt": CFG.get("wowAlt", "A striped lionfish with long, feathery fins hovering over a coral reef"),
  "caption": CFG.get("wowCap", "A lionfish, an invader on Florida's reefs"),
  "html": "<p style=\"margin:0 0 8px\">Lionfish come from the Pacific and Indian Oceans. In Florida they eat native reef fish that keep algae off the coral.</p><p style=\"margin:0\">So Florida made a plan: pay divers to catch them, and count every one. In the 2026 Lionfish Challenge, divers removed more than 36,000 lionfish. The count is the evidence the plan is working.</p>",
  "inset": "inset", "insetCap": CFG.get("insetCap", "A diver at work on a Florida reef.")}

keyIdea = "When a habitat is threatened, scientists and citizens write protection proposals. A strong proposal names the problem, gives evidence that it's real, describes a solution, and sets criteria you can count or measure to know if it worked. A proposal without evidence is just an opinion. Evidence turns an opinion into a case."

M = ["🧪 Pollution", "🦎 Invasive species", "🏗️ Habitat loss", "👣 Too many visitors", "🌊 Rising seas"]
SHORT = ["pollution", "an invasive species", "habitat loss", "too many visitors", "rising seas"]
SOL = [["clean", "🧹 Stop it at the source and clean up"], ["remove", "🚫 Remove the invaders"], ["land", "🏞️ Protect more land"], ["trail", "🚶 Build trails and set visitor rules"], ["adapt", "🌱 Plant mangroves and marsh to help nature adjust"]]
def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}
C = CFG.get("cards", {})
def cc(k, f, d): return C.get(k, {}).get(f, d)

det = {
  "look": "Five real threats to Florida's wild places. Each card shows the threat. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 threats, one at a time. Tap a clue, then name the threat. Predict a solution that fits, and watch it at work.",
  "noun": "Threat", "need": 3, "inferQ": "What is the threat?", "inferDone": "Threat", "chartSo": "so a good solution is to",
  "predict": {"q": "Which solution do you predict fits this threat?", "options": SOL},
  "kicker": "The solution at work", "enough": "You already solved 3 threat files. Nice work, park scientist!",
  "cols": ["Threat file", "My observation", "Threat", "Solution", "My evidence"],
  "write": {"label": "Threat __ is ___. My solution is ___, and I'll know it worked when ___.", "starter": "Start with: \"Threat __ is…\"", "min": 15,
            "chips": [["trait", "Names what you see"], ["crit", "Names something to count or measure"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", cc("d1", "alt", "Bright green algae covering the water of a big lake"),
         [{"t": "Green algae covering a lake, fed by fertilizer runoff", "ok": True}, {"t": "A snake from Asia", "miss": "Look again. What is covering the water?"}, {"t": "A crowded trail", "miss": "Look again. This is a lake."}],
         0, "Fertilizer runoff feeds the algae. Which threat is that? Try again.",
         "clean", "The fertilizer comes from farms and lawns. Which solution stops it where it starts? Try again.",
         "d1h", cc("d1h", "alt", "A huge man-made marsh with plants cleaning water, seen from the air"), cc("d1h", "cap", "A filter marsh that traps fertilizer · South Florida"),
         "This filter marsh is evidence that stopping pollution works: it takes out most of the fertilizer before the water reaches the Everglades. Criteria: test the water.", "lake",
         "Lake Okeechobee sometimes grows huge algae blooms after rain washes fertilizer into it. Scientists test the water to measure how much fertilizer is in it."),
    card("B", "d2", cc("d2", "alt", "A striped lionfish with long, feathery fins over a reef"),
         [{"t": "A fish from the Pacific Ocean eating Florida reef fish", "ok": True}, {"t": "Bare dirt from too many hikers", "miss": "Look again. What animal is this?"}, {"t": "Rising salt water", "miss": "Look again. What animal is this?"}],
         1, "This fish doesn't belong in Florida. Which threat is that? Try again.",
         "remove", "The lionfish is an invader. Which solution takes it out? Try again.",
         "d2h", cc("d2h", "alt", "A diver holding a spear near a reef"), cc("d2h", "cap", "A diver removing lionfish · Florida"),
         "This diver is evidence that removing invaders helps: in 2026, divers removed more than 36,000 lionfish. Criteria: count how many are caught, and how many native fish are left.", "reef",
         "Lionfish have no natural enemies in Florida, so their numbers grew fast. Now people even cook and eat them."),
    card("C", "d3", cc("d3", "alt", "Rows of new houses built right up to the edge of a green wetland, seen from the air"),
         [{"t": "Houses built right up to the edge of wild land", "ok": True}, {"t": "Algae in a lake", "miss": "Look again. What is next to the wild land?"}, {"t": "A lionfish", "miss": "Look again. These are houses."}],
         2, "The wild land is being covered with houses. Which threat is that? Try again.",
         "land", "Animals are losing space. Which solution saves space for them? Try again.",
         "d3h", cc("d3h", "alt", "Tall cypress trees in a protected Florida swamp"), cc("d3h", "cap", "Protected land · Big Cypress National Preserve, Florida"),
         "This preserve is evidence that protecting land saves space for wildlife, like Florida panthers. Criteria: count the acres saved and the animals living there.", "swamp",
         "The Florida Wildlife Corridor is a plan to connect wild lands from the Everglades to the Panhandle, so animals can move safely between them."),
    card("D", "d4", cc("d4", "alt", "Many visitors walking across a beach and dunes"),
         [{"t": "Crowds of people packed onto a beach", "ok": True}, {"t": "A python", "miss": "Look again. Who is on the beach?"}, {"t": "New houses", "miss": "Look again. What is covering the sand?"}],
         3, "So many feet crush dune plants. Which threat is that? Try again.",
         "trail", "The plants need people to stay on a path. Which solution does that? Try again.",
         "d4h", cc("d4h", "alt", "A wooden walkover crossing over a sand dune to the beach"), cc("d4h", "cap", "A dune walkover · Florida"),
         "This walkover is evidence that trails protect plants: people still reach the beach, and the sea oats keep growing. Criteria: are the dune plants growing back?", "dune",
         "Some popular parks use timed tickets or limits so only so many people visit at once."),
    card("E", "d5", cc("d5", "alt", "Dead gray trees standing in salty water near the coast"),
         [{"t": "Trees killed after a hurricane pushed the sea inland", "ok": True}, {"t": "Bare dirt from hikers", "miss": "Look again. What killed these trees?"}, {"t": "A lionfish", "miss": "Look again. These are trees."}],
         4, "Storms and rising seas push salt water inland. Which threat is that? Try again.",
         "adapt", "Mangroves and marsh plants can handle salt water. Which solution plants them? Try again.",
         "d5h", cc("d5h", "alt", "Young mangrove plants growing along a shoreline"), cc("d5h", "cap", "Planting mangroves on a shoreline · Florida"),
         "These mangroves are evidence that helping nature adjust works: their roots hold the shore and shelter baby fish. Criteria: measure how far the shore wears away.", "coast",
         "Dead trees like these are called a ghost forest. As seas rise, storms push salt water farther inland. Mangroves and salt marshes can grow where seawater reaches."),
  ]
}

rebuild = {"title": "Use your evidence to rebuild the place", "missPrefix": "Hmm. Look at your threat file again. ", "kicker": "🌍 Rebuild the place", "whyStart": "I chose this because the threat file…",
  "envs": [
    {"key": "lake", "name": "🌊 A big lake", "img": "d1h", "cap": "Fresh water and marsh…"},
    {"key": "reef", "name": "🪸 A coral reef", "img": "d2h", "cap": "Clear salt water…"},
    {"key": "swamp", "name": "🌳 A cypress swamp", "img": "d3h", "cap": "Tall trees in water…"},
    {"key": "dune", "name": "🏖️ A beach dune", "img": "d4h", "cap": "Sand and sea oats…"},
    {"key": "coast", "name": "🌿 A mangrove coast", "img": "d5h", "cap": "Roots in salt water…"}
  ],
  "life": [
    {"name": "🦆 Ducks", "img": "d1h", "env": "lake", "miss": "Ducks swim on the lake and marsh."},
    {"name": "🐠 Parrotfish", "img": "d2h", "env": "reef", "miss": "Parrotfish graze on the reef."},
    {"name": "🐆 Florida panthers", "img": "d3h", "env": "swamp", "miss": "Florida panthers hunt in the cypress swamp."},
    {"name": "🦀 Ghost crabs", "img": "d4h", "env": "dune", "miss": "Ghost crabs dig in beach sand."},
    {"name": "🐟 Baby snook", "img": "d5h", "env": "coast", "miss": "Baby snook hide among mangrove roots."}
  ]}

quiz = [
  {"q": "What is a habitat?", "options": [
    {"t": "The place where a plant or animal lives and gets the food, water, and shelter it needs", "ok": "🌿 Yes! A habitat is the place where an organism lives, where it gets everything it needs to survive."},
    {"t": "A plan that scientists write to protect nature", "miss": "A habitat is a place, not a plan and not a list of rules."},
    {"t": "A list of rules for visitors at a national park", "miss": "A habitat is a place, not a plan and not a list of rules."}]},
  {"q": "A student notices that pollution from a nearby road is washing into a park river and killing fish. What should their habitat protection proposal include?", "options": [
    {"t": "Evidence that the pollution is harming the fish, plus a specific plan to reduce runoff", "ok": "🌲 Exactly! A strong proposal connects the problem to real evidence and explains a specific solution: not just what's wrong, but what to do about it."},
    {"t": "A drawing of a healthy river with no roads nearby", "miss": "A proposal needs both evidence AND a solution. A drawing alone doesn't explain what to do or why it would help."},
    {"t": "A list of every type of fish that lives in the river", "miss": "A proposal needs both evidence AND a solution. A species list alone doesn't explain what to do or why it would help."}]},
  {"q": "Which of the following is the best example of a \"criteria for success\" in a habitat protection proposal?", "options": [
    {"t": "\"The park has many different animals living in it\"", "miss": "Criteria should be specific and measurable, something you can actually observe and count over time."},
    {"t": "\"We want to protect the Everglades wetlands\"", "miss": "Criteria should be specific and measurable. \"We want to protect\" is a goal, not a measure of success."},
    {"t": "\"The number of nesting birds increases within two years of the cleanup\"", "ok": "⭐ That's it! Criteria need to be specific and measurable. \"Nesting birds increase within two years\" is something you can actually check."}]}
]

partA = {"title": "Plan your proposal", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  {"n": 1, "q": "List three different threats that could damage a national park habitat. Write one short sentence about what each one does.", "type": "text", "min": 15, "chips": [["threat", "Names threats (pollution, invaders, habitat loss…)"]]},
  {"n": 2, "q": "For each threat you listed, name one kind of evidence a scientist could use to show it's real. (Example: \"To prove pollution is a problem, test the water every month.\")", "type": "text", "min": 15, "chips": [["crit", "Names something to count or measure"]]},
  {"n": 3, "q": "Which threat will you write your protection proposal about?", "type": "text", "min": 3, "chips": [["threat", "Names one threat"]]}
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "What problem did you describe in your proposal? Explain it in two complete sentences. Be specific about what is being harmed and why it matters.", "type": "text", "min": 15, "chips": [["threat", "Names the threat"], ["because", "Gives a reason (because, so)"]]},
    {"n": 2, "q": "What criteria did you choose for your proposal? Explain how you would know, by observing or measuring something, that your solution is actually working.", "type": "text", "min": 12, "chips": [["crit", "Names something to count or measure"]]}
  ]},
  "write": {"title": "Make the case for your proposal", "do": "Pick one from your evidence chart. Answer the three questions. Use at least two of the science words under the boxes.",
    "vocab": ["habitat", "threat", "conservation", "proposal", "criteria", "evidence"], "need": 2,
    "prompts": [["What threat did you choose, and what evidence tells you it's a real problem?", "Start with: \"The threat I chose is… I know it's real because…\""],
                ["What is your solution?", "Start with: \"My solution is…\""],
                ["How will you know it worked?", "Start with: \"I will know it worked when I count or measure…\""]]},
  "partC": {"do": "Draw your solution in action in the park. Label the threat it stops, and one thing you will count or measure to check it.",
            "labels": ["The threat my solution stops", "What I will count or measure"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 threat files and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: my threats, evidence, and choice.", "req": {"text": {"in-a1": 15, "in-a2": 15, "in-a3": 3}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 15, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least two science words.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 2}}
  ]
}

premiere = {"title": "Premiere my park proposal", "thinkLabel": "The threat is", "director": "JUNIOR PARK SCIENTIST", "storyKicker": "My park proposal",
  "frames": [
    {"k": "formation", "label": "The proposal path", "img": "o2", "cap": "The proposal path: problem, evidence, solution, criteria."},
    {"k": "compare", "label": "The Footprint Test", "img": "ta", "cap": "The Footprint Test: a boardwalk keeps plants safe."},
    {"k": "wall", "label": "The River Comeback", "img": "l4", "cap": "The River Comeback: a plan with evidence brought a river back."},
    {"k": "det", "label": "Threat files", "img": "d2", "cap": "Threat files: each threat needs its own solution."}]}

nxt = {"title": "Unit 8 is complete", "text": "You finished Human Impact & Conservation! Next, Unit 9 begins: matter and energy."}

chips = {
  "part": {"any": ["scale", "scales", "diamond", "blotch", "blotches", "pattern", "brown", "dark", "pale", "skin", "shed", "see-through", "clear", "long", "snake", "python", "belly", "spots", "head", "tail"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["algae", "green", "lake", "fish", "lionfish", "fins", "houses", "homes", "people", "visitors", "dune", "beach", "trees", "dead", "salt", "water", "reef", "stripes"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "crit": {"any": ["count", "counts", "measure", "measures", "test", "tests", "number", "how many", "percent", "more", "fewer", "increase", "decrease", "track"]},
  "threat": {"any": ["pollution", "invasive", "invader", "invaders", "python", "lionfish", "habitat", "loss", "visitors", "trampling", "climate", "sea", "seas", "building", "roads"]}
}

L = {"id": "g3sci-25-02", "lesson": "25.02", "title": "Investigation: Protect a Park Proposal", "emoji": "📋",
  "details": ["📅 Q3 · Unit 8 · Human Impact &amp; Conservation", "📖 Week 25 · Lesson 25.02", "🌎 CPALMS SC.3.N.1.1, SC.3.N.1.7 · NGSS 3-LS4-4, 3-5-ETS1-1, 3-5-ETS1-2", "⏱ About 35 minutes"],
  "icans": ["identify a threat to a park habitat and explain why it matters.", "write a habitat protection proposal that includes a problem, evidence, solution, and criteria.", "use evidence to make a claim about why my proposed solution would reduce harm."],
  "opti": {"warm": "Our film starts in a quiet marsh, with something hiding in the grass. First, inspect a strange specimen from the Everglades.",
           "lesson": "Today you're a park scientist. Build a proposal, test two trails, then watch a river come back.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to write your own proposal. Name the threat, show your evidence, and tell us how you'll know it worked."},
  "film": film, "scientist": "park scientist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": [CFG.get("musicCredit", "Music: see credits."),
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The hidden-python scan, the proposal movie, the Footprint Test, and the River Comeback are models; every place photo is real."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-25-02-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the specimen, then tap three things you notice."},
  "how-25-02-compare": {"page": "Put the boots under one tray and the water under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the boots under one tray and the water under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-25-02-wall": {"page": wall["do"], "say": wall["do"]},
  "how-25-02-det": {"page": det["do"], "say": "Pick three threats, one at a time. Tap a clue, then name the threat. Predict a solution that fits, and watch it at work."},
  "how-25-02-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"25-02-welcome": L["opti"]["warm"], "25-02-lesson": L["opti"]["lesson"], "25-02-check": L["opti"]["check"], "25-02-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
