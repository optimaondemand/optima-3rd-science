#!/usr/bin/env python3
"""Build an inline preview of the Wonder Films opener for one lesson.
usage: build.py <data.json> <out.html>"""
import json, base64, sys, pathlib, html
ROOT = pathlib.Path(__file__).resolve().parent.parent
data = json.loads(pathlib.Path(sys.argv[1]).read_text())
out = pathlib.Path(sys.argv[2])
css = (ROOT / 'src/wf-film.css').read_text()
js = (ROOT / 'src/wf-film.js').read_text()

def uri(p, mime):
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()

img = {}
keys = {s.get('img') for s in data['shots'] if s.get('img')} | {data['poster'], data.get('endPoster', data['poster'])}
for k in sorted(k for k in keys if k):
    img[k] = uri(ROOT / f'build/{k}.jpg', 'image/jpeg')
img['music'] = uri(ROOT / 'build/music.mp3', 'audio/mpeg')
for c in data.get('captions', []):          # voice clips plug in when they exist
    v = ROOT / f"build/{c.get('voice')}.mp3"
    if c.get('voice') and v.exists():
        img[c['voice']] = uri(v, 'audio/mpeg')

cred = json.loads((ROOT / 'img/credits.json').read_text())
used = {k for k in keys}
lines = []
for c in cred:
    if c['key'] in used:
        t = c['title'].rsplit('.', 1)[0]
        t = t if len(t) < 70 else t[:67] + '…'
        lines.append(f'<a href="{html.escape(c["url"])}" target="_blank" rel="noopener">{html.escape(t)}</a>, {html.escape(c["artist"] or "unknown")}, {html.escape(c["license"])}')
lines.append('Music: Smetana, <i>Vltava</i> (The Moldau), Musopen Symphony, public domain (<a href="https://commons.wikimedia.org/wiki/File:Smetana_-_M%C3%A1_Vlast_-_Vltava_(Musopen_Symphony).flac" target="_blank" rel="noopener">Wikimedia Commons</a>)')
lines.append('Sound effects made in the browser. Some colors were adjusted for the film.')
data['credits'] = lines

page = f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Wonder Films · {html.escape(data["title"])} (preview)</title>
<style>
body{{margin:0;background:#f4efe4;font-family:system-ui,Segoe UI,Arial,sans-serif;color:#222}}
.hdr{{background:#1f3b2d;color:#fff;padding:12px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap}}
.hdr b{{font-size:18px}} .hdr span{{opacity:.8;font-size:13px}}
main{{padding:16px}}
.note{{max-width:1100px;margin:0 auto 14px;background:#fff8e6;border:1px dashed #d6b35c;border-radius:10px;padding:10px 14px;font-size:14px}}
.stub{{max-width:1100px;margin:18px auto;background:#fff;border-radius:12px;padding:18px;border:1px solid #e3dccb}}
.stub h3{{margin:0 0 6px}}
{css}
</style></head><body>
<div class="hdr"><b>🦴 Lesson 17.01: What Can Fossils Tell Us?</b><span>Q3 · Unit 6 · NGSS 3-LS4-1</span></div>
<main>
<div class="note"><b>Preview for Bethany.</b> This is the Wonder Films opener that sits at the very top of the Warm-Up tab. Captions show Opti's script; his voice plugs in once you OK the words (one take each).</div>
<div id="wf-film"></div>
<section class="stub" id="tab-vocab"><h3>🌅 Warm-Up</h3><p>(The lesson starts here. "Start the lesson" lands on this spot.)</p></section>
</main>
<script>window.WF_IMG={json.dumps(img)};window.WF_DATA={json.dumps(data)};</script>
<script>{js}</script>
</body></html>'''
out.write_text(page)
print(out, round(out.stat().st_size / 1e6, 2), 'MB')
