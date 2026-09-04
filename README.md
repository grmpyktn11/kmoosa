# kmoosa

Personal site. Static HTML, no build step, no dependencies — open `index.html`
and it works.

Live at <https://grmpyktn11.github.io/kmoosa/>

## Pages

| | |
|---|---|
| `index.html` | Homepage. Click the cat and the navigation unfolds. |
| `projects.html` | Gallery of every project. |
| `project-*.html` | One page per project — generated, see below. |
| `resume.html` | Full resume, with print styles and a PDF link. |
| `about.html` | Placeholder. |

## Shared files

| | |
|---|---|
| `site.css` | Everything except the homepage, which carries its own hero layout. |
| `site.js` | Header cat's eye tracking, light/dark toggle. |
| `transition.js` | The paw swipe between the gallery and a project page. |
| `contact.js` | The contact popup. Self-contained — injects its own styles. |

## Editing projects

Project content lives in one place: **`tools/projects_data.py`**.

```bash
python tools/gen_site.py
```

That rewrites `projects.html` and all 22 `project-*.html` pages. The order of the
list in that file is the order on the site, currently newest first — move a dict
to move a tile.

Each entry takes a slug, title, year, kind, stack, kaomoji, a short blurb for the
tile, longer notes for the detail page, and a list of `(label, url)` links.

## Adding a video to a project page

Every detail page has the markup commented out already:

```html
<video src="video/<slug>.mp4" poster="video/<slug>.jpg"
       controls muted loop playsinline preload="metadata"></video>
```

Uncomment it, drop the file in `video/`, and delete the `.no-video` block above
it. Do it in `tools/gen_site.py` if you want it on every page.

## Notes

Two colours throughout: `#543920` brown and `#feeac7` cream, which swap for dark
mode. The toggle remembers your choice and follows the system setting otherwise.

Everything degrades: with JavaScript off the navigation links still work, the
contact links fall back to `mailto:`, and the transitions are skipped. All motion
is disabled under `prefers-reduced-motion`.
