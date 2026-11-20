#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/30-01/lesson.json, how-lines.json, scripts.json, credits.json (30.01: no voices recorded; scripts only)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "How do Florida animals survive in such a wild, watery world?"

film = {
  "id": "g3sci-30-01", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 30.01 · How Are Florida Animals Adapted?",
  "title": "Now You See Me",
  "bigQuestion": BQ,
  "poster": "f_eyes", "endPoster": "f_trail", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.6},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 3.6, "type": "black", "sfxAt": [{"at": 0.4, "name": "bubbles"}, {"at": 2.0, "name": "bubbles"}], "fade": 0.5},
    ph(7.0, 5.6, "f_dawn", "Dark, still swamp water under a fallen branch covered with spiky air plants", "Corkscrew Swamp Sanctuary, Florida",
       frm=(1.12, .5, .6), to=(1.0, .5, .5), fade=1.0),
    ph(12.6, 5.8, "f_eyes", "An alligator swimming with only its eyes, nose, and the top of its head above the water", "An alligator near the Anhinga Trail · Everglades National Park",
       frm=(1.05, .4, .6), to=(1.25, .3, .8), sfxAt=[{"at": 0.4, "name": "bubbles"}]),
    ph(18.4, 5.6, "f_lizard", "A small gray-brown lizard on pale sand, almost the same color as the ground", "A Florida scrub lizard · Lake June-in-Winter Scrub State Park, Florida",
       frm=(1.0, .5, .5), to=(1.14, .45, .55)),
    {"t": 24.0, "d": 8.4, "type": "split", "img": "f_kitten", "alt": "A one-month-old Florida panther kitten with dark spots and blue eyes",
     "img2": "f_adult", "alt2": "A grown Florida panther with plain tan fur, resting on a log among palm fronds",
     "splitAt": 2.6, "splitDur": 2.4, "lab1": "A panther kitten · one month old", "lab2": "A grown Florida panther",
     "from": [1.0, .5, .45], "to": [1.06, .5, .45], "fade": 0.6, "sfxAt": [{"at": 2.6, "name": "whoosh"}]},
    ph(32.4, 7.6, "f_trail", "A long boardwalk crossing a grassy marsh toward a forest of tall cypress trees", "Corkscrew Swamp Sanctuary, Florida",
       frm=(1.0, .5, .5), to=(1.08, .5, .5), fade=0.9),
    {"t": 40.0, "d": 6.0, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 7.4, "d": 5.0, "text": "A dark, still swamp. Something is watching.", "voice": "opti-1"},
    {"t": 13.0, "d": 5.2, "text": "An alligator's eyes and nose sit right on top of its head.", "voice": "opti-2"},
    {"t": 18.8, "d": 5.0, "text": "On pale sand, a scrub lizard nearly disappears.", "voice": "opti-3"},
    {"t": 24.4, "d": 7.6, "text": "A panther kitten is born with spots. They fade as it grows.", "voice": "opti-4"},
    {"t": 32.8, "d": 6.8, "text": BQ, "voice": "opti-5"}
  ]
}

specimen = {
  "img": "spec", "aspect": "3/2", "radius": 0.07,
  "hotspots": [
    {"name": "A raised bump where the eye sat", "x": 0.68, "y": 0.09},
    {"name": "A nose hole at the very tip", "x": 0.10, "y": 0.32},
    {"name": "Cone-shaped teeth", "x": 0.27, "y": 0.45},
    {"name": "A big opening in the jaw", "x": 0.78, "y": 0.42},
    {"name": "A long, strong lower jaw", "x": 0.60, "y": 0.70}
  ],
  "kicker": "🔎 Mystery specimen", "title": "Whose skull is this?",
  "alt": "A long, pale skull with an open jaw full of cone-shaped teeth, on a black background",
  "look": "A real skull, the bones of an animal's head, about as long as your arm. Look at its parts: the bumps on top, the tip of the snout, the teeth, and the jaw. A specimen is one real thing that scientists study. This animal lives in Florida. Whose skull is it? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the skull, then tap 3 things you notice.",
  "number": "No. 30.01-A",
  "card": ["<b>Specimen A</b>", "Length: about 47 cm (18 inches)", "Belonged to: a Florida animal", "Whose is it? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🦎", "adaptation", "A body feature or behavior that helps an animal survive in its habitat."],
  ["🏡", "habitat", "The natural place where an animal lives and finds what it needs to survive."],
  ["🍃", "camouflage", "Colors or patterns that help an animal blend in and hide from predators or prey."],
  ["🦅", "predator", "An animal that hunts and eats other animals to survive."],
  ["🐟", "prey", "An animal that is hunted and eaten by a predator."],
  ["🧬", "trait", "A feature of an animal's body or behavior that it inherits from its parents."],
  ["🧭", "migrate", "To move from one place to another when the seasons change. Many birds migrate to Florida for the winter."]
]

parts = [
  {"kicker": "🌱 Part 1", "title": "What Is an Adaptation?",
   "html": "<p>An adaptation is a body part or behavior that helps an animal survive in its habitat. Adaptations are traits passed down from parents. An animal can't grow a new one just because it needs it.</p><p>Animals also respond when the seasons change. In winter, manatees swim to warm springs, and many birds migrate south to Florida from colder places.</p>"},
  {"kicker": "🌤 Part 2", "title": "Florida Animals Up Close",
   "html": "<p>An alligator's eyes and nostrils sit on top of its head, so it can hide underwater and still see and breathe. A Florida panther's padded paws let it walk quietly, and its tan fur blends with the forest.</p><p>Camouflage helps predators sneak up on prey. It also helps prey hide.</p>"},
  {"kicker": "🌍 Part 3", "title": "Animal Groups",
   "html": "<p>Scientists sort animals into groups by their body features. Mammals have fur and feed their babies milk. Birds have feathers. Reptiles have dry scales. Amphibians have smooth, wet skin. Fish have scales and breathe with gills.</p><p>All of these are vertebrates: animals with a backbone. Insects and spiders have no backbone. Some animals, like panthers, give birth to live young; others, like alligators, lay eggs.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Adaptation Files"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the cold weather.",
  "kicker": "🎞️ Put the scenes in order", "title": "What do manatees do when winter comes?",
  "look": "Four real photos show what Florida manatees do in winter, from the first cold days to the warm days of spring. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "A thin white mist lying on a calm pond at sunrise on a cool morning", "text": "A cold front cools Florida's rivers and bays.", "play": "Cold weather comes.",
     "miss": ["", "Winter starts with the cold weather. Try frame 1.", "Winter starts with the cold weather. Try frame 1.", "Winter starts with the cold weather. Try frame 1."]},
    {"img": "o2", "alt": "Three manatees swimming over a sandy spring bottom toward a quiet spot", "text": "Manatees swim upriver toward a warm spring.", "play": "They swim to a spring.",
     "miss": ["The cold has to come first. Try a later frame.", "", "They swim there before they crowd in. Try an earlier frame.", "They swim there before they crowd in. Try an earlier frame."]},
    {"img": "o3", "alt": "Dozens of manatees resting close together in clear, shallow spring water", "text": "Many manatees crowd into the warm spring water.", "play": "They crowd in.",
     "miss": ["They have to reach the spring first. Try a later frame.", "They have to reach the spring first. Try a later frame.", "", "They crowd in before spring comes. Try an earlier frame."]},
    {"img": "o4", "alt": "Two manatees swimming in clear blue-green water", "text": "When warm weather returns, they spread out to feed again.", "play": "Spring: they spread out.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Mia says, \"If a manatee gets cold, it will just grow thick fur.\" What do you think?",
    "options": [
      {"t": "Mia is right. It will grow fur when it needs it.", "miss": "Look at the movie again. What did the manatees do when it got cold?"},
      {"t": "It can't grow new body parts when it wants to. It swims to warm water instead.", "ok": "Yes! Adaptations are passed down from parents. A manatee's way of surviving winter is a behavior: it moves to warm springs."}
    ]
  }
}

movie = {
  "model": "manatee-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "❄️",
  "real": "real", "realAlt": "Manatees resting in clear, shallow spring water near a rope line",
  "stamp": "SAFE AND WARM!", "endCap": "Real manatees in a warm spring.",
  "beats": [
    {"at": 0, "cap": "1 · Cold weather comes.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["November"], "sfx": "whoosh"},
    {"at": 2600, "cap": "2 · They swim to a spring.", "model": {"show": "s2"}, "counter": ["December"]},
    {"at": 5200, "cap": "3 · They crowd in.", "model": {"show": "s3"}, "counter": ["January"]},
    {"at": 7800, "cap": "4 · Spring: they spread out.", "model": {"show": "s4"}, "counter": ["March"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Hide Test", "title": "Which background hides which animal?",
  "look": "Two real Florida animals, each on a lit tray. Specimen A is a green tree frog. Specimen B is a Florida scrub lizard. Under the trays are two model backgrounds: a big green leaf, and a patch of pale scrub sand.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "A bright green tree frog sitting on a green leaf", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A gray-brown scrub lizard on sand and dry leaves", "label": "Specimen B"}
  ],
  "materials": [{"key": "leaf", "label": "A big green leaf", "img": "m_leaf"}, {"key": "sand", "label": "A patch of pale sand", "swatch": "sand"}],
  "ask": [
    {"q": "Which animal is bright green?", "ans": "A", "ok": "Yes. Specimen A is the green tree frog.", "miss": "Look closely. Which one is green?"},
    {"q": "Which animal is gray-brown, like sand?", "ans": "B", "ok": "Yes. Specimen B is the scrub lizard.", "miss": "Look again. Which one is sandy-colored?"}
  ],
  "press": "🎯 Run the test",
  "testDo": "Put the green leaf under one tray and the pale sand under the other: drag them, or tap one, then a tray. Press <b>Run the test</b>. Then swap.",
  "disclaimer": "This is a model. No real animals are tested.",
  "results": {
    "Aleaf": {"text": "The green frog almost disappears on the green leaf!", "fx": "shade"},
    "Asand": {"text": "The bright green frog stands out on the pale sand. A hawk could spot it.", "fx": "glow"},
    "Bleaf": {"text": "The sandy lizard stands out against the green leaf.", "fx": "glow"},
    "Bsand": {"text": "The lizard almost vanishes on the pale sand!", "fx": "shade"}
  },
  "best": ["Aleaf", "Bsand"],
  "frame": "This animal's color matches ___, so it hides best in ___.", "claimLead": "This animal's color matches", "claimMid": "so it hides best in",
  "claim": {
    "A": {"feat": ["green leaves", "pale sand"], "featOk": 0, "eat": ["a wet, leafy cypress forest", "dry, sandy scrub"], "eatOk": 0},
    "B": {"feat": ["green leaves", "pale sand"], "featOk": 1, "eat": ["a wet, leafy cypress forest", "dry, sandy scrub"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>Green camouflage.</b> A green tree frog's color blends with leaves, and its sticky toe pads hold it on wet leaves and bark.",
    "B": "<b>Sandy camouflage.</b> A scrub lizard's gray-brown skin blends with pale scrub sand, which hides it from hawks."
  },
  "missFeat": "Look at your tests for {label} again. Where did it almost disappear?",
  "missClaim": "Think about your tests. Which Florida habitat has that background?",
  "done": "Camouflage works when an animal's colors match its habitat. The frog hides on leaves. The lizard hides on sand.",
  "after": {"kicker": "🎬 Behind the scenes · Wet wings", "img": "after", "alt": "An anhinga with its wings spread wide, drying them in the sun",
            "html": "An anhinga's feathers soak up water, so it can sink and swim underwater to spear fish. After a dive, it spreads its wings in the sun to dry them before it can fly well."}
}

wall = {
  "kicker": "🗄️ The Classification Cabinet", "title": "Open one drawer for each animal group",
  "look": "A model cabinet with four drawers. Each drawer holds one Florida animal and a real photo. The brass dial on the left shows which drawer is open.",
  "do": "First, make a prediction. Then brush the glowing step: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "A panther and an anhinga both hunt. Do you predict they belong to the same animal group?",
              "options": [["no", "No, they are in different groups"], ["yes", "Yes, they are both hunters"]], "answer": "no",
              "mine": "Your prediction: <b>{p}</b>. Let's open the drawers and find out.",
              "confirm": "You predicted different groups. You were right: a panther is a mammal and an anhinga is a bird.",
              "change": "You predicted the same group. The cabinet changed that idea: scientists group animals by body features, so the panther is a mammal and the anhinga is a bird."},
  "sky": "sky", "skyAlt": "A long boardwalk crossing a marsh toward cypress trees", "skyCap": "Corkscrew Swamp Sanctuary, Florida",
  "unit": "Drawer", "found": "Clue found in Drawer {n}",
  "elevator": ["Cabinet", "Mammal", "Bird", "Reptile", "Amphibian"],
  "line": ["FUR AND FEATHERS", "SCALES AND WET SKIN"],
  "lockTag": "🔒 Open the drawer above first", "locked": "Open the drawer above first. We go one drawer at a time.",
  "first": "Brush the glowing top drawer. Drag across it (or tap it again and again).", "next": "Keep going. Brush Drawer {n}.",
  "endTitle": "All 4 drawers opened",
  "endText": "Look at the cabinet. Each group shares body features: fur, feathers, dry scales, or smooth, wet skin.",
  "rule": "<b>Scientists sort animals into groups by their features.</b> Mammals have fur or hair and feed milk to their babies. Birds have feathers. Reptiles have dry scales. Amphibians have smooth, wet skin and start life in water.",
  "choices": ["🐾 Mammal: fur, milk for babies", "🪶 Bird: feathers and wings", "🐊 Reptile: dry, tough scales", "🐸 Amphibian: smooth, wet skin"],
  "layers": [
    {"name": "Drawer 1 · Florida panther", "rock": "leafdark", "img": "l1", "alt": "A Florida panther walking along a dirt trail beside green plants",
     "ask": "Look at Drawer 1. Read the clue AND the photo. What group is it?",
     "clue": "A Florida panther has a coat of fur. A mother panther feeds her kittens milk.",
     "ans": 0, "ok": "Yes! Fur and milk for babies: the panther is a mammal.", "tag": "🐾 Panther · mammal",
     "miss": {"1": "Look again. Does a panther have feathers?", "2": "Not quite. Is a panther covered in scales?", "3": "Not yet. Does a panther have smooth, wet skin?"},
     "env": "e1", "envAlt": "A mother panther and two kittens walking past on a trail camera", "envCap": "A mother panther and kittens on a trail camera · Florida Panther National Wildlife Refuge"},
    {"name": "Drawer 2 · Anhinga", "rock": "haze", "img": "l2", "alt": "An anhinga with its wings spread open on a branch over blue water",
     "ask": "Look at Drawer 2. Read the clue AND the photo. What group is it?",
     "clue": "An anhinga has feathers and wings. It lays eggs in a nest of sticks.",
     "ans": 1, "ok": "Yes! Feathers and wings: the anhinga is a bird.", "tag": "🪶 Anhinga · bird",
     "miss": {"0": "Not quite. Does an anhinga have fur?", "2": "Close! It lays eggs, but read the clue: does it have scales or feathers?", "3": "Not yet. Is its skin smooth and wet?"},
     "env": "e2", "envAlt": "White egrets and dark wading birds feeding together in a shallow marsh", "envCap": "Birds feeding together · Shark Valley, Everglades National Park"},
    {"name": "Drawer 3 · American alligator", "rock": "water2", "img": "l3", "alt": "An alligator swimming low in dark water, its bumpy back showing",
     "ask": "Look at Drawer 3. Read the clue AND the photo. What group is it?",
     "clue": "An alligator has dry, tough scales. It lays eggs with hard shells in a nest on land.",
     "ans": 2, "ok": "Yes! Dry, tough scales: the alligator is a reptile.", "tag": "🐊 Alligator · reptile",
     "miss": {"0": "Not quite. Does an alligator have fur?", "1": "Not yet. Does it have feathers?", "3": "Close! It lives near water, but read the clue: is its skin smooth and wet, or scaly?"},
     "env": "e3", "envAlt": "A boardwalk through a swamp with tall cypress trees", "envCap": "A cypress swamp · Corkscrew Swamp Sanctuary, Florida"},
    {"name": "Drawer 4 · Green tree frog", "rock": "leafsun", "img": "l4", "alt": "A green tree frog gripping a thin stem",
     "ask": "Look at Drawer 4. Read the clue AND the photo. What group is it?",
     "clue": "A green tree frog has smooth, wet skin. It lays its eggs in water, and its tadpoles live in water.",
     "ans": 3, "ok": "Yes! Smooth, wet skin and a start in water: the frog is an amphibian.", "tag": "🐸 Tree frog · amphibian",
     "miss": {"0": "Not this one. Does a frog have fur?", "1": "Not quite. Does a frog have feathers?", "2": "Close! But read the clue: is its skin dry and scaly, or smooth and wet?"},
     "env": "e4", "envAlt": "A boardwalk winding through a green, wet forest", "envCap": "A wet cypress forest · Corkscrew Swamp Sanctuary, Florida"}
  ],
  "mix": {
    "q": "Jay says, \"Camouflage only helps animals that get hunted.\" What do you think?",
    "options": [
      {"t": "Jay is right. Only prey use camouflage.", "miss": "Think about the panther's tan fur and the alligator's dark, bumpy back. Are they prey?"},
      {"t": "Predators use camouflage too, to sneak up on their prey.", "ok": "Yes! A panther's tan fur and an alligator's dark back help them get close to prey without being seen."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "Only in Florida",
  "img": "wow", "alt": "A blue and gray Florida scrub-jay perched on a bare branch in scrub",
  "caption": "A Florida scrub-jay at Merritt Island National Wildlife Refuge",
  "html": "<p style=\"margin:0 0 8px\">The Florida scrub-jay lives nowhere else in the world. It lives only in Florida's dry, sandy scrub.</p><p style=\"margin:0\">Each fall, a scrub-jay buries thousands of acorns in the sand, then digs many of them up to eat later.</p>",
  "inset": "inset", "insetCap": "Scrub-jays perch up high to watch for hawks."}

keyIdea = "Adaptations are traits that help animals survive in their habitats, and they are passed down from parents. Florida animals have adaptations that match their homes: an alligator's eyes on top of its head, a panther's quiet paws, a lizard's sandy camouflage. Animals also respond to the seasons, like manatees swimming to warm springs in winter. Scientists sort animals into groups, like mammals, birds, reptiles, and amphibians, by their body features."

M = ["🐾 Mammal", "🪶 Bird", "🐊 Reptile", "🐸 Amphibian"]
SHORT = ["a mammal", "a bird", "a reptile", "an amphibian"]
SOL = [["water", "💧 Deep, dark swamp water"], ["forest", "🌲 Pine forest"], ["edge", "🌿 A river or spring edge"], ["cypress", "🌳 A wet, leafy forest"], ["scrub", "🏜️ Dry, sandy scrub"]]


def card(id_, img, alt, clues, orgAns, orgMiss, envAns, envMiss, envImg, envAlt, envCap, reveal, rb, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": M, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "env": dict(SOL)[envAns].split(" ", 1)[1], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": rb, "bts": bts}


det = {
  "look": "Five real Florida animals. Each card shows what scientists saw. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap an adaptation you see, then name its animal group. Predict where it lives, and watch its habitat appear.",
  "noun": "Card", "need": 3, "inferQ": "What group is it in?", "inferDone": "It's", "chartSo": "and it lives in",
  "predict": {"q": "Where do you predict it lives?", "options": SOL},
  "kicker": "Its real habitat", "enough": "You already solved 3 adaptation cards. Nice work, biologist!",
  "cols": ["Card", "My observation", "Animal group", "Habitat", "My evidence"],
  "write": {"label": "Card __ shows ___. This adaptation helps it ___ in its habitat, because ___.", "starter": "Start with: \"Card __ shows…\"", "min": 15,
            "chips": [["trait", "Names an adaptation"], ["hab", "Names the habitat"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "An alligator resting in shallow, clear water, its eyes and nostrils on top of its head",
         [{"t": "Eyes and nostrils on top of its head", "ok": True}, {"t": "Sticky toe pads", "miss": "Look again. Does it have toe pads?"}, {"t": "Feathers", "miss": "Look again. Does it have feathers?"}],
         2, "An alligator has dry, tough scales. Which group is that? Try again.",
         "water", "With its eyes and nose on top, where can it hide and still see and breathe? Try again.",
         "d1h", "Dark, still swamp water under tangled trees", "A dark swamp · Corkscrew Swamp Sanctuary, Florida",
         "With its eyes and nostrils on top of its head, an alligator hides in dark swamp water and still sees and breathes.", "water",
         "Baby alligators have yellow stripes. The stripes fade as they grow too big for most predators."),
    card("B", "d2", "A Florida panther sitting in tall grass among palm plants",
         [{"t": "Big, padded paws and tan fur", "ok": True}, {"t": "Wet wings", "miss": "Look again. Does it have wings?"}, {"t": "Scaly skin", "miss": "Look again. Is it scaly?"}],
         0, "A panther has fur, and mothers feed their kittens milk. Which group is that? Try again.",
         "forest", "Quiet paws and tan fur help it sneak through which habitat? Try again.",
         "d2h", "Tall, thin pine trees and palmettos under a blue sky", "Pine flatwoods · Royal Palm Beach Pines Natural Area, Florida",
         "Padded paws let a panther walk quietly through pine forests, and its tan fur blends with the shadows. Scientists think only about 120 to 230 adult Florida panthers live in the wild.", "forest",
         "Panther kittens are born with spots that help them hide. The spots fade as they grow."),
    card("C", "d3", "A dark anhinga with its wings spread out to dry among tall grass",
         [{"t": "Wet wings spread out to dry", "ok": True}, {"t": "Sandy-colored skin", "miss": "Look again. Is it sandy?"}, {"t": "Padded paws", "miss": "Look again. Does it have paws?"}],
         1, "An anhinga has feathers and wings. Which group is that? Try again.",
         "edge", "It dives for fish, then dries its wings in the sun. Where would it live? Try again.",
         "d3h", "Clear water flowing between trees hung with Spanish moss, with a red canoe", "A spring run, where anhingas fish · Blue Spring State Park, Florida",
         "An anhinga's feathers get soaked, so it can swim underwater and spear fish. Then it perches by the water to dry its wings.", "edge",
         "Anhingas are sometimes called snakebirds, because they swim with only their long neck above the water."),
    card("D", "d4", "A green tree frog sitting on a big green leaf",
         [{"t": "Sticky toe pads and bright green skin", "ok": True}, {"t": "A long, scaly tail", "miss": "Look again. Does it have a tail?"}, {"t": "Feathers", "miss": "Look again. Does it have feathers?"}],
         3, "A tree frog has smooth, wet skin and starts life as a tadpole. Which group is that? Try again.",
         "cypress", "Sticky toes and green skin help it climb and hide where? Try again.",
         "d4h", "Dark swamp water under a fallen branch covered with air plants", "A wet, leafy swamp · Corkscrew Swamp Sanctuary, Florida",
         "Sticky toe pads let a green tree frog climb wet leaves and bark, and its green skin hides it among the leaves.", "cypress",
         "Green tree frogs live across the southeastern United States, including all of Florida."),
    card("E", "d5", "A gray-brown scrub lizard lying flat on pale, speckled sand",
         [{"t": "Gray-brown skin that matches the sand", "ok": True}, {"t": "Wet wings", "miss": "Look again. Does it have wings?"}, {"t": "Soft fur", "miss": "Look again. Does it have fur?"}],
         2, "A scrub lizard has dry scales. Which group is that? Try again.",
         "scrub", "Its skin matches pale sand. Where would it hide best? Try again.",
         "d5h", "Two hikers walking a sandy trail through low scrub bushes", "Florida scrub · Juniper Prairie Wilderness, Ocala National Forest",
         "The Florida scrub lizard lives in dry, sandy scrub. Its gray-brown skin blends with the pale sand and hides it from hawks.", "scrub",
         "Like the scrub-jay, the Florida scrub lizard lives only in Florida.")
  ]
}

rebuild = {"title": "Use your evidence to rebuild the scene", "missPrefix": "Hmm. Look at your adaptation card again. ", "kicker": "🌍 Rebuild the scene", "whyStart": "I chose this because its adaptation…",
  "envs": [
    {"key": "water", "name": "💧 A dark swamp", "img": "d1h", "cap": "Deep, dark water…"},
    {"key": "forest", "name": "🌲 A pine forest", "img": "d2h", "cap": "Tall pines…"},
    {"key": "edge", "name": "🌿 A spring run", "img": "d3h", "cap": "Clear water…"},
    {"key": "cypress", "name": "🌳 A leafy swamp", "img": "d4h", "cap": "Wet leaves and bark…"},
    {"key": "scrub", "name": "🏜️ Sandy scrub", "img": "d5h", "cap": "Pale sand…"}
  ],
  "life": [
    {"name": "🐊 An alligator", "img": "d1", "env": "water", "miss": "The alligator belongs in the dark swamp."},
    {"name": "🐾 A Florida panther", "img": "d2", "env": "forest", "miss": "The panther belongs in the pine forest."},
    {"name": "🪶 An anhinga", "img": "d3", "env": "edge", "miss": "The anhinga belongs by the spring run."},
    {"name": "🐸 A green tree frog", "img": "d4", "env": "cypress", "miss": "The tree frog belongs in the leafy swamp."},
    {"name": "🦎 A scrub lizard", "img": "d5", "env": "scrub", "miss": "The scrub lizard belongs in the sandy scrub."}
  ]}

quiz = [
  {"q": "What is an adaptation?", "options": [
    {"t": "A type of food that Florida animals eat to survive", "miss": "Think about the vocabulary word. An adaptation isn't about food or places. It's about body features and behaviors that help an animal live and thrive."},
    {"t": "A trait that helps an animal survive in its habitat", "ok": "🌿 Exactly right! An adaptation is a trait, passed from parents, that helps an animal survive where it lives."},
    {"t": "The name of a Florida ecosystem or wild place", "miss": "Think about the vocabulary word. An adaptation isn't about food or places. It's about body features and behaviors that help an animal live and thrive."}]},
  {"q": "The American alligator's eyes and nostrils sit on top of its head. How does this help it survive?", "options": [
    {"t": "It helps the alligator hear better underwater", "miss": "Think about what an animal needs to do when hunting, and what the top-of-the-head placement makes possible."},
    {"t": "It helps the alligator digest fish more easily", "miss": "Think about what an animal needs to do when hunting, and what the top-of-the-head placement makes possible."},
    {"t": "It lets the alligator breathe and watch for prey while mostly underwater", "ok": "🐊 Yes! Eyes and nostrils on top mean the alligator can stay hidden in dark water and still hunt. It's one of its most important adaptations."}]},
  {"q": "A Florida scrub lizard has sandy-colored skin that matches the pale ground around it. This is an example of what?", "options": [
    {"t": "Camouflage", "ok": "⭐ Right! When an animal's colors blend into its surroundings, that's camouflage, one of the most common adaptations for both predators and prey."},
    {"t": "Predation", "miss": "Camouflage, predation, and migration are all different things. Which word describes blending in with your surroundings?"},
    {"t": "Migration", "miss": "Camouflage, predation, and migration are all different things. Which word describes blending in with your surroundings?"}]}
]


def matchq(n, q, opts, ans, ok, miss):
    return {"n": n, "q": q, "type": "choice", "options": [{"t": c, "ok": ok} if i == ans else {"t": c, "miss": miss} for i, c in enumerate(opts)]}


partA = {"title": "Match the adaptation", "do": "Read each one. Pick the best answer, or type your answer.", "items": [
  matchq(1, "Sticky toe pads that grip wet bark and leaves in the cypress forest.", ["Green tree frog", "Florida panther", "Anhinga"], 0, "Yes. Sticky toe pads belong to the green tree frog.", "Which animal climbs wet leaves and bark?"),
  matchq(2, "Eyes and nostrils on top of the skull for hunting while underwater.", ["Florida scrub lizard", "American alligator", "Green tree frog"], 1, "Yes. That's the American alligator.", "Which animal hides in water with only its eyes and nose showing?"),
  matchq(3, "Sandy-colored skin that blends with dry, pale scrub soil.", ["Anhinga", "Florida panther", "Florida scrub lizard"], 2, "Yes. That's the Florida scrub lizard.", "Which animal lives on pale scrub sand?"),
  matchq(4, "Feathers that are not waterproof, so it can swim underwater to catch fish.", ["Anhinga", "American alligator", "Green tree frog"], 0, "Yes. That's the anhinga.", "Which animal has feathers?"),
  matchq(5, "Large, padded paws for quiet movement through pine flatwoods.", ["Green tree frog", "Florida panther", "Florida scrub lizard"], 1, "Yes. That's the Florida panther.", "Which animal has paws?")
]}

assign = {
  "partA": partA,
  "partB": {"title": "Short answer", "do": "Answer in complete sentences. Use your science words.", "items": [
    {"n": 1, "q": "What is an adaptation? Give one example from a Florida animal and explain how it helps that animal survive.", "type": "text", "min": 12, "chips": [["adapt", "Says what an adaptation is"], ["animal", "Names a Florida animal"]]},
    {"n": 2, "q": "Why do animals in different habitats have different adaptations? Use the words habitat and trait in your answer.", "type": "text", "min": 12, "chips": [["habw", "Uses the word habitat"], ["traitw", "Uses the word trait"]]}
  ]},
  "write": {"title": "A Florida scrub lizard and a green tree frog live in very different places. How do their adaptations help each one survive where it lives?", "do": "Pick one from your evidence chart. Answer the three questions. Use at least one of the science words under the boxes.",
    "vocab": ["adaptation", "camouflage", "habitat", "trait"], "need": 1,
    "prompts": [["What do you think?", "Start with: \"I think the scrub lizard and the tree frog survive in different places because…\""],
                ["What did you learn that supports your thinking?", "Start with: \"I know this because the lesson showed that…\""],
                ["Why does that make sense?", "Start with: \"This makes sense because animals that match their habitat…\""]]},
  "partC": {"do": "Pick any Florida animal from this lesson. Draw it in its habitat and label two adaptations. For each label, name the feature and how it helps.",
            "labels": ["Adaptation 1: the feature and how it helps", "Adaptation 2: the feature and how it helps"]},
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 adaptation cards and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: all five matched.", "req": {"choice": ["a1", "a2", "a3", "a4", "a5"]}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 12, "in-b2": 12}}},
    {"k": "c", "t": "Part C: my drawing and both labels.", "req": {"sketch": True, "text": {"in-c1": 6, "in-c2": 6}}},
    {"k": "w", "t": "Write and explain, with at least one science word.", "req": {"text": {"in-w1": 10, "in-w2": 10, "in-w3": 10}, "vocab": 1}}
  ]
}

premiere = {"title": "Premiere my Florida animal story", "thinkLabel": "Its animal group", "director": "JUNIOR BIOLOGIST", "storyKicker": "My Florida animal story",
  "frames": [
    {"k": "formation", "label": "Manatee winter", "img": "o3", "cap": "Manatee winter: cold comes, they swim to a warm spring."},
    {"k": "compare", "label": "The Hide Test", "img": "ta", "cap": "The Hide Test: each color hides best in its own habitat."},
    {"k": "wall", "label": "The Classification Cabinet", "img": "l2", "cap": "The Classification Cabinet: mammal, bird, reptile, amphibian."},
    {"k": "det", "label": "Adaptation files", "img": "d2", "cap": "Adaptation files: the right animal for the right place."}]}

nxt = {"title": "Coming up next: 30.02", "text": "Investigation: Adaptation Comparison. Next time, compare animals of the same kind and find out why small differences matter."}

chips = {
  "part": {"any": ["teeth", "tooth", "bump", "bumps", "eye", "eyes", "socket", "nose", "nostril", "hole", "holes", "jaw", "snout", "long", "skull", "bone", "bones", "sharp", "pointy", "white", "open"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "trait": {"any": ["eyes", "nostrils", "top", "paws", "padded", "fur", "tan", "wings", "wet", "feathers", "toe", "pads", "sticky", "green", "skin", "sandy", "sand", "camouflage", "scales"]},
  "hab": {"any": ["swamp", "water", "forest", "pine", "spring", "river", "scrub", "sand", "sandy", "leafy", "habitat", "cypress"]},
  "because": {"re": "\\b(because|since|so)\\b"},
  "adapt": {"any": ["adaptation", "trait", "helps", "survive", "feature", "behavior"]},
  "animal": {"any": ["alligator", "panther", "anhinga", "frog", "lizard", "manatee", "scrub-jay", "jay", "heron"]},
  "habw": {"any": ["habitat", "habitats"]},
  "traitw": {"any": ["trait", "traits"]}
}

L = {"id": "g3sci-30-01", "lesson": "30.01", "title": "How Are Florida Animals Adapted?", "emoji": "🪿",
  "details": ["📅 Q4 · Unit 10 · Florida Ecosystems", "📖 Week 30 · Lesson 30.01", "🌎 CPALMS SC.3.L.15.1, SC.3.L.17.1", "⏱ About 35 minutes"],
  "icans": ["explain what an adaptation is and why animals need them to survive.", "describe specific adaptations of Florida animals and connect each one to survival.", "use evidence to explain why some animals survive better in certain Florida habitats than others."],
  "opti": {"warm": "Our film starts in a dark Florida swamp where something is watching. First, inspect a mysterious skull.",
           "lesson": "Today you're a biologist. Follow manatees through winter, test which animal hides where, then open the Classification Cabinet.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to show what you learned. Match the adaptations, then draw a Florida animal in its home."},
  "film": film, "scientist": "biologist", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: Swan Lake, Act II (Pyotr Ilyich Tchaikovsky), European Archive via Musopen, public domain recording (via Wikimedia Commons).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The manatee movie, the Hide Test, and the Classification Cabinet are models; every place photo is real. The green leaf in the Hide Test is cut from the tree frog photo."]}

json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-30-01-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the skull, then tap three things you notice."},
  "how-30-01-compare": {"page": "Put the green leaf under one tray and the pale sand under the other: drag them, or tap one, then a tray. Press Run the test. Then swap.",
                        "say": "Put the green leaf under one tray and the pale sand under the other: drag them, or tap one, then a tray. Press Run the test. Then swap."},
  "how-30-01-wall": {"page": wall["do"], "say": wall["do"]},
  "how-30-01-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap an adaptation you see, then name its animal group. Predict where it lives, and watch its habitat appear."},
  "how-30-01-partc": {"page": assign["partC"]["do"], "say": assign["partC"]["do"]}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"30-01-welcome": L["opti"]["warm"], "30-01-lesson": L["opti"]["lesson"], "30-01-check": L["opti"]["check"], "30-01-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
