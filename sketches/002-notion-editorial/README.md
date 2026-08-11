# Variant 002: Notion Editorial

## Design stance

A Notion-style **Editorial Monitor** — warm paper aesthetic with serif display
typography, alternating white / warm-cream sections, and the signature Notion
pill badges with tinted backgrounds. Single Notion Blue accent reserved for
CTAs and live status. Reads more like a magazine than a control panel.

## Key choices

- **Surfaces**: alternating `#ffffff` / `#f6f5f4` section bands with
  generous vertical rhythm (56px padding).
- **Type**: Source Serif 4 for display numbers and section headings (with
  negative letter-spacing at scale), Inter for body and UI.
- **Color**: warm near-black `rgba(0,0,0,0.95)` text on white/cream, single
  Notion Blue `#0075de` accent for primary actions and live indicators.
- **Pill badges**: tinted backgrounds per category (本地 / SCMP / Verge etc)
  — Notion's signature pattern replacing monospace source labels.
- **Weather warning**: left-border accent block with warm tint (replaces
  flat tag from V1).
- **Section headings**: serif `Today` / `News & Activity` / `Design preferences`
  ground each band with editorial structure.
- **Borders**: whisper-thin `1px solid rgba(0,0,0,0.1)` everywhere.
- **Shadows**: 4-layer Notion card stack (max 0.04 opacity).

## Trade-offs

- Strong at: editorial feel, generous breathing room, paper-like warmth,
  pill badge pattern for source categorization.
- Weak at: dense data scanning (more whitespace = less density), dark mode
  ambient vibe (light theme by default), power-user "I want everything
  visible now" feel.

## Best for

HK dashboard for a thoughtful reader — wants news to feel like a curated
magazine, weather and clock to feel like quality paper. Less appropriate
for a trader-style "show me everything" power user.

## Slop diagnostic (out of 10, lower = better)

Score: **0/10**

- ❌ Tell #1 tech gradient: pass
- ❌ Tell #2 generic tech hue: pass (Notion Blue is deliberate, not generic)
- ❌ Tell #3 feature-tile grid: pass (varied widget sizes, no equal-card grid)
- ❌ Tell #4 accent rail: borderline — weather warning has left-border
  accent block. Justified: it IS a callout block in Notion's own pattern.
- ❌ Tell #5 unearned blur: pass
- ❌ Tell #6 monument stat: pass (numbers are data, not decoration)
- ❌ Tell #7 icon topper: pass (inline icons, no separate tiles)
- ❌ Tell #8 center stack: pass (left-aligned, grid-driven)
- ❌ Tell #9 default type: pass (Source Serif 4 + Inter chosen deliberately)
- ❌ Tell #10 wrong surface: pass (Monitor + editorial flavor)

## File

`index.html` — 27 KB, self-contained, demo data (no backend fetch).

## Comparison vs V1 (Linear Monitor)

| Dimension | V1 Linear | V2 Notion |
|-----------|-----------|-----------|
| Mode | Dark | Light |
| Display type | Inter 510 (sans) | Source Serif 4 (serif) |
| Accent | Indigo `#5e6ad2` | Notion Blue `#0075de` |
| Section structure | Flat 12-col grid | Alternating bands |
| Source labels | Mono dot prefix | Tinted pill badges |
| Warning | Flat tag | Left-border accent block |
| Density | High | Medium |
| Best for | Power user | Editorial reader |
