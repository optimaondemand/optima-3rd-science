#!/usr/bin/env python3
"""32.02 image prep: raw/<src>.jpg -> img/<key>.jpg (archive canvases, crops, the Slide Studio photo bank pb_*), raw/keymeta.json for credits."""
import json, os
from PIL import Image, ImageOps, ImageFilter
D = os.path.dirname(os.path.abspath(__file__)); R = f'{D}/raw'; O = f'{D}/img'
meta = json.load(open(f'{R}/meta.json')); KM = {}
os.makedirs(O, exist_ok=True)
def load(k, box=None):
    im = ImageOps.exif_transpose(Image.open(f'{R}/{k}.jpg')).convert('RGB')
    if box: W, H = im.size; im = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    return im
def put(key, im, w, src, q=56):
    if im.size[0] > w: im = im.resize((w, round(im.size[1]*w/im.size[0])), Image.LANCZOS)
    im.save(f'{O}/{key}.jpg', quality=q, optimize=True, progressive=True); KM[key] = src
def save(key, src, box=None, w=880): put(key, load(src, box), w, src)
def canvas(key, src, box=None, mw=700, mh=720, dark=.5):
    """an archive print (poster, old photo) centered on a 1000x750 canvas so the archive frame shows all of it"""
    p = load(src, box); p.thumbnail((mw, mh), Image.LANCZOS); bgc = p.resize((1, 1)).getpixel((0, 0))
    C = Image.new('RGB', (1000, 750), tuple(int(v * dark) for v in bgc)); C.paste(p, ((1000 - p.size[0])//2, (750 - p.size[1])//2)); put(key, C, 1000, src)
# film
canvas('f_rns', 'f_rns', (.04, .03, .96, .97)); canvas('f_walk', 'f_walk', None, 520, 720, .35)
for key in ('f_exhibit', 'f_talk', 'f_read', 'f_end'): save(key, key, None, 1000)
# warm-up specimen: a glass lantern slide, cropped to 5:4
s = load('spec'); W, H = s.size; s = s.crop((0, (H - W*4//5)//2, W, (H - W*4//5)//2 + W*4//5)); put('spec', s, 1100, 'spec')
# order + movie
save('o1', 'o1'); save('o2', 'o2'); save('o3', 'o3', None, 880); save('o4', 'o4'); save('real', 'real')
# comparison (the Visitor Test)
save('ta', 'ta', None, 600); save('tb', 'tb', (0, 0, 1, .82), 700); save('m_vis', 'm_vis', None, 600); save('m_read', 'm_read', (.05, 0, .95, 1), 600); save('after', 'after', None, 500)
# wall (the Criteria Hunt)
save('sky', 'ysky'); save('l1', 'g_storm'); save('e1', 'g_river'); save('l2', 'g_elk'); save('e2', 'wolfsnow'); save('l3', 'py1'); save('e3', 'g_newpy')
save('l4', 'peri', (0, .05, 1, .8)); save('e4', 'elcap2')
save('wow', 'wow'); save('inset', 'inset', None, 500)
# evidence cards
save('d1', 'g_gator'); save('d1h', 'g_hole'); save('d2', 'lyell'); save('d2h', 'ywinter'); save('d3', 'lamar'); save('d3h', 'wolfsnow')
save('d4', 'py2'); save('d4h', 'g_racc'); save('d5', 'burn'); save('d5h', 'g_seq')
save('ex_sal', 'g_sal', None, 700)   # the studio's example slide (Great Smoky Mountains, a park students don't present)
# Slide Studio photo bank: all public domain (Bethany: "a library of several image options from public domain")
BANK = ['g_river', 'g_prairie', 'g_storm', 'g_peri', 'g_gator', 'g_spoon', 'g_wading', 'g_panther', 'g_deer', 'g_py', 'g_bridge', 'g_sta',
        'yfalls', 'hdome', 'ysky', 'ywinter', 'lyell', 'ybear', 'toad', 'sal2', 'peri', 'oak', 'mfire', 'elcap2',
        'prism', 'lamar', 'lfalls', 'g_bison', 'g_elk', 'wolfsnow', 'grizz', 'beaver', 'cutt', 'ltrout', 'fire88', 'g_wolfrel']
for b in BANK:
    lic = meta[b]['license'].lower(); assert 'public domain' in lic or 'cc0' in lic or 'no restrictions' in lic, (b, lic)
    put('pb_' + b, load(b), 1000, b, 58); t = load(b); t.thumbnail((260, 260)); put('pt_' + b, t, 260, b, 60)   # pt_ = small picker thumbnail
json.dump({k: meta[s] for k, s in KM.items()}, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB;', 'bank', sum(os.path.getsize(f'{O}/pb_{b}.jpg') for b in BANK)//1024, 'KB + thumbs', sum(os.path.getsize(f'{O}/pt_{b}.jpg') for b in BANK)//1024, 'KB')
