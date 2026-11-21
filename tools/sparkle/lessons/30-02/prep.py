#!/usr/bin/env python3
"""30.02 image prep: raw/<src>.jpg -> img/<key>.jpg (crops, two-photo panels), and raw/keymeta.json for credits."""
import json, os
from PIL import Image, ImageOps
D = os.path.dirname(os.path.abspath(__file__)); R = f'{D}/raw'; O = f'{D}/img'
meta = json.load(open(f'{R}/meta.json'))
def load(k, box=None):
    im = ImageOps.exif_transpose(Image.open(f'{R}/{k}.jpg')).convert('RGB')
    if box: W, H = im.size; im = im.crop((int(box[0]*W), int(box[1]*H), int(box[2]*W), int(box[3]*H)))
    return im
def save(key, im, w, src):
    if im.size[0] > w: im = im.resize((w, round(im.size[1]*w/im.size[0])), Image.LANCZOS)
    im.save(f'{O}/{key}.jpg', quality=56, optimize=True, progressive=True); KM[key] = src
def fit(im, w, h):
    return ImageOps.fit(im, (w, h), Image.LANCZOS)
def pair(key, a, b, srcs, w=880, h=587):
    hw = (w - 6)//2; S = Image.new('RGB', (w, h), 'white')
    S.paste(fit(a, hw, h), (0, 0)); S.paste(fit(b, hw, h), (w - hw, 0)); save(key, S, w, srcs)
def split(key, im, side, src, w=1000, h=562):
    half = fit(im, w//2, h); S = Image.new('RGB', (w, h)); S.paste(half, (0 if side == 'L' else w//2, 0))
    if side == 'L':  # shown full-frame before the split: soft blurred photo behind, sharp mouse half feathered into it
        from PIL import ImageFilter
        S = fit(load(src[0], (.66, 0, 1, 1)), w, h).filter(ImageFilter.GaussianBlur(14))
        mask = Image.new('L', (w//2, h), 255); g = Image.new('L', (140, h)); g.putdata([int(255*(1-x/139)) for y in range(h) for x in range(140)])
        mask.paste(g, (w//2-140, 0)); S.paste(half, (0, 0), mask)
    else: S.paste(ImageOps.mirror(half), (0, 0))
    save(key, S, w, src)
KM = {}
os.makedirs(O, exist_ok=True)
F = 1000
for key, src, box in [('f_smoke', 'f_smoke', None), ('f_fire', 'f_fire', None), ('f_dig', 'f_dig', (.15, .2, .9, .85)),
                      ('f_burnt', 'x_burnt', None), ('f_sprout', 'x_sprout', None), ('f_dune', 'dune', None)]:
    save(key, load(src, box), F, [src])
split('f_pale', load('f_pale', (.12, 0, .78, 1)), 'L', ['f_pale'])
split('f_dark', load('f_dark', (.36, 0, .94, 1)), 'R', ['f_dark'])
save('spec', load('spec', (.14, .22, .86, .86)), 1300, ['spec'])
save('real', load('real', (.25, .1, .9, .75)), 880, ['real'])
save('ta', load('f_pale', (.08, .08, .82, .97)), 880, ['f_pale'])
save('tb', load('f_dark', (.12, .05, .9, 1)), 880, ['f_dark'])
save('m_sand', load('dune', (.1, .55, .9, 1)), 600, ['dune'])
save('osprey', load('osprey_c'), 880, ['osprey'])
save('sky', load('f_burrow'), 880, ['f_burrow'])
save('l1', load('l_mouse', (.12, .33, .88, .85)), 880, ['l_mouse'])
save('l2', load('l_snake'), 880, ['l_snake'])
save('l3', load('l_frog'), 880, ['l_frog'])
save('l4', load('l_tort'), 880, ['l_tort'])
save('e1', load('e_hole'), 880, ['e_hole'])
save('e3', load('x_before'), 880, ['o_after'])
save('e4', load('o_out'), 880, ['o_out'])
save('wow', load('e_racer', (.05, 0, .95, 1)), 880, ['e_racer'])
pair('d1', load('white', (.0, .05, .6, 1)), load('g_gator', (.1, .25, .75, 1)), ['white', 'g_gator'])
save('d1h', load('g_swamp'), 880, ['g_swamp'])
pair('d2', load('key2', (.42, .05, .95, 1)), load('g_deer', (.12, .1, .95, 1)), ['key2', 'g_deer'])
save('d2h', load('key1'), 880, ['key1'])
save('d3', load('g_jay'), 880, ['g_jay'])
save('d3h', load('g_scrub'), 880, ['g_scrub'])
pair('d4', load('sh1', (.05, .25, .9, .95)), load('sh2', (.05, .25, .95, .9)), ['sh1', 'sh2'])
save('d5', load('g_spoon'), 880, ['g_spoon'])
save('d5h', load('g_marsh'), 880, ['g_marsh'])
# credits: keyed by image key (second photo of a two-photo panel gets <key>_2)
used = {}
for k, srcs in KM.items():
    for j, sname in enumerate(srcs): used[k if j == 0 else f'{k}_{j+1}'] = meta['o_after' if sname.startswith('x_') else sname]
json.dump(used, open(f'{R}/keymeta.json', 'w'), indent=1, ensure_ascii=False)
print(len(KM), 'images;', sum(os.path.getsize(f'{O}/{k}.jpg') for k in KM)//1024, 'KB')
