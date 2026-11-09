#!/usr/bin/env python3
"""Build the inline mockup of a sparkled G3 science lesson (film + lesson layer).
usage: build_mock.py <film.json> <lesson-data.json> <lesson-body.html> <out.html>"""
import json, base64, sys, pathlib, html, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
film = json.loads(pathlib.Path(sys.argv[1]).read_text())
data = json.loads(pathlib.Path(sys.argv[2]).read_text())
body = pathlib.Path(sys.argv[3]).read_text()
out = pathlib.Path(sys.argv[4])
film['startTarget'] = '.wl-ican'

def uri(p, mime):
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()

keys = {s.get('img') for s in film['shots'] if s.get('img')} | {film['poster'], film.get('endPoster', film['poster'])}
keys |= set(re.findall(r'\{\{(\w+)\}\}', body)) - {'credits', 'opti', 'optima_logo', 'FISH_SVG'}
keys |= {data['spec']['img'], 'leaf', 'phareodus', 'tooth_sharp', 'gc_wall'} | {l['env'] for l in data['dig']} | {f['envImg'] for f in data['det']} | {e['img'] for e in data['rebuild']['envs']} | {l['img'] for l in data['rebuild']['life']}
for blob in (data.get('order', {}).get('scenes', []), data.get('dig', []), data.get('det', [])):
    keys |= {x['img'] for x in blob}
img = {k: uri(ROOT / f'build/{k}.jpg', 'image/jpeg') for k in sorted(k for k in keys if k)}
img['opti'] = uri(ROOT / 'build/opti.png', 'image/png')
img['optima_logo'] = uri(ROOT / 'build/optima-logo.png', 'image/png')
img['music'] = uri(ROOT / 'build/music.mp3', 'audio/mpeg')
for c in film.get('captions', []):
    v = ROOT / f"build/{c.get('voice')}.mp3"
    if c.get('voice') and v.exists(): img[c['voice']] = uri(v, 'audio/mpeg')

cred = {c['key']: c for c in json.loads((ROOT / 'img/credits.json').read_text())}
alias = {'school_s': 'school', 'dig_s': 'dig', 'layers_close': 'layers', 'env_forest': 'env_ferns2', 'env_lake': 'env_lake2', 'leaf': 'leaf1', 'grp_shell': 'det_shell', 'grp_fish': 'school', 'grp_ferns': 'env_ferns2'}
lines, seen = [], set()
for k in sorted(keys):
    c = cred.get(alias.get(k, k))
    if not c or c['url'] in seen: continue
    seen.add(c['url'])
    t = c['title'].rsplit('.', 1)[0]; t = t if len(t) < 80 else t[:77] + '…'
    a = re.sub(r'\s+', ' ', c['artist'] or 'unknown').strip()[:60]
    lines.append(f'<li><a href="{html.escape(c["url"])}" target="_blank" rel="noopener">{html.escape(t)}</a>, {html.escape(a)}, {html.escape(c["license"])}</li>')
lines.append('<li>Music: Smetana, <i>Vltava</i> (The Moldau), Musopen Symphony, public domain (Wikimedia Commons).</li>')
lines.append('<li>Opti the owl: Optima Academy. Sound effects are made by the page. Some photo colors were adjusted for the film.</li>')
film['credits'] = [re.sub(r'^<li>|</li>$', '', l) for l in lines]

def fill(m):
    k = m.group(1)
    if k == 'credits': return '\n'.join(lines)
    if k == 'FISH_SVG': return (ROOT / 'src/fish-model.svg').read_text()
    return img[k]
body = re.sub(r'\{\{(\w+)\}\}', fill, body)

css = (ROOT / 'src/wf-film.css').read_text() + '\n' + (ROOT / 'src/wf-lesson.css').read_text()
js_film = (ROOT / 'src/wf-film.js').read_text()
js_les = (ROOT / 'src/wf-lesson-v4.js').read_text() + '\n' + (ROOT / 'src/wf-lesson.js').read_text()
page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lesson 17.01: What Can Fossils Tell Us? · Wonder Films mockup</title>
<style>{css}
.wf-credits{{display:none}}</style></head><body>
{body}
<script>window.WF_IMG={json.dumps(img)};window.WF_DATA={json.dumps(film)};window.WL_DATA={json.dumps(data)};</script>
<script>{js_film}</script>
<script>{js_les}</script>
</body></html>'''
out.write_text(page)
print(out, round(out.stat().st_size / 1e6, 2), 'MB')
