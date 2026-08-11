# Variant 001: Linear Monitor

## Design stance

A Linear-style **Monitor** surface — dense, glanceable, ultra-minimal dark
canvas with Inter Variable typography and a single indigo accent. Every
element earns its place; nothing decorative.

## Key choices

- **Surface**: `#08090a` page, `rgba(255,255,255,0.02)` widget surface,
  whisper-thin `rgba(255,255,255,0.08)` borders. No drop shadows except
  floating overlays.
- **Type**: Inter Variable with `font-feature-settings: 'cv01', 'ss03'`
  globally. Display numbers at 510 weight, tight negative letter-spacing.
- **Color**: Achromatic except brand indigo `#5e6ad2` (CTA / dot / focus).
- **Layout**: 12-col CSS grid, no floating overlays (Tweaks is a widget).
- **Tabular numbers** for clock + weather + KPI values via `font-variant-numeric`.
- **Mono accents** for labels (`時鐘`, `天氣 · HKO`, `ACTIVITY`) and timestamps
  via JetBrains Mono.
- **Live pulse dot** for status indicators (clock + news feed freshness).

## Trade-offs

- Strong at: power-user feel, data density, professional dashboard tone,
  zero decoration overhead.
- Weak at: warmth / consumer appeal, marketing-first impression, casual
  browsing — this is a workspace tool not a lifestyle app.

## Best for

HK dashboard for a power user who treats it as a workspace — checks
weather, scans news, manages todos. Wants information density without
visual noise. Doesn't need playful branding.

## Slop diagnostic (out of 10 tells, lower = better)

Score: **1/10**

- ❌ Tell #1 tech gradient: pass (no gradient bg)
- ❌ Tell #2 generic tech hue: pass (indigo is Linear's signature, deliberate)
- ❌ Tell #3 feature-tile grid: pass (no 3-equal cards)
- ❌ Tell #4 accent rail: pass (no left-border accent strips)
- ❌ Tell #5 unearned blur: pass (no glassmorphism)
- ❌ Tell #6 monument stat: borderline — 34° / 847 / 312 numbers are big
  but they're the actual data the user needs to scan, not decorative.
- ❌ Tell #7 icon topper: pass (icons inline with labels, no separate tile)
- ❌ Tell #8 center stack: pass (everything left-aligned, grid-driven)
- ❌ Tell #9 default type: pass (Inter chosen deliberately, with cv01/ss03)
- ❌ Tell #10 wrong surface: pass (Monitor, not Decide — no hero)

Single border-line call (#6) is justified: weather temperature IS the
information the user opens the widget to see.

## File

`index.html` — 23 KB, self-contained, demo data (no backend fetch).
