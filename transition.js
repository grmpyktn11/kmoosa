/* kmoosa - the cat transition.
   Click a project: a paw swipes up from the bottom of the screen, scattering the
   other tiles, the chosen one is pushed to the top, then it grows into the page.

   Plain navigation still works with JS off, on modified clicks, and under
   prefers-reduced-motion. */

(function () {
  var reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* ---------- arriving: grow the page in ---------- */
  try {
    if (sessionStorage.getItem('kmoosa-grow') === '1') {
      sessionStorage.removeItem('kmoosa-grow');
      if (!reduce) document.documentElement.classList.add('growing');
    }
  } catch (e) {}

  var grid = document.querySelector('.grid');
  if (!grid || reduce) return;

  var PAW = [
    '⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣤⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀',
    '⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⠟⠛⠛⠛⠿⣿⣿⣿⣿⣶⣤⡀⠀⠀⠀⠀⠀',
    '⠀⠀⠀⠀⠀⣠⣴⣿⡟⠁⢀⣤⣀⠀⠀⠀⠀⠀⠀⠉⠻⣿⣦⠀⠀⠀⠀',
    '⠀⠀⠀⠀⣾⡿⠿⠛⠁⣰⣿⣿⣿⡆⠀⠀⣴⣶⣶⠄⠀⢻⣿⡄⠀⠀⠀',
    '⠀⠀⣾⡿⠁⠀⠀⠀⠀⠻⣿⣿⣿⠃⠀⣼⣿⣿⣿⠀⠀⠀⢿⣷⣄⠀⠀',
    '⠀⣾⣿⠁⠀⣤⣶⡄⠀⠀⠈⠉⠁⠀⠀⠈⠛⠊⠁⠀⠀⠀⠀⠙⢿⣷⠀',
    '⠀⣿⡇⠀⢸⣿⣿⡿⡆⠀⠀⣴⣶⣶⣴⣶⣄⠀⠀⢠⣶⣿⣦⠀⠀⣿⡇',
    '⠀⣿⡇⠀⠀⠛⠙⠉⠀⣰⣿⣿⣿⣿⣿⣿⣿⣇⠀⣿⣿⣿⣿⠀⠀⣿⡇',
    '⠀⣿⣇⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣷⣿⣷⡀⠀⠉⠉⠀⠀⣸⣿⠇',
    '⠀⣿⣿⠀⠀⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⣻⡟⠘',
    '⠀⢹⣿⠀⠀⠀⠀⠀⠉⠛⠉⠁⠉⠁⠙⠻⠿⠟⠀⠀⠀⠀⠀⣾⣿⠁⠀',
    '⠀⠀⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀',
    '⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀',
    '⠀⠀⣻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀',
    '⠀⠀⢸⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⡇⠀⠀'
  ].join('\n');

  var tiles = [].slice.call(grid.querySelectorAll('.tile'));

  grid.addEventListener('click', function (e) {
    if (e.button !== 0 || e.metaKey || e.ctrlKey || e.shiftKey || e.altKey) return;
    var tile = e.target.closest('.tile');
    if (!tile || !tile.getAttribute('href')) return;
    e.preventDefault();
    leave(tile, tile.getAttribute('href'));
  });

  function leave(tile, href) {
    document.body.classList.add('is-leaving');

    /* the paw, swiping up from the bottom of the screen */
    /* Braille is not monospaced in the fonts that actually have it - the
       advances vary by ~5px at 48px, which shears the art. So every cell gets
       an explicit width instead of trusting the font's metrics. */
    var paw = document.createElement('div');
    paw.className = 'paw';
    paw.setAttribute('aria-hidden', 'true');
    paw.innerHTML = PAW.split('\n').map(function (line) {
      return '<span class="pr">' +
        [].map.call(line, function (ch) { return '<i>' + ch + '</i>'; }).join('') +
        '</span>';
    }).join('');
    document.body.appendChild(paw);

    /* everything else scatters up and outward, away from where the paw enters,
       nearest tiles first */
    var mid = innerWidth / 2;
    tiles.forEach(function (t) {
      if (t === tile) return;
      var r = t.getBoundingClientRect();
      var dir = ((r.left + r.width / 2) - mid) / mid;          /* -1 .. 1 */
      t.style.setProperty('--tx', (dir * 78).toFixed(1) + 'vw');
      t.style.setProperty('--ty', (-72 - Math.random() * 16).toFixed(1) + 'vh');
      t.style.setProperty('--rot', (dir * 26).toFixed(1) + 'deg');
      /* lower tiles are hit first, since the paw comes from below */
      var fromBottom = Math.max(0, innerHeight - r.bottom);
      t.style.transitionDelay = Math.round(100 + (fromBottom / innerHeight) * 220) + 'ms';
      t.classList.add('swept');
    });
    [].slice.call(document.querySelectorAll('.top, main > h1, main > .lede, .foot'))
      .forEach(function (el, i) {
        el.style.transitionDelay = (140 + i * 40) + 'ms';
        el.classList.add('swept-soft');
      });

    /* The chosen tile: straight up to the top, staying in its own column, then
       it grows from there. Scaling about its own centre means a tile at either
       edge still covers the screen, so nothing has to slide sideways. */
    var r0 = tile.getBoundingClientRect();
    var cx = r0.left + r0.width / 2;
    var cover = (2 * Math.max(cx, innerWidth - cx) / r0.width) * 1.06;
    var lift = 40 - r0.top;          /* up to just below the top edge */
    var flush = -r0.top;             /* then flush, as it fills */

    tile.classList.add('chosen');
    tile.style.transformOrigin = '50% 0';

    /* linear overall, with the easing on each keyframe - otherwise one curve is
       stretched across all three phases and the tile grows before it has moved */
    tile.animate([
      { transform: 'translateY(0px) scale(1)', offset: 0, easing: 'linear' },
      { transform: 'translateY(0px) scale(1)', offset: 0.28,
        easing: 'cubic-bezier(.34,.9,.32,1)' },
      { transform: 'translateY(' + lift + 'px) scale(1)', offset: 0.62,
        easing: 'cubic-bezier(.5,0,.35,1)' },
      { transform: 'translateY(' + flush + 'px) scale(' + cover.toFixed(3) + ')',
        offset: 1 }
    ], { duration: 900, easing: 'linear', fill: 'forwards' });

    [].slice.call(tile.children).forEach(function (c) {
      c.animate([{ opacity: 1 }, { opacity: 1, offset: 0.55 }, { opacity: 0, offset: 0.78 },
                 { opacity: 0 }],
                { duration: 900, fill: 'forwards' });
    });

    setTimeout(function () {
      try { sessionStorage.setItem('kmoosa-grow', '1'); } catch (err) {}
      location.href = href;
    }, 820);
  }
})();
