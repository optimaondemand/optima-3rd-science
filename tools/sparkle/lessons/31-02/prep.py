#!/usr/bin/env python3
"""31.02 image prep: raw/<src>.jpg -> img/<key>.jpg (crops), and raw/keymeta.json for credits."""
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
for key, src, box in [('f_sunset', 'sunset', (0, 0, 1, .52)), ('f_night', 'night', None), ('f_sign', 'g_sign', None), ('f_under', 'g_under', None),
                      ('f_cam', 'cam', None), ('f_fam', 'g_kitten', (0, .28, .66, .98))]:
    save(key, src, box, 1000)
save('spec', 'spec', None, 1300)
save('o1', 'g_sign2'); save('o2', 'blue', (.0, .0, 1, .8)); save('o4', 'g_kitten'); save('real', 'g_bear')
save('ta', 'culv', (.0, .2, 1, .95)); save('m_cat', 'pant', (.45, .0, 1, 1), 600); save('m_turtle', 'turt', (.25, .15, .8, .85), 600)
save('paynes', 'paynes'); save('sky', 'i75')
save('l2', 'g_sta'); save('e2', 'g_lakeo', (0, .1, 1, .85)); save('l3', 'kiss'); save('e3', 'kcanal'); save('l4', 'pep', (0, .1, 1, .9)); save('e4', 'rem')
save('d4h', 'turt')
save('wow', 'kiss2')
json.dump({k: meta[s] for k, s in KM.items()}, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB')
