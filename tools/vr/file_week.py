#!/usr/bin/env python3
"""File one recorded VR week into the repo (run from the repo root, after the clips are in Downloads).
  python3 tools/vr/file_week.py 21 '{"brief":"c3c0e551",...}' '{"step1":19,"step4":17,"step5":17}'
arg 2: clip -> first 8 hex of the sha256 of the downloaded mp3 (the browser saves them as <guid>.tmp)
arg 3: clip -> week whose identical clip is reused (0 credits)
Copies clips, rebuilds every vr-<W>.html, copies engine + week assets, appends the 8 rows to clip-log.json/csv
(never run cliplog.py build here: it drops rows), and tars a mirror for the http playtest in tools/vr/out/.
"""
import os, sys, glob, shutil, hashlib, json, subprocess, csv, io
WK = int(sys.argv[1]); want = json.loads(sys.argv[2]); reuse = json.loads(sys.argv[3])
D = os.path.expanduser('~/mnt/Downloads'); wk = 'tools/vr/weeks/%d' % WK
sha = {}
for f in glob.glob(D + '/*.tmp') + glob.glob(D + '/g3sci-vr%d-opti-*.mp3' % WK):
    if os.path.getsize(f) < 600000: sha[hashlib.sha256(open(f, 'rb').read()).hexdigest()[:8]] = f
for k, h in want.items(): shutil.copyfile(sha[h], wk + '/audio/opti-%s.mp3' % k)
for k, w in reuse.items(): shutil.copyfile('tools/vr/weeks/%d/audio/opti-%s.mp3' % (w, k), wk + '/audio/opti-%s.mp3' % k)
weeks = sorted(int(os.path.basename(p)) for p in glob.glob('tools/vr/weeks/*') if os.path.exists(p + '/audio/opti-brief.mp3'))
for w in weeks: subprocess.run(['python3', 'tools/vr/build_vr.py', 'tools/vr/weeks/%d/week.json' % w, 'vr-%d.html' % w, '--repo'], check=True, stdout=subprocess.DEVNULL)
a = 'assets/sparkle/vr-%d' % WK
os.makedirs(a + '/img', exist_ok=True); os.makedirs(a + '/audio', exist_ok=True)
for f in glob.glob(wk + '/img/*'): shutil.copy(f, a + '/img/')
for f in glob.glob(wk + '/audio/*.mp3'): shutil.copy(f, a + '/audio/')
for f in ('vr.css', 'vr.js'): shutil.copy('tools/vr/engine/' + f, 'assets/sparkle/vr/')
sys.path.insert(0, 'tools'); import cliplog
W = json.load(open(wk + '/week.json', encoding='utf8'))
raw = open('clip-log.json', encoding='utf8').read(); old = json.loads(raw); rows = []
have = {r['file'] for r in old}
for k in ['brief', 'extra', 'step1', 'step2', 'step3', 'step4', 'step5', 'studio']:
    f = a + '/audio/opti-%s.mp3' % k; b = open(f, 'rb').read(); t = W['voice'][k]
    if f in have: continue
    rows.append({"repo": "optima-3rd-science", "grade": "3", "subject": "science", "voice": "opti", "file": f, "text": t, "key": cliplog.norm(t), "chars": len(t), "kind": "speech", "script_source": wk + "/week.json", "bytes": len(b), "md5": hashlib.md5(b).hexdigest()})
open('clip-log.json', 'w', encoding='utf8', newline='').write(json.dumps(old + rows, ensure_ascii=('\\u' in raw), indent=0))
craw = open('clip-log.csv', encoding='utf8', newline='').read()
buf = io.StringIO(); wr = csv.writer(buf, lineterminator='\n')
for r in rows: wr.writerow([r[h] for h in ['repo', 'voice', 'text', 'chars', 'file', 'kind', 'script_source', 'md5']])
open('clip-log.csv', 'w', encoding='utf8', newline='').write(craw + buf.getvalue())
os.makedirs('tools/vr/out', exist_ok=True)
subprocess.run('tar cf tools/vr/out/mirror.tar ' + ' '.join('vr-%d.html assets/sparkle/vr-%d' % (w, w) for w in weeks) + ' assets/sparkle/wf-lesson.css assets/sparkle/opti.png assets/sparkle/optima-logo.png assets/sparkle/vr images/vr-canvas-help-*.jpg', shell=True, check=True)
print('filed week', WK, '| log rows +%d' % len(rows), '| pages', weeks, '| distinct clips', len({hashlib.md5(open(f,'rb').read()).hexdigest() for f in glob.glob(a + '/audio/*.mp3')}))
