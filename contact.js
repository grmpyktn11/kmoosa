/* kmoosa - the contact popup.
   Self-contained: injects its own styles and dialog, then takes over every
   CONTACT link on the page. Native <dialog>, so Esc, the focus trap and the
   backdrop come from the browser. With JS off the links stay plain mailto. */

(function () {
  var EMAIL = 'Khalidmoosa749@gmail.com';

  var ROWS = [
    ['EMAIL',    EMAIL,                'mailto:' + EMAIL],
    ['GITHUB',   'grmpyktn11',         'https://github.com/grmpyktn11'],
    ['LINKEDIN', 'khalid-moosa',       'https://www.linkedin.com/in/khalid-moosa-956830299/'],
    ['ITCH.IO',  'grumpykitten1',      'https://grumpykitten1.itch.io/'],
    ['BASED IN', 'Chantilly, Virginia', null]
  ];

  var css = document.createElement('style');
  css.textContent = [
    '#contact{border:1px dashed var(--ink); background:var(--bg); color:var(--ink);',
    '  padding:0; width:min(30rem,92vw); max-width:none;}',
    '#contact::backdrop{background:color-mix(in srgb, var(--ink) 62%, transparent);',
    '  backdrop-filter:blur(2px);}',
    '#contact .cbar{display:flex; align-items:center; justify-content:space-between;',
    '  gap:1rem; padding:.75rem .5rem .75rem 1.1rem; border-bottom:1px dashed var(--ink);',
    '  font-family:"Silkscreen",monospace; font-size:.78rem; letter-spacing:.16em;}',
    '#contact .cx{font:inherit; color:var(--ink); background:none; border:0;',
    '  padding:.45rem .8rem; cursor:pointer; line-height:1;}',
    '#contact .cx:hover{background:var(--ink); color:var(--bg);}',
    '#contact .cbody{padding:1.1rem 1.1rem 1.3rem;}',
    '#contact dl{margin:0; display:grid; grid-template-columns:auto 1fr; gap:.1rem .9rem;}',
    '#contact dt{font-family:"Silkscreen",monospace; font-size:.62rem; letter-spacing:.1em;',
    '  opacity:.75; padding:.5rem 0; white-space:nowrap;}',
    '#contact dd{margin:0; padding:.45rem 0; font-size:.98rem; overflow-wrap:anywhere;}',
    '#contact dd a{text-decoration:none; border-bottom:1px dashed var(--ink);}',
    '#contact dd a:hover{background:var(--ink); color:var(--bg); border-color:transparent;}',
    '#contact .ccopy{margin-top:1.1rem; display:flex; align-items:center; gap:.8rem;}',
    '#contact .ccopy button{font-family:"Silkscreen",monospace; font-size:.7rem;',
    '  letter-spacing:.12em; color:var(--ink); background:var(--bg);',
    '  border:1px dashed var(--ink); padding:.7rem 1rem; cursor:pointer;}',
    '#contact .ccopy button:hover{background:var(--ink); color:var(--bg);}',
    '#contact .said{font-family:"Silkscreen",monospace; font-size:.62rem;',
    '  letter-spacing:.1em; opacity:0; transition:opacity 140ms linear;}',
    '#contact .said.on{opacity:.85;}',
    '@media (prefers-reduced-motion:reduce){#contact .said{transition:none}}'
  ].join('\n');
  document.head.appendChild(css);

  var dlg = document.createElement('dialog');
  dlg.id = 'contact';
  dlg.setAttribute('aria-labelledby', 'contact-t');

  dlg.innerHTML =
    '<div class="cbar"><span id="contact-t">CONTACT</span>' +
    '<button class="cx" type="button" aria-label="Close">&#10005;</button></div>' +
    '<div class="cbody"><dl>' +
    ROWS.map(function (r) {
      var val = r[2]
        ? '<a href="' + r[2] + '">' + r[1] + '</a>'
        : r[1];
      return '<dt>' + r[0] + '</dt><dd>' + val + '</dd>';
    }).join('') +
    '</dl><div class="ccopy">' +
    '<button class="ccopy-btn" type="button">COPY EMAIL</button>' +
    '<span class="said" role="status" aria-live="polite"></span>' +
    '</div></div>';

  document.body.appendChild(dlg);

  function open() {
    if (typeof dlg.showModal === 'function') dlg.showModal();
    else dlg.setAttribute('open', '');
  }
  function close() {
    if (typeof dlg.close === 'function') dlg.close();
    else dlg.removeAttribute('open');
  }

  dlg.querySelector('.cx').addEventListener('click', close);
  /* click the backdrop (i.e. outside the panel) to dismiss */
  dlg.addEventListener('click', function (e) {
    if (e.target === dlg) close();
  });

  var said = dlg.querySelector('.said');
  dlg.querySelector('.ccopy-btn').addEventListener('click', function () {
    function done(ok) {
      said.textContent = ok ? 'COPIED' : EMAIL;
      said.classList.add('on');
      setTimeout(function () { said.classList.remove('on'); }, 2200);
    }
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(EMAIL).then(function () { done(true); },
                                                function () { done(false); });
    } else {
      done(false);   /* no clipboard: show the address so it can be selected */
    }
  });

  /* take over anything that says CONTACT, plus anything opted in explicitly */
  function wire() {
    [].slice.call(document.querySelectorAll('a[href^="mailto:"], [data-contact]'))
      .forEach(function (a) {
        if (a.dataset.contactWired) return;
        var label = (a.textContent || '').trim().toUpperCase();
        if (!a.hasAttribute('data-contact') && label !== 'CONTACT') return;
        a.dataset.contactWired = '1';
        a.addEventListener('click', function (e) {
          if (e.metaKey || e.ctrlKey || e.shiftKey || e.altKey || e.button !== 0) return;
          e.preventDefault();
          open();
        });
      });
  }
  wire();
})();
