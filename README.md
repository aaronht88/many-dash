# many-dash

A hackable Hong Kong dashboard prototype — 12-column drag-resize grid with
GridStack v11, HKO weather, RSS news, clock, sticky notes.

Single-file HTML + a Python RSS proxy. Open `index.html` directly in a
browser, or serve it locally.

## Preview

![screenshot](https://materials-percent-malpractice-addition.trycloudflare.com/index.html)

(The Cloudflare quick-tunnel URL expires when the relay is closed; the file
itself is the source of truth.)

## Run locally

```bash
# Option 1: Just open it
xdg-open index.html     # Linux
open index.html         # macOS

# Option 2: Local server (recommended for RSS proxy)
python3 -m http.server 8765
# Visit http://127.0.0.1:8765/index.html
```

The Python RSS proxy (`rss_proxy.py`) wraps feeds with a 5-min in-memory
cache and browser CORS headers, so the demo works on `file://` or HTTP.

```bash
# RSS proxy in another terminal
python3 rss_proxy.py 8766
# Visits http://127.0.0.1:8766/api/rss?url=<feed-url>
```

## Widgets

| Widget | Data source |
|---|---|
| Weather | HKO public API (Hong Kong Observatory) |
| News | RSS aggregator via `rss_proxy.py` |
| Clock | Live client-side |
| Notes | LocalStorage |

Drag widgets by their header, resize from the bottom-right handle. Configure
each widget with the ⚙ button. Multi-page tabs at the top, persistent in
localStorage.

## Tech stack

- GridStack v11 (drag-resize grid)
- Vanilla JS (no React/Vue)
- Python stdlib RSS proxy (urllib)
- HKO public API

## Layout

12-column grid, 60px cell height, float + animate. Handheld to desktop
without media queries.

## License

Personal prototype, public for sharing.
