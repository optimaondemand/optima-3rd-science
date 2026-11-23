/* G3 Science VR · On Location engine. No week words: everything comes from window.VR (built from week.json). */
(function () {
  var V = window.VR || {}, G = V.game || {}, PRE = V.pre || 'g3sci-vr';
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  function load() { try { return JSON.parse(localStorage.getItem(PRE) || '{}'); } catch (e) { return {}; } }
  var st = load();
  st.steps = st.steps || []; st.m = st.m || []; st.p = st.p || []; st.w = st.w || ['', ''];
  function save() { try { localStorage.setItem(PRE, JSON.stringify(st)); } catch (e) {} }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function words(s) { return (String(s).replace(/___/g, ' ').match(/[A-Za-z0-9’']+/g) || []).length; }

  /* details pill */
  var db = $('#wl-details-btn'), dd = $('#wl-details');
  if (db && dd) db.addEventListener('click', function () { var o = dd.classList.toggle('open'); db.setAttribute('aria-expanded', o); });

  /* audio */
  var audio = null, playing = null;
  $$('.vr-play').forEach(function (b) {
    b.addEventListener('click', function () {
      var c = b.getAttribute('data-clip');
      if (audio) { audio.pause(); }
      $$('.vr-play').forEach(function (x) { x.classList.remove('on'); });
      if (playing === b) { playing = null; return; }
      audio = new Audio(V.clips[c]); playing = b; b.classList.add('on');
      audio.onended = function () { b.classList.remove('on'); playing = null; };
      audio.play().catch(function () { b.classList.remove('on'); });
    });
  });

  /* teacher video: shown only when the file exists */
  if (V.video && window.fetch) {
    fetch(V.video, { method: 'HEAD' }).then(function (r) {
      if (r.ok) { var w = $('#vr-video'); $('video', w).src = V.video; w.hidden = false; }
    }).catch(function () {});
  }

  /* path toggle */
  function showPath(id) {
    $$('.vr-path').forEach(function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-path') === id); });
    $$('.vr-pane').forEach(function (p) { p.classList.toggle('on', p.id === id); });
    st.path = id; save();
  }
  $$('.vr-path').forEach(function (b) {
    b.addEventListener('click', function () {
      showPath(b.getAttribute('data-path'));
      var p = $('#' + b.getAttribute('data-path')); if (p) p.scrollIntoView({ behavior: 'smooth', block: 'start' });
    });
  });
  if (st.path) showPath(st.path);

  /* checklist */
  var steps = $$('.vr-step');
  function paintSteps() {
    var n = 0;
    steps.forEach(function (s, i) {
      var d = !!st.steps[i]; if (d) n++;
      s.classList.toggle('done', d);
      var b = $('.vr-chk', s); b.textContent = d ? '✓' : ''; b.setAttribute('aria-pressed', d);
    });
    var t = $('#vr-prog-t'), bar = $('#vr-prog-b');
    if (t) t.textContent = n + ' of ' + steps.length + ' steps done';
    if (bar) bar.style.width = (100 * n / steps.length) + '%';
    var sent = $('#vr-sent'); if (sent) sent.checked = !!st.sent;
    var bd = $('#vr-badge'); if (bd) bd.classList.toggle('on', n === steps.length && !!st.sent);
  }
  steps.forEach(function (s, i) {
    $('.vr-chk', s).addEventListener('click', function () { st.steps[i] = !st.steps[i]; save(); paintSteps(); });
  });
  var sent = $('#vr-sent');
  if (sent) sent.addEventListener('change', function () {
    st.sent = sent.checked;
    if (sent.checked) steps.forEach(function (s, i) { st.steps[i] = true; });
    save(); paintSteps();
  });
  paintSteps();

  /* help drawer: load the video and images only when opened */
  var help = $('#vr-help');
  if (help) help.addEventListener('toggle', function () {
    if (!help.open) return;
    var f = $('iframe[data-src]', help); if (f && !f.src) f.src = f.getAttribute('data-src');
  });

  /* ---------- Studio Day: match game. Two looks, both from DATA:
     default  = drag the card onto a picture (week 17, cousins match)
     dragOpts = drag a picture onto the card (week 18, casting call) ---------- */
  var game = $('#vr-game'), P = G.pairs || [], C = G.cousins || [], L = G.labels || {};
  function cz(k) { return C.filter(function (x) { return x.key === k; })[0]; }
  var drag = null;
  function frames() {
    P.forEach(function (p, i) {
      var f = $('.vr-frame[data-f="' + i + '"]'); if (!f) return;
      var lit = st.m[i] && st.p[i];
      f.classList.toggle('lit', !!lit);
      $('.pl', f).textContent = lit ? (G.framePl === 'tag' ? L.tag : G.framePl === 'bin' ? G.bins[p.bin] : G.framePl === 'cousin' ? cz(p.cousin).name : G.places[p.place]) : '';
    });
  }
  function cur() { for (var i = 0; i < P.length; i++) if (!(st.m[i] && st.p[i])) return i; return -1; }
  function render() {
    frames();
    var i = cur();
    if (i < 0) {
      game.innerHTML = '<div class="vr-fb ok">' + esc(L.done) + '</div>';
      $('#vr-write').hidden = false; checkStamp(); return;
    }
    $('#vr-write').hidden = true;
    if (G.type === 'fly') { renderFly(); return; }
    if (G.type === 'clean') { renderClean(); return; }
    if (G.type === 'spot') { renderSpot(); return; }
    if (G.type === 'sort') { renderSort(i, P[i]); return; }
    var p = P[i], h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(p.name) + '</div><div class="vr-q">' +
      '<div class="vr-fossil"' + (G.dragOpts ? '' : ' draggable="true"') + ' id="vr-fos"><img src="' + p.img + '" alt="' + esc(p.alt) + '">' + esc(p.name) + (p.facts ? '<small>' + esc(p.facts) + '</small>' : '') + '</div><div>';
    if (!st.m[i]) {
      h += '<div class="vr-opts">' + C.map(function (c) {
        return '<button class="vr-opt" type="button" data-k="' + c.key + '"' + (G.dragOpts ? ' draggable="true"' : '') + '><img src="' + c.img + '" alt="' + esc(c.alt) + '">' + esc(c.name) + '</button>';
      }).join('') + '</div>';
    } else {
      var c = C.filter(function (x) { return x.key === p.cousin; })[0];
      h += '<div class="vr-opts" style="grid-template-columns:1fr"><div class="vr-opt ok"><img src="' + c.img + '" alt="' + esc(c.alt) + '">' + esc(c.name) + '</div></div>' +
        '<div class="vr-fb ok">' + esc(p.ok) + '</div><div class="vr-gstep">' + esc(L.q2) + '</div><div class="vr-place">' +
        Object.keys(G.places).map(function (k) { return '<button type="button" data-pl="' + k + '">' + esc(G.places[k]) + '</button>'; }).join('') + '</div>';
    }
    h += '<div class="vr-fb" id="vr-fb" aria-live="polite"></div></div></div>';
    game.innerHTML = h;
    var fb = $('#vr-fb');
    function pick(k, el) {
      if (k === p.cousin) { st.m[i] = true; save(); render(); }
      else { fb.className = 'vr-fb no'; fb.textContent = G.miss; if (el) { el.classList.remove('no'); void el.offsetWidth; el.classList.add('no'); } }
    }
    $$('.vr-opt[data-k]', game).forEach(function (b) {
      b.addEventListener('click', function () { pick(b.getAttribute('data-k'), b); });
      b.addEventListener('dragover', function (e) { if (G.dragOpts) return; e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) { e.preventDefault(); b.classList.remove('drop'); if (!G.dragOpts) pick(b.getAttribute('data-k'), b); });
    });
    var fos = $('#vr-fos');
    if (fos && !G.dragOpts) fos.addEventListener('dragstart', function (e) { try { e.dataTransfer.setData('text/plain', 'f'); } catch (x) {} });
    if (fos && G.dragOpts && !st.m[i]) {
      $$('.vr-opt[data-k]', game).forEach(function (b) {
        b.addEventListener('dragstart', function (e) { drag = b; try { e.dataTransfer.setData('text/plain', b.getAttribute('data-k')); } catch (x) {} });
      });
      fos.addEventListener('dragover', function (e) { e.preventDefault(); fos.classList.add('drop'); });
      fos.addEventListener('dragleave', function () { fos.classList.remove('drop'); });
      fos.addEventListener('drop', function (e) { e.preventDefault(); fos.classList.remove('drop'); if (drag) pick(drag.getAttribute('data-k'), drag); drag = null; });
    }
    $$('.vr-place button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.getAttribute('data-pl') === p.place) {
          b.classList.add('ok'); st.p[i] = true; save();
          setTimeout(render, 650); frames();
        } else { b.classList.add('no'); fb.className = 'vr-fb no'; fb.textContent = p.placeMiss; }
      });
    });
  }

  /* fly game (week 21): tap a flower to pick up pollen, then tap or drag to another flower of the same kind */
  var flyCarry = null, flyMsg = null, flyCls = '';
  function fill(t, a, b) { return String(t).split('{from}').join(a || '').split('{to}').join(b || '').split('{kind}').join(a || ''); }
  function renderFly() {
    var F = G.flowers || [], n = P.filter(function (p, i) { return st.m[i]; }).length;
    function kindOf(id) { return F.filter(function (f) { return f.id === id; })[0].kind; }
    function kIdx(k) { for (var i = 0; i < P.length; i++) if (P[i].key === k) return i; return -1; }
    var h = '<div class="vr-gstep">' + esc(L.flight) + ' ' + (n + 1) + ' of ' + P.length + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div><div class="vr-fly">' +
      F.map(function (f) {
        var done = st.m[kIdx(f.kind)];
        return '<button type="button" class="vr-flower' + (done ? ' ok' : '') + (flyCarry === f.id ? ' on' : '') + '" data-id="' + f.id + '"' + (done ? ' disabled' : ' draggable="true"') + '>' +
          '<img src="' + f.img + '" alt="' + esc(f.alt) + '">' + esc(f.name) + (flyCarry === f.id ? '<i class="bee" aria-hidden="true">🐝</i>' : '') + (done ? '<em>' + esc(L.tag) + '</em>' : '') + '</button>';
      }).join('') + '</div>';
    game.innerHTML = h;
    function act(id) {
      var k = kindOf(id), i = kIdx(k);
      if (st.m[i]) return;
      if (!flyCarry) { flyCarry = id; flyMsg = fill(L.pick, P[i].kind); flyCls = ''; }
      else if (id === flyCarry) { flyMsg = L.same; flyCls = 'no'; }
      else if (k === kindOf(flyCarry)) { st.m[i] = true; st.p[i] = true; save(); flyCarry = null; flyMsg = P[i].ok; flyCls = 'ok'; }
      else { flyMsg = fill(L.miss, P[kIdx(kindOf(flyCarry))].kind, P[i].kind); flyCls = 'no'; }
      render();
    }
    var dragId = null;
    $$('.vr-flower', game).forEach(function (b) {
      var id = b.getAttribute('data-id');
      b.addEventListener('click', function () { act(id); });
      b.addEventListener('dragstart', function (e) { dragId = id; try { e.dataTransfer.setData('text/plain', id); } catch (x) {} });
      b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) { e.preventDefault(); if (dragId && dragId !== id) { flyCarry = dragId; act(id); } dragId = null; });
    });
  }

  /* clean game (week 22): tap or drag only the litter into the bin, then pick the action that helps */
  function renderClean() {
    var I = G.items || [], T = I.filter(function (x) { return x.trash; }), A = G.action, last = P.length - 1;
    function tIdx(id) { for (var i = 0; i < T.length; i++) if (T[i].id === id) return i; return -1; }
    var n = T.filter(function (x, i) { return st.m[i]; }).length, h;
    if (n < T.length) {
      h = '<div class="vr-gstep">Step 1 of 2 · ' + esc(L.step1) + '</div><div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div><div class="vr-fly n4">' +
        I.map(function (x) {
          var gone = x.trash && st.m[tIdx(x.id)];
          return '<button type="button" class="vr-flower' + (gone ? ' gone' : '') + '" data-id="' + x.id + '"' + (gone ? ' disabled' : ' draggable="true"') + '><img src="' + x.img + '" alt="' + esc(x.alt) + '">' + esc(x.name) + (gone ? '<em>' + esc(L.tag) + '</em>' : '') + '</button>';
        }).join('') + '</div><div class="vr-bin vr-litter" id="vr-litter">' + esc(L.bin) + ' · ' + n + ' of ' + T.length + '</div>';
      game.innerHTML = h;
      var act = function (id) {
        var x = I.filter(function (y) { return y.id === id; })[0], i = tIdx(id);
        if (x.trash) { st.m[i] = true; st.p[i] = true; save(); flyCls = 'ok'; } else { flyCls = ''; }
        flyMsg = x.msg; render();
      };
      var dragId = null, bin = $('#vr-litter');
      $$('.vr-flower', game).forEach(function (b) {
        var id = b.getAttribute('data-id');
        b.addEventListener('click', function () { act(id); });
        b.addEventListener('dragstart', function (e) { dragId = id; try { e.dataTransfer.setData('text/plain', id); } catch (x) {} });
      });
      bin.addEventListener('dragover', function (e) { e.preventDefault(); bin.classList.add('drop'); });
      bin.addEventListener('dragleave', function () { bin.classList.remove('drop'); });
      bin.addEventListener('drop', function (e) { e.preventDefault(); bin.classList.remove('drop'); if (dragId) act(dragId); dragId = null; });
    } else {
      h = '<div class="vr-gstep">Step 2 of 2 · ' + esc(L.step2) + '</div><div class="vr-fb ok">' + esc(L.cleared) + '</div><div class="vr-gstep">' + esc(A.q) + '</div><div class="vr-place vr-col">' +
        Object.keys(A.options).map(function (k) { return '<button type="button" data-a="' + k + '">' + esc(A.options[k]) + '</button>'; }).join('') + '</div><div class="vr-fb" id="vr-fb" aria-live="polite"></div>';
      game.innerHTML = h;
      var fb = $('#vr-fb');
      $$('.vr-place button', game).forEach(function (b) {
        b.addEventListener('click', function () {
          if (b.getAttribute('data-a') === A.right) { b.classList.add('ok'); st.m[last] = true; st.p[last] = true; save(); setTimeout(render, 650); frames(); }
          else { b.classList.add('no'); fb.className = 'vr-fb no'; fb.textContent = A.miss; }
        });
      });
    }
  }

  /* spot game (week 23): tap a pin on a drawn scene (or drag the lens onto it); a find shows a real photo and asks what kind it is */
  var spotOpen = null;
  function renderSpot() {
    var S = G.spots || [], n = P.filter(function (p, i) { return st.m[i]; }).length;
    function pIdx(id) { for (var i = 0; i < P.length; i++) if (P[i].key === id) return i; return -1; }
    function sp(id) { return S.filter(function (x) { return x.id === id; })[0]; }
    var h = '<div class="vr-gstep">' + esc(L.find) + ' ' + (n + 1) + ' of ' + P.length + '</div><div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div>' +
      '<div class="vr-scene"><img src="' + G.scene.img + '" alt="' + esc(G.scene.alt) + '">' + S.map(function (s) {
        var i = pIdx(s.id), found = i >= 0 && st.m[i];
        return '<button type="button" class="vr-pin' + (found ? ' ok' : '') + (spotOpen === s.id ? ' on' : '') + '" style="left:' + s.x + '%;top:' + s.y + '%" data-id="' + s.id + '" aria-label="' + esc(s.name) + '"' + (found ? ' disabled' : '') + '>' + (found ? '✓' : '?') + '</button>';
      }).join('') + '</div>';
    if (spotOpen) {
      var o = sp(spotOpen);
      h += '<div class="vr-q"><figure class="vr-proof"><img src="' + o.proof.img + '" alt="' + esc(o.proof.alt) + '"><figcaption>' + esc(o.proof.cap) + '</figcaption></figure><div><div class="vr-gstep">' + esc(L.q2) + '</div><div class="vr-place">' +
        Object.keys(G.places).map(function (k) { return '<button type="button" data-pl="' + k + '">' + esc(G.places[k]) + '</button>'; }).join('') + '</div><div class="vr-fb" id="vr-fb2" aria-live="polite"></div></div></div>';
    } else h += '<div class="vr-lens" id="vr-lens" draggable="true">🔎 ' + esc(L.lens) + '</div>';
    game.innerHTML = h;
    function act(id) {
      if (spotOpen) return;
      var s = sp(id), i = pIdx(id);
      if (i >= 0 && st.m[i]) return;
      if (s.pollute) { spotOpen = id; flyCls = 'ok'; } else flyCls = '';
      flyMsg = s.msg; render();
    }
    $$('.vr-pin', game).forEach(function (b) {
      var id = b.getAttribute('data-id');
      b.addEventListener('click', function () { act(id); });
      b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) { e.preventDefault(); b.classList.remove('drop'); act(id); });
    });
    var lens = $('#vr-lens');
    if (lens) lens.addEventListener('dragstart', function (e) { try { e.dataTransfer.setData('text/plain', 'lens'); } catch (x) {} });
    $$('.vr-place button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        var o = sp(spotOpen), i = pIdx(spotOpen);
        if (b.getAttribute('data-pl') === o.kind) { b.classList.add('ok'); st.m[i] = true; st.p[i] = true; save(); spotOpen = null; flyMsg = L.next; flyCls = ''; setTimeout(render, 650); frames(); }
        else { b.classList.add('no'); var f2 = $('#vr-fb2'); f2.className = 'vr-fb no'; f2.textContent = o.miss; }
      });
    });
  }

  /* sort game (week 19): one card at a time goes into one of two bins; an IN card then asks which part takes it in */
  function renderSort(i, p) {
    var h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(p.name) + '</div><div class="vr-q">' +
      '<div class="vr-fossil"' + (st.m[i] ? '' : ' draggable="true"') + ' id="vr-fos"><img src="' + p.img + '" alt="' + esc(p.alt) + '">' + esc(p.name) + (p.facts ? '<small>' + esc(p.facts) + '</small>' : '') + '</div><div>';
    if (!st.m[i]) {
      h += '<div class="vr-gstep">' + esc(p.q || L.q1) + '</div><div class="vr-bins' + (Object.keys(G.bins).length > 2 ? ' n4' : '') + '">' + Object.keys(G.bins).map(function (k) {
        return '<button type="button" class="vr-bin" data-b="' + k + '">' + esc(G.bins[k]) + '</button>';
      }).join('') + '</div>';
    } else {
      h += '<div class="vr-fb ok">' + esc(p.ok) + '</div>';
      if (p.proof) h += '<figure class="vr-proof"><img src="' + p.proof.img + '" alt="' + esc(p.proof.alt) + '"><figcaption>' + esc(p.proof.cap) + '</figcaption></figure>';
      if (p.place) h += '<div class="vr-gstep">' + esc(L.q2) + '</div><div class="vr-place">' + Object.keys(G.places).map(function (k) {
        return '<button type="button" data-pl="' + k + '">' + esc(G.places[k]) + '</button>';
      }).join('') + '</div>';
      else h += '<button type="button" class="vr-next" id="vr-next">' + esc(L.next) + '</button>';
    }
    h += '<div class="vr-fb" id="vr-fb" aria-live="polite"></div></div></div>';
    game.innerHTML = h;
    var fb = $('#vr-fb');
    function pick(k, el) {
      if (k === p.bin) { st.m[i] = true; save(); render(); }
      else { fb.className = 'vr-fb no'; fb.textContent = p.miss || G.miss; if (el) { el.classList.remove('no'); void el.offsetWidth; el.classList.add('no'); } }
    }
    $$('.vr-bin', game).forEach(function (b) {
      b.addEventListener('click', function () { pick(b.getAttribute('data-b'), b); });
      b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) { e.preventDefault(); b.classList.remove('drop'); pick(b.getAttribute('data-b'), b); });
    });
    var fos = $('#vr-fos');
    if (fos && !st.m[i]) fos.addEventListener('dragstart', function (e) { try { e.dataTransfer.setData('text/plain', 'c'); } catch (x) {} });
    var nx = $('#vr-next');
    if (nx) nx.addEventListener('click', function () { st.p[i] = true; save(); render(); });
    $$('.vr-place button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.getAttribute('data-pl') === p.place) { b.classList.add('ok'); st.p[i] = true; save(); setTimeout(render, 650); frames(); }
        else { b.classList.add('no'); fb.className = 'vr-fb no'; fb.textContent = p.placeMiss; }
      });
    });
  }

  /* writing */
  var tas = $$('#vr-write textarea');
  var last = tas[0];
  tas.forEach(function (t, i) {
    t.value = st.w[i] || '';
    t.addEventListener('focus', function () { last = t; });
    t.addEventListener('input', function () { st.w[i] = t.value; save(); count(); });
  });
  $$('#vr-write .vr-chips button').forEach(function (b) {
    b.addEventListener('click', function () {
      var t = last || tas[0]; if (!t) return;
      t.value = (t.value && !/\s$/.test(t.value) ? t.value + ' ' : t.value) + b.textContent;
      t.dispatchEvent(new Event('input')); t.focus();
    });
  });
  function total() { return tas.reduce(function (a, t) { return a + words(t.value); }, 0); }
  function eachStarted() { return tas.every(function (t) { return words(t.value) >= 4; }); }
  function count() {
    var n = total(), c = $('#vr-count');
    if (c) { c.textContent = n >= G.min ? (eachStarted() ? n + ' words ✓' : n + ' words · finish both sentences') : n + ' of ' + G.min + ' words'; c.classList.toggle('ok', n >= G.min && eachStarted()); }
    checkStamp();
  }
  function studioDone() { return cur() < 0 && total() >= G.min && eachStarted(); }
  function checkStamp() { var s = $('#vr-stamp'); if (s) s.classList.toggle('on', studioDone()); }

  /* first name with a kind filter */
  var BAD = /(stupid|dumb|idiot|hate|kill|poop|butt|fart|ugly|loser|sex|damn|hell|crap|shit|fuck|bitch|ass\b)/i;
  var nm = $('#vr-name'), nmMsg = $('#vr-name-msg');
  if (nm) {
    nm.value = st.name || '';
    nm.addEventListener('input', function () {
      var v = nm.value.trim();
      if (BAD.test(v) || /[^A-Za-zÀ-ÿ' -]/.test(v)) { nmMsg.textContent = 'Please type just your first name.'; }
      else { nmMsg.textContent = ''; st.name = v; save(); }
    });
  }

  /* PDF */
  var pdf = $('#vr-pdf');
  if (pdf) pdf.addEventListener('click', function () {
    var name = (st.name || '').trim();
    if (!name) { nmMsg.textContent = 'Type your first name first.'; nm.focus(); return; }
    var rows = P.map(function (p, i) {
      var two = G.type === 'spot' ? G.places[p.place] : G.type === 'clean' ? p.ok : G.type === 'fly' ? L.tag : G.type === 'sort' ? G.bins[p.bin] : cz(p.cousin).name;
      var three = p.place ? (st.p[i] ? esc(G.places[p.place]) : '<i>not picked yet</i>') : '';
      return '<tr><td>' + esc(p.name) + '</td><td>' + (st.m[i] ? esc(two) : '<i>not matched yet</i>') + '</td>' + (L.cols.length > 2 ? '<td>' + three + '</td>' : '') + '</tr>';
    }).join('');
    var sents = tas.map(function (t, i) { return '<p><b>' + esc(G.frames[i]) + '</b><br>' + (t.value ? esc(t.value) : '<i>(not written yet)</i>') + '</p>'; }).join('');
    var h = '<!doctype html><html><head><meta charset="utf-8"><title>' + esc(V.canvas) + ' · ' + esc(name) + '</title><style>body{font:16px/1.5 Arial,sans-serif;max-width:720px;margin:24px auto;padding:0 16px;color:#222}h1{font-size:22px;margin:4px 0}.k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#7A5F2C}table{border-collapse:collapse;width:100%}th{background:#14110D;color:#fff;text-align:left;padding:5px 8px;font-size:13px}td{border:1px solid #ddd;padding:6px 8px}.st{display:inline-block;border:3px solid #1B4332;color:#1B4332;font-weight:900;letter-spacing:2px;padding:3px 12px;border-radius:8px;transform:rotate(-3deg);text-transform:uppercase}@media print{button{display:none}}</style></head><body>' +
      '<div class="k">Optima Academy Online · 3rd Grade Science · Week ' + V.week + '</div><h1>' + esc(V.canvas) + ' (Studio Day)</h1>' +
      '<p><b>Name:</b> ' + esc(name) + ' &nbsp; <b>Date:</b> ' + new Date().toLocaleDateString() + '</p>' +
      '<h2>' + esc(L.pdfTitle) + '</h2><table><tr><th>' + L.cols.map(esc).join('</th><th>') + '</th></tr>' + rows + '</table>' +
      '<h2>What I think (' + total() + ' words)</h2>' + sents + (studioDone() ? '<div class="st">' + esc(V.stamp) + '</div>' : '') +
      '<p style="margin-top:24px"><button onclick="print()">🖨 Print or save as PDF</button></p></body></html>';
    var w = null; try { w = window.open('', '_blank'); } catch (e) {}
    if (w && w.document) { w.document.open(); w.document.write(h); w.document.close(); setTimeout(function () { try { w.print(); } catch (e) {} }, 400); }
    else {
      var a = document.createElement('a'); a.href = URL.createObjectURL(new Blob([h], { type: 'text/html' }));
      a.download = 'week-' + V.week + '-vr-studio-' + name.replace(/\s+/g, '-') + '.html'; document.body.appendChild(a); a.click(); a.remove();
    }
  });

  if (game) render();
  count();
  window.VR_TEST = { state: st, render: render };
})();
