/* Opti's Wonder Films — cinematic opener engine (G3 science sparkle layer).
   DATA-driven: window.WF_DATA = {kicker, lesson, title, bigQuestion, poster, music:{src,vol}, shots:[...], captions:[...], credits:[...], startTarget}
   Shot types: leader | black | photo | reveal | xray | flash | archive | title. Any shot may carry sfxAt [{at,name,arg}].  Holds NO lesson content. */
(function () {
  'use strict';
  var D = window.WF_DATA; if (!D) return;
  var IMG = window.WF_IMG || {};
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;
  var host = document.getElementById(D.mount || 'wf-film'); if (!host) return;
  function el(tag, cls, html) { var e = document.createElement(tag); if (cls) e.className = cls; if (html != null) e.innerHTML = html; return e; }
  function src(k) { return IMG[k] || k; }
  function clamp(x, a, b) { return Math.max(a, Math.min(b, x)); }
  function ease(x) { return x < .5 ? 2 * x * x : 1 - Math.pow(-2 * x + 2, 2) / 2; }
  function lerp(a, b, t) { return a + (b - a) * t; }
  var END = 0; D.shots.forEach(function (s) { END = Math.max(END, s.t + s.d); });

  /* ---------- DOM ---------- */
  var wrap = el('div', 'wf-wrap'); host.appendChild(wrap);
  var stage = el('div', 'wf-stage'); stage.setAttribute('role', 'region'); stage.setAttribute('aria-label', 'Lesson film: ' + D.title);
  wrap.appendChild(stage);
  var svgNS = 'http://www.w3.org/2000/svg';
  var defs = document.createElementNS(svgNS, 'svg'); defs.setAttribute('width', 0); defs.setAttribute('height', 0); defs.style.position = 'absolute';
  defs.innerHTML = '<filter id="wfRipple"><feTurbulence type="fractalNoise" baseFrequency="0.012 0.03" numOctaves="2" seed="3" result="n"/>' +
    '<feDisplacementMap in="SourceGraphic" in2="n" scale="0" xChannelSelector="R" yChannelSelector="G"/></filter>' +
    '<filter id="wfCaustic" x="0" y="0" width="100%" height="100%"><feTurbulence type="turbulence" baseFrequency="0.018 0.032" numOctaves="2" seed="8"/>' +
    '<feColorMatrix values="0 0 0 0 0.75  0 0 0 0 0.95  0 0 0 0 1  0 0 0 9 -6.2"/></filter>';
  stage.appendChild(defs);
  var rippleMap = defs.querySelector('#wfRipple feDisplacementMap');
  var causticTurb = defs.querySelector('#wfCaustic feTurbulence');

  var layers = D.shots.map(function (s, i) {
    var L;
    if (s.type === 'leader') {
      L = el('div', 'wf-layer wf-leader', '<div class="k">' + (s.top || '') + '</div><div class="rule"></div><div class="n">' + (s.name || D.kicker) + '</div><div class="rule"></div><div class="p">' + (s.bottom || 'presents') + '</div>');
    } else if (s.type === 'flash') {
      L = el('div', 'wf-layer wf-flash', s.lines.map(function (l) { return '<span>' + l + '</span>'; }).join(''));
    } else if (s.type === 'title') {
      L = el('div', 'wf-layer wf-title', '<div class="k">' + D.kicker + '</div><h2>' + D.title + '</h2><div class="s">' + (D.lesson || '') + '</div>');
    } else if (s.type === 'black') {
      L = el('div', 'wf-layer wf-black');
    } else if (s.type === 'archive') {
      L = el('div', 'wf-layer wf-archive', '<div class="print"><img alt="' + (s.alt || '') + '" src="' + src(s.img) + '"><i>' + (s.note || '') + '</i></div>');
    } else {
      L = el('div', 'wf-layer' + (s.contain ? ' wf-contain' : ''), '<img alt="' + (s.alt || '') + '" src="' + src(s.img) + '">');
      if (s.grade) L.querySelector('img').style.filter = s.grade;
      if (s.type === 'reveal') { var c = el('canvas', 'wf-fx'); L.appendChild(c); s._cv = c; }
      if (s.type === 'xray') { var xb = el('div', 'wf-xband'); var xw = el('div', 'wf-xwin', '<img alt="' + (s.alt2 || '') + '" src="' + src(s.img2) + '">' + (s.xlabel ? '<b>' + s.xlabel + '</b>' : ''));
        var w = s.win || [30, 60, 40]; xw.style.left = w[0] + '%'; xw.style.top = w[1] + '%'; xw.style.width = w[2] + '%'; xb.style.height = ((s.band || .16) * 100) + '%'; L.appendChild(xb); L.appendChild(xw); s._xb = xb; s._xw = xw; }
      if (s.tags) s._tags = s.tags.map(function (tg) { var t = el('div', 'wf-tag', tg.text); t.style.left = tg.x + '%'; t.style.top = tg.y + '%'; L.appendChild(t); return t; });
      if (s.fx && s.fx.indexOf('caustics') > -1) {
        var cs = document.createElementNS(svgNS, 'svg'); cs.setAttribute('class', 'wf-fx'); cs.setAttribute('preserveAspectRatio', 'none');
        cs.setAttribute('viewBox', '0 0 100 56'); cs.style.mixBlendMode = 'screen'; cs.style.opacity = '.45';
        cs.innerHTML = '<rect width="100" height="56" filter="url(#wfCaustic)"/>'; L.appendChild(cs);
      }
      if (s.fx && s.fx.indexOf('rays') > -1) {
        var r = el('div', 'wf-fx'); r.style.background = 'repeating-linear-gradient(100deg,rgba(255,255,230,0) 0 7%,rgba(255,255,230,.16) 9%,rgba(255,255,230,0) 12% 19%)';
        r.style.mixBlendMode = 'screen'; r.style.maskImage = r.style.webkitMaskImage = 'linear-gradient(#000,transparent 85%)'; s._rays = r; L.appendChild(r);
      }
      if (s.fx && s.fx.indexOf('sweep') > -1) {
        var sw = el('div', 'wf-fx'); sw.style.background = 'linear-gradient(0deg,rgba(255,220,140,0) 0%,rgba(255,220,140,.35) 6%,rgba(255,220,140,0) 12%)';
        sw.style.mixBlendMode = 'screen'; sw.style.backgroundSize = '100% 200%'; s._sweep = sw; L.appendChild(sw);
      }
    }
    L.dataset.i = i; stage.appendChild(L); s._el = L; s._img = L.querySelector('img');
    return L;
  });

  var part = el('canvas', 'wf-fx'); part.style.zIndex = 25; stage.appendChild(part);
  var grain = el('canvas', 'wf-fx wf-grain'); stage.appendChild(grain);
  stage.appendChild(el('div', 'wf-fx wf-vignette'));
  var flick = el('div', 'wf-fx wf-flicker'); stage.appendChild(flick);
  stage.appendChild(el('div', 'wf-bar top')); stage.appendChild(el('div', 'wf-bar bot'));
  var place = el('div', 'wf-place'); stage.appendChild(place);
  var count = el('div', 'wf-count', '<div class="num">0</div><div class="lab">years ago</div>'); stage.appendChild(count);
  var cap = el('div', 'wf-cap'); cap.setAttribute('aria-live', 'off'); stage.appendChild(cap);

  var ctrl = el('div', 'wf-ctrl');
  var bPause = el('button', '', '❚❚ Pause'), bCC = el('button', '', 'CC'), bSnd = el('button', '', '🔊 Sound'), bSkip = el('button', '', 'Skip ⏭');
  bCC.setAttribute('aria-pressed', 'true'); bSnd.setAttribute('aria-pressed', 'true');
  [bPause, bCC, bSnd, bSkip].forEach(function (b) { b.type = 'button'; ctrl.appendChild(b); });
  stage.appendChild(ctrl);

  var cover = el('div', 'wf-cover');
  cover.style.setProperty('--wf-poster', 'url("' + src(D.poster) + '")');
  stage.appendChild(cover);

  var credits = el('details', 'wf-credits', '<summary>Photo and music credits</summary><ul>' + (D.credits || []).map(function (c) {
    return '<li>' + c + '</li>'; }).join('') + '</ul>');
  wrap.appendChild(credits);

  function showPoster() {
    cover.innerHTML = '<div class="k">' + D.kicker + '</div><h2>' + D.title + '</h2>' +
      '<button class="wf-btn" type="button">▶ Play the film</button>' +
      '<div class="meta">' + Math.round(END) + ' seconds · Sound on, please!</div>';
    cover.classList.remove('wf-hidden');
    cover.querySelector('button').onclick = play;
  }
  function showEnd() {
    cover.innerHTML = '<div class="k">' + (D.endKicker || 'Our Big Question') + '</div>' +
      '<p class="q">' + D.bigQuestion + '</p>' +
      '<div><button class="wf-btn go" type="button">▶ Start the lesson</button><button class="wf-btn ghost again" type="button">↻ Watch again</button></div>';
    cover.style.setProperty('--wf-poster', 'url("' + src(D.endPoster || D.poster) + '")');
    cover.classList.remove('wf-hidden');
    cover.querySelector('.again').onclick = function () { play(); };
    cover.querySelector('.go').onclick = function () {
      var t = D.startTarget && document.querySelector(D.startTarget);
      if (t) { var bar = document.querySelector(D.stickyBar || '.wl-top'), y = t.getBoundingClientRect().top + window.scrollY - (bar ? bar.offsetHeight + 12 : 70); window.scrollTo({ top: y, behavior: window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches ? 'auto' : 'smooth' }); }
    };
    try { localStorage.setItem('wf-seen-' + D.id, '1'); } catch (e) {}
  }

  /* ---------- audio ---------- */
  var AC = null, master = null, sound = true;
  var music = new Audio(); music.preload = 'auto'; if (D.music) music.src = src(D.music.src);
  var voices = {};
  (D.captions || []).forEach(function (c, i) { var vs = c.voice && (IMG[c.voice] || (D.voiceBase ? D.voiceBase + c.voice + '.mp3' : '')); if (vs) { var a = new Audio(); a.preload = 'auto'; a.src = vs; a.onerror = function () { voices[i] = null; }; voices[i] = a; } });
  function ac() { if (!AC) { try { AC = new (window.AudioContext || window.webkitAudioContext)(); master = AC.createGain(); master.gain.value = .55; master.connect(AC.destination); } catch (e) {} } return AC; }
  function noiseBuf(sec) { var b = AC.createBuffer(1, AC.sampleRate * sec, AC.sampleRate), d = b.getChannelData(0); for (var i = 0; i < d.length; i++) d[i] = Math.random() * 2 - 1; return b; }
  var SFX = {
    whoosh: function (dur) { dur = dur || 1.2; var n = AC.createBufferSource(); n.buffer = noiseBuf(dur); var f = AC.createBiquadFilter(); f.type = 'bandpass'; f.Q.value = 1.2;
      var g = AC.createGain(), t = AC.currentTime; f.frequency.setValueAtTime(300, t); f.frequency.exponentialRampToValueAtTime(3200, t + dur * .7);
      g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.5, t + dur * .5); g.gain.linearRampToValueAtTime(0, t + dur);
      n.connect(f); f.connect(g); g.connect(master); n.start(); },
    thump: function () { var o = AC.createOscillator(), g = AC.createGain(), t = AC.currentTime; o.frequency.setValueAtTime(110, t); o.frequency.exponentialRampToValueAtTime(38, t + .5);
      g.gain.setValueAtTime(.9, t); g.gain.exponentialRampToValueAtTime(.001, t + .7); o.connect(g); g.connect(master); o.start(); o.stop(t + .8); },
    brush: function () { var n = AC.createBufferSource(); n.buffer = noiseBuf(.35); var f = AC.createBiquadFilter(); f.type = 'highpass'; f.frequency.value = 2400;
      var g = AC.createGain(), t = AC.currentTime; g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.16, t + .08); g.gain.linearRampToValueAtTime(0, t + .33);
      n.connect(f); f.connect(g); g.connect(master); n.start(); },
    shimmer: function () { [880, 1320, 1760, 2640].forEach(function (fq, k) { var o = AC.createOscillator(), g = AC.createGain(), t = AC.currentTime + k * .09;
      o.type = 'sine'; o.frequency.value = fq; g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.12, t + .02); g.gain.exponentialRampToValueAtTime(.001, t + 1.6);
      o.connect(g); g.connect(master); o.start(t); o.stop(t + 1.7); }); },
    rumble: function (dur) { dur = dur || 3; var n = AC.createBufferSource(); n.buffer = noiseBuf(dur); var f = AC.createBiquadFilter(); f.type = 'lowpass'; f.frequency.value = 140;
      var g = AC.createGain(), t = AC.currentTime; g.gain.setValueAtTime(0, t); g.gain.linearRampToValueAtTime(.7, t + dur * .4); g.gain.linearRampToValueAtTime(0, t + dur);
      n.connect(f); f.connect(g); g.connect(master); n.start(); },
    bubbles: function () { for (var k = 0; k < 6; k++) { var o = AC.createOscillator(), g = AC.createGain(), t = AC.currentTime + k * .13 + Math.random() * .05;
      o.frequency.setValueAtTime(300 + Math.random() * 300, t); o.frequency.exponentialRampToValueAtTime(900 + Math.random() * 600, t + .08);
      g.gain.setValueAtTime(.0, t); g.gain.linearRampToValueAtTime(.08, t + .01); g.gain.exponentialRampToValueAtTime(.001, t + .1); o.connect(g); g.connect(master); o.start(t); o.stop(t + .12); } },
    step: function () { var n = AC.createBufferSource(); n.buffer = noiseBuf(.28); var f = AC.createBiquadFilter(); f.type = 'lowpass'; f.frequency.value = 520; var g = AC.createGain(), t = AC.currentTime;
      g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.7, t + .03); g.gain.exponentialRampToValueAtTime(.001, t + .26); n.connect(f); f.connect(g); g.connect(master); n.start();
      var o = AC.createOscillator(), g2 = AC.createGain(); o.frequency.setValueAtTime(90, t); o.frequency.exponentialRampToValueAtTime(40, t + .2); g2.gain.setValueAtTime(.35, t); g2.gain.exponentialRampToValueAtTime(.001, t + .25); o.connect(g2); g2.connect(master); o.start(); o.stop(t + .3); },
    scan: function (dur) { dur = dur || 3; var o = AC.createOscillator(), g = AC.createGain(), t = AC.currentTime; o.type = 'sine'; o.frequency.setValueAtTime(320, t); o.frequency.linearRampToValueAtTime(980, t + dur);
      g.gain.setValueAtTime(.0001, t); g.gain.exponentialRampToValueAtTime(.08, t + .3); g.gain.setValueAtTime(.08, t + dur - .3); g.gain.exponentialRampToValueAtTime(.001, t + dur); o.connect(g); g.connect(master); o.start(); o.stop(t + dur + .05); },
    tick: function () { var o = AC.createOscillator(), g = AC.createGain(), t = AC.currentTime; o.type = 'square'; o.frequency.value = 2000;
      g.gain.setValueAtTime(.05, t); g.gain.exponentialRampToValueAtTime(.001, t + .03); o.connect(g); g.connect(master); o.start(t); o.stop(t + .04); }
  };
  function sfx(name, arg) { if (!sound || !ac() || !SFX[name]) return; try { SFX[name](arg); } catch (e) {} }

  /* ---------- particles + grain ---------- */
  var pctx = part.getContext('2d'), gctx = grain.getContext('2d'), P = [];
  function size() { var r = stage.getBoundingClientRect(), dpr = Math.min(2, window.devicePixelRatio || 1);
    part.width = r.width * dpr; part.height = r.height * dpr; grain.width = Math.max(1, r.width / 3 | 0); grain.height = Math.max(1, r.height / 3 | 0);
    D.shots.forEach(function (s) { if (s._cv) { s._cv.width = r.width * dpr; s._cv.height = r.height * dpr; s._cvReady = false; } }); }
  window.addEventListener('resize', size);
  function spawn(kind, n, x, y) {
    var W = part.width, H = part.height;
    for (var i = 0; i < n; i++) {
      if (kind === 'dust') P.push({ k: kind, x: Math.random() * W, y: Math.random() * H, vx: (Math.random() * .4 + .1) * W / 900, vy: (Math.random() - .5) * H / 1600, r: Math.random() * 2.2 + .6, a: Math.random() * .5 + .2, life: 1e9 });
      if (kind === 'bubble') P.push({ k: kind, x: Math.random() * W, y: H + Math.random() * H * .3, vx: 0, vy: -(Math.random() * 1.4 + .6) * H / 500, r: Math.random() * 5 + 2, a: .55, life: 1e9, ph: Math.random() * 6 });
      if (kind === 'chip') P.push({ k: kind, x: x, y: y, vx: (Math.random() - .3) * W / 160, vy: -(Math.random() * 1.2 + .2) * H / 160, r: Math.random() * 2.5 + 1, a: .9, life: 50 });
      if (kind === 'spark') P.push({ k: kind, x: W * (.2 + Math.random() * .6), y: H * (.35 + Math.random() * .3), vx: (Math.random() - .5) * W / 900, vy: -(Math.random() * .6 + .1) * H / 600, r: Math.random() * 1.8 + .5, a: 1, life: 120 + Math.random() * 80 });
    }
  }
  function stepParticles() {
    var W = part.width, H = part.height; pctx.clearRect(0, 0, W, H);
    for (var i = P.length - 1; i >= 0; i--) {
      var p = P[i]; p.life--; if (p.k === 'chip') p.vy += H / 9000;
      if (p.k === 'bubble') { p.ph += .08; p.x += Math.sin(p.ph) * .6; }
      p.x += p.vx; p.y += p.vy;
      if (p.life <= 0 || p.y < -20 || p.y > H + 60 || p.x > W + 20) { if (p.k === 'dust' && p.life > 0) { p.x = -10; p.y = Math.random() * H; } else { P.splice(i, 1); continue; } }
      var a = p.k === 'chip' ? p.a * p.life / 50 : p.k === 'spark' ? Math.min(1, p.life / 60) : p.a;
      pctx.beginPath(); pctx.arc(p.x, p.y, p.r * (W / 1100), 0, 6.283);
      if (p.k === 'bubble') { pctx.strokeStyle = 'rgba(220,245,255,' + a + ')'; pctx.lineWidth = 1.2; pctx.stroke(); }
      else { pctx.fillStyle = p.k === 'chip' ? 'rgba(214,198,166,' + a + ')' : p.k === 'spark' ? 'rgba(255,224,150,' + a + ')' : 'rgba(255,240,210,' + a + ')'; pctx.fill(); }
    }
  }
  var gimg = null, gtick = 0;
  function stepGrain() { if (RM) return; if (++gtick % 2) return; var w = grain.width, h = grain.height; if (!gimg || gimg.width !== w) gimg = gctx.createImageData(w, h);
    var d = gimg.data; for (var i = 0; i < d.length; i += 4) { var v = Math.random() * 255 | 0; d[i] = d[i + 1] = d[i + 2] = v; d[i + 3] = 255; } gctx.putImageData(gimg, 0, 0);
    flick.style.opacity = Math.random() < .04 ? .05 : 0; }

  /* ---------- reveal (brush away the dust) ---------- */
  function prepReveal(s) {
    var c = s._cv, x = c.getContext('2d'), W = c.width, H = c.height;
    x.globalCompositeOperation = 'source-over';
    var g = x.createLinearGradient(0, 0, W, H); g.addColorStop(0, '#d9ccb0'); g.addColorStop(1, '#c4b38f'); x.fillStyle = g; x.fillRect(0, 0, W, H);
    for (var i = 0; i < 2600; i++) { x.fillStyle = 'rgba(' + (Math.random() < .5 ? '90,74,50' : '250,240,220') + ',' + (Math.random() * .18) + ')';
      x.fillRect(Math.random() * W, Math.random() * H, Math.random() * 3 + 1, Math.random() * 3 + 1); }
    s._cvReady = true; s._stroke = 0;
  }
  function brushTo(s, prog) {
    var c = s._cv, x = c.getContext('2d'), W = c.width, H = c.height, N = 7;
    var target = Math.floor(prog * N * 30);
    x.globalCompositeOperation = 'destination-out'; x.lineCap = 'round';
    while (s._stroke < target) {
      var k = s._stroke++, row = Math.floor(k / 30), f = (k % 30) / 30, dir = row % 2 ? -1 : 1;
      var bx = W * (dir > 0 ? lerp(.04, .96, f) : lerp(.96, .04, f)), by = H * (.12 + row * .125) + Math.sin(f * 9) * H * .03;
      var rr = W * .075; var gr = x.createRadialGradient(bx, by, rr * .2, bx, by, rr);
      gr.addColorStop(0, 'rgba(0,0,0,.95)'); gr.addColorStop(1, 'rgba(0,0,0,0)'); x.fillStyle = gr; x.beginPath(); x.arc(bx, by, rr, 0, 6.283); x.fill();
      if (k % 3 === 0) spawn('chip', RM ? 0 : 5, bx, by);
      if (k % 10 === 0) sfx('brush');
    }
  }

  /* ---------- timeline ---------- */
  var t0 = 0, playing = false, paused = false, pauseAt = 0, raf = 0, fired = {}, capIdx = -1;
  function now() { return playing && !paused ? (performance.now() - t0) / 1000 : pauseAt; }
  function play() {
    ac(); if (AC && AC.state === 'suspended') AC.resume();
    cover.classList.add('wf-hidden'); stage.classList.add('wf-scope'); document.body.classList.add('wf-dim'); ctrl.classList.add('show'); setTimeout(function () { ctrl.classList.remove('show'); }, 2500);
    P.length = 0; fired = {}; capIdx = -1; size();
    D.shots.forEach(function (s) { s._cvReady = false; s._el.style.opacity = 0; if (s._tags) s._tags.forEach(function (t) { t.classList.remove('on'); }); s._el.classList.remove('on');
      if (s.type === 'flash') s._el.querySelectorAll('span').forEach(function (sp) { sp.classList.remove('on'); });
      if (s._xw) { s._xw.classList.remove('on'); s._xb.style.opacity = 0; } });
    if (D.music) { try { music.currentTime = 0; music.volume = sound ? (D.music.vol || .8) : 0; music.play().catch(function () {}); } catch (e) {} }
    t0 = performance.now(); playing = true; paused = false; bPause.innerHTML = '❚❚ Pause';
    cancelAnimationFrame(raf); raf = requestAnimationFrame(frame);
  }
  function stop(toEnd) {
    playing = false; cancelAnimationFrame(raf); music.pause(); Object.values(voices).forEach(function (a) { if (a) a.pause(); });
    stage.classList.remove('wf-scope'); document.body.classList.remove('wf-dim'); place.classList.remove('on'); count.classList.remove('on'); cap.classList.remove('on');
    if (toEnd) showEnd();
  }
  function once(key, fn) { if (!fired[key]) { fired[key] = 1; fn(); } }

  function frame() {
    var T = now();
    if (T >= END) { stop(true); return; }
    var placeText = '', countOn = false;
    D.shots.forEach(function (s, i) {
      var L = s._el, local = T - s.t, fin = s.fade == null ? .8 : s.fade, next = D.shots[i + 1];
      var visible = local >= -0.001 && local < s.d + (next ? (next.fade == null ? .8 : next.fade) : .6);
      if (!visible) { if (L.style.opacity !== '0') L.style.opacity = 0; return; }
      var op = clamp(local / fin, 0, 1); L.style.opacity = op; L.style.zIndex = 2 + i;
      var p = clamp(local / s.d, 0, 1), e = ease(p);
      if (s._img && s.from && !RM && s.type !== 'archive') {
        var a = s.from, b = s.to || s.from, sc = lerp(a[0], b[0], e), x = lerp(a[1], b[1], e), y = lerp(a[2], b[2], e);
        s._img.style.transform = 'scale(' + sc + ') translate(' + ((.5 - x) * 100 / sc * .9).toFixed(2) + '%,' + ((.5 - y) * 100 / sc * .9).toFixed(2) + '%)';
      }
      if (s.in === 'ripple' && !RM) { var rs = local < 1.6 ? 90 * (1 - local / 1.6) : 0; L.style.filter = rs > 0.5 ? 'url(#wfRipple)' : 'none'; rippleMap.setAttribute('scale', rs.toFixed(1)); }
      if (s.in === 'blur' && !RM) L.style.filter = local < 1.2 ? 'blur(' + (12 * (1 - local / 1.2)).toFixed(1) + 'px)' : 'none';
      if (local >= 0 && local < s.d) {
        if (s.place) placeText = s.place;
        if (s.count) { countOn = true; var cp = clamp(local / (s.count.dur || 2.2), 0, 1); count.querySelector('.num').textContent = Math.round(s.count.to * ease(cp)).toLocaleString('en-US');
          count.querySelector('.lab').textContent = s.count.label || 'years ago'; if (cp < 1 && Math.floor(local * 14) !== s._tk) { s._tk = Math.floor(local * 14); sfx('tick'); } }
        if (s.sfx) once('sfx' + i, function () { sfx(s.sfx, s.sfxArg); });
        if (s.fx && s.fx.indexOf('dust') > -1) once('dust' + i, function () { if (!RM) spawn('dust', 60); });
        if (s.fx && s.fx.indexOf('bubbles') > -1) { once('bub' + i, function () { sfx('bubbles'); }); if (!RM && Math.random() < .25) spawn('bubble', 1); }
        if (s._rays && !RM) s._rays.style.transform = 'translateX(' + (Math.sin(T * .5) * 3).toFixed(2) + '%)';
        if (s._sweep) s._sweep.style.backgroundPosition = '0 ' + (100 - 200 * p).toFixed(1) + '%';
        if (s.type === 'reveal') { if (!s._cvReady) prepReveal(s); var rp = clamp((local - (s.revealAt || .8)) / (s.revealDur || 5), 0, 1); brushTo(s, rp);
          if (rp >= 1) once('rv' + i, function () { sfx('shimmer'); s._cv.style.transition = 'opacity 1s'; s._cv.style.opacity = 0; }); else s._cv.style.opacity = 1; }
        if (s.type === 'flash') s._el.querySelectorAll('span').forEach(function (sp, k) { var at = (s.beats || [.1, .9])[k]; if (local >= at && !sp.classList.contains('on')) { sp.classList.add('on'); sfx('thump'); if (!RM) { stage.classList.remove('wf-shake'); void stage.offsetWidth; stage.classList.add('wf-shake'); } } });
        if (s._tags) s._tags.forEach(function (tg, k) { if (local >= s.tags[k].at) tg.classList.add('on'); });
        if (s.sfxAt) s.sfxAt.forEach(function (q, k) { if (local >= q.at) once('sa' + i + '_' + k, function () { sfx(q.name, q.arg); }); });
        if (s.type === 'xray') { var xa = s.xrayAt || 1, xd = s.xrayDur || 3.5, xp = clamp((local - xa) / xd, 0, 1), y0 = s.y0 != null ? s.y0 : 0, y1 = s.y1 != null ? s.y1 : .6;
          if (RM) { s._xb.style.opacity = 0; s._xw.classList.add('on'); }
          else { s._xb.style.top = ((y0 + (y1 - y0) * ease(xp)) * 100).toFixed(2) + '%'; s._xb.style.opacity = local >= xa ? (xp >= 1 ? .55 : 1) : 0;
            if (local >= xa) once('xs' + i, function () { sfx('scan', xd); });
            if (xp >= 1) once('xr' + i, function () { s._xw.classList.add('on'); sfx('shimmer'); }); } }
        if (s.type === 'title') { once('ti' + i, function () { L.classList.add('on'); sfx('shimmer'); if (!RM) spawn('spark', 70); }); }
        if (s.type === 'leader') once('ld' + i, function () { sfx('rumble', 3); });
      }
    });
    if (placeText) { if (place.dataset.t !== placeText) { place.dataset.t = placeText; place.innerHTML = '<b></b>' + placeText; } place.classList.add('on'); } else place.classList.remove('on');
    count.classList.toggle('on', countOn);
    // captions + optional voice
    var ci = -1; (D.captions || []).forEach(function (c, k) { if (T >= c.t && T < c.t + c.d) ci = k; });
    var flashOn = D.shots.some(function (s) { return s.type === 'flash' && T >= s.t && T < s.t + s.d; });
    if (ci !== capIdx) { capIdx = ci; if (ci > -1) { cap.textContent = D.captions[ci].text; cap.classList.toggle('on', !flashOn); var v = voices[ci]; if (v && sound) { try { v.currentTime = 0; v.play().catch(function () {}); } catch (e) {} } } else cap.classList.remove('on'); }
    var anyVoice = Object.keys(voices).some(function (k) { var a = voices[k]; return a && !a.paused; });
    if (D.music && sound) { var mv = D.music.vol || .8, tail = END - T; music.volume = clamp((anyVoice ? mv * .4 : mv) * (tail < 3 ? tail / 3 : 1), 0, 1); }
    stepParticles(); stepGrain();
    raf = requestAnimationFrame(frame);
  }

  bPause.onclick = function () {
    if (!playing) return;
    if (!paused) { pauseAt = now(); paused = true; music.pause(); bPause.innerHTML = '▶ Play'; Object.values(voices).forEach(function (a) { if (a) a.pause(); }); }
    else { t0 = performance.now() - pauseAt * 1000; paused = false; music.play().catch(function () {}); bPause.innerHTML = '❚❚ Pause'; }
  };
  bSkip.onclick = function () { stop(true); };
  bCC.onclick = function () { var on = stage.classList.toggle('wf-nocc'); bCC.setAttribute('aria-pressed', String(!on)); try { localStorage.setItem('wf-cc', on ? '0' : '1'); } catch (e) {} };
  bSnd.onclick = function () { sound = !sound; bSnd.setAttribute('aria-pressed', String(sound)); music.volume = sound ? (D.music && D.music.vol || .8) : 0; bSnd.innerHTML = sound ? '🔊 Sound' : '🔇 Muted'; };
  try { if (localStorage.getItem('wf-cc') === '0') { stage.classList.add('wf-nocc'); bCC.setAttribute('aria-pressed', 'false'); } } catch (e) {}
  stage.tabIndex = 0;
  stage.addEventListener('keydown', function (e) { if (e.code === 'Space' && playing) { e.preventDefault(); bPause.onclick(); } });
  document.addEventListener('visibilitychange', function () { if (document.hidden && playing && !paused) bPause.onclick(); });
  size(); showPoster();
  window.WF_FILM = { play: play, stop: stop, end: END, at: function () { return now(); } };
})();
