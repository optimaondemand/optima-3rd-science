#!/usr/bin/env python3
"""Wonder Films page builder (G3 science). One lesson.json in -> one sparkled page out.
Every lesson gets the SAME structure; only lesson.json changes.

usage: build_page.py lessons/<WW-LL>/lesson.json out/<file>.html
  Builds the inline preview (all images, music, audio embedded; one shareable file)."""
import json, base64, sys, pathlib, html, re
ROOT = pathlib.Path(__file__).resolve().parent
LP = pathlib.Path(sys.argv[1]); L = json.loads(LP.read_text()); OUT = pathlib.Path(sys.argv[2])
LDIR = LP.parent
E = html.escape

# ---------------- helpers ----------------
def opti(key, say):
    return f'<div class="wl-opti"><img src="{{{{opti}}}}" alt="Opti the owl"><div class="bub"><b class="who">Opti</b>{L["opti"][key]}<button class="wl-say" data-say="{say}" aria-label="Listen to Opti">🔊</button></div></div>'
def scene(n, name):
    return f'<div class="wl-scene"><div class="wl-clap"><div class="t"></div><div class="b">{L["lesson"]}</div></div><h2><small>Scene {n}</small>{name}</h2></div>'
def chips(spec):
    return '<div class="wl-hint-chips">' + ''.join(f'<span data-chip="{k}">{t}</span>' for k, t in spec) + '</div>'
def textbox(id_, gather, mn, ch=None, label=None, starter=None, style=''):
    h = f'<label for="{id_}">{label}</label>' if label else ''
    h += f'<p class="wl-starter">{starter}</p>' if starter else ''
    h += f'<textarea id="{id_}" data-gather="{E(gather)}" data-min="{mn}"' + (f' data-chips="{",".join(k for k, _ in ch)}"' if ch else '') + (f' style="{style}"' if style else '') + '></textarea>'
    if ch: h += chips(ch)
    if mn: h += f'<div class="wl-count" data-for="{id_}"></div>'
    return h
def choice_group(key, options, gather=None):
    g = f' data-gather="{E(gather)}"' if gather else ''
    return f'<div class="wl-choices" data-choice="{key}"{g}>' + ''.join(
        f'<button class="wl-choice" ' + (f'data-ok="{E(o["ok"])}"' if 'ok' in o else f'data-miss="{E(o["miss"])}"') + f'>{o["t"]}</button>' for o in options) + '</div><p class="wl-fb"></p>'
def stage(id_, cls, kicker, title, look, do, inner, say=''):
    return f'''<div class="wl-stage {cls}" id="{id_}"><h3 class="wl-stage-h"><span class="k">{kicker}</span>{title}</h3>
<div class="wl-look dark"><b>👀 What am I looking at?</b> {look}</div><p class="wl-do dark" data-say="{say}"><b>What to do:</b> {do}</p>{inner}</div>'''
def part(p):
    return f'<div class="wl-card wl-read"><h3><span class="k">{p["kicker"]}</span>{p["title"]}</h3>{p.get("html","")}</div>'

S, O, M, C, W, D = L['specimen'], L['order'], L['movie'], L['compare'], L['wall'], L['det']
P = L['parts']; A = L['assign']; PR = L['premiere']

# ---------------- page ----------------
tabs = [('warm', 'Scene 1', '🌅 Warm-Up'), ('lesson', 'Scene 2', '📖 The Lesson'), ('check', 'Scene 3', '🧠 Self-Check'), ('assign', 'Scene 4', '✍️ Assignment')]
body = f'''<div class="page-wrap">
<div class="header"><div class="header-brand"><div class="header-logo"><img src="{{{{optima_logo}}}}" alt="Optima Academy" /></div>
<div><div class="header-org">Optima Academy Online</div><div class="header-sub">An Education Experience Company</div></div></div>
<div class="header-title">Lesson {L["lesson"]}: {L["title"]}</div><div class="header-badge"><span>{L["emoji"]}</span><span>Lesson {L["lesson"]}</span></div></div>
<div class="wl-top"><div class="wl-hdr"><button class="wl-pill" id="wl-details-btn" aria-expanded="false">Lesson details ▾</button>
<button class="wl-pill" id="wl-music" aria-pressed="false">🎵 Music</button><button class="wl-pill" id="wl-motion" aria-pressed="true">✨ Motion</button></div>
<div class="wl-details" id="wl-details">{"".join(f"<span>{d}</span>" for d in L["details"])}</div>
<div class="wl-tabs"><nav role="tablist">{"".join(f'<button class="wl-tab" role="tab" data-tab="{k}" aria-selected="{str(i==0).lower()}"><small>{s}</small>{n}<span class="ck"></span></button>' for i,(k,s,n) in enumerate(tabs))}</nav></div></div>
<main>
<section class="wl-panel on" id="tab-warm" role="tabpanel">{scene(1,"Warm-Up")}
<div id="wf-film"></div>
<div class="wl-card wl-ican"><h3><span class="k">🎯 Today</span>I can…</h3><ol>{"".join(f"<li>{i}</li>" for i in L["icans"])}</ol></div>
{opti("warm", L["lesson"].replace(".","-")+"-welcome")}
''' + stage('m-spec', 'wl-wood', S['kicker'], S['title'], S['look'], S['do'], f'''
<div class="wl-specimen" id="spec-a"><div class="wl-slab"><img src="{{{{{S["img"]}}}}}" alt="{E(S["alt"])}"></div><div class="wl-brass">{S["number"]}</div>
<div class="wl-idcard">{"".join(f"<span>{c}</span>" if i else c for i,c in enumerate(S["card"]))}</div></div>
<div style="text-align:center"><button class="wl-btn gold" id="spec-open">🔍 Inspect specimen</button></div><p class="wl-fb dark" id="spec-fb"></p>
<div class="wl-paper wl-in" id="spec-boxes" hidden>{textbox("in-notice","Warm-Up · I notice",4,[["part","Names a part you saw"]],S["notice"])}{textbox("in-wonder","Warm-Up · I wonder",4,[["ask","Asks a question"]],S["wonder"])}</div>''', 'how-inspect') + f'''
<div class="wl-card" id="m-words"><h3><span class="k">📚 Word Wall</span>Words scientists use</h3><p class="wl-do" data-say="how-flip"><b>What to do:</b> Tap or click each card to flip it and read what the word means.</p>
<div class="wl-words">{"".join(f'<button class="wl-flip" type="button"><div class="in"><div class="f">{e} {w}<small>tap to flip</small></div><div class="bk"><b>{w}</b>{d}</div></div></button>' for e,w,d in L["words"])}</div></div>
<div class="wl-next"><button class="wl-btn gold" data-go="lesson">Next: 🎬 Scene 2 · The Lesson →</button></div></section>

<section class="wl-panel" id="tab-lesson" role="tabpanel">{scene(2,"The Lesson")}{opti("lesson", L["lesson"].replace(".","-")+"-lesson")}
{part(P[0])}
<div class="wl-card" id="m-order"><h3><span class="k">{O["kicker"]}</span>{O["title"]}</h3>
<div class="wl-look"><b>👀 What am I looking at?</b> {O["look"]}</div>
<p class="wl-do" data-say="how-order"><b>What to do:</b> Drag each photo into the film strip, from first to last. You can also tap a photo, then tap a frame. Get the order right and your strip becomes a movie.</p>
<div class="wl-strip" id="order-strip">{"".join(f'<div class="wl-slot" data-slot="{i}">{i+1}</div>' for i in range(4))}</div>
<div class="wl-strip-cap" id="order-cap">Frame 1 is empty. Which scene comes first?</div><div class="wl-tray" id="order-tray" style="margin-top:10px"></div>
<div class="wl-movie bg-{M.get("bg","water")}" id="fm-movie" hidden><div class="wl-mv-water"></div><div class="wl-mv-rays"></div><canvas class="wl-mv-part"></canvas><div class="wl-mv-layers"></div>
<div class="wl-mv-fish">{{{{MODEL_SVG}}}}</div><img class="wl-mv-real" src="{{{{{M["real"]}}}}}" alt="{E(M["realAlt"])}"><div class="wl-mv-count"></div><div class="wl-mv-cap"></div><div class="wl-mv-model">A model</div><div class="wl-mv-stamp">{M["stamp"]}</div></div>
<div style="text-align:center"><button class="wl-btn ghost" id="fm-replay" hidden>↻ Play my movie again</button></div>
<p class="wl-fb" id="order-fb"></p>
<div id="order-check" hidden><div class="wl-step"><div class="n">Quick check</div><p>{O["check"]["q"]}</p></div>{choice_group("bone", O["check"]["options"])}</div></div>
{part(P[1])}
''' + stage('m-bite', 'wl-wood', C['kicker'], C['title'], C['look'], 'Follow the steps one at a time. You will pick, test, and then explain.', f'''
<div class="wl-trays">{"".join(f'<div class="wl-tray-spec" data-t="{t["id"]}"><div class="wl-lit"><img src="{{{{{t["img"]}}}}}" alt="{E(t["alt"])}"></div><div class="wl-brass">{t["label"]}</div><div class="wl-drop" data-drop="{t["id"]}">Drop a test material here</div><div class="wl-curator"><b>Curator\'s interpretation</b><span></span></div></div>' for t in C["trays"])}</div>
<div class="wl-mats" id="bite-mats" hidden>{"".join(f'<div class="wl-mat" data-mat="{m["key"]}" tabindex="0" role="button">' + (f'<img src="{{{{{m["img"]}}}}}" alt="{E(m["label"])}">' if m.get("img") else f'<span class="wl-swatch sw-{m["swatch"]}"></span>') + m["label"] + (f'<small>{m["note"]}</small>' if m.get("note") else '') + '</div>' for m in C["materials"])}</div>
<div class="wl-paper" id="bite-step"></div>
<div id="teeth-end" hidden><div class="wl-bts" style="margin-top:14px"><b>{C["after"]["kicker"]}</b><div style="display:grid;grid-template-columns:120px 1fr;gap:12px;align-items:center;margin-top:6px"><img src="{{{{{C["after"]["img"]}}}}}" alt="{E(C["after"]["alt"])}" style="width:100%;border-radius:8px"><div>{C["after"]["html"]}</div></div></div></div>''', 'how-compare') + f'''
{part(P[2])}
''' + stage('m-dig', 'wl-stone', W['kicker'], W['title'], W['look'], W['do'], f'''
<div class="wl-paper" id="dig-predict"><div class="wl-step"><div class="n">Predict first</div><p>{W["predict"]["q"]}</p></div><div class="wl-chips">{"".join(f'<button class="wl-chip" data-p="{k}">{t}</button>' for k,t in W["predict"]["options"])}</div></div>
<div class="wl-digwrap" id="dig-wrap" hidden><div class="wl-elev" id="dig-elev"><div class="wl-elev-track"></div><div class="wl-elev-car">▶</div>{"".join(f'<span style="top:{[2,24,45,66,88][i]}%">{t}</span>' for i,t in enumerate(W["elevator"]))}</div>
<div class="wl-cliff" id="dig-cliff"><div class="wl-sky"><img class="now" src="{{{{{W["sky"]}}}}}" alt="{E(W["skyAlt"])}"><img class="then" alt=""><div class="wl-sky-cap">{W["skyCap"]}</div></div><div class="wl-soil"></div>
{"".join(f'<div class="wl-band b{i+1}{(' rock-' + l['rock']) if l.get('rock') else ''}" data-l="{i}"><img class="frag" src="{{{{{l["img"]}}}}}" alt=""><canvas></canvas><span class="lab">{W["unit"]} {i+1}</span></div>' for i,l in enumerate(W["layers"]))}
<div class="wl-olderline" id="dig-line"><span>{W["line"][0]}</span><i></i><span>{W["line"][1]}</span></div></div><div class="wl-digside"><div id="dig-card"></div></div></div>
<div class="wl-paper" id="dig-after" hidden><p style="margin:0 0 6px">{W["rule"]}</p><p id="dig-pred-res" style="margin:0 0 10px"></p>
<div class="wl-step"><div class="n">Think like a scientist</div><p>{W["mix"]["q"]}</p></div>{choice_group("mix", W["mix"]["options"])}</div>''', 'how-dig') + f'''
<div class="wl-wow" id="m-wow"><div class="k">{L["wow"]["kicker"]}</div><h3>{L["wow"]["title"]}</h3><div class="grid"><figure style="margin:0"><img src="{{{{{L["wow"]["img"]}}}}}" alt="{E(L["wow"]["alt"])}"><figcaption>{L["wow"]["caption"]}</figcaption></figure>
<div>{L["wow"]["html"]}<figure style="margin:10px 0 0"><img src="{{{{{L["wow"]["inset"]}}}}}" alt="" style="max-width:120px"><figcaption>{L["wow"]["insetCap"]}</figcaption></figure></div></div></div>
<div class="wl-key"><b>⭐ Key idea:</b> {L["keyIdea"]}</div>
<div class="wl-card" id="m-det"><h3><span class="k">{P[3]["kicker"]}</span>{P[3]["title"]}</h3><div class="wl-look"><b>👀 What am I looking at?</b> {D["look"]}</div>
<p class="wl-do" data-say="how-detective"><b>What to do:</b> {D["do"]}</p><div class="wl-det" id="det-cards"></div><div id="det-work"></div>
<table class="wl-chart" id="det-chart"><thead><tr>{"".join(f"<th>{c}</th>" for c in D["cols"])}</tr></thead><tbody></tbody></table>
<details class="wl-drawer" id="rebuild" hidden><summary><span class="k">🌍 Rebuild the ancient scene</span>{L["rebuild"]["title"]} <span class="wl-bonus">OPTIONAL</span><span class="wl-open">Open ▾</span></summary>
<p class="wl-do"><b>What to do:</b> Pick one you solved. Pick the place it points to, then pick the living things that belong there.</p><div class="wl-chips" id="rb-fossils"></div>
<div class="wl-rb-stage" id="rb-stage"><div class="wl-rb-bg"></div><div class="wl-rb-water"></div><div class="wl-rb-life"></div><div class="wl-rb-fossil"></div><div class="wl-rb-cap">Pick one to start.</div></div><div id="rb-steps"></div></details>
<div id="det-write" class="wl-in" hidden><div class="wl-step"><div class="n">Last step</div><p>Pick one from your chart and explain it.</p></div>{textbox("in-det","Lesson · My explanation",D["write"]["min"],D["write"]["chips"],D["write"]["label"],D["write"]["starter"])}</div></div>
<div class="wl-next"><button class="wl-btn gold" data-go="check">Next: 🎬 Scene 3 · Self-Check →</button></div></section>

<section class="wl-panel" id="tab-check" role="tabpanel">{scene(3,"Self-Check")}{opti("check", L["lesson"].replace(".","-")+"-check")}
<div class="wl-card" id="m-quiz">{"".join(f'<div class="wl-q{" on" if i==0 else ""}"><div class="wl-qnum">Question {i+1} of {len(L["quiz"])}</div><h3>{q["q"]}</h3>{choice_group("q"+str(i+1), q["options"])}</div>' for i,q in enumerate(L["quiz"]))}
<div class="wl-score" id="quiz-score" hidden></div><div style="text-align:center"><button class="wl-btn" id="quiz-next" disabled>Next question →</button></div></div>
<div class="wl-next"><button class="wl-btn gold" data-go="assign">Next: 🎬 Scene 4 · Assignment →</button></div></section>

<section class="wl-panel" id="tab-assign" role="tabpanel">{scene(4,"Assignment")}{opti("assign", L["lesson"].replace(".","-")+"-assign")}
<div class="wl-card">'''
def items(sec, prefix):
    h = ''
    for it in sec['items']:
        h += f'<p><b>{it["n"]}.</b> {it["q"]}</p>'
        key = f'{prefix}{it["n"]}'
        h += choice_group(key, it['options'], f'Part {prefix.upper()} · {it["n"]}') if it['type'] == 'choice' else textbox('in-' + key, f'Part {prefix.upper()} · {it["n"]}', it['min'], it.get('chips'))
    return h
body += f'<h3><span class="k">🔍 Part A</span>{A["partA"]["title"]}</h3><p class="wl-do"><b>What to do:</b> {A["partA"]["do"]}</p><div class="wl-in">{items(A["partA"],"a")}</div>'
body += f'<div class="wl-part wl-in"><h3><span class="k">🚀 Part B</span>{A["partB"]["title"]}</h3><p class="wl-do"><b>What to do:</b> {A["partB"]["do"]}</p>{items(A["partB"],"b")}</div>'
Wr = A['write']
body += f'<div class="wl-part wl-in"><h3><span class="k">✍️ Write and explain</span>{Wr["title"]}</h3><p class="wl-do"><b>What to do:</b> {Wr["do"]}</p>'
body += ''.join(textbox(f'in-w{i+1}', ['Write · I noticed', 'Write · I can infer', 'Write · Why it makes sense'][i], 10, None, lab, st) for i, (lab, st) in enumerate(Wr['prompts']))
body += '<div class="wl-hint-chips" id="vocab-chips">' + ''.join(f'<span data-v="{v}">{v}</span>' for v in Wr['vocab']) + f'</div><div class="wl-count" id="vocab-count" data-need="{Wr["need"]}">Science words used: 0 of {Wr["need"]}</div></div>'
PC = A['partC']
body += f'''<div class="wl-part wl-in" id="partc"><h3><span class="k">🎨 Part C</span>Draw and label</h3>
<p class="wl-do"><b>What to do:</b> {PC["do"]}</p><div class="wl-tools" id="sk-tools"><button style="background:#2B1D12" data-c="#2B1D12" class="on" aria-label="Black"></button><button style="background:#9c4a31" data-c="#9c4a31" aria-label="Red-brown"></button><button style="background:#d6c093" data-c="#d6c093" aria-label="Sand"></button><button style="background:#2D6A4F" data-c="#2D6A4F" aria-label="Green"></button><button style="background:#0288D1" data-c="#0288D1" aria-label="Blue"></button><button class="txt" id="sk-clear">Clear</button></div>
<canvas class="wl-sketch" id="sketch"></canvas><div style="text-align:right"><button class="wl-btn ghost" id="sk-save">⬇️ Save my drawing</button></div><div class="wl-in">{textbox("in-c1","Part C · 1",PC.get("min",6),None,PC["labels"][0],None,"min-height:52px")}{textbox("in-c2","Part C · 2",PC.get("min",6),None,PC["labels"][1],None,"min-height:52px")}</div></div>
<div class="wl-part"><h3><span class="k">🎬 Your question from Scene 1</span>Can you answer it now?</h3><p id="wonder-back" class="wl-look">You haven't written a question yet. Go to the Warm-Up to add one.</p><div class="wl-in"><textarea id="in-answer" data-gather="My question, answered" data-min="0" style="min-height:60px" placeholder="My answer is…"></textarea></div></div></div>
<div class="wl-card wl-gather"><h3><span class="k">📋 My answers</span>Everything you wrote, in one place</h3><pre id="gather-out">(Your answers show up here as you write.)</pre>
<button class="wl-btn" id="g-copy">📋 Copy my answers</button><button class="wl-btn ghost" id="g-dl">⬇️ Download</button><button class="wl-btn ghost" id="g-print">🖨️ Print</button>
<p class="wl-do" style="margin-top:10px"><b>How to turn in:</b> Copy your answers and paste them into the Canvas assignment. Or download the file and upload it. Then press <b>Save my drawing</b> in Part C and upload your drawing too.</p>
<h3 style="margin-top:14px">✅ Checklist</h3><p class="wl-do"><b>What to do:</b> Tap each item when it is done. Items you finish on the page check themselves.</p>
<ul class="wl-check" id="checklist">{"".join(f'<li data-ck="{c["k"]}">{c["t"]}</li>' for c in A["checklist"])}</ul></div>
<div class="wl-stage wl-film" id="m-premiere"><h3 class="wl-stage-h"><span class="k">🎬 {PR["title"]}</span>Your exhibit</h3>
<p class="wl-do dark"><b>What to do:</b> Check your exhibit. Pick the one you wrote about, add your first name, then press Premiere film.</p>
<div class="wl-exhibit" id="exhibit"><div class="wl-ex-spec"><div class="wl-slab sm"><img alt="" id="ex-img"></div><div class="wl-brass" id="ex-num">My specimen</div><div class="wl-chips" id="ex-pick"></div></div>
<div class="wl-ex-card"><p><b>I observed…</b><span id="ex-obs"></span></p><p><b>I think it was…</b><span id="ex-org"></span></p><p><b>My evidence…</b><span id="ex-ev"></span></p><p><b>It tells us…</b><span id="ex-tells"></span></p><div id="ex-sketch"></div></div></div>
<div class="wl-paper wl-in" style="margin-top:10px"><label for="in-director">Director's first name</label><input id="in-director" class="wl-name" maxlength="20" autocomplete="off" placeholder="First name"><p class="wl-fb" id="dir-fb"></p></div>
<h4 class="wl-reel-h">🎞️ This film's frames</h4><div class="wl-reel" id="reel">{"".join(f'<div class="wl-frame locked" data-f="{f["k"]}"><div class="ph"><img src="{{{{{f["img"]}}}}}" alt=""></div>Frame {i+1}<br>{f["label"]}</div>' for i,f in enumerate(PR["frames"]))}</div>
<p class="wl-do dark" id="reel-msg">Earn all four frames in the Lesson, then finish the checklist.</p><div style="text-align:center"><button class="wl-btn gold" id="premiere-btn" disabled>🎬 Premiere film</button></div></div>
<div class="wl-card"><h3><span class="k">🔜 Coming up next</span>{L["next"]["title"]}</h3><p style="margin:0">{L["next"]["text"]}</p></div>
<details class="wl-card wl-credits"><summary><b>Photo and music credits</b></summary><ul>{{{{credits}}}}</ul></details>
</section></main></div>
<div class="wl-theater" id="theater" hidden><button class="wl-th-x" aria-label="Close">✕</button><div class="wl-th-screen"></div></div>
<div class="wl-inspect" id="inspect" hidden role="dialog" aria-label="Inspect specimen"><div class="wl-ins-box"><button class="wl-ins-x" aria-label="Close">✕ Close</button>
<div class="wl-ins-view" style="--ar:{S.get("aspect","16/9")}"><img id="ins-img" alt="Specimen, close up"><div class="wl-lens" hidden></div><div class="wl-ins-marks"></div></div>
<div class="wl-ins-ctrl"><button class="wl-pill dark" id="ins-lens" aria-pressed="true">🔍 Magnifying lens: on</button><label>Zoom <input type="range" id="ins-zoom" min="1" max="3" step="0.1" value="1"></label><span id="ins-found">Found 0 of 3</span></div>
<p class="wl-ins-tip" id="ins-tip">Move the lens over it. When you spot something, tap it.</p></div></div>'''

# ---------------- assets ----------------
REPO = '--repo' in sys.argv   # repo mode: reference assets/sparkle/... instead of inlining (pages stay small)
COPY = []                      # (source, repo-relative destination) for repo mode
SLUG = 'g3sci-' + LDIR.name
def uri(p, mime):
    if not REPO: return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()
    dest = f'assets/sparkle/{p.name}' if p.parent.name == 'shared' else f'assets/sparkle/{SLUG}/{p.parent.name + "-" if p.parent.name == "audio" else ""}{p.name}'
    COPY.append((p, dest)); return dest
keys = set(re.findall(r'\{\{(\w+)\}\}', body)) - {'credits', 'opti', 'optima_logo', 'MODEL_SVG'}
film = L['film']; film['startTarget'] = '.wl-ican'
keys |= {s.get(f) for s in film['shots'] for f in ('img', 'img2') if s.get(f)} | {film['poster'], film.get('endPoster', film['poster'])}
keys |= {x['img'] for x in O['scenes']} | {l['img'] for l in W['layers']} | {l['env'] for l in W['layers']} | {f['img'] for f in D['items']} | {f['envImg'] for f in D['items']}
keys |= {e['img'] for e in L['rebuild']['envs']} | {x['img'] for x in L['rebuild']['life']} | {f['img'] for f in PR['frames']} | {S['img'], M['real']}
keys.discard(None)
IMGD, SH = LDIR / 'img', ROOT / 'shared'
missing_img = [k for k in sorted(keys) if not (IMGD / f'{k}.jpg').exists()]
if missing_img: sys.exit('MISSING IMAGES in ' + str(IMGD) + ': ' + ', '.join(missing_img))
img = {k: uri(IMGD / f'{k}.jpg', 'image/jpeg') for k in sorted(keys)}
img['opti'] = uri(SH / 'opti.png', 'image/png'); img['optima_logo'] = uri(SH / 'optima-logo.png', 'image/png')
if (LDIR / 'music.mp3').exists(): img['music'] = uri(LDIR / 'music.mp3', 'audio/mpeg')
for c in film.get('captions', []):
    v = LDIR / 'audio' / f"{c.get('voice')}.mp3"
    if c.get('voice') and v.exists(): img[c['voice']] = uri(v, 'audio/mpeg')
for nk in ('welcome', 'lesson', 'check', 'assign'):  # Opti's notes: audio/<WW-LL>-<note>.mp3 -> the note's 🔊 button
    v = LDIR / 'audio' / f"{L['lesson'].replace('.', '-')}-{nk}.mp3"
    if v.exists(): img[f"say-{L['lesson'].replace('.', '-')}-{nk}"] = uri(v, 'audio/mpeg')

cred = {c['key']: c for c in json.loads((LDIR / 'credits.json').read_text())}
alias = L.get('creditAlias', {})
lines, seen = [], set()
for k in sorted(keys):
    c = cred.get(alias.get(k, k))
    if not c or c['url'] in seen: continue
    seen.add(c['url']); t = c['title'].rsplit('.', 1)[0]; t = t if len(t) < 80 else t[:77] + '…'
    a = re.sub(r'\s+', ' ', c['artist'] or 'unknown').strip()[:60]
    lines.append(f'<li><a href="{E(c["url"])}" target="_blank" rel="noopener">{E(t)}</a>, {E(a)}, {E(c["license"])}</li>')
for extra in L.get('creditsExtra', []): lines.append(f'<li>{extra}</li>')
film['credits'] = [re.sub(r'^<li>|</li>$', '', l) for l in lines]
missing = [k for k in sorted(keys) if alias.get(k, k) not in cred]
if missing: print('WARNING: no credit for', missing)

def fill(m):
    k = m.group(1)
    if k == 'credits': return '\n'.join(lines)
    if k == 'MODEL_SVG': return (LDIR / M['model']).read_text()
    return img[k]
body = re.sub(r'\{\{(\w+)\}\}', fill, body)
SRC = ROOT / 'engine'
css = (SRC / 'wf-film.css').read_text() + '\n' + (SRC / 'wf-lesson.css').read_text()
js = (SRC / 'wf-film.js').read_text() + '\n' + (SRC / 'wf-modules.js').read_text() + '\n' + (SRC / 'wf-lesson.js').read_text()
data = {k: v for k, v in L.items() if k not in ('film',)}
if REPO:
    for f in ('wf-film.css', 'wf-lesson.css', 'wf-film.js', 'wf-modules.js', 'wf-lesson.js'): COPY.append((SRC / f, f'assets/sparkle/{f}'))
    v = __import__('hashlib').md5((css + js).encode()).hexdigest()[:8]
    head_css = f'<link rel="stylesheet" href="assets/sparkle/wf-film.css?v={v}"><link rel="stylesheet" href="assets/sparkle/wf-lesson.css?v={v}"><style>.wf-credits{{display:none}}</style>'
    tail_js = ''.join(f'<script src="assets/sparkle/{f}?v={v}"></script>' for f in ('wf-film.js', 'wf-modules.js', 'wf-lesson.js'))
else:
    head_css = f'<style>{css}\n.wf-credits{{display:none}}</style>'; tail_js = f'<script>{js}</script>'
fix_urls = "for(var k in WF_IMG)if(!/^data:/.test(WF_IMG[k]))WF_IMG[k]=new URL(WF_IMG[k],document.baseURI).href;" if REPO else ''
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lesson {L["lesson"]}: {E(L["title"])} · Wonder Films</title>{head_css}</head><body>
{body}
<script>window.WF_IMG={json.dumps(img)};window.WF_DATA={json.dumps(film)};window.WL_DATA={json.dumps(data)};{fix_urls}</script>
{tail_js}
</body></html>'''
if REPO:
    import shutil
    root = OUT.parent
    for src, dest in COPY:
        d = root / dest; d.parent.mkdir(parents=True, exist_ok=True); shutil.copyfile(src, d)
    print('repo assets:', len(set(d for _, d in COPY)))
OUT.write_text(page)
print(OUT, round(OUT.stat().st_size / 1e6, 2), 'MB')
