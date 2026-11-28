/* Park Slide Studio (G3 science 32.02, Nov 2026). Bethany: "could we have them build their presentation in the lesson?
   like an embedded mini powerpoint tool?"  Students pick a park, build 6 slides (one per criterion) from a bank of
   public-domain park photos (or their own picture), present with a 2-minute timer, and download a real .pptx for Canvas.
   Data: WL_DATA.studio. Saves in this browser (localStorage, wrapped in try). The checklist asks WLStudio.done(). */
(function () {
  'use strict';
  var D = window.WL_DATA || {}, ST = D.studio, IMG = window.WF_IMG || {}, root = document.getElementById('wl-studio');
  if (!ST || !root) return;
  var $ = function (s, r) { return (r || document).querySelector(s); }, $$ = function (s, r) { return [].slice.call((r || document).querySelectorAll(s)); };
  var KEY = 'wl-studio-' + D.id, S = {};
  try { S = JSON.parse(localStorage.getItem(KEY) || '{}') || {}; } catch (e) { S = {}; }
  S.slides = S.slides || {};
  var warned = false;
  function save() { try { localStorage.setItem(KEY, JSON.stringify(S)); } catch (e) { if (!warned) { warned = true; toast('Your slides are too big to save in this browser. Finish and download them before you close the page.'); } } refresh(); }
  function refresh() { if (window.WL4 && WL4.refresh) WL4.refresh(); }
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function words(t) { return ((t || '').trim().match(/[A-Za-z0-9'’]+/g) || []).length; }
  function toast(m) { var t = document.createElement('div'); t.className = 'wl-toast'; t.setAttribute('role', 'status'); t.innerHTML = m + '<button aria-label="Close">✕</button>'; document.body.appendChild(t);
    var bar = $('.wl-top'); t.style.top = ((bar ? bar.offsetHeight : 0) + 10) + 'px'; t.querySelector('button').onclick = function () { t.remove(); }; setTimeout(function () { t.remove(); }, 6000); }
  var CR = ST.criteria, MAXW = ST.words || 30, MINW = ST.minWords || 5;
  /* voice recordings (Bethany, 21 Nov 2026): kept in memory only, never saved to the device or sent anywhere.
     The only copy is the one placed inside the downloaded .pptx. Closing the page deletes them. */
  var REC = {}, recNow = null, MAXREC = ST.maxRecord || 30;
  function rec(i) { var p = park(); return p && REC[p.k] ? REC[p.k][i] : null; }
  function nRec() { var p = park(); return p && REC[p.k] ? Object.keys(REC[p.k]).filter(function (k) { return REC[p.k][k]; }).length : 0; }
  function park() { return ST.parks.filter(function (p) { return p.k === S.park; })[0] || null; }
  function deck() { var p = park(); if (!p) return null; var d = S.slides[p.k]; if (!d) { d = S.slides[p.k] = CR.map(function () { return { text: '', img: null, up: null }; }); } return d; }
  function photo(k) { var p = park(); return p ? p.photos.filter(function (x) { return x.img === k; })[0] : null; }
  function picSrc(s) { return s.up || (s.img && IMG[s.img]) || ''; }
  function webOf(p) { return p.web; }
  function org(p, n) { return p.web.orgs.filter(function (o) { return o.n === n; })[0]; }
  function chainOk(p, ch) { if (!ch || ch.length !== 3 || ch.some(function (x) { return !x; })) return false;
    var E = p.web.edges.map(function (e) { return e.join('>'); }); return E.indexOf(ch[0] + '>' + ch[1]) >= 0 && E.indexOf(ch[1] + '>' + ch[2]) >= 0; }
  function named(p, t) { t = ' ' + (t || '').toLowerCase().replace(/[^a-z\s-]/g, ' ') + ' '; var n = 0, seen = {};
    p.names.forEach(function (w) { var re = new RegExp('\\b' + w.replace(/[-]/g, '[- ]') + '(s|es)?\\b'); if (re.test(t) && !seen[w]) { seen[w] = 1; n++; } }); return n; }
  function specific(p, t, c) { if (c && c.k === 'place' && p.state && t.toLowerCase().indexOf(p.state.toLowerCase()) >= 0) return true; return /\d/.test(t) || /\b(because|so|since|which|when|by)\b/i.test(t) || named(p, t) > 0; }
  /* one slide is "done" when it meets its criterion inside the constraint: words in range + a picture (food web: a correct chain) */
  function slideOk(i) { var p = park(), d = deck(); if (!p) return false; var s = d[i], w = words(s.text), c = CR[i];
    if (w < MINW || w > MAXW) return false;
    if (c.k === 'web') return chainOk(p, s.chain);
    if (c.k === 'orgs' && named(p, s.text) < 3) return false;
    return !!picSrc(s); }
  function nDone() { var d = deck(); return d ? CR.filter(function (c, i) { return slideOk(i); }).length : 0; }

  window.WLStudio = {
    done: function () { return nDone() === CR.length && !!S.dl; },
    summary: function () { var p = park(), d = deck(); if (!p) return '';
      var o = ['PART C · MY SLIDES: ' + p.name + ' (' + nDone() + ' of ' + CR.length + ' criteria met' + (S.dl ? ', downloaded' : ', not downloaded yet') + ')'];
      CR.forEach(function (c, i) { var s = d[i]; o.push((i + 1) + '. ' + c.name + ': ' + (s.text.trim() || '(empty)') + (c.k === 'web' && s.chain ? '  [Sun → ' + s.chain.filter(Boolean).join(' → ') + ']' : '')); });
      return o.join('\n') + '\n'; }
  };

  /* ---------- slide drawing (editor preview, present mode and print all use this) ---------- */
  function slideHTML(i, opts) {
    var p = park(), d = deck(), s = d[i], c = CR[i], pic = picSrc(s), ph = s.img ? photo(s.img) : null, t = esc(s.text.trim()), nm = esc((S.name || '').trim());
    var cap = s.up ? 'My own picture' : (ph ? ph.cap : '');
    if (c.k === 'place') return '<div class="st-sl st-title" style="--pc:' + p.color + '">' + (pic ? '<img class="st-bg" src="' + pic + '" alt="' + esc(cap) + '">' : '') +
      '<div class="st-tt"><small>' + esc(ST.deckKicker || 'A national park ecosystem') + '</small><h4>' + esc(p.name) + '</h4><p>' + (t || '<i>' + esc(c.hint) + '</i>') + '</p>' + (nm ? '<em>by ' + nm + '</em>' : '') + '</div>' + (cap ? '<span class="st-cap">📷 ' + esc(cap) + '</span>' : '') + '</div>';
    var body;
    if (c.k === 'web') {
      var ch = s.chain || [], cells = [{ n: 'Sun', e: '☀️' }].concat([0, 1, 2].map(function (j) { return ch[j] ? org(p, ch[j]) : null; }));
      body = '<div class="st-web">' + cells.map(function (o, j) { return (j ? '<b class="st-arr" aria-hidden="true">➜</b>' : '') + '<span class="st-node' + (o ? '' : ' empty') + '">' + (o ? '<i>' + o.e + '</i>' + esc(o.n) : '?') + '</span>'; }).join('') + '</div>' +
        '<p class="st-webkey">' + esc(ST.webKey) + '</p><p class="st-tx">' + (t || '<i>' + esc(c.hint) + '</i>') + '</p>';
      return '<div class="st-sl st-std st-webs" style="--pc:' + p.color + '"><div class="st-k">' + c.icon + ' ' + esc(c.name) + '</div>' + body + '</div>';
    }
    return '<div class="st-sl st-std" style="--pc:' + p.color + '"><div class="st-pic">' + (pic ? '<img src="' + pic + '" alt="' + esc(cap) + '">' + (cap ? '<span class="st-cap">📷 ' + esc(cap) + '</span>' : '') : '<span class="st-nopic">📷 Pick a photo</span>') + '</div>' +
      '<div class="st-side"><div class="st-k">' + c.icon + ' ' + esc(c.name) + '</div><p class="st-tx">' + (t || '<i>' + esc(c.hint) + '</i>') + '</p></div></div>';
  }

  /* ---------- the studio ---------- */
  var cur = Math.min(S.cur || 0, CR.length - 1);
  function draw() {
    var p = park();
    if (!p && ST.intro && !S.intro) { intro(); return; }
    if (!p) {   // step 1: pick a park
      root.innerHTML = path(0) + '<div class="st-pick"><p class="st-lead">' + esc(ST.pickLead) + '</p><div class="st-parks">' + ST.parks.map(function (q) {
        return '<button type="button" class="st-park" data-p="' + q.k + '"><img src="' + IMG[q.cover] + '" alt="' + esc(q.coverAlt) + '"><b>' + esc(q.name) + '</b><span>' + esc(q.state) + '</span></button>'; }).join('') + '</div>' + (ST.intro ? '<p class="st-foot"><button type="button" class="st-link" id="st-intro">What\'s a presentation? See the example again</button></p>' : '') + '</div>';
      var ib = $('#st-intro', root); if (ib) ib.onclick = function () { S.intro = 0; save(); draw(); };
      $$('.st-park', root).forEach(function (b) { b.onclick = function () { S.park = b.dataset.p; S.cur = cur = 0; var d = deck(), a1 = ($('#in-a1') || {}).value || '';
        if (!d[0].text && a1.trim()) d[0].text = a1.trim().split(/\s+/).slice(0, MAXW).join(' ');   // Part A answer 1 starts the title slide
        save(); draw(); }; });
      return;
    }
    var d = deck(), s = d[cur], c = CR[cur], w = words(s.text), n = nDone();
    var meter = '<div class="st-meter" role="img" aria-label="' + n + ' of ' + CR.length + ' criteria met">' + CR.map(function (x, i) { return '<i class="' + (slideOk(i) ? 'on' : '') + '" title="' + esc(x.name) + '">' + x.icon + '</i>'; }).join('') + '<span>' + n + ' of ' + CR.length + ' criteria</span></div>';
    var rail = '<div class="st-rail" role="tablist" aria-label="My slides">' + CR.map(function (x, i) { return '<button type="button" role="tab" class="st-th' + (i === cur ? ' cur' : '') + (slideOk(i) ? ' ok' : '') + '" data-i="' + i + '" aria-selected="' + (i === cur) + '"><span>' + (i + 1) + '</span>' + x.icon + '<small>' + esc(x.short) + '</small></button>'; }).join('') + '</div>';
    var nudge = '';
    if (s.text.trim()) {
      if (c.k === 'orgs') { var k = named(p, s.text); nudge = k >= 3 ? '' : '<p class="st-ev">🔍 Evidence check: name 3 organisms from your park (you have ' + k + ').</p>'; }
      else if (c.k !== 'web') nudge = specific(p, s.text, c) ? '' : '<p class="st-ev">🔍 Evidence check: add something specific, like a number, a name, or a “because.”</p>';
    }
    var count = '<div class="st-count' + (w > MAXW ? ' over' : w >= MINW ? ' good' : '') + '">' + w + ' of ' + MAXW + ' words' + (w > MAXW ? ' · too many! Cut ' + (w - MAXW) + '. Visitors only have ' + (ST.minutes || 2) + ' minutes.' : w < MINW ? ' · write at least ' + MINW : ' ✓') + '</div>';
    var pic = c.k === 'web' ? chainOk(p, s.chain) : !!picSrc(s), wok = w >= MINW && w <= MAXW, eok = c.k === 'orgs' ? named(p, s.text) >= 3 : (c.k === 'web' ? chainOk(p, s.chain) && wok : specific(p, s.text, c));
    var checks = '<ul class="st-checks" aria-label="Strong slide checklist"><li class="' + (wok ? 'ok' : '') + '">' + MINW + ' to ' + MAXW + ' words</li><li class="' + (pic ? 'ok' : '') + '">' + (c.k === 'web' ? 'A food web with real arrows' : 'A picture') + '</li><li class="' + (eok ? 'ok' : '') + '">' + (c.k === 'orgs' ? '3 organisms named' : 'A specific detail') + '</li></ul>';
    var starter = !s.text.trim() && c.starter ? '<button type="button" class="st-mini" id="st-start">✏️ Use a sentence starter</button>' : '';
    var a2 = (($('#in-a2') || {}).value || '').trim();
    var FN = (p.notes || {})[c.k] || [], fnotes = FN.length ? '<details class="st-notes" open><summary>' + esc((ST.notesLead || '📒 Field Notes').replace('{park}', p.short)) + '</summary><ul>' + FN.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ul><p>' + esc(ST.notesTip || '') + '</p></details>' : '';
    var tools = fnotes + '<label class="st-lab" for="st-text">' + c.icon + ' Slide ' + (cur + 1) + ': ' + esc(c.ask) + '</label><textarea id="st-text" rows="3" placeholder="' + esc(c.hint) + '">' + esc(s.text) + '</textarea>' + starter + count + checks + nudge +
      (a2 && c.k !== 'web' ? '<button type="button" class="st-mini" id="st-a2">📌 Add my strongest evidence from Part A</button>' : '') +
      (c.k === 'place' ? '<label class="st-lab" for="st-name">Presenter (your first name)</label><input id="st-name" class="st-name" maxlength="20" autocomplete="off" value="' + esc(S.name || '') + '">' : '');
    if (c.k === 'web') {
      var W = p.web, ch = s.chain || [null, null, null];
      tools = fnotes + '<p class="st-lab">🕸️ Build your food web: pick one for each box.</p><div class="st-chain">' + (W.steps || ST.webSteps).map(function (st, j) {
        return '<div class="st-step"><b>' + esc(st.label) + '</b><div class="st-chips">' + W.orgs.filter(function (o) { return o.role === st.role; }).map(function (o) { return '<button type="button" class="st-chip' + (ch[j] === o.n ? ' on' : '') + '" data-j="' + j + '" data-n="' + esc(o.n) + '">' + o.e + ' ' + esc(o.n) + '</button>'; }).join('') + '</div></div>'; }).join('') + '</div>' +
        (ch.every(Boolean) ? (chainOk(p, ch) ? '<p class="st-ev ok">✅ Every arrow is real: each animal eats the one before it.</p>' : '<p class="st-ev">🤔 Check your arrows. ' + esc(webMiss(p, ch)) + '</p>') : '') + tools.replace(fnotes, '');
    } else {
      var mine = p.photos.filter(function (x) { return x.tag === c.k; }), rest = p.photos.filter(function (x) { return x.tag !== c.k; });
      tools += '<p class="st-lab">📷 Pick a real photo from ' + esc(p.short) + ' (all public domain), or upload your own.</p><div class="st-bank" role="listbox" aria-label="Photo bank">' +
        mine.concat(rest).map(function (x, j) { return (j === mine.length && mine.length ? '<span class="st-more">More photos</span>' : '') + '<button type="button" role="option" class="st-ph' + (s.img === x.img && !s.up ? ' on' : '') + '" data-k="' + x.img + '" aria-selected="' + (s.img === x.img && !s.up) + '" title="' + esc(x.cap) + '"><img loading="lazy" src="' + IMG[x.thumb || x.img] + '" alt="' + esc(x.cap) + '"></button>'; }).join('') + '</div>' +
        '<div class="st-uprow"><label class="st-mini st-up">⬆️ Upload my own picture<input type="file" accept="image/*" id="st-file" hidden></label>' + (s.up ? '<button type="button" class="st-mini" id="st-unup">✕ Remove my picture</button>' : '') + '</div>';
    }
    if (ST.record !== false) { var r0 = rec(cur);
      tools += '<div class="st-rec"><p class="st-lab">🎙️ Your voice (optional)</p>' + (recNow ? '<button type="button" class="st-mini st-recon" id="st-recstop">⏹ Stop recording <span id="st-rect">0</span>s</button>' :
        r0 ? '<audio controls src="' + r0.url + '"></audio><div><button type="button" class="st-mini" id="st-recgo">↻ Record again</button><button type="button" class="st-mini" id="st-recdel">✕ Delete my recording</button></div>' :
        '<button type="button" class="st-mini" id="st-recgo">🎙️ Record my voice for this slide</button>') +
        '<p class="st-note">Talk for up to ' + MAXREC + ' seconds. Your voice goes inside your downloaded slides. It is not saved anywhere else, so download before you close this page.</p><p class="st-ev" id="st-recmsg" hidden></p></div>'; }
    root.innerHTML = path(S.dl ? 4 : S.practiced ? 3 : n === CR.length ? 2 : 1) + '<div class="st-top"><b>' + esc(p.name) + '</b>' + meter + '</div>' + rail +
      '<div class="st-main"><div class="st-view" aria-live="polite">' + slideHTML(cur) + '</div><div class="st-tools">' + tools + '</div></div>' +
      '<div class="st-acts">' + (cur ? '<button type="button" class="wl-btn ghost" id="st-prev">◂ Slide ' + cur + '</button>' : '') + (cur < CR.length - 1 ? '<button type="button" class="wl-btn ghost" id="st-next">Next: slide ' + (cur + 2) + ' ▸</button>' : '') +
      '<button type="button" class="wl-btn gold" id="st-show">▶ Present (' + (ST.minutes || 2) + ' min)</button><button type="button" class="wl-btn" id="st-vidmake">🎬 Make my video</button><button type="button" class="wl-btn" id="st-dl">⬇️ Download my slides</button><button type="button" class="wl-btn ghost" id="st-print">🖨️ Print or save as PDF</button></div>' +
      '<p class="st-foot">' + (S.dl ? '✅ Downloaded. Upload the file to Canvas. Then press Clear my slides if someone else uses this computer. ' : '') + (nRec() ? '🎙️ ' + nRec() + ' of ' + CR.length + ' slides have your voice. ' : '') + '<button type="button" class="st-link" id="st-switch">Switch park</button> · Your words and pictures save in this browser. <button type="button" class="st-link" id="st-clear">🧹 Clear my slides</button></p>';
    wire();
  }
  function c0(i) { var p = park(), c = CR[i]; return (c.starter || '').replace('{name}', p.name).replace('{state}', p.state).replace('{short}', p.short); }
  /* the 4-step path at the top: Pick → Build 6 slides → Practice → Download */
  function path(at) { var st = ST.steps || []; if (!st.length) return '';
    return '<ol class="st-path" aria-label="Your steps">' + st.map(function (t, i) { return '<li class="' + (i < at ? 'done' : i === at ? 'now' : '') + '"><b>' + (i < at ? '✓' : i + 1) + '</b>' + esc(t) + '</li>'; }).join('') + '</ol>'; }
  /* scaffolding for first-timers: what a presentation is, with one strong and one weak example slide */
  function intro() { var I = ST.intro, ex = function (o, img) { return '<figure class="st-ex"><div class="st-sl st-std" style="--pc:#3E6B4E">' + (img ? '<div class="st-pic"><img src="' + IMG[I.img] + '" alt="' + esc(I.imgCap) + '"><span class="st-cap">📷 ' + esc(I.imgCap) + '</span></div>' : '<div class="st-pic"><span class="st-nopic">no picture</span></div>') +
      '<div class="st-side"><div class="st-k">' + esc(o.kicker) + '</div><p class="st-tx' + (img ? '' : ' st-tiny') + '">' + esc(o.text) + '</p></div></div><figcaption>' + esc(o.why) + '</figcaption></figure>'; };
    root.innerHTML = path(0) + '<div class="st-intro"><h4>' + esc(I.title) + '</h4><ul>' + I.points.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul><div class="st-exs">' + ex(I.good, true) + ex(I.bad, false) + '</div><div style="text-align:center"><button type="button" class="wl-btn gold" id="st-go">' + esc(I.go) + '</button></div></div>';
    $('#st-go', root).onclick = function () { S.intro = 1; save(); draw(); var t = $('#m-studio'); if (t && t.getBoundingClientRect().top < 0) t.scrollIntoView({ block: 'start' }); }; }
  /* before Present: how to present like a ranger */
  function tips(next) { var T = ST.tips; if (!T) return next(); var o = document.createElement('div'); o.className = 'st-show st-tipsbox'; o.setAttribute('role', 'dialog'); o.setAttribute('aria-label', T.title);
    o.innerHTML = '<div class="st-tips"><h4>' + esc(T.title) + '</h4><ol>' + T.items.map(function (x) { return '<li>' + esc(x) + '</li>'; }).join('') + '</ol><p>' + esc(T.who) + '</p><div class="st-tipsb"><button type="button" class="wl-btn ghost" data-x>Not yet</button><button type="button" class="wl-btn gold" data-go>' + esc(T.go) + '</button></div></div>';
    document.body.appendChild(o); o.querySelector('[data-x]').onclick = function () { o.remove(); }; o.querySelector('[data-go]').onclick = function () { o.remove(); S.practiced = 1; save(); draw(); next(); }; o.querySelector('[data-go]').focus(); }
  function recMsg(t) { var m = $('#st-recmsg', root); if (m) { m.hidden = false; m.innerHTML = t; } }
  function record(pk, ix) {
    var blocked = 'The microphone is blocked here, so the studio can\'t record. That\'s OK: your slides still work. If your teacher asks for your voice, use <b>Record media</b> on the Canvas assignment.';
    if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia || !window.MediaRecorder) { recMsg(blocked); return; }
    navigator.mediaDevices.getUserMedia({ audio: true }).then(function (stream) {
      var chunks = [], mr; try { mr = new MediaRecorder(stream); } catch (e) { stream.getTracks().forEach(function (t) { t.stop(); }); recMsg(blocked); return; }
      var t0 = Date.now(), tm = setInterval(function () { var s = Math.floor((Date.now() - t0) / 1000), e = $('#st-rect', root); if (e) e.textContent = s; if (s >= MAXREC && mr.state === 'recording') mr.stop(); }, 250);
      mr.ondataavailable = function (e) { if (e.data && e.data.size) chunks.push(e.data); };
      mr.onstop = function () { clearInterval(tm); stream.getTracks().forEach(function (t) { t.stop(); }); recNow = null;
        var blob = new Blob(chunks, { type: mr.mimeType || 'audio/webm' }), old = (REC[pk] || {})[ix]; if (old) URL.revokeObjectURL(old.url);
        if (blob.size) { REC[pk] = REC[pk] || {}; REC[pk][ix] = { blob: blob, url: URL.createObjectURL(blob), sec: Math.round((Date.now() - t0) / 1000) }; }
        draw(); };
      recNow = mr; mr.start(); draw();
    }, function () { recMsg(blocked); });
  }
  /* a recording goes into PowerPoint as a WAV file (mono, 22 kHz), which PowerPoint and Keynote both play */
  function wav(blob, cb) {
    var AC = window.AudioContext || window.webkitAudioContext; if (!AC || !blob) return cb(null);
    blob.arrayBuffer().then(function (buf) { var ac = new AC(); return ac.decodeAudioData(buf).then(function (ab) { try { ac.close(); } catch (e) {}
      var rate = 22050, n = Math.ceil(ab.duration * rate), oc = new (window.OfflineAudioContext || window.webkitOfflineAudioContext)(1, n, rate), src = oc.createBufferSource(); src.buffer = ab; src.connect(oc.destination); src.start(0);
      return oc.startRendering(); }); }).then(function (r) {
      var d = r.getChannelData(0), b = new ArrayBuffer(44 + d.length * 2), v = new DataView(b), w = function (o, t) { for (var i = 0; i < t.length; i++) v.setUint8(o + i, t.charCodeAt(i)); };
      w(0, 'RIFF'); v.setUint32(4, 36 + d.length * 2, true); w(8, 'WAVE'); w(12, 'fmt '); v.setUint32(16, 16, true); v.setUint16(20, 1, true); v.setUint16(22, 1, true); v.setUint32(24, 22050, true); v.setUint32(28, 44100, true); v.setUint16(32, 2, true); v.setUint16(34, 16, true); w(36, 'data'); v.setUint32(40, d.length * 2, true);
      for (var i = 0; i < d.length; i++) { var x = Math.max(-1, Math.min(1, d[i])); v.setInt16(44 + i * 2, x < 0 ? x * 0x8000 : x * 0x7FFF, true); }
      var fr = new FileReader(); fr.onload = function () { cb(fr.result); }; fr.onerror = function () { cb(null); }; fr.readAsDataURL(new Blob([b], { type: 'audio/wav' }));
    }).catch(function () { cb(null); });
  }

  /* ---------- 🎬 Make my video (Bethany, 21 Nov 2026: "maybe it should download as an mp4 for easier grading"):
     the slides play in order on a canvas, each with the student's own recording (or about 6 seconds without one),
     and the browser records it as an .mp4 (Chrome, Edge, Safari) or .webm. Takes as long as the video. Nothing is uploaded. */
  function loadImg(src) { return new Promise(function (ok) { if (!src) return ok(null); var im = new Image(); im.onload = function () { ok(im); }; im.onerror = function () { ok(null); }; im.src = src; }); }
  function cover(x, im, X0, Y0, W, H) { var r = W / H, iw = im.naturalWidth, ih = im.naturalHeight, sw = iw, sh = ih; if (iw / ih > r) sw = ih * r; else sh = iw / r; x.drawImage(im, (iw - sw) / 2, (ih - sh) / 2, sw, sh, X0, Y0, W, H); }
  function wrap(x, t, X0, Y0, W, maxH, size, font, lh) { var s = size, lines;
    for (;;) { x.font = font.replace('{s}', s); lines = []; var line = ''; t.split(/\s+/).forEach(function (w) { var tt = line ? line + ' ' + w : w; if (x.measureText(tt).width > W && line) { lines.push(line); line = w; } else line = tt; }); if (line) lines.push(line);
      if (lines.length * s * lh <= maxH || s <= 16) break; s -= 2; }
    lines.forEach(function (l, i) { x.fillText(l, X0, Y0 + s + i * s * lh); }); return Y0 + lines.length * s * lh; }
  function paint(x, i, p, d, im) { var c = CR[i], s = d[i], t = s.text.trim() || c.hint, G = p.color, ph = s.img ? photo(s.img) : null, cap = s.up ? 'My own picture' : ph ? ph.cap : '';
    x.fillStyle = '#15231B'; x.fillRect(0, 0, 1280, 720); x.textBaseline = 'alphabetic';
    if (c.k === 'place') { if (im) cover(x, im, 0, 0, 1280, 720); var g = x.createLinearGradient(0, 330, 0, 720); g.addColorStop(0, 'rgba(0,0,0,0)'); g.addColorStop(.35, 'rgba(0,0,0,.78)'); g.addColorStop(1, 'rgba(0,0,0,.85)'); x.fillStyle = g; x.fillRect(0, 330, 1280, 390);
      x.fillStyle = '#E3B04B'; x.font = 'bold 24px Arial'; x.fillText((ST.deckKicker || '').toUpperCase(), 60, 500); x.fillStyle = '#fff'; x.font = 'bold 64px Georgia'; x.fillText(p.name, 60, 570);
      x.fillStyle = '#fff'; var y = wrap(x, t, 60, 586, 1160, 90, 32, '{s}px Arial', 1.3); if ((S.name || '').trim()) { x.fillStyle = '#E3B04B'; x.font = 'italic 26px Georgia'; x.fillText('by ' + S.name.trim(), 60, Math.min(700, y + 34)); } }
    else if (c.k === 'web') { x.fillStyle = '#fff'; x.font = 'bold 44px Georgia'; x.fillText(c.icon + '  ' + c.name, 60, 90);
      var cells = [{ n: 'Sun', e: '☀️' }].concat((s.chain || [null, null, null]).map(function (n) { return n ? org(p, n) : { n: '?', e: '' }; }));
      cells.forEach(function (o, j) { var X0 = 60 + j * 300; x.fillStyle = j ? G : '#E3B04B'; x.beginPath(); if (x.roundRect) x.roundRect(X0, 160, 240, 170, 18); else x.rect(X0, 160, 240, 170); x.fill();
        x.fillStyle = j ? '#fff' : '#15231B'; x.textAlign = 'center'; x.font = '54px Arial'; if (o.e) x.fillText(o.e, X0 + 120, 240); x.font = 'bold 26px Arial'; x.fillText(o.n, X0 + 120, 300); x.textAlign = 'left';
        if (j < 3) { x.strokeStyle = '#fff'; x.lineWidth = 5; x.beginPath(); x.moveTo(X0 + 248, 245); x.lineTo(X0 + 290, 245); x.stroke(); x.beginPath(); x.moveTo(X0 + 296, 245); x.lineTo(X0 + 282, 236); x.lineTo(X0 + 282, 254); x.closePath(); x.fillStyle = '#fff'; x.fill(); } });
      x.fillStyle = '#C9D8CF'; x.font = 'italic 22px Arial'; x.fillText(ST.webKey, 60, 380); x.fillStyle = '#fff'; wrap(x, t, 60, 410, 1160, 270, 38, '{s}px Arial', 1.3); }
    else { if (im) cover(x, im, 0, 0, 666, 720); else { x.fillStyle = '#0b120e'; x.fillRect(0, 0, 666, 720); } x.fillStyle = G; x.fillRect(666, 0, 10, 720);
      x.fillStyle = '#E3B04B'; x.font = 'bold 26px Arial'; x.fillText(c.icon + '  ' + c.name.toUpperCase(), 712, 90); x.fillStyle = '#fff'; wrap(x, t, 712, 120, 520, 560, 40, '{s}px Arial', 1.32); }
    if (cap) { x.font = '16px Arial'; var w = x.measureText('📷 ' + cap).width + 16, X0 = c.k === 'place' ? 1264 - w : 12; x.fillStyle = 'rgba(0,0,0,.6)'; x.fillRect(X0, 690, w, 24); x.fillStyle = '#fff'; x.fillText('📷 ' + cap, X0 + 8, 708); } }
  function movie() {
    var p = park(); if (!p) return; var d = deck();
    if (!window.MediaRecorder || !HTMLCanvasElement.prototype.captureStream) { toast('This browser can\'t make videos. Use Download my slides instead.'); return; }
    var types = ['video/mp4;codecs=avc1.42E01E,mp4a.40.2', 'video/mp4;codecs=avc1,mp4a.40.2', 'video/mp4;codecs=avc1,opus', 'video/mp4', 'video/webm;codecs=vp9,opus', 'video/webm;codecs=vp8,opus', 'video/webm'], type = types.filter(function (t) { return MediaRecorder.isTypeSupported(t); })[0];
    if (!type) { toast('This browser can\'t make videos. Use Download my slides instead.'); return; }
    var o = document.createElement('div'); o.className = 'st-show st-making'; o.setAttribute('role', 'dialog'); o.setAttribute('aria-label', 'Making my video');
    o.innerHTML = '<div class="st-mk"><h4>🎬 Making your video…</h4><canvas width="1280" height="720"></canvas><div class="st-bar2"><i></i></div><p class="st-mkt">Getting ready…</p><p class="st-note">Keep this page open. Your video is made on this computer and isn\'t uploaded anywhere.</p><button type="button" class="wl-btn ghost" data-x>Cancel</button></div>';
    document.body.appendChild(o); var cv = o.querySelector('canvas'), x = cv.getContext('2d'), bar = o.querySelector('.st-bar2 i'), msg = o.querySelector('.st-mkt'), stop = false, mr = null, AC = null;
    o.querySelector('[data-x]').onclick = function () { stop = true; if (mr && mr.state === 'recording') mr.stop(); o.remove(); try { AC && AC.close(); } catch (e) {} };
    var AudioC = window.AudioContext || window.webkitAudioContext; AC = AudioC ? new AudioC() : null; var dest = AC ? AC.createMediaStreamDestination() : null;
    if (AC && dest) { try { var hum = AC.createOscillator(), hz = AC.createGain(); hz.gain.value = 0; hum.connect(hz); hz.connect(dest); hum.start(); } catch (e) {} }
    Promise.all(CR.map(function (c, i) { return loadImg(c.k === 'web' ? '' : picSrc(d[i])); })).then(function (ims) {
      return Promise.all(CR.map(function (c, i) { var r = (REC[p.k] || {})[i]; return r && AC ? r.blob.arrayBuffer().then(function (b) { return AC.decodeAudioData(b); }).catch(function () { return null; }) : Promise.resolve(null); })).then(function (bufs) { return [ims, bufs]; });
    }).then(function (res) { if (stop) return; var ims = res[0], bufs = res[1];
      var durs = CR.map(function (c, i) { return bufs[i] ? bufs[i].duration + 1.2 : 6; }), total = durs.reduce(function (a, b) { return a + b; }, 0) + 1;
      paint(x, 0, p, d, ims[0]); var stream = cv.captureStream(30); if (dest) dest.stream.getAudioTracks().forEach(function (t) { stream.addTrack(t); });
      var chunks = []; mr = new MediaRecorder(stream, { mimeType: type, videoBitsPerSecond: 2500000 }); mr.ondataavailable = function (e) { if (e.data && e.data.size) chunks.push(e.data); };
      mr.onstop = function () { clearInterval(tk); if (stop) return; try { AC && AC.close(); } catch (e) {} var ext = /mp4/.test(type) ? 'mp4' : 'webm', blob = new Blob(chunks, { type: type.split(';')[0] }), a = document.createElement('a');
        a.href = URL.createObjectURL(blob); a.download = 'Lesson-' + (D.lesson || '').replace('.', '-') + '-' + p.k + '-my-presentation.' + ext; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 5000);
        o.remove(); S.dl = true; save(); draw(); toast('🎬 Your video is in your Downloads. Upload it to Canvas.'); };
      if (AC && AC.state === 'suspended') AC.resume();
      mr.start(1000); var t0 = performance.now(), cur = -1, starts = [], acc = 0; durs.forEach(function (v) { starts.push(acc); acc += v; });
      var tk = setInterval(function () { var t = (performance.now() - t0) / 1000, i = 0; while (i < CR.length - 1 && t >= starts[i + 1]) i++;
        if (i !== cur) { cur = i; if (bufs[i] && AC) { var src = AC.createBufferSource(); src.buffer = bufs[i]; src.connect(dest); src.start(AC.currentTime + .4); } msg.textContent = 'Slide ' + (i + 1) + ' of ' + CR.length + (bufs[i] ? ' · with your voice' : ''); }
        paint(x, i, p, d, ims[i]); bar.style.width = Math.min(100, t / total * 100) + '%'; if (t >= total && mr.state === 'recording') mr.stop(); }, 100);
    });
  }
  function webMiss(p, ch) { var E = p.web.edges.map(function (e) { return e.join('>'); });
    if (E.indexOf(ch[0] + '>' + ch[1]) < 0) return 'Does the ' + ch[1].toLowerCase() + ' eat ' + ch[0].toLowerCase() + '? Try another plant-eater or plant.';
    return 'Does the ' + ch[2].toLowerCase() + ' eat the ' + ch[1].toLowerCase() + '? Try another pair.'; }
  function preview() { var v = $('.st-view', root); if (v) v.innerHTML = slideHTML(cur); }
  function wire() {
    var d = deck(), s = d[cur];
    $$('.st-th', root).forEach(function (b) { b.onclick = function () { go(+b.dataset.i); }; });
    var ta = $('#st-text', root);
    if (ta) ta.addEventListener('input', function () { s.text = ta.value; preview(); clearTimeout(ta._t); ta._t = setTimeout(function () { save(); var pos = ta.selectionStart; draw(); var t2 = $('#st-text', root); if (t2) { t2.focus(); t2.setSelectionRange(pos, pos); } }, 700); });
    var sb = $('#st-start', root); if (sb) sb.onclick = function () { s.text = c0(cur); save(); draw(); var t2 = $('#st-text', root); if (t2) { t2.focus(); t2.setSelectionRange(t2.value.length, t2.value.length); } };
    var nm = $('#st-name', root); if (nm) nm.addEventListener('input', function () { S.name = nm.value; preview(); save(); });
    var a2 = $('#st-a2', root); if (a2) a2.onclick = function () { var v = (($('#in-a2') || {}).value || '').trim(); s.text = (s.text.trim() ? s.text.trim() + ' ' : '') + v; save(); draw(); toast('📌 Added. Now trim it to fit ' + MAXW + ' words.'); };
    $$('.st-ph', root).forEach(function (b) { b.onclick = function () { s.img = b.dataset.k; s.up = null; save(); draw(); }; });
    $$('.st-chip', root).forEach(function (b) { b.onclick = function () { s.chain = s.chain || [null, null, null]; s.chain[+b.dataset.j] = b.dataset.n; save(); draw(); }; });
    var f = $('#st-file', root); if (f) f.onchange = function () { var file = f.files && f.files[0]; if (!file) return; shrink(file, function (url) { if (!url) { toast('That picture could not be opened. Try a JPG or PNG.'); return; } s.up = url; save(); draw(); }); };
    var un = $('#st-unup', root); if (un) un.onclick = function () { s.up = null; save(); draw(); };
    var pv = $('#st-prev', root), nx = $('#st-next', root); if (pv) pv.onclick = function () { go(cur - 1); }; if (nx) nx.onclick = function () { go(cur + 1); };
    $('#st-show', root).onclick = function () { tips(show); }; $('#st-dl', root).onclick = download; $('#st-vidmake', root).onclick = movie; $('#st-print', root).onclick = print;
    var rg = $('#st-recgo', root), rs = $('#st-recstop', root), rd = $('#st-recdel', root), ix = cur, pk = park().k;
    if (rg) rg.onclick = function () { record(pk, ix); };
    if (rs) rs.onclick = function () { if (recNow) recNow.stop(); };
    if (rd) rd.onclick = function () { var r = (REC[pk] || {})[ix]; if (r) URL.revokeObjectURL(r.url); if (REC[pk]) delete REC[pk][ix]; draw(); };
    var cl = $('#st-clear', root); if (cl) cl.onclick = function () { if (!cl.dataset.sure) { cl.dataset.sure = 1; cl.textContent = 'Tap again to erase all your slides on this computer'; setTimeout(function () { if (cl.isConnected) { delete cl.dataset.sure; cl.textContent = '🧹 Clear my slides'; } }, 5000); return; }
      Object.keys(REC).forEach(function (k) { Object.keys(REC[k]).forEach(function (i) { if (REC[k][i]) URL.revokeObjectURL(REC[k][i].url); }); }); REC = {}; S = { slides: {}, intro: 1 }; cur = 0; save(); draw(); toast('🧹 Cleared. Your slides are erased from this computer.'); };
    $('#st-switch', root).onclick = function () { if (!confirmSwitch()) return; S.park = null; save(); draw(); };
  }
  function confirmSwitch() { return true; }   // each park keeps its own slides, so switching never loses work
  function go(i) { if (i < 0 || i >= CR.length) return; cur = S.cur = i; save(); draw(); var t = $('.st-view', root); if (t && t.getBoundingClientRect().top < 60) t.scrollIntoView({ block: 'start' }); }
  /* an uploaded picture is shrunk so it fits in the browser's storage (max 900 px, JPEG) */
  function shrink(file, cb) { var r = new FileReader(); r.onload = function () { var im = new Image(); im.onload = function () { var k = Math.min(1, 900 / Math.max(im.width, im.height)), c = document.createElement('canvas');
    c.width = Math.round(im.width * k); c.height = Math.round(im.height * k); c.getContext('2d').drawImage(im, 0, 0, c.width, c.height); try { cb(c.toDataURL('image/jpeg', .72)); } catch (e) { cb(null); } }; im.onerror = function () { cb(null); }; im.src = r.result; }; r.onerror = function () { cb(null); }; r.readAsDataURL(file); }

  /* ---------- present mode: full screen, arrow keys, a 2-minute visitor timer ---------- */
  function show() {
    var p = park(); if (!p) return; var i = 0, left = (ST.minutes || 2) * 60, o = document.createElement('div'); o.className = 'st-show'; o.setAttribute('role', 'dialog'); o.setAttribute('aria-label', 'Present my slides');
    o.innerHTML = '<div class="st-stage"></div><div class="st-bar"><button type="button" class="st-b" data-a="prev" aria-label="Previous slide">◂</button><span class="st-n"></span><button type="button" class="st-b" data-a="next" aria-label="Next slide">▸</button><span class="st-clock" aria-live="off"></span><button type="button" class="st-b" data-a="x">✕ Done</button></div>';
    document.body.appendChild(o); var stage = $('.st-stage', o), clock = $('.st-clock', o);
    function paint() { stage.innerHTML = slideHTML(i); $('.st-n', o).textContent = 'Slide ' + (i + 1) + ' of ' + CR.length; }
    function tick() { left--; var m = Math.max(0, left); clock.textContent = '⏱ ' + Math.floor(m / 60) + ':' + ('0' + m % 60).slice(-2); clock.classList.toggle('low', m <= 20); if (left === 0) clock.textContent = '⏰ Time! Did your visitor see all ' + CR.length + '?'; }
    function close() { clearInterval(tm); document.removeEventListener('keydown', key); if (document.fullscreenElement) document.exitFullscreen().catch(function () {}); o.remove(); }
    function key(e) { if (e.key === 'ArrowRight' || e.key === ' ') { e.preventDefault(); i = Math.min(CR.length - 1, i + 1); paint(); } else if (e.key === 'ArrowLeft') { i = Math.max(0, i - 1); paint(); } else if (e.key === 'Escape') close(); }
    o.addEventListener('click', function (e) { var a = e.target.closest('[data-a]'); if (!a) return; if (a.dataset.a === 'x') close(); else { i = Math.max(0, Math.min(CR.length - 1, i + (a.dataset.a === 'next' ? 1 : -1))); paint(); } });
    document.addEventListener('keydown', key); paint(); left++; tick(); var tm = setInterval(tick, 1000);
    try { if (o.requestFullscreen) o.requestFullscreen().catch(function () {}); } catch (e) {}
  }

  /* ---------- print / save as PDF ---------- */
  function print() {
    if (!park()) return; var w = window.open(''); if (!w) { toast('Your browser blocked the print window. Allow pop-ups, then try again.'); return; }
    var css = [].slice.call(document.styleSheets).map(function (sh) { try { return [].slice.call(sh.cssRules).map(function (r) { return r.cssText; }).join('\n'); } catch (e) { return ''; } }).join('\n');
    w.document.write('<!doctype html><html><head><meta charset="utf-8"><title>' + esc(park().name) + ' · my slides</title><style>' + css + '\nbody{margin:0;background:#fff}.st-print{width:960px;margin:0 auto}.st-print .st-sl{margin:0 0 18px;page-break-inside:avoid;break-inside:avoid}@page{size:landscape;margin:10mm}</style></head><body><div class="st-print">' +
      CR.map(function (c, i) { return slideHTML(i); }).join('') + '</div></body></html>');
    w.document.close(); setTimeout(function () { w.focus(); w.print(); }, 700);
  }

  /* ---------- download a real PowerPoint file (pptxgenjs, loaded only now) ---------- */
  function lib(cb) { if (window.PptxGenJS) return cb(); if (!ST.lib) { toast('The slide maker could not load. Use Print or save as PDF instead.'); return; }
    var sc = document.createElement('script'); sc.src = new URL(ST.lib, document.baseURI).href; sc.onload = cb; sc.onerror = function () { toast('The slide maker could not load. Check your internet, or use Print or save as PDF.'); }; document.head.appendChild(sc); }
  /* every picture is cropped here to the exact box it fills, so it is never stretched in PowerPoint */
  function boxed(src, bw, bh, cb) { if (!src) return cb(null); var im = new Image(); im.crossOrigin = 'anonymous';
    im.onload = function () { var r = bw / bh, W = im.naturalWidth, H = im.naturalHeight, sw = W, sh = H; if (W / H > r) sw = H * r; else sh = W / r;
      var c = document.createElement('canvas'), px = Math.min(1400, Math.round(sw)); c.width = px; c.height = Math.round(px / r);
      c.getContext('2d').drawImage(im, (W - sw) / 2, (H - sh) / 2, sw, sh, 0, 0, c.width, c.height); try { cb(c.toDataURL('image/jpeg', .85)); } catch (e) { cb(null); } };
    im.onerror = function () { cb(null); }; im.src = src; }
  function download() {
    var p = park(); if (!p) return; var btn = $('#st-dl', root); if (btn) { btn.disabled = true; btn.textContent = '⏳ Making your file…'; }
    var d = deck(), jobs = CR.map(function (c, i) { return c.k === 'web' ? null : { src: picSrc(d[i]), w: c.k === 'place' ? 10 : 5.2, h: 5.625 }; }), pics = [], left = jobs.length;
    jobs.forEach(function (j, i) { if (!j) { pics[i] = null; if (!--left) build(); return; } boxed(j.src, j.w, j.h, function (u) { pics[i] = u; if (!--left) build(); }); });
    function done(ok) { if (btn) { btn.disabled = false; btn.textContent = '⬇️ Download my slides'; } if (ok) { S.dl = true; save(); draw(); toast('⬇️ Downloaded! Find the file in your Downloads, then upload it to Canvas.'); } }
    function build() { var auds = [], left2 = CR.length; CR.forEach(function (c, i) { var r = (REC[p.k] || {})[i]; if (!r) { if (!--left2) go2(); return; } wav(r.blob, function (u) { auds[i] = u; if (!--left2) go2(); }); });
      function go2() { lib(function () { try { make(p, d, pics, auds).then(function () { done(true); }, function () { toast('The file did not save. Try again, or use Print or save as PDF.'); done(false); }); } catch (e) { toast('The file did not save. Try again, or use Print or save as PDF.'); done(false); } }); } }
  }
  function make(p, d, pics, auds) {
    var X = new window.PptxGenJS(); X.layout = 'LAYOUT_16x9'; X.title = p.name + ' · my national park presentation'; X.author = (S.name || '').trim() || 'Grade 3 scientist';
    var G = p.color.replace('#', ''), F = 'Georgia', nm = (S.name || '').trim();
    CR.forEach(function (c, i) {
      var s = d[i], sl = X.addSlide(), tx = s.text.trim() || c.hint, ph = s.img ? photo(s.img) : null, cap = s.up ? 'Photo: my own picture' : ph ? 'Photo: ' + ph.cap + ' (public domain)' : '';
      sl.background = { color: '15231B' };
      if (c.k === 'place') {
        if (pics[i]) sl.addImage({ data: pics[i], x: 0, y: 0, w: 10, h: 5.625 });
        sl.addShape('rect', { x: 0, y: 3.0, w: 10, h: 2.625, fill: { color: '000000', transparency: 35 }, line: { color: '000000', transparency: 100 } });
        sl.addText((ST.deckKicker || 'A national park ecosystem').toUpperCase(), { x: .5, y: 3.1, w: 9, h: .35, fontFace: 'Arial', fontSize: 12, bold: true, color: 'E3B04B', charSpacing: 2 });
        sl.addText(p.name, { x: .5, y: 3.4, w: 9, h: .75, fontFace: F, fontSize: 36, bold: true, color: 'FFFFFF', fit: 'shrink' });
        sl.addText(tx, { x: .5, y: 4.15, w: 9, h: .9, fontFace: 'Arial', fontSize: 18, color: 'FFFFFF', fit: 'shrink', valign: 'top' });
        if (nm) sl.addText('by ' + nm, { x: .5, y: 5.05, w: 5, h: .35, fontFace: F, fontSize: 14, italic: true, color: 'E3B04B' });
      } else if (c.k === 'web') {
        sl.addText(c.icon + '  ' + c.name, { x: .5, y: .3, w: 9, h: .6, fontFace: F, fontSize: 26, bold: true, color: 'FFFFFF' });
        var cells = [{ n: 'Sun', e: '☀️' }].concat((s.chain || []).map(function (n) { return n ? org(p, n) : { n: '?', e: '' }; }));
        while (cells.length < 4) cells.push({ n: '?', e: '' });
        cells.forEach(function (o, j) { var x = .45 + j * 2.4;
          sl.addText((o.e ? o.e + '\n' : '') + o.n, { x: x, y: 1.35, w: 1.85, h: 1.35, shape: X.ShapeType.roundRect, rectRadius: .15, fill: { color: j ? G : 'E3B04B' }, color: j ? 'FFFFFF' : '15231B', fontFace: 'Arial', fontSize: 16, bold: true, align: 'center', valign: 'middle', fit: 'shrink' });
          if (j < 3) sl.addShape(X.ShapeType.line, { x: x + 1.9, y: 2.03, w: .45, h: 0, line: { color: 'FFFFFF', width: 3, endArrowType: 'triangle' } }); });
        sl.addText(ST.webKey, { x: .5, y: 2.85, w: 9, h: .4, fontFace: 'Arial', fontSize: 12, italic: true, color: 'C9D8CF' });
        sl.addText(tx, { x: .5, y: 3.35, w: 9, h: 1.9, fontFace: 'Arial', fontSize: 20, color: 'FFFFFF', valign: 'top', fit: 'shrink' });
      } else {
        if (pics[i]) sl.addImage({ data: pics[i], x: 0, y: 0, w: 5.2, h: 5.625 });
        sl.addShape('rect', { x: 5.2, y: 0, w: .08, h: 5.625, fill: { color: G }, line: { color: G } });
        sl.addText(c.icon + '  ' + c.name.toUpperCase(), { x: 5.55, y: .35, w: 4.2, h: .7, fontFace: 'Arial', fontSize: 14, bold: true, color: 'E3B04B', fit: 'shrink' });
        sl.addText(tx, { x: 5.55, y: 1.1, w: 4.15, h: 4.1, fontFace: 'Arial', fontSize: 22, color: 'FFFFFF', valign: 'top', fit: 'shrink' });
      }
      if (cap) sl.addText(cap, { x: .15, y: 5.3, w: c.k === 'place' ? 9.7 : 5.0, h: .28, fontFace: 'Arial', fontSize: 8, color: 'FFFFFF', align: c.k === 'place' ? 'right' : 'left' });
      if (auds && auds[i]) sl.addMedia({ type: 'audio', data: auds[i].replace(/^data:/, ''), extn: 'wav', x: 9.2, y: 4.85, w: .5, h: .5 });
      sl.addNotes(c.name + ': ' + c.ask + (auds && auds[i] ? ' (My voice is on this slide: click the speaker to play it.)' : ''));
    });
    var notes = (ST.teacher || []).map(function (q) { var v = (($('#' + q.id) || {}).value || '').trim(); return { q: q.label, v: v || '(not answered yet)' }; });
    if (notes.length) { var t = X.addSlide(); t.background = { color: 'F8F3E6' };
      t.addText('For my teacher · Parts A and B', { x: .5, y: .25, w: 9, h: .5, fontFace: F, fontSize: 22, bold: true, color: '15231B' });
      t.addText(notes.map(function (n) { return [{ text: n.q + '\n', options: { bold: true, fontSize: 12, color: '7A5520' } }, { text: n.v + '\n\n', options: { fontSize: 12, color: '15231B' } }]; }).reduce(function (a, b) { return a.concat(b); }, []),
        { x: .5, y: .85, w: 9, h: 4.55, fontFace: 'Arial', valign: 'top', fit: 'shrink' }); }
    var name = 'Lesson-' + (D.lesson || '').replace('.', '-') + '-' + p.k + '-my-slides.pptx';
    if (!auds || !auds.some(Boolean) || !window.JSZip) return X.writeFile({ fileName: name });
    /* pptxgenjs writes every clip as <a:videoFile>; PowerPoint expects <a:audioFile> for a sound, so fix the slides before saving */
    return X.write({ outputType: 'blob' }).then(function (blob) { return window.JSZip.loadAsync(blob); }).then(function (z) {
      var jobs = Object.keys(z.files).filter(function (f) { return /^ppt\/slides\/slide\d+\.xml$/.test(f); }).map(function (f) {
        var rel = f.replace('slides/', 'slides/_rels/') + '.rels';
        return Promise.all([z.file(f).async('string'), z.file(rel) ? z.file(rel).async('string') : '']).then(function (r) {
          var xml = r[0], ids = (r[1].match(/Id="rId\d+" Type="[^"]*relationships\/audio"/g) || []).map(function (m) { return m.match(/rId\d+/)[0]; });
          ids.forEach(function (id) { xml = xml.split('<a:videoFile r:link="' + id + '"').join('<a:audioFile r:link="' + id + '"'); }); if (ids.length) z.file(f, xml); }); });
      return Promise.all(jobs).then(function () { return z.generateAsync({ type: 'blob', mimeType: 'application/vnd.openxmlformats-officedocument.presentationml.presentation' }); });
    }).then(function (out) { var a = document.createElement('a'); a.href = URL.createObjectURL(out); a.download = name; document.body.appendChild(a); a.click(); setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 4000); });
  }

  /* the how-to video (a screen tour of this studio) in a closed drawer above it; loads only when opened */
  (function () { var d = document.getElementById('st-vid'); if (!d || !ST.video) return; var base = new URL(ST.video, document.baseURI).href;
    d.addEventListener('toggle', function () { var v = d.querySelector('video'); if (!d.open) { if (v) v.pause(); return; } if (v) return;
      d.querySelector('.wl-start-b').innerHTML = '<video controls playsinline preload="metadata" poster="' + base + '.jpg"><source src="' + base + '.mp4" type="video/mp4"><track kind="captions" srclang="en" label="English" src="' + base + '.vtt" default></video><p class="wl-start-n">Captions are on. To turn them off, press CC on the video.</p>'; }); })();
  draw(); setTimeout(refresh, 0);
  document.addEventListener('input', function (e) { if (e.target && /^in-a[12]$/.test(e.target.id) && park() && !$('#st-text:focus')) { clearTimeout(draw._t); draw._t = setTimeout(draw, 800); } });
})();
