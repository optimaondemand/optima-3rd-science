#!/usr/bin/env python3
"""Writes tools/sparkle/lessons/32-02/lesson.json, how-lines.json, scripts.json, credits.json (32.02: no voices recorded; scripts only).
Images come from prep.py (run it first). Part C is the Park Slide Studio (engine/wf-studio.js)."""
import json, os
D = os.path.dirname(os.path.abspath(__file__))


def ph(t, d, img, alt, place, frm=(1.0, .5, .5), to=(1.1, .5, .5), fade=.8, **kw):
    s = {"t": t, "d": d, "type": "photo", "img": img, "alt": alt, "from": list(frm), "to": list(to), "place": place, "fade": fade}
    s.update(kw); return s


BQ = "How do you turn scientific research into something other people can actually understand?"

film = {
  "id": "g3sci-32-02", "mount": "wf-film", "kicker": "Opti's Wonder Films", "lesson": "Lesson 32.02 · Build a Park Ecosystem Presentation",
  "title": "Campfire Talk",
  "bigQuestion": BQ,
  "poster": "f_rns", "endPoster": "f_end", "startTarget": "#tab-vocab", "music": {"src": "music", "vol": 0.5},
  "shots": [
    {"t": 0, "d": 3.4, "type": "leader", "top": "Optima Academy", "name": "Opti's Wonder Films", "bottom": "presents", "fade": 1.0},
    {"t": 3.4, "d": 6.2, "type": "archive", "img": "f_rns", "alt": "An old blue poster of a white geyser, with the words Ranger Naturalist Service: nature walks, field trips, campfire programs, nature talks", "note": "A park poster from about 1938.", "fade": 0.8, "sfx": "whoosh", "sfxArg": 0.8},
    {"t": 9.6, "d": 6.6, "type": "archive", "img": "f_walk", "alt": "An old black-and-white photo of a group of visitors standing with a guide below a tall waterfall", "note": "A nature walk in Yosemite Valley, about 1920.", "fade": 0.8},
    ph(16.2, 6.4, "f_exhibit", "A bright museum exhibit with a big photo panel and a model of a mosquito", "An exhibit at the Guy Bradley Visitor Center · Everglades National Park",
       frm=(1.12, .5, .5), to=(1.0, .5, .5)),
    ph(22.6, 6.0, "f_talk", "A park ranger in a flat hat talking with a group of visitors outside", "A ranger talks with visitors at Logan Pass · Glacier National Park",
       frm=(1.0, .5, .45), to=(1.1, .5, .4)),
    ph(28.6, 5.6, "f_read", "A visitor reading a sign with photos beside a trail", "Reading a trail sign · Cuyahoga Valley National Park",
       frm=(1.0, .45, .5), to=(1.08, .5, .5)),
    ph(34.2, 8.2, "f_end", "A tall waterfall pouring over granite cliffs, with a calm river below", "Upper and Lower Yosemite Falls · Yosemite National Park",
       frm=(1.0, .5, .5), to=(1.08, .5, .45), fade=0.9),
    {"t": 42.4, "d": 5.6, "type": "title", "fade": 1.2}
  ],
  "captions": [
    {"t": 3.8, "d": 5.6, "text": "Long ago, parks began sending rangers to teach visitors about nature.", "voice": "opti-1"},
    {"t": 10.0, "d": 6.0, "text": "In 1920, scientists started free nature walks in Yosemite.", "voice": "opti-2"},
    {"t": 16.6, "d": 5.8, "text": "Today, exhibits use real photos, models, and just a few words.", "voice": "opti-3"},
    {"t": 23.0, "d": 5.4, "text": "Rangers give short talks, so visitors can understand in minutes.", "voice": "opti-4"},
    {"t": 29.0, "d": 5.0, "text": "Every sign, talk, and slide starts with real evidence.", "voice": "opti-5"},
    {"t": 34.6, "d": 7.4, "text": BQ, "voice": "opti-6"}
  ]
}

specimen = {
  "img": "spec", "aspect": "5/4", "radius": 0.03,
  "hotspots": [
    {"name": "A paper label with the number 2425", "x": 0.91, "y": 0.11},
    {"name": "A tall white plume of steam and water", "x": 0.55, "y": 0.62},
    {"name": "Tiny people standing near the plume", "x": 0.68, "y": 0.78},
    {"name": "A dark forest on a hill", "x": 0.30, "y": 0.66},
    {"name": "A black frame with rounded corners around the picture", "x": 0.06, "y": 0.50},
    {"name": "Tape along the top edge of the glass", "x": 0.42, "y": 0.05}
  ],
  "kicker": "🔎 Mystery specimen", "title": "A picture made of glass?",
  "alt": "An old glass slide with a black frame and a black-and-white photo of a geyser erupting, with tiny people nearby",
  "look": "A real glass slide, more than 100 years old. Long ago, a lamp shone through slides like this one to show a big picture on a wall. Look at the picture, its frame, and its label. Why would someone need a slide like this? That's for you to figure out.",
  "do": "Press Inspect specimen. Move the magnifying lens over the slide, then tap 3 things you notice.",
  "number": "No. 32.02-A",
  "card": ["<b>Specimen A</b>", "Made of: glass, tape, and paper", "Shows: Beehive Geyser, Yellowstone", "What was it for? <i>You decide.</i>"],
  "notice": "I notice… (one thing you see on the specimen)",
  "wonder": "I wonder… (one question you want answered by the end of the lesson)"
}

words = [
  ["🎯", "criteria", "The specific requirements a design must meet to be considered successful."],
  ["⏳", "constraint", "A limit on your design, like the time you have, the materials you can use, or the space you have."],
  ["🔍", "evidence", "Specific facts or observations that support a claim, not guesses or opinions."],
  ["📐", "model", "A drawing, diagram, or display that represents something real so it's easier to understand."],
  ["🕸️", "food web", "A diagram showing how energy passes from one organism to another in an ecosystem."],
  ["💬", "claim", "A statement about what you think is true, backed up by evidence from your research."]
]

parts = [
  {"kicker": "🎯 Part 1", "title": "What Makes a Good Presentation?",
   "html": "<p>Scientists don't just collect data. They share it. A presentation helps other people understand what you found. But not every presentation does that well.</p><p>Good presentations are built on criteria, the requirements a design must meet. Think of criteria like a recipe. Leave out an ingredient, and the dish doesn't come out right. Leave out a criterion, and your audience doesn't get the full picture of the ecosystem.</p>"},
  {"kicker": "🔍 Part 2", "title": "Evidence Is the Foundation",
   "html": "<p>Knowing something and proving it are different. Evidence is specific: a fact, an observation, or a number that backs up your claim.</p><p>\"Wolves live in Yellowstone\" is a claim. \"Gray wolves travel in packs, which lets them hunt elk much larger than one wolf could catch alone\" is evidence. One is a sentence. The other teaches you something real about the ecosystem. Your presentation also has constraints, like time and space. A visitor at a park sign may stop for only a minute or two.</p>"},
  {"kicker": "📋 Part 3", "title": "Six Things Your Presentation Must Show",
   "html": "<p>Your ecosystem presentation has six criteria: the park's name and location, its environmental conditions, three or more organisms and how they survive, a food web, one ecosystem challenge, and one conservation effort. A presentation that shows all six tells the full story of an ecosystem.</p><p>Scientists who study national parks write many reports every year. They spend a lot of time sharing what they find, because sharing science clearly is part of the job.</p>"},
  {"kicker": "🕵️ Part 4", "title": "Evidence Cards"}
]

order = {
  "mix": [2, 0, 3, 1], "hint": "Start with the scientist in the field.",
  "kicker": "🎞️ Put the scenes in order", "title": "How does park science reach visitors?",
  "look": "Four real photos show how science gets from a park to the people who visit it. They are mixed up. The dark film strip has four empty frames, from first (1) to last (4).",
  "done": "🎬 Your order is right. Now watch it as a movie!",
  "scenes": [
    {"img": "o1", "alt": "A park scientist in a winter hat working on a small recording box strapped to a tree", "text": "A scientist observes and collects data in the park.", "play": "Observe.",
     "miss": ["", "Science starts out in the park. Try frame 1.", "Science starts out in the park. Try frame 1.", "Science starts out in the park. Try frame 1."]},
    {"img": "o2", "alt": "Three scientists by a lake measuring fish and writing on a clipboard", "text": "Scientists measure and record evidence.", "play": "Collect evidence.",
     "miss": ["Observing comes first. Try a later frame.", "", "You need evidence before you can make a model. Try an earlier frame.", "You need evidence before you can make a model. Try an earlier frame."]},
    {"img": "o3", "alt": "A diagram of a food web with drawings of plants, fish, and birds joined by arrows", "text": "They make a model, like a food web.", "play": "Make a model.",
     "miss": ["The model is made from the evidence. Try a later frame.", "The model is made from the evidence. Try a later frame.", "", "Sharing comes last. Try an earlier frame."]},
    {"img": "o4", "alt": "A park ranger talking with visitors on a trail beside a mountain lake", "text": "A ranger shares it with visitors.", "play": "Share it.",
     "miss": ["This is the last step. Try frame 4.", "This is the last step. Try frame 4.", "This is the last step. Try frame 4.", ""]}
  ],
  "check": {
    "q": "Ava says, \"Pictures are just decoration on a presentation.\" What do you think?",
    "options": [
      {"t": "Ava is right. Only the words matter.", "miss": "Think about the movie. What did the food web model help people see?"},
      {"t": "A photo or a model, like a food web, can explain something faster than words.", "ok": "Yes! Scientists use models and photos because they help people understand quickly."}
    ]
  }
}

movie = {
  "model": "slide-model.svg", "modelBox": {"left": "0%", "width": "100%", "rot": 0}, "start": "0%", "bg": "lab", "counterIcon": "🔬",
  "real": "real", "realAlt": "A park ranger talking with a family of visitors outdoors",
  "stamp": "SCIENCE SHARED!", "endCap": "A real ranger sharing science with visitors.",
  "beats": [
    {"at": 0, "cap": "1 · Observe.", "model": {"top": "0%", "rot": 0, "show": "s1"}, "counter": ["Step 1"], "sfx": "whoosh"},
    {"at": 2600, "cap": "2 · Collect evidence.", "model": {"show": "s2"}, "counter": ["Step 2"]},
    {"at": 5200, "cap": "3 · Make a model.", "model": {"show": "s3"}, "counter": ["Step 3"]},
    {"at": 7800, "cap": "4 · Share it with visitors.", "model": {"show": "s4"}, "counter": ["Step 4"]},
    {"at": 10400, "cap": "The real thing.", "model": {"hide": True}, "real": True},
    {"at": 12200, "stamp": True}
  ]
}

compare = {
  "kicker": "🧪 The Visitor Test", "title": "Which one works for a visitor with two minutes?",
  "look": "Two real ways park science gets shared, each on a lit tray. Specimen A is a page from Yosemite Nature Notes, a 1947 report written by park naturalists. Specimen B is a trail sign in Glacier National Park. Under the trays are two kinds of readers: a visitor with two minutes, and a reader with lots of time.",
  "trays": [
    {"id": "A", "img": "ta", "alt": "An old printed page covered in two columns of small words, titled Broadleaved Trees of Yosemite National Park", "label": "Specimen A"},
    {"id": "B", "img": "tb", "alt": "A trail sign with a huge photo of a baby mountain goat and only a few short paragraphs", "label": "Specimen B"}
  ],
  "materials": [{"key": "quick", "label": "A visitor with 2 minutes", "img": "m_vis"}, {"key": "slow", "label": "A reader with lots of time", "img": "m_read"}],
  "ask": [
    {"q": "Which one is almost all small words?", "ans": "A", "ok": "Yes. Specimen A is the science report.", "miss": "Look closely. Which one is mostly words?"},
    {"q": "Which one has a big picture and just a few words?", "ans": "B", "ok": "Yes. Specimen B is the trail sign.", "miss": "Look again. Which one has a big photo?"}
  ],
  "press": "⏱️ Start reading",
  "testDo": "Put the visitor with 2 minutes under one tray and the reader with lots of time under the other: drag them, or tap one, then a tray. Press <b>Start reading</b>. Then swap.",
  "disclaimer": "This is a model. No real visitors are timed.",
  "results": {
    "Aquick": {"text": "The visitor reads a few lines, and time's up before they reach the big idea!", "fx": "glow"},
    "Aslow": {"text": "With lots of time, the reader studies every detail. Long, careful writing fits a science report.", "fx": "shade"},
    "Bquick": {"text": "The visitor sees the big photo, reads a few words, and remembers it!", "fx": "shade"},
    "Bslow": {"text": "The reader finishes in one minute and wishes it had more details and evidence.", "fx": "glow"}
  },
  "best": ["Aslow", "Bquick"],
  "frame": "This one ___, so it works best for ___.", "claimLead": "This one", "claimMid": "so it works best for",
  "claim": {
    "A": {"feat": ["has lots of details to read", "shows a big picture and a few words"], "featOk": 0, "eat": ["a reader with lots of time", "a visitor with 2 minutes"], "eatOk": 0},
    "B": {"feat": ["has lots of details to read", "shows a big picture and a few words"], "featOk": 1, "eat": ["a reader with lots of time", "a visitor with 2 minutes"], "eatOk": 1}
  },
  "curator": {
    "A": "<b>A science report.</b> Park naturalists wrote Yosemite Nature Notes every month, starting in 1922, with careful details other scientists could check.",
    "B": "<b>A trail sign.</b> Park signs use one big picture and a few words, because most visitors stop for only a short time."
  },
  "missFeat": "Look at your tests for {label} again. What is it made of: lots of words, or a big picture?",
  "missClaim": "Think about your tests. Which reader did it work for?",
  "done": "Both share real science. The trick is to match your design to your audience, and your visitor only has two minutes.",
  "after": {"kicker": "🎬 Behind the scenes · From report to visitors", "img": "after", "alt": "An old magazine cover with the words Yosemite Nature Notes and a drawing of bears under tall trees",
            "html": "This cover is from 1926. Yosemite's naturalists wrote Nature Notes to share what they saw in the park, and rangers turned those findings into walks and talks for visitors."}
}

wall = {
  "kicker": "🔦 The Criteria Hunt", "title": "Four exhibits, four different criteria",
  "look": "A model museum wall with four covered exhibits from three national parks. Each exhibit holds a clue and a real photo. The dial on the left shows which park the exhibit comes from.",
  "do": "First, make a prediction. Then brush the glowing exhibit: drag across it (or tap it again and again) until the photo shows.",
  "predict": {"q": "Do you predict one kind of evidence is enough for a whole presentation?",
              "options": [["no", "No, it needs different kinds"], ["yes", "Yes, one kind is enough"]], "answer": "no",
              "mine": "Your prediction: <b>{p}</b>. Let's uncover the exhibits and find out.",
              "confirm": "You predicted it needs different kinds. You were right: each exhibit shows a different criterion.",
              "change": "You predicted one kind is enough. The exhibits changed that idea: each one shows a different part of the story."},
  "sky": "sky", "skyAlt": "A wide green meadow below granite cliffs and Half Dome", "skyCap": "A meadow in Yosemite Valley",
  "unit": "Exhibit", "found": "Exhibit {n} found",
  "elevator": ["Exhibit hall", "Everglades", "Yellowstone", "Everglades", "Yosemite"],
  "line": ["THE PARK", "PEOPLE HELP"],
  "lockTag": "🔒 Open the exhibit above first", "locked": "Open the exhibit above first. We go one exhibit at a time.",
  "first": "Brush the glowing first exhibit. Drag across it (or tap it again and again).", "next": "Keep going. Brush Exhibit {n}.",
  "endTitle": "All 4 exhibits found",
  "endText": "Look at the wall. Each exhibit shows a different criterion, and together they tell the whole story.",
  "rule": "<b>A full presentation needs different kinds of evidence.</b> Conditions, a food web, a challenge, and a conservation effort each show a different part of the ecosystem's story.",
  "choices": ["🌡️ Environmental conditions", "🕸️ Food web", "⚠️ Ecosystem challenge", "🛡️ Conservation effort"],
  "layers": [
    {"name": "Exhibit 1 · Everglades, Florida", "rock": "water1", "img": "l1", "alt": "Dark storm clouds and rain over a wide, flat marsh",
     "ask": "Look at Exhibit 1. Read the clue AND the photo. Which criterion does it show?",
     "clue": "Most of the Everglades' rain falls from May to October, the wet season. Then shallow water spreads across the sawgrass.",
     "ans": 0, "ok": "Yes! Rain and shallow water are environmental conditions.", "tag": "🌡️ Everglades · conditions",
     "miss": {"1": "Not quite. Does the clue say who eats whom?", "2": "Close! But rain is normal here. Is it a problem, or the weather?", "3": "Not yet. Are people doing something in this clue?"},
     "env": "e1", "envAlt": "A wide river of grass and water stretching to the sky", "envCap": "The River of Grass · Everglades National Park"},
    {"name": "Exhibit 2 · Yellowstone, Wyoming", "rock": "limestone", "img": "l2", "alt": "Elk standing in a winding river between snowy banks",
     "ask": "Look at Exhibit 2. Read the clue AND the photo. Which criterion does it show?",
     "clue": "Gray wolves eat elk. Elk eat grasses and willows. The grasses get their energy from the Sun.",
     "ans": 1, "ok": "Yes! Who eats whom, starting with the Sun, is a food web.", "tag": "🕸️ Yellowstone · food web",
     "miss": {"0": "Not quite. Is the clue about the weather?", "2": "Close! Wolves hunt elk, but read the clue: it follows the energy.", "3": "Not yet. Are people doing something in this clue?"},
     "env": "e2", "envAlt": "A gray wolf wearing a radio collar, lying on snow", "envCap": "A gray wolf with a radio collar, so scientists can track it"},
    {"name": "Exhibit 3 · Everglades, Florida", "rock": "snowcap", "img": "l3", "alt": "A large Burmese python coiled in shallow water",
     "ask": "Look at Exhibit 3. Read the clue AND the photo. Which criterion does it show?",
     "clue": "Burmese pythons don't belong in Florida. In parts of the Everglades, scientists counted far fewer raccoons and opossums after pythons spread.",
     "ans": 2, "ok": "Yes! An invasive snake is a real problem for the ecosystem.", "tag": "⚠️ Everglades · challenge",
     "miss": {"0": "Not quite. Is this about the weather?", "1": "Close! Pythons do eat animals, but read the clue: is this a healthy part of the park?", "3": "Not yet. Does the clue say what people are doing about it?"},
     "env": "e3", "envAlt": "A small newborn python on the ground", "envCap": "A newborn python found in the Everglades"},
    {"name": "Exhibit 4 · Yosemite, California", "rock": "haze", "img": "l4", "alt": "A peregrine falcon with a sharp hooked beak",
     "ask": "Look at Exhibit 4. Read the clue AND the photo. Which criterion does it show?",
     "clue": "Each spring, Yosemite closes some climbing routes so peregrine falcons can raise their chicks on the cliffs in peace.",
     "ans": 3, "ok": "Yes! People protecting the falcons is a conservation effort.", "tag": "🛡️ Yosemite · conservation",
     "miss": {"0": "Not quite. Is this about the weather?", "1": "Not yet. Does the clue say who eats whom?", "2": "Close! But read the clue: what are people doing to help?"},
     "env": "e4", "envAlt": "The giant granite cliff El Capitan above green trees", "envCap": "El Capitan, where peregrine falcons nest · Yosemite National Park"}
  ],
  "mix": {
    "q": "Leo says, \"Any fact about the park counts as evidence for my presentation.\" What do you think?",
    "options": [
      {"t": "Leo is right. Every fact is evidence.", "miss": "Think about it: does the fact support what your slide is trying to show?"},
      {"t": "Evidence has to support your claim. \"The gift shop sells hats\" is a fact, but it isn't evidence about the ecosystem.", "ok": "Yes! Good evidence is specific, AND it supports your claim."}
    ]
  }
}

wow = {"kicker": "🎬 Director's cut", "title": "A Museum on the Trail",
  "img": "wow", "alt": "A dirt path through tall pines leading to a stone and log building",
  "caption": "The trail to the Norris Geyser Basin Museum · Yellowstone National Park",
  "html": "<p style=\"margin:0 0 8px\">In 1929 and 1930, Yellowstone built small \"trailside museums\" right beside its trails, so visitors could learn about the geysers in just a few minutes.</p><p style=\"margin:0\">The Norris museum is still open today, almost 100 years later, and rangers still share science there.</p>",
  "inset": "inset", "insetCap": "The museum's front and open walkway."}

keyIdea = "A science presentation shares real evidence so other people can understand it. It must meet its criteria (for our parks: location, conditions, organisms, a food web, a challenge, and a conservation effort) and fit its constraints, like time and space. Strong evidence is specific, and models like food webs and photos help people understand quickly."

CRIT = ["🌡️ Environmental conditions", "🐾 Organisms and survival", "🕸️ Food web", "🛡️ Challenge or conservation"]
SHORT = ["environmental conditions", "organisms and survival", "the food web", "challenge or conservation"]
SOL = [["strong", "💪 Strong evidence: it's specific"], ["weak", "🤔 Weak: it's too vague"]]


def card(id_, img, alt, clues, orgAns, orgMiss, sentence, envAns, envMiss, envImg, envAlt, envCap, reveal, bts):
    return {"id": id_, "img": img, "alt": alt, "clues": clues, "org": CRIT, "orgAns": orgAns, "orgShort": SHORT[orgAns], "orgMiss": orgMiss,
            "predict": {"q": "A slide says: \"" + sentence + "\" Is that strong evidence?", "options": SOL},
            "env": dict(SOL)[envAns].split(" ", 1)[1].split(":")[0], "envAns": envAns, "envMiss": envMiss, "envImg": envImg, "envAlt": envAlt, "envCap": envCap, "reveal": reveal, "rebuildEnv": envAns, "bts": bts}


det = {
  "look": "Five real photos from national parks. Each card goes with a sentence a student wants to put on a slide. Under the cards is an evidence chart, a table that holds what you figure out.",
  "do": "Pick 3 cards, one at a time. Tap what you see, then name the criterion it fits. Decide if the slide's sentence is strong evidence, and see the answer.",
  "noun": "Card", "need": 3, "inferQ": "Which criterion does this card fit?", "inferDone": "It fits", "chartSo": "so it fits",
  "predict": {"q": "Is the slide's sentence strong evidence?", "options": SOL},
  "kicker": "The evidence check", "enough": "You already checked 3 cards. Nice work, science communicator!",
  "cols": ["Card", "What I see", "Criterion", "Its sentence", "My evidence"],
  "write": {"label": "Card __ shows ___. It fits ___, and its sentence is strong / weak evidence because ___.", "starter": "Start with: \"Card __ shows…\"", "min": 15,
            "chips": [["crit", "Names a criterion"], ["sw", "Says strong or weak"], ["because", "Gives a reason (because, so)"]]},
  "items": [
    card("A", "d1", "An alligator floating in dark green water",
         [{"t": "An alligator in shallow water", "ok": True}, {"t": "A snake in a tree", "miss": "Look again. Does it have legs?"}, {"t": "A bird on a branch", "miss": "Look again. Does it have feathers?"}],
         1, "This card is about one animal and how it survives. Try again.",
         "Alligators dig gator holes that hold water in the dry season, so fish and birds can survive there.",
         "strong", "This one names a real behavior and gives a reason with \"so.\" That's specific evidence.",
         "d1h", "A round pond of water in a marsh, seen from the air", "A gator hole seen from the air · Everglades National Park",
         "Strong! It names the organism, tells what it does, and explains why it matters.",
         "In the dry season, a gator hole can be one of the only wet spots for a long way."),
    card("B", "d2", "A rocky mountain peak with patches of snow under a blue sky",
         [{"t": "A snowy mountain peak", "ok": True}, {"t": "A sandy beach", "miss": "Look again. Is there water and sand?"}, {"t": "A green swamp", "miss": "Look again. Is it wet and green?"}],
         0, "This card is about the land and the weather. Try again.",
         "Yosemite has weather.",
         "weak", "Every place has weather. Which weather? How much? Specific evidence gives details.",
         "d2h", "Snow covering the trees and meadow of Yosemite Valley", "Yosemite Valley in winter",
         "Too vague! Stronger: Yosemite Valley is about 4,000 feet high, but Mount Lyell is over 13,000 feet, so the high mountains stay snowy much longer.",
         "Mount Lyell is the highest mountain in Yosemite."),
    card("C", "d3", "Many bison and a few pronghorn grazing in a wide green valley",
         [{"t": "Animals grazing on grass in a valley", "ok": True}, {"t": "Fish in a river", "miss": "Look again. Are they in water?"}, {"t": "A forest fire", "miss": "Look again. Is there smoke?"}],
         2, "This card is about who eats what. Try again.",
         "Things eat other things in Yellowstone.",
         "weak", "\"Things eat other things\" doesn't name a single organism. Specific evidence names who eats whom.",
         "d3h", "A gray wolf wearing a radio collar, lying on snow", "A gray wolf with a radio collar",
         "Too vague! Stronger: In Yellowstone, grasses feed elk and bison, and gray wolves hunt elk and bison.",
         "Bison and pronghorn both eat the grasses of Lamar Valley in Yellowstone."),
    card("D", "d4", "A large snake with a brown and tan pattern, coiled in water",
         [{"t": "A large snake with a pattern", "ok": True}, {"t": "An alligator", "miss": "Look again. Does it have legs?"}, {"t": "A tree root", "miss": "Look again. Is it alive?"}],
         3, "This card is about a problem in the park. Try again.",
         "After Burmese pythons spread in the Everglades, scientists counted far fewer raccoons, opossums, and rabbits.",
         "strong", "This one names the problem, the organisms, and what scientists counted. That's specific evidence.",
         "d4h", "A raccoon looking at the camera", "A raccoon, one of the animals pythons eat",
         "Strong! It names the problem, the organisms, and what scientists measured.",
         "Pythons are not from Florida. People let pet snakes go, and the snakes spread."),
    card("E", "d5", "A firefighter walking through smoke from a low fire in a forest",
         [{"t": "A small, planned fire in a forest", "ok": True}, {"t": "A snowy mountain", "miss": "Look again. Is there snow?"}, {"t": "A flooded marsh", "miss": "Look again. Is there water?"}],
         3, "This card is about what people do to protect the forest. Try again.",
         "Rangers set careful, planned fires in giant sequoia forests, because the heat opens sequoia cones and clears the ground for seedlings.",
         "strong", "This one tells what people do and explains why with \"because.\" That's specific evidence.",
         "d5h", "A giant sequoia trunk reaching up into a blue sky", "A giant sequoia in the Mariposa Grove · Yosemite National Park",
         "Strong! It tells what people do and explains why, with \"because.\"",
         "This planned fire was in Sequoia and Kings Canyon National Parks, south of Yosemite.")
  ]
}

rebuild = {"title": "Sort the slide sentences", "missPrefix": "Hmm. Look at your card again. ", "kicker": "🗂️ Strong or vague?", "whyStart": "I chose this because the sentence…",
  "envs": [
    {"key": "strong", "name": "💪 Strong evidence", "img": "d1h", "cap": "Specific details…"},
    {"key": "weak", "name": "🤔 Too vague", "img": "d2h", "cap": "Needs more details…"}
  ],
  "life": [
    {"name": "🐊 Gator holes save fish and birds", "img": "d1", "env": "strong", "miss": "It names the animal, what it does, and why."},
    {"name": "🏔️ \"Yosemite has weather.\"", "img": "d2", "env": "weak", "miss": "Every place has weather. Which weather?"},
    {"name": "🦬 \"Things eat other things.\"", "img": "d3", "env": "weak", "miss": "It doesn't name a single organism."},
    {"name": "🐍 Fewer raccoons after pythons", "img": "d4", "env": "strong", "miss": "It names the problem and what scientists counted."},
    {"name": "🔥 Planned fires for sequoias", "img": "d5", "env": "strong", "miss": "It tells what people do, with \"because.\""}
  ]}

quiz = [
  {"q": "What is a design criterion?", "options": [
    {"t": "A list of materials you are allowed to use", "miss": "A criterion is about what your design must achieve, not what it looks like or what materials you use. Think: what must my presentation DO to be complete?"},
    {"t": "A specific requirement your design must meet to be successful", "ok": "🎯 Exactly. A criterion is a requirement: something your design must do or include to be complete and successful."},
    {"t": "A description of what your design looks like", "miss": "A criterion is about what your design must achieve, not what it looks like or what materials you use. Think: what must my presentation DO to be complete?"}]},
  {"q": "Maria has 30 minutes to build and can only use paper and markers. What do scientists call those limits?", "options": [
    {"t": "Criteria", "miss": "Criteria are what the design must do. Constraints are what limit the design: time, materials, and space. Maria's 30 minutes and markers are limits."},
    {"t": "Evidence", "miss": "Criteria are what the design must do. Constraints are what limit the design: time, materials, and space. Maria's 30 minutes and markers are limits."},
    {"t": "Constraints", "ok": "⏳ That's it. Time and materials are constraints, limits that affect what your design can realistically be."}]},
  {"q": "Which of these is the strongest piece of scientific evidence for an ecosystem presentation?", "options": [
    {"t": "\"Wolves are important animals in Yellowstone.\"", "miss": "That one is general. Real evidence has a detail that helps you understand something. Look for the option that explains a behavior."},
    {"t": "\"Yellowstone has a lot of interesting wildlife.\"", "miss": "That one is general. Real evidence has a detail that helps you understand something. Look for the option that explains a behavior."},
    {"t": "\"Gray wolves travel in packs, which lets them hunt elk that are much larger than a single wolf could tackle alone.\"", "ok": "🔍 Strong evidence is specific. It shows exactly how something works, not just that it exists."}]}
]

assign = {
  "partA": {"title": "Plan your presentation", "do": "Answer each one in a sentence. Your answers help you start your slides in Part C.", "items": [
    {"n": 1, "q": "Which park will you present? Where is it?", "type": "text", "min": 5, "chips": [["park", "Names a park"], ["where", "Says where it is (a state)"]]},
    {"n": 2, "q": "What is your strongest piece of evidence? Write the whole fact in one sentence.", "type": "text", "min": 8, "chips": [["spec", "Has a number, a name, or a because"]]},
    {"n": 3, "q": "Name one constraint on your presentation. How will it change what you include?", "type": "text", "min": 8, "chips": [["con", "Names a limit (time, words, space)"]]}
  ]},
  "partB": {"title": "Short answer", "do": "Answer in complete sentences.", "items": [
    {"n": 1, "q": "What is the difference between a criterion and a constraint? Give one example of each from your own presentation.", "type": "text", "min": 15, "chips": [["crit2", "Uses the word criterion or criteria"], ["con", "Names a limit (time, words, space)"]]},
    {"n": 2, "q": "How does including a conservation effort make your presentation stronger? Why does that information matter to the audience?", "type": "text", "min": 12, "chips": [["cons", "Names a way people protect the park"], ["because", "Gives a reason (because, so)"]]}
  ]},
  "partC": {"kicker": "🎤 Part C", "title": "Build your slides in the Park Slide Studio", "map": "Part C · build your slides",
            "do": "Pick your park. Build 6 slides, one for each criterion. Practice with the 2-minute timer. Then make your video (or download your slides) and upload the file to Canvas.", "labels": []},
  "turnIn": "In Part C, press <b>Make my video</b> (or <b>Download my slides</b>) and upload that file to Canvas. Then copy your answers here and paste them into the Canvas assignment too. (The slides file already has your Part A and Part B answers on its last slide.)",
  "checklist": [
    {"k": "det", "t": "My evidence chart has 3 cards and my explanation.", "req": {"det": 3, "text": {"in-det": 15}}},
    {"k": "a", "t": "Part A: my plan, all three answered.", "req": {"text": {"in-a1": 5, "in-a2": 8, "in-a3": 8}}},
    {"k": "b", "t": "Part B: questions 1 and 2.", "req": {"text": {"in-b1": 15, "in-b2": 12}}},
    {"k": "c", "t": "Part C: all 6 slides meet the criteria, and I made my video or downloaded my slides.", "req": {"studio": True}}
  ]
}


# Field Notes (Bethany, 21 Nov 2026): 2-3 checked facts per park per slide, so no one has to search the web. Sources: nps.gov park pages.
NOTES = {
  "ever": {
    "place": ["Everglades National Park is at the southern tip of Florida.", "It became a national park in 1947.", "It is the largest subtropical wilderness in the United States, about 1.5 million acres."],
    "cond": ["The wet season is May to November. Most of the year's rain, nearly 60 inches, falls then.", "The dry season is December to April, and water dries up in many places.", "Water moves slowly south through the sawgrass, so people call it a River of Grass."],
    "orgs": ["Alligators dig gator holes that hold water in the dry season, so fish and birds survive there.", "Roseate spoonbills sweep their flat bills through shallow water to catch food.", "The Everglades is the only place where alligators and crocodiles live side by side."],
    "web": ["Algae mats called periphyton feed snails and small fish.", "Snail kites eat almost nothing but apple snails.", "Alligators are top predators: they eat fish, turtles, birds, and small mammals."],
    "chal": ["Burmese pythons don't belong in Florida. Where they spread, scientists counted far fewer raccoons, opossums, and rabbits.", "Roads and canals changed how water flows, so some parts of the park get too little water."],
    "cons": ["In 2013, a one-mile bridge was built on the Tamiami Trail road so more water can flow into the park.", "Filter marshes clean water from farms before it reaches the Everglades.", "Scientists and trained hunters remove pythons to protect native animals."]},
  "yose": {
    "place": ["Yosemite National Park is in the Sierra Nevada mountains of California.", "It became a national park in 1890.", "Yosemite Falls drops 2,425 feet, one of the tallest waterfalls in North America."],
    "cond": ["Yosemite Valley is about 4,000 feet high, but Mount Lyell is over 13,000 feet.", "Most rain and snow falls in winter, and summers are dry.", "Melting snow makes the waterfalls biggest in late spring."],
    "orgs": ["Giant sequoias can live more than 2,000 years. Their thick bark protects them from fire.", "Many mule deer move to lower places in winter, where it's easier to find food.", "Yosemite toads live in high mountain meadows. They are a threatened species."],
    "web": ["Mule deer eat grasses, shrubs, and acorns.", "Mountain lions mostly hunt deer.", "Acorns from black oaks feed squirrels, deer, bears, and woodpeckers."],
    "chal": ["Bears that get human food can become dangerous, and people's food can harm them.", "Long droughts can make wildfires bigger. The 2013 Rim Fire burned part of the park."],
    "cons": ["Each spring, some climbing routes close so peregrine falcons can raise chicks on the cliffs.", "Visitors must store food in bear-proof lockers so bears stay wild.", "Rangers set careful, planned fires to keep forests and sequoia groves healthy."]},
  "yell": {
    "place": ["Yellowstone became the first national park in the world in 1872.", "It is mostly in Wyoming, with small parts in Montana and Idaho.", "It has more than 10,000 hot springs, mud pots, and geysers, including Old Faithful."],
    "cond": ["Much of the park is about 8,000 feet high.", "Winters are long, and temperatures often drop below 0°F.", "Hot water underground heats the geysers and hot springs, even in winter."],
    "orgs": ["Bison swing their big heads to push snow off the grass they eat.", "Gray wolves hunt in packs, so they can catch elk bigger than one wolf.", "Grizzly bears sleep in dens through the winter."],
    "web": ["Elk and bison eat grasses. Elk and beavers eat willows.", "Wolves eat mostly elk, especially in winter.", "Yellowstone cutthroat trout are food for bears, otters, and eagles."],
    "chal": ["Lake trout don't belong in Yellowstone Lake. Found there in 1994, they eat the native cutthroat trout.", "Before 1995, wolves had been gone for about 70 years, and elk ate many young willows."],
    "cons": ["In 1995, gray wolves were brought back to Yellowstone.", "Park crews use nets to remove millions of lake trout and protect the cutthroat trout.", "Visitors must stay at least 100 yards from bears and wolves."]}
}
# ---------- the Park Slide Studio ----------
def P(img, cap, tag): return {"img": "pb_" + img, "thumb": "pt_" + img, "cap": cap, "tag": tag}
studio = {
  "words": 30, "minWords": 5, "minutes": 2, "deckKicker": "A national park ecosystem",
  "video": "assets/video/g3sci-32-02-studio-howto", "videoLen": "2-minute video",
  "pickLead": "Step 1: Pick the park you'll present. Each park has its own bank of real photos.",
  "webKey": "Arrows show where the energy goes: from the Sun, to a plant, to the animal that eats it.",
  "webSteps": [{"label": "1 · A plant (it uses sunlight)", "role": "p"}, {"label": "2 · An animal that eats that plant", "role": "h"}, {"label": "3 · An animal that eats that animal", "role": "c"}],
  "steps": ["Pick a park", "Build 6 slides", "Practice", "Make my video"],
  "notesLead": "📒 Field Notes: facts about {park} for this slide", "notesTip": "Pick a fact, then write it in your own words. You can use what you learned in 32.01 too.",
  "intro": {
    "title": "New to presentations? Start here.",
    "points": ["A <b>presentation</b> is a few slides you show while you talk.", "Each slide has <b>one big idea</b>, <b>one picture</b>, and <b>a few words</b>.", "Your visitor has only <b>2 minutes</b>, so every word has to count.", "You talk about the slide. The slide doesn't say everything."],
    "img": "ex_sal", "imgCap": "A black-chinned red salamander, Great Smoky Mountains",
    "good": {"kicker": "🐾 Key organisms & survival", "text": "Black-chinned red salamanders breathe through their wet skin, so they need cool, rainy forests like the Smokies.",
             "why": "✅ Strong slide: one idea, a real photo, 18 words, and a specific fact with \"so.\""},
    "bad": {"kicker": "🐾 Key organisms & survival", "text": "There are lots of animals in the Great Smoky Mountains and they are really cool and interesting and I like them a lot. There are bears and birds and deer and salamanders and they all live there in the forest and some of them are big and some are small and they eat things and they live in the trees and on the ground and in the water too.",
            "why": "❌ Weak slide: 70 words, no picture, and no specific evidence. A visitor runs out of time."},
    "go": "Got it! Pick my park →"
  },
  "tips": {"title": "🎤 Present like a ranger", "items": ["Look at your listener, not just the screen.", "Point to your picture when you talk about it.", "Say one more thing than the slide says.", "Watch the timer: about 20 seconds for each slide."],
           "who": "Practice out loud, by yourself or with someone at home.", "go": "▶ Start presenting"},
  "criteria": [
    {"k": "place", "icon": "🏞️", "name": "Park name & location", "short": "Park & place", "ask": "Which park is it, and where is it?", "hint": "Name your park and the state it is in.", "starter": "{name} is in {state}. It protects "},
    {"k": "cond", "icon": "🌡️", "name": "Environmental conditions", "short": "Conditions", "ask": "What are the weather, land, and water like?", "hint": "Tell about the weather, land, or water. Use a number if you can.", "starter": "In {short}, the weather is "},
    {"k": "orgs", "icon": "🐾", "name": "Key organisms & survival", "short": "Organisms", "ask": "Name 3 organisms and how they survive.", "hint": "Name 3 living things and one way each survives.", "starter": "Three organisms that live here are "},
    {"k": "web", "icon": "🕸️", "name": "Food web", "short": "Food web", "ask": "What does your food web show?", "hint": "Tell what your arrows show.", "starter": "My food web shows that "},
    {"k": "chal", "icon": "⚠️", "name": "Ecosystem challenge", "short": "Challenge", "ask": "What real problem does the ecosystem face?", "hint": "Name one real problem and what it hurts.", "starter": "One problem in {short} is "},
    {"k": "cons", "icon": "🛡️", "name": "Conservation effort", "short": "Protecting it", "ask": "What are people doing to protect it?", "hint": "Tell what people do and why it helps.", "starter": "To protect the park, people "}
  ],
  "teacher": [{"id": "in-a1", "label": "Part A 1 · My park and where it is"}, {"id": "in-a2", "label": "Part A 2 · My strongest evidence"}, {"id": "in-a3", "label": "Part A 3 · A constraint and how it changed my plan"},
              {"id": "in-b1", "label": "Part B 1 · Criterion vs. constraint"}, {"id": "in-b2", "label": "Part B 2 · Why a conservation effort makes it stronger"}],
  "parks": [
    {"k": "ever", "name": "Everglades National Park", "short": "the Everglades", "state": "Florida", "color": "#2D6A4F", "cover": "pb_g_river", "coverAlt": "A wide river of grass and water under a big sky",
     "names": ["alligator", "crocodile", "spoonbill", "wood stork", "heron", "egret", "anhinga", "snail kite", "kite", "apple snail", "snail", "panther", "deer", "raccoon", "rabbit", "python", "sawgrass", "algae", "periphyton", "mangrove", "manatee", "fish", "turtle", "frog", "bobcat", "otter", "ibis", "opossum", "plants"],
     "web": {"orgs": [{"n": "Algae", "e": "🟢", "role": "p"}, {"n": "Marsh plants", "e": "🌿", "role": "p"}, {"n": "Apple snail", "e": "🐌", "role": "h"}, {"n": "Marsh rabbit", "e": "🐇", "role": "h"}, {"n": "White-tailed deer", "e": "🦌", "role": "h"},
                      {"n": "Snail kite", "e": "🦅", "role": "c"}, {"n": "Alligator", "e": "🐊", "role": "c"}, {"n": "Florida panther", "e": "🐆", "role": "c"}],
             "edges": [["Algae", "Apple snail"], ["Marsh plants", "Marsh rabbit"], ["Marsh plants", "White-tailed deer"], ["Apple snail", "Snail kite"], ["Marsh rabbit", "Alligator"], ["Marsh rabbit", "Florida panther"], ["White-tailed deer", "Florida panther"], ["White-tailed deer", "Alligator"]]},
     "photos": [P("g_river", "The River of Grass, Everglades National Park", "place"), P("g_prairie", "Sawgrass prairie, Everglades National Park", "place"),
                P("g_storm", "A summer thunderstorm, Everglades National Park", "cond"), P("g_peri", "Periphyton, a mat of algae, in Everglades water", "cond"),
                P("g_gator", "An American alligator on the Anhinga Trail", "orgs"), P("g_spoon", "A roseate spoonbill, Everglades National Park", "orgs"),
                P("g_wading", "Wading birds feeding at Shark Valley", "orgs"), P("g_panther", "A Florida panther", "orgs"), P("g_deer", "A white-tailed deer in sawgrass, Everglades", "orgs"),
                P("g_py", "A Burmese python in the Everglades", "chal"), P("g_bridge", "Building the Tamiami Trail bridge (2011) so water can flow", "cons"),
                P("g_sta", "Filter marshes that clean water on its way to the Everglades", "cons")]},
    {"k": "yose", "name": "Yosemite National Park", "short": "Yosemite", "state": "California", "color": "#4A6FA5", "cover": "pb_yfalls", "coverAlt": "A tall waterfall pouring over granite cliffs",
     "names": ["deer", "mule deer", "black bear", "bear", "mountain lion", "bobcat", "coyote", "peregrine falcon", "falcon", "toad", "salamander", "sequoia", "oak", "acorn", "squirrel", "chipmunk", "woodpecker", "jay", "trout", "pika", "marmot", "bighorn sheep", "pine", "grass", "grasses", "owl", "plants"],
     "web": {"orgs": [{"n": "Meadow grasses", "e": "🌾", "role": "p"}, {"n": "Black oak acorns", "e": "🌰", "role": "p"}, {"n": "Mule deer", "e": "🦌", "role": "h"}, {"n": "Gray squirrel", "e": "🐿️", "role": "h"},
                      {"n": "Mountain lion", "e": "🐆", "role": "c"}, {"n": "Bobcat", "e": "🐈", "role": "c"}],
             "edges": [["Meadow grasses", "Mule deer"], ["Black oak acorns", "Mule deer"], ["Black oak acorns", "Gray squirrel"], ["Mule deer", "Mountain lion"], ["Gray squirrel", "Bobcat"]]},
     "photos": [P("yfalls", "Upper and Lower Yosemite Falls", "place"), P("hdome", "Half Dome at sunset, Yosemite", "place"),
                P("ysky", "A meadow in Yosemite Valley", "cond"), P("ywinter", "Yosemite Valley in winter snow", "cond"), P("lyell", "Mount Lyell, Yosemite's highest peak", "cond"),
                P("ybear", "A black bear in Yosemite", "orgs"), P("toad", "A pair of Yosemite toads", "orgs"), P("sal2", "A Mount Lyell salamander", "orgs"),
                P("peri", "A peregrine falcon", "orgs"), P("oak", "A California black oak tree", "orgs"),
                P("mfire", "The Meadow Fire near Half Dome, 2014", "chal"), P("elcap2", "El Capitan, where peregrine falcons nest", "cons")]},
    {"k": "yell", "name": "Yellowstone National Park", "short": "Yellowstone", "state": "Wyoming", "color": "#9C5B2E", "cover": "pb_prism", "coverAlt": "A huge hot spring with bright blue water and orange edges",
     "names": ["bison", "elk", "wolf", "wolves", "grizzly", "bear", "pronghorn", "beaver", "trout", "cutthroat", "lake trout", "eagle", "raven", "willow", "willows", "aspen", "grass", "grasses", "coyote", "fox", "otter", "moose", "pine", "plants"],
     "web": {"orgs": [{"n": "Grasses", "e": "🌾", "role": "p"}, {"n": "Willows", "e": "🌿", "role": "p"}, {"n": "Elk", "e": "🦌", "role": "h"}, {"n": "Bison", "e": "🦬", "role": "h"}, {"n": "Beaver", "e": "🦫", "role": "h"},
                      {"n": "Gray wolf", "e": "🐺", "role": "c"}, {"n": "Grizzly bear", "e": "🐻", "role": "c"}],
             "edges": [["Grasses", "Elk"], ["Grasses", "Bison"], ["Willows", "Elk"], ["Willows", "Beaver"], ["Elk", "Gray wolf"], ["Bison", "Gray wolf"], ["Elk", "Grizzly bear"], ["Beaver", "Gray wolf"]]},
     "photos": [P("prism", "Grand Prismatic Spring, Yellowstone", "place"), P("lamar", "Bison and pronghorn in Lamar Valley, Yellowstone", "place"),
                P("lfalls", "Lower Falls of the Yellowstone in winter", "cond"), P("g_bison", "Bison in deep snow, Yellowstone", "cond"),
                P("g_elk", "Elk in the Gibbon River in winter, Yellowstone", "orgs"), P("wolfsnow", "A gray wolf with a radio collar", "orgs"),
                P("grizz", "A grizzly bear in Yellowstone", "orgs"), P("beaver", "A beaver on the Yellowstone River", "orgs"), P("cutt", "A Yellowstone cutthroat trout", "orgs"),
                P("ltrout", "Lake trout, a fish that doesn't belong, in Shoshone Lake", "chal"), P("fire88", "A wildfire above the Snake River, Yellowstone", "chal"),
                P("g_wolfrel", "1995: a wolf arrives back in Yellowstone", "cons")]}
  ]
}

premiere = {"title": "Premiere my presentation", "thinkLabel": "It fits", "director": "JUNIOR SCIENCE COMMUNICATOR", "storyKicker": "My evidence check",
  "frames": [
    {"k": "formation", "label": "Field to Slide", "img": "o4", "cap": "Field to Slide: observe, collect, model, share."},
    {"k": "compare", "label": "The Visitor Test", "img": "tb", "cap": "The Visitor Test: match the design to the audience."},
    {"k": "wall", "label": "The Criteria Hunt", "img": "l2", "cap": "The Criteria Hunt: each criterion tells part of the story."},
    {"k": "det", "label": "Evidence cards", "img": "d1", "cap": "Evidence cards: strong evidence is specific."}]}

nxt = {"title": "Coming up next: 33.01", "text": "How Is Everything Connected? Next time, you'll connect the big ideas from the whole year of science."}

chips = {
  "part": {"any": ["glass", "frame", "label", "number", "geyser", "steam", "water", "people", "trees", "forest", "tape", "black", "white", "picture", "photo", "corners", "round", "2425"]},
  "ask": {"re": "\\?|\\b(why|how|what|when|where|who|which|does|do|is|are|can|did|will)\\b"},
  "crit": {"any": ["conditions", "condition", "organism", "organisms", "survival", "food web", "challenge", "conservation", "location", "weather"]},
  "sw": {"re": "\\b(strong|weak|vague)\\b"},
  "because": {"re": "\\b(because|since|so)\\b"},
  "park": {"any": ["everglades", "yosemite", "yellowstone", "park"]},
  "where": {"any": ["florida", "california", "wyoming", "montana", "idaho", "state"]},
  "spec": {"re": "\\d|\\b(because|so|which|when)\\b|\\b(alligator|wolf|wolves|elk|bison|panther|python|bear|falcon|sequoia|snail|kite|deer|beaver|trout|spoonbill)"},
  "con": {"any": ["time", "minutes", "minute", "words", "word", "space", "materials", "limit", "slides", "slide", "2"]},
  "crit2": {"any": ["criterion", "criteria"]},
  "cons": {"any": ["protect", "protects", "protecting", "closes", "close", "restore", "bridge", "remove", "removing", "fire", "fires", "save", "law", "rangers", "clean"]}
}

L = {"id": "g3sci-32-02", "lesson": "32.02", "title": "Build a Park Ecosystem Presentation", "emoji": "🎤",
  "details": ["📅 Q4 · Unit 11 · National Park Capstone", "📖 Week 32 · Lesson 32.02", "🌎 CPALMS SC.3.N.1.4, SC.3.N.3.2", "⏱ About 45 minutes"],
  "icans": ["name the criteria and constraints for an ecosystem presentation.", "use scientific evidence to plan what goes in my presentation.", "build a presentation that shows how organisms, habitat, and conservation connect."],
  "opti": {"warm": "Our film starts with park rangers from 100 years ago. First, inspect a mystery made of glass.",
           "lesson": "Today you're a science communicator. Follow park science to visitors, run the Visitor Test, then hunt for the criteria.",
           "check": "Three quick questions. It's not graded. It's just for you, so give each one your best try.",
           "assign": "Time to build! Plan in Part A, then make your real slides in the Park Slide Studio and present them."},
  "film": film, "scientist": "science communicator", "specimen": specimen, "words": words, "parts": parts, "order": order, "movie": movie,
  "compare": compare, "wall": wall, "wow": wow, "keyIdea": keyIdea, "det": det, "rebuild": rebuild, "quiz": quiz, "assign": assign, "studio": studio,
  "premiere": premiere, "next": nxt, "chips": chips, "creditAlias": {},
  "creditsExtra": ["Music: String Quartet No. 12 \"American,\" II. Lento (Antonín Dvořák), Musopen String Quartet, public domain recording (via Wikimedia Commons).",
                   "Park Slide Studio: every photo in the photo bank is public domain. Field Notes facts come from National Park Service park pages (nps.gov). The \"Download my slides\" file is made with PptxGenJS (MIT license).",
                   "Opti the owl: Optima Academy. Sound effects are made by the page. The science-sharing movie, the Visitor Test, and the Criteria Hunt are models; every place photo is real. The planned-fire photo is from Sequoia and Kings Canyon National Parks."]}

for pk in studio['parks']: pk['notes'] = NOTES[pk['k']]
json.dump(L, open(f'{D}/lesson.json', 'w'), indent=1, ensure_ascii=False)

how = {
  "how-32-02-specimen": {"page": specimen["do"], "say": "Press Inspect specimen. Move the magnifying lens over the slide, then tap three things you notice."},
  "how-32-02-compare": {"page": "Put the visitor with 2 minutes under one tray and the reader with lots of time under the other: drag them, or tap one, then a tray. Press Start reading. Then swap.",
                        "say": "Put the visitor with two minutes under one tray and the reader with lots of time under the other: drag them, or tap one, then a tray. Press Start reading. Then swap."},
  "how-32-02-wall": {"page": wall["do"], "say": wall["do"].replace("brush the glowing exhibit", "brush the glowing exhibit")},
  "how-32-02-det": {"page": det["do"], "say": "Pick three cards, one at a time. Tap what you see, then name the criterion it fits. Decide if the slide's sentence is strong evidence, and see the answer."},
  "how-32-02-partc": {"page": assign["partC"]["do"], "say": "Pick your park. Build six slides, one for each criterion. Practice with the two-minute timer. Then make your video, or download your slides, and upload the file to Canvas."}
}
json.dump(how, open(f'{D}/how-lines.json', 'w'), indent=1, ensure_ascii=False)

# the Slide Studio how-to video narration (voiced later; the tour is timed to these lines, see studio-video.json)
VIDEO = json.load(open(f'{D}/studio-video.json')) if os.path.exists(f'{D}/studio-video.json') else {"lines": []}
scripts = {c["voice"]: c["text"] for c in film["captions"]}
scripts.update({"32-02-welcome": L["opti"]["warm"], "32-02-lesson": L["opti"]["lesson"], "32-02-check": L["opti"]["check"], "32-02-assign": L["opti"]["assign"]})
for k, v in how.items(): scripts[k] = v["say"]
for w in words: scripts["word-" + w[1].replace(" ", "-")] = w[1]
for i, ln in enumerate(VIDEO["lines"]): scripts[f"studio-howto-{i+1:02d}"] = ln["say"]
json.dump(scripts, open(f'{D}/scripts.json', 'w'), indent=1, ensure_ascii=False)

meta = json.load(open(f'{D}/raw/keymeta.json'))
json.dump([dict(key=k, **{x: meta[k][x] for x in ("title", "url", "license", "artist")}) for k in sorted(meta)], open(f'{D}/credits.json', 'w'), indent=1, ensure_ascii=False)
print('ok')
