/* kmoosa - shared behaviour for the interior pages:
   the header cat's eyes, and the light/dark toggle. */

(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------------- the header cat ---------------- */
  var EYES = [].slice.call(document.querySelectorAll('.home .eye'));
  if (EYES.length) {
    var PUPIL = '•', SHUT = '^';
    var mx = null, my = null, blinking = false, centres = [];

    function measureEyes() {
      centres = EYES.map(function (el) {
        var r = el.getBoundingClientRect();
        return { x: r.left + r.width / 2, y: r.top + r.height / 2 };
      });
    }

    function setEyes() {
      EYES.forEach(function (el, i) {
        if (blinking) { el.textContent = SHUT; el.style.transform = ''; return; }
        var ox = 0, oy = 0;
        if (mx !== null && centres[i]) {
          var dx = mx - centres[i].x, dy = my - centres[i].y;
          var len = Math.hypot(dx, dy);
          if (len > 10) { ox = Math.round(dx / len); oy = Math.round(dy / len); }
        }
        el.textContent = PUPIL;
        el.style.transform = 'translate(' + (ox * 0.15) + 'em,' + (oy * 0.13) + 'em)';
      });
    }

    addEventListener('mousemove', function (e) {
      mx = e.clientX; my = e.clientY; setEyes();
    }, { passive: true });
    addEventListener('resize', measureEyes, { passive: true });
    addEventListener('scroll', measureEyes, { passive: true });

    function blink() {
      blinking = true; setEyes();
      setTimeout(function () { blinking = false; setEyes(); }, 130);
      setTimeout(blink, 3200 + Math.random() * 4200);
    }
    measureEyes(); setEyes();
    if (!reduce) setTimeout(blink, 2600);
  }

  /* ---------------- light / dark ---------------- */
  var root = document.documentElement;
  try {
    var saved = localStorage.getItem('kmoosa-theme');
    if (saved) root.dataset.theme = saved;
    else if (matchMedia('(prefers-color-scheme: dark)').matches) root.dataset.theme = 'dark';
  } catch (e) {}

  var btn = document.getElementById('mode');
  function syncMode() {
    if (!btn) return;
    var dark = root.dataset.theme === 'dark';
    btn.setAttribute('aria-pressed', String(dark));
    btn.setAttribute('aria-label', dark ? 'Switch to light mode' : 'Switch to dark mode');
    var tc = document.getElementById('tc');
    if (tc) tc.setAttribute('content', dark ? '#543920' : '#feeac7');
  }
  if (btn) {
    btn.addEventListener('click', function () {
      root.dataset.theme = root.dataset.theme === 'dark' ? 'light' : 'dark';
      try { localStorage.setItem('kmoosa-theme', root.dataset.theme); } catch (err) {}
      syncMode();
    });
  }
  syncMode();
})();
