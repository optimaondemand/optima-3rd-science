// Plays one G3 VR page end to end and screenshots each part.
//   node playtest_vr.js <page.html> <width> <outdir>
// Prints one line: errors, steps, badge, game, words, stamp, pdf, help images, sideways.
const { chromium } = require('playwright');
const path = require('path'), fs = require('fs');
(async () => {
  const [file, width = '1150', outdir = 'out/pt'] = process.argv.slice(2);
  const W = +width; fs.mkdirSync(outdir, { recursive: true });
  const browser = await chromium.launch();
  const ctx = await browser.newContext({ viewport: { width: W, height: 900 } });
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  page.on('console', m => { if (m.type() === 'error' && !/youtube|net::|Failed to load resource/i.test(m.text())) errors.push(m.text()); });
  await page.goto('file://' + path.resolve(file));
  await page.evaluate(() => { try { localStorage.clear(); } catch (e) {} });
  await page.reload();
  const shot = async (name, sel) => {
    const p = path.join(outdir, `${W}-${name}.png`);
    if (sel) { const el = await page.$(sel); if (el) { await el.screenshot({ path: p }); return; } }
    await page.screenshot({ path: p, fullPage: false });
  };
  await shot('01-top');
  await shot('02-hook', '.vr-sheet');
  // VR path
  const n = await page.$$eval('.vr-step', s => s.length);
  await shot('03-step1', '.vr-step[data-step="0"]');
  await shot('04-step3', '.vr-step[data-step="2"]');
  for (let i = 0; i < n; i++) await page.click(`.vr-step[data-step="${i}"] .vr-chk`);
  await page.check('#vr-sent');
  const badge = await page.$eval('#vr-badge', e => e.classList.contains('on'));
  await shot('05-badge', '#vr-loc .wl-card');
  // help drawer
  await page.click('#vr-help summary');
  await page.$$eval('#vr-help img', ims => ims.forEach(i => i.loading = 'eager'));
  await page.waitForTimeout(500);
  const helpImgs = await page.$$eval('#vr-help img', ims => ims.filter(i => i.complete && i.naturalWidth > 0).length + '/' + ims.length);
  await shot('06-help', '#vr-help');
  // Studio Day
  await page.click('.vr-path[data-path="vr-studio"]');
  await page.waitForTimeout(300);
  await shot('07-studio', '#vr-studio .wl-card');
  const pairs = await page.evaluate(() => window.VR.game.pairs.map(p => [p.cousin, p.place]));
  const keys = await page.evaluate(() => window.VR.game.cousins.map(c => c.key));
  const placeKeys = await page.evaluate(() => Object.keys(window.VR.game.places));
  const pdfTitle = await page.evaluate(() => window.VR.game.labels.pdfTitle);
  let g = 0;
  const gtype = await page.evaluate(() => window.VR.game.type);
  const bins = await page.evaluate(() => window.VR.game.pairs.map(p => p.bin));
  const binKeys = await page.evaluate(() => Object.keys(window.VR.game.bins || {}));
  if (gtype === 'season') {
    const A = await page.evaluate(() => ({ an: window.VR.game.animals.map(a => a.zone), zones: Object.keys(window.VR.game.zones), cl: [Object.keys(window.VR.game.claim.options), window.VR.game.claim.right] }));
    await shot('08-wet', '#vr-game');
    await page.click('.vr-switch button[data-v="dry"]');
    for (const [n, z] of A.an.entries()) {
      if (n === 0) { await page.click(`.vr-zone[data-z="${A.zones.find(k => k !== z)}"]`); await shot('08-miss', '#vr-game'); }
      if (n === 1) await page.dragAndDrop('#vr-fos', `.vr-zone[data-z="${z}"]`);
      else if (n === 2) await page.click(`.vr-zkey button[data-z="${z}"]`);
      else await page.click(`.vr-zone[data-z="${z}"]`);
      if (n === 2) await shot('09b-next', '#vr-game');
      g++;
    }
    await page.click(`.vr-place button[data-a="${A.cl[0].find(k => k !== A.cl[1])}"]`); await shot('09-place-miss', '#vr-game');
    await page.click(`.vr-place button[data-a="${A.cl[1]}"]`); await page.waitForTimeout(800); g++;
  } else if (gtype === 'meter') {
    const T = await page.evaluate(() => ({ things: window.VR.game.things.map(t => t.gives), meters: window.VR.game.meters.map(m => m.key) }));
    for (const [n, gives] of T.things.entries()) {
      for (const [j, m] of T.meters.entries()) {
        if (n === 1 && j === 0) await page.dragAndDrop(`.vr-mtool[data-m="${m}"]`, '#vr-mtarget');
        else await page.click(`.vr-mtool[data-m="${m}"]`);
      }
      if (n === 0) { await page.click(`.vr-place button[data-t="${T.meters.find(k => !gives.includes(k))}"]`); await page.click('#vr-check'); await shot('08-miss', '#vr-game');
        await page.click(`.vr-place button[data-t="${T.meters.find(k => !gives.includes(k))}"]`); }
      for (const k of gives) await page.click(`.vr-place button[data-t="${k}"]`);
      if (n === 1) await shot('09b-next', '#vr-game');
      await page.click('#vr-check'); await page.waitForTimeout(300); g++;
      if (n === 0) await shot('09-place-miss', '#vr-game');
    }
  } else if (gtype === 'dial') {
    const R = await page.evaluate(() => window.VR.game.rounds.map(r => [r.start, r.min, r.max, r.right]));
    const keys = await page.evaluate(() => Object.keys(window.VR.game.changes));
    for (const [n, [start, mn, mx, right]] of R.entries()) {
      const target = mn > start ? mn : mx;
      if (n === 0) { await page.click('.vr-dial-btns button[data-d="5"]'); await shot('08-miss', '#vr-game'); }
      await page.$eval('#vr-slide', (el, v) => { el.value = v; el.dispatchEvent(new Event('change')); }, target);
      if (n === 0) { await page.click(`.vr-place button[data-ch="${keys.find(k => k !== right)}"]`); await shot('09-place-miss', '#vr-game'); }
      if (n === 1) await shot('09b-next', '#vr-game');
      await page.click(`.vr-place button[data-ch="${right}"]`); await page.waitForTimeout(800); g++;
    }
  } else if (gtype === 'clue') {
    const C = await page.evaluate(() => ({ clues: window.VR.game.clues, props: window.VR.game.props.map(p => p.id) }));
    const out = C.clues.flatMap(c => c.out), keep = C.props.find(p => !out.includes(p));
    for (const [n, c] of C.clues.entries()) {
      if (n === 0) { await page.click(`.vr-prop[data-id="${keep}"]`); await shot('08-miss', '#vr-game'); }
      for (const [j, id] of c.out.entries()) {
        if (n === 1 && j === 0) await page.dragAndDrop(`.vr-prop[data-id="${id}"]`, '#vr-off');
        else await page.click(`.vr-prop[data-id="${id}"]`);
        if (n === 0 && j === 0) await shot('09-place-miss', '#vr-game');
      }
      if (n === 1) await shot('09b-next', '#vr-game');
      g++;
    }
  } else if (gtype === 'web') {
    const G = await page.evaluate(() => ({ links: window.VR.game.links, snip: window.VR.game.snip, sp: window.VR.game.species.map(x => [x.id, x.plant]), cl: [Object.keys(window.VR.game.claim.options), window.VR.game.claim.right] }));
    const card = id => `.vr-sp[data-id="${id}"]`;
    await page.click(card(G.sp.find(x => x[1])[0]));                      // a plant first: says tap an animal
    const L0 = G.links[0], wrong = G.sp.find(x => !x[1] && x[0] !== L0.from && !G.links.some(l => l.from === L0.from && l.to === x[0]))[0];
    await page.click(card(L0.from)); await page.click(card(wrong)); await shot('08-miss', '#vr-game');
    for (const [i, l] of G.links.entries()) {
      if (i === 1) {   // one string by drag
        await page.dragAndDrop(card(l.from), card(l.to));
      } else { await page.click(card(l.from)); await page.click(card(l.to)); }
      if (i === 2) await shot('09b-next', '#vr-game');
    }
    g++; await shot('09c-web', '#vr-game');
    await page.click(card(G.snip.hit[0]));                                   // before the snip: asks for scissors
    await page.dragAndDrop('#vr-snip', card(G.snip.gone));
    const safe = Object.keys(G.snip.safe)[0]; await page.click(card(safe)); await shot('09d-snip', '#vr-game');
    for (const h of G.snip.hit) await page.click(card(h));
    g++; await shot('09e-snipdone', '#vr-game');
    await page.click(`.vr-place button[data-a="${G.cl[0].find(k => k !== G.cl[1])}"]`); await shot('09-place-miss', '#vr-game');
    await page.click(`.vr-place button[data-a="${G.cl[1]}"]`); await page.waitForTimeout(800); g++;
  } else if (gtype === 'count') {
    const sc = await page.evaluate(() => window.VR.game.scenes.map(s => s.spots.map(x => [x.id, x.nest])));
    const cl = await page.evaluate(() => [Object.keys(window.VR.game.claim.options), window.VR.game.claim.right]);
    for (const spots of sc) {
      await page.click(`.vr-nest[data-id="${spots.find(x => !x[1])[0]}"]`); if (g === 0) await shot('08-miss', '#vr-game');
      for (const [id, nest] of spots) if (nest) await page.click(`.vr-nest[data-id="${id}"]`);
      g++; if (g === 1) await shot('09b-next', '#vr-game');
    }
    await page.click(`.vr-place button[data-a="${cl[0].find(k => k !== cl[1])}"]`); await shot('09-place-miss', '#vr-game');
    await page.click(`.vr-place button[data-a="${cl[1]}"]`); await page.waitForTimeout(800); g++;
  } else if (gtype === 'spot') {
    const sp = await page.evaluate(() => window.VR.game.spots.map(x => [x.id, x.pollute, x.kind]));
    await page.click(`.vr-pin[data-id="${sp.find(x => !x[1])[0]}"]`); await shot('08-miss', '#vr-game');
    for (const [id, pol, kind] of sp) if (pol) {
      await page.click(`.vr-pin[data-id="${id}"]`);
      if (g === 0) { await page.click(`.vr-place button[data-pl="${placeKeys.find(k => k !== kind)}"]`); await shot('09-place-miss', '#vr-game'); }
      await page.click(`.vr-place button[data-pl="${kind}"]`); await page.waitForTimeout(800); g++;
    }
  } else if (gtype === 'clean') {
    const it = await page.evaluate(() => window.VR.game.items.map(x => [x.id, x.trash]));
    const act = await page.evaluate(() => [Object.keys(window.VR.game.action.options), window.VR.game.action.right]);
    await page.click(`.vr-flower[data-id="${it.find(x => !x[1])[0]}"]`); await shot('08-miss', '#vr-game');
    for (const [id, trash] of it) if (trash) { await page.click(`.vr-flower[data-id="${id}"]`); g++; }
    await page.click(`.vr-place button[data-a="${act[0].find(k => k !== act[1])}"]`); await shot('09-place-miss', '#vr-game');
    await page.click(`.vr-place button[data-a="${act[1]}"]`); await page.waitForTimeout(800); g++;
  } else if (gtype === 'fly') {
    const fl = await page.evaluate(() => window.VR.game.flowers.map(f => [f.id, f.kind]));
    for (const k of [...new Set(fl.map(f => f[1]))]) {
      const mine = fl.filter(f => f[1] === k), other = fl.filter(f => f[1] !== k).pop();
      await page.click(`.vr-flower[data-id="${mine[0][0]}"]`);
      if (g === 0) { await page.click(`.vr-flower[data-id="${other[0]}"]`); await shot('08-miss', '#vr-game'); }
      await page.click(`.vr-flower[data-id="${mine[1][0]}"]`);
      if (g === 0) await shot('09-place-miss', '#vr-game');
      g++;
    }
  } else for (const [cousin, place] of pairs) {
    if (gtype === 'sort') {
      await page.click(`.vr-bin[data-b="${binKeys.find(k => k !== bins[g])}"]`);
      if (g === 0) await shot('08-miss', '#vr-game');
      await page.click(`.vr-bin[data-b="${bins[g]}"]`);
      if (!place) { if (g === 1) await shot('09b-next', '#vr-game'); await page.click('#vr-next'); g++; continue; }
    } else {
      const wrong = keys.find(k => k !== cousin);
      await page.click(`.vr-opt[data-k="${wrong}"]`);
      if (g === 0) await shot('08-miss', '#vr-game');
      await page.click(`.vr-opt[data-k="${cousin}"]`);
    }
    const otherPlace = placeKeys.find(k => k !== place);
    await page.click(`.vr-place button[data-pl="${otherPlace}"]`);
    if (g === 0) await shot('09-place-miss', '#vr-game');
    await page.click(`.vr-place button[data-pl="${place}"]`);
    await page.waitForTimeout(800);
    g++;
  }
  const lit = await page.$$eval('.vr-frame.lit', f => f.length);
  await page.fill('#vr-write textarea[data-w="0"]', 'I think this one fits its place because of what I saw in the photos today.');
  await page.fill('#vr-write textarea[data-w="1"]', 'I saw one thing that helps it there, so I am sure about my answer today.');
  await page.click('#vr-write .vr-chips button');
  const words = await page.$eval('#vr-count', e => e.textContent);
  const stamp = await page.$eval('#vr-stamp', e => e.classList.contains('on'));
  await shot('10-studio-done', '#vr-studio .wl-card');
  await page.fill('#vr-name', 'Ava');
  const [pop] = await Promise.all([page.waitForEvent('popup', { timeout: 4000 }).catch(() => null), page.click('#vr-pdf')]);
  let pdf = 'no popup';
  if (pop) { await pop.waitForLoadState(); pdf = (await pop.content()).includes(pdfTitle) ? 'ok' : 'bad'; await pop.screenshot({ path: path.join(outdir, `${W}-11-pdf.png`), fullPage: true }); }
  const sideways = await page.evaluate(() => document.documentElement.scrollWidth > window.innerWidth + 1);
  await page.screenshot({ path: path.join(outdir, `${W}-12-full.png`), fullPage: true });
  console.log(JSON.stringify({ width: W, errors, steps: n, badge, help: helpImgs, game: `${g}/${pairs.length}`, lit, words, stamp, pdf, sideways }));
  await browser.close();
})();
