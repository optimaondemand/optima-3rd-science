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

  /* ---------- Studio Day: cousins match ---------- */
  var game = $('#vr-game'), P = G.pairs || [], C = G.cousins || [];
  var drag = null;
  function frames() {
    P.forEach(function (p, i) {
      var f = $('.vr-frame[data-f="' + i + '"]'); if (!f) return;
      var lit = st.m[i] && st.p[i];
      f.classList.toggle('lit', !!lit);
      $('.pl', f).textContent = lit ? G.places[p.place] : '';
    });
  }
  function cur() { for (var i = 0; i < P.length; i++) if (!(st.m[i] && st.p[i])) return i; return -1; }
  function render() {
    frames();
    var i = cur();
    if (i < 0) {
      game.innerHTML = '<div class="vr-fb ok">All 4 frames are on the storyboard. Nice work, crew!</div>';
      $('#vr-write').hidden = false; checkStamp(); return;
    }
    $('#vr-write').hidden = true;
    var p = P[i], h = '<div class="vr-gstep">Step ' + (i + 1) + ' of ' + P.length + ' · ' + esc(p.name) + '</div><div class="vr-q">' +
      '<div class="vr-fossil" draggable="true" id="vr-fos"><img src="' + p.img + '" alt="' + esc(p.alt) + '">' + esc(p.name) + '</div><div>';
    if (!st.m[i]) {
      h += '<div class="vr-opts">' + C.map(function (c) {
        return '<button class="vr-opt" type="button" data-k="' + c.key + '"><img src="' + c.img + '" alt="' + esc(c.alt) + '">' + esc(c.name) + '</button>';
      }).join('') + '</div>';
    } else {
      var c = C.filter(function (x) { return x.key === p.cousin; })[0];
      h += '<div class="vr-opts" style="grid-template-columns:1fr"><div class="vr-opt ok"><img src="' + c.img + '" alt="' + esc(c.alt) + '">' + esc(c.name) + '</div></div>' +
        '<div class="vr-fb ok">' + esc(p.ok) + '</div><div class="vr-gstep">Where did this living thing live?</div><div class="vr-place">' +
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
      b.addEventListener('dragover', function (e) { e.preventDefault(); b.classList.add('drop'); });
      b.addEventListener('dragleave', function () { b.classList.remove('drop'); });
      b.addEventListener('drop', function (e) { e.preventDefault(); b.classList.remove('drop'); pick(b.getAttribute('data-k'), b); });
    });
    var fos = $('#vr-fos');
    if (fos) fos.addEventListener('dragstart', function (e) { try { e.dataTransfer.setData('text/plain', 'f'); } catch (x) {} });
    $$('.vr-place button', game).forEach(function (b) {
      b.addEventListener('click', function () {
        if (b.getAttribute('data-pl') === p.place) {
          b.classList.add('ok'); st.p[i] = true; save();
          setTimeout(render, 650); frames();
        } else { b.classList.add('no'); fb.className = 'vr-fb no'; fb.textContent = p.placeMiss; }
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
      var c = C.filter(function (x) { return x.key === p.cousin; })[0];
      return '<tr><td>' + esc(p.name) + '</td><td>' + (st.m[i] ? esc(c.name) : '<i>not matched yet</i>') + '</td><td>' + (st.p[i] ? esc(G.places[p.place]) : '<i>not picked yet</i>') + '</td></tr>';
    }).join('');
    var sents = tas.map(function (t, i) { return '<p><b>' + esc(G.frames[i]) + '</b><br>' + (t.value ? esc(t.value) : '<i>(not written yet)</i>') + '</p>'; }).join('');
    var h = '<!doctype html><html><head><meta charset="utf-8"><title>' + esc(V.canvas) + ' · ' + esc(name) + '</title><style>body{font:16px/1.5 Arial,sans-serif;max-width:720px;margin:24px auto;padding:0 16px;color:#222}h1{font-size:22px;margin:4px 0}.k{font-size:12px;letter-spacing:.14em;text-transform:uppercase;color:#7A5F2C}table{border-collapse:collapse;width:100%}th{background:#14110D;color:#fff;text-align:left;padding:5px 8px;font-size:13px}td{border:1px solid #ddd;padding:6px 8px}.st{display:inline-block;border:3px solid #1B4332;color:#1B4332;font-weight:900;letter-spacing:2px;padding:3px 12px;border-radius:8px;transform:rotate(-3deg);text-transform:uppercase}@media print{button{display:none}}</style></head><body>' +
      '<div class="k">Optima Academy Online · 3rd Grade Science · Week ' + V.week + '</div><h1>' + esc(V.canvas) + ' (Studio Day)</h1>' +
      '<p><b>Name:</b> ' + esc(name) + ' &nbsp; <b>Date:</b> ' + new Date().toLocaleDateString() + '</p>' +
      '<h2>Fossil cousins</h2><table><tr><th>Fossil</th><th>Living cousin</th><th>Where it lived</th></tr>' + rows + '</table>' +
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
