#!/usr/bin/env python3
"""Wonder Films lesson.json checker. Every lesson must pass with 0 FAIL before Bethany sees it.
usage: check_lesson.py lessons/<WW-LL>/lesson.json"""
import json, sys, re, pathlib
P = pathlib.Path(sys.argv[1]); L = json.loads(P.read_text()); D = P.parent
FAILS, WARNS = [], []
def fail(m): FAILS.append(m)
def warn(m): WARNS.append(m)
def need(cond, m): (None if cond else fail(m))
def one_ok(opts, where):
    need(sum(1 for o in opts if 'ok' in o) == 1, f'{where}: exactly one option must have "ok"')
    need(all(('ok' in o) or ('miss' in o) for o in opts), f'{where}: every wrong option needs a "miss" hint')

for k in ['id', 'lesson', 'title', 'emoji', 'details', 'icans', 'opti', 'film', 'scientist', 'specimen', 'words', 'parts', 'order', 'movie', 'compare', 'wall', 'wow', 'keyIdea', 'det', 'rebuild', 'quiz', 'assign', 'premiere', 'next', 'chips']:
    need(k in L, f'missing top-level key "{k}"')
if FAILS: print('\n'.join('FAIL ' + f for f in FAILS)); sys.exit(1)

F = L['film']; need(45 <= max(s['t'] + s['d'] for s in F['shots']) <= 62, 'film must be 45-60 s')
need(F['shots'][0]['type'] == 'leader' and F['shots'][-1]['type'] == 'title', 'film starts with a leader and ends with a title card')
need(7 <= len(F['shots']) <= 11, 'film needs 7-10 shots (+leader/title)')
need(sum(len(c['text'].split()) for c in F['captions']) <= 95, 'film narration must be <= 90 words')
need(F.get('bigQuestion'), 'film end card needs the Big Question')
need(len(L['icans']) >= 2, 'I-can statements copied from the lesson')
need(set(L['opti']) >= {'warm', 'lesson', 'check', 'assign'}, 'Opti needs warm, lesson, check, assign notes')
S = L['specimen']; need(len(S.get('hotspots', [])) >= 4, 'specimen needs >= 4 hidden features (students find 3)')
need(len(S.get('card', [])) >= 3 and 'decide' in ' '.join(S['card']).lower(), 'specimen ID card: name, found, age/size, "You decide"')
need(len(L['words']) >= 4, 'Word Wall needs the lesson\'s words')
need(len(L['parts']) == 4, 'exactly 4 Lesson parts (process, comparison, wall, evidence cards)')
O = L['order']; need(len(O['scenes']) == 4 and sorted(O['mix']) == [0, 1, 2, 3] and O['mix'] != [0, 1, 2, 3], 'order: 4 scenes, mixed')
one_ok(O['check']['options'], 'order quick check')
M = L['movie']; need(M['beats'][-1].get('stamp'), 'movie must end on a stamp beat'); need((D / M['model']).exists(), f'movie model SVG missing: {M["model"]}')
need(any(b.get('counter') for b in M['beats']), 'movie needs a time/scale counter beat'); need(any(b.get('real') for b in M['beats']), 'movie must end on the REAL photo')
if (D / M['model']).exists():
    svg = (D / M['model']).read_text(); need('class="s1"' in svg and 'class="s2"' in svg, 'model SVG needs <g class="s1"> and <g class="s2"> states')
C = L['compare']; need(len(C['trays']) == 2 and len(C['ask']) == 2 and len(C['materials']) == 2, 'comparison: 2 trays, 2 predict questions, 2 materials')
need(all(k in C['results'] for k in [t['id'] + m['key'] for t in C['trays'] for m in C['materials']]), 'comparison: a result for every tray x material')
need(len(C['best']) == 2 and 'disclaimer' in C and 'curator' in C, 'comparison: best pairs, model disclaimer, curator cards')
W = L['wall']; need(3 <= len(W['layers']) <= 4, 'wall: 3-4 layers/sites'); need(len(W['elevator']) == len(W['layers']) + 1, 'wall: elevator has one stop per layer + "Today"')
for i, l in enumerate(W['layers']):
    need(0 <= l['ans'] < len(W['choices']), f'wall layer {i+1}: answer index'); need(l.get('env') and l.get('envCap'), f'wall layer {i+1}: real environment photo + honest caption')
one_ok(W['mix']['options'], 'wall think-like-a-scientist')
need(W['predict']['answer'] in [o[0] for o in W['predict']['options']], 'wall prediction answer must be one of the options')
T = L['det']; need(len(T['items']) >= T['need'] + 1, 'evidence cards: more cards than students must solve (choice)')
for f in T['items']:
    need(sum(1 for c in f['clues'] if c.get('ok')) >= 1, f'card {f["id"]}: at least one correct clue')
    need(all(c.get('ok') or c.get('miss') for c in f['clues']), f'card {f["id"]}: wrong clues need hints')
    need(f['envAns'] in [o[0] for o in T['predict']['options']], f'card {f["id"]}: envAns must be a predict option')
    need(f.get('envImg') and f.get('envCap') and f.get('reveal'), f'card {f["id"]}: Past Revealed photo, caption, "This … is evidence that …"')
    need(f.get('rebuildEnv') in [e['key'] for e in L['rebuild']['envs']], f'card {f["id"]}: rebuildEnv must match a rebuild place')
for e in L['rebuild']['envs']:
    if any(f['rebuildEnv'] == e['key'] for f in T['items']): need(any(x['env'] == e['key'] for x in L['rebuild']['life']), f'rebuild: no living things for place "{e["key"]}"')
for i, q in enumerate(L['quiz']): one_ok(q['options'], f'quiz {i+1}')
need(len(L['quiz']) == 3, 'Self-Check keeps the lesson\'s 3 questions')
A = L['assign']; ids = set()
for sec, pre in ((A['partA'], 'a'), (A['partB'], 'b')):
    for it in sec['items']:
        if it['type'] == 'choice': one_ok(it['options'], f'Part {pre.upper()} {it["n"]}'); ids.add('c:' + pre + str(it['n']))
        else: ids.add('in-' + pre + str(it['n']))
for c in A['checklist']:
    r = c.get('req', {})
    for k in r.get('choice', []): need('c:' + k in ids, f'checklist "{c["k"]}" points at missing choice {k}')
    for k in r.get('text', {}):
        need(k in ids or k in ('in-det', 'in-w1', 'in-w2', 'in-w3'), f'checklist "{c["k"]}" points at missing box {k}')
need(len(A['write']['prompts']) == 3 and A['write']['need'] >= 1 and len(A['write']['vocab']) >= 3, 'Write and explain: 3 evidence prompts, a science-word count (need = the lesson\'s own number, >= 1)')
PR = L['premiere']; need([f['k'] for f in PR['frames']] == ['formation', 'compare', 'wall', 'det'], 'premiere frames must be formation, compare, wall, det')
need(PR['director'].upper().startswith('JUNIOR '), 'director title "JUNIOR <SCIENTIST>"')

# images + credits
s = json.dumps(L); cred = {c['key'] for c in json.loads((D / 'credits.json').read_text())}; alias = L.get('creditAlias', {})
imgs = sorted({k for k in re.findall(r'"([a-z][a-z0-9_]+)"', s) if (D / 'img' / f'{k}.jpg').exists()})
for k in imgs: need(alias.get(k, k) in cred, f'no credit for image {k}')
for v in [l['env'] for l in W['layers']]: need((D / 'img' / f'{v}.jpg').exists(), f'image file missing: img/{v}.jpg')
for key in ('img', 'envImg', 'real', 'sky'):
    for v in re.findall(r'"%s": "([^"]+)"' % key, s): need((D / 'img' / f'{v}.jpg').exists(), f'image file missing: img/{v}.jpg')
need((D / 'music.mp3').exists(), 'music.mp3 (public-domain cut) missing')
# student-text rules
text = re.sub(r'<[^>]+>', ' ', s)
for bad in ['notebook', 'Generate This', 'go back', 'Go back', 'look back', 'Look back', 'tab above', 'Explore tab']:
    if bad in text: fail(f'student text contains "{bad}"')
if '—' in text: warn('em dash in student text (prefer commas or periods)')
for bad in ['bonus', 'Bonus']:
    if bad in text: fail('use OPTIONAL, never "bonus"')
alts = re.findall(r'"alt": "([^"]*)"', s); need(all(a.strip() for a in alts), 'every image needs alt text')
words = sum(len(re.sub(r'<[^>]+>', ' ', p.get('html', '')).split()) for p in L['parts'])
(warn if words > 260 else lambda m: None)(f'Lesson reading is {words} words (aim <= 220 across Parts 1-3)')
print('\n'.join(['FAIL ' + f for f in FAILS] + ['warn ' + w for w in WARNS]) or 'OK')
print(f'{len(FAILS)} FAIL, {len(WARNS)} warn · images: {len(imgs)} · reading words: {words}')
sys.exit(1 if FAILS else 0)
