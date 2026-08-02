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

## Process
Ship at 80%. 2-3 passes max per card, then move on. The per-card DIRECTIVES block
(ranked 1-N, with a non-negotiable / makes-it-Thoth / garnish tiering) carries
everything specific to the card.
