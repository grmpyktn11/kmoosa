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

That rewrites `projects.html` and all 25 `project-*.html` pages. The order of the
list in that file is the order on the site, currently newest first — move a dict
to move a tile.

Each entry takes a slug, title, year, kind, stack, kaomoji, a short blurb for the
tile, longer notes for the detail page, and a list of `(label, url)` links.

## Demo videos

Drop `video/<slug>.mp4` (and `video/<slug>.jpg` as its poster) in and re-run
`gen_site.py`. The detail page swaps its still for the video, which autoplays
muted and looped (paused under `prefers-reduced-motion`), and the gallery tile
gets a `▶ DEMO` tag.

- `yt='<id>'` on a project embeds that YouTube video instead.
- `tall=True` gives a portrait recording a portrait frame.
- Without either, the still in `img/shots/<slug>.<ext>` is used, then the
  placeholder.

Most of the clips were recorded with Playwright against each project's own
front end, with its backend mocked where it needs keys or a database.

## Notes

Two colours throughout: `#543920` brown and `#feeac7` cream, which swap for dark
mode. The toggle remembers your choice and follows the system setting otherwise.

Everything degrades: with JavaScript off the navigation links still work, the
contact links fall back to `mailto:`, and the transitions are skipped. All motion
is disabled under `prefers-reduced-motion`.
