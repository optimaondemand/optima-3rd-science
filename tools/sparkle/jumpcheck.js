// Jump check: the playtest walk, plus a log of every layout shift the student didn't cause and every script scroll.
// usage: node jumpcheck.js <page.html> <width> <shotsPrefix>   (look for shifts > 0.05 where the moved element was on screen,
// i.e. a y→y line that doesn't end in →0; things pushed off the bottom of the screen are fine)
const { chromium } = require('playwright');
const [F, Wd, PRE] = [process.argv[2], +process.argv[3] || 1150, process.argv[4] || 'out/pt'];
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: Wd, height: 900 } });
  await p.addInitScript(() => { window.__log = []; window.__step = 'load';
    const desc = n => { if (!n || !n.tagName) return '?'; let d = n.tagName.toLowerCase() + (n.id ? '#' + n.id : '') + (n.className && typeof n.className === 'string' ? '.' + n.className.trim().split(/\s+/).slice(0,2).join('.') : ''); const pid = n.closest && n.closest('[id]'); return d + (pid && pid !== n ? ' in #' + pid.id : ''); };
    new PerformanceObserver(l => l.getEntries().forEach(e => { if (e.hadRecentInput) return; const src = (e.sources || []).map(s => desc(s.node) + ' dy=' + Math.round(s.currentRect.y - s.previousRect.y)).filter(x => !/dy=0$/.test(x)); if (e.value > 0.005) window.__log.push({ k: 'shift', step: window.__step, v: +e.value.toFixed(3), src: (e.sources||[]).map(s => desc(s.node) + ' y' + Math.round(s.previousRect.y) + '→' + Math.round(s.currentRect.y) + ' h' + Math.round(s.previousRect.height) + '→' + Math.round(s.currentRect.height)).slice(0,3), t: Math.round(e.startTime) }); })).observe({ type: 'layout-shift', buffered: true });
    const wrap = (o, f) => { const g = o[f]; o[f] = function (...a) { const y0 = scrollY; const r = g.apply(this, a); window.__log.push({ k: f, step: window.__step, who: this === window ? 'window' : desc(this), y0, arg: JSON.stringify(a[0]).slice(0, 60), t: Math.round(performance.now()) }); return r; }; };
    new MutationObserver(ms => ms.forEach(m => { const n = m.target; if (!n.tagName) return; if (m.type === 'attributes' && (m.attributeName === 'hidden' || m.attributeName === 'open')) window.__log.push({ k: 'attr', step: window.__step, n: desc(n), a: m.attributeName, v: n.getAttribute(m.attributeName), t: Math.round(performance.now()) }); })).observe(document, { subtree: true, attributes: true, attributeFilter: ['hidden', 'open'] });
    wrap(window, 'scrollTo'); wrap(window, 'scrollBy'); wrap(Element.prototype, 'scrollIntoView');
  });
  const errs = []; p.on('pageerror', e => errs.push('PAGEERR ' + e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  // one step at a time: open the step that holds a thing before the test touches it (the tab's own Next button is replaced by the walker's)
  for (const m of ['click', 'fill', '$', 'waitForSelector', 'hover']) { const f = p[m].bind(p); p[m] = async (sel, ...a) => {
    if (typeof sel === 'string') await p.evaluate(s => { try { const e = document.querySelector(s.split(' >> ')[0]); if (e && window.OneStep) window.OneStep.reveal(e); } catch (x) {} }, sel).catch(() => {});
    if (m === 'click' && /^\[data-go=/.test(sel)) return p.evaluate(s => document.querySelector(s).click(), sel);
    return f(sel, ...a); }; }
  await p.goto(/^https?:/.test(F) ? F : 'file://' + require('path').resolve(F)); await p.waitForTimeout(800);
  const D = await p.evaluate(() => WL_DATA);
  const el = async (sel, n) => { const e = await p.$(sel); await e.scrollIntoViewIfNeeded(); await p.waitForTimeout(150); await e.screenshot({ path: `${PRE}-${Wd}-${n}.png` }); };
  const shot = n => p.screenshot({ path: `${PRE}-${Wd}-${n}.png` });
  const toasts = () => p.$$eval('.wl-toast button', bs => bs.forEach(x => x.click()));
  const okIdx = opts => opts.findIndex(o => o.ok);
  const step = async (name, fn) => { await p.evaluate(n => window.__step = n, name).catch(()=>{}); try { await fn(); } catch (e) { errs.push('STEP ' + name + ': ' + e.message.split('\n')[0]); } };
  await step('film', async () => { await p.click('.wf-cover .wf-btn'); await p.waitForTimeout(2500); await shot('01-film'); await p.click('.wf-ctrl button:nth-child(4)', { force: true }); await p.waitForTimeout(300); await p.click('.wf-cover .go'); });
  await step('specimen', async () => { await el('#m-spec', '02-spec'); await p.click('#spec-open'); await p.waitForTimeout(300); const r = await (await p.$('#ins-img')).boundingBox();
    for (const h of D.specimen.hotspots.slice(0, 3)) { await p.mouse.click(r.x + r.width * h.x, r.y + r.height * h.y); await p.waitForTimeout(120); }
    await p.mouse.move(r.x + r.width * .5, r.y + r.height * .5); await shot('03-inspect'); await p.click('.wl-ins-x');
    await p.fill('#in-notice', 'I see a shape and some lines in it'); await p.fill('#in-wonder', 'How old is this and where did it come from?'); });
  await p.click('[data-go="lesson"]'); await p.waitForTimeout(300);
  await step('order+movie', async () => { for (const i of [0, 1, 2, 3]) { await p.click(`.wl-scard[data-i="${i}"]`); await p.click(`.wl-slot[data-slot="${i}"]`); }
    await p.waitForSelector('#fm-movie:not([hidden])', { timeout: 60000 }); const last = await p.evaluate(() => { const T = WL4.movieTimes(); return T[T.length - 1]; }); await p.waitForTimeout(last * .45); await el('#fm-movie', '04-movie-mid'); await p.waitForSelector('#order-check:not([hidden])', { timeout: 60000 }); await p.waitForTimeout(800); await el('#fm-movie', '05-movie-end');
    await p.click(`[data-choice="bone"] .wl-choice >> nth=${okIdx(D.order.check.options)}`); await toasts(); });
  await step('compare', async () => { const C = D.compare;
    for (const a of C.ask) { await p.click(`.wl-tray-spec[data-t="${a.ans}"] .wl-lit`); await p.waitForTimeout(300); await p.click('#bite-step .wl-nextstep'); await p.waitForTimeout(200); }
    // one press per round: each round puts a best match on its tray (and, if free, the other material on the other tray) until every best key is tested
    const done = new Set(), mats = C.materials.map(m => m.key), trays = C.trays.map(t => t.id);
    for (let r = 0; r < 4 && done.size < C.best.length; r++) { const plan = {}, used = new Set();
      for (const k of C.best) { if (done.has(k) || plan[k[0]] || used.has(k.slice(1))) continue; plan[k[0]] = k.slice(1); used.add(k.slice(1)); }
      for (const t of trays) if (!plan[t]) { const m = mats.find(x => !used.has(x)); if (m) { plan[t] = m; used.add(m); } }
      for (const t of trays) if (plan[t]) { await p.click(`.wl-mat[data-mat="${plan[t]}"]`); await p.click(`.wl-drop[data-drop="${t}"]`); }
      await p.click('#bite-press'); await p.waitForTimeout(800); if (r === 0) await el('#m-bite', '06-compare-test');
      for (const t of trays) if (plan[t] && C.best.includes(t + plan[t])) done.add(t + plan[t]); await p.waitForTimeout(900); }
    await p.click('#bite-step .wl-nextstep'); await p.waitForTimeout(300);
    for (const t of C.trays) { const c = C.claim[t.id]; await p.click(`.wl-chips[data-k="${t.id}f"] .wl-chip >> nth=${c.featOk}`); await p.click(`.wl-chips[data-k="${t.id}e"] .wl-chip >> nth=${c.eatOk}`); await p.waitForTimeout(150); }
    await p.waitForTimeout(1500); await toasts(); await el('#m-bite', '07-compare-done'); });
  await step('wall', async () => { const Wl = D.wall; await p.click(`#dig-predict .wl-chip[data-p="${Wl.predict.answer}"]`); await p.waitForTimeout(800);
    for (let i = 0; i < Wl.layers.length; i++) { const band = await p.$(`.wl-band[data-l="${i}"]`); await band.scrollIntoViewIfNeeded(); const bb = await band.boundingBox();
      for (let row = 0; row < 4 && !(await p.$(`.wl-band[data-l="${i}"].open`)); row++) { const y = bb.y + bb.height * (.2 + row * .2); await p.mouse.move(bb.x + 4, y); await p.mouse.down(); await p.mouse.move(bb.x + bb.width - 4, y, { steps: 18 }); await p.mouse.up(); }
      await p.waitForTimeout(500); if (i === 1) await el('#m-dig', '08-wall-card');
      await p.click(`#dig-card .wl-choice >> nth=${Wl.layers[i].ans}`); await p.waitForTimeout(400); await p.click('#dig-card .wl-nextstep'); await p.waitForTimeout(600); await toasts(); }
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
    for (const i of [1, 2, 3]) await p.fill('#in-w' + i, long);
    { const cv = await p.$('#sketch'); await cv.scrollIntoViewIfNeeded(); const bb = await cv.boundingBox(); await p.mouse.move(bb.x + 40, bb.y + 40); await p.mouse.down(); await p.mouse.move(bb.x + 200, bb.y + 90, { steps: 8 }); await p.mouse.up(); }
    await p.fill('#in-c1', long); await p.fill('#in-c2', long); await p.fill('#in-director', 'Maya'); await p.waitForTimeout(300); await toasts(); await el('#m-premiere', '12-premiere'); });
  await step('premiere', async () => { await p.click('#premiere-btn'); await p.waitForTimeout(4000); await shot('13-theater-frames'); await p.waitForTimeout(16000); await shot('14-theater-end'); await p.click('.wl-th-x'); });
  const st = await p.evaluate(() => ({ ticks: [...document.querySelectorAll('.wl-tab .ck')].map(e => e.textContent).join(''), frames: Object.keys(WL.state.frames || {}).join(','), checklist: document.querySelectorAll('#checklist li.done').length + '/' + document.querySelectorAll('#checklist li').length, sideways: document.documentElement.scrollWidth > innerWidth, mb: +(document.documentElement.outerHTML.length / 1e6).toFixed(1) }));
  console.log(JSON.stringify({ width: Wd, errors: errs, ...st })); console.log(JSON.stringify(await p.evaluate(() => window.__log), null, 0).replace(/},{/g, '},\n{'));
  await b.close(); process.exit(errs.length ? 1 : 0);
})();
