#!/usr/bin/env python3
"""Replace placeholder <pre> blocks in the site index.html with finished
truecolor card renders. Idempotent: re-running refreshes the same blocks."""
import os, re
import cardkit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DRAFTS = os.path.join(ROOT, "drafts")

SECTIONS = {
    "02-priestess": "II THE PRIESTESS",
    "03-empress": "III THE EMPRESS",
    "04-emperor": "IV THE EMPEROR",
    # panel finals land in the main slot where only a placeholder existed
    "01-magus-final": "I THE MAGUS",
    "05-hierophant-final": "V THE HIEROPHANT",
}

path = os.path.join(ROOT, "index.html")
with open(path) as f:
    page = f.read()

for card, marker in SECTIONS.items():
    cfg = cardkit.CONFIGS[card]
    lines, grid = cardkit.load_grid(
        os.path.join(DRAFTS, cfg["txt"]),
        os.path.join(DRAFTS, cfg["classes"]), cfg["default"])
    html = cardkit.html_card(lines, grid, cfg["true"])
    section_re = re.compile(
        r"(<!-- =+ " + re.escape(marker) + r" =+ -->.*?<div class=\"col-ascii\">)"
        r"<pre>.*?</pre>", re.DOTALL)
    # function repl: card html may contain backslash sequences (\o/ etc.)
    # that re's template parser would reject as bad escapes
    page, n = section_re.subn(
        lambda m, h=html: m.group(1) + "<pre>" + h + "</pre>", page, count=1)
    print(f"{card}: {'replaced' if n else 'MARKER NOT FOUND'}")

with open(path, "w") as f:
    f.write(page)
print("index.html updated")
