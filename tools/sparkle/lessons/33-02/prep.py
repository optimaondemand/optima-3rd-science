#!/usr/bin/env python3
"""33.02 image prep: raw/<key>.jpg -> img/<key>.jpg, raw/keymeta.json for credits."""
import json, os
from PIL import Image, ImageOps
D = os.path.dirname(os.path.abspath(__file__)); R = f'{D}/raw'; O = f'{D}/img'
meta = json.load(open(f'{R}/meta.json')); KM = {}
os.makedirs(O, exist_ok=True)
def load(k, box=None):
    im = ImageOps.exif_transpose(Image.open(f'{R}/{k}.jpg')).convert('RGB')
    if box: W, H = im.size; im = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    return im
def save(key, src=None, box=None, w=880, q=56):
    src = src or key; im = load(src, box)
    if im.size[0] > w: im = im.resize((w, round(im.size[1]*w/im.size[0])), Image.LANCZOS)
    im.save(f'{O}/{key}.jpg', quality=q, optimize=True, progressive=True); KM[key] = src
# film (16:9 crops)
save('f_air', None, (0, .03, 1, .97), 1000); save('f_fire', None, (.12, 0, .88, .5), 1000); save('f_burn', None, (0, .06, 1, .94), 1000)
save('f_regrow', None, (0, .03, 1, .97), 1000); save('f_count', None, (0, .03, 1, .97), 1000); save('f_hatch', 'hatch', (0, .06, 1, .94), 1000)
save('f_pika', None, (.04, .36, .84, .96), 1000); save('f_end', None, (0, .03, 1, .97), 1000)
# specimen
save('spec', None, None, 1500, 60)
# order + movie
save('o1'); save('o2', None, (.1, .3, .95, .8)); save('o3'); save('o4'); save('real')
# compare
save('ta'); save('tb', None, (0, .08, 1, .82)); save('hatch'); save('after2')
# wall
save('sky'); save('l1'); save('e1', None, (0, .3, 1, .82)); save('l2', None, (0, .12, 1, .88)); save('e2')
save('l3'); save('e3', None, (0, .1, 1, .9)); save('l4'); save('e4'); save('f_meadow')
# wow
save('wow', None, None, 900); save('inset', 'o3', (.05, .05, .6, .95), 500)
# evidence cards
for k in ('d1', 'd1h', 'd2', 'd2h', 'd3', 'd3h', 'd4', 'd4h', 'd5', 'd5h'): save(k)
json.dump({k: meta[s] for k, s in KM.items()}, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB')
