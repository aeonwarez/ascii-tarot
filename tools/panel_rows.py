#!/usr/bin/env python3
"""Insert/refresh the ultracode-panel rows for a card section in index.html:
a row with the 3 composer candidates, then a centered row with the synthesis.
Idempotent via <!-- panel:<card> --> marker comments; re-running refreshes.

Usage: python3 panel_rows.py <card> "<SECTION MARKER>"
  e.g. python3 panel_rows.py 00-fool "0 THE FOOL"
Expects cardkit CONFIGS entries <card>-v3a/-v3b/-v3c and <card>-final.
Candidate captions live in LABELS below (strategy names + judge tally).
"""
import os, re, sys
import cardkit

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DRAFTS = os.path.join(ROOT, "drafts")

LABELS = {
    "00-fool": {
        "v3a": "A · figure-dominant · judges 6 pts",
        "v3b": "B · vortex-dominant · judges 3 pts",
        "v3c": "C · mandala-balanced · judges 9 pts · winner",
        "final": "synthesis · v3c base + v3a figure + v3b dove/coins",
    },
    "01-magus": {
        "v3a": "A · mercury-glyph figure · judges 7 pts",
        "v3b": "B · caduceus-spine · judges 7 pts · base",
        "v3c": "C · juggling-orbit · judges 4 pts",
        "final": "synthesis · v3b base + v3a foot-wings + v3c kether V",
    },
    "05-hierophant": {
        "v3a": "A · nested-geometry · judges 3 pts",
        "v3b": "B · enthroned-figure · judges 9 pts · winner",
        "v3c": "C · shrine-symmetry · judges 6 pts",
        "final": "synthesis · v3b base + v3a hexagram + v3c pentagram/child",
    },
}


def card_html(key):
    cfg = cardkit.CONFIGS[key]
    lines, grid = cardkit.load_grid(
        os.path.join(DRAFTS, cfg["txt"]),
        os.path.join(DRAFTS, cfg["classes"]), cfg["default"])
    return cardkit.html_card(lines, grid, cfg["true"])


def block(card):
    labels = LABELS[card]
    cands = "\n".join(
        f'  <figure class="col-ascii"><pre>{card_html(f"{card}-{v}")}</pre>'
        f'<figcaption>{labels[v]}</figcaption></figure>'
        for v in ("v3a", "v3b", "v3c"))
    final = (f'  <figure class="col-ascii"><pre>{card_html(f"{card}-final")}'
             f'</pre><figcaption>{labels["final"]}</figcaption></figure>')
    return (f"<!-- panel:{card} -->\n"
            f'<h3 class="panelhead">~ ultracode panel · 3 candidates ~</h3>\n'
            f'<div class="row panel">\n{cands}\n</div>\n'
            f'<h3 class="panelhead">~ synthesis ~</h3>\n'
            f'<div class="row panel final">\n{final}\n</div>\n'
            f"<!-- /panel:{card} -->")


if __name__ == "__main__":
    card, marker = sys.argv[1], sys.argv[2]
    path = os.path.join(ROOT, "index.html")
    with open(path) as f:
        page = f.read()
    blk = block(card)
    panel_re = re.compile(
        rf"<!-- panel:{re.escape(card)} -->.*?<!-- /panel:{re.escape(card)} -->",
        re.DOTALL)
    if panel_re.search(page):
        page = panel_re.sub(lambda m: blk, page, count=1)
        print(f"{card}: panel refreshed")
    else:
        sec = re.search(
            r"(<!-- =+ " + re.escape(marker) + r" =+ -->.*?)(</section>)",
            page, re.DOTALL)
        if not sec:
            sys.exit(f"section marker {marker!r} not found")
        page = (page[:sec.end(1)] + blk + "\n" + page[sec.end(1):])
        print(f"{card}: panel inserted")
    with open(path, "w") as f:
        f.write(page)
