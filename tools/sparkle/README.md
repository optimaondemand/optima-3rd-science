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
- `film` — wf-film DATA: `shots` (leader · black · photo · reveal · xray · flash · archive · title; any shot may add `sfxAt` [{at, name: step|whoosh|thump|brush|shimmer|rumble|bubbles|tick|scan}]; `xray` = base `img` + hidden `img2`/`alt2` in window `win` [left%, top%, width%], scan band `band` from `y0` to `y1` starting `xrayAt` for `xrayDur` s, `xlabel`; `contain: true` letterboxes a portrait photo; a `reveal` may set `cover` [c1, c2] for the layer that is brushed away (default sand dust; 27.01 uses frost white) and `chip` "r,g,b" for the flecks), `captions` (Opti's lines + `voice` file names), `bigQuestion`, `poster`, `endPoster`, `music`
- `specimen` {img, aspect ("w/h" of the image so hotspots line up; default 16/9), alt, kicker, title, look, do, number, card[ "<b>Name</b>", "Found: …", "Age/size: …", "What is it? <i>You decide.</i>"], hotspots[{name,x,y}] (≥4, fractions of the image), radius, notice, wonder}
- `words` [[emoji, word, meaning]] — voiced when `audio/word-<slug>.mp3` exists (slug = the word in lower case, other characters become `-`): a 🔊 on each Word Wall card and inside the pop-up of every dotted word. Record all the words in ONE take ("Fossil. Evidence. …"), Scribe it, cut one clip per word at the quiet gaps, 64 kbps mono. The build prints `key words voiced: n / n`.
- **"What to do" lines read by Opti** (14 Nov 2026): `shared/how-lines.json` + `shared/audio/<slug>.mp3` (recorded once, reused by every lesson whose printed line has the same words; repo `assets/sparkle/how/`) and `lessons/<WW-LL>/how-lines.json` + `audio/how-<WW-LL>-<part>.mp3` (this lesson only). Entry: `{"page": printed words, "say": words sent}`. Every `.wl-do` line and `compare.testDo` is matched by its exact printed words; a 🔊 appears only when the clip exists; a lesson entry whose line changed is not attached (the build warns). The build prints `what to do voiced: n / n`. Write lines in the shared wording when the lesson allows, so only lesson-specific lines (usually the comparison test step and Part C) cost credits.
- `parts` [4 × {kicker, title, html}] — the lesson's own reading, plain-language trimmed (Part 4 has no html)
- `order` {kicker, title, look, mix[4], scenes[4 × {img, alt, text, play, miss[4]}], check{q, options}} — scene i belongs in frame i
- `movie` {model (SVG file with `<g class="s1">`, `<g class="s2">`…), bg (water | swamp), bands[] + particleColors[] (optional layer/mud colors), real, realAlt, stamp, endCap, beats[{at ms, cap, particles{n,stop,dir,colors}, model{top,rot,show,hide}, layers{add,height | from,step,stagger}, counter[…], cut, clear, real, stamp, sfx}]} — must end on the real photo + stamp. Optional `counterIcon` (default ⏳; 27.02 uses 🌡️ for a temperature counter)
- `compare` {kicker, title, look, trays[2 × {id,img,alt,label}], materials[2 × {key,label,img | swatch,note}], ask[2 × {q, ans, ok, miss}], testDo, press, disclaimer, results{<tray><material>: {text, fx}}, best[2], claimLead, claimMid, claim{<tray>: {feat[], featOk, eat[], eatOk}}, curator{<tray>: html}, missFeat, missClaim, done, after{kicker,img,alt,html}}
  - fx: crush · slice · squash · holes · bend · sink · float · melt · bounce · print · slump · wick · warm · wet · rip · sway · glow · shade · none. swatches: clay wood metal rubber ice sponge water mud sand towelstrip darkpaper cup box lamp torch fan sieve lid pad scissors fence (25.01) boots (25.02) marble (26.01) ruler balance (26.02). fx `frost` (27.01: icy glow when heat is taken away). Wall band looks `snowcap`, `cloud`, `haze`, `gulf` (27.01 Sky Ladder, high and cold → warm Gulf). Swatch `thermo` (thermometer) and wall bands `night`, `space` (28.01 Glow Test, Star Elevator). Swatch `sun` (an hour of sunshine; 28.02 Shirt Test)
  - movie `bg`: water · swamp · grove · prairie · lab. Wall band looks also include water1–water4 (bright shallow → dark deep) and maze1–maze4 (cardboard, bright near a light hole → dark at the bottom; 20.02).
  - `best` may list the same material for both trays (17.02: Amud, Bmud): students press, swap, press again.
- `wall` {kicker, title, look, do, predict{q, options[[k,label]], answer, mine, confirm, change}, sky, skyAlt, skyCap, unit, found, elevator[n+1], line[2], locked, first, next, endTitle, endText, rule, choices[3], layers[3–4 × {name, rock (optional band look: limestone | mudstone | shale | sandstone | redbed | leafsun | leafmid | leafshade | leafdark | bark | branch | soil), img, alt, ask, clue, ans, ok, miss{}, tag, env, envAlt, envCap}], mix{q, options}}
- `wow` {kicker, title, img, alt, caption, html, inset, insetCap} · `keyIdea`
- `det` {look, do, noun, need (3), predict{q, options}, kicker, enough, cols[5], write{label, starter, min, chips}, items[≥4 × {id, img, alt, clues[{t, ok | miss}], org[], orgAns, orgShort, orgMiss, env, envAns, envMiss, envImg, envAlt, envCap, reveal, rebuildEnv, bts}]}
- `rebuild` {title, missPrefix, envs[{key,name,img,cap}], life[{name,img,env,miss}]}
- `quiz` [3 × {q, options[{t, ok | miss}]}] — the lesson's own questions and answers
- `assign` {partA, partB {title, do, items[{n, q, type choice|text|graph, options | min, chips}]}, write{title, do, vocab[], need, prompts[3]}, partC{do, labels[2], min (words per label, default 6)}, checklist[{k, t, req{det, choice[], text{id: min}, vocab, sketch}}]} — the checklist MUST have a Part C item: `{"k":"c","t":"Part C: my drawing and both labels.","req":{"sketch":true,"text":{"in-c1":6,"in-c2":6}}}`
- `premiere` {title, director "JUNIOR <SCIENTIST>", storyKicker, frames[formation, compare, wall, det × {k, label, img, cap}]}
- `next` {title, text} · `chips` (answer-chip word lists) · `creditAlias` · `creditsExtra`

Images: `img/<key>.jpg`, ≤1280 px (zoom specimen 1600), q≈62, every one in `credits.json` (title, url, license, artist).
Keep the built file under ~10 MB so it can be emailed for audits.

## Safety: the kit never silently loses a page edit (kit_guard.py, 10 Nov 2026)

Every build compares the live page with what the kit last wrote (`lessons/<key>/built.sha1`; `?v=` stamps are ignored).

- Page unchanged since the last build: the build overwrites it as usual.
- Page edited outside the kit (a standards pass, a typo fix, a find-and-replace across pages): the build **stops before writing** and shows what would be lost. Then:
  - `--check` shows the differences between the page and what the kit would build (writes nothing).
  - `--absorb` turns those differences into new entries at the end of the lesson's `fixes.json`, proves a rebuild now gives back the page exactly, and saves. Run the build again afterwards.
  - `--force` overwrites anyway (the outside edits are lost).
- Edits inside the DATA block can't be absorbed: change the lesson's data file instead.
- Habit: after any edit made straight to lesson pages, run every lesson with `--check` (then `--absorb`) before the next rebuild.

## One step at a time (`assets/sparkle/onestep.js` + `onestep.css`, 11 Nov 2026)

The ELA step walker, for science. On each tab the student sees ONE step, with **◂ Back · Step 3 of 27 · 👆 Next**; the last step's button opens the next tab. Nothing is removed: hidden steps keep their answers, so saving, the gathered answers and the checklists still work. The same two files sit in the G3, G4 and G5 science repos (the grade is detected from the page); change one, copy it to the other two.

- On for every Wonder Films lesson (the builder adds the two files). Off for a lesson: `"onestep": false` in `lesson.json`.
- Off for one visit: add `?steps=0` to the address.
- How a tab is cut: big cards are opened up and their header stays on screen; a heading, Opti/Dr. Reyes strip or short label line starts a step and pulls the next thing in; answer boxes, help ladders, buttons and anything hidden at load stay with the thing before; a game, lab or stage is one step; reading is cut at about 70 words. A step with nothing showing is skipped and not counted.
- Jumps: any script that scrolls to a part of the page calls `OneStep.reveal(element)` first (already done in the page's jump helper, so the Assignment map and "show me" buttons open the right step).
- Write for the steps: every step needs its own direction line; a direction never names something that only appears on a later step.
- Test: `node tools/sparkle/stepwalk.js http://localhost:<port>/<page>.html 1150` and again at `420` (serve the repo first). It walks every Next and Back and fails on an empty step, sideways scroll, a count that does not move, a last step that is not "Step N of N", or a page error. Add a third argument to save a picture of every step, and look at them.
- Target: about 20 to 27 steps a lesson.
- `playtest.js` and `jumpcheck.js` open the step that holds a thing before they touch it, so they run with the walker on.

## Part A bar graph (19.02, 14 Nov 2026)
A Part A item may be `{"n":1, "type":"graph", "q", "title", "yLabel", "cats":[…], "series":[{"name","color","values":[…]}], "max", "unit"}`. The page shows the data table and an empty bar graph; students tap or drag in a column, use ＋/－, or arrow keys, then press **Check my graph** (wrong bars get a red outline). A correct graph counts like a right choice: put its key (e.g. `a1`) in the checklist's `choice` list. Its values go into My answers. check_lesson.py checks the data; playtest builds it with the ＋ buttons.

## Film badge + rewind lines, lid swatch, teacher intro video (22.01, 16 Nov 2026)
- Any film shot may add `badge {text, dur}` (a corner label such as "◀◀ REWIND" or "▶ PLAY"; `dur` = seconds it stays, default the whole shot) and `vhs: true` (tape-rewind lines; off with reduced motion).
- New comparison swatch `lid` (clear plastic lid) and effect `runoff` (water slides off and away).
- Teacher intro video: every page has a hidden slot under Opti's Warm-Up note (`#tvid`, `data-slot="<WW-LL>-intro"`). On load it reads `video-manifest.json` (default: the repo's raw GitHub copy; override with `videoManifest` in lesson.json). Only when that slot is `"status": "ready"` with a YouTube or Vimeo embed does the card appear; otherwise it stays hidden. Nothing per lesson. A manifest that isn't valid JSON keeps every slot hidden.

## Evidence cards: per-card "which fix works?" prediction (22.02, 16 Nov 2026)
- Any `det.items[i]` may carry its own `predict {q, options[[k,label]]}`; it replaces `det.predict` for that card (its keys must still be in `det.predict.options`, and `envAns` must be one of them). Write the labels as phrases that read after "You pictured …" (e.g. "Moving the tortoises to protected land").
- `det.inferQ` (Step 2 question, default "What was it?"), `det.inferDone` (the done line, default "It was"), `det.chartSo` (chart evidence, default "so it was").
- `premiere.thinkLabel` (exhibit line, default "I think it was").
All optional; lessons without them are unchanged (all 12 built lessons re-checked: 0 FAIL, playtest 1150 pass).

## Film threads (33.01, 21 Nov 2026)
Any photo shot may add `threads {pts: [[x%, y%], …], at, dur}`: glowing gold threads draw themselves from point to point across the photo and a dot lights at each point (tick, then a shimmer on the last). Points are percent of a 16:9 frame, so crop the photo to 16:9 and keep the zoom gentle (≤ 1.05) so the dots stay on their subjects. Keep points out of the caption box (bottom middle). Reduced motion: the whole web appears at `at`. All built lessons re-checked (check + playtest 1150).
