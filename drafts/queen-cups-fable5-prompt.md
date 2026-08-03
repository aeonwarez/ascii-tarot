# Fable5 Prompt - Queen of Cups (Thoth court card)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is
not to draw a diagram of the card's symbols but to reproduce the *composition
and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's
iconography AND to the feel of the original image both matter. Work in a
fixed-width grid, Courier New assumed. Note: a Harris scan of this court card
DOES exist in this repo (`reference/queen-cups-card.jpg`, scan source
esotericmeanings.com court-cards page), so you judge against a pixel reference
as well as Crowley's verbal description in the Book of Thoth.

## Invariants (recap of FABLE_TEMPLATE.md)
Monospace Thoth tarot art. Canvas art 47x32, framed 51x39, aspect 0.64, exact
leading whitespace preserved on every line. **Center on the axis (col 23):**
the goddess-as-chalice and the still water she rises from are the stage,
centered on column 23; her chalice-body is balanced about the axis, and her
near-unbroken reflection hangs directly below her on the same axis. Place
asymmetric sprites (the ibis, the lotus, the shell-cup with crayfish) at
`23 - len(s)//2` and verify with `--axis`. Cells are 1:2 so draw circles and
curves (the cup bowl, the veiling arcs of light, the crown radiance) about 2:1
wider than tall. Courier New; extended alphabet `´ ‾ ¡ ·` + line-glyphs
`o O v V T L 7 U c C x X` allowed. Solid masses dithered for volume, never open
outlines, lit directionally. Foreground figure drawn ON TOP; break background
edges (veiling curves, water line) behind her. Full-bleed to the border. Keep
outer frame + bottom title band. Courts have NO numeral plaque; use the
elemental title band. Sign `aw` or unsigned, never `jgs`. Output one `.txt` +
one `.ans` (256 + 16 fallback).

## Reasoning tier
Author at the highest tier (x-high / best). Low-volume, high-craft work; the
marginal quality shows in the esoteric synthesis and clean compositor
structure. It does NOT fix placement drift, an under-scaled chalice-body, or
the mirror-reflection read - for those, use the render & review loop.

## Subject
**Queen of Cups.** Water of Water (the watery part of Water, its power of
reception and reflection). Tetragrammaton: He primal (first He) of the
water-suit; she receives, ferments, and transmits the Knight's energy, seated
upon her throne. Rules 21 degrees Gemini to 20 degrees Cancer; dominates
cardinal Cancer. GD titles: Queen of the Thrones of Water, Queen of the Nymphs
or Undines. Crest: Ibis. Water of Water is mirror to mirror: she reflects the
nature of the observer in great perfection, and the sea returns her image
almost unbroken.

## The composition, in one sentence
A veiled goddess who IS a great cup rises out of still water, robed in endless
curves of light, bearing a shell-cup with a crayfish and the Lotus of Isis,
while the mirror-flat sea beneath her carries her near-unbroken reflection.

Hold two facts above all else: she is the CHALICE, not a woman holding one (her
body is the stem, per the High Priestess mirror-geometry), and the lower half
is a MIRROR returning her almost unbroken. If you get only two things right,
get the goddess-as-cup and the reflecting still water.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The goddess IS the cup, and the cup is the stage.** DuQuette: the card
presents "the image of a great cup, the stem of which is formed by the body of
a goddess," and it is Atu II (High Priestess) turned upside down. Draw the
central figure as a large chalice standing on the axis: a wide dithered bowl
above, the veiled body narrowing to a stem below, planted in the water. Not a
woman holding a goblet, a woman who reads AS a goblet. This is the #1
compositional read. Dither for volume (`. : · '`), never open outline.

**2. Still water as her throne, mirror-flat.** "She is represented as enthroned
upon still water." There is no solid seat; the lower half of the card is a
glassy surface she rises out of. Draw a hard flat waterline across the axis
and keep everything below it calm, unrippled, reflective.

**3. The near-unbroken reflection.** "The sea upon which she is enthroned
conveys the almost unbroken images of the image which she represents." Water of
Water is mirror to mirror. Below the waterline, echo the figure inverted, the
chalice mirrored point-for-point but softened, so the reflection reads almost
as strong as the figure. This is the single most Thoth-specific idea in the
card: reflection of reflection. Center the mirror on the same axis (col 23).

**4. Veiled by endless curves of light.** "She is robed in, and veiled by,
endless curves of light." Her robe is not cloth but overlapping arcs and
ribbons of light nested over the whole upper card (`,-~^~-.` stacked arcs).
They half-hide her: "to see the Truth of her is hardly possible." Keep her face
indistinct, low-contrast, given to reflection rather than expression.

**5. The shell-cup with the crayfish, and the Lotus of Isis.** "In her hand she
bears a shell-like cup, from which issues a crayfish, and she bears also the
Lotus of Isis, of the Great Mother." Two named held objects: a scalloped
sea-shell cup with a small crayfish crawling out of it, and a long-stemmed
lotus (sacred to the mother goddess) with pads low on the water. Make the shell
scalloped (not a plain goblet) and the crayfish legible.

**6. The ibis in the still water.** The GD crest is the Ibis; in the Harris
painting a pale heron/ibis wading bird stands in the water, mirrored in the
surface. Place it to one side of the axis, occlude cleanly where it crosses the
reflection, and echo it inverted below the waterline like everything else.

**7. Water of Water - cool the whole palette.** Cool blues and blue-greens
dominate this card, as DuQuette says they do all the Cups court cards. Keep the
field teal / slate / pale blue, with silver-white on the veiling curves of
light. One warm exception only: a pale cream radiance breaking at the crown
(directive 9). Green solely for the lotus and its pads.

**8. Palette (ANSI/256 + 16-color fallback), scan-observed.** Map from the
Harris scan `reference/queen-cups-card.jpg`:
   - Field / masses: cool blue, teal, slate blue-green.
   - Veiling curves of light: silver-white, pale blue-green (brightest values).
   - Crown radiance: pale warm cream / yellow (the one warm note).
   - Figure / chalice-body: blue-green and grey-white, veiled, low contrast.
   - Still water / mirror: darker blue-green below, paler blue-white
     reflected highlights.
   - Ibis: pale grey-white.
   - Lotus and pads: green.
   Introduce no color with no referent in the scan.

**9. The crown radiance as light source.** A pale cream / yellow light breaks
at the top center of the card and feeds the veiling curves of light. It is the
head of the chalice and the one warm value against the cool field. Rayed but
soft (`\ \|/ /`), not a hard sunburst.

**10. Reflection as the meaning, and garnish.** Divinatory tone to honor:
dreaminess, illusion, tranquillity; the perfect agent and patient who receives
and transmits everything without being affected. Water of Water is mirror to
mirror. She reflects the observer back at themselves. Render her serene,
veiled, self-effacing, given to the water. Garnish: lily pads on the mirror,
reflected highlights, the ripple-free calm that makes the mirror possible. It
is the difference between Thoth and a generic queen with a chalice.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the
  cup bowl, the veiling arcs, and the crown radiance WIDER than tall or they
  render as squashed eggs. Bake the correction into every circle and curve.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the
  overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }``
  plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs
  `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border. The
  painting is edge-to-edge; do not float a sparse figure in empty frame.
- **Card frame + court title band.** Keep the outer border box. Courts carry
  NO numeral plaque up top. Bottom band line 1: `QUEEN OF CUPS`; line 2:
  `~ he . water of water ~`. Romanized letter only in the art; the real Hebrew
  glyph lives in site chrome (HTML), never in the `.txt` / `.ans`.

## Render & review
Do not judge chalice scale, the goddess-as-cup read, the mirror reflection,
placement, or palette by reading the source. Run the chain and LOOK:
`compose_queen-cups_lg.py` -> `frame.py` -> `cardkit.py queen-cups` ->
`render_png.py queen-cups --axis`, then OPEN the PNG and critique it against the
Harris scan `reference/queen-cups-card.jpg`. Does the central figure read as a
great cup (goddess-as-stem), centered on the axis guide, not a woman holding a
goblet? Is the lower half a mirror-flat water carrying her near-unbroken
inverted reflection on the same axis? Is she veiled by nested curves of light?
Are the shell-cup with crayfish and the Lotus of Isis both present? Is the ibis
wading and mirrored? Is the palette cool blue / blue-green / silver-white with
one warm cream crown light and green only for the lotus, no stray colors? Fix
the compositor and repeat. Ship at ~80% once the render holds (2-3 passes max).
Note: `queen-cups` must be in `cardkit.CONFIGS` before render_png will run. See
FABLE_TEMPLATE.md "Render & review loop."

## Full ultracode panel (creation + review)
Produce this card via the FABLE_TEMPLATE.md full ultracode panel: three
composer agents in parallel (each running the Render & review loop above to a
finished candidate, viewing its own PNG each pass and judging against the
Harris scan), three judges scoring each candidate on iconographic fidelity to
text and scan, composition/energy, legibility at 47x32, occlusion, and palette,
then synthesis / polish / integration merging the strongest read. Three
strategies to seed the composers:
- **A. Chalice-as-stage dominant** - the great cup (goddess-as-stem) is the
  field, filling the axis top to waterline; the shell-cup, lotus, and ibis are
  small satellites, the mirror echoing it below.
- **B. Mirror-dominant** - the near-unbroken reflection is the hero read: the
  card is split hard at the waterline, figure above answered almost exactly
  below, the whole composition about reflection of reflection.
- **C. Veil-of-light-field dominant** - the endless curves of light are the
  field: nested luminous arcs sweep the whole upper card, the veiled goddess
  emerging from within them, the water calm beneath.
Tier: **full panel** - contested read (goddess-as-cup vs. woman-with-cup, and
how strongly to commit the mirror) justifies the full cost.

## Output
- One large-format art block (target the existing large-format card dimensions,
  47x32 art / 51x39 framed).
- Provide both a plain `.txt` version and a `.ans` version with the palette
  from directive 8 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
A veiled goddess who IS a great cup rises from mirror-flat still water that
returns her almost unbroken: get the goddess-as-chalice and the reflection of
reflection and the card stops being a queen with a goblet.
