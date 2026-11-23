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
    if (G.type === 'meter') { renderMeter(i, P[i]); return; }
    if (G.type === 'season') { renderSeason(); return; }
    if (G.type === 'build') { renderBuild(i, P[i]); return; }
    if (G.type === 'path') { if (i >= G.maps.length) renderClaim(P.length, G.allBuilt); else renderPath(i); return; }
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

  /* meter game (week 28): test each object with every meter, then tag the energy it gives off */
  function renderMeter(i, p) {
    st.c = st.c || {}; st.c.r = st.c.r || {}; st.c.s = st.c.s || {};
    var T = G.things[i], M = G.meters, got = st.c.r[i] = st.c.r[i] || {}, sel = st.c.s[i] = st.c.s[i] || [];
    var all = M.every(function (m) { return got[m.key]; });
    function lvl(v) { return v >= 50 ? L.lots : v >= 10 ? L.little : L.none; }
    var h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(T.name) + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div>' +
      '<div class="vr-meter"><figure class="vr-meter-pic" id="vr-mtarget"><img src="' + T.img + '" alt="' + esc(T.alt) + '"><figcaption>' + esc(T.name) + '</figcaption></figure>' +
      '<div><div class="vr-meter-tools">' + M.map(function (m) {
        return '<button type="button" class="vr-mtool' + (got[m.key] ? ' used' : '') + '" draggable="true" data-m="' + m.key + '">' + m.icon + ' ' + esc(m.name) + '</button>'; }).join('') + '</div>' +
      M.map(function (m) {
        var v = T.read[m.key] || 0, on = got[m.key];
        return '<div class="vr-gauge"><span>' + m.icon + ' ' + esc(m.short) + '</span><div class="vr-gbar"><i style="width:' + (on ? Math.max(v, 3) : 0) + '%"></i></div><b>' + (on ? esc(lvl(v)) : '?') + '</b></div>'; }).join('') +
      '</div></div>';
    if (all) h += '<div class="vr-gstep">' + esc(L.q2) + '</div><div class="vr-place">' + M.map(function (m) {
        return '<button type="button" class="' + (sel.indexOf(m.key) >= 0 ? 'on' : '') + '" data-t="' + m.key + '" aria-pressed="' + (sel.indexOf(m.key) >= 0) + '">' + m.icon + ' ' + esc(m.short) + '</button>'; }).join('') +
      '<button type="button" class="vr-next" id="vr-check">' + esc(L.check) + '</button></div>';
    game.innerHTML = h;
    function test(k) {
      if (!k) return;
      got[k] = 1; save();
      var m = M.filter(function (x) { return x.key === k; })[0], v = T.read[k] || 0;
      flyCls = ''; flyMsg = fill(L.reading, m.short, lvl(v).toLowerCase());
      if (M.every(function (x) { return got[x.key]; })) flyMsg += ' ' + L.allDone;
      render();
    }
    var dragM = null, tgt = $('#vr-mtarget');
    $$('.vr-mtool', game).forEach(function (b) {
      b.addEventListener('click', function () { test(b.getAttribute('data-m')); });
      b.addEventListener('dragstart', function (e) { dragM = b.getAttribute('data-m'); try { e.dataTransfer.setData('text/plain', dragM); } catch (x) {} });
    });
    tgt.addEventListener('dragover', function (e) { e.preventDefault(); tgt.classList.add('drop'); });
    tgt.addEventListener('dragleave', function () { tgt.classList.remove('drop'); });
    tgt.addEventListener('drop', function (e) { e.preventDefault(); tgt.classList.remove('drop'); test(dragM); dragM = null; });
    $$('.vr-place button[data-t]', game).forEach(function (b) {
      b.addEventListener('click', function () {
        var k = b.getAttribute('data-t'), at = sel.indexOf(k);
        if (at >= 0) sel.splice(at, 1); else sel.push(k);
        save(); flyMsg = null; render();
      });
    });
    var ck = $('#vr-check');
    if (ck) ck.addEventListener('click', function () {
      var ok = sel.length === T.gives.length && T.gives.every(function (k) { return sel.indexOf(k) >= 0; });
      if (ok) { st.m[i] = true; st.p[i] = true; save(); flyMsg = T.ok; flyCls = 'ok'; frames(); render(); }
      else { flyMsg = T.miss; flyCls = 'no'; render(); }
    });
  }

  /* season game (week 29): flip a drawn wetland to the dry season, put each animal where it goes, then pick why */
  function renderSeason() {
    st.c = st.c || {}; st.c.at = st.c.at || {};
    var A = G.animals, Z = G.zones, i = cur(), dry = !!st.c.dry, view = st.c.view || (dry ? 'dry' : 'wet');
    if (dry && i >= A.length) { renderClaim(P.length, G.allPlaced); return; }
    var a = A[i], h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(dry ? a.name : L.flip) + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || (!dry ? L.start : view === 'wet' ? L.peek : fill(L.q, a.name.toLowerCase()))) + '</div>' +
      '<div class="vr-switch" role="group"><button type="button" data-v="wet" aria-pressed="' + (view === 'wet') + '">🌧️ ' + esc(L.wet) + '</button><button type="button" data-v="dry" aria-pressed="' + (view === 'dry') + '">☀️ ' + esc(L.dry) + '</button></div>' +
      '<div class="vr-scene vr-season"><img src="' + (view === 'wet' ? G.wet.img : G.dry.img) + '" alt="' + esc(view === 'wet' ? G.wet.alt : G.dry.alt) + '">';
    if (view === 'dry') {
      h += Object.keys(Z).map(function (k) {
        var here = A.filter(function (x, j) { return st.m[j] && x.zone === k; });
        return '<button type="button" class="vr-zone" data-z="' + k + '" style="left:' + Z[k].x + '%;top:' + Z[k].y + '%" aria-label="' + esc(Z[k].name) + '">' + Z[k].icon +
          here.map(function (x) { return '<img class="vr-zpic" src="' + x.img + '" alt="">'; }).join('') + '</button>'; }).join('');
    }
    h += '</div>';
    if (view === 'dry') h += '<div class="vr-zkey"><div class="vr-acard" draggable="true" id="vr-fos"><img src="' + a.img + '" alt="' + esc(a.alt) + '"><span>' + esc(a.name) + '</span></div>' +
      Object.keys(Z).map(function (k) { return '<button type="button" class="vr-next" data-z="' + k + '">' + Z[k].icon + ' ' + esc(Z[k].name) + '</button>'; }).join('') + '</div>';
    game.innerHTML = h;
    $$('.vr-switch button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        var v = b.getAttribute('data-v');
        if (v === 'dry' && !st.c.dry) { st.c.dry = 1; flyMsg = L.flipped; flyCls = 'ok'; } else { flyMsg = null; flyCls = ''; }
        st.c.view = v; save(); render();
      });
    });
    function put(z) {
      if (z === a.zone) { st.m[i] = true; st.p[i] = true; save(); flyMsg = a.ok; flyCls = 'ok'; frames(); }
      else { flyMsg = a.miss; flyCls = 'no'; }
      render();
    }
    $$('[data-z]', game).forEach(function (b) {
      b.addEventListener('click', function () { put(b.getAttribute('data-z')); });
      b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) { e.preventDefault(); b.classList.remove('drop'); put(b.getAttribute('data-z')); });
    });
    var fos = $('#vr-fos'); if (fos) fos.addEventListener('dragstart', function (e) { try { e.dataTransfer.setData('text/plain', 'a'); } catch (x) {} });
  }

  /* build game (week 30): for each habitat photo pick a color, a body part and a trick, then meet the real animal */
  function renderBuild(i, p) {
    st.c = st.c || {}; st.c.b = st.c.b || {};
    var Hb = G.habitats[i], picks = st.c.b[i] = st.c.b[i] || {}, done = st.m[i];
    var h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(Hb.name) + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div>' +
      '<div class="vr-build"><figure class="vr-dial-pic"><img src="' + Hb.img + '" alt="' + esc(Hb.alt) + '"><figcaption>' + esc(Hb.name) + '</figcaption></figure><div>' +
      G.cats.map(function (c) {
        return '<div class="vr-bcat"><b>' + esc(c.name) + '</b><div class="vr-place">' + Object.keys(G.choices[c.key]).map(function (k) {
          var on = picks[c.key] === k;
          return '<button type="button" class="' + (on ? 'ok' : '') + '" data-c="' + c.key + '" data-k="' + k + '"' + (picks[c.key] && !on ? ' disabled' : '') + '>' + esc(G.choices[c.key][k]) + '</button>'; }).join('') + '</div></div>'; }).join('') +
      '</div></div>';
    if (done) h += '<figure class="vr-proof"><img src="' + Hb.real.img + '" alt="' + esc(Hb.real.alt) + '"><figcaption>' + esc(Hb.real.cap) + '</figcaption></figure><button type="button" class="vr-next" id="vr-next">' + esc(L.next) + '</button>';
    game.innerHTML = h;
    $$('.vr-bcat button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        var c = b.getAttribute('data-c'), k = b.getAttribute('data-k');
        if (picks[c]) return;
        if (Hb.right[c] === k) {
          picks[c] = k; flyCls = 'ok'; flyMsg = Hb.ok[c];
          if (G.cats.every(function (x) { return picks[x.key]; })) { st.m[i] = true; flyMsg = Hb.done; frames(); }
          save();
        } else { flyCls = 'no'; flyMsg = Hb.miss[c]; }
        render();
      });
    });
    var nx = $('#vr-next');
    if (nx) nx.addEventListener('click', function () { st.p[i] = true; save(); flyMsg = null; flyCls = ''; render(); });
  }

  /* path game (week 31): tap tiles on a drawn grid to build a wildlife crossing, then test it against the criteria */
  function renderPath(i) {
    st.c = st.c || {}; st.c.t = st.c.t || {};
    var M = G.maps[i], on = st.c.t[i] = st.c.t[i] || [], rows = M.grid, nc = rows[0].length, res = st.c.res && st.c.res[i];
    function ch(r, c) { return rows[r] && rows[r][c]; }
    var h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(M.name) + '</div>' +
      '<div class="vr-clue">🛠️ ' + esc(fill(M.q, String(M.max))) + '</div>' +
      '<div class="vr-fb ' + flyCls + '" id="vr-fb" aria-live="polite">' + esc(flyMsg || L.start) + '</div>' +
      '<div class="vr-grid" style="grid-template-columns:repeat(' + nc + ',1fr)" role="group" aria-label="' + esc(M.name) + '">';
    rows.forEach(function (row, r) {
      row.split('').forEach(function (t, c) {
        var id = r + '-' + c, picked = on.indexOf(id) >= 0, cls = { L: 'forest', G: 'forest', R: 'road', X: 'house', W: 'water', '.': 'open' }[t];
        var can = t === '.' || t === 'R';
        h += '<button type="button" class="vr-tile ' + cls + (picked ? ' on' : '') + '" data-id="' + id + '"' + (can && !st.m[i] ? '' : ' disabled') + ' aria-label="' + esc(L.tiles[cls]) + (picked ? ', ' + esc(L.picked) : '') + '">' +
          (t === 'L' && r === 0 && c === 0 ? '🐆' : t === 'G' && r === rows.length - 1 && c === nc - 1 ? '🌳' : t === 'X' ? '🏠' : t === 'W' ? '💧' : picked ? (t === 'R' ? '🕳️' : '🐾') : '') + '</button>';
      });
    });
    h += '</div><div class="vr-tally">' + esc(L.count) + ': ' + on.length + ' / ' + M.max + '</div>';
    if (res) h += '<ul class="vr-crit">' + res.map(function (x) { return '<li class="' + (x[1] ? 'ok' : 'no') + '">' + (x[1] ? '✓ ' : '✗ ') + esc(x[0]) + '</li>'; }).join('') + '</ul>';
    if (!st.m[i]) h += '<div class="vr-dial-btns"><button type="button" class="vr-next" id="vr-test">' + esc(L.test) + '</button><button type="button" class="vr-next vr-clear" id="vr-clear">' + esc(L.clear) + '</button></div>';
    else h += '<button type="button" class="vr-next" id="vr-next">' + esc(L.next) + '</button>';
    game.innerHTML = h;
    $$('.vr-tile', game).forEach(function (b) {
      b.addEventListener('click', function () {
        var id = b.getAttribute('data-id'), k = on.indexOf(id);
        if (k >= 0) on.splice(k, 1); else on.push(id);
        if (st.c.res) st.c.res[i] = null;
        flyMsg = null; flyCls = ''; save(); render();
      });
    });
    function test() {
      var seen = {}, q = [], ok = false, road = false;
      rows.forEach(function (row, r) { if (row[0] === 'L') { q.push([r, 0]); seen[r + '-0'] = 1; } });
      while (q.length) {
        var p = q.shift(), r = p[0], c = p[1];
        [[1, 0], [-1, 0], [0, 1], [0, -1]].forEach(function (d) {
          var rr = r + d[0], cc = c + d[1], id = rr + '-' + cc, t = ch(rr, cc);
          if (!t || seen[id]) return;
          if (t === 'G') { ok = true; return; }
          if (t === 'L' || on.indexOf(id) >= 0) { seen[id] = 1; if (t === 'R') road = true; q.push([rr, cc]); }
        });
      }
      var list = [[L.c1, ok], [L.c2, ok && road], [fill(L.c3, String(M.max)), on.length > 0 && on.length <= M.max]];
      st.c.res = st.c.res || {}; st.c.res[i] = list;
      if (list.every(function (x) { return x[1]; })) { st.m[i] = true; flyMsg = M.ok; flyCls = 'ok'; frames(); }
      else { flyMsg = !ok ? L.noPath : L.tooMany; flyCls = 'no'; }
      save(); render();
    }
    var tb = $('#vr-test'); if (tb) tb.addEventListener('click', test);
    var cb = $('#vr-clear'); if (cb) cb.addEventListener('click', function () { st.c.t[i] = []; if (st.c.res) st.c.res[i] = null; flyMsg = null; flyCls = ''; save(); render(); });
    var nx = $('#vr-next'); if (nx) nx.addEventListener('click', function () { st.p[i] = true; flyMsg = null; flyCls = ''; save(); render(); });
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
      var two = (G.type === 'count' || G.type === 'web' || G.type === 'clue' || G.type === 'dial' || G.type === 'meter' || G.type === 'season' || G.type === 'build' || G.type === 'path') ? p.tag : G.type === 'spot' ? G.places[p.place] : G.type === 'clean' ? p.ok : G.type === 'fly' ? L.tag : G.type === 'sort' ? G.bins[p.bin] : cz(p.cousin).name;
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
