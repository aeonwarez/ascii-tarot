# Fable Prompt Template — ASCII Tarot (Thoth deck)

The locked, card-agnostic block. Every per-card prompt inlines a compact recap of
this and then adds its own SUBJECT + ranked DIRECTIVES. Update here when an
invariant changes; do not re-derive per card.

## Role
You render monospace ASCII/ANSI art of a Thoth Tarot card. The job is not a diagram
of the symbols but a reproduction of the *composition and energy* of Lady Frieda
Harris's painting in text. Fidelity to iconography AND to the feel of the image both
matter. Fixed-width grid, Courier New assumed.

## Invariants (do not violate)

- **Canvas (LOCKED):** art 47 cols × 32 rows, framed 51 × 39. Rendered aspect 0.64,
  the Thoth card ratio (70×110mm). Preserve EXACT leading whitespace on every line;
  never let it collapse.
- **Center on the axis (col 23).** The vertical axis of the 47-wide art is column 23
  (0-indexed). Every element on the central figure must sit so its VISUAL center is
  col 23 — not its left edge. The recurring bug: hand-placed sprites land 2-3 cols
  left because the coder set the start col to the axis instead of `axis - width//2`.
  Prefer the mirror helpers (`PM`/`PMB` about `AXIS = 23.0`) for anything bilaterally
  symmetric; they cannot drift. For asymmetric sprites, place at `23 - len(s)//2` and
  confirm with `--axis` in the render (below). A card whose head is centered but whose
  body leans is the classic tell.
- **Cell aspect 1:2.** Monospace cells are taller than wide. Draw circles, spheres,
  and curves ~2:1 WIDER than tall or they render as squashed eggs. Bake it into the
  geometry.
- **Font pin: Courier New.** Extended alphabet allowed: basic printable
  `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus `´ ‾ ¡ ·` and
  line-glyphs `o O v V T L 7 U c C x X`. (Share Tech Mono breaks the overline `‾`.)
- **Masses are dithered, never outlined.** Any solid body (sphere, globe, disk) gets
  a density ramp `. : · ' ° :` for volume, NOT an open circle. Light it directionally
  (dense one edge, open the opposite) so it reads round.
- **Occlusion.** The foreground figure is drawn ON TOP. Break/erase background edges
  where the figure overlaps. Never let a background line slice through the figure.
- **Full-bleed density.** Push composition to the border. No sparse figure floating in
  empty frame; the paintings are edge to edge.
- **Frame + title band.** Keep the outer double-rule border. Rendered by
  `tools/frame.py` (`-s majors|wands|cups|swords|disks` picks corner sigils;
  `-n <NUMERAL>` sets the top plaque). Layout mirrors Harris:
  top rule: numeral plaque set into the rule, e.g. `.=(+)====[ XVII ]====(+)=.`
  bottom band line 1: `<CARD NAME>` (name only — numeral lives up top)
  bottom band line 2 (majors): `~ <romanized letter> · <sign/element> ~`
  (e.g. `~ heh · aquarius ~`); smalls: `~ <crowley title> · <decan> ~`;
  courts: elemental title.
  The Hebrew LETTER is the primary attribution (the card's Tree-of-Life address);
  the sign is derived. Romanized only — real Hebrew glyphs are Unicode and live in
  site chrome (HTML beside the card), NEVER in the .txt/.ans art.
- **Color.** Map to the actual Harris palette for that card. Introduce no color with
  no referent in the painting.
- **Signature.** Sign `aw` or leave unsigned. NEVER `jgs`. Credit style "after jgs".

## Output
- One large `.txt` (exact whitespace preserved).
- One `.ans` with the card's palette: 256-color, with a 16-color fallback.

## Reasoning tier
Author at the highest tier (x-high / best). This is low-volume, high-craft work; the
cost is negligible and the marginal quality shows most in the esoteric SYNTHESIS
(right attributions, letter/path/element) and in clean compositor structure. It does
NOT fix placement drift — for that, use the loop.

## Render & review loop (do not skip)
You cannot judge glyph placement, mass volume, occlusion, or palette by reading the
source; you must SEE the rendered card. Every pass runs the full chain and then LOOKS:

1. `compose_<card>_lg.py`  -> emits `<card>-art-lg.txt` + `<card>-lg-classes.json`
2. `frame.py <art> "<NAME>" "<attrib>" -w 47 -s majors -n <NUMERAL> -o <card>-lg-v1.txt`
3. `cardkit.py <card>`     -> emits `-preview.html` + `-lg-256.ans` + `-lg-16.ans`
4. `render_png.py <card> --axis`  -> emits `<card>-render.png` (Harris scan beside the
   colored render, center-axis guide drawn). **Open the PNG and critique it** against
   the scan: is the figure centered on the axis line? do masses read round and lit, not
   flat outlines? does the foreground occlude cleanly? is the palette the painting's?
5. Fix the compositor and repeat from 1. Do NOT ship a card whose PNG you have not
   viewed at least once. Ship at ~80% once the render holds up: 2-3 review passes max,
   then move on.

The per-card DIRECTIVES block (ranked 1-N, non-negotiable / makes-it-Thoth / garnish)
carries everything specific to the card.

## Full ultracode panel (creation + review)
The full-quality production method for a card. Instead of one composer authoring blind
and committing to its first instinct, run a multi-agent PANEL:

1. **Three composer agents, in parallel.** Each commits to a DISTINCT composition
   strategy for the card (different framing / dominant element / emphasis — see the
   per-card "three strategies" seed in the prompt). Each composer runs the full Render
   & review loop above end to end (3+ compose -> `render_png.py --axis` -> VIEW png ->
   critique cycles, viewing its own PNG each pass) and returns its best candidate as
   `.txt` + `.ans` + `-render.png`.
2. **Three judge agents.** Score the three candidates against the Harris scan + the
   axis guide on: iconographic fidelity, composition/energy, legibility at 47×32,
   occlusion, and palette. Each judge ranks; tally the votes.
3. **Synthesis / polish / integration (lead).** Take the winning candidate or MERGE the
   strongest elements across candidates, run one final render & review pass, finalize
   the `.txt` + `.ans`, then wire into `cardkit.CONFIGS` + `index.html`.

Cost: ~300-450k tokens/card (3 composers @ ~60-90k + 3 judges @ ~25-40k + synthesis) —
roughly 10-15x the solo cost for ~1.5-2x quality. Its real value is exploring three
composition strategies instead of committing to the first instinct; reserve the full
cost for cards whose composition is genuinely hard or contested. The MIDDLE PATH (one
composer + the mandatory render loop + one adversarial critique pass, ~80-120k) captures
most of the benefit for the rest; solo (~one pass) is the floor. State which tier a card
runs at in its prompt.

## Every per-card prompt MUST
- open by referencing THIS file (`FABLE_TEMPLATE.md`) and recap its invariants compactly;
- restate the axis rule (center on col 23) in the directives;
- include a "Render & review" line pointing at the loop above (`render_png.py --axis`);
- state the reasoning tier (x-high / best);
- include a "Full ultracode panel" block: the 3-composer / 3-judge / synthesis workflow
  plus a card-specific THREE STRATEGIES seed (the three distinct composition directions
  the composers should each take).
