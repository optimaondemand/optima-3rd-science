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
    if (tab === 'assign') wonderBack();
    S.tab = tab; save();
  }
  $$('.wl-tab').forEach(function (b) { b.onclick = function () { show(b.dataset.tab); }; });
  $$('[data-go]').forEach(function (b) { b.onclick = function () { show(b.dataset.go); }; });
  function markTab(tab) { var b = $('.wl-tab[data-tab="' + tab + '"] .ck'); if (b) b.textContent = '✓'; }

  /* ---- glossary ---- */
  $$('.wl-glos').forEach(function (g) {
    g.tabIndex = 0; var tip;
    function open() { if (tip) return; tip = document.createElement('span'); tip.className = 'wl-tip'; tip.textContent = g.dataset.tip; g.appendChild(tip); }
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
  WL4.ctx = { D: D, IMG: IMG, S: S, save: save, $: $, $$: $$, RM: RM, ding: ding, cheer: cheer, oops: oops, toast: toast, glow: glow, choices: choices, words: words, chipTest: chipTest, gather: function () { return gather(); }, checklist: function () { checklist(); }, markTab: markTab, ac: ac, val: function (id) { return val(id); } };
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
      var k = 0; cheer(); tray.hidden = true;
      (function step() { slots.forEach(function (s, j) { s.classList.toggle('lit', j === k); }); cap.textContent = (k + 1) + '. ' + O.scenes[k].play;
        if (++k < 4) setTimeout(step, RM ? 400 : 1300); else setTimeout(function () { slots.forEach(function (s) { s.classList.remove('lit'); }); cap.textContent = '🎬 Your order is right. Now watch it as a movie!'; WL4.movie(function () { $('#order-check').hidden = false; $('#fm-replay').hidden = false; }); }, RM ? 400 : 1300); })();
    }
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

  /* ---- sketch (bonus) ---- */
  (function () {
    var cv = $('#sketch'), cx = cv.getContext('2d'), col = '#2B1D12', down = false;
    function size() { var r = cv.getBoundingClientRect(), d = window.devicePixelRatio || 1, img = cv.width ? cx.getImageData(0, 0, cv.width, cv.height) : null; cv.width = r.width * d; cv.height = r.height * d; cx.scale(d, d); cx.lineCap = 'round'; cx.lineJoin = 'round'; cx.lineWidth = 4; if (S.sketch) { var im = new Image(); im.onload = function () { cx.drawImage(im, 0, 0, r.width, r.height); }; im.src = S.sketch; } }
    var dr = $('#partc'); if (dr) dr.addEventListener('toggle', function () { if (dr.open) size(); }); else setTimeout(size, 50);
    function pt(e) { var r = cv.getBoundingClientRect(); return [e.clientX - r.left, e.clientY - r.top]; }
    cv.addEventListener('pointerdown', function (e) { down = true; cv.setPointerCapture(e.pointerId); var p = pt(e); cx.strokeStyle = col; cx.beginPath(); cx.moveTo(p[0], p[1]); });
    cv.addEventListener('pointermove', function (e) { if (!down) return; var p = pt(e); cx.lineTo(p[0], p[1]); cx.stroke(); });
    cv.addEventListener('pointerup', function () { down = false; try { S.sketch = cv.toDataURL('image/png'); save(); } catch (e) {} });
    $$('#sk-tools button[data-c]').forEach(function (b) { b.onclick = function () { col = b.dataset.c; $$('#sk-tools button').forEach(function (x) { x.classList.toggle('on', x === b); }); }; });
    $('#sk-clear').onclick = function () { cx.clearRect(0, 0, cv.width, cv.height); delete S.sketch; save(); };
  })();

  /* ---- wonder callback ---- */
  function wonderBack() { var w = ($('#in-wonder') || {}).value || ''; var el = $('#wonder-back'); if (w.trim()) el.innerHTML = '<b>Your question:</b> “' + w.trim().replace(/</g, '&lt;') + '”'; }

  /* ---- gather + checklist + reel ---- */
  function gather() {
    var out = ['Lesson ' + D.lesson + ' · ' + D.title, ''];
    var det = S.det || {}; var rows = Object.keys(det).filter(function (k) { return det[k].done; });
    if (rows.length) { out.push('EVIDENCE CHART'); rows.forEach(function (k) { var f = D.det.items[k]; out.push(D.det.noun + ' ' + f.id + ': I observe ' + det[k].clue.toLowerCase() + ' · ' + f.org[f.orgAns] + ' · ' + f.env); }); out.push(''); }
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
      if (r.vocab && vocab() < r.vocab) ok = false; ck[c.k] = ok; });
    var man = S.ckMan || {}, all = true;
    $$('#checklist li').forEach(function (li) { var k = li.dataset.ck, d = k in man ? man[k] : !!ck[k]; li.classList.toggle('done', d); li.setAttribute('aria-checked', d); if (!d) all = false; });
    if (window.WL4 && WL4.reel) WL4.reel(all); else window.__ck = all;
  }
  $$('#checklist li').forEach(function (li) {
    li.setAttribute('role', 'checkbox'); li.tabIndex = 0;
    function flip() { var man = S.ckMan = S.ckMan || {}; man[li.dataset.ck] = !li.classList.contains('done'); save(); if (man[li.dataset.ck]) ding(); checklist(); }
    li.addEventListener('click', flip);
    li.addEventListener('keydown', function (e) { if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); flip(); } });
  });
  $('#g-copy').onclick = function () { var t = gather(); (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { toast('📋 Copied! Paste it into Canvas.'); }, function () { toast('Select the text in the box and copy it.'); }); };
  $('#g-dl').onclick = function () { var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([gather()], { type: 'text/plain' })); a.download = 'lesson-' + D.lesson.replace('.', '-') + '-my-answers.txt'; a.click(); };
  $('#g-print').onclick = function () { var w = window.open(''); if (!w) return; w.document.write('<pre style="font:16px/1.5 sans-serif;white-space:pre-wrap">' + gather().replace(/</g, '&lt;') + '</pre>'); w.print(); };

  /* tab ticks */
  function ticks() { if ((S.specFound || []).length >= 3 && words(val('in-notice')) >= 4 && words(val('in-wonder')) >= 4) markTab('warm');
    var F = S.frames || {}; if (D.premiere.frames.every(function (f) { return F[f.k]; }) && words(val('in-det')) >= (D.det.write.min || 15)) markTab('lesson'); if (S.reel) markTab('assign'); }
  document.addEventListener('click', function () { setTimeout(ticks, 50); }); document.addEventListener('input', ticks);
  gather(); checklist(); ticks();
  if (S.tab && S.tab !== 'warm') show(S.tab);
  window.WL = { state: S, show: show };
  WL4.after && WL4.after();
})();
