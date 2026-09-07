# -*- coding: utf-8 -*-
"""Builds the project gallery and one detail page per project.

All the content lives in projects_data.py - edit that, re-run this, and both the
gallery and every detail page regenerate together.
"""
import io, os, sys, html, struct
sys.stdout.reconfigure(encoding='utf-8')

# repo root, whichever directory this is run from
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
OUT = os.path.dirname(HERE)

from projects_data import PROJECTS

# video/<slug>.mp4 wins if it exists, with video/<slug>.jpg as its poster.
# Failing that a still from img/shots/<slug>.<ext> stands in, and failing that
# the placeholder. All three key off the same slug, so cutting a demo for a
# project is a matter of dropping two files in video/ and re-running this.
SHOT_EXTS = ('png', 'gif', 'jpg')


def media(slug, title):
    """The frame contents for a project. Portrait media is contained rather than
    cropped - the frame is 16:9 and a phone recording would lose most of itself
    to a cover crop."""
    vid = 'video/%s.mp4' % slug
    if os.path.exists(os.path.join(OUT, vid)):
        poster = 'video/%s.jpg' % slug
        has_poster = os.path.exists(os.path.join(OUT, poster))
        # Orientation comes from the poster, which is a frame of the video and
        # so shares its aspect ratio. Without one, assume landscape.
        cls = ' class="tall"' if has_poster and is_portrait(
            os.path.join(OUT, poster)) else ''
        return ('<video src="%s"%s controls muted loop playsinline preload="none"'
                ' aria-label="A demo of %s"%s></video>'
                % (vid, ' poster="%s"' % poster if has_poster else '',
                   html.escape(title, quote=True), cls))
    for ext in SHOT_EXTS:
        rel = 'img/shots/%s.%s' % (slug, ext)
        if not os.path.exists(os.path.join(OUT, rel)):
            continue
        cls = ' class="tall"' if is_portrait(os.path.join(OUT, rel)) else ''
        return ('<img src="%s" alt="A screenshot of %s" loading="lazy" decoding="async"%s>'
                % (rel, html.escape(title, quote=True), cls))
    return '<div class="no-video">VIDEO NOT AVAILABLE :c</div>'


def is_portrait(path):
    """Taller than wide. Read from the file header - no pillow dependency, and
    these are the only formats in img/shots and video."""
    try:
        with io.open(path, 'rb') as f:
            head = f.read(4)
            if head[1:4] == b'PNG':
                rest = f.read(20)
                w, h = struct.unpack('>II', rest[12:20])
                return h > w
            if head[:3] == b'GIF':
                rest = f.read(6)
                w, h = struct.unpack('<HH', rest[2:6])
                return h > w
            if head[:2] != b'\xff\xd8':
                return False
            # jpeg: walk the segment chain to the frame header, which is the
            # only place the dimensions are written
            f.seek(2)
            while True:
                marker = f.read(2)
                if len(marker) < 2 or marker[0] != 0xFF:
                    return False
                if 0xC0 <= marker[1] <= 0xCF and marker[1] not in (0xC4, 0xC8, 0xCC):
                    f.read(3)                     # length, then sample precision
                    h, w = struct.unpack('>HH', f.read(4))
                    return h > w
                size = struct.unpack('>H', f.read(2))[0]
                f.seek(size - 2, 1)
    except Exception:
        return False

HEAD = '''<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="theme-color" content="#feeac7" id="tc">
<title>{title} — Khalid Moosa</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Pixelify+Sans:wght@400;600&family=Silkscreen&family=VT323&display=swap" rel="stylesheet">
<link rel="stylesheet" href="site.css">
</head>
<body>

<a class="skip" href="#main">Skip to content</a>
<button class="mode" id="mode" type="button" aria-pressed="false" aria-label="Switch to dark mode">MODE</button>

<div class="wrap">

  <header class="top">
    <a class="home" href="index.html" aria-label="Home">=^ <span class="eye" aria-hidden="true">&#8226;</span>w<span class="eye" aria-hidden="true">&#8226;</span> ^=</a>
    <nav aria-label="Main">
      <a href="resume.html">RESUME</a>
      <a href="projects.html" aria-current="page">PROJECTS</a>
      <a href="about.html">ABOUT</a>
      <a href="https://github.com/grmpyktn11">GITHUB</a>
      <a href="mailto:Khalidmoosa749@gmail.com">CONTACT</a>
    </nav>
  </header>
'''

FOOT = '''
</div>

<script src="site.js"></script>
<script src="transition.js"></script>
<script src="contact.js"></script>
</body>
</html>
'''


def detail(i, p):
    prev = PROJECTS[i - 1]
    nxt = PROJECTS[(i + 1) % len(PROJECTS)]
    rant = '\n'.join('      <p>%s</p>' % para for para in p['rant'].split('\n\n'))
    links = '\n'.join(
        '        <a class="btn" href="%s">%s &rarr;</a>' % (u, l) for l, u in p['links'])
    if not links:
        links = '        <span class="btn is-off">INTERNAL &mdash; NO PUBLIC LINK</span>'
    desc = html.escape(html.unescape(p['blurb']), quote=True)

    return HEAD.format(title=p['title'].replace('&rsquo;', "'"), desc=desc) + '''
  <main id="main">

    <a class="back" href="projects.html">&larr; ALL PROJECTS</a>

    <div class="hero" style="view-transition-name:card-{slug}">
      <div class="ico-big" aria-hidden="true">{kao}</div>
      <h1>{title}</h1>
      <div class="meta">{year} &middot; {kind}</div>
      <div class="stack">{stack}</div>
    </div>

    <!-- Do not hand-edit this block - media() in tools/gen_site.py picks the
         demo video if video/{slug}.mp4 exists, else a still, else a placeholder.
         The poster ships next to the video rather than reusing the still,
         because the two need not share an aspect ratio. -->
    <div class="frame">
      {media}
    </div>

    <section class="rant">
      <h2>NOTES</h2>
{rant}
    </section>

    <div class="btns">
{links}
    </div>

    <nav class="pager" aria-label="Other projects">
      <a href="project-{pslug}.html"><span>&larr; PREV</span>{ptitle}</a>
      <a href="project-{nslug}.html" class="next"><span>NEXT &rarr;</span>{ntitle}</a>
    </nav>

  </main>

  <footer class="foot">
    <a href="projects.html">ALL PROJECTS</a> &middot;
    <a href="index.html">HOME</a> &middot;
    <a href="mailto:Khalidmoosa749@gmail.com">KHALIDMOOSA749@GMAIL.COM</a>
  </footer>
'''.format(slug=p['slug'], media=media(p['slug'], p['title']), kao=p['kao'], title=p['title'], year=p['year'],
           kind=p['kind'], stack=p['stack'], rant=rant, links=links,
           pslug=prev['slug'], ptitle=prev['title'],
           nslug=nxt['slug'], ntitle=nxt['title']) + FOOT


def gallery():
    tiles = []
    for p in PROJECTS:
        tiles.append('''      <a class="tile" href="project-{slug}.html" style="view-transition-name:card-{slug}">
        <div class="ico" aria-hidden="true">{kao}</div>
        <h3>{title}</h3>
        <div class="yr">{year} &middot; {kind}</div>
        <div class="stack">{stack}</div>
        <p>{blurb}</p>
        <div class="go">OPEN &rarr;</div>
      </a>'''.format(**p))
    return '\n\n'.join(tiles)


# ---- write the detail pages ----
for i, p in enumerate(PROJECTS):
    io.open(os.path.join(OUT, 'project-%s.html' % p['slug']), 'w',
            encoding='utf-8').write(detail(i, p))

# ---- splice the regenerated tiles into the gallery ----
gpath = os.path.join(OUT, 'projects.html')
g = io.open(gpath, encoding='utf-8').read()
start = g.index('<div class="grid">') + len('<div class="grid">')
end = g.index('    </div>\n\n  </main>')
g = g[:start] + '\n\n' + gallery() + '\n\n' + g[end:]
io.open(gpath, 'w', encoding='utf-8').write(g)

print('wrote %d detail pages + gallery' % len(PROJECTS))
