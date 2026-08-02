# Fable5 Prompt — Atu XVII, The Star (Thoth)

## Role
You are rendering monospace ASCII/ANSI art of a Thoth Tarot card. Your job is not to draw a diagram of the card's symbols but to reproduce the *composition and energy* of Lady Frieda Harris's painting in text. Fidelity to Crowley's iconography AND to the feel of the original image both matter. Work in a fixed-width grid, Courier New assumed.

## Subject
**Atu XVII — The Star.** Hebrew letter Heh, attribution Aquarius (post-AL II:57 swap: Star keeps Aquarius, Emperor takes Aries/Tzaddi). Nuith personified in tangible human form. The card of hope arriving after the Tower's destruction.

## The composition, in one sentence
She kneels against a giant rose celestial globe; everything in the frame spirals except one rigid straight stream from the lower cup.

Hold those two facts above all else. If you get only two things right, get the globe-as-backdrop and the spiral-vs-straight contrast.

---

## Ranked directives (1-5 non-negotiable, 6-8 make it Thoth, 9-10 soul + garnish)

**1. The globe IS the stage.** The huge pink/rose celestial sphere is the backdrop the whole composition sits against, not a satellite floating in the corner. Draw it large enough that the figure kneels *in front of* it. Give it volume with a dithering density ramp (`. : · ' ° :` light-to-dark), not a flat outline circle. It is the entire heavens, not Earth. This is the #1 compositional fix.

**2. Spiral everything except one rigid stream.** Crowley's own thesis: every energy in the card spirals (curved glyphs `( ) , ´ . ´ , . - ' \ /`) EXCEPT the lower cup's rectilinear streams (rigid vertical `| |`). Humanity's blindness is "the illusion of straightness." In monospace this contrast reads even harder than in paint, exploit it. This is the single most ASCII-native idea in the card.

**3. Figure seen from behind, whirling.** Nuith is nude, kneeling, viewed from behind, one arm arched overhead, her pose "a whirling swastika of motion." Currently the render is frontal and stiff. Rebuild the body with flowing diagonal anti-aliasing strokes so the torso reads as an S-curve / spiral, not a stick figure.

**4. Three Babalon stars, rotation implied by ray angle.**
   - The great seven-pointed white-crystal star, upper left, spinning counterclockwise (curl the ray tips CCW). The A∴A∴ sigil.
   - A second star whirling on the celestial globe itself.
   - A tiny star-seed tumbling clockwise, falling out of the golden cup.
   Make all three real heptagrams (7 points), not sun/compass bursts.

**5. Two cups, opposite roles.**
   - **Golden cup, raised high:** pours ethereal water ("milk of the stars") onto her own head. She is her own fountain. Curved cascade.
   - **Silver/pewter cup, lowered:** pours the immortal liquor onto the junction of land and water. THIS is the rigid rectilinear stream from directive 2.

**6. The crystalline earth at the junction.** Twenty-plus seven-sided translucent solids at her feet, the geometry of matter, where the formless Sea of Binah meets the fertile shore. Shade the facets (light plane / dark plane per solid) instead of open `<>` outlines so they read as faceted crystal.

**7. Palette (ANSI/256 + 16-color fallback).** Map Harris's colors deliberately:
   - Figure: silver / cyan-white
   - Globe + crystals + roses: rose / magenta / pink
   - Cosmos / swirls / Abyss clouds: indigo / violet / deep blue
   - Stars: bright white
   Do not introduce colors with no referent in the painting (no stray yellow/red unless it maps to a real element).

**8. The whirling background.** Her hair whirls up into clouds that hide the Abyss. Fill remaining negative space with curved sweep strokes radiating from behind her, so the field reads as cosmic motion, not dead black. (Directive 1's globe already does most of this work.)

**9. Hope as the meaning.** Divinatory sense to honor in tone: hope, unexpected help, clearness of vision, realization of possibilities, spiritual insight. The promise of things unseen after the Tower. Light and upward-reaching, not somber.

**10. Witnesses of the shore.** Butterflies (liberated souls, spirit = 5), dark red roses (Venus, fertility), and the Pyramid City across the sea (home of enlightened souls). Small, lower area. Garnish, but it's the difference between Thoth and generic.

---

## Technical constraints (do not violate)
- **Cell aspect ratio ~1:2.** Monospace cells are taller than wide. Draw the globe and stars WIDER than tall or they render as squashed eggs. Bake the correction into every circle/curve.
- **Font pin: Courier New.** The extended line alphabet (`´ ‾ ¡ ·`) breaks the overline glyph in Share Tech Mono. Assume Courier New for all spacing.
- **Line alphabet:** basic `` ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }`` plus extended `´ ‾ ¡ ·` and alphanumeric line-glyphs `o O v V T L 7 U c C x X`.
- **Full-bleed density.** Push composition out to the card border. The painting is edge-to-edge; do not float a sparse figure in the middle of empty frame.
- **Card frame:** keep the outer border box and the bottom title band `XVII . THE STAR  ~ aquarius ~`.

## Output
- One large-format art block (target the existing `17-star-art-lg.txt` dimensions).
- Provide both a plain `.txt` version and a `.ans` version with the palette from directive 7 (256-color, with a 16-color fallback).
- Preserve exact leading whitespace on every line. Do not let it collapse.

## The one-line brief
She kneels against a giant dithered rose globe; everything spirals except one rigid stream from the lower cup. Get those two and the card stops being a diagram.
