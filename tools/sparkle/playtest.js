// Generic Wonder Films play test: walks EVERY module of ANY lesson using the answers in WL_DATA.
// usage: node playtest.js <page.html> <width> <shotsPrefix>
const { chromium } = require('playwright');
const [F, Wd, PRE] = [process.argv[2], +process.argv[3] || 1150, process.argv[4] || 'out/pt'];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: Wd, height: 900 } });
  const errs = []; p.on('pageerror', e => errs.push('PAGEERR ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  await p.goto(/^https?:/.test(F) ? F : 'file://' + require('path').resolve(F)); await p.waitForTimeout(800);
  const D = await p.evaluate(() => WL_DATA);
  const el = async (sel, n) => { const e = await p.$(sel); await e.scrollIntoViewIfNeeded(); await p.waitForTimeout(150); await e.screenshot({ path: `${PRE}-${Wd}-${n}.png` }); };
  const shot = n => p.screenshot({ path: `${PRE}-${Wd}-${n}.png` });
  const toasts = () => p.$$eval('.wl-toast button', bs => bs.forEach(x => x.click()));
  const okIdx = opts => opts.findIndex(o => o.ok);
  const step = async (name, fn) => { try { await fn(); } catch (e) { errs.push('STEP ' + name + ': ' + e.message.split('\n')[0]); } };
  await step('film', async () => { await p.click('.wf-cover .wf-btn'); await p.waitForTimeout(2500); await shot('01-film'); await p.click('.wf-ctrl button:nth-child(4)', { force: true }); await p.waitForTimeout(300); await p.click('.wf-cover .go'); });
  await step('specimen', async () => { await el('#m-spec', '02-spec'); await p.click('#spec-open'); await p.waitForTimeout(300); const r = await (await p.$('#ins-img')).boundingBox();
    for (const h of D.specimen.hotspots.slice(0, 3)) { await p.mouse.click(r.x + r.width * h.x, r.y + r.height * h.y); await p.waitForTimeout(120); }
    await p.mouse.move(r.x + r.width * .5, r.y + r.height * .5); await shot('03-inspect'); await p.click('.wl-ins-x');
    await p.fill('#in-notice', 'I see a shape and some lines in it'); await p.fill('#in-wonder', 'How old is this and where did it come from?'); });
  await p.click('[data-go="lesson"]'); await p.waitForTimeout(300);
  await step('order+movie', async () => { for (const i of [0, 1, 2, 3]) { await p.click(`.wl-scard[data-i="${i}"]`); await p.click(`.wl-slot[data-slot="${i}"]`); }
    const last = Math.max(...D.movie.beats.map(x => x.at)); await p.waitForTimeout(5300 + last * .45); await el('#fm-movie', '04-movie-mid'); await p.waitForTimeout(last * .55 + 1500); await el('#fm-movie', '05-movie-end');
    await p.click(`[data-choice="bone"] .wl-choice >> nth=${okIdx(D.order.check.options)}`); await toasts(); });
  await step('compare', async () => { const C = D.compare;
    for (const a of C.ask) { await p.click(`.wl-tray-spec[data-t="${a.ans}"] .wl-lit`); await p.waitForTimeout(1500); }
    // one press per round: each round puts a best match on its tray (and, if free, the other material on the other tray) until every best key is tested
    const done = new Set(), mats = C.materials.map(m => m.key), trays = C.trays.map(t => t.id);
    for (let r = 0; r < 4 && done.size < C.best.length; r++) { const plan = {}, used = new Set();
      for (const k of C.best) { if (done.has(k) || plan[k[0]] || used.has(k.slice(1))) continue; plan[k[0]] = k.slice(1); used.add(k.slice(1)); }
      for (const t of trays) if (!plan[t]) { const m = mats.find(x => !used.has(x)); if (m) { plan[t] = m; used.add(m); } }
      for (const t of trays) if (plan[t]) { await p.click(`.wl-mat[data-mat="${plan[t]}"]`); await p.click(`.wl-drop[data-drop="${t}"]`); }
      await p.click('#bite-press'); await p.waitForTimeout(800); if (r === 0) await el('#m-bite', '06-compare-test');
      for (const t of trays) if (plan[t] && C.best.includes(t + plan[t])) done.add(t + plan[t]); await p.waitForTimeout(done.size < C.best.length ? 900 : 2600); }
    for (const t of C.trays) { const c = C.claim[t.id]; await p.click(`.wl-chips[data-k="${t.id}f"] .wl-chip >> nth=${c.featOk}`); await p.click(`.wl-chips[data-k="${t.id}e"] .wl-chip >> nth=${c.eatOk}`); await p.waitForTimeout(150); }
    await p.waitForTimeout(1500); await toasts(); await el('#m-bite', '07-compare-done'); });
  await step('wall', async () => { const Wl = D.wall; await p.click(`#dig-predict .wl-chip[data-p="${Wl.predict.answer}"]`); await p.waitForTimeout(800);
    for (let i = 0; i < Wl.layers.length; i++) { const band = await p.$(`.wl-band[data-l="${i}"]`); await band.scrollIntoViewIfNeeded(); const bb = await band.boundingBox();
      for (let row = 0; row < 4 && !(await p.$(`.wl-band[data-l="${i}"].open`)); row++) { const y = bb.y + bb.height * (.2 + row * .2); await p.mouse.move(bb.x + 4, y); await p.mouse.down(); await p.mouse.move(bb.x + bb.width - 4, y, { steps: 18 }); await p.mouse.up(); }
      await p.waitForTimeout(500); if (i === 1) await el('#m-dig', '08-wall-card');
      await p.click(`#dig-card .wl-choice >> nth=${Wl.layers[i].ans}`); await p.waitForTimeout(2500); await toasts(); }
    await p.waitForTimeout(1500); await el('#m-dig', '09-wall-end'); await p.click(`[data-choice="mix"] .wl-choice >> nth=${okIdx(Wl.mix.options)}`); await toasts(); });
  await step('detective', async () => { const T = D.det; for (let i = 0; i < T.need; i++) { const f = T.items[i];
      await p.click(`.wl-dcard[data-i="${i}"]`); await p.click(`#det-work .wl-chip[data-k="${f.clues.findIndex(c => c.ok)}"]`); await p.click(`#det-work .wl-chip[data-k="${f.orgAns}"]`); await p.click(`#det-work .wl-chip[data-k="${f.envAns}"]`);
      await p.waitForTimeout(2200); if (i === 0) await el('#det-work', '10-past-revealed'); await toasts(); }
    await p.fill('#in-det', 'It may show a living thing because I saw clear clues in it. The place may have been very different long ago.'); });
  await step('rebuild', async () => { await p.click('#rebuild summary'); await p.click('#rb-fossils .wl-chip >> nth=0'); const f = D.det.items[0];
    await p.click(`#rb-steps .wl-chip >> nth=${D.rebuild.envs.findIndex(e => e.key === f.rebuildEnv)}`); await p.waitForTimeout(400);
    for (const [i, l] of D.rebuild.life.entries()) if (l.env === f.rebuildEnv) await p.click(`#rb-steps .wl-chip >> nth=${i}`);
    await p.waitForTimeout(1500); await el('#rebuild', '11-rebuild'); });
  await toasts(); await p.click('[data-go="check"]'); await p.waitForTimeout(300);
  await step('quiz', async () => { for (const q of D.quiz) { await p.click(`#m-quiz .wl-q.on .wl-choice >> nth=${okIdx(q.options)}`); await p.click('#quiz-next'); await p.waitForTimeout(120); } });
  await p.click('[data-go="assign"]'); await p.waitForTimeout(300);
  const long = 'I think this because the ' + D.assign.write.vocab.join(' and the ') + ' all show what happened long ago in this place, so that is my answer.';
  await step('assign', async () => { for (const sec of [D.assign.partA, D.assign.partB]) for (const it of sec.items) { const key = (sec === D.assign.partA ? 'a' : 'b') + it.n;
      if (it.type === 'choice') await p.click(`[data-choice="${key}"] .wl-choice >> nth=${okIdx(it.options)}`); else await p.fill('#in-' + key, long); }
    for (const i of [1, 2, 3]) await p.fill('#in-w' + i, long); await p.fill('#in-director', 'Maya'); await p.waitForTimeout(300); await toasts(); await el('#m-premiere', '12-premiere'); });
  await step('premiere', async () => { await p.click('#premiere-btn'); await p.waitForTimeout(4000); await shot('13-theater-frames'); await p.waitForTimeout(16000); await shot('14-theater-end'); await p.click('.wl-th-x'); });
  const st = await p.evaluate(() => ({ ticks: [...document.querySelectorAll('.wl-tab .ck')].map(e => e.textContent).join(''), frames: Object.keys(WL.state.frames || {}).join(','), checklist: document.querySelectorAll('#checklist li.done').length + '/' + document.querySelectorAll('#checklist li').length, sideways: document.documentElement.scrollWidth > innerWidth, mb: +(document.documentElement.outerHTML.length / 1e6).toFixed(1) }));
  console.log(JSON.stringify({ width: Wd, errors: errs, ...st }));
  await b.close(); process.exit(errs.length ? 1 : 0);
})();
