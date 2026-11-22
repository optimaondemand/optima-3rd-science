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
  for (const [cousin, place] of pairs) {
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
