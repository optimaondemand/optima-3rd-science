#!/usr/bin/env python3
"""31.01 image prep: raw/<src>.jpg -> img/<key>.jpg (crops), and raw/keymeta.json for credits."""
import json, os
from PIL import Image, ImageOps
D = os.path.dirname(os.path.abspath(__file__)); R = f'{D}/raw'; O = f'{D}/img'
meta = json.load(open(f'{R}/meta.json')); KM = {}
os.makedirs(O, exist_ok=True)
def load(k, box=None):
    im = ImageOps.exif_transpose(Image.open(f'{R}/{k}.jpg')).convert('RGB')
    if box: W, H = im.size; im = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    return im
def save(key, src, box=None, w=880):
    im = load(src, box)
    if im.size[0] > w: im = im.resize((w, round(im.size[1]*w/im.size[0])), Image.LANCZOS)
    im.save(f'{O}/{key}.jpg', quality=56, optimize=True, progressive=True); KM[key] = src
# film (1000 px)
for key, src, box in [('f_trail', 'trail', None), ('f_egret', 'egret', (0, .02, 1, .66)), ('f_py', 'py', None), ('f_rac', 'rac', None),
                      ('f_measure', 'newpy', None), ('f_marsh', 'heron', None)]:
    save(key, src, box, 1000)
save('spec', 'spec', (.2, .12, .95, .87), 1300)
save('o1', 'run'); save('o2', 'canal'); save('o3', 'lakeo', (0, .08, 1, .83)); save('o4', 'algae')
save('ta', 'pond37'); save('tb', 'run', (.0, .0, .8, 1)); save('m_plants', 'pond35', (.0, .45, .6, .8), 600)
save('bob', 'bob')
save('sky', 'modis')
save('l2', 'pyc'); save('l3', 'kendall'); save('l4', 'under')
save('e2', 'rab'); save('e3', 'saga'); save('e4', 'sign')
save('d2', 'ig'); save('d2h', 'canal'); save('d3', 'cape'); save('d3h', 'trail'); save('d4', 'sign2'); save('d4h', 'bear')
save('d5', 'lion'); save('d5h', 'diver'); save('sta', 'sta')
save('wow', 'g_river'); save('inset', 'dredge')
json.dump({k: meta[s] for k, s in KM.items()}, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB')
