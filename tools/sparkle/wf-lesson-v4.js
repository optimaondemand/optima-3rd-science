/* Wonder Films v4 modules: museum specimens + magnifier, formation movie, Bite Lab, excavation wall + time elevator,
   Past Revealed, Rebuild the ancient scene, Premiere. DATA-driven from WL_DATA; holds no lesson content. */
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
  W.frame = function (k) { if (S.frames[k]) return; S.frames[k] = 1; C.save(); C.cheer(); C.toast('🎞️ New frame for your film: ' + { formation: 'Evidence preserved', bite: 'The Bite Lab', dig: 'The excavation', det: 'Fossil detective' }[k]); W.reel(); };
  W.reel = function (checkDone) {
    if (checkDone != null) W._ck = checkDone;
    var n = 0; $$('#reel .wl-frame').forEach(function (f) { var on = !!S.frames[f.dataset.f]; f.classList.toggle('locked', !on); f.classList.toggle('lit', on); if (on) n++; });
    var ready = n === 4 && W._ck; var b = $('#premiere-btn'); if (b) b.disabled = !ready;
    var m = $('#reel-msg'); if (m) m.textContent = ready ? '🎬 All four frames are in and your checklist is done. Premiere your film!' : (n + ' of 4 frames earned in the Lesson.' + (W._ck ? '' : ' Then finish the checklist.'));
    if (ready && !S.reel) { S.reel = 1; C.save(); C.markTab('assign'); }
    exhibit();
  };

  /* ---------- 1. Specimen + magnifier inspect ---------- */
  (function () {
    var HS = D.spec.hotspots, found = S.specFound = S.specFound || [], box = $('#inspect'), view = $('.wl-ins-view'), img = $('#ins-img'), lens = $('.wl-lens'), marks = $('.wl-ins-marks'),
      zoom = $('#ins-zoom'), lensOn = true, z = 1, px = 0, py = 0, drag = null;
    img.src = IMG[D.spec.img];
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
      if (best > -1 && bd < D.spec.radius) { if (found.indexOf(best) < 0) { found.push(best); C.save(); C.ding(); noise(80, 3000, .08); } drawMarks(); tip(); }
      else { var vr = view.getBoundingClientRect(), d = el('div', 'dot'); d.style.left = (e.clientX - vr.left) + 'px'; d.style.top = (e.clientY - vr.top) + 'px'; marks.appendChild(d); setTimeout(function () { d.remove(); }, 1000); $('#ins-tip').textContent = 'Nothing new there. Slide the lens slowly and look for a shape.'; } });
    function tip() { $('#ins-tip').textContent = found.length >= 3 ? '✅ Great observing! Close the viewer and write what you noticed.' : 'You found: ' + found.map(function (k) { return HS[k].name.toLowerCase(); }).join(', ') + '. Keep looking!';
      if (found.length >= 3) { $('#spec-boxes').hidden = false; $('#spec-fb').className = 'wl-fb dark ok'; $('#spec-fb').textContent = 'You found ' + found.length + ' things. Now write about one of them.'; } }
    zoom.oninput = function () { var r = view.getBoundingClientRect(), cx = r.width / 2, cy = r.height / 2, nz = +zoom.value; px = cx - (cx - px) * nz / z; py = cy - (cy - py) * nz / z; z = nz; apply(); };
    $('#ins-lens').onclick = function () { lensOn = !lensOn; this.setAttribute('aria-pressed', lensOn); this.textContent = '🔍 Magnifying lens: ' + (lensOn ? 'on' : 'off'); view.style.cursor = lensOn ? 'none' : 'grab'; };
    function open() { box.hidden = false; $('#spec-a').classList.add('lit'); setTimeout(apply, 30); tip(); if (!found.length) $('#ins-tip').textContent = 'Move the lens over the rock. When you spot something, tap it.'; }
    function close() { box.hidden = true; $('#spec-a').classList.remove('lit'); }
    $('#spec-open').onclick = open; $('.wl-ins-x').onclick = close; box.addEventListener('click', function (e) { if (e.target === box) close(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !box.hidden) close(); });
    $('#spec-a').onclick = open;
    if (found.length >= 3) $('#spec-boxes').hidden = false;
  })();

  /* ---------- 2. Formation mini-movie (model) ---------- */
  (function () {
    var mv = $('#fm-movie'), fish = $('.wl-mv-fish', mv), layers = $('.wl-mv-layers', mv), real = $('.wl-mv-real', mv), cnt = $('.wl-mv-count', mv), cap = $('.wl-mv-cap', mv), stamp = $('.wl-mv-stamp', mv), rays = $('.wl-mv-rays', mv), cv = $('.wl-mv-part', mv), ctx = cv.getContext('2d'), P = [], raf, timers = [];
    var BANDS = ['#8b7355', '#a08866', '#7d6a50', '#b19a74', '#94795a', '#6f5d45'];
    function reset() { timers.forEach(clearTimeout); timers = []; cancelAnimationFrame(raf); P = []; fish.style.transition = 'none'; fish.style.top = '12%'; fish.style.transform = 'rotate(-4deg)'; fish.querySelector('.flesh').style.opacity = 1; fish.querySelector('.skel').style.opacity = 0; fish.style.opacity = 1;
      layers.innerHTML = ''; layers.style.height = '0'; real.style.opacity = 0; cnt.textContent = ''; cap.textContent = ''; stamp.classList.remove('on'); rays.style.opacity = 1; mv.classList.remove('cut'); void fish.offsetWidth; fish.style.transition = ''; }
    function at(t, f) { timers.push(setTimeout(f, RM ? t / 3 : t)); }
    function loop() { var r = mv.getBoundingClientRect(); if (cv.width !== (r.width | 0)) { cv.width = r.width | 0; cv.height = r.height | 0; } ctx.clearRect(0, 0, cv.width, cv.height);
      P.forEach(function (p) { p.y += p.v; p.x += Math.sin(p.y / 20) * .3; if (p.y > p.stop) p.y = p.stop; ctx.fillStyle = p.c; ctx.fillRect(p.x, p.y, p.s, p.s); }); raf = requestAnimationFrame(loop); }
    function sediment(n, stopFrac) { var r = mv.getBoundingClientRect(); for (var i = 0; i < n; i++) P.push({ x: Math.random() * r.width, y: -Math.random() * r.height * .6, v: .6 + Math.random() * 1.4, s: 1.5 + Math.random() * 2.5, c: ['#c8b28c', '#a8916c', '#8f7a5a'][i % 3], stop: r.height * (stopFrac - Math.random() * .04) }); }
    W.movie = function (done) {
      mv.hidden = false; reset(); loop(); mv.scrollIntoView({ block: 'center', behavior: RM ? 'auto' : 'smooth' });
      cap.textContent = '1 · A fish dies and sinks to the bottom of the lake.'; sediment(40, .9);
      at(300, function () { fish.style.top = '58%'; fish.style.transform = 'rotate(3deg)'; });
      at(2600, function () { cap.textContent = '2 · Mud and sand drift down and cover it.'; sediment(160, .86); layers.style.height = '24%'; addBand(0); addBand(1); noise(600, 400, .1); });
      at(4400, function () { cap.textContent = '3 · Layer after layer piles on top. Time passes…'; mv.classList.add('cut'); rays.style.opacity = 0; P = []; [2, 3, 4, 5].forEach(function (k, i) { at(i * 320, function () { addBand(k); layers.style.height = (30 + (i + 1) * 11) + '%'; }); });
        var steps = ['100 years', '1,000 years', '100,000 years', '1,000,000 years', 'Millions of years']; steps.forEach(function (t, i) { at(i * 380, function () { cnt.textContent = '⏳ ' + t; C.ding && noise(40, 5000, .05); }); });
        fish.querySelector('.flesh').style.opacity = 0; fish.querySelector('.skel').style.opacity = 1; });
      at(6800, function () { cap.textContent = '4 · The soft parts are gone. Rock has filled in the shape of the bones.'; fish.style.opacity = 0; real.style.opacity = 1; });
      at(8400, function () { stamp.classList.add('on'); thud(); cap.textContent = 'The real thing: a fossil fish from Fossil Butte, Wyoming.'; cancelAnimationFrame(raf); done && done(); });
    };
    W.movieStatic = function () { mv.hidden = false; reset(); fish.style.opacity = 0; real.style.opacity = 1; mv.classList.add('cut'); rays.style.opacity = 0; [0, 1, 2, 3, 4, 5].forEach(addBand); layers.style.height = '70%'; stamp.classList.add('on'); cap.textContent = 'The real thing: a fossil fish from Fossil Butte, Wyoming.'; };
    function addBand(k) { var b = el('div'); b.style.background = 'repeating-linear-gradient(0deg,' + BANDS[k] + ' 0 5px,' + BANDS[(k + 2) % 6] + ' 5px 7px)'; layers.appendChild(b); requestAnimationFrame(function () { b.style.height = '18%'; b.style.flex = '1'; }); }
    $('#fm-replay').onclick = function () { W.movie(); };
  })();

  /* ---------- 3. The Bite Lab ---------- */
  (function () {
    var B = D.bite, st = S.bite || { step: 0, tests: {} }, box = $('#bite-step'), mats = $('#bite-mats'), trays = $$('.wl-tray-spec');
    S.bite = st; function sv() { C.save(); }
    function trayOf(t) { return $('.wl-tray-spec[data-t="' + t + '"]'); }
    function render() {
      trays.forEach(function (t) { t.classList.remove('pick'); });
      mats.hidden = st.step !== 2;
      if (st.step === 0 || st.step === 1) { var q = B.ask[st.step]; box.innerHTML = '<div class="wl-step"><div class="n">Step ' + (st.step + 1) + ' of 4 · Predict</div><p>' + q.q + ' Tap a tray.</p></div><p class="wl-fb"></p>'; }
      if (st.step === 2) box.innerHTML = '<div class="wl-step"><div class="n">Step 3 of 4 · Test it with a model</div><p>Drag the leaf onto one tray and the clay strip onto the other (or tap a material, then tap a tray). Then press <b>Press down</b>.</p></div><div style="text-align:center"><button class="wl-btn" id="bite-press" disabled>⬇ Press down</button></div><p class="wl-fb"></p><p class="wl-starter">This is a model. It shows how a tooth\'s shape can match its job. It is not proof of exactly what each animal ate.</p>';
      if (st.step === 3) { box.innerHTML = '<div class="wl-step"><div class="n">Step 4 of 4 · Explain</div><p>Finish each sentence.</p></div>' + ['A', 'B'].map(function (t) { var c = B.claim[t]; return '<p style="margin:8px 0 4px"><b>Specimen ' + t + ':</b> This tooth has <span class="wl-chips" style="display:inline-flex;margin:0" data-k="' + t + 'f">' + c.feat.map(function (f, i) { return '<button class="wl-chip" data-i="' + i + '">' + f + '</button>'; }).join('') + '</span>, so I think the animal probably ate <span class="wl-chips" style="display:inline-flex;margin:0" data-k="' + t + 'e">' + c.eat.map(function (f, i) { return '<button class="wl-chip" data-i="' + i + '">' + f + '</button>'; }).join('') + '</span>.</p>'; }).join('') + '<p class="wl-fb"></p>';
        var pick = {};
        $$('.wl-chips[data-k]', box).forEach(function (g) { $$('.wl-chip', g).forEach(function (b) { b.onclick = function () { var k = g.dataset.k, t = k[0], kind = k[1], c = B.claim[t], ok = (kind === 'f' ? c.featOk : c.eatOk) === +b.dataset.i, fb = box.querySelector('.wl-fb');
          if (!ok) { b.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = kind === 'f' ? 'Look at the tooth on Specimen ' + t + ' again. What shape do you see?' : 'Think about your test. What did this shape do best?'; C.oops(); return; }
          $$('.wl-chip', g).forEach(function (x) { x.classList.toggle('on', x === b); }); pick[k] = 1; fb.textContent = ''; C.ding();
          if (pick[t + 'f'] && pick[t + 'e']) { var tr = trayOf(t); tr.querySelector('.wl-curator span').innerHTML = B.curator[t]; tr.classList.add('flip'); noise(300, 1800, .1); }
          if (Object.keys(pick).length === 4) { st.step = 4; st.claims = 1; sv(); setTimeout(finish, 900); } }; }); });
      }
      if (st.step >= 4) finish();
    }
    function finish() { box.innerHTML = '<p class="wl-stampmini">CURATOR\'S NOTES COMPLETE</p><p style="margin:4px 0 0">Shape can tell us about function (the job a part does). That helps scientists infer how extinct animals lived.</p>'; mats.hidden = true;
      trays.forEach(function (t) { t.querySelector('.wl-curator span').innerHTML = B.curator[t.dataset.t]; t.classList.add('flip'); }); $('#teeth-end').hidden = false; W.frame('bite'); }
    trays.forEach(function (t) { t.addEventListener('click', function (e) { if (e.target.closest('.wl-drop')) return;
      if (st.step === 0 || st.step === 1) { var q = B.ask[st.step], fb = box.querySelector('.wl-fb'); st.pred = st.pred || [];
        if (t.dataset.t !== q.ans) { t.classList.add('no'); setTimeout(function () { t.classList.remove('no'); }, 450); fb.className = 'wl-fb miss'; fb.textContent = q.miss; C.oops(); return; }
        t.classList.add('pick'); fb.className = 'wl-fb ok'; fb.textContent = q.ok; C.ding(); st.step++; sv(); setTimeout(render, 1300); }
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
      placed[t] = mat; var d = $('.wl-drop[data-drop="' + t + '"]'); d.innerHTML = mat === 'leaf' ? '<img src="' + IMG.leaf + '" alt="Leaf" style="width:62px;height:62px;object-fit:cover;border-radius:50%">' : '<span class="wl-clay"></span>';
      selMat = null; $$('.wl-mat', mats).forEach(function (x) { x.classList.remove('sel'); }); C.ding();
      var pb = $('#bite-press'); if (pb) { pb.disabled = !(placed.A || placed.B); pb.onclick = press; }
    }
    function press() {
      var fb = box.querySelector('.wl-fb'), msgs = [];
      ['A', 'B'].forEach(function (t) { var mat = placed[t]; if (!mat) return; var tr = trayOf(t), d = $('.wl-drop[data-drop="' + t + '"]'); tr.classList.add('press'); thud();
        setTimeout(function () { tr.classList.remove('press');
          var key = t + mat, r = B.result[key]; msgs.push('<b>Specimen ' + t + ' + ' + (mat === 'leaf' ? 'leaf' : 'clay') + ':</b> ' + r);
          if (key === 'Bleaf') { d.querySelector('img').classList.add('crush'); crumbs(d); noise(350, 900, .2); }
          if (key === 'Aleaf') d.querySelector('img').classList.add('holes');
          if (key === 'Aclay') { d.querySelector('.wl-clay').classList.add('cut'); noise(200, 4000, .15); }
          if (key === 'Bclay') d.querySelector('.wl-clay').classList.add('squash');
          st.tests[key] = 1; sv(); fb.className = 'wl-fb'; fb.innerHTML = msgs.join('<br>');
          if (st.tests.Bleaf && st.tests.Aclay && st.step === 2) { st.step = 3; sv(); setTimeout(render, 2600); fb.innerHTML += '<br><b style="color:#2E7D32">You tested the best match for each tooth.</b>'; }
          else if (!(st.tests.Bleaf && st.tests.Aclay)) fb.innerHTML += '<br>Try swapping the materials to test the other way.'; }, 380); });
    }
    function crumbs(d) { for (var i = 0; i < 12; i++) { var c = el('span', 'wl-crumb'); c.style.left = '50%'; c.style.top = '50%'; c.style.setProperty('--dx', (Math.random() * 80 - 40) + 'px'); c.style.setProperty('--dy', (Math.random() * 40 - 10) + 'px'); d.appendChild(c); setTimeout(function (x) { x.remove(); }.bind(null, c), 900); } }
    render();
  })();

  /* ---------- 4. Excavation wall + time elevator ---------- */
  (function () {
    var L = D.dig, st = S.digv = S.digv || { done: 0 }, bands = $$('.wl-band'), card = $('#dig-card'), car = $('.wl-elev-car'), sky = $('.wl-sky'), stops = [2, 24, 45, 66, 88];
    function sv() { C.save(); }
    if (st.pred) start(true);
    $$('#dig-predict .wl-chip').forEach(function (b) { b.onclick = function () { st.pred = b.dataset.p; sv(); $$('#dig-predict .wl-chip').forEach(function (x) { x.classList.toggle('on', x === b); }); C.ding(); setTimeout(function () { start(); }, 500); }; });
    function start(restore) {
      $('#dig-predict').innerHTML = '<p style="margin:0">Your prediction: <b>the ' + st.pred + ' layer formed first.</b> Let\'s dig and find out.</p>'; $('#dig-wrap').hidden = false;
      bands.forEach(function (b, i) { prep(b, i); }); paint(); if (st.done >= 4) end(true);
    }
    function paint() {
      bands.forEach(function (b, i) { b.classList.toggle('active', i === st.done && !b._open); b.classList.toggle('locked', i > st.done); if (i < st.done) open(b, i, true); });
      car.style.top = 'calc(' + stops[Math.min(st.done, 4)] + '% - 4px)'; $$('.wl-elev span').forEach(function (s, i) { s.classList.toggle('on', i === Math.min(st.done, 4)); });
      if (st.done === 0) { card.classList.add('in'); card.innerHTML = '<div class="wl-step"><div class="n">Layer 1 of 4</div><p>Brush the glowing top layer. Drag across it (or tap it again and again).</p></div>'; }
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
      b.addEventListener('pointerdown', function (e) { if (i !== st.done) { if (i > st.done) { C.toast('Clear the layer above first. It sits on top, so you reach it first.'); } return; } down = true; b.setPointerCapture(e.pointerId); brush(e); for (var k = 0; k < 4; k++) brush({ clientX: e.clientX + (Math.random() * 60 - 30), clientY: e.clientY + (Math.random() * 30 - 15) }); });
      b.addEventListener('pointermove', function (e) { if (down) brush(e); });
      b.addEventListener('pointerup', function () { down = false; });
    }
    function dust(b, e) { if (RM) return; var r = b.getBoundingClientRect(); for (var k = 0; k < 5; k++) { var c = el('span', 'wl-crumb'); c.style.background = '#cdb98f'; c.style.left = (e.clientX - r.left) + 'px'; c.style.top = (e.clientY - r.top) + 'px'; c.style.setProperty('--dx', (Math.random() * 60 - 30) + 'px'); c.style.setProperty('--dy', (-Math.random() * 40) + 'px'); b.appendChild(c); setTimeout(function (x) { x.remove(); }.bind(null, c), 850); } }
    function open(b, i, silent) {
      if (b._open) return; b._open = 1; b.classList.add('open'); b.classList.remove('active'); var cv = b.querySelector('canvas'); cv.style.transition = 'opacity .6s'; cv.style.opacity = 0;
      if (silent) { tagBand(b, i); return; }
      C.ding(); var l = L[i];
      card.classList.remove('in'); setTimeout(function () {
        card.innerHTML = '<div class="wl-step"><div class="n">Fossil recovered from Layer ' + (i + 1) + '</div><p>' + l.ask + '</p></div><img src="' + IMG[l.img] + '" alt="' + l.alt + '"><p style="font-size:15px;margin:6px 0">' + l.clue + '</p><div class="wl-choices" data-choice="digv' + i + '">' + D.digChoices.map(function (c, k) { return '<button class="wl-choice" ' + (k === l.ans ? 'data-ok="' + l.ok + '"' : 'data-miss="' + (l.miss[k] || 'Read the clue again.') + '"') + '>' + c + '</button>'; }).join('') + '</div><p class="wl-fb"></p>';
        card.classList.add('in'); delete S['c-digv' + i];
        C.choices(card.querySelector('.wl-choices'), function () { tagBand(b, i); then(i); setTimeout(function () { st.done = i + 1; sv(); paint(); if (st.done < 4) { card.innerHTML = '<div class="wl-step"><div class="n">Layer ' + (st.done + 1) + ' of 4</div><p>Going deeper, and farther back in time. Brush Layer ' + (st.done + 1) + '.</p></div>'; } else end(); }, 2200); });
      }, 250);
    }
    function tagBand(b, i) { if (!b.querySelector('.tag')) b.appendChild(el('span', 'tag', L[i].tag)); }
    function then(i) { var l = L[i], t = sky.querySelector('.then'); t.src = IMG[l.env]; t.alt = l.envAlt; sky.classList.add('past'); sky.querySelector('.wl-sky-cap').textContent = l.envCap; }
    function end(restore) {
      bands.forEach(function (b, i) { open(b, i, true); }); car.style.top = 'calc(88% - 4px)';
      $('#dig-cliff').classList.add('pull'); setTimeout(function () { $('#dig-line').classList.add('on'); }, restore ? 0 : 900);
      card.classList.add('in'); card.innerHTML = '<div class="wl-step"><div class="n">All 4 layers recovered</div><p>Look at the line on the cliff. It runs from the oldest layer at the bottom to the youngest at the top.</p></div>';
      $('#dig-after').hidden = false;
      $('#dig-pred-res').innerHTML = st.pred === 'bottom' ? '<span class="wl-stampmini">PREDICTION CONFIRMED</span> You predicted the bottom layer formed first. The evidence agrees.' : '<span class="wl-stampmini" style="border-color:#B5532A;color:#B5532A">PREDICTION CHANGED</span> You predicted the top layer. The evidence changed that idea: the bottom layer formed first, so it is the oldest.';
      if (!restore) C.cheer();
      C.choices($('[data-choice="mix"]'), function () { W.frame('dig'); });
    }
    function resz(force) { bands.forEach(function (b) { if (!b._open && b._size && (force || !b.querySelector('canvas').width)) b._size(); }); }
    window.addEventListener('resize', function () { resz(true); }); document.addEventListener('click', function () { setTimeout(function () { resz(false); }, 80); });
  })();

  /* ---------- 5. Fossil detective with Past Revealed ---------- */
  (function () {
    var F = D.det, wrap = $('#det-cards'), work = $('#det-work'), body = $('#det-chart tbody'), res = S.det = S.det || {};
    F.forEach(function (f, i) { var c = el('button', 'wl-dcard'); c.type = 'button'; c.dataset.i = i; c.innerHTML = '<img src="' + IMG[f.img] + '" alt="' + f.alt + '">Specimen ' + f.id; c.onclick = function () { pick(i); }; wrap.appendChild(c); });
    function solved() { return Object.keys(res).filter(function (k) { return res[k].done; }); }
    function chart() {
      var rows = solved();
      body.innerHTML = rows.length ? rows.map(function (k) { var r = res[k], f = F[k]; return '<tr><td><b>' + f.id + '</b></td><td>' + r.clue + '</td><td>' + f.org[f.orgAns] + '</td><td>' + f.env + '</td><td>I saw ' + r.clue.toLowerCase() + ', so it was ' + f.orgShort + '.</td></tr>'; }).join('') : '<tr><td class="empty" colspan="5">Your chart fills in as you solve fossils.</td></tr>';
      for (var k = rows.length; k < 3; k++) body.insertAdjacentHTML('beforeend', '<tr><td class="empty">?</td><td class="empty"></td><td class="empty"></td><td class="empty"></td><td class="empty"></td></tr>');
      $$('.wl-dcard').forEach(function (c) { c.classList.toggle('done', !!(res[c.dataset.i] && res[c.dataset.i].done)); });
      $('#det-write').hidden = rows.length < 3; $('#rebuild').hidden = rows.length < 1; C.save(); C.gather(); C.checklist(); W.rebuildFossils && W.rebuildFossils(); exhibit();
      if (rows.length >= 3) W.frame('det');
    }
    function pick(i) {
      var f = F[i]; if (res[i] && res[i].done) return; if (solved().length >= 3) { C.toast('You already solved 3 fossils. Nice detective work!'); return; }
      $$('.wl-dcard').forEach(function (c) { c.classList.toggle('pick', +c.dataset.i === i); });
      var st = 0, r = res[i] = { clue: '' };
      function draw() {
        var h = '';
        if (st < 3) { h = '<div class="wl-dwork"><figure class="wl-fig" style="margin:0"><div class="wl-slab sm"><img src="' + IMG[f.img] + '" alt="' + f.alt + '"></div><figcaption>Specimen ' + f.id + '</figcaption></figure><div>';
          if (st === 0) h += '<div class="wl-step"><div class="n">Step 1 of 3 · Observe</div><p>What clue do you see? Tap one.</p></div><div class="wl-chips">' + f.clues.map(function (c, k) { return '<button class="wl-chip" data-k="' + k + '">' + c.t + '</button>'; }).join('') + '</div>';
          if (st === 1) h += '<div class="wl-done-row">✓ I observe: ' + r.clue + '</div><div class="wl-step"><div class="n">Step 2 of 3 · Infer</div><p>What was it?</p></div><div class="wl-chips">' + f.org.map(function (c, k) { return '<button class="wl-chip" data-k="' + k + '">' + c + '</button>'; }).join('') + '</div>';
          if (st === 2) h += '<div class="wl-done-row">✓ I observe: ' + r.clue + '</div><div class="wl-done-row">✓ It was: ' + f.org[f.orgAns] + '</div><div class="wl-step"><div class="n">Step 3 of 3 · Predict</div><p>Does this fossil make you picture water or land?</p></div><div class="wl-chips"><button class="wl-chip" data-k="water">💧 Water</button><button class="wl-chip" data-k="land">🌳 Land</button></div>';
          h += '<p class="wl-fb"></p></div></div>'; }
        else {
          var ok = r.pred === f.envAns;
          h = '<div class="wl-past" id="past"><div class="now"></div><img class="then" src="' + IMG[f.envImg] + '" alt="' + esc(f.envAlt) + '"><div class="ring"></div><div class="fos"><img src="' + IMG[f.img] + '" alt=""></div><div class="kicker">The past revealed</div><div class="sub">' + f.envCap + '</div><div class="cap">' + f.reveal + '</div></div>' +
            '<p style="margin:6px 0">' + (ok ? '<span class="wl-stampmini">PREDICTION CONFIRMED</span> You pictured ' + r.pred + '. The evidence agrees.' : '<span class="wl-stampmini" style="border-color:#B5532A;color:#B5532A">EVIDENCE CHANGED MY IDEA</span> You pictured ' + r.pred + '. ' + f.envMiss.replace(/\s*Try again\.$/, '')) + '</p><div class="wl-bts"><b>🎬 Behind the scenes</b>' + f.bts + '</div>';
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
    W.rebuildFossils = function () { var box = $('#rb-fossils'); box.innerHTML = W.detSolved().map(function (k) { return '<button class="wl-chip" data-k="' + k + '">Specimen ' + D.det[k].id + '</button>'; }).join('');
      $$('.wl-chip', box).forEach(function (b) { b.onclick = function () { $$('.wl-chip', box).forEach(function (x) { x.classList.toggle('on', x === b); }); begin(+b.dataset.k); }; }); };
    function begin(k) { cur = D.det[k]; envSel = null; lifeSel = {}; stage.querySelector('.wl-rb-fossil').innerHTML = '<img src="' + IMG[cur.img] + '" alt="">'; stage.querySelector('.wl-rb-bg').style.backgroundImage = ''; stage.querySelector('.wl-rb-water').style.height = '0'; stage.querySelector('.wl-rb-life').innerHTML = '';
      stage.querySelector('.wl-rb-cap').textContent = 'Specimen ' + cur.id + ': ' + cur.org[cur.orgAns] + '. What place does it point to?';
      steps.innerHTML = '<div class="wl-step"><div class="n">Step 1 of 3</div><p>Pick the place.</p></div><div class="wl-chips">' + R.envs.map(function (e, i) { return '<button class="wl-chip" data-i="' + i + '">' + e.name + '</button>'; }).join('') + '</div><p class="wl-fb"></p>';
      $$('.wl-chip', steps).forEach(function (b) { b.onclick = function () { var e = R.envs[+b.dataset.i], fb = steps.querySelector('.wl-fb');
        if (e.key !== cur.rebuildEnv) { b.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = 'Hmm. Look at your fossil again. ' + cur.envMiss; C.oops(); return; }
        envSel = e; C.ding(); stage.querySelector('.wl-rb-bg').style.backgroundImage = 'url("' + IMG[e.key === 'water' ? cur.envImg : e.img] + '")'; if (e.key === 'water') setTimeout(function () { stage.querySelector('.wl-rb-water').style.height = '100%'; }, 300); stage.querySelector('.wl-rb-cap').textContent = e.cap; life(); }; }); }
    function life() { steps.innerHTML = '<div class="wl-step"><div class="n">Step 2 of 3</div><p>Pick the living things that belong in this place. Tap each one.</p></div><div class="wl-chips">' + R.life.map(function (l, i) { return '<button class="wl-chip" data-i="' + i + '">' + l.name + '</button>'; }).join('') + '</div><p class="wl-fb"></p>';
      $$('.wl-chip', steps).forEach(function (b) { b.onclick = function () { var l = R.life[+b.dataset.i], fb = steps.querySelector('.wl-fb'); if (lifeSel[b.dataset.i]) return;
        if (l.env !== envSel.key) { b.classList.add('miss'); fb.className = 'wl-fb miss'; fb.textContent = l.miss; C.oops(); return; }
        lifeSel[b.dataset.i] = 1; b.classList.add('on'); C.ding(); var im = el('img'); im.src = IMG[l.img]; im.alt = l.name; stage.querySelector('.wl-rb-life').appendChild(im);
        var need = R.life.filter(function (x) { return x.env === envSel.key; }).length; if (Object.keys(lifeSel).length === need) why(); }; }); }
    function why() { steps.innerHTML = '<div class="wl-step"><div class="n">Step 3 of 3</div><p>What evidence made you choose this place?</p></div><div class="wl-in"><textarea id="in-rebuild" data-min="6" placeholder="I chose this because the fossil…"></textarea></div>';
      var ta = $('#in-rebuild'); ta.value = S['t-in-rebuild'] || ''; ta.oninput = function () { S['t-in-rebuild'] = ta.value; C.save(); }; C.cheer(); stage.querySelector('.wl-rb-cap').textContent = '🌍 Scene rebuilt from your evidence.'; }
    var dr = $('#rebuild'); dr.addEventListener('toggle', function () { if (dr.open) W.rebuildFossils(); });
  })();

  /* ---------- 7. Premiere my fossil story ---------- */
  var exPick = null;
  function exhibit() {
    if (!$('#exhibit')) return; var sol = W.detSolved ? W.detSolved() : [];
    if (exPick == null || sol.indexOf(String(exPick)) < 0) exPick = S.exPick != null && sol.indexOf(String(S.exPick)) > -1 ? S.exPick : sol[0];
    $('#ex-pick').innerHTML = sol.map(function (k) { return '<button class="wl-chip' + (String(k) === String(exPick) ? ' on' : '') + '" data-k="' + k + '">' + D.det[k].id + '</button>'; }).join('');
    $$('#ex-pick .wl-chip').forEach(function (b) { b.onclick = function () { exPick = b.dataset.k; S.exPick = exPick; C.save(); exhibit(); }; });
    var f = exPick != null ? D.det[exPick] : null, r = f ? S.det[exPick] : null;
    $('#ex-img').src = f ? IMG[f.img] : IMG[D.spec.img]; $('#ex-num').textContent = f ? 'Specimen ' + f.id : 'My specimen';
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
      var frames = [['formation', IMG.phareodus, 'Evidence preserved: mud, time, and stone made a fossil.'], ['bite', IMG.tooth_sharp, 'The Bite Lab: a tooth\'s shape matches its job.'], ['dig', IMG.gc_wall, 'The excavation: in undisturbed rock, lower layers formed first.'], ['det', IMG[D.det[exPick || 0].img], 'Fossil detective: fossils tell us about places long ago.']];
      at(2800, function () { cnt.remove(); });
      frames.forEach(function (fr, i) { at(2800 + i * 2300, function () { var d = el('div', 'wl-th-frame', '<img src="' + fr[1] + '" alt=""><p>' + fr[2] + '</p>'); scr.appendChild(d); requestAnimationFrame(function () { d.classList.add('on'); }); noise(120, 2200, .12); at(2000, function () { d.classList.remove('on'); }); }); });
      at(2800 + 4 * 2300, function () {
        var f = D.det[exPick || 0], d = el('div', 'wl-th-frame', '<div class="wl-th-final"><img src="' + IMG[f.img] + '" alt=""><div><p style="text-align:left;margin:0 0 8px;color:#e3b04b;font-size:.85em;letter-spacing:.12em;text-transform:uppercase">My fossil story</p><p style="text-align:left" id="th-type"></p></div></div>');
        scr.appendChild(d); requestAnimationFrame(function () { d.classList.add('on'); });
        var txt = ($('#ex-obs').textContent + ' I think it was ' + (D.det[exPick || 0].orgShort || 'a living thing') + '. ' + $('#ex-tells').textContent).trim(), k = 0, tp = $('#th-type');
        var iv = setInterval(function () { tp.textContent = txt.slice(0, ++k); if (k >= txt.length) clearInterval(iv); }, RM ? 1 : 28); timers.push(iv);
        at(RM ? 300 : Math.min(5200, txt.length * 28 + 800), function () { var dir = el('div', 'wl-th-dir', 'DIRECTED BY: JUNIOR PALEONTOLOGIST' + (S.director ? '<br>' + esc(S.director).toUpperCase() : '')); scr.appendChild(dir); requestAnimationFrame(function () { dir.classList.add('on'); }); C.cheer(); });
      });
    };
    function close() { th.hidden = true; timers.forEach(function (t) { clearTimeout(t); clearInterval(t); }); scr.innerHTML = ''; }
    $('.wl-th-x').onclick = close; document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && !th.hidden) close(); });
  })();

  W.after = function () { W.reel(window.__ck); exhibit(); };
}
