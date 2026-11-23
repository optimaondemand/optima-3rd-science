#!/usr/bin/env python3
"""Rules check for one G3 VR week. Must print 0 FAIL before Bethany sees the page.
  python3 check_vr.py weeks/17/week.json [built.html]
"""
import html, json, os, re, sys

KIT = os.path.dirname(os.path.abspath(__file__))
fails, warns = [], []
def F(m): fails.append(m)
def Wn(m): warns.append(m)

wp = sys.argv[1]
wdir = os.path.dirname(os.path.abspath(wp))
W = json.load(open(wp, encoding='utf-8'))
cred = json.load(open(os.path.join(wdir, 'credits.json'), encoding='utf-8'))

# map must exist in the app's asset list (Everglades is not in the app)
assets = open(os.path.join(KIT, 'vr-assets.txt'), encoding='utf-8', errors='ignore').read() if os.path.exists(os.path.join(KIT, 'vr-assets.txt')) else ''
if W['map'] == 'The Everglades': F('map: The Everglades is not in the app')
if assets and W['map'].replace(' ', '') not in assets.replace(' ', '').replace('\n', ''): F('map not in vr-assets.txt: ' + W['map'])
if W['mapWord'].lower() not in W['map'].lower(): F('mapWord must be part of the map name')

steps = W['vr']['steps']
if len(steps) != 5: F('VR path needs exactly 5 steps (has %d)' % len(steps))
models = [m for g in W['vr']['groups'] for m in g['models']]
if not 4 <= len(models) <= 6: F('4 to 6 models (has %d)' % len(models))
if not 1 <= len(W['vr']['groups']) <= 2: F('1 or 2 model groups')
for m in models:
    if not m.get('word'): F('model without a search word: ' + m['name'])
    if assets and m['word'].replace(' ', '').lower() not in assets.replace(' ', '').replace('\n', '').lower(): F('search word not found in vr-assets: ' + m['word'])
if '@CANVAS@' not in json.dumps(W['vr']['steps']): F('a step must name the Canvas assignment (@CANVAS@)')
if not re.match(r'^\d+\.01 VR · ', W['canvasName']): F('canvasName must look like "<W>.01 VR · <Title>" (first lesson of the week)')
if not W['lesson'].endswith('.01'): F('the weekly VR goes with the first lesson of the week (W.01)')

# voice: brief, step1-5, extra, studio; no done/badge clip
need = ['brief', 'step1', 'step2', 'step3', 'step4', 'step5', 'extra', 'studio']
for c in need:
    if c not in W['voice']: F('missing voice line: ' + c)
for c, t in W['voice'].items():
    if c not in need: F('extra voice clip not allowed (no done/badge clip): ' + c)
    n = len(t.split())
    if not 8 <= n <= 25: Wn('voice %s is %d words (aim 8-25)' % (c, n))
    a = os.path.join(wdir, 'audio', 'opti-%s.mp3' % c)
    if not os.path.exists(a): Wn('audio not recorded yet: ' + c)

# studio
S = W['studio']
if S['write']['min'] < 20: F('Studio writing minimum is 20 words')
if len(S['write']['frames']) != 2: F('Studio needs exactly 2 sentence frames')
keys = {c['key'] for c in S.get('cousins', [])}
if S.get('type') == 'clean':
    if len([x for x in S['items'] if x.get('trash')]) < 3: F('clean game: at least 3 pieces of litter')
    if S['action']['right'] not in S['action']['options']: F('clean game: action.right is not one of the options')
if S.get('type') == 'fly':
    for k in S['kinds']:
        if len([f for f in S['flowers'] if f['kind'] == k['key']]) != 2: F('fly game: each kind needs exactly 2 flowers: ' + k['key'])
for p in S.get('pairs', []):
    if S.get('type') == 'sort':
        if p.get('bin') not in S.get('bins', {}): F('pair bin missing: ' + str(p.get('bin')))
        if p.get('place') and p['place'] not in S['places']: F('pair place missing: ' + p['place'])
        continue
    if p['cousin'] not in keys: F('pair cousin missing: ' + p['cousin'])
    if p['place'] not in S['places']: F('pair place missing: ' + p['place'])

# images + credits
imgs = set()
def walk(o):
    if isinstance(o, dict):
        for k, v in o.items():
            if k == 'img' and isinstance(v, str): imgs.add(v)
            walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
walk(W)
for k in imgs:
    if not os.path.exists(os.path.join(wdir, 'img', k + '.jpg')): F('image file missing: ' + k)
    if k not in cred: F('no credit for image: ' + k)
def alts(o):
    if isinstance(o, dict):
        if 'img' in o and not o.get('alt') and 'cousin' not in o: F('image without alt text: ' + str(o.get('img')))
        for v in o.values(): alts(v)
    elif isinstance(o, list):
        for v in o: alts(v)
alts(W)

# banned words + dashes in student text
txt = json.dumps({k: v for k, v in W.items() if k not in ('id',)}, ensure_ascii=False)
for bad in ['bonus', 'notebook', 'go back', 'Generate This']:
    if re.search(bad, txt, re.I): F('banned word: ' + bad)
if re.search(r' [—–] |—', txt): F('dash in student text')
if 'Everglades' in txt: Wn('mentions Everglades: check no student is sent there')

# built page: reading load per path (a student reads the shared top + ONE path). Opti's voiced bubbles don't count.
if len(sys.argv) > 2:
    s = open(sys.argv[2], encoding='utf-8').read()
    s = re.sub(r'(?s)<details class="vr-help".*?</details>', '', s)
    s = re.sub(r'(?s)<style.*?</style>|<script.*?</script>|<footer.*?</footer>|<textarea.*?</textarea>|<div class="bub">.*?</div>|<span class="vr-word">.*?</span>|<div class="vr-video".*?</video></div></div>|<div class="vr-badge".*?</div></div>|<div class="wl-details".*?</div>', '', s)
    def wc(x): return len(re.findall(r"[A-Za-z0-9’']+", html.unescape(re.sub(r'<[^>]+>', ' ', x))))
    a = s.find('<section class="vr-pane on"'); b = s.find('<section class="vr-pane" id="vr-studio"')
    top, vr, st = wc(s[:a]), wc(s[a:b]), wc(s[b:])
    print('reading words: top %d + On Location %d = %d; top + Studio Day %d = %d (game text added by the engine not counted)' % (top, vr, top + vr, st, top + st))
    for name, n in (('On Location', top + vr), ('Studio Day', top + st)):
        if n > 520: F('%s reading load %d words (limit ~450)' % (name, n))
        elif n > 450: Wn('%s reading load %d words (aim <= 450)' % (name, n))

for m in warns: print('warn:', m)
for m in fails: print('FAIL:', m)
print('%d FAIL, %d warn' % (len(fails), len(warns)))
sys.exit(1 if fails else 0)
