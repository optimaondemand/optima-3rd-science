/* Wonder Films lesson layer (G3 science) — mockup engine. Lesson content lives in window.WL_DATA. */
(function () {
  'use strict';
  var D = window.WL_DATA, IMG = window.WF_IMG || {};
  var $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var KEY = 'wl-' + D.id, S = {};
  try { S = JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) {}
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) {} }
  var RM = window.matchMedia && matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---- sounds (WebAudio, never on load) ---- */
  var AC = null;
  function ac() { if (!AC) try { AC = new (window.AudioContext || window.webkitAudioContext)(); } catch (e) {} return AC; }
  function tone(seq) { if (!ac()) return; var t = AC.currentTime; seq.forEach(function (n, i) { var o = AC.createOscillator(), g = AC.createGain(); o.type = n[2] || 'sine'; o.frequency.value = n[0];
    g.gain.setValueAtTime(0, t + n[1]); g.gain.linearRampToValueAtTime(.13, t + n[1] + .02); g.gain.exponentialRampToValueAtTime(.001, t + n[1] + .45); o.connect(g); g.connect(AC.destination); o.start(t + n[1]); o.stop(t + n[1] + .5); }); }
  var ding = function () { tone([[660, 0], [990, .1]]); }, cheer = function () { tone([[523, 0], [659, .1], [784, .2], [1047, .32]]); }, oops = function () { tone([[300, 0, 'triangle'], [240, .12, 'triangle']]); };
  function snapClap() { if (!ac()) return; var n = AC.createBufferSource(), b = AC.createBuffer(1, AC.sampleRate * .08, AC.sampleRate), d = b.getChannelData(0); for (var i = 0; i < d.length; i++) d[i] = (Math.random() * 2 - 1) * (1 - i / d.length); n.buffer = b; var g = AC.createGain(); g.gain.value = .35; n.connect(g); g.connect(AC.destination); n.start(); }

  function toast(msg) { var t = document.createElement('div'); t.className = 'wl-toast'; t.setAttribute('role', 'status'); t.innerHTML = msg + '<button aria-label="Close">✕</button>';
    $$('.wl-toast').slice(0, -2).forEach(function (o) { o.remove(); }); document.body.appendChild(t); var n = $$('.wl-toast').length; t.style.top = ($('.wl-top').offsetHeight + 10 + (n - 1) * 74) + 'px'; t.querySelector('button').onclick = function () { t.remove(); }; }
  /* smooth scroll so el's top sits just under the sticky top bar */
  function pin(el) { if (!el) return; var bar = $('.wl-top'), y = el.getBoundingClientRect().top + window.scrollY - (bar ? bar.offsetHeight : 0) - 12; window.scrollTo({ top: Math.max(0, y), behavior: RM ? 'auto' : 'smooth' }); }
  /* scroll only if el isn't already fully on screen below the top bar */
  function reveal(el) { if (!el) return; var bar = $('.wl-top'), top = bar ? bar.offsetHeight : 0, r = el.getBoundingClientRect();
    if (r.top >= top && r.bottom <= window.innerHeight) return;
    if (r.top < top || r.height > window.innerHeight - top - 24) { pin(el); return; }
    window.scrollBy({ top: r.bottom - window.innerHeight + 12, behavior: RM ? 'auto' : 'smooth' }); }  /* nudge up just enough */
  function glow(el) { if (!el) return; el.classList.add('wl-glow'); setTimeout(function () { el.classList.remove('wl-glow'); }, 1600); }

  /* ---- header ---- */
  $('#wl-details-btn').onclick = function () { var o = $('#wl-details').classList.toggle('open'); this.setAttribute('aria-expanded', o); };
  var mus = new Audio(); mus.loop = true; mus.volume = .18; if (IMG.music) mus.src = IMG.music;
  $('#wl-music').onclick = function () { var on = this.getAttribute('aria-pressed') !== 'true'; this.setAttribute('aria-pressed', on); if (on) mus.play().catch(function () {}); else mus.pause(); };
  $('#wl-motion').onclick = function () { var on = this.getAttribute('aria-pressed') !== 'true'; this.setAttribute('aria-pressed', on); document.documentElement.classList.toggle('wl-nomotion', !on); };

  /* ---- tabs (land at the top of the new section) ---- */
  function show(tab) {
    $$('.wl-tab').forEach(function (b) { b.setAttribute('aria-selected', b.dataset.tab === tab); });
    $$('.wl-panel').forEach(function (p) { p.classList.toggle('on', p.id === 'tab-' + tab); });
    var p = $('#tab-' + tab), sc = p.querySelector('.wl-scene');
    window.scrollTo({ top: p.getBoundingClientRect().top + window.scrollY - $('.wl-top').offsetHeight - 8, behavior: 'instant' });
    if (sc) { sc.classList.remove('snap'); setTimeout(function () { sc.classList.add('snap'); snapClap(); }, 120); }
    if (tab === 'assign') { wonderBack(); if (WL4.sketchSize) setTimeout(WL4.sketchSize, 30); }
    S.tab = tab; save();
  }
  $$('.wl-tab').forEach(function (b) { b.onclick = function () { show(b.dataset.tab); }; });
  $$('[data-go]').forEach(function (b) { b.onclick = function () { show(b.dataset.go); }; });
  function markTab(tab) { var b = $('.wl-tab[data-tab="' + tab + '"] .ck'); if (b) b.textContent = '✓'; }

  /* ---- every Word Wall word is defined where it is read: wrap its first use in each reading (whole word, plurals too) ---- */
  (function () {
    (D.words || []).forEach(function (w) {
      var word = w[1], meaning = w[2]; if (!word || !meaning) return;
      var re = new RegExp('\\b(' + word.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '(?:s|es)?)\\b', 'i');
      $$('.wl-read, .wl-card .wl-do, .wl-step p').forEach(function (box) {
        if ($$('.wl-glos', box).some(function (g) { return re.test(g.textContent); })) return;
        var tw = document.createTreeWalker(box, NodeFilter.SHOW_TEXT, { acceptNode: function (n) { return n.parentElement.closest('.wl-glos, button, a, .wl-choice, .wl-chip, textarea, label') ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT; } }), n;
        while ((n = tw.nextNode())) { var m = re.exec(n.nodeValue); if (!m) continue;
          var after = n.splitText(m.index); after.nodeValue = after.nodeValue.slice(m[1].length);
          var sp = document.createElement('span'); sp.className = 'wl-glos'; sp.dataset.tip = meaning; sp.textContent = m[1]; after.parentNode.insertBefore(sp, after); break; }
      });
    });
  })();
  /* ---- key words read aloud (clips: audio/word-<slug>.mp3; a 🔊 shows only when the clip exists) ---- */
  var wordAudio = null;
  function wordSlug(w) { return String(w || '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, ''); }
  function wordKey(t) { t = String(t || '').trim().toLowerCase(); var hit = null;
    (D.words || []).forEach(function (w) { var x = String(w[1] || '').toLowerCase(); if (t === x || t === x + 's' || t === x + 'es') hit = 'word-' + wordSlug(x); });
    return hit && IMG[hit] ? hit : null; }
  function sayWord(k) { try { if (wordAudio) wordAudio.pause(); wordAudio = new Audio(IMG[k]); wordAudio.play().catch(function () {}); } catch (e) {} }
  $$('.wl-wsay[data-word]').forEach(function (b) { var k = 'word-' + b.dataset.word; if (IMG[k]) { b.classList.add('ready'); b.onclick = function () { sayWord(k); }; } });
  /* ---- glossary ---- */
  $$('.wl-glos').forEach(function (g) {
    g.tabIndex = 0; var tip;
    function open() { if (tip) return; tip = document.createElement('span'); tip.className = 'wl-tip'; tip.textContent = g.dataset.tip; g.appendChild(tip);
      var k = wordKey(g.firstChild ? g.firstChild.nodeValue : ''); if (k) { var b = document.createElement('button'); b.type = 'button'; b.className = 'wl-wsay ready in-tip'; b.textContent = '🔊'; b.setAttribute('aria-label', 'Hear the word');
        b.addEventListener('mousedown', function (e) { e.preventDefault(); }); b.addEventListener('click', function (e) { e.stopPropagation(); sayWord(k); }); tip.insertBefore(b, tip.firstChild); } }
    function close() { if (tip) { tip.remove(); tip = null; } }
    g.addEventListener('mouseenter', open); g.addEventListener('mouseleave', close); g.addEventListener('focus', open); g.addEventListener('blur', close);
    g.addEventListener('click', function (e) { e.stopPropagation(); tip ? close() : open(); });
  });
  /* 🔊 buttons show only when the clip exists */
  $$('.wl-say').forEach(function (b) { var k = 'say-' + b.dataset.say; if (IMG[k]) { b.classList.add('ready'); b.onclick = function () { new Audio(IMG[k]).play(); }; } });

  /* ---- choices (generic) ---- */
  function choices(group, onOk) {
    var fb = group.nextElementSibling && group.nextElementSibling.classList.contains('wl-fb') ? group.nextElementSibling : null, key = 'c-' + group.dataset.choice;
    $$('.wl-choice', group).forEach(function (b, i) {
      b.onclick = function () {
        if (group.dataset.done) return;
        if (b.dataset.ok) { b.classList.add('ok'); group.dataset.done = 1; if (fb) { fb.className = 'wl-fb ok'; fb.textContent = b.dataset.ok; } ding(); S[key] = i; if (group.dataset.gather) S['g-' + group.dataset.gather] = b.textContent.trim(); save(); onOk && onOk(); gather(); checklist(); }
        else { b.classList.add('miss'); if (fb) { fb.className = 'wl-fb miss'; fb.textContent = b.dataset.miss; } oops(); }
      };
      if (S[key] === i) { b.classList.add('ok'); group.dataset.done = 1; if (fb) { fb.className = 'wl-fb ok'; fb.textContent = b.dataset.ok; } setTimeout(function () { onOk && onOk(true); }, 0); }
    });
  }

  /* ---- text inputs: counters, chips, saving ---- */
  var CHIPS = D.chips;
  function words(t) { return (t.trim().match(/[A-Za-z']+/g) || []).length; }
  function chipTest(id, t) { var c = CHIPS[id]; if (!c) return false; t = ' ' + t.toLowerCase() + ' '; if (c.re) return new RegExp(c.re, 'i').test(t); return c.any.some(function (w) { return t.indexOf(w) > -1; }); }
  $$('textarea[data-gather]').forEach(function (ta) {
    if (S['t-' + ta.id]) ta.value = S['t-' + ta.id];
    function upd() {
      var n = words(ta.value), min = +ta.dataset.min || 0, cnt = $('.wl-count[data-for="' + ta.id + '"]');
      if (cnt && min) { cnt.textContent = n + ' of ' + min + ' words'; cnt.classList.toggle('met', n >= min); }
      (ta.dataset.chips || '').split(',').forEach(function (c) { if (!c) return;
        $$('.wl-hint-chips span[data-chip="' + c + '"]').forEach(function (s) { if (s.parentNode.previousElementSibling === ta) s.classList.toggle('lit', chipTest(c, ta.value)); }); });
      S['t-' + ta.id] = ta.value; save(); gather(); checklist(); vocab();
    }
    ta.addEventListener('input', upd); upd();
  });
  function vocab() { var all = ['in-w1', 'in-w2', 'in-w3'].map(function (i) { return ($('#' + i) || {}).value || ''; }).join(' ').toLowerCase(), n = 0;
    $$('#vocab-chips span').forEach(function (s) { var on = new RegExp('\\b' + s.dataset.v).test(all); s.classList.toggle('lit', on); if (on) n++; });
    var vc = $('#vocab-count'); if (vc) { var need = +vc.dataset.need || 2; vc.textContent = 'Science words used: ' + n + ' of ' + need; vc.classList.toggle('met', n >= need); } return n; }

  var WL4 = window.WL4 = {};
  WL4.ctx = { D: D, IMG: IMG, S: S, save: save, $: $, $$: $$, RM: RM, ding: ding, cheer: cheer, oops: oops, toast: toast, glow: glow, pin: pin, reveal: reveal, choices: choices, words: words, chipTest: chipTest, gather: function () { return gather(); }, checklist: function () { checklist(); }, markTab: markTab, ac: ac, val: function (id) { return val(id); } };
  WL4_INIT(WL4);
  /* ---- flip cards ---- */
  $$('.wl-flip').forEach(function (f) { f.onclick = function () { f.classList.toggle('on'); }; });

  /* ---- order the scenes ---- */
  (function () {
    var O = D.order, tray = $('#order-tray'), slots = $$('#order-strip .wl-slot'), cap = $('#order-cap'), fb = $('#order-fb'), placed = S.order || [null, null, null, null], sel = null;
    var mix = O.mix;
    mix.forEach(function (idx) {
      var sc = O.scenes[idx], c = document.createElement('div'); c.className = 'wl-scard'; c.dataset.i = idx; c.tabIndex = 0; c.setAttribute('role', 'button');
      c.innerHTML = '<img src="' + IMG[sc.img] + '" alt="' + sc.alt + '">' + sc.text; tray.appendChild(c);
      c.addEventListener('click', function () { if (c.classList.contains('used')) return; $$('.wl-scard').forEach(function (x) { x.classList.remove('sel'); }); sel = idx; c.classList.add('sel'); cap.textContent = 'Now tap the frame where this scene goes.'; });
      c.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); c.click(); } });
      // drag with pointer
      c.addEventListener('pointerdown', function (e) {
        if (c.classList.contains('used')) return; var sx = e.clientX, sy = e.clientY, ghost = null, moved = false;
        function mv(ev) { if (!moved && Math.hypot(ev.clientX - sx, ev.clientY - sy) < 8) return; moved = true;
          if (!ghost) { ghost = c.cloneNode(true); ghost.classList.add('drag'); document.body.appendChild(ghost); }
          ghost.style.left = (ev.clientX - 85) + 'px'; ghost.style.top = (ev.clientY - 60) + 'px';
          slots.forEach(function (s) { var r = s.getBoundingClientRect(); s.classList.toggle('over', ev.clientX > r.left && ev.clientX < r.right && ev.clientY > r.top && ev.clientY < r.bottom); }); }
        function up(ev) { document.removeEventListener('pointermove', mv); document.removeEventListener('pointerup', up);
          if (ghost) ghost.remove(); var hit = slots.filter(function (s) { return s.classList.contains('over'); })[0]; slots.forEach(function (s) { s.classList.remove('over'); });
          if (moved && hit) { drop(idx, +hit.dataset.slot); } }
        document.addEventListener('pointermove', mv); document.addEventListener('pointerup', up);
      });
    });
    slots.forEach(function (s) { s.addEventListener('click', function () { if (sel != null) drop(sel, +s.dataset.slot); }); });
    function drop(idx, slot) {
      if (placed[slot] != null) return;
      if (idx !== slot) { fb.className = 'wl-fb miss'; fb.textContent = O.scenes[idx].miss[slot] || O.hint; oops(); glow(slots[slot]); return; }
      placed[slot] = idx; S.order = placed; save(); render(); ding(); sel = null;
    }
    function render() {
      slots.forEach(function (s, k) { if (placed[k] != null) { var sc = O.scenes[placed[k]]; s.innerHTML = '<img src="' + IMG[sc.img] + '" alt="' + sc.alt + '"><span class="num">' + (k + 1) + '</span>'; } });
      $$('.wl-scard').forEach(function (c) { c.classList.toggle('used', placed.indexOf(+c.dataset.i) > -1); c.classList.remove('sel'); });
      var n = placed.filter(function (x) { return x != null; }).length;
      fb.className = 'wl-fb ok'; fb.textContent = n ? (n < 4 ? 'Yes! Frame ' + n + ' is right. Which scene comes next?' : '') : '';
      cap.textContent = n < 4 ? 'Frame ' + (n + 1) + ' is empty. Which scene comes ' + (n ? 'next' : 'first') + '?' : '';
      if (n === 4 && !render.played) { render.played = 1; play(); }
    }
    function play() {
      /* The movie starts right away (it used to wait about 20 seconds while the four frames replayed one by one,
         which looked like the movie never loaded). No jump: the movie takes the scene cards' place. */
      cheer(); slots.forEach(function (s) { s.classList.remove('lit'); }); cap.textContent = '🎬 Your order is right. Now watch it as a movie!';
      tray.classList.add('wl-tray-done'); pin($('#order-strip'));
      setTimeout(function () { var th = tray.offsetHeight; tray.hidden = true; tray.classList.remove('wl-tray-done');
        WL4.movie(function () { $('#order-check').hidden = false; $('#fm-replay').hidden = false; }); ease(th); }, RM ? 0 : 700);
    }
    /* if the movie is shorter than the cards it replaced, close the gap slowly instead of snapping */
    function ease(th) { var mv = $('#fm-movie'), d = th - mv.offsetHeight - 10; if (d <= 0 || RM) return; mv.style.transition = 'none'; mv.style.marginBottom = (10 + d) + 'px'; void mv.offsetWidth;
      mv.style.transition = 'margin-bottom .9s ease'; setTimeout(function () { mv.style.marginBottom = ''; setTimeout(function () { mv.style.transition = ''; }, 1000); }, 700); }
    if (placed.filter(function (x) { return x != null; }).length === 4) render.played = 1;   /* already done: show the finished movie, do not replay */
    render();
    choices($('[data-choice="bone"]'), function () { S.orderDone = 1; save(); WL4.frame('formation'); });
    if (placed.filter(function (x) { return x != null; }).length === 4) { tray.hidden = true; $('#order-check').hidden = false; $('#fm-replay').hidden = false; WL4.movieStatic(); }
  })();

  /* ---- self-check: one question at a time ---- */
  (function () {
    var qs = $$('#m-quiz .wl-q'), i = S.qi || 0, score = S.qscore || 0, next = $('#quiz-next'), tried = {};
    function showQ() { qs.forEach(function (q, k) { q.classList.toggle('on', k === i); }); next.disabled = !qs[i].querySelector('.wl-choices').dataset.done; next.textContent = i < 2 ? 'Next question →' : 'See my score'; }
    qs.forEach(function (q, k) { var g = q.querySelector('.wl-choices');
      $$('.wl-choice', g).forEach(function (b) { b.addEventListener('click', function () { if (b.dataset.miss) tried[k] = 1; }); });
      choices(g, function (restored) { if (!restored && !tried[k]) { score++; S.qscore = score; save(); } if (k === i) next.disabled = false; }); });
    next.onclick = function () { if (i < 2) { i++; S.qi = i; save(); showQ(); } else { $('#quiz-score').hidden = false; $('#quiz-score').textContent = '🎬 You got ' + score + ' of 3 right on the first try!'; next.hidden = true; markTab('check'); cheer(); } };
    showQ();
  })();

  /* ---- assignment choices ---- */
  ['a1', 'a3'].forEach(function (k) { choices($('[data-choice="' + k + '"]')); });

  /* ---- Part C sketch (required) ---- */
  (function () {
    var cv = $('#sketch'), cx = cv.getContext('2d'), col = '#2B1D12', down = false;
    function size() { var r = cv.getBoundingClientRect(), d = window.devicePixelRatio || 1; if (!r.width || (cv.width === Math.round(r.width * d) && cv.height === Math.round(r.height * d))) return; var img = cv.width ? cx.getImageData(0, 0, cv.width, cv.height) : null; cv.width = Math.round(r.width * d); cv.height = Math.round(r.height * d); cx.setTransform(d, 0, 0, d, 0, 0); cx.lineCap = 'round'; cx.lineJoin = 'round'; cx.lineWidth = 4; if (S.sketch) { var im = new Image(); im.onload = function () { cx.drawImage(im, 0, 0, r.width, r.height); }; im.src = S.sketch; } }
    WL4.sketchSize = size; setTimeout(size, 50); window.addEventListener('resize', size);
    function pt(e) { var r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
    cv.addEventListener('pointerdown', function (e) { down = true; cv.setPointerCapture(e.pointerId); var p = pt(e); cx.strokeStyle = col; cx.beginPath(); cx.moveTo(p[0], p[1]); });
    cv.addEventListener('pointermove', function (e) { if (!down) return; var p = pt(e); cx.lineTo(p[0], p[1]); cx.stroke(); });
    cv.addEventListener('pointerup', function () { if (!down) return; down = false; try { S.sketch = cv.toDataURL('image/png'); save(); } catch (e) {} gather(); checklist(); });
    $$('#sk-tools button[data-c]').forEach(function (b) { b.onclick = function () { col = b.dataset.c; $$('#sk-tools button').forEach(function (x) { x.classList.toggle('on', x === b); }); }; });
    $('#sk-clear').onclick = function () { cx.clearRect(0, 0, cv.width, cv.height); delete S.sketch; save(); gather(); checklist(); };
    /* the drawing is turned in as a picture: white background, so it reads in Canvas */
    function png() { var o = document.createElement('canvas'); o.width = cv.width; o.height = cv.height; var c = o.getContext('2d'); c.fillStyle = '#fff'; c.fillRect(0, 0, o.width, o.height); c.drawImage(cv, 0, 0); return o.toDataURL('image/png'); }
    WL4.sketchPng = function () { return S.sketch ? png() : ''; };
    $('#sk-save').onclick = function () { if (!S.sketch) { toast('🎨 Draw your picture first, then save it.'); glow(cv); return; } var a = document.createElement('a'); a.href = png(); a.download = 'lesson-' + D.lesson.replace('.', '-') + '-my-drawing.png'; a.click(); toast('🎨 Saved! Upload this picture to Canvas with your answers.'); };
  })();

  /* ---- Start here: one how-to video (Opti) for every lesson, in a closed drawer at the top of the Warm-Up ---- */
  (function () {
    var first = $('#tab-warm'); if (!first) return;
    var base = D.startHere || 'assets/video/start-here/g3sci-start-here';
    // build_page.py writes the drawer into the page so nothing moves on load; older pages get it here
    var d = $('.wl-start'), made = !d; if (made) { d = document.createElement('details'); d.className = 'wl-start'; }
    if (made) {
      d.innerHTML = '<summary><span class="wl-start-k">▶ Start here</span><span class="wl-start-t">How your Wonder Films lessons work</span><span class="wl-start-m">1-minute video</span><span class="wl-start-o">Open ▾</span></summary><div class="wl-start-b"></div>';
      var sc = first.querySelector('.wl-scene'); first.insertBefore(d, sc ? sc.nextSibling : first.firstChild);
    }
    d.addEventListener('toggle', function () {
      var v = d.querySelector('video'); if (!d.open) { if (v) v.pause(); return; } if (v) return;
      d.querySelector('.wl-start-b').innerHTML = '<video controls playsinline preload="metadata" poster="' + base + '.jpg"><source src="' + base + '.mp4" type="video/mp4"><track kind="captions" srclang="en" label="English" src="' + base + '.vtt" default></video><p class="wl-start-n">Captions are on. To turn them off, press CC on the video.</p>';
    });
  })();
  /* ---- click cues (pilot feedback, like the other G3 courses): a bouncing 👆 sits on the next thing to touch in each
         activity and leaves on the first touch. It points at a group of choices, never at one answer. ---- */
  (function () {
    if (window.WL_NO_CUES) return;
    var vis = function (e) { return e && e.offsetParent !== null && !e.closest('[hidden]') && e.getClientRects().length; };
    var first = function (sel, root) { return $$(sel, root).filter(vis)[0] || null; };
    function nextIn(m) {
      var n = first('.wl-nextstep', m); if (n) return [n];
      var id = m.id, g;
      if (id === 'm-spec') { return (S.specFound || []).length < 3 ? [first('#spec-open', m)] : null; }
      if (id === 'm-order') {
        if (vis($('#order-tray'))) { var sel = first('.wl-scard.sel', m); return sel ? [first('.wl-slot:not(:has(img))', m)] : [first('.wl-scard:not(.used)', m)]; }
        g = first('#order-check .wl-choices', m); return g && !g.dataset.done ? [g, 1] : null;
      }
      if (id === 'm-bite') {
        var box = $('#bite-step');
        if (vis($('#bite-mats'))) {
          var sm = first('.wl-mat.sel', m), empty = $$('.wl-drop', m).filter(function (d) { return !d.querySelector('img,.wl-swatch'); })[0], pb = $('#bite-press');
          if (sm && empty) return [empty];
          if (pb && !pb.disabled && !empty) return [pb];
          if (pb && !pb.disabled && box && /Try swapping/.test(box.textContent)) return [first('.wl-mat', m)];
          return empty ? [first('.wl-mat', m)] : (pb && !pb.disabled ? [pb] : null);
        }
        g = $$('#bite-step .wl-chips[data-k]', m).filter(function (x) { return vis(x) && !x.querySelector('.on'); })[0]; if (g) return [g, 1];
        if (box && /Tap a tray/.test(box.textContent)) return [first('.wl-trays', m), 1];
        return null;
      }
      if (id === 'm-dig') {
        var pr = first('#dig-predict', m); if (pr && pr.querySelector('.wl-chip') && !pr.querySelector('.on')) return [pr, 1];
        g = first('#dig-card .wl-choices', m); if (g && !g.dataset.done) return [g, 1];
        var b = first('.wl-band.active', m); if (b) return [b];
        g = first('[data-choice="mix"]', m); return g && !g.dataset.done ? [g, 1] : null;
      }
      if (id === 'm-det') {
        g = first('#det-work .wl-chips', m); if (g) return [g, 1];
        var solved = Object.keys(S.det || {}).filter(function (k) { return S.det[k].done; }).length;
        return solved < (D.det.need || 3) ? [first('.wl-dcard:not(.done)', m)] : null;
      }
      if (id === 'm-quiz') { g = first('.wl-q.on .wl-choices', m); if (g && !g.dataset.done) return [g, 1]; var qn = $('#quiz-next'); return qn && vis(qn) && !qn.disabled ? [qn] : null; }
      if (id === 'm-premiere') { var pbn = $('#premiere-btn'); return pbn && !pbn.disabled ? [pbn] : null; }
      return null;
    }
    var hands = {}, quiet = {};
    function place(key, t, group) {
      var h = hands[key]; if (!h) { h = hands[key] = document.createElement('div'); h.className = 'wl-cue'; h.textContent = '👆'; h.setAttribute('aria-hidden', 'true'); document.body.appendChild(h); }
      var r = t.getBoundingClientRect(), x = group ? r.left + Math.min(28, r.width / 2) : r.left + r.width / 2, y = r.bottom;
      h.style.left = (x + window.scrollX - 14) + 'px'; h.style.top = (y + window.scrollY - 6) + 'px'; h.hidden = false; h._t = t;
    }
    function tick() {
      var panel = $('.wl-panel.on'), seen = {};
      var film = first('.wf-cover .wf-btn'); if (film && !quiet.film) { place('film', film); seen.film = 1; }
      if (panel) $$('[id^="m-"]', panel).forEach(function (m) {
        if (quiet[m.id] || !vis(m)) return; var r = nextIn(m); if (!r || !r[0] || !vis(r[0])) return;
        place(m.id, r[0], r[1]); seen[m.id] = 1; });
      Object.keys(hands).forEach(function (k) { if (!seen[k]) hands[k].hidden = true; });
    }
    document.addEventListener('pointerdown', function (e) {   /* the hand leaves on the first touch of what it points at */
      Object.keys(hands).forEach(function (k) { var h = hands[k]; if (!h.hidden && h._t && h._t.contains(e.target)) { h.hidden = true; quiet[k] = 1; setTimeout(function () { quiet[k] = 0; }, 900); } });
    }, true);
    setInterval(tick, 400); window.addEventListener('resize', tick); tick();
  })();
  /* ---- wonder callback ---- */
  // the Scene 1 question shows here; if the Warm-Up box was left empty, the student writes it right here (never "go to the Warm-Up")
  function wonderBack() { var src = $('#in-wonder'), w = (src || {}).value || '', el = $('#wonder-back'), here = $('#wonder-here'), box = $('#in-wonder2'); if (!el) return;
    if (box && !box.dataset.on) { box.dataset.on = '1'; box.addEventListener('input', function () { if (!src) return; src.value = box.value; src.dispatchEvent(new Event('input', { bubbles: true })); }); }
    if (w.trim() && !(box && document.activeElement === box)) { el.innerHTML = '<b>Your question:</b> “' + w.trim().replace(/</g, '&lt;') + '”'; if (here) here.hidden = true; } }

  /* ---- gather + checklist + reel ---- */
  function gather() {
    var out = ['Lesson ' + D.lesson + ' · ' + D.title, ''];
    var det = S.det || {}; var rows = Object.keys(det).filter(function (k) { return det[k].done; });
    if (rows.length) { out.push('EVIDENCE CHART'); rows.forEach(function (k) { var f = D.det.items[k]; out.push(D.det.noun + ' ' + f.id + ': I observe ' + det[k].clue.toLowerCase() + ' · ' + f.org[f.orgAns] + ' · ' + f.env); }); out.push(''); }
    if (S.sketch) out.push('Part C drawing: done (upload the saved picture too)\n');
    $$('textarea[data-gather], .wl-choices[data-gather]').forEach(function (el) { var v = el.tagName === 'TEXTAREA' ? el.value.trim() : (S['g-' + el.dataset.gather] || ''); if (v) out.push(el.dataset.gather + ':\n' + v + '\n'); });
    var g = $('#gather-out'); if (g) g.textContent = out.length > 2 ? out.join('\n') : '(Your answers show up here as you write.)';
    return out.join('\n');
  }
  function val(id) { return (($('#' + id) || {}).value || ''); }
  function checklist() {
    var det = S.det || {}, n = Object.keys(det).filter(function (k) { return det[k].done; }).length;
    var ck = {}; (D.assign.checklist || []).forEach(function (c) { var r = c.req || {}, ok = true;
      if (r.det && n < r.det) ok = false;
      (r.choice || []).forEach(function (k) { if (S['c-' + k] == null) ok = false; });
      Object.keys(r.text || {}).forEach(function (id) { if (words(val(id)) < r.text[id]) ok = false; });
      if (r.vocab && vocab() < r.vocab) ok = false;
      if (r.sketch && !S.sketch) ok = false; ck[c.k] = ok; });
    var man = S.ckMan || {}, all = true;
    $$('#checklist li').forEach(function (li) { var k = li.dataset.ck, d = !!ck[k] || man[k] === true; li.classList.toggle('auto', !!ck[k]); li.classList.toggle('done', d); li.setAttribute('aria-checked', d); if (!d) all = false; });
    $$('.wl-amap-b[data-ck]').forEach(function (b) { var k = b.dataset.ck, d = !!ck[k] || man[k] === true; b.classList.toggle('done', d); });
    if (window.WL4 && WL4.reel) WL4.reel(all); else window.__ck = all;
  }
  /* ---- Assignment map (Bethany, 11 Nov 2026): one line at the top of the Assignment listing its parts.
     Each chip jumps to its part and gets a check when the checklist says that part is done. ---- */
  (function () {
    var tab = $('#tab-assign'); if (!tab || D.assignMap === false || $('.wl-amap', tab)) return;
    function head(re) { var hs = $$('h3 .k', tab); for (var i = 0; i < hs.length; i++) if (re.test(hs[i].textContent)) return hs[i].parentNode; return null; }
    var A = D.assign || {}, jobs = [];
    function q(o) { var n = ((o || {}).items || []).length; return n ? ' \u00B7 ' + n + ' question' + (n === 1 ? '' : 's') : ''; }
    var hA = head(/Part A/), hB = head(/Part B/), hW = head(/Write and explain/), hC = $('#partc', tab), hP = $('#m-premiere', tab);
    if (hA) jobs.push(['Part A' + q(A.partA), hA, 'a']);
    if (hB) jobs.push(['Part B' + q(A.partB), hB, 'b']);
    if (hW) jobs.push(['Write and explain', hW, 'w']);
    if (hC) jobs.push(['Part C \u00B7 draw and label', hC, 'c']);
    if (hP) jobs.push(['Premiere your film', hP, '']);
    if (jobs.length < 2 || !hA) return;
    var box = document.createElement('div'); box.className = 'wl-amap';
    box.innerHTML = '<b>\uD83D\uDDFA In this scene \u00B7 ' + jobs.length + ' things to do</b><ol></ol>';
    var ol = box.querySelector('ol');
    jobs.forEach(function (j, i) { var li = document.createElement('li'), b = document.createElement('button'); b.type = 'button'; b.className = 'wl-amap-b'; if (j[2]) b.dataset.ck = j[2];
      b.innerHTML = '<span>' + (i + 1) + '</span>' + j[0]; b.addEventListener('click', function () { pin(j[1]); }); li.appendChild(b); ol.appendChild(li); });
    var card = hA.closest('.wl-card') || hA.parentNode; card.parentNode.insertBefore(box, card);
  })();
  $$('#checklist li').forEach(function (li) {
    li.setAttribute('role', 'checkbox'); li.tabIndex = 0;
    function flip() { if (li.classList.contains('auto')) { toast('✅ This one checked itself because the work is done.'); return; }
      var man = S.ckMan = S.ckMan || {}; man[li.dataset.ck] = !li.classList.contains('done'); save(); if (man[li.dataset.ck]) ding(); checklist(); }
    li.addEventListener('click', flip);
    li.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); flip(); } });
  });
  $('#g-copy').onclick = function () { var t = gather(); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { toast('📋 Copied! Paste it into Canvas.'); }, function () { toast('Select the text in the box and copy it.'); }); };
  $('#g-dl').onclick = function () { var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([gather()], { type: 'text/plain' })); a.download = 'lesson-' + D.lesson.replace('.', '-') + '-my-answers.txt'; a.click(); };
  $('#g-print').onclick = function () { var w = window.open(''); if (!w) return; var im = WL4.sketchPng ? WL4.sketchPng() : ''; w.document.write('<pre style="font:16px/1.5 sans-serif;white-space:pre-wrap">' + gather().replace(/</g, '&lt;') + '</pre>' + (im ? '<p style="font:bold 16px sans-serif">Part C drawing</p><img src="' + im + '" style="max-width:100%;border:1px solid #999">' : '')); w.document.close(); setTimeout(function () { w.print(); }, 300); };

  /* tab ticks */
  function ticks() { if ((S.specFound || []).length >= 3 && words(val('in-notice')) >= 4 && words(val('in-wonder')) >= 4) markTab('warm');
    var F = S.frames || {}; if (D.premiere.frames.every(function (f) { return F[f.k]; }) && words(val('in-det')) >= (D.det.write.min || 15)) markTab('lesson'); if (S.reel) markTab('assign'); }
  document.addEventListener('click', function () { setTimeout(ticks, 50); }); document.addEventListener('input', ticks);
  gather(); checklist(); ticks();
  if (S.tab && S.tab !== 'warm') show(S.tab);
  window.WL = { state: S, show: show };
  WL4.after && WL4.after();
})();
