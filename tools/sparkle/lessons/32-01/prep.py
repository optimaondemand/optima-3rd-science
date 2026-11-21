#!/usr/bin/env python3
"""32.01 image prep: raw/<src>.jpg -> img/<key>.jpg (crops, stamp/poster frames for the split shots), raw/keymeta.json for credits."""
import json, os
from PIL import Image, ImageOps, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); R = f'{D}/raw'; O = f'{D}/img'
meta = json.load(open(f'{R}/meta.json')); KM = {}
os.makedirs(O, exist_ok=True)
def load(k, box=None):
    im = ImageOps.exif_transpose(Image.open(f'{R}/{k}.jpg')).convert('RGB')
    if box: W, H = im.size; im = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    return im
def put(key, im, w, src):
    if im.size[0] > w: im = im.resize((w, round(im.size[1]*w/im.size[0])), Image.LANCZOS)
    im.save(f'{O}/{key}.jpg', quality=56, optimize=True, progressive=True); KM[key] = src
def save(key, src, box=None, w=880): put(key, load(src, box), w, src)
def framed(key, src, box=None, bg=(28, 24, 20), cx=250, mw=300, mh=360):
    """an archive print (stamp or poster) standing in the left half of a dark 16:9 frame"""
    S = Image.new('RGB', (1000, 562), bg); a = load(src, box); a.thumbnail((mw, mh), Image.LANCZOS)
    sh = Image.new('RGB', (a.size[0] + 16, a.size[1] + 16), (10, 8, 6)).filter(ImageFilter.GaussianBlur(4))
    x, y = cx - a.size[0]//2, 281 - a.size[1]//2; S.paste(sh, (x + 6, y + 8)); S.paste(a, (x, y)); put(key, S, 1000, src)
framed('f_stamp', 'stamp'); framed('f_poster', 'poster')
p = load('see', (.09, .085, .91, .895)); p.thumbnail((700, 720), Image.LANCZOS); bgc = p.resize((1, 1)).getpixel((0, 0))
C = Image.new('RGB', (1000, 750), tuple(int(v * .55) for v in bgc)); C.paste(p, ((1000 - p.size[0])//2, (750 - p.size[1])//2)); put('f_see', C, 1000, 'see')
for key, src, box in [('f_ever', 'g_river', None), ('f_old', 'old', None), ('f_tunnel', 'tunnel', None),
                      ('f_ranger', 'ranger', None), ('f_valley', 'valley', None)]:
    save(key, src, box, 1000)
save('spec', 'cone', (.2, .1, .8, .97), 1100)
save('o1', 'elk2'); save('o2', 'wolfrel'); save('o3', 'elk', (0, .1, 1, .8)); save('o4', 'willow'); save('real', 'wolf')
save('ta', 'bison3'); save('tb', 'deer'); save('m_snow', 'bison2', (.0, .0, .45, .45), 600); save('m_valley', 'valley', (.0, .55, .7, 1), 600)
save('after', 'ranger2')
save('sky', 'elcap'); save('l1', 'g_river'); save('e1', 'g_gator'); save('l2', 'tunnel'); save('e2', 'seq'); save('l3', 'old'); save('e3', 'bison', (0, .1, 1, .75))
save('l4', 'smoky2'); save('e4', 'sal')
save('d1', 'g_gator'); save('d2', 'g_spoon'); save('d3', 'seq'); save('d4', 'bison3'); save('d5', 'wolf')
save('d1h', 'bison2'); save('d2h', 'elcap'); save('d3h', 'g_prairie'); save('d4h', 'smoky'); save('d5h', 'deer2')
save('wow', 'sal'); save('inset', 'bear')
json.dump({k: meta[s] for k, s in KM.items()}, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB')
