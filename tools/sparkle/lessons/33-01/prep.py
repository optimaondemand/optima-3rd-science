#!/usr/bin/env python3
"""33.01 image prep: raw/<src>.jpg|png -> img/<key>.jpg, raw/keymeta.json for credits."""
import json, os
from PIL import Image, ImageOps
D = os.path.dirname(os.path.abspath(__file__)); R = f'{D}/raw'; O = f'{D}/img'
meta = json.load(open(f'{R}/meta.json')); KM = {}
os.makedirs(O, exist_ok=True)
def load(k, box=None):
    p = f'{R}/{k}.jpg' if os.path.exists(f'{R}/{k}.jpg') else f'{R}/{k}.png'
    im = ImageOps.exif_transpose(Image.open(p)).convert('RGB')
    if box: W, H = im.size; im = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    return im
def save(key, src, box=None, w=880, q=56):
    im = load(src, box)
    if im.size[0] > w: im = im.resize((w, round(im.size[1]*w/im.size[0])), Image.LANCZOS)
    im.save(f'{O}/{key}.jpg', quality=q, optimize=True, progressive=True); KM[key] = src
# film (16:9 where it matters)
save('f_web', 'web_0', (0, .08, 1, .92), 1000); save('f_spring', 'man_7', (0, .03, 1, .97), 1000)
save('f_thread', 'gbh_0', (0, 200/1280, 1, 1), 1000); save('f_dry', 'dry_1', (0, .12, 1, .88), 1000)
save('f_storks', 'storkf_0', None, 1000); save('f_people', 'sgr_0', (0, .05, 1, .9), 1000); save('f_end', 'sun_1', None, 1000)
# specimen
save('spec', 'pel_8', (200/1920, 230/1337, 1800/1920, 1300/1337), 1200, 60)
# order + movie
save('o1', 'crew_2'); save('o2', 'anerr_0'); save('o3', 'str_4', (.08, 0, .92, 1)); save('o4', 'apr_3', (0, .06, 1, .94)); save('real', 'oyr_0')
# compare
save('ta', 'srs_6'); save('tb', 'lev_4', (0, .25, 1, .75)); save('after', 'sci_0')
# wall
save('sky', 'srs_7'); save('l1', 'anh_0'); save('e1', 'dry_0'); save('l2', 'low_0', (0, .2, 1, .8)); save('e2', 'dry_1')
save('l3', 'gar_7'); save('e3', 'gbh_2'); save('l4', 'stork_7'); save('e4', 'stork_0')
# wow
save('wow', 'gh_7', None, 760); save('inset', 'ahe_0', None, 600)
# evidence cards
save('d1', 'ahe_1'); save('d1h', 'gbh_1', (0, .18, 1, .82)); save('d2', 'ta_0'); save('d2h', 'tb_6')
save('d3', 'mang_5'); save('d3h', 'mang_9'); save('d4', 'ich_2'); save('d4h', 'sgr_0'); save('d5', 'gt_2'); save('d5h', 'race_0', (.2, 0, .8, 1))
json.dump({k: meta[s] for k, s in KM.items()}, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB')
