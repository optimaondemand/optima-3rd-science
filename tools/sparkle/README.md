# Wonder Films kit (G3 science) — `tools/sparkle/`

One lesson = one folder `lessons/<WW-LL>/`. The engine, the page structure and the tests are shared, so every
lesson comes out with the same shape and the same polish. Only the folder changes.

```
tools/sparkle/
  build_page.py      lesson.json -> one self-contained page (film, every module, credits, audio embedded)
  check_lesson.py    rules check: must say "0 FAIL" before anyone sees the lesson
  playtest.js        plays every module with the answers in lesson.json (Playwright), screenshots each one
  engine/            wf-film.js/.css (opener), wf-modules.js (modules), wf-lesson.js/.css (core). NO lesson content.
  shared/            opti.png (story-map owl), optima-logo.png
  lessons/17-01/     the model lesson: lesson.json, credits.json, fish-model.svg, music.mp3, img/*.jpg, audio/*.mp3
```

## Commands (run from tools/sparkle)
```
python3 check_lesson.py lessons/WW-LL/lesson.json
python3 build_page.py  lessons/WW-LL/lesson.json out/G3-Science-WW.LL-Wonder-Films-mockup.html
node playtest.js out/G3-Science-WW.LL-Wonder-Films-mockup.html 1150 out/pt
node playtest.js out/G3-Science-WW.LL-Wonder-Films-mockup.html 420 out/pt
```
playtest prints one line: `errors: []`, `ticks: ✓✓✓✓`, `frames: formation,compare,wall,det`, `checklist: n/n` (5/5 with Part C), `sideways: false`.

## The fixed page (every lesson, this order)
| Tab | Slot | lesson.json key |
|---|---|---|
| Warm-Up | original OAO header · film opener (end card = Big Question) · I can · Opti · **Specimen + Inspect** · Word Wall | `film`, `icans`, `opti.warm`, `specimen`, `words` |
| Lesson | Part 1 reading → **Process order + mini-movie** → quick check | `parts[0]`, `order`, `movie` |
| | Part 2 reading → **Comparison station** (predict ×2, model test, explain, curator cards) → behind-the-scenes card | `parts[1]`, `compare` |
| | Part 3 reading → **Investigation wall** (predict, brush 3–4 layers/sites, time elevator, real environment sky, pull-back line) → think-like-a-scientist | `parts[2]`, `wall` |
| | Director's cut (wow) · Key idea | `wow`, `keyIdea` |
| | Part 4 **Evidence cards** (observe → infer → predict → Past Revealed) · chart · Rebuild the scene (optional drawer) · explanation | `parts[3]`, `det`, `rebuild` |
| Self-Check | the lesson's 3 questions, one at a time | `quiz` |
| Assignment | Part A · Part B · Write and explain · Part C (REQUIRED: drawing + 2 labels, Save my drawing) · question callback · My answers · clickable checklist · **Premiere** · Coming up | `assign`, `premiere`, `next` |

## lesson.json keys (17.01 is the worked example — copy it, then replace every value)
- `id` `g3sci-WW-LL` · `lesson` "WW.LL" · `title` · `emoji` (header badge) · `details` (4 chips) · `icans` (verbatim) · `scientist`
- `opti` {warm, lesson, check, assign} — Opti's notes (de-ai-ify them)
- `film` — wf-film DATA: `shots` (leader · black · photo · reveal · xray · flash · archive · title; any shot may add `sfxAt` [{at, name: step|whoosh|thump|brush|shimmer|rumble|bubbles|tick|scan}]; `xray` = base `img` + hidden `img2`/`alt2` in window `win` [left%, top%, width%], scan band `band` from `y0` to `y1` starting `xrayAt` for `xrayDur` s, `xlabel`; `contain: true` letterboxes a portrait photo), `captions` (Opti's lines + `voice` file names), `bigQuestion`, `poster`, `endPoster`, `music`
- `specimen` {img, aspect ("w/h" of the image so hotspots line up; default 16/9), alt, kicker, title, look, do, number, card[ "<b>Name</b>", "Found: …", "Age/size: …", "What is it? <i>You decide.</i>"], hotspots[{name,x,y}] (≥4, fractions of the image), radius, notice, wonder}
- `words` [[emoji, word, meaning]]
- `parts` [4 × {kicker, title, html}] — the lesson's own reading, plain-language trimmed (Part 4 has no html)
- `order` {kicker, title, look, mix[4], scenes[4 × {img, alt, text, play, miss[4]}], check{q, options}} — scene i belongs in frame i
- `movie` {model (SVG file with `<g class="s1">`, `<g class="s2">`…), bg (water | swamp), bands[] + particleColors[] (optional layer/mud colors), real, realAlt, stamp, endCap, beats[{at ms, cap, particles{n,stop,dir,colors}, model{top,rot,show,hide}, layers{add,height | from,step,stagger}, counter[…], cut, clear, real, stamp, sfx}]} — must end on the real photo + stamp
- `compare` {kicker, title, look, trays[2 × {id,img,alt,label}], materials[2 × {key,label,img | swatch,note}], ask[2 × {q, ans, ok, miss}], testDo, press, disclaimer, results{<tray><material>: {text, fx}}, best[2], claimLead, claimMid, claim{<tray>: {feat[], featOk, eat[], eatOk}}, curator{<tray>: html}, missFeat, missClaim, done, after{kicker,img,alt,html}}
  - fx: crush · slice · squash · holes · bend · sink · float · melt · bounce · print · slump · none. swatches: clay wood metal rubber ice sponge water mud sand
  - `best` may list the same material for both trays (17.02: Amud, Bmud): students press, swap, press again.
- `wall` {kicker, title, look, do, predict{q, options[[k,label]], answer, mine, confirm, change}, sky, skyAlt, skyCap, unit, found, elevator[n+1], line[2], locked, first, next, endTitle, endText, rule, choices[3], layers[3–4 × {name, rock (optional band look: limestone | mudstone | shale | sandstone | redbed), img, alt, ask, clue, ans, ok, miss{}, tag, env, envAlt, envCap}], mix{q, options}}
- `wow` {kicker, title, img, alt, caption, html, inset, insetCap} · `keyIdea`
- `det` {look, do, noun, need (3), predict{q, options}, kicker, enough, cols[5], write{label, starter, min, chips}, items[≥4 × {id, img, alt, clues[{t, ok | miss}], org[], orgAns, orgShort, orgMiss, env, envAns, envMiss, envImg, envAlt, envCap, reveal, rebuildEnv, bts}]}
- `rebuild` {title, missPrefix, envs[{key,name,img,cap}], life[{name,img,env,miss}]}
- `quiz` [3 × {q, options[{t, ok | miss}]}] — the lesson's own questions and answers
- `assign` {partA, partB {title, do, items[{n, q, type choice|text, options | min, chips}]}, write{title, do, vocab[], need, prompts[3]}, partC{do, labels[2], min (words per label, default 6)}, checklist[{k, t, req{det, choice[], text{id: min}, vocab, sketch}}]} — the checklist MUST have a Part C item: `{"k":"c","t":"Part C: my drawing and both labels.","req":{"sketch":true,"text":{"in-c1":6,"in-c2":6}}}`
- `premiere` {title, director "JUNIOR <SCIENTIST>", storyKicker, frames[formation, compare, wall, det × {k, label, img, cap}]}
- `next` {title, text} · `chips` (answer-chip word lists) · `creditAlias` · `creditsExtra`

Images: `img/<key>.jpg`, ≤1280 px (zoom specimen 1600), q≈62, every one in `credits.json` (title, url, license, artist).
Keep the built file under ~10 MB so it can be emailed for audits.
