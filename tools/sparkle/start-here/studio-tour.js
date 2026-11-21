// Records the Park Slide Studio how-to video (silent, captions from the script) against a built page.
// usage: node studio-tour.js <pageUrl> <lessons/WW-LL/studio-video.json> <outDir>
// Each line lasts max(3 s, words / 2.5 words per second) + 0.6 s until Opti's real clips exist; then pass real lengths in line.dur.
const { chromium } = require('playwright'); const fs = require('fs');
const [URL, SPEC, OUT] = process.argv.slice(2); const V = JSON.parse(fs.readFileSync(SPEC, 'utf8'));
const sleep = ms => new Promise(r => setTimeout(r, ms));
(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  let t = 1.2; V.lines.forEach(l => { const w = l.say.split(/\s+/).length; l.t = t; l.d = l.dur || Math.max(3, w / 2.5) + 0.6; t += l.d; }); const total = t + 1.5;
  const b = await chromium.launch({ args: ['--use-fake-ui-for-media-stream', '--use-fake-device-for-media-stream'] });
  const ctx = await b.newContext({ viewport: { width: 880, height: 495 }, recordVideo: { dir: OUT, size: { width: 880, height: 495 } }, permissions: ['microphone'] });
  const tPage = Date.now(); const p = await ctx.newPage();
  await p.addInitScript(seed => { try { localStorage.clear(); localStorage.setItem('wl-studio-g3sci-32-02', JSON.stringify(seed)); } catch (e) {} }, V.seed || {});
  await p.goto(URL, { waitUntil: 'domcontentloaded' }); await p.waitForFunction(() => window.OneStep && OneStep.ready, null, { timeout: 20000 });
  await p.evaluate(() => { document.querySelector('.wl-tab[data-tab="assign"]').click(); OneStep.reveal(document.getElementById('m-studio'));
    const st = document.createElement('style'); st.textContent = `#tr-cur{position:fixed;left:0;top:0;z-index:2147483647;width:26px;height:26px;pointer-events:none;transition:transform .7s cubic-bezier(.3,.1,.2,1);transform:translate(640px,360px)}
    #tr-cur:before{content:'';position:absolute;left:-12px;top:-12px;width:30px;height:30px;border-radius:50%;background:rgba(245,184,61,.45);border:2px solid #F5B83D}
    #tr-ring{position:fixed;z-index:2147483646;pointer-events:none;border:4px solid #F5B83D;border-radius:14px;box-shadow:0 0 0 4px rgba(245,184,61,.25),0 0 22px rgba(245,184,61,.7);opacity:0;transition:opacity .35s}
    #tr-cap{position:fixed;left:50%;bottom:22px;transform:translateX(-50%);z-index:2147483647;max-width:1000px;padding:10px 18px;border-radius:12px;background:rgba(0,0,0,.78);color:#fff;font:600 24px/1.3 Arial,sans-serif;text-align:center;pointer-events:none}
    #tr-cap:empty{display:none}.wl-cue,.wl-top,.os-bar{display:none!important}`;
    document.head.appendChild(st); const c = document.createElement('div'); c.id = 'tr-cur';
    c.innerHTML = '<svg width="26" height="26" viewBox="0 0 26 26" style="position:absolute;left:0;top:0"><path d="M3 2 L3 20 L8 15.5 L11.5 23 L14.5 21.6 L11 14.2 L18 14 Z" fill="#fff" stroke="#111" stroke-width="1.6" stroke-linejoin="round"/></svg>';
    const r = document.createElement('div'); r.id = 'tr-ring'; const cap = document.createElement('div'); cap.id = 'tr-cap'; document.body.append(r, c, cap);
    let target = null; window.__ring = el => { target = el; r.style.opacity = el ? 1 : 0; if (el) { const q = el.getBoundingClientRect(); c.style.transform = 'translate(' + (q.left + Math.min(q.width * .5, 60)) + 'px,' + (q.top + Math.min(q.height * .5, 40)) + 'px)'; } };
    (function tick() { if (target) { const q = target.getBoundingClientRect(), pad = 6; Object.assign(r.style, { left: (q.left - pad) + 'px', top: (q.top - pad) + 'px', width: (q.width + pad * 2 - 8) + 'px', height: (q.height + pad * 2 - 8) + 'px' }); } requestAnimationFrame(tick); })();
    window.__cap = t => { cap.textContent = t; }; });
  await sleep(600);
  const t0 = Date.now(); const at = s => sleep(Math.max(0, t0 + s * 1000 - Date.now()));
  const steps = []; V.lines.forEach(l => { steps.push([l.t, 'CAP:' + l.say]); l.act.forEach(([o, a]) => steps.push([l.t + o, a])); }); steps.sort((a, b) => a[0] - b[0]);
  for (const [s, a] of steps) { await at(s); const [, k, rest] = a.match(/^(\w+):([\s\S]*)$/);
    try {
      if (k === 'CAP') { if (process.env.BURN) await p.evaluate(t => __cap(t), rest); }
      else if (k === 'RING') await p.evaluate(sel => __ring(sel === 'null' ? null : document.querySelector(sel)), rest);
      else if (k === 'GO') { const [sel, top] = rest.split(/:(?=\d+$)/); await p.evaluate(([sel, top]) => { const e = document.querySelector(sel); if (e) window.scrollTo({ top: Math.max(0, e.getBoundingClientRect().top + scrollY - (+top || 150) * innerHeight / 720), behavior: 'smooth' }); }, [sel, top]); }
      else if (k === 'CLICK') await p.evaluate(sel => { const e = document.querySelector(sel); if (e) { const q = e.getBoundingClientRect(); document.getElementById('tr-cur').style.transform = 'translate(' + (q.left + q.width / 2) + 'px,' + (q.top + q.height / 2) + 'px)'; setTimeout(() => e.click(), 380); } }, rest);
      else if (k === 'TYPE') { const i = rest.indexOf(':'), sel = rest.slice(0, i), txt = rest.slice(i + 1); const el = await p.$(sel); if (el) { await el.focus(); await p.keyboard.press('End'); await p.keyboard.type(txt, { delay: 60 }); } }
      else if (k === 'KEY') await p.keyboard.press(rest);
    } catch (e) { console.log('step error', a.slice(0, 50), e.message.split('\n')[0]); } }
  await at(total); const path = await p.video().path(); await ctx.close();
  const vtt = ['WEBVTT', ''].concat(V.lines.map((l, i) => { const f = s => new Date(s * 1000).toISOString().slice(11, 23); return (i + 1) + '\n' + f(l.t) + ' --> ' + f(l.t + l.d - 0.2) + '\n' + l.say + '\n'; })).join('\n');
  fs.writeFileSync(OUT + '/captions.vtt', vtt);
  fs.writeFileSync(OUT + '/meta.json', JSON.stringify({ path, offset: (t0 - tPage) / 1000, total, lines: V.lines.map(l => ({ t: l.t, d: l.d, say: l.say })) }, null, 1));
  console.log(path, 'offset', (t0 - tPage) / 1000, 'total', total.toFixed(1)); await b.close();
})();
