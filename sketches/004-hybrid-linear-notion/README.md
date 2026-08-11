# Variant 004: Hybrid Linear × Notion

## Design stance

A hybrid **Editorial Monitor** combining Linear's precision and ultra-minimal
dark canvas with Notion's editorial patterns — serif display numbers for
clock + temperature + KPIs, pill badges for source labels, soft 4-layer
shadows, alternating barely-darker section bands. The dark base is
suitable for long-viewing dashboards while the serif weight + pills give
content an editorial warmth that pure Linear lacks.

## Pairing rationale

| Layer | Source | Why |
|-------|--------|-----|
| Canvas | V1 Linear `#08090a` | Dashboard ambient — dark protects eyes during long viewing |
| Grid | V1 Linear 12-col flat | Familiar structure, no Section alt bands breaking widget flow |
| Display numbers | **V2 Notion Source Serif 4** | Serif weight on dark canvas = editorial contrast that Inter 510 can't match |
| Section titles | **V2 Notion Source Serif 4** | Grounding each band with editorial structure |
| Source labels | **V2 Notion pill badges** | Replace V1 monospace dots for better category scanning |
| Warnings | **V2 Notion left-border block** | V1 flat tag → V2 callout pattern (orange tint) |
| Borders | V1 Linear whisper-thin | `rgba(255,255,255,0.08)` — discipline preserved |
| Shadows | **V2 Notion 4-layer soft** | On dark surface, gives widget cards subtle elevation |
| Section bands | **V2 Notion alt** | Barely-darker (`#0d0e10`) alternation — visible but subtle |
| Brand accent | V1 Linear indigo `#5e6ad2` | Preserved; complements serif on dark |
| Live indicator | V1 Linear pulse dot | Preserved on `LIVE` pill |
| Topbar | V1 Linear | Sticky dark, brand mark, search, icon-btn, primary CTA |

## Key choices

- **Surfaces**: `#08090a` page canvas, `#0d0e10` barely-darker alt bands,
  widget surface `rgba(255,255,255,0.02)` with whisper-thin border.
- **Type**: Source Serif 4 for display + section titles, Inter for UI,
  JetBrains Mono for timestamps + forecast numbers.
- **Pill badges**: 5 distinct tints per category (本地 amber / SCMP indigo /
  tech violet / intl indigo / etc), uppercase 10px with 0.06em letter-spacing.
- **Weather warning**: orange-tinted left-border block with `#dd5b00` border
  + `rgba(221, 91, 0, 0.10)` bg — Notion callout pattern adapted for dark.
- **Activity KPIs**: Source Serif 4 metric values (847/312/7) with mono
  delta arrows — combines V2 serif stat + V3 mono data hint.
- **Forecast**: 7-column grid with mono numbers (35°/29°), minimal padding,
  linear feel preserved.

## Trade-offs

- Strong at: editorial gravitas on dark canvas, improved category scanning
  via pills, subtle section rhythm without breaking widget flow, suitable
  for both work and reading.
- Weak at: pure utility / no-frills vibe (V1 wins), warm-light reading
  feel (V2 wins), terminal-grade density (V3 wins) — by design, hybrid
  trades purity for breadth.

## Best for

HK dashboard for a thoughtful power user — wants Linear's precision but
also wants news + reading list to feel curated. Editorial warmth on dark
canvas = unique balance.

## Slop diagnostic (out of 10, lower = better)

Score: **0/10**

- ❌ Tell #1 tech gradient: pass
- ❌ Tell #2 generic tech hue: pass (Linear indigo + Notion serif both deliberate)
- ❌ Tell #3 feature-tile grid: pass (varied widget sizes)
- ❌ Tell #4 accent rail: pass (weather warning justified as callout)
- ❌ Tell #5 unearned blur: pass
- ❌ Tell #6 monument stat: pass (numbers are data)
- ❌ Tell #7 icon topper: pass (inline icons)
- ❌ Tell #8 center stack: pass
- ❌ Tell #9 default type: pass (Source Serif 4 + Inter + JetBrains Mono all chosen)
- ❌ Tell #10 wrong surface: pass (Monitor + editorial)

## File

`index.html` — 27 KB, self-contained, demo data.

## Comparison vs all 3 originals

| Dimension | V1 Linear | V2 Notion | V3 Sentry | V4 Hybrid |
|-----------|-----------|-----------|-----------|-----------|
| Canvas | Dark `#08090a` | Light `#ffffff` | Dark `#1f1633` | Dark `#08090a` |
| Display | Inter 510 sans | Source Serif 4 serif | JetBrains Mono (data) | **Source Serif 4 serif** |
| Accent | Indigo `#5e6ad2` | Blue `#0075de` | Purple + Lime | **Indigo `#5e6ad2`** |
| Sections | Flat 12-col grid | Alternating bands | Multi-row dashboard | Alternating bands (subtle) |
| Source labels | Mono dot prefix | Tinted pill badges | Mono tag pills | **Tinted pill badges** |
| Warning | Flat tag | Left-border block | Left-border block | **Left-border block** |
| Borders | Whisper-thin semi-transparent | Whisper-thin dark | Purple-tinted dark | **Whisper-thin semi-transparent** |
| Shadows | None | 4-layer soft | Inset + ambient | **4-layer soft (on dark)** |
| Density | High | Medium | Very high | **High** |
| User mental model | Workspace | Magazine | IDE | **Editorial workspace** |
| Best for | Power user | Editorial reader | Developer / trader | **Editorial power user** |
