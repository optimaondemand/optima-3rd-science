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
      $('.pl', f).textContent = lit ? (G.framePl === 'ptag' ? p.tag : G.framePl === 'tag' ? L.tag : G.framePl === 'bin' ? G.bins[p.bin] : G.framePl === 'cousin' ? cz(p.cousin).name : G.places[p.place]) : '';
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
    if (G.type === 'count') { renderCount(); return; }
    if (G.type === 'web') { renderWeb(); return; }
    if (G.type === 'clue') { renderClue(); return; }
    if (G.type === 'dial') { renderDial(); return; }
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

  /* count game (week 24): tag and count the nests in two drawn scenes, then pick the claim the numbers support */
  function renderCount() {
    st.c = st.c || {};
    var SC = G.scenes, stage = !st.m[0] ? 0 : !st.m[1] ? 1 : 2, h;
    if (stage < 2) {
      var sc = SC[stage], got = st.c[sc.key] || [], total = sc.spots.filter(function (s) { return s.nest; }).length;
      h = '<div class="vr-gstep">Step ' + (stage + 1) + ' of 3 · ' + esc(sc.title) + '</div><div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div>' +
        '<div class="vr-scene"><img src="' + sc.img + '" alt="' + esc(sc.alt) + '">' + sc.spots.map(function (s) {
          var k = got.indexOf(s.id);
          return '<button type="button" class="vr-nest' + (k >= 0 ? ' ok' : '') + '" style="left:' + s.x + '%;top:' + s.y + '%" data-id="' + s.id + '" aria-label="' + esc(L.spot) + '"' + (k >= 0 ? ' disabled' : '') + '>' + (k >= 0 ? '🚩' + (k + 1) : '') + '</button>';
        }).join('') + '</div><div class="vr-tally">' + esc(L.count) + ': ' + got.length + '</div><div class="vr-lens" id="vr-lens" draggable="true">🚩 ' + esc(L.flag) + '</div>';
      game.innerHTML = h;
      var act = function (id) {
        var s = sc.spots.filter(function (x) { return x.id === id; })[0];
        if (got.indexOf(id) >= 0) return;
        if (s.nest) {
          got.push(id); st.c[sc.key] = got; flyCls = 'ok'; flyMsg = fill(L.tagged, String(got.length));
          if (got.length === total) { st.m[stage] = true; st.p[stage] = true; flyMsg = sc.done; }
          save();
        } else { flyCls = ''; flyMsg = s.msg; }
        render();
      };
      $$('.vr-nest', game).forEach(function (b) {
        var id = b.getAttribute('data-id');
        b.addEventListener('click', function () { act(id); });
        b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
        b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
        b.addEventListener('drop', function (e) { e.preventDefault(); b.classList.remove('drop'); act(id); });
      });
      var lens = $('#vr-lens');
      if (lens) lens.addEventListener('dragstart', function (e) { try { e.dataTransfer.setData('text/plain', 'flag'); } catch (x) {} });
    } else {
      var A = G.claim;
      h = '<div class="vr-gstep">Step 3 of 3 · ' + esc(L.step3) + '</div><div class="vr-fb ok">' + esc(P[0].name + ': ' + P[0].tag + '. ' + P[1].name + ': ' + P[1].tag + '.') + '</div><div class="vr-gstep">' + esc(A.q) + '</div><div class="vr-place vr-col">' +
        Object.keys(A.options).map(function (k) { return '<button type="button" data-a="' + k + '">' + esc(A.options[k]) + '</button>'; }).join('') + '</div><div class="vr-fb" id="vr-fb" aria-live="polite"></div>';
      game.innerHTML = h;
      var fb = $('#vr-fb');
      $$('.vr-place button', game).forEach(function (b) {
        b.addEventListener('click', function () {
          if (b.getAttribute('data-a') === A.right) { b.classList.add('ok'); st.m[2] = true; st.p[2] = true; save(); setTimeout(render, 650); frames(); }
          else { b.classList.add('no'); fb.className = 'vr-fb no'; fb.textContent = A.miss; }
        });
      });
    }
  }

  /* web game (week 25): pin strings from each eater to its food, snip one species, then pick the claim */
  var webResize = false;
  function renderWeb() {
    st.c = st.c || {}; st.c.links = st.c.links || []; st.c.hit = st.c.hit || [];
    var SP = G.species, LK = G.links, SN = G.snip, stage = !st.m[0] ? 0 : !st.m[1] ? 1 : 2, h;
    function sp(id) { return SP.filter(function (x) { return x.id === id; })[0]; }
    if (stage === 2) { renderClaim(3, G.snipDone); return; }
    var snipped = stage === 1 && st.c.snipped;
    h = '<div class="vr-gstep">Step ' + (stage + 1) + ' of 3 · ' + esc(stage === 0 ? L.step1 : L.step2) + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || (stage === 0 ? L.start : snipped ? SN.q : L.snipStart)) + '</div>' +
      '<div class="vr-web" id="vr-web"><svg class="vr-strings" aria-hidden="true"></svg>' + SP.map(function (s) {
        var gone = snipped && s.id === SN.gone, hit = stage === 1 && st.c.hit.indexOf(s.id) >= 0;
        return '<button type="button" class="vr-sp' + (flyCarry === s.id ? ' on' : '') + (gone ? ' gone' : '') + (hit ? ' hit' : '') + '" style="left:' + s.x + '%;top:' + s.y + '%" data-id="' + s.id + '"' + (gone || hit ? ' disabled' : ' draggable="true"') + '>' +
          '<img src="' + s.img + '" alt="' + esc(s.alt) + '"><span>' + esc(s.name) + '</span>' + (gone ? '<i aria-hidden="true">✂️</i>' : '') + (hit ? '<em>' + esc(L.hitTag) + '</em>' : '') + '</button>';
      }).join('') + '</div>';
    if (stage === 0) h += '<div class="vr-tally">' + esc(L.count) + ': ' + st.c.links.length + ' of ' + LK.length + '</div>';
    else if (!snipped) h += '<button type="button" class="vr-lens vr-snip" id="vr-snip" draggable="true">✂️ ' + esc(L.snipBtn) + '</button>';
    else h += '<div class="vr-tally">' + esc(L.hitCount) + ': ' + st.c.hit.length + ' of ' + SN.hit.length + '</div>';
    game.innerHTML = h;
    var web = $('#vr-web');
    function draw() {
      var svg = $('svg', web); if (!svg) return;
      var r = web.getBoundingClientRect(), out = '';
      svg.setAttribute('viewBox', '0 0 ' + r.width + ' ' + r.height);
      st.c.links.forEach(function (k) {
        var ab = k.split('>'), a = $('.vr-sp[data-id="' + ab[0] + '"]', web), b = $('.vr-sp[data-id="' + ab[1] + '"]', web);
        if (!a || !b) return;
        var ra = a.getBoundingClientRect(), rb = b.getBoundingClientRect();
        var x1 = ra.left + ra.width / 2 - r.left, y1 = ra.top + ra.height / 2 - r.top, x2 = rb.left + rb.width / 2 - r.left, y2 = rb.top + rb.height / 2 - r.top;
        var cut = snipped && (ab[0] === SN.gone || ab[1] === SN.gone);
        out += '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" class="' + (cut ? 'cut' : '') + '"/>';
      });
      svg.innerHTML = out;
    }
    draw(); setTimeout(draw, 60);
    if (!webResize) { webResize = true; window.addEventListener('resize', function () { if (G.type === 'web' && cur() >= 0 && !st.m[1]) render(); }); }
    $$('img', web).forEach(function (im) { if (!im.complete) im.addEventListener('load', draw); });
    function link(from, to) {
      var a = sp(from), k = from + '>' + to, l = LK.filter(function (x) { return x.from === from && x.to === to; })[0];
      flyCarry = null;
      if (a.plant) { flyMsg = a.food; flyCls = 'no'; }
      else if (st.c.links.indexOf(k) >= 0) { flyMsg = L.already; flyCls = ''; }
      else if (l) {
        st.c.links.push(k); flyMsg = l.msg; flyCls = 'ok';
        if (st.c.links.length === LK.length) { st.m[0] = true; st.p[0] = true; flyMsg = G.web.done; }
        save();
      } else { flyMsg = a.food; flyCls = 'no'; }
      render();
    }
    function tapCard(id) {
      if (stage === 0) {
        if (!flyCarry) {
          if (sp(id).plant) { flyMsg = sp(id).food; flyCls = 'no'; }
          else { flyCarry = id; flyMsg = fill(L.pick, sp(id).name); flyCls = ''; }
          render();
        } else if (flyCarry === id) { flyCarry = null; flyMsg = L.start; flyCls = ''; render(); }
        else link(flyCarry, id);
      } else if (!snipped) { flyMsg = L.snipFirst; flyCls = ''; render(); }
      else {
        if (SN.hit.indexOf(id) >= 0) {
          if (st.c.hit.indexOf(id) < 0) st.c.hit.push(id);
          flyMsg = SN.ok[id]; flyCls = 'ok';
          if (st.c.hit.length === SN.hit.length) { st.m[1] = true; st.p[1] = true; flyMsg = G.snipDone; }
          save();
        } else { flyMsg = SN.safe[id]; flyCls = ''; }
        render();
      }
    }
    function doSnip() { st.c.snipped = true; save(); flyMsg = SN.q; flyCls = ''; render(); }
    var dragId = null;
    $$('.vr-sp', web).forEach(function (b) {
      var id = b.getAttribute('data-id');
      b.addEventListener('click', function () { tapCard(id); });
      b.addEventListener('dragstart', function (e) { dragId = id; try { e.dataTransfer.setData('text/plain', id); } catch (x) {} });
      b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) {
        e.preventDefault(); b.classList.remove('drop');
        if (dragId === 'snip') { if (id === SN.gone) doSnip(); else { flyMsg = L.snipFirst; flyCls = ''; render(); } }
        else if (stage === 0 && dragId && dragId !== id) link(dragId, id);
        dragId = null;
      });
    });
    var sn = $('#vr-snip');
    if (sn) {
      sn.addEventListener('click', doSnip);
      sn.addEventListener('dragstart', function (e) { dragId = 'snip'; try { e.dataTransfer.setData('text/plain', 'snip'); } catch (x) {} });
    }
  }
  /* last step shared by the web game: pick the claim (same look as the count game's step 3) */
  function renderClaim(n, lead) {
    var A = G.claim;
    game.innerHTML = '<div class="vr-gstep">Step ' + n + ' of ' + n + ' · ' + esc(L.step3) + '</div>' + (lead ? '<div class="vr-fb ok">' + esc(lead) + '</div>' : '') + '<div class="vr-gstep">' + esc(A.q) + '</div><div class="vr-place vr-col">' +
      Object.keys(A.options).map(function (k) { return '<button type="button" data-a="' + k + '">' + esc(A.options[k]) + '</button>'; }).join('') + '</div><div class="vr-fb" id="vr-fb" aria-live="polite"></div>';
    var fb = $('#vr-fb');
    $$('.vr-place button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.getAttribute('data-a') === A.right) { b.classList.add('ok'); st.m[n - 1] = true; st.p[n - 1] = true; save(); setTimeout(render, 650); frames(); }
        else { b.classList.add('no'); fb.className = 'vr-fb no'; fb.textContent = A.miss; }
      });
    });
  }

  /* clue game (week 26): read one property clue at a time and clear every prop that does not fit; one prop is left */
  function renderClue() {
    st.c = st.c || {}; st.c.out = st.c.out || [];
    var i = cur(), CL = G.clues[i], PR = G.props, h;
    function pr(id) { return PR.filter(function (x) { return x.id === id; })[0]; }
    function low(id) { return pr(id).name.toLowerCase(); }
    h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + G.clues.length + ' · ' + esc(L.clue) + ' ' + (i + 1) + '</div>' +
      '<div class="vr-clue">🔎 ' + esc(CL.text) + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div>' +
      '<div class="vr-table">' + PR.map(function (p) {
        var gone = st.c.out.indexOf(p.id) >= 0;
        return '<button type="button" class="vr-prop' + (gone ? ' gone' : '') + '" data-id="' + p.id + '"' + (gone ? ' disabled' : ' draggable="true"') + '><img src="' + p.img + '" alt="' + esc(p.alt) + '"><span>' + esc(p.name) + '</span>' + (gone ? '<em>' + esc(L.offTag) + '</em>' : '') + '</button>';
      }).join('') + '</div><div class="vr-off" id="vr-off">⬇ ' + esc(L.off) + '</div>';
    game.innerHTML = h;
    function act(id) {
      if (st.c.out.indexOf(id) >= 0) return;
      if (CL.out.indexOf(id) >= 0) {
        st.c.out.push(id); flyCls = 'ok'; flyMsg = fill(CL.gone, low(id));
        if (CL.out.every(function (x) { return st.c.out.indexOf(x) >= 0; })) { st.m[i] = true; st.p[i] = true; flyMsg = CL.done; }
        save();
      } else { flyCls = 'no'; flyMsg = fill(CL.keep, low(id)); }
      render();
    }
    var dragId = null, off = $('#vr-off');
    $$('.vr-prop', game).forEach(function (b) {
      var id = b.getAttribute('data-id');
      b.addEventListener('click', function () { act(id); });
      b.addEventListener('dragstart', function (e) { dragId = id; try { e.dataTransfer.setData('text/plain', id); } catch (x) {} });
    });
    off.addEventListener('dragover', function (e) { e.preventDefault(); off.classList.add('drop'); });
    off.addEventListener('dragleave', function () { off.classList.remove('drop'); });
    off.addEventListener('drop', function (e) { e.preventDefault(); off.classList.remove('drop'); if (dragId) act(dragId); dragId = null; });
  }

  /* dial game (week 27): turn the temperature dial until the water changes state, then name the change */
  function renderDial() {
    st.c = st.c || {}; st.c.t = st.c.t || [];
    var i = cur(), R = G.rounds[i], lo = G.dial.min, hi = G.dial.max;
    if (st.c.t[i] == null) st.c.t[i] = R.start;
    var t = st.c.t[i], s = R.states.filter(function (x) { return t <= x.upTo; })[0] || R.states[R.states.length - 1];
    var hit = t >= R.min && t <= R.max, pct = Math.round(100 * (t - lo) / (hi - lo));
    var h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + G.rounds.length + ' · ' + esc(R.name) + '</div>' +
      '<div class="vr-clue">🎬 ' + esc(R.q) + '</div>' +
      '<div class="vr-dial"><figure class="vr-dial-pic"><img src="' + s.img + '" alt="' + esc(s.alt) + '"><figcaption>' + esc(s.label) + '</figcaption></figure>' +
      '<div class="vr-dial-ctl"><div class="vr-therm" aria-hidden="true"><i style="height:' + pct + '%"></i></div>' +
      '<div><div class="vr-temp" id="vr-temp">' + t + ' °C</div>' +
      '<input type="range" id="vr-slide" min="' + lo + '" max="' + hi + '" step="1" value="' + t + '" aria-label="' + esc(L.dial) + '">' +
      '<div class="vr-dial-btns"><button type="button" class="vr-next" data-d="-5">' + esc(L.down) + '</button><button type="button" class="vr-next" data-d="5">' + esc(L.up) + '</button></div>' +
      '<div class="vr-dial-key">' + esc(L.key) + '</div></div></div></div>' +
      '<div class="vr-fb ' + (hit ? 'ok' : flyCls) + '" id="vr-fb" aria-live="polite">' + esc(hit ? R.ok : (flyMsg || L.start)) + '</div>';
    if (hit) h += '<div class="vr-gstep">' + esc(L.q2) + '</div><div class="vr-place">' + Object.keys(G.changes).map(function (k) {
      return '<button type="button" data-ch="' + k + '">' + esc(G.changes[k]) + '</button>'; }).join('') + '</div><div class="vr-fb" id="vr-fb2" aria-live="polite"></div>';
    game.innerHTML = h;
    function set(v, keepFocus) {
      v = Math.max(lo, Math.min(hi, Math.round(v)));
      st.c.t[i] = v; save();
      flyCls = ''; flyMsg = v > R.max ? L.tooHot : v < R.min ? L.tooCold : '';
      render();
      if (keepFocus) { var sl = $('#vr-slide'); if (sl) sl.focus(); }
    }
    var sl = $('#vr-slide');
    sl.addEventListener('change', function () { set(+sl.value, true); });
    sl.addEventListener('input', function () { $('#vr-temp').textContent = sl.value + ' °C'; });
    $$('.vr-dial-btns button', game).forEach(function (b) { b.addEventListener('click', function () { set(t + (+b.getAttribute('data-d'))); }); });
    $$('.vr-place button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.getAttribute('data-ch') === R.right) { b.classList.add('ok'); st.m[i] = true; st.p[i] = true; save(); flyMsg = null; flyCls = ''; setTimeout(render, 650); frames(); }
        else { b.classList.add('no'); var f2 = $('#vr-fb2'); f2.className = 'vr-fb no'; f2.textContent = R.miss; }
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
      var two = (G.type === 'count' || G.type === 'web' || G.type === 'clue' || G.type === 'dial') ? p.tag : G.type === 'spot' ? G.places[p.place] : G.type === 'clean' ? p.ok : G.type === 'fly' ? L.tag : G.type === 'sort' ? G.bins[p.bin] : cz(p.cousin).name;
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
