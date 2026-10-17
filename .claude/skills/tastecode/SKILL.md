---
name: tastecode
description: TasteCode Design Mode guidance (from github.com/Leonxlnx/tastecode, packages/design-agent). Use when designing or redesigning a website or landing page — layout cases for hero/nav/feature/about/stats/CTA/footer, typography pools, visible-motion rules, copywriting and review checks that keep pages from looking generic.
---

# TasteCode Design Mode

TasteCode itself is a desktop app for coding agents. This skill packages the design
rules its Design Mode agent follows. The source prompts are copied verbatim into
`references/` — read the relevant file before deciding that part of the page.

| File | What it governs |
| --- | --- |
| `references/layout-guidance.ts` (`PAGE_LAYOUT_GUIDANCE`) | Named layout cases: hero-text-1..7, hero-visual-1..7, navigation-1..6, about, feature-heading/grid/timed/spatial, how-it-works, stats, social proof, FAQ, CTA, pricing, contact, footer — plus global quality constraints |
| `references/typography.ts` | Curated Google font pools (sans / serif / display / mono) |
| `references/motion-guidance.ts` + `reveal.js` | Visible-motion contract and a reference reveal implementation |
| `references/copywriting.ts` | Copy rules (headline length, banned filler, specificity) |
| `references/content-guidance.ts` | Section count/scope for landing pages |
| `references/palette.ts`, `gradients.ts` | Palette roles and gradient usage limits |
| `references/source-quality.ts`, `review-phase.ts` | Checks used to reject sloppy output |

## Workflow

1. Brief: product, audience, the one action the visitor should take.
2. Pick a navigation case and, for each section, a layout family + case ID. Adjacent
   sections must not repeat the same composition.
3. Resolve type, colour roles, radii, spacing and motion from the brand — the layout
   case is only part of the result.
4. Build. Wire real motion: hero entrance on load, distinct reveals for 2+ later
   sections, interaction feedback. Reveals run once, CSS defaults to the visible state,
   honour `prefers-reduced-motion`.
5. Review in a browser at desktop and mobile width against `review-phase.ts` checks.

## Hard rules (summarised from the references)

- Headings plan for one or two lines; never four.
- No eyebrows, uppercase mono micro-labels, decorative section numbers, ornamental
  hairline grids, or one-sided accent borders on cards.
- One base card language and at most one emphasised variant.
- Brand accent goes on real actions, focus/selected states and a recurring treatment —
  not sprinkled across every card in different colours.
- SVG only for icons, logos, or truthful diagrams — never as filler.
- Don't switch font families inside one line, card, or nav item.
