#!/usr/bin/env python3
"""G3 Science VR kit: weeks/<WW>/week.json -> one page.

  python3 build_vr.py weeks/17/week.json out/G3-Science-Week-17-VR-mockup.html          (mockup: everything inline)
  python3 build_vr.py weeks/17/week.json ../../vr-17.html --repo                         (repo: assets referenced)

Repo mode expects, relative to the repo root:
  assets/sparkle/wf-lesson.css, assets/sparkle/opti.png, assets/sparkle/optima-logo.png (already there from Wonder Films)
  assets/sparkle/vr/vr.css, assets/sparkle/vr/vr.js        (engine, copied from tools/vr/engine)
  assets/sparkle/vr-<W>/img/<key>.jpg, assets/sparkle/vr-<W>/audio/opti-<clip>.mp3
  images/vr-canvas-help-*.jpg                              (help drawer, shared with G4)
The engine holds no week words. All words live in week.json.
"""
import base64, html, json, os, re, sys

KIT = os.path.dirname(os.path.abspath(__file__))


def kitfile(*cands):
    # first existing path: lets the kit run inside the repo (tools/vr next to tools/sparkle, images/ at the root)
    for c in cands:
        p = os.path.join(KIT, c)
        if os.path.exists(p):
            return p
    raise FileNotFoundError(cands[0])
E = html.escape


def b64(path, mime):
    with open(path, 'rb') as f:
        return 'data:%s;base64,%s' % (mime, base64.b64encode(f.read()).decode())


def build(week_path, out_path, repo=False):
    wdir = os.path.dirname(os.path.abspath(week_path))
    W = json.load(open(week_path, encoding='utf-8'))
    wk = W['week']
    credits = json.load(open(os.path.join(wdir, 'credits.json'), encoding='utf-8'))
    used = []

    def img(key):
        if key not in used:
            used.append(key)
        if repo:
            return 'assets/sparkle/vr-%s/img/%s.jpg' % (wk, key)
        return b64(os.path.join(wdir, 'img', key + '.jpg'), 'image/jpeg')

    def art(key):
        # a drawn model (weeks/WW/img/<key>.svg), used where a real photo would give the answer away
        if repo:
            return 'assets/sparkle/vr-%s/img/%s.svg' % (wk, key)
        return b64(os.path.join(wdir, 'img', key + '.svg'), 'image/svg+xml')

    def pic(card):
        return art(card['art']) if card.get('art') else img(card['img'])

    def shared(name):
        if repo:
            return 'assets/sparkle/' + name
        return b64(kitfile('shared/' + name, '../sparkle/shared/' + name), 'image/png')

    def help_img(name):
        if repo:
            return 'images/' + name
        return b64(kitfile('images/' + name, '../../images/' + name), 'image/jpeg')

    clips = {}
    for c in W['voice']:
        p = os.path.join(wdir, 'audio', 'opti-%s.mp3' % c)
        if os.path.exists(p):
            clips[c] = ('assets/sparkle/vr-%s/audio/opti-%s.mp3' % (wk, c)) if repo else b64(p, 'audio/mpeg')

    def play(c):
        if c in clips:
            return '<button class="vr-play" type="button" data-clip="%s" aria-label="Listen to Opti">🔊 Opti</button>' % c
        return ''

    canvas = E(W['canvasName'])

    # ---------- models block ----------
    mb = []
    for g in W['vr']['groups']:
        mb.append('<div class="vr-group"><h4>%s</h4><div class="vr-models">' % E(g['title']))
        for m in g['models']:
            mb.append('<div class="vr-model"><img src="%s" alt="%s" loading="lazy"><div><b>%s</b>%s<span class="vr-word">%s</span></div></div>'
                      % (img(m['img']), E(m['alt']), E(m['name']), ('<span class="vr-trait">%s</span>' % E(m['trait'])) if m.get('trait') else '', E(m['word'])))
        mb.append('</div></div>')
    models_html = ''.join(mb)

    # ---------- steps ----------
    steps = []
    n = len(W['vr']['steps'])
    for i, s in enumerate(W['vr']['steps']):
        if s.get('where'):
            steps.append('<div class="vr-where">%s</div>' % E(s['where']))
        body = s['html'].replace('@MODELS@', models_html).replace('@CANVAS@', canvas)
        steps.append('<div class="vr-step" data-step="%d"><button class="vr-chk" type="button" aria-label="Mark step %d done" aria-pressed="false"></button>'
                     '<div><div class="sn">Step %d of %d · %s %s</div><div class="st">%s</div></div></div>'
                     % (i, i + 1, i + 1, n, E(s['title']), play(s.get('clip', '')), body))
        ex = W['vr'].get('extra')
        if ex and ex['after'] == i + 1:
            steps.append('<div class="vr-extra"><span class="vr-tag">VR only</span><b>Extra shot, if you have time</b> %s<div class="st">%s</div></div>'
                         % (play(ex.get('clip', '')), ex['html']))

    # ---------- hook ----------
    h = W['hook']
    rows = ''.join('<tr><td>%s</td><td>%s</td></tr>' % (E(a), E(b)) for a, b in h['rows'])
    if h.get('strip'):
        # storyboard hook: a strip of real photos and one blank frame for the student's shot
        fig = ('<div><div class="vr-strip">' + ''.join('<figure><img src="%s" alt="%s"><figcaption>%s</figcaption></figure>' % (img(f['img']), E(f['alt']), E(f['cap'])) for f in h['strip'])
               + '<figure class="blank"><div>?</div><figcaption>%s</figcaption></figure></div><p class="vr-stripcap">%s</p></div>' % (E(h['blank']), E(h['cap'])))
    else:
        fig = '<figure><img src="%s" alt="%s"><figcaption>%s</figcaption></figure>' % (img(h['img']), E(h['alt']), E(h['cap']))
    hook = ('<div class="wl-card"><div class="wl-look"><b>👀 What am I looking at?</b> %s</div>'
            '<div class="vr-sheet"><div class="hd"><b>%s</b><span>%s</span></div><table>%s</table>'
            '<div class="ph%s">%s'
            '<div class="vr-note"><small>Note from Opti</small>%s</div></div></div></div>'
            % (h['look'], E(h['head']), E(h['sub']), rows, ' strip' if h.get('strip') else '', fig, E(h['note'])))

    opti_img = shared('opti.png')

    def opti(text, clip):
        return ('<div class="wl-opti"><img src="%s" alt="Opti the owl"><div class="bub"><b class="who">Opti · Director</b>%s %s</div></div>'
                % (opti_img, E(text), play(clip)))

    # ---------- VR pane ----------
    B = W['badge']
    vr = ('<section class="vr-pane on" id="vr-loc" aria-label="On Location">'
          '<div class="wl-card"><div class="vr-kick">On Location · about 10 minutes</div><h3 class="vr-h3">Build %s</h3>'
          '<div class="wl-look"><b>👀 What am I looking at?</b> %s</div>'
          '<div class="vr-job"><span><span class="n">1</span>Build the scene in VR</span><i>→</i><span><span class="n">2</span>Take the shot</span><i>→</i><span><span class="n">3</span>Send it to Canvas</span></div>'
          '<div class="vr-prog" aria-live="polite"><span id="vr-prog-t">0 of %d steps done</span> · tap the box when you finish a step<div class="bar"><i id="vr-prog-b"></i></div></div>'
          '%s'
          '<div class="vr-full">⭐ <b>Full points:</b> %s</div>'
          '<label class="vr-done"><input type="checkbox" id="vr-sent"> Photo sent!</label>'
          '<div class="vr-badge" id="vr-badge" role="status"><span class="em">%s</span><div><b>%s badge earned!</b>%s</div></div>'
          '%s</div></section>'
          % (E(W['title']), W['vr']['look'], n, ''.join(steps), E(W['vr']['full']), B['emoji'], E(B['name']), E(B['line']), help_drawer(W, help_img)))

    # ---------- Studio pane ----------
    S = W['studio']
    if S.get('type') == 'fly':   # week 21: each kind of flower is one round; the flower cards come from studio.flowers
        S['pairs'] = [{'card': {'img': k['img'], 'name': k['plural'], 'alt': k['alt']}, 'ok': k['ok'], 'key': k['key'], 'kind': k['name']} for k in S['kinds']]
    if S.get('type') == 'clean':   # week 22: one round per piece of litter, plus the last round (the action that helps)
        A = S['action']
        S['pairs'] = [{'card': {'img': x['img'], 'name': x['name'], 'alt': x['alt']}, 'ok': x['why']} for x in S['items'] if x.get('trash')]
        S['pairs'].append({'card': {'img': A['img'], 'name': A['name'], 'alt': A['alt']}, 'ok': A['options'][A['right']]})
    if S.get('type') == 'spot':   # week 23: one round per polluting spot on the drawn scene
        S['pairs'] = [{'card': {'img': s['proof']['img'], 'name': s['name'], 'alt': s['proof']['alt']}, 'ok': s['msg'], 'place': s['kind'], 'placeMiss': s['miss'], 'key': s['id']} for s in S['spots'] if s.get('pollute')]
    if S.get('type') == 'count':   # week 24: two scenes to count, then the claim
        C2 = S['claim']
        S['pairs'] = [{'card': {'art': sc['art'], 'name': sc['title'], 'alt': sc['alt']}, 'ok': sc['done'], 'tag': S['unit'] % len([x for x in sc['spots'] if x.get('nest')])} for sc in S['scenes']]
        S['pairs'].append({'card': {'img': C2['img'], 'name': C2['name'], 'alt': C2['alt']}, 'ok': C2['options'][C2['right']], 'tag': C2['tag']})
    if S.get('type') == 'web':   # week 25: pin the strings, snip one species, then the claim
        C2 = S['claim']
        S['pairs'] = [{'card': {'img': r['img'], 'name': r['name'], 'alt': r['alt']}, 'ok': r['done'], 'tag': r['tag']} for r in (S['web'], S['snip'])]
        S['pairs'].append({'card': {'img': C2['img'], 'name': C2['name'], 'alt': C2['alt']}, 'ok': C2['options'][C2['right']], 'tag': C2['tag']})
    if S.get('type') == 'clue':   # week 26: one round per clue
        S['pairs'] = [{'card': {'img': c['img'], 'name': '%s %d: %s' % (S['labels'].get('clue', 'Clue'), n + 1, c['text']), 'alt': c['alt']}, 'ok': c['done'], 'tag': c['tag']} for n, c in enumerate(S['clues'])]
    # each round's card: a fossil (week 17) or a place card (week 18, key "card")
    for p in S['pairs']:
        p['fossil'] = p.get('card') or p['fossil']
    cast = S.get('type') == 'cast'   # casting call: drag a picture onto the card; the board shows the picked picture
    cousin_src = {c['key']: c['img'] for c in S.get('cousins', [])}
    frames = ''.join('<div class="vr-frame" data-f="%d">Frame %d<img src="%s" alt=""><span class="pl"></span></div>'
                     % (i, i + 1, (img(cousin_src[p['cousin']]) if S.get('frameImg') == 'cousin' else pic(p['fossil']))) for i, p in enumerate(S['pairs']))
    cousin_imgs = {c['key']: img(c['img']) for c in S.get('cousins', [])}
    fossil_imgs = [pic(p['fossil']) for p in S['pairs']]
    labels = {'done': 'All 4 frames are on the storyboard. Nice work, crew!', 'q2': 'Where did this living thing live?',
              'q1': 'Where does it go?', 'next': 'Next ▶', 'pdfTitle': 'Fossil cousins', 'cols': ['Fossil', 'Living cousin', 'Where it lived']}
    labels.update(S.get('labels', {}))
    wr = S['write']
    wframes = ''.join('<div class="vr-lead">%s</div><textarea data-w="%d" aria-label="%s" placeholder="%s"></textarea>'
                      % (E(f['lead']), i, E(f['lead']), E(f['starter'])) for i, f in enumerate(wr['frames']))
    chips = ''.join('<button type="button">%s</button>' % E(c) for c in wr['chips'])
    studio = ('<section class="vr-pane" id="vr-studio" aria-label="Studio Day">'
              '<div class="wl-card"><div class="vr-kick">%s</div><h3 class="vr-h3">%s</h3>%s'
              '<div class="wl-look"><b>👀 What am I looking at?</b> %s</div><div class="wl-do"><b>What to do:</b> %s</div>'
              '<div class="vr-board" aria-label="Storyboard">%s</div>'
              '<div id="vr-game"></div>'
              '<div id="vr-write" hidden><div class="vr-gstep">Tell Opti what you think</div>'
              '<div class="wl-look"><b>👀 What am I looking at?</b> Two sentence starters. Finish both in your own words. Tap a word to add it.</div>'
              '<div class="vr-chips">%s</div><div class="vr-frames-w">%s</div>'
              '<div class="vr-count" id="vr-count">0 of %d words</div></div>'
              '<div class="vr-stamp" id="vr-stamp">✔ %s</div>'
              '<div class="vr-full">⭐ <b>Full points:</b> %s</div>'
              '<div class="vr-gather"><b>📄 My answers</b><div style="margin:6px 0">First name: <input type="text" id="vr-name" maxlength="20" autocomplete="given-name"></div>'
              '<div class="ok-name" id="vr-name-msg"></div>'
              '<button class="vr-pdf" type="button" id="vr-pdf">📄 Download my answers (PDF)</button>'
              '<div style="font-size:15.5px">Choose <b>Save as PDF</b>, then upload that file to the Canvas assignment.</div></div>'
              '</div></section>'
              % (E(S['kicker']), E(S['title']), opti(W['opti']['studio'], 'studio'), S['look'], E(S['do']), frames, chips, wframes, wr['min'], E(W['stamp']), E(S['full'])))

    game = {
        'pairs': [{'name': p['fossil']['name'], 'alt': p['fossil']['alt'], 'img': fossil_imgs[i], 'cousin': p.get('cousin', ''), 'place': p.get('place', ''), 'bin': p.get('bin', ''), 'tag': p.get('tag', ''), 'key': p.get('key', ''), 'kind': p.get('kind', ''), 'q': p.get('q', ''), 'proof': ({'img': img(p['proof']['img']), 'alt': p['proof']['alt'], 'cap': p['proof']['cap']} if p.get('proof') else None), 'miss': p.get('miss', ''),
                   'ok': p.get('ok', ''), 'placeMiss': p.get('placeMiss', ''), 'facts': p['fossil'].get('facts', '')} for i, p in enumerate(S['pairs'])],
        'labels': labels, 'dragOpts': cast, 'framePl': S.get('framePl', S.get('frameImg', '')), 'type': S.get('type', ''), 'scenes': [{'key': sc['key'], 'title': sc['title'], 'alt': sc['alt'], 'done': sc['done'], 'img': art(sc['art']), 'spots': [{'id': x['id'], 'x': x['x'], 'y': x['y'], 'nest': bool(x.get('nest')), 'msg': x.get('msg', '')} for x in sc['spots']]} for sc in S.get('scenes', [])], 'claim': ({k: S['claim'][k] for k in ('q', 'options', 'right', 'miss')} if S.get('claim') else None), 'scene': ({'img': art(S['scene']['art']), 'alt': S['scene']['alt']} if S.get('scene') else None), 'spots': [dict({k: s.get(k) for k in ('id', 'x', 'y', 'name', 'kind', 'msg', 'miss')}, pollute=bool(s.get('pollute')), proof=({'img': img(s['proof']['img']), 'alt': s['proof']['alt'], 'cap': s['proof']['cap']} if s.get('proof') else None)) for s in S.get('spots', [])], 'items': [{'id': x['id'], 'name': x['name'], 'alt': x['alt'], 'img': img(x['img']), 'trash': bool(x.get('trash')), 'msg': x['msg']} for x in S.get('items', [])], 'action': ({k: S['action'][k] for k in ('q', 'options', 'right', 'miss')} if S.get('action') else None), 'flowers': [{'id': f['id'], 'kind': f['kind'], 'name': f['name'], 'alt': f['alt'], 'img': img(f['img'])} for f in S.get('flowers', [])], 'bins': S.get('bins', {}),
        'species': [{'id': x['id'], 'name': x['name'], 'alt': x['alt'], 'img': img(x['img']), 'x': x['x'], 'y': x['y'], 'plant': bool(x.get('plant')), 'food': x['food']} for x in S.get('species', [])],
        'links': S.get('links', []), 'web': ({'done': S['web']['done']} if S.get('web') else None), 'snipDone': S.get('snip', {}).get('done', ''),
        'snip': ({k: S['snip'][k] for k in ('gone', 'q', 'hit', 'ok', 'safe')} if S.get('snip') else None),
        'props': [{'id': x['id'], 'name': x['name'], 'alt': x['alt'], 'img': img(x['img'])} for x in S.get('props', [])],
        'clues': [{k: c[k] for k in ('text', 'out', 'gone', 'keep', 'done')} for c in S.get('clues', [])],
        'cousins': [{'key': c['key'], 'name': c['name'], 'alt': c['alt'], 'img': cousin_imgs[c['key']]} for c in S.get('cousins', [])],
        'places': S.get('places', {}), 'miss': S.get('miss', ''), 'min': wr['min'], 'frames': [f['lead'] for f in wr['frames']],
    }
    cfg = {'pre': W['id'], 'clips': clips, 'game': game, 'canvas': W['canvasName'], 'title': W['title'], 'week': wk,
           'lesson': W['lesson'], 'stamp': W['stamp'], 'video': 'assets/video/teacher/g3sci-vr-%s.mp4' % wk if repo else ''}

    paths = ('<div class="vr-paths" role="group" aria-label="Pick your path">'
             '<button class="vr-path" type="button" data-path="vr-loc" aria-pressed="true"><span class="ic">🎬</span><span><b>On Location (VR)</b><small>Earn the %s badge</small></span></button>'
             '<button class="vr-path" type="button" data-path="vr-studio" aria-pressed="false"><span class="ic">🎨</span><span><b>No headset today? Studio Day</b><small>Do it on your computer</small></span></button></div>'
             % E(B['name']))

    video = '<div class="vr-video" id="vr-video" hidden><div class="wl-card"><div class="vr-kick">From your teacher</div><video controls preload="none"></video></div></div>'

    cred = []
    for k in used:
        c = credits[k]
        cred.append('%s: <a href="%s" target="_blank" rel="noopener">%s</a>, %s (%s)'
                    % (E(k), E(c['url']), E(c['title'].replace('File:', '')), E(c['artist'] or 'unknown'), E(c['license'])))
    credits_html = '<footer class="vr-credits"><b>Photo credits</b> (Wikimedia Commons): ' + '; '.join(cred) + '. Opti the owl © Optima Academy Online.</footer>'

    header = ('<div class="header"><div class="header-brand"><div class="header-logo"><img src="%s" alt="Optima Academy"></div>'
              '<div><div class="header-org">Optima Academy Online</div><div class="header-sub">An Education Experience Company</div></div></div>'
              '<div class="header-title">%s VR: %s</div><div class="header-badge"><span>%s</span><span>Week %s · VR</span></div></div>'
              % (shared('optima-logo.png'), E(W['lesson']), E(W['title']), W['emoji'], wk))
    details = ''.join('<span>%s</span>' % E(d) for d in W['details'])
    top = ('<div class="wl-top"><div class="wl-hdr"><button class="wl-pill" id="wl-details-btn" aria-expanded="false">Activity details ▾</button></div>'
           '<div class="wl-details" id="wl-details">%s</div></div>' % details)

    if repo:
        css = ('<link rel="stylesheet" href="assets/sparkle/wf-lesson.css"><link rel="stylesheet" href="assets/sparkle/vr/vr.css">')
        js = '<script src="assets/sparkle/vr/vr.js"></script>'
    else:
        wf = open(kitfile('shared/wf-lesson.css', '../sparkle/engine/wf-lesson.css'), encoding='utf-8').read()
        css = '<style>%s</style><style>%s</style>' % (wf, open(os.path.join(KIT, 'engine', 'vr.css'), encoding='utf-8').read())
        js = '<script>%s</script>' % open(os.path.join(KIT, 'engine', 'vr.js'), encoding='utf-8').read()

    page = ('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">'
            '<!-- G3 Science VR · Week %s · built by tools/vr/build_vr.py from weeks/%s/week.json. Edit the JSON, not this file. -->'
            '<title>%s VR · %s</title>%s</head><body><div class="page-wrap">%s%s<main class="vr">%s%s%s%s%s</main>%s</div>'
            '<script>window.VR=%s;</script>%s</body></html>'
            % (wk, wk, E(W['lesson']), E(W['title']), css, header, top, hook, opti(W['opti']['brief'], 'brief'), video, paths,
               vr + studio, credits_html, json.dumps(cfg, ensure_ascii=False).replace('</', '<\\/'), js))
    os.makedirs(os.path.dirname(os.path.abspath(out_path)), exist_ok=True)
    open(out_path, 'w', encoding='utf-8').write(page)
    missing = [k for k in used if k not in credits]
    print('built', out_path, '%.1f MB' % (len(page) / 1e6), 'clips:', len(clips), 'of', len(W['voice']), 'missing credits:', missing)


def help_drawer(W, help_img):
    m = E(W['map'])
    def s(n, img, title, text):
        return '<div class="vr-hs"><img src="%s" alt="%s" loading="lazy"><div class="t"><b class="k">%s</b><b>%s</b><br>%s</div></div>' % (help_img(img), E(title), n, E(title), text)
    return ('<details class="vr-help" id="vr-help"><summary><span>🛟 Having trouble in VR?<small>Steps with pictures, and a how-to video</small></span></summary><div class="in">'
            '<div class="vid"><iframe data-src="https://www.youtube-nocookie.com/embed/slDH-WN4scY?rel=0" title="How-to video: Optima On-Demand and Canvas" allowfullscreen></iframe></div>'
            '<p style="font-size:15px">These pictures come from other maps. Your map will be <b>%s</b>, but the buttons are the same.</p>'
            '<h5>🖥️ First time only: connect Canvas (on your computer)</h5>'
            + s(1, 'vr-canvas-help-01-login.jpg', 'Log in', 'Go to <b>xr.optimaed.com</b>. Log in with your VR login.')
            + s(2, 'vr-canvas-help-02-authorize.jpg', 'Connect to Canvas', 'Click <b>Connect to Canvas</b>. Log in to Canvas, then click <b>Authorize</b>. You will see <b>Canvas connection completed</b>.')
            + s(3, 'vr-canvas-help-03-connected.jpg', 'Find our class', 'Click <b>Canvas</b> on the left and pick our class. You only do this one time.')
            + '<h5>📄 Only if the assignment has a file</h5>'
            + s(4, 'vr-canvas-help-04-upload.jpg', 'Get the file ready', 'Open the assignment. Click <b>Open in Canvas</b> to download the file. Then click <b>My Files</b> and <b>Upload File</b>.')
            + '<h5>🥽 In the headset</h5>'
            + s(5, 'vr-canvas-help-05-explore.jpg', 'Explore tab', 'Click <b>Explore</b>. Type the map name in <b>Filter environments</b>.')
            + s(6, 'vr-canvas-help-06-begin-solo.jpg', 'Begin Solo', 'Click the map, then click <b>Begin Solo</b>.')
            + s(7, 'vr-canvas-help-07-canvas.jpg', 'Read the assignment', 'Press the <b>top button on your right controller</b>. Click the <b>Canvas</b> tab and pick our assignment. Tip: point at a mint side grip and squeeze to pull the tablet to your hand.')
            + s(8, 'vr-canvas-help-08-models.jpg', 'Bring out the models', 'Click <b>Models</b>. Type the gray word in the search box. Click a model to bring it out.')
            + s(9, 'vr-canvas-help-08b-move.jpg', 'Move and resize', 'Grab a model with the <b>palm trigger</b>. Use <b>both</b> palm triggers to make it bigger or smaller.')
            + s(10, 'vr-canvas-help-09-placed.jpg', 'Need a file?', 'Click <b>Library</b>, then <b>Files</b>. Pick your file to place it.')
            + s(11, 'vr-canvas-help-10-camera.jpg', 'Take a photo', 'Click <b>Library</b>, then <b>Camera</b>. Move the tablet until your scene fits. Click <b>Take photo</b>.')
            + s(12, 'vr-canvas-help-11-choose.jpg', 'Pick your photo', 'Click the <b>Canvas</b> tab and pick our assignment. Click <b>Choose from My Files</b>, pick your newest photo, then <b>Use this file</b>.')
            + s(13, 'vr-canvas-help-12-submitted.jpg', 'Submit to Canvas', 'Click <b>Submit to Canvas</b>. Look for the green <b>Submitted</b> tag. To leave, press the <b>Meta button</b>, then click <b>Quit</b>.')
            + '<h5>🔁 Didn’t work in VR? Two other ways</h5>'
            + s(14, 'vr-canvas-help-13-portal-submit.jpg', 'Use the website', 'Go to <b>xr.optimaed.com</b> and click <b>Canvas</b>. Pick our assignment, click <b>Choose from My Files</b>, pick your photo and submit it.')
            + '<p style="font-size:15px">Your photos save to <b>My Files</b> at xr.optimaed.com. You can also download your photo there and upload it to the Canvas assignment yourself.</p>'
            '</div></details>') % m


if __name__ == '__main__':
    a = [x for x in sys.argv[1:] if not x.startswith('--')]
    build(a[0], a[1], repo='--repo' in sys.argv)
