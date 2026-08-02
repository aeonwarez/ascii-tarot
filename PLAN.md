# ASCII Tarot — Project Plan

Sibling site to [ascii-ching](../ascii-ching): a full 78-card tarot deck rendered
as original line-style ASCII art (after jgs / Joan Stark), using the **Thoth
deck** (Crowley/Harris) as the primary visual + esoteric reference, with a
Rider–Waite–Smith variant possible later.

## The deck (Thoth structure — 78 cards)

### Major Arcana (22) — Thoth names
| # | Card | Thoth notes |
|---|------|-------------|
| 0 | The Fool | air, green man / vortex |
| I | The Magus | Mercury, juggling weapons of the four suits |
| II | The Priestess | Moon, veil of light, camel |
| III | The Empress | Venus, pelican, twisted flames |
| IV | The Emperor | Aries, bees & fleur-de-lys, ram |
| V | The Hierophant | Taurus, bull, pentagram-child |
| VI | The Lovers | Gemini, alchemical marriage, orphic egg |
| VII | The Chariot | Cancer, four sphinxes, Holy Grail |
| VIII | Adjustment | Libra (RWS: Justice), masked woman on toes, sword & scales |
| IX | The Hermit | Virgo, lamp/sun, wheat, Cerberus |
| X | Fortune | Jupiter, wheel with sphinx/Hermanubis/Typhon |
| XI | Lust | Leo (RWS: Strength), Babalon riding the Beast |
| XII | The Hanged Man | water, ankh, serpent |
| XIII | Death | Scorpio, skeleton with scythe, fish/scorpion/eagle |
| XIV | Art | Sagittarius (RWS: Temperance), alchemical fusion, cauldron |
| XV | The Devil | Capricorn, goat before world-tree |
| XVI | The Tower | Mars, eye of Horus, dove & serpent, falling figures |
| XVII | The Star | Aquarius, Nuit pouring two cups |
| XVIII | The Moon | Pisces, twin towers, Anubis, scarab with sun |
| XIX | The Sun | Sun, twin children on green mound, zodiac wall |
| XX | The Aeon | fire (RWS: Judgement), Nuit arch, Horus child |
| XXI | The Universe | Saturn/earth, dancer with serpent in oval |

### Minor Arcana (56)
Four suits — **Wands** (fire), **Cups** (water), **Swords** (air), **Disks**
(earth; RWS: Pentacles). Ace–10 each, plus Thoth courts: **Knight, Queen,
Prince, Princess** (map to RWS King/Queen/Knight/Page).

Every small card (2–10) carries its Crowley title (e.g. 2 of Wands
"Dominion", 3 of Swords "Sorrow", 10 of Disks "Wealth") plus its astrological
decan — these go in the card data and on the rendered card.

## Art pipeline (reuse ascii-agent)

1. `ascii-agent/generator/jgs.py exemplars "<subject>"` → 2–4 jgs exemplars
   per card subject (archive: 6,350 pieces; strong on moons, suns, stars,
   angels, swords, cups, towers, wizards, animals).
2. Generate original line-style art per the invariants in
   `ascii-agent/ASCII_ART_AGENT.md` + `generator/GENERATE.md`:
   - printable ASCII only, no Unicode/box-drawing
   - curves `. - ' \ / ( ) ~`, texture `: ; = *`, whitespace does the shading
   - fixed card canvas (size TBD — consistent frame across all 78)
   - **sign `aw` or unsigned, NEVER `jgs`**; credit style "after jgs"
3. Curate/reroll; store one `.txt` (or JSON entry) per card.

## Site (mirror ascii-ching architecture)

ascii-ching is a zero-dependency static site: `index.html` (all CSS inline,
2,084 lines) + `app.js` (all logic, 3,377 lines) + per-item asset dirs +
built JSON, deployed via GitHub Pages (CNAME + .nojekyll + manifest +
sitemap + robots). We mirror that shape with these adaptations:

### Keep verbatim (port from ascii-ching)
- CSS-variable theme system: `themes` object in JS applies ~22 custom
  properties, 7 themes (terminal/void/abyss/amethyst/sapphire/93/ember),
  matching `favicon_<theme>.png` swap, `localStorage` persistence
- Per-character span wave engine (`startAsciiWave` — the site's signature
  visual), scanline/CRT overlays, starfield
- `crypto.getRandomValues` for draws (not Math.random)
- Signature toggle: `*_nosig.txt` art variants + `ascii_artists.js`-style
  attribution map
- `saveReading()` 80-col text export, `copyPrompt()` AI-analysis button,
  themed 404 ("The Card That Is Not"), `footer-effects.js` for secondary pages
- Coin-flip animation technique — the horizontal width-squeeze that fakes 3D
  rotation (`renderCoinStage`) becomes the **card flip** (face-down → face-up)

### Improve over ascii-ching (its known warts)
1. One render path + CSS layout switching instead of duplicated
   Desktop/Mobile function pairs (~halves app.js)
2. Shared `styles.css` instead of inline CSS copy-pasted per page — so
   secondary pages theme too
3. No parallel hand-maintained content dumps; generate from JSON
4. No vendored archives/PDFs in the deploy tree
5. Correct manifest icon sizes; wire the retro day-counter properly

### Data layout
```
cards/00-fool/ … 21-universe/        (Majors, Thoth names)
cards/wands-ace … wands-10, wands-knight/queen/prince/princess
cards/cups-… swords-… disks-…       (78 dirs total)
  ascii_card.txt / ascii_card_nosig.txt
  text_<source>.txt                  (authored interpretation sources)
decks/<source>.json                  (built, one fetch per source, keyed by slug)
  { id, name, number, arcana, suit, title,        // "Dominion" etc.
    attribution,                                   // "Mars in Aries" etc.
    upright, reversed, keywords[], imagery }
build/build-decks.js                 (txt → json, like build-translations.js)
```

### Draw mechanics
- Shuffle + draw: single card, three-card spread; Celtic Cross later
- Card flip animation (width-squeeze), reversed cards as inverted meaning
  (art stays upright — ASCII doesn't flip well; mark reversal in the frame)
- Spread positions as clickable regions (like the bagua logo's span-slicing)

## Canvas standard (LOCKED 2026-08-01)

**Art 47 cols × 32 rows → framed 51×39.** Rendered aspect = 0.5 × 51/39 =
0.64 — the exact Thoth card ratio (70×110mm). Rationale: spheres/circles
need WIDTH (2:1) because monospace cells are 1:2; 36-col alternatives
starve the Star's globe and force horizontal re-cuts. Compact 37-interior
(41×26) format remains for multi-card spread layouts.

## Open decisions

- [ ] Interpretive text source(s) — Book of Thoth distillation? multiple
      "translations" like ascii-ching?
- [ ] Domain + deploy setup
- [ ] RWS variant as a second "deck" toggle (later)
