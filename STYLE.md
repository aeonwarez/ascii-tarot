# Joan Stark (jgs) Line-Style Dossier

Compiled 2026-07-31 from her own archived tutorial/FAQ pages (oldcompcz/jgs
GitHub mirror of her Geocities site — 13,291 `<pre>` blocks, ~7,900 signed
works analyzed programmatically), Wikipedia, the alt.ascii-art FAQ she
hosted, and secondary sources. Complements
`../ascii-agent/ASCII_ART_AGENT.md` and `../ascii-agent/generator/GENERATE.md`.

## Who she was

Joan G. Stark ("jgs", handle "Spunk"/"spunk1111"), from suburban Cleveland,
Ohio. Discovered ASCII art 1995 on alt.ascii-art, began drawing May–July 1996
(first big piece: a fire-breathing dragon that took a week). Active
1996–2003, 1,500+ pieces, dubbed the **"Queen of ASCII art"**. Worked
freehand in Windows Notepad, ~20 min/piece. Her gallery
(geocities.com/SoHo/7373, later www.ascii-art.com) drew 250k+ visitors
1996–98. Geocities died 2009; the site survives via the oocities mirror,
the oldcompcz/jgs GitHub mirror (the one vendored in ascii-agent and
ascii-ching), and Christopher Johnson's collection (asciiart.website,
1,514 attributed pieces). The Velvetyne "Jgs Font" is a typographic tribute
to her line style, which Velvetyne compares to **ligne claire** comics.

## Tarot connection (verified)

Her site received an **"Aeclectic Award" (October 1998) from Solandia**,
founder of Aeclectic Tarot — a site award for her gallery, NOT commissioned
tarot art (zero hits for "tarot" across her 974 mirrored files). Her
occult/mystical catalogue is still deep and directly usable as exemplars:
wizards, mage, crystal balls, swords/Excalibur, crowns, dragons, knights,
Medusa, Grim Reaper, fairies, mermaids, suns, moons, **phases of the moon**,
stars, comets, **zodiac signs**, witches, cauldrons, devils, skeletons,
skulls, tombstones.

## Character vocabulary (measured from her corpus)

```
_ (~11%)  | (~8%)  . (~8%)  - (~7.5%)  / (~6.5%)  \ (~6%)
' (~4%)   : (~4%)  ` (~3%)  = (~2.7%)  ~ (~2%)    " (~2%)
( ) each ~2%   * (~1.6%)  o (~1.5%)  , (~1.5%)  ; (~1.4%)  ^ (~1.4%)
then # @ % < > { } and letters-as-texture (s S w W m M e o)
```

- **Horizontals:** `_` cell floor, `-`/`=` mid-cell, `~` waves, `"`/`'` top ticks
- **Verticals/diagonals:** `|` (never capital I), `/`, `\`
- **Curves:** `( )` for bellies/cheeks/curls (beards = stacked `((( )))`),
  corner idioms `.-'` `'-.` `` `-. `` `_.-~`, tiny segments `, . ' ` ``
- **Slope alphabet** (her core lesson): `_,.-'"^` — gradual `__,,..--""^^`,
  steep `_.-"` stacked
- **Glyph height matters:** bottom-dwellers `. , _`; mid `- = +`; top `' " ^`.
  Interchangeable pairs for fine-tuning: `"↔'`, `.↔,`, `-↔=`
- **Texture (selective, inside outlines, never tonal fill):** `:` lattices
  (`.:.:.:`) for cloth/glass, `;`/`,` stipple, `#`/`@` dark accents,
  `o O *` dots/stars/bubbles, `sSSs` `wwWWWww` `mMm` fur/foliage/flame
- **Sparkle/magic idioms:** `\'/  -= * =-` (mage's staff-star), scattered
  `. * '` star fields with irregular spacing, `( .*)` swirls
- **Ground/water:** repeated `~^~_-~^_~` and `^^^ ^^ ^` runs
- **Eyes/faces:** `@ @`, `o o`, `6 6`, `(.)(.)`, cheeks `( )`, mouths
  `\__/` `'--'` — rounded folk-art warmth is part of the style

## Canvas & formats (measured)

- Median width **~38 cols**; bulk 20–60; nothing over 79 (Usenet wrap limit).
  Heights typically 8–35 rows. Small is authentic.
- House title format above a piece: `~ Title ~  M/YY` or `-=[ title ]=-`
- Signature: lowercase `jgs` **inside the artwork's footprint, lower-left**,
  padded by spaces, 1–2 rows above the bottom edge (7,861 lowercase vs 59
  uppercase in corpus). FAQ commandment: never strip a signature.

## Character palette (PROJECT RULE)

Adopted 2026-08-01: the Stone Story RPG tutorial kit PLUS the full jgs kit
(user: jgs items always allowed; the rule is not stricter than her practice).
Card art may use ONLY these characters (enforced by `tools/frame.py`):

```
Structural:            ` ~ ! ^ ( ) - _ + = ; : ' " , . \ / | < > [ ] { }
Extended (style-safe): ´ ‾ ¡ ·
Shape letters:         o O v V T L 7 U c C x X    (Stone Story)
jgs texture letters:   s S w W m M e i 6          (hair sSSs, fur wwWWww,
                                                   flame mMm, eyes 6 6, }i{)
jgs accents:           * @ # % &                  (stars, centers, dense dark)
```

Everything else (digits other than 6/7, remaining letters, `$ ? [caps]`) is
out unless we amend this list. The `aw` signature is exempt (signature, not
art). Both idioms are valid where they overlap: stars `*` or `+ x ·`,
butterflies `}i{` or `}v{`, hair `sSSs` or `cCCc`.

## Rules for new ascii-tarot art

1. Fixed-width font; strict printable ASCII 32–126. No Unicode, no
   box-drawing, no accented chars.
2. Outlines, not fills — contour like ink drawing, whitespace interiors,
   selective texture only. (Her "Solid to Line Conversions" page is the
   Rosetta stone: dense `$$$` masses → clean `.-''-.` contours + `@` eyes
   + small `:::` accents.)
3. Avoid serif-fragile constructions: no `L`/`7`/`J` corners; design to
   survive `~`/`'`/`^` rendering differently across fonts.
4. Card canvas ≤ 79 cols total including frame; keep art in her sweet spot.
5. Sign **`aw`** (lower-left, inside the footprint) or leave unsigned —
   NEVER `jgs`. Credit the style "after jgs" in site attribution.
6. Learn her way: duplicate an existing jgs piece line-by-line, then modify,
   then draw new from exemplars (`../ascii-agent/generator/jgs.py exemplars`).

## Key sources

- Tutorial: https://oldcompcz.github.io/jgs/joan_stark/howto.html
- "Who is jgs?": https://oldcompcz.github.io/jgs/joan_stark/me.html
- alt.ascii-art FAQ: https://oldcompcz.github.io/jgs/joan_stark/faq.html
- Solid→Line conversions: https://oldcompcz.github.io/jgs/joan_stark/conversi.html
- Mirror: https://github.com/oldcompcz/jgs · https://www.oocities.org/spunk1111/
- Wikipedia: https://en.wikipedia.org/wiki/Joan_Stark
- Velvetyne Jgs font: https://velvetyne.fr/news/about-ascii-art-and-jgs-font/
- Christopher Johnson collection: https://asciiart.website/artist.php?artist_id=4
