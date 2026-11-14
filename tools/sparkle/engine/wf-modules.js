/* Wonder Films modules (G3 science): specimen + magnifier, process mini-movie, comparison station, investigation wall +
   time elevator, evidence cards + Past Revealed, rebuild the scene, premiere. Every word and image comes from WL_DATA
   (lesson.json); this file holds NO lesson content. */
function WL4_INIT(W) {
  'use strict';
  var C = W.ctx, D = C.D, IMG = C.IMG, S = C.S, $ = C.$, $$ = C.$$, RM = C.RM;
  function el(t, c, h) { var e = document.createElement(t); if (c) e.className = c; if (h != null) e.innerHTML = h; return e; }
  function esc(t) { return String(t || '').replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function noise(ms, f, vol) { var A = C.ac(); if (!A) return; var n = A.createBufferSource(), b = A.createBuffer(1, A.sampleRate * ms / 1000, A.sampleRate), d = b.getChannelData(0);
    for (var i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / d.length); n.buffer = b; var fl = A.createBiquadFilter(); fl.type = 'bandpass'; fl.frequency.value = f || 2500; var g = A.createGain(); g.gain.value = vol || .15; n.connect(fl); fl.connect(g); g.connect(A.destination); n.start(); }
  function thud() { var A = C.ac(); if (!A) return; var o = A.createOscillator(), g = A.createGain(), t = A.currentTime; o.frequency.setValueAtTime(140, t); o.frequency.exponentialRampToValueAtTime(45, t + .3); g.gain.setValueAtTime(.4, t); g.gain.exponentialRampToValueAtTime(.001, t + .4); o.connect(g); g.connect(A.destination); o.start(); o.stop(t + .45); }

  /* ---------- frames + reel ---------- */
  S.frames = S.frames || {};
  /* time a 3rd grader needs to read a line (≈ 2.4 words/s, never under 2.6 s) */
  W.readMs = function (t) { var n = ((t || '').replace(/<[^>]+>/g, ' ').match(/[A-Za-z0-9']+/g) || []).length; return Math.max(2600, n * 420 + 600); };   /* reduced motion still needs reading time */
  /* student-paced step change: feedback stays on screen until they tap Next */
  W.next = function (host, label, fn) { var w = el('div', 'wl-nextwrap'), b = el('button', 'wl-btn wl-nextstep', label); b.type = 'button'; w.appendChild(b); host.appendChild(w);
    b.onclick = function () { w.remove(); fn(); }; setTimeout(function () { try { b.focus({ preventScroll: true }); } catch (e) {} C.reveal && C.reveal(w); }, 60); return b; };
  W.frame = function (k) { if (S.frames[k]) return; S.frames[k] = 1; C.save(); C.cheer(); var f = D.premiere.frames.filter(function (x) { return x.k === k; })[0]; C.toast('🎞️ New frame for your film: ' + (f ? f.label : k)); W.reel(); };
  W.reel = function (checkDone) {
    if (checkDone != null) W._ck = checkDone;
    var n = 0; $$('#reel .wl-frame').forEach(function (f) { var on = !!S.frames[f.dataset.f]; f.classList.toggle('locked', !on); f.classList.toggle('lit', on); if (on) n++; });
    var ready = n === D.premiere.frames.length && W._ck; var b = $('#premiere-btn'); if (b) b.disabled = !ready;
    var m = $('#reel-msg'); if (m) m.textContent = ready ? '🎬 All four frames are in and your checklist is done. Premiere your film!' : (n + ' of ' + D.premiere.frames.length + ' frames earned in the Lesson.' + (W._ck ? '' : ' Then finish the checklist.'));
    if (ready && !S.reel) { S.reel = 1; C.save(); C.markTab('assign'); }
    exhibit();
  };

  /* ---------- 1. Specimen + magnifier inspect ---------- */
  (function () {
    var HS = D.specimen.hotspots, found = S.specFound = S.specFound || [], box = $('#inspect'), view = $('.wl-ins-view'), img = $('#ins-img'), lens = $('.wl-lens'), marks = $('.wl-ins-marks'),
      zoom = $('#ins-zoom'), lensOn = true, z = 1, px = 0, py = 0, drag = null;
    img.src = IMG[D.specimen.img];
    function apply() { var r = view.getBoundingClientRect(); var maxX = r.width * (z - 1), maxY = r.height * (z - 1); px = Math.max(-maxX, Math.min(0, px)); py = Math.max(-maxY, Math.min(0, py)); img.style.transform = 'translate(' + px + 'px,' + py + 'px) scale(' + z + ')'; drawMarks(); }
    function drawMarks() { var r = view.getBoundingClientRect(); marks.querySelectorAll('.m').forEach(function (m) { m.remove(); });
      found.forEach(function (k) { var h = HS[k], m = el('div', 'm', '<i></i><b>' + h.name + '</b>'); m.style.left = (px + h.x * r.width * z) + 'px'; m.style.top = (py + h.y * r.height * z) + 'px'; marks.appendChild(m); });
      $('#ins-found').textContent = 'Found ' + Math.min(found.length, 3) + ' of 3'; }
    function frac(e) { var r = img.getBoundingClientRect(); return [(e.clientX - r.left) / r.width, (e.clientY - r.top) / r.height]; }
    function moveLens(e) { if (!lensOn) { lens.hidden = true; return; } var vr = view.getBoundingClientRect(), ir = img.getBoundingClientRect(), x = e.clientX - vr.left, y = e.clientY - vr.top, M = 2.6, lw = lens.offsetWidth / 2;
      lens.hidden = false; lens.style.left = x + 'px'; lens.style.top = y + 'px'; lens.style.backgroundImage = 'url("' + img.src + '")';
      lens.style.backgroundSize = (ir.width * M) + 'px ' + (ir.height * M) + 'px';
      lens.style.backgroundPosition = (-(e.clientX - ir.left) * M + lw) + 'px ' + (-(e.clientY - ir.top) * M + lw) + 'px'; }
    view.addEventListener('pointermove', function (e) { if (drag) { px = drag.px + e.clientX - drag.x; py = drag.py + e.clientY - drag.y; apply(); } moveLens(e); });
    view.addEventListener('pointerleave', function () { lens.hidden = true; });
    view.addEventListener('pointerdown', function (e) { view.setPointerCapture(e.pointerId); drag = { x: e.clientX, y: e.clientY, px: px, py: py, moved: false }; moveLens(e); });
    view.addEventListener('pointerup', function (e) { var moved = drag && Math.hypot(e.clientX - drag.x, e.clientY - drag.y) > 6; drag = null; if (moved) return;
      var f = frac(e), best = -1, bd = 1; HS.forEach(function (h, k) { var d = Math.hypot((f[0] - h.x) * 1.6, f[1] - h.y); if (d < bd) { bd = d; best = k; } });
      if (best > -1 && bd < D.specimen.radius) { if (found.indexOf(best) < 0) { found.push(best); C.save(); C.ding(); noise(80, 3000, .08); } drawMarks(); tip(); }
      else { var vr = view.getBoundingClientRect(), d = el('div', 'dot'); d.style.left = (e.clientX - vr.left) + 'px'; d.style.top = (e.clientY - vr.top) + 'px'; marks.appendChild(d); setTimeout(function () { d.remove(); }, 1000); $('#ins-tip').textContent = 'Nothing new there. Slide the lens slowly and look for a shape.'; } });
    function tip() { $('#ins-tip').textContent = found.length >= 3 ? '✅ Great observing! Close the viewer and write what you noticed.' : 'You found: ' + found.map(function (k) { return HS[k].name.toLowerCase(); }).join(', ') + '. Keep looking!';
      if (found.length >= 3) { $('#spec-boxes').hidden = false; $('#spec-fb').className = 'wl-fb dark ok'; $('#spec-fb').textContent = 'You found ' + found.length + ' things. Now write about one of them.'; } }
    zoom.oninput = function () { var r = view.getBoundingClientRect(), cx = r.width / 2, cy = r.height / 2, nz = +zoom.value; px = cx - (cx - px) * nz / z; py = cy - (cy - py) * nz / z; z = nz; apply(); };
    $('#ins-lens').onclick = function () { lensOn = !lensOn; this.setAttribute('aria-pressed', lensOn); this.textContent = '🔍 Magnifying lens: ' + (lensOn ? 'on' : 'off'); view.style.cursor = lensOn ? 'none' : 'grab'; };
    function open() { box.hidden = false; $('#spec-a').classList.add('lit'); setTimeout(apply, 30); tip(); if (!found.length) $('#ins-tip').textContent = 'Move the lens over it. When you spot something, tap it.'; }
    function close() { box.hidden = true; $('#spec-a').classList.remove('lit'); }
    $('#spec-open').onclick = open; $('.wl-ins-x').onclick = close; box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !box.hidden) close(); });
    $('#spec-a').onclick = open;
    if (found.length >= 3) $('#spec-boxes').hidden = false;
  })();

  /* ---------- 2. Process mini-movie (a model, driven by D.movie.beats) ---------- */
  (function () {
    var MV = D.movie, mv = $('#fm-movie'), model = $('.wl-mv-fish', mv), layers = $('.wl-mv-layers', mv), real = $('.wl-mv-real', mv), cnt = $('.wl-mv-count', mv), cap = $('.wl-mv-cap', mv), stamp = $('.wl-mv-stamp', mv), rays = $('.wl-mv-rays', mv), cv = $('.wl-mv-part', mv), ctx = cv.getContext('2d'), P = [], raf, timers = [], nb = 0;
    var BANDS = MV.bands || ['#8b7355', '#a08866', '#7d6a50', '#b19a74', '#94795a', '#6f5d45'], PCOL = MV.particleColors || ['#c8b28c', '#a8916c', '#8f7a5a'];
    function show(state) { $$('svg > g', model).forEach(function (g) { var c = g.getAttribute('class') || ''; if (/^s\d$/.test(c)) g.style.opacity = c === state ? 1 : 0; }); }
    function reset() { timers.forEach(clearTimeout); timers = []; cancelAnimationFrame(raf); P = []; nb = 0; model.style.transition = 'none'; model.style.top = MV.start || '12%'; model.style.transform = 'rotate(' + (MV.modelBox && MV.modelBox.rot != null ? MV.modelBox.rot : -4) + 'deg)'; if (MV.modelBox) { model.style.left = MV.modelBox.left; model.style.width = MV.modelBox.width; } model.style.opacity = 1; show('s1');
      layers.innerHTML = ''; layers.style.height = '0'; real.style.opacity = 0; cnt.textContent = ''; cap.textContent = ''; stamp.classList.remove('on'); rays.style.opacity = 1; mv.classList.remove('cut'); void model.offsetWidth; model.style.transition = ''; }
    function at(t, f) { timers.push(setTimeout(f, t)); }   /* captions need the same reading time with reduced motion */
    function loop() { var r = mv.getBoundingClientRect(); if (cv.width !== (r.width | 0)) { cv.width = r.width | 0; cv.height = r.height | 0; } ctx.clearRect(0, 0, cv.width, cv.height);
      P.forEach(function (p) { p.y += p.v; p.x += Math.sin(p.y / 20) * .3; if (p.v > 0 && p.y > p.stop) p.y = p.stop; if (p.v < 0 && p.y < p.stop) p.y = p.stop; ctx.fillStyle = p.c; ctx.fillRect(p.x, p.y, p.s, p.s); }); raf = requestAnimationFrame(loop); }
    function particles(o) { var r = mv.getBoundingClientRect(), up = o.dir === 'up', cols = o.colors || PCOL; for (var i = 0; i < o.n; i++) P.push({ x: Math.random() * r.width, y: up ? r.height * (1 + Math.random() * .6) : -Math.random() * r.height * .6, v: (up ? -1 : 1) * (.6 + Math.random() * 1.4), s: 1.5 + Math.random() * 2.5, c: cols[i % cols.length], stop: r.height * ((o.stop != null ? o.stop : (up ? .1 : .9)) - Math.random() * .04) }); }
    function addBand() { var k = nb++ % BANDS.length, b = el('div'); b.style.background = 'repeating-linear-gradient(0deg,' + BANDS[k] + ' 0 5px,' + BANDS[(k + 2) % BANDS.length] + ' 5px 7px)'; layers.appendChild(b); requestAnimationFrame(function () { b.style.flex = '1'; b.style.height = '18%'; }); }
    function beat(bt, skipModel) {
      if (bt.cap) cap.textContent = bt.cap;
      if (bt.clear) P = [];
      if (bt.particles) particles(bt.particles);
      if (bt.cut) { mv.classList.add('cut'); rays.style.opacity = 0; }
      if (bt.model && !skipModel) { if (bt.model.top) model.style.top = bt.model.top; if (bt.model.rot != null) model.style.transform = 'rotate(' + bt.model.rot + 'deg)'; if (bt.model.show) show(bt.model.show); if (bt.model.hide) model.style.opacity = 0; }
      if (bt.layers) { var Ly = bt.layers; if (Ly.stagger) { for (var i = 0; i < Ly.add; i++) (function (i) { at(i * Ly.stagger, function () { addBand(); layers.style.height = (Ly.from + (i + 1) * Ly.step) + '%'; }); })(i); } else { for (var j = 0; j < Ly.add; j++) addBand(); layers.style.height = Ly.height + '%'; } }
      if (bt.counter) bt.counter.forEach(function (t, i) { at(i * 380, function () { cnt.textContent = '⏳ ' + t; noise(40, 5000, .05); }); });
      if (bt.sfx === 'rumble') noise(600, 400, .1);
      if (bt.real) real.style.opacity = 1;
      if (bt.stamp) { stamp.classList.add('on'); thud(); cap.textContent = MV.endCap; cancelAnimationFrame(raf); }
    }
    W.movie = function (done) {
      mv.hidden = false; mv.classList.remove('wl-fadein'); void mv.offsetWidth; mv.classList.add('wl-fadein'); reset(); loop(); (W.ctx.reveal || function (e) { e.scrollIntoView({ block: 'nearest' }); })(mv);
      var T = W.movieTimes(); MV.beats.forEach(function (bt, i) { at(T[i], function () { beat(bt, i === 0); if (bt.stamp && done) done(); }); });
      var m0 = MV.beats[0] && MV.beats[0].model; if (m0) at(300, function () { if (m0.top) model.style.top = m0.top; if (m0.rot != null) model.style.transform = 'rotate(' + m0.rot + 'deg)'; if (m0.show) show(m0.show); });
    };
    /* beat times stretched so every caption stays up long enough to read (lesson.json times are the minimum) */
    W.movieTimes = function () { var B = MV.beats, T = [], sh = 0, last = null;
      B.forEach(function (bt, i) { if (last != null && (bt.cap || bt.stamp)) { var need = W.readMs(B[last].cap), have = bt.at - B[last].at; if (need > have) sh += need - have; }
        T[i] = bt.at + sh; if (bt.cap) last = i; }); return T; };
    W.movieStatic = function () { mv.hidden = false; reset(); MV.beats.forEach(function (bt) { if (bt.layers) for (var i = 0; i < bt.layers.add; i++) addBand(); }); model.style.opacity = 0; real.style.opacity = 1; mv.classList.add('cut'); rays.style.opacity = 0; layers.style.height = '70%'; stamp.classList.add('on'); cap.textContent = MV.endCap; };
    $('#fm-replay').onclick = function () { W.movie(); };
  })();

  /* ---------- 3. The Bite Lab ---------- */
  (function () {
    var B = D.compare, st = S.bite || { step: 0, tests: {} }, box = $('#bite-step'), mats = $('#bite-mats'), trays = $$('.wl-tray-spec');
    S.bite = st; function sv() { C.save(); }
    function trayOf(t) { return $('.wl-tray-spec[data-t="' + t + '"]'); }
    function render() {
      trays.forEach(function (t) { t.classList.remove('pick'); });
      mats.hidden = st.step !== 2;
      if (st.step === 0 || st.step === 1) { var q = B.ask[st.step]; box.innerHTML = '<div class="wl-step"><div class="n">Step ' + (st.step + 1) + ' of 4 · Predict</div><p>' + q.q + ' Tap a tray.</p></div><p class="wl-fb"></p>'; }
      if (st.step === 2) box.innerHTML = '<div class="wl-step"><div class="n">Step 3 of 4 · Test it with a model</div><p' + (B.testSay ? ' data-say="' + esc(B.testSay) + '"' : '') + '>' + B.testDo + '</p></div><div style="text-align:center"><button class="wl-btn" id="bite-press" disabled>' + B.press + '</button></div><p class="wl-fb"></p><p class="wl-starter">' + B.disclaimer + '</p>';
      if (st.step === 3) { box.innerHTML = '<div class="wl-step"><div class="n">Step 4 of 4 · Explain</div><p>Finish each sentence.</p></div>' + ['A', 'B'].map(function (t) { var c = B.claim[t]; var lab = B.trays.filter(function (x) { return x.id === t; })[0].label; return '<p style="margin:8px 0 4px"><b>' + lab + ':</b> ' + B.claimLead + ' <span class="wl-chips" style="display:inline-flex;margin:0" data-k="' + t + 'f">' + c.feat.map(function (f, i) { return '<button class="wl-chip" data-i="' + i + '">' + f + '</button>'; }).join('') + '</span>, ' + B.claimMid + ' <span class="wl-chips" style="display:inline-flex;margin:0" data-k="' + t + 'e">' + c.eat.map(function (f, i) { return '<button class="wl-chip" data-i="' + i + '">' + f + '</button>'; }).join('') + '</span>.</p>'; }).join('') + '<p class="wl-fb"></p>';
        var pick = {};
        $$('.wl-chips[data-k]', box).forEach(function (g) { $$('.wl-chip', g).forEach(function (b) { b.onclick = function () { var k = g.dataset.k, t = k[0], kind = k[1], c = B.claim[t], ok = (kind === 'f' ? c.featOk : c.eatOk) === +b.dataset.i, fb = box.querySelector('.wl-fb');
          if (!ok) { b.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = kind === 'f' ? B.missFeat.replace('{label}', B.trays.filter(function (x) { return x.id === t; })[0].label) : B.missClaim; C.oops(); return; }
          $$('.wl-chip', g).forEach(function (x) { x.classList.toggle('on', x === b); }); pick[k] = 1; fb.textContent = ''; C.ding();
          if (pick[t + 'f'] && pick[t + 'e']) { var tr = trayOf(t); tr.querySelector('.wl-curator span').innerHTML = B.curator[t]; tr.classList.add('flip'); noise(300, 1800, .1); }
          if (Object.keys(pick).length === 4) { st.step = 4; st.claims = 1; sv(); setTimeout(finish, 900); } }; }); });
      }
      if (st.step >= 4) finish();
    }
    function finish() { box.innerHTML = '<p class="wl-stampmini">CURATOR\'S NOTES COMPLETE</p><p style="margin:4px 0 0">' + B.done + '</p>'; mats.hidden = true;
      trays.forEach(function (t) { t.querySelector('.wl-curator span').innerHTML = B.curator[t.dataset.t]; t.classList.add('flip'); }); $('#teeth-end').hidden = false; W.frame('compare'); }
    trays.forEach(function (t) { t.addEventListener('click', function (e) { if (e.target.closest('.wl-drop')) return;
      if (box.querySelector('.wl-nextstep')) return;
      if (st.step === 0 || st.step === 1) { var q = B.ask[st.step], fb = box.querySelector('.wl-fb'); st.pred = st.pred || [];
        if (t.dataset.t !== q.ans) { t.classList.add('no'); setTimeout(function () { t.classList.remove('no'); }, 450); fb.className = 'wl-fb miss'; fb.textContent = q.miss; C.oops(); return; }
        t.classList.add('pick'); fb.className = 'wl-fb ok'; fb.textContent = q.ok; C.ding(); st.step++; sv(); W.next(box, st.step === 1 ? 'Next question →' : 'Next: test it →', render); }
      else if (st.step === 2 && selMat) place(selMat, t.dataset.t); }); });
    // materials: drag or tap
    var selMat = null, placed = {};
    $$('.wl-mat', mats).forEach(function (m) {
      m.addEventListener('click', function () { selMat = m.dataset.mat; $$('.wl-mat', mats).forEach(function (x) { x.classList.toggle('sel', x === m); }); });
      m.addEventListener('pointerdown', function (e) { var sx = e.clientX, sy = e.clientY, g = null;
        function mv(ev) { if (!g && Math.hypot(ev.clientX - sx, ev.clientY - sy) < 8) return; if (!g) { g = m.cloneNode(true); g.classList.add('drag'); document.body.appendChild(g); }
          g.style.left = (ev.clientX - 40) + 'px'; g.style.top = (ev.clientY - 40) + 'px'; $$('.wl-drop').forEach(function (d) { var r = d.getBoundingClientRect(); d.classList.toggle('over', ev.clientX > r.left && ev.clientX < r.right && ev.clientY > r.top && ev.clientY < r.bottom); }); }
        function up() { document.removeEventListener('pointermove', mv); document.removeEventListener('pointerup', up); if (g) { g.remove(); var hit = $$('.wl-drop').filter(function (d) { return d.classList.contains('over'); })[0]; $$('.wl-drop').forEach(function (d) { d.classList.remove('over'); }); if (hit) place(m.dataset.mat, hit.dataset.drop); } }
        document.addEventListener('pointermove', mv); document.addEventListener('pointerup', up); });
    });
    $$('.wl-drop').forEach(function (d) { d.addEventListener('click', function () { if (st.step === 2 && selMat) place(selMat, d.dataset.drop); }); });
    function place(mat, t) {
      Object.keys(placed).forEach(function (k) { if (placed[k] === mat) { delete placed[k]; $('.wl-drop[data-drop="' + k + '"]').innerHTML = 'Drop a test material here'; } });
      placed[t] = mat; var d = $('.wl-drop[data-drop="' + t + '"]'), md = B.materials.filter(function (x) { return x.key === mat; })[0]; d.innerHTML = md.img ? '<img class="wl-matimg" src="' + IMG[md.img] + '" alt="' + md.label + '" style="width:62px;height:62px;object-fit:cover;border-radius:50%">' : '<span class="wl-swatch sw-' + md.swatch + '"></span>';
      selMat = null; $$('.wl-mat', mats).forEach(function (x) { x.classList.remove('sel'); }); C.ding();
      var pb = $('#bite-press'); if (pb) { pb.disabled = !(placed.A || placed.B); pb.onclick = press; }
    }
    function press() {
      var fb = box.querySelector('.wl-fb'), msgs = [];
      ['A', 'B'].forEach(function (t) { var mat = placed[t]; if (!mat) return; var tr = trayOf(t), d = $('.wl-drop[data-drop="' + t + '"]'); tr.classList.add('press'); thud();
        setTimeout(function () { tr.classList.remove('press');
          var key = t + mat, R = B.results[key] || { text: '', fx: '' }, md = B.materials.filter(function (x) { return x.key === mat; })[0], tg = d.querySelector('.wl-matimg') || d.querySelector('.wl-swatch');
          msgs.push('<b>' + B.trays.filter(function (x) { return x.id === t; })[0].label + ' + ' + md.label.toLowerCase() + ':</b> ' + R.text);
          if (tg && R.fx) { tg.classList.add('fx-' + R.fx); if (R.fx === 'crush') { crumbs(d); noise(350, 900, .2); } if (R.fx === 'slice') noise(200, 4000, .15); }
          st.tests[key] = 1; sv(); fb.className = 'wl-fb'; fb.innerHTML = msgs.join('<br>');
          if (B.best.every(function (k) { return st.tests[k]; })) { fb.innerHTML += '<br><b style="color:#2E7D32">You tested the best match for each one.</b>'; if (st.step === 2) { st.step = 3; sv(); } if (!box.querySelector('.wl-nextstep')) W.next(box, 'Next: explain →', render); }
          else fb.innerHTML += '<br>Try swapping the materials to test the other way.'; }, 380); });
    }
    function crumbs(d) { for (var i = 0; i < 12; i++) { var c = el('span', 'wl-crumb'); c.style.left = '50%'; c.style.top = '50%'; c.style.setProperty('--dx', (Math.random() * 80 - 40) + 'px'); c.style.setProperty('--dy', (Math.random() * 40 - 10) + 'px'); d.appendChild(c); setTimeout(function (x) { x.remove(); }.bind(null, c), 900); } }
    render();
  })();

  /* ---------- 4. Excavation wall + time elevator ---------- */
  (function () {
    var WL = D.wall, L = WL.layers, st = S.digv = S.digv || { done: 0 }, bands = $$('.wl-band'), card = $('#dig-card'), car = $('.wl-elev-car'), sky = $('.wl-sky'), stops = [2, 24, 45, 66, 88];
    function sv() { C.save(); }
    if (st.pred) start(true);
    $$('#dig-predict .wl-chip').forEach(function (b) { b.onclick = function () { st.pred = b.dataset.p; sv(); $$('#dig-predict .wl-chip').forEach(function (x) { x.classList.toggle('on', x === b); }); C.ding(); setTimeout(function () { start(); }, 500); }; });
    function start(restore) {
      $('#dig-predict').innerHTML = '<p style="margin:0">' + WL.predict.mine.replace('{p}', st.pred) + '</p>'; $('#dig-wrap').hidden = false;
      bands.forEach(function (b, i) { prep(b, i); }); paint(); if (st.done >= L.length) end(true);
    }
    function paint() {
      bands.forEach(function (b, i) { b.classList.toggle('active', i === st.done && !b._open); b.classList.toggle('locked', i > st.done); if (i < st.done) open(b, i, true); });
      car.style.top = 'calc(' + stops[Math.min(st.done, L.length)] + '% - 4px)'; $$('.wl-elev span').forEach(function (s, i) { s.classList.toggle('on', i === Math.min(st.done, L.length)); });
      if (st.done === 0) { card.classList.add('in'); card.innerHTML = '<div class="wl-step"><div class="n">' + WL.unit + ' 1 of ' + L.length + '</div><p>' + WL.first + '</p></div>'; }
    }
    function prep(b, i) {
      var cv = b.querySelector('canvas'); if (b._prepped) return; b._prepped = 1;
      function size() { var r = b.getBoundingClientRect(); if (!r.width) return; cv.width = r.width; cv.height = r.height; var x = cv.getContext('2d'); x.globalCompositeOperation = 'source-over';
        var g = x.createLinearGradient(0, 0, 0, r.height); g.addColorStop(0, 'rgba(201,185,150,.96)'); g.addColorStop(1, 'rgba(170,150,115,.96)'); x.fillStyle = g; x.fillRect(0, 0, r.width, r.height);
        for (var k = 0; k < 500; k++) { x.fillStyle = 'rgba(90,70,45,' + Math.random() * .25 + ')'; x.fillRect(Math.random() * r.width, Math.random() * r.height, 2, 2); } b._area = 0; }
      setTimeout(size, 30); b._size = size;
      var down = false, last = null;
      function brush(e) { if (i !== st.done || b._open) return; var r = cv.getBoundingClientRect(), x = e.clientX - r.left, y = e.clientY - r.top, c = cv.getContext('2d');
        c.globalCompositeOperation = 'destination-out'; var gr = c.createRadialGradient(x, y, 4, x, y, 34); gr.addColorStop(0, 'rgba(0,0,0,1)'); gr.addColorStop(1, 'rgba(0,0,0,0)'); c.fillStyle = gr; c.beginPath(); c.arc(x, y, 34, 0, 7); c.fill();
        if (!last || Math.hypot(x - last[0], y - last[1]) > 14) { noise(60, 3500, .05); last = [x, y]; dust(b, e); }
        if (++b._area % 6 === 0) { var d = c.getImageData(0, 0, cv.width, cv.height).data, clear = 0, tot = 0; for (var k = 3; k < d.length; k += 64) { tot++; if (d[k] < 60) clear++; } if (clear / tot > .5) open(b, i); } }
      b.addEventListener('pointerdown', function (e) { if (i !== st.done) { if (i > st.done) { C.toast(WL.locked); } return; } down = true; b.setPointerCapture(e.pointerId); brush(e); for (var k = 0; k < 4; k++) brush({ clientX: e.clientX + (Math.random() * 60 - 30), clientY: e.clientY + (Math.random() * 30 - 15) }); });
      b.addEventListener('pointermove', function (e) { if (down) brush(e); });
      b.addEventListener('pointerup', function () { down = false; });
    }
    function dust(b, e) { if (RM) return; var r = b.getBoundingClientRect(); for (var k = 0; k < 5; k++) { var c = el('span', 'wl-crumb'); c.style.background = '#cdb98f'; c.style.left = (e.clientX - r.left) + 'px'; c.style.top = (e.clientY - r.top) + 'px'; c.style.setProperty('--dx', (Math.random() * 60 - 30) + 'px'); c.style.setProperty('--dy', (-Math.random() * 40) + 'px'); b.appendChild(c); setTimeout(function (x) { x.remove(); }.bind(null, c), 850); } }
    function open(b, i, silent) {
      if (b._open) return; b._open = 1; b.classList.add('open'); b.classList.remove('active'); var cv = b.querySelector('canvas'); cv.style.transition = 'opacity .6s'; cv.style.opacity = 0;
      if (silent) { tagBand(b, i); return; }
      C.ding(); var l = L[i];
      card.classList.remove('in'); setTimeout(function () {
        card.innerHTML = '<div class="wl-step"><div class="n">' + WL.found.replace('{n}', i + 1) + '</div><p>' + l.ask + '</p></div><img src="' + IMG[l.img] + '" alt="' + l.alt + '"><p style="font-size:15px;margin:6px 0">' + l.clue + '</p><div class="wl-choices" data-choice="digv' + i + '">' + WL.choices.map(function (c, k) { return '<button class="wl-choice" ' + (k === l.ans ? 'data-ok="' + l.ok + '"' : 'data-miss="' + (l.miss[k] || 'Read the clue again.') + '"') + '>' + c + '</button>'; }).join('') + '</div><p class="wl-fb"></p>';
        card.classList.add('in'); delete S['c-digv' + i];
        C.choices(card.querySelector('.wl-choices'), function () { tagBand(b, i); then(i);
          W.next(card, i + 1 < L.length ? 'Next ' + WL.unit.toLowerCase() + ' →' : 'See the whole wall →', function () { st.done = i + 1; sv(); paint(); if (st.done < L.length) { card.innerHTML = '<div class="wl-step"><div class="n">' + WL.unit + ' ' + (st.done + 1) + ' of ' + L.length + '</div><p>' + WL.next.replace('{n}', st.done + 1) + '</p></div>'; C.reveal && C.reveal(bands[st.done]); } else end(); }); });
      }, 250);
    }
    function tagBand(b, i) { if (!b.querySelector('.tag')) b.appendChild(el('span', 'tag', L[i].tag)); }
    function then(i) { var l = L[i], t = sky.querySelector('.then'); t.src = IMG[l.env]; t.alt = l.envAlt; sky.classList.add('past'); sky.querySelector('.wl-sky-cap').textContent = l.envCap; }
    function end(restore) {
      bands.forEach(function (b, i) { open(b, i, true); }); car.style.top = 'calc(88% - 4px)';
      $('#dig-cliff').classList.add('pull'); setTimeout(function () { $('#dig-line').classList.add('on'); }, restore ? 0 : 900);
      card.classList.add('in'); card.innerHTML = '<div class="wl-step"><div class="n">' + WL.endTitle + '</div><p>' + WL.endText + '</p></div>';
      $('#dig-after').hidden = false;
      $('#dig-pred-res').innerHTML = st.pred === WL.predict.answer ? '<span class="wl-stampmini">PREDICTION CONFIRMED</span> ' + WL.predict.confirm : '<span class="wl-stampmini" style="border-color:#B5532A;color:#B5532A">PREDICTION CHANGED</span> ' + WL.predict.change;
      if (!restore) C.cheer();
      C.choices($('[data-choice="mix"]'), function () { W.frame('wall'); });
    }
    function resz(force) { bands.forEach(function (b) { if (!b._open && b._size && (force || !b.querySelector('canvas').width)) b._size(); }); }
    window.addEventListener('resize', function () { resz(true); }); document.addEventListener('click', function () { setTimeout(function () { resz(false); }, 80); });
  })();

  /* ---------- 5. Evidence cards (detective) with Past Revealed ---------- */
  (function () {
    var DT = D.det, F = DT.items, wrap = $('#det-cards'), work = $('#det-work'), body = $('#det-chart tbody'), res = S.det = S.det || {};
    F.forEach(function (f, i) { var c = el('button', 'wl-dcard'); c.type = 'button'; c.dataset.i = i; c.innerHTML = '<img src="' + IMG[f.img] + '" alt="' + f.alt + '">' + DT.noun + ' ' + f.id; c.onclick = function () { pick(i); }; wrap.appendChild(c); });
    function predLabel(k) { var o = DT.predict.options.filter(function (x) { return x[0] === k; })[0]; return o ? o[1].replace(/^[^A-Za-z]+/, '').toLowerCase() : k; }
    function solved() { return Object.keys(res).filter(function (k) { return res[k].done; }); }
    function chart() {
      var rows = solved();
      body.innerHTML = rows.length ? rows.map(function (k) { var r = res[k], f = F[k]; return '<tr><td><b>' + f.id + '</b></td><td>' + r.clue + '</td><td>' + f.org[f.orgAns] + '</td><td>' + f.env + '</td><td>I saw ' + r.clue.toLowerCase() + ', so it was ' + f.orgShort + '.</td></tr>'; }).join('') : '<tr><td class="empty" colspan="5">Your chart fills in as you solve fossils.</td></tr>';
      for (var k = rows.length; k < DT.need; k++) body.insertAdjacentHTML('beforeend', '<tr><td class="empty">?</td><td class="empty"></td><td class="empty"></td><td class="empty"></td><td class="empty"></td></tr>');
      $$('.wl-dcard').forEach(function (c) { c.classList.toggle('done', !!(res[c.dataset.i] && res[c.dataset.i].done)); });
      $('#det-write').hidden = rows.length < DT.need; $('#rebuild').hidden = rows.length < 1; C.save(); C.gather(); C.checklist(); W.rebuildFossils && W.rebuildFossils(); exhibit();
      if (rows.length >= DT.need) W.frame('det');
    }
    function pick(i) {
      var f = F[i]; if (res[i] && res[i].done) return; if (solved().length >= DT.need) { C.toast(DT.enough); return; }
      $$('.wl-dcard').forEach(function (c) { c.classList.toggle('pick', +c.dataset.i === i); });
      var st = 0, r = res[i] = { clue: '' };
      function draw() {
        var h = '';
        if (st < 3) { h = '<div class="wl-dwork"><figure class="wl-fig" style="margin:0"><div class="wl-slab sm"><img src="' + IMG[f.img] + '" alt="' + f.alt + '"></div><figcaption>' + DT.noun + ' ' + f.id + '</figcaption></figure><div>';
          if (st === 0) h += '<div class="wl-step"><div class="n">Step 1 of 3 · Observe</div><p>What clue do you see? Tap one.</p></div><div class="wl-chips">' + f.clues.map(function (c, k) { return '<button class="wl-chip" data-k="' + k + '">' + c.t + '</button>'; }).join('') + '</div>';
          if (st === 1) h += '<div class="wl-done-row">✓ I observe: ' + r.clue + '</div><div class="wl-step"><div class="n">Step 2 of 3 · Infer</div><p>What was it?</p></div><div class="wl-chips">' + f.org.map(function (c, k) { return '<button class="wl-chip" data-k="' + k + '">' + c + '</button>'; }).join('') + '</div>';
          if (st === 2) h += '<div class="wl-done-row">✓ I observe: ' + r.clue + '</div><div class="wl-done-row">✓ It was: ' + f.org[f.orgAns] + '</div><div class="wl-step"><div class="n">Step 3 of 3 · Predict</div><p>' + DT.predict.q + '</p></div><div class="wl-chips">' + DT.predict.options.map(function (o) { return '<button class="wl-chip" data-k="' + o[0] + '">' + o[1] + '</button>'; }).join('') + '</div>';
          h += '<p class="wl-fb"></p></div></div>'; }
        else {
          var ok = r.pred === f.envAns;
          h = '<div class="wl-past" id="past"><div class="now"></div><img class="then" src="' + IMG[f.envImg] + '" alt="' + esc(f.envAlt) + '"><div class="ring"></div><div class="fos"><img src="' + IMG[f.img] + '" alt=""></div><div class="kicker">' + DT.kicker + '</div><div class="sub">' + f.envCap + '</div><div class="cap">' + f.reveal + '</div></div>' +
            '<p style="margin:6px 0">' + (ok ? '<span class="wl-stampmini">PREDICTION CONFIRMED</span> You pictured ' + predLabel(r.pred) + '. The evidence agrees.' : '<span class="wl-stampmini" style="border-color:#B5532A;color:#B5532A">EVIDENCE CHANGED MY IDEA</span> You pictured ' + predLabel(r.pred) + '. ' + f.envMiss.replace(/\s*Try again\.$/, '')) + '</p><div class="wl-bts"><b>🎬 Behind the scenes</b>' + f.bts + '</div>';
        }
        work.innerHTML = h; var fb = work.querySelector('.wl-fb');
        if (st === 3) { setTimeout(function () { var p = $('#past'); p && p.classList.add('on'); noise(900, 600, .12); }, 120); r.done = 1; chart(); return; }
        $$('.wl-chip', work).forEach(function (c) { c.onclick = function () {
          if (st === 0) { var cl = f.clues[+c.dataset.k]; if (!cl.ok) { c.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = cl.miss; C.oops(); return; } r.clue = cl.t; st = 1; C.ding(); draw(); }
          else if (st === 1) { if (+c.dataset.k !== f.orgAns) { c.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = f.orgMiss; C.oops(); return; } st = 2; C.ding(); draw(); }
          else if (st === 2) { r.pred = c.dataset.k; st = 3; C.ding(); draw(); } }; });
      }
      draw(); work.scrollIntoView({ block: 'nearest' });
    }
    W.detSolved = solved; chart();
  })();

  /* ---------- 6. Rebuild the ancient scene (optional) ---------- */
  (function () {
    var R = D.rebuild, stage = $('#rb-stage'), steps = $('#rb-steps'), cur = null, envSel = null, lifeSel = {};
    W.rebuildFossils = function () { var box = $('#rb-fossils'); box.innerHTML = W.detSolved().map(function (k) { return '<button class="wl-chip" data-k="' + k + '">' + D.det.noun + ' ' + D.det.items[k].id + '</button>'; }).join('');
      $$('.wl-chip', box).forEach(function (b) { b.onclick = function () { $$('.wl-chip', box).forEach(function (x) { x.classList.toggle('on', x === b); }); begin(+b.dataset.k); }; }); };
    function begin(k) { cur = D.det.items[k]; envSel = null; lifeSel = {}; stage.querySelector('.wl-rb-fossil').innerHTML = '<img src="' + IMG[cur.img] + '" alt="">'; stage.querySelector('.wl-rb-bg').style.backgroundImage = ''; stage.querySelector('.wl-rb-water').style.height = '0'; stage.querySelector('.wl-rb-life').innerHTML = '';
      stage.querySelector('.wl-rb-cap').textContent = D.det.noun + ' ' + cur.id + ': ' + cur.org[cur.orgAns] + '. What place does it point to?';
      steps.innerHTML = '<div class="wl-step"><div class="n">Step 1 of 3</div><p>Pick the place.</p></div><div class="wl-chips">' + R.envs.map(function (e, i) { return '<button class="wl-chip" data-i="' + i + '">' + e.name + '</button>'; }).join('') + '</div><p class="wl-fb"></p>';
      $$('.wl-chip', steps).forEach(function (b) { b.onclick = function () { var e = R.envs[+b.dataset.i], fb = steps.querySelector('.wl-fb');
        if (e.key !== cur.rebuildEnv) { b.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = R.missPrefix + cur.envMiss.replace(/\s*Try again\.$/, ''); C.oops(); return; }
        envSel = e; C.ding(); stage.querySelector('.wl-rb-bg').style.backgroundImage = 'url("' + IMG[e.key === 'water' ? cur.envImg : e.img] + '")'; if (e.key === 'water') setTimeout(function () { stage.querySelector('.wl-rb-water').style.height = '100%'; }, 300); stage.querySelector('.wl-rb-cap').textContent = e.cap; life(); }; }); }
    function life() { steps.innerHTML = '<div class="wl-step"><div class="n">Step 2 of 3</div><p>Pick the living things that belong in this place. Tap each one.</p></div><div class="wl-chips">' + R.life.map(function (l, i) { return '<button class="wl-chip" data-i="' + i + '">' + l.name + '</button>'; }).join('') + '</div><p class="wl-fb"></p>';
      $$('.wl-chip', steps).forEach(function (b) { b.onclick = function () { var l = R.life[+b.dataset.i], fb = steps.querySelector('.wl-fb'); if (lifeSel[b.dataset.i]) return;
        if (l.env !== envSel.key) { b.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = l.miss; C.oops(); return; }
        lifeSel[b.dataset.i] = 1; b.classList.add('on'); C.ding(); var im = el('img'); im.src = IMG[l.img]; im.alt = l.name; stage.querySelector('.wl-rb-life').appendChild(im);
        var need = R.life.filter(function (x) { return x.env === envSel.key; }).length; if (Object.keys(lifeSel).length === need) why(); }; }); }
    function why() { steps.innerHTML = '<div class="wl-step"><div class="n">Step 3 of 3</div><p>What evidence made you choose this place?</p></div><div class="wl-in"><textarea id="in-rebuild" data-min="6" placeholder="' + esc(D.rebuild.whyStart || 'I chose this because the fossil…') + '"></textarea></div>';
      var ta = $('#in-rebuild'); ta.value = S['t-in-rebuild'] || ''; ta.oninput = function () { S['t-in-rebuild'] = ta.value; C.save(); }; C.cheer(); stage.querySelector('.wl-rb-cap').textContent = '🌍 Scene rebuilt from your evidence.'; }
    var dr = $('#rebuild'); dr.addEventListener('toggle', function () { if (dr.open) W.rebuildFossils(); });
  })();

  /* ---------- 7. Premiere ---------- */
  var exPick = null;
  function exhibit() {
    if (!$('#exhibit')) return; var sol = W.detSolved ? W.detSolved() : [];
    if (exPick == null || sol.indexOf(String(exPick)) < 0) exPick = S.exPick != null && sol.indexOf(String(S.exPick)) > -1 ? S.exPick : sol[0];
    $('#ex-pick').innerHTML = sol.map(function (k) { return '<button class="wl-chip' + (String(k) === String(exPick) ? ' on' : '') + '" data-k="' + k + '">' + D.det.items[k].id + '</button>'; }).join('');
    $$('#ex-pick .wl-chip').forEach(function (b) { b.onclick = function () { exPick = b.dataset.k; S.exPick = exPick; C.save(); exhibit(); }; });
    var f = exPick != null ? D.det.items[exPick] : null, r = f ? S.det[exPick] : null;
    $('#ex-img').src = f ? IMG[f.img] : IMG[D.specimen.img]; $('#ex-num').textContent = f ? D.det.noun + ' ' + f.id : 'My specimen';
    $('#ex-obs').textContent = C.val('in-w1').trim() || (r ? 'I saw ' + r.clue.toLowerCase() + '.' : '');
    $('#ex-org').textContent = f ? f.org[f.orgAns] : '';
    $('#ex-ev').textContent = C.val('in-w3').trim() || C.val('in-det').trim();
    $('#ex-tells').textContent = f ? f.reveal : '';
    $('#ex-sketch').innerHTML = S.sketch ? '<b style="display:block;font:800 12px Georgia,serif;letter-spacing:.12em;text-transform:uppercase;color:#7a5520">Scientist\'s reconstruction drawing</b><img src="' + S.sketch + '" alt="My drawing">' : '';
  }
  W.exhibit = exhibit;
  document.addEventListener('input', function (e) { if (e.target.matches && e.target.matches('textarea')) exhibit(); });
  var BAD = /(stupid|dumb|idiot|poop|butt|hate|kill|sex|damn|hell|crap|fart|ugly)/i;
  (function () {
    var nm = $('#in-director'); nm.value = S.director || '';
    nm.oninput = function () { var v = nm.value.trim(); if (BAD.test(v)) { $('#dir-fb').className = 'wl-fb miss'; $('#dir-fb').textContent = 'Please use a kind name, like your first name.'; S.director = ''; } else { $('#dir-fb').textContent = ''; S.director = v.replace(/[^A-Za-z' -]/g, '').slice(0, 20); } C.save(); };
    var th = $('#theater'), scr = $('.wl-th-screen'), timers = [];
    function at(t, f) { timers.push(setTimeout(f, t)); }
    function proj() { noise(2400, 1200, .05); }
    $('#premiere-btn').onclick = function () {
      exhibit(); th.hidden = false; scr.innerHTML = ''; timers.forEach(clearTimeout); timers = []; proj();
      var cnt = el('div', 'wl-th-count'); scr.appendChild(cnt);
      [3, 2, 1].forEach(function (n, i) { at(i * 900, function () { cnt.textContent = n; var a = 0, iv = setInterval(function () { a += 24; cnt.style.setProperty('--a', a + 'deg'); if (a >= 360) clearInterval(iv); }, 55); C.ding(); }); });
      var frames = D.premiere.frames.map(function (f) { return [f.k, IMG[f.k === 'det' ? D.det.items[exPick || 0].img : f.img], f.cap]; });
      at(2800, function () { cnt.remove(); });
      var ft = [2800]; frames.forEach(function (fr) { ft.push(ft[ft.length - 1] + Math.max(2300, W.readMs(fr[2]))); });
      frames.forEach(function (fr, i) { at(ft[i], function () { var d = el('div', 'wl-th-frame', '<img src="' + fr[1] + '" alt=""><p>' + fr[2] + '</p>'); scr.appendChild(d); requestAnimationFrame(function () { d.classList.add('on'); }); noise(120, 2200, .12); at(ft[i + 1] - ft[i] - 300, function () { d.classList.remove('on'); }); }); });
      at(ft[frames.length], function () {
        var f = D.det.items[exPick || 0], d = el('div', 'wl-th-frame', '<div class="wl-th-final"><img src="' + IMG[f.img] + '" alt=""><div><p style="text-align:left;margin:0 0 8px;color:#e3b04b;font-size:.85em;letter-spacing:.12em;text-transform:uppercase">' + D.premiere.storyKicker + '</p><p style="text-align:left" id="th-type"></p></div></div>');
        scr.appendChild(d); requestAnimationFrame(function () { d.classList.add('on'); });
        var txt = ($('#ex-obs').textContent + ' I think it was ' + (D.det.items[exPick || 0].orgShort || 'a living thing') + '. ' + $('#ex-tells').textContent).trim(), k = 0, tp = $('#th-type');
        var iv = setInterval(function () { tp.textContent = txt.slice(0, ++k); if (k >= txt.length) clearInterval(iv); }, RM ? 1 : 28); timers.push(iv);
        at(RM ? 300 : Math.min(5200, txt.length * 28 + 800), function () { var dir = el('div', 'wl-th-dir', 'DIRECTED BY: ' + D.premiere.director + (S.director ? '<br>' + esc(S.director).toUpperCase() : '')); scr.appendChild(dir); requestAnimationFrame(function () { dir.classList.add('on'); }); C.cheer(); });
      });
    };
    function close() { th.hidden = true; timers.forEach(function (t) { clearTimeout(t); clearInterval(t); }); scr.innerHTML = ''; }
    $('.wl-th-x').onclick = close; document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !th.hidden) close(); });
  })();

  W.after = function () { W.reel(window.__ck); exhibit(); };
}
