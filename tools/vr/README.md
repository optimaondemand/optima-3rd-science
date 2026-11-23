# G3 Science VR kit (`tools/vr/`) — one weekly VR page (goes with lesson W.01)

```
python3 check_vr.py weeks/WW/week.json                        # rules (0 FAIL)
python3 build_vr.py weeks/WW/week.json out/G3-Science-Week-WW-VR-mockup.html
python3 check_vr.py weeks/WW/week.json out/G3-Science-Week-WW-VR-mockup.html   # + reading load per path
node playtest_vr.js out/G3-Science-Week-WW-VR-mockup.html 1150 out/pt
node playtest_vr.js out/G3-Science-Week-WW-VR-mockup.html 420 out/pt
python3 build_vr.py weeks/WW/week.json ../../vr-WW.html --repo   # live page (assets referenced)
```
playtest prints one line: errors [], steps 5, badge true, help 14/14, game n/n, words ✓, stamp true, pdf ok, sideways false.

- `engine/vr.css`, `engine/vr.js`: no week words. Repo copies go to `assets/sparkle/vr/`.
- `weeks/WW/`: week.json, credits.json, img/<key>.jpg (≤1280 px, q≈62), audio/opti-<clip>.mp3 (brief, step1–5, extra, studio; no done/badge clip). Repo copies go to `assets/sparkle/vr-WW/`.
- Copy `weeks/17/` to start a new week, then replace every value. Model pilot: week 17 (The Lost Sea).
- Help drawer images: `images/vr-canvas-help-*.jpg` at the repo root (same as G4). `vr-assets.txt` = the app's asset list (map + search words are checked against it).

## Studio Day games (one engine, DATA picks the look)
- **Cousins match** (week 17): `studio.pairs[].fossil` + `studio.cousins`; drag the card onto a picture, then tap a place.
- **Casting call** (week 18): add `"type": "cast"`, `"frameImg": "cousin"`, `studio.labels` (done, q2, pdfTitle, cols) and give each round a `card` (img, name, alt, facts). Drag a picture onto the place card, then tap the trait. `studio.places` holds the trait buttons.
- A model card can carry one `trait` line (week 18).
- playtest_vr.js reads the place keys and the PDF title from the page, so it plays either game.
- **Sort** (week 19): `"type": "sort"`, `"framePl": "bin"`, `studio.bins` (two bins), each round a `card` + `bin` + `ok` + `miss`; a round with a `place` then asks the follow-up from `studio.places`, a round without one shows a Next button. Labels add `q1` and `next`. No `cousins` needed.
- Week 20 additions (all optional, DATA only): a sort round can carry its own question `q`, a drawn card (`card.art` = `img/<key>.svg`, a model with no words on it; say "A model" in `facts`) and a real-photo `proof` shown after the right answer; more than 2 bins lay out as 4 arrows. The hook can be a storyboard: `hook.strip` (photos with captions) + `hook.blank` instead of `hook.img`.
- **Fly** (week 21): `"type": "fly"`, `"framePl": "tag"`, `studio.kinds` (key, name, plural, img, alt, ok) and `studio.flowers` (id, kind, name, img, alt; exactly 2 per kind, listed in the order they show). Tap one, then tap or drag to its match. Labels: flight, start, pick ({kind}), same, miss ({from}, {to}), tag, done, pdfTitle, cols (2 columns).
- **Clean** (week 22): `"type": "clean"`, `"framePl": "tag"`, `studio.items` (id, name, img, alt, msg; litter also has `"trash": true` and `why`) and `studio.action` (name, img, alt, q, options, right, miss). Tap or drag only the litter into the bin, then pick the action. Labels: step1, step2, start, bin, tag, cleared, done, pdfTitle, cols (2 columns).
- **Spot** (week 23): `"type": "spot"`, `studio.scene` (art = `img/<key>.svg`, alt), `studio.spots` (id, x, y in percent, name, msg; polluting ones add `"pollute": true`, kind, miss, proof {img, alt, cap}) and `studio.places` (the kinds). Put each pin beside its object, not on top of it. Labels: find, start, lens, q2, next, done, pdfTitle, cols (2 columns).
