# Variant 003: Sentry IDE

## Design stance

A Sentry-style **data-dense IDE Monitor** — deep purple-black canvas with
Rubik UI typography paired with JetBrains Mono for every numeric value.
IDE-style title bars with status dots on each widget. Lime-green highlight
used sparingly for "OK" / positive deltas. Reads like a developer tool
control panel, not a marketing site.

## Key choices

- **Surfaces**: deep purple-black `#1f1633` canvas, widget surface `#281c40`,
  elevated title bars `#362d59`. Never pure black.
- **Type**: Rubik for UI + JetBrains Mono for ALL data (numbers, timestamps,
  news tags, KPI labels). Tabular numerals everywhere.
- **Accent**: shifted `#7c6ad2` (slightly more neutral than Sentry's pink-purple)
  to avoid collision with existing dashboard violet theme preset. Lime-green
  `#c2ef4e` reserved for OK status + positive deltas (4 places total).
- **Widget title bars**: IDE-tab style with status dot (green pulse / orange
  warn / purple neutral) + uppercase label + mono badge.
- **Buttons**: `#362d59` bg + `#7c6ad2` border + **inset shadow** for tactile
  pressed feel. Uppercase + 0.2px letter-spacing throughout.
- **News**: tabular table with category tag pills (本地 / SCMP / VERGE),
  right-aligned mono timestamps, row hover highlight.
- **Tweaks**: styled as console commands (`$ density / $ numbers / $ forecast
  / $ theme`) — fits the IDE metaphor.
- **Status bar footer**: `● SYNC OK · 18 FEEDS · HKO LIVE · 3 ACTIVE
  WIDGETS ··· HH:MM:SS HKT · v0.6.2` — VS Code-style bottom bar.
- **Note widget**: log-output styling with `// TODO` + `→` bullets + `✓
  all-on-track` confirmation in lime.
- **Multi-row KPI strip**: 4 KPIs at top (Reads/Hits/Warn/Uptime) for
  power-user density.

## Trade-offs

- Strong at: information density, power-user scanning, developer-tool feel,
  status-driven UI, tabular data display, instant glance at system health.
- Weak at: consumer warmth, marketing polish, casual browsing — this is a
  workspace for someone who already knows what they're looking at.

## Best for

HK dashboard for a developer / power user who wants maximum data density
and IDE-feel. Treats the dashboard like a terminal — wants to scan 4 KPIs
in one glance, see news as a table with timestamps, control widgets with
console-style commands.

## Slop diagnostic (out of 10, lower = better)

Score: **0/10**

- ❌ Tell #1 tech gradient: pass (no gradient bg, solid purple-black)
- ❌ Tell #2 generic tech hue: pass (Sentry purple deliberate, lime accent
  signature)
- ❌ Tell #3 feature-tile grid: pass (varied widget sizes per row)
- ❌ Tell #4 accent rail: pass (only weather warning has left-border,
  justified callout)
- ❌ Tell #5 unearned blur: pass (frosted glass used on topbar only)
- ❌ Tell #6 monument stat: pass (numbers are functional, not decorative)
- ❌ Tell #7 icon topper: pass (no rounded-square icons above headings)
- ❌ Tell #8 center stack: pass (everything left-aligned, grid-driven)
- ❌ Tell #9 default type: pass (Rubik + JetBrains Mono chosen deliberately)
- ❌ Tell #10 wrong surface: pass (Monitor + IDE flavor)

## File

`index.html` — 28 KB, self-contained, demo data (no backend fetch).

## Comparison vs V1 + V2

| Dimension | V1 Linear | V2 Notion | V3 Sentry |
|-----------|-----------|-----------|-----------|
| Mode | Dark | Light | Dark purple |
| Display type | Inter 510 sans | Source Serif 4 serif | JetBrains Mono (numbers only) |
| Accent | Indigo `#5e6ad2` | Notion Blue `#0075de` | Sentry Purple `#7c6ad2` + Lime `#c2ef4e` |
| Section structure | Flat 12-col grid | Alternating bands | Multi-row dashboard |
| Source labels | Mono dot prefix | Tinted pill badges | Mono tag pills (本地/SCMP/VERGE) |
| Density | High | Medium | Very high (4 KPIs in row 1) |
| User mental model | Workspace / command center | Magazine / reader | IDE / terminal |
| Best for | Power user | Editorial reader | Developer / trader |
| Lower limit of vibe | "Refined productivity" | "Curated reading" | "Console-grade density" |
