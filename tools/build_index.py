#!/usr/bin/env python3
"""Build drafts/gallery.html — a compact dark gallery of every finished
card in truecolor. NOTE: the real site page is the hand-structured root
index.html (updated via update_index.py); this gallery is a quick-look
extra and must NOT write to the root."""
import os
import cardkit
import star_html, fool_html, moon_html

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DRAFTS = os.path.join(ROOT, "drafts")

# (sort key, caption, heb, loader) — loader returns (lines, grid, palette)


def legacy(mod, card_arg=None):
    def load():
        lines, grid = mod.load(*(card_arg and [card_arg] or []))
        return lines, grid, mod.TRUE
    return load


def kit(card):
    def load():
        cfg = cardkit.CONFIGS[card]
        lines, grid = cardkit.load_grid(
            os.path.join(DRAFTS, cfg["txt"]),
            os.path.join(DRAFTS, cfg["classes"]), cfg["default"])
        return lines, grid, cfg["true"]
    return load


CARDS = [
    ("0 · THE FOOL", "aleph · air", "&#x5D0;", legacy(fool_html)),
    ("II · THE PRIESTESS", "gimel · moon", "&#x5D2;", kit("02-priestess")),
    ("III · THE EMPRESS", "daleth · venus", "&#x5D3;", kit("03-empress")),
    ("IV · THE EMPEROR", "tzaddi · aries", "&#x5E6;", kit("04-emperor")),
    ("XVII · THE STAR", "heh · aquarius", "&#x5D4;", legacy(star_html, "large")),
    ("XVIII · THE MOON", "qoph · pisces", "&#x5E7;", legacy(moon_html)),
]

figs = []
for caption, attrib, heb, loader in CARDS:
    lines, grid, pal = loader()
    card = cardkit.html_card(lines, grid, pal)
    figs.append(
        f'<figure><pre>{card}</pre>'
        f'<figcaption><b>{caption}</b><br>{heb} · {attrib}</figcaption></figure>')

page = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>ASCII Tarot — the Thoth deck, after jgs</title>
<style>
  body {{ background: #000; color: #c8c8d8; margin: 2rem;
         font-family: "Courier New", Courier, monospace; }}
  header {{ text-align: center; margin-bottom: 2.5rem; }}
  h1 {{ font-size: 22px; letter-spacing: .35em; color: #d8cfa8;
       font-weight: bold; margin: 0 0 .4rem; }}
  header p {{ color: #666; font-size: 13px; margin: 0; }}
  main {{ display: flex; gap: 3rem; justify-content: center;
         flex-wrap: wrap; }}
  figure {{ margin: 0 0 2rem; }}
  pre {{ font-family: "Courier New", Courier, monospace; font-weight: bold;
        font-size: 13px; line-height: 1.2; }}
  figcaption {{ text-align: center; margin-top: .8rem; font-size: 13px;
               color: #8f8fb8; }}
  figcaption b {{ color: #d8cfa8; letter-spacing: .15em; }}
  footer {{ text-align: center; color: #555; font-size: 12px;
           margin-top: 2rem; }}
</style></head><body>
<header><h1>ASCII TAROT</h1>
<p>the Thoth deck in line-style ASCII · after jgs · 6 of 78</p></header>
<main>{''.join(figs)}</main>
<footer>art: original, in the line style of Joan G. Stark (jgs) ·
deck: Crowley/Harris Thoth · aw</footer>
</body></html>
"""
with open(os.path.join(DRAFTS, "gallery.html"), "w") as f:
    f.write(page)
print("wrote drafts/gallery.html")
