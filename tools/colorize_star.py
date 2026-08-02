#!/usr/bin/env python3
"""Color maps for the Star card drafts (small 37-col and large 47-col).

Painting is anchored on substrings of the exact framed renders, applied in
order so later tokens override earlier ones. Classes: frame, title, star,
babalon, globe, gold, nuith, silver, fly, rose, crystal, earth, pyramid,
water, sig, sky.

Run directly to emit terminal versions of the small card:
  drafts/17-star-16.ans / drafts/17-star-256.ans
"""
import os, re

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "drafts", "17-star-v2.txt")
LG_SRC = os.path.join(HERE, "..", "drafts", "17-star-lg-v1.txt")

# ---- small card (37-col interior), rows are framed-file rows ----
ROW_TOKENS = {
    2: [(r"\ | /", "babalon")],
    3: [("-==(O)==-", "babalon")],
    4: [(r"/ . \_,-~.", "babalon")],
    5: [("`-._`~.", "babalon")],
    6: [("`-.", "babalon")],
    7: [("(  .-.", "gold")],
    8: [(") (o_)", "gold")],
    9: [(",cCCc.", "nuith"), ("( /", "gold"), ("/", "nuith")],
    10: [("c(-. )/", "nuith")],
    11: [("__", "silver"), (r"/\ _/\ ".rstrip(), "nuith")],
    12: [("( o`./", "silver"), (r"/ (    \ ".rstrip(), "nuith")],
    13: [("`--'\\", "silver"), (r"\  (    )", "nuith")],
    14: [("| |", "silver"), (") )    (", "nuith")],
    15: [("| |", "silver"), (r"( (  \  )", "nuith")],
    16: [("| |", "silver"), (") )  )  )", "nuith")],
    17: [("| |", "silver"), ("( (  (   (__", "nuith")],
    18: [(".__|_|_", "silver"), (r"/ \___\___/", "earth"),
         (r"<>_/\_<>_/\_.", "crystal")],
    19: [("~.~^~.~^~.~^~ aw ~.", "water"), ("aw", "sig")],
}

# large card: per-cell classes come from the compositor's JSON
# (drafts/17-star-lg-classes.json, art coordinates; art starts at framed
# file row 2, col 2)
LG_CLASSES = os.path.join(HERE, "..", "drafts", "17-star-lg-classes.json")

# painted everywhere they occur, after row tokens
GLOBAL_TOKENS = [("}v{", "fly"), ("}i{", "fly"),
                 (",o,", "rose"), (",o,'", "rose"),
                 (",+,", "rose"), (",+,'", "rose")]

PALETTES = {
    "16": {
        "frame": "\033[90m", "title": "\033[37m", "sky": "\033[34m",
        "star": "\033[97m", "babalon": "\033[93m", "globe": "\033[94m",
        "gold": "\033[33m", "nuith": "\033[95m", "silver": "\033[97m",
        "fly": "\033[96m", "rose": "\033[91m", "crystal": "\033[96m",
        "earth": "\033[32m", "pyramid": "\033[37m", "water": "\033[36m",
        "sig": "\033[90m",
    },
    "256": {
        "frame": "\033[38;5;61m", "title": "\033[38;5;250m",
        "sky": "\033[38;5;111m", "star": "\033[38;5;230m",
        "babalon": "\033[38;5;220m", "globe": "\033[38;5;117m",
        "gold": "\033[38;5;214m", "nuith": "\033[38;5;147m",
        "silver": "\033[38;5;253m", "fly": "\033[38;5;123m",
        "rose": "\033[38;5;197m", "crystal": "\033[38;5;87m",
        "earth": "\033[38;5;108m", "pyramid": "\033[38;5;180m",
        "water": "\033[38;5;38m", "sig": "\033[38;5;60m",
    },
}
RESET = "\033[0m"
STAR_GLYPHS = set("*+x.'\"`·")


def paint_classes(lines, row_tokens):
    """Return a per-line list of per-char class labels."""
    nrows = len(lines)
    grid = []
    for r, line in enumerate(lines):
        cls = [None] * len(line)
        right = len(line) - 2
        for c, ch in enumerate(line):
            if r in (0, nrows - 1) or c <= 1 or c >= right:
                cls[c] = "frame"
            elif r >= nrows - 4:
                cls[c] = "title"
        for tok, label in row_tokens.get(r, []):
            i = line.find(tok)
            if i >= 0:
                for c in range(i, i + len(tok)):
                    if cls[c] != "frame":
                        cls[c] = label
        for tok, label in GLOBAL_TOKENS:
            for m in re.finditer(re.escape(tok), line):
                for c in range(m.start(), m.end()):
                    if cls[c] != "frame":
                        cls[c] = label
        for c, ch in enumerate(line):
            if cls[c] is None and ch != " ":
                cls[c] = "star" if ch in STAR_GLYPHS else "sky"
        grid.append(cls)
    return grid


def load(card="small"):
    if card == "small":
        with open(SRC) as f:
            lines = f.read().splitlines()
        return lines, paint_classes(lines, ROW_TOKENS)
    # large: framed render + compositor class map
    import json
    with open(LG_SRC) as f:
        lines = f.read().splitlines()
    with open(LG_CLASSES) as f:
        art = json.load(f)
    nrows = len(lines)
    grid = []
    for r, line in enumerate(lines):
        cls = [None] * len(line)
        right = len(line) - 2
        for c, ch in enumerate(line):
            if r in (0, nrows - 1) or c <= 1 or c >= right:
                cls[c] = "frame"
            elif r >= nrows - 4:
                cls[c] = "title"
            elif 2 <= r < 2 + len(art) and 0 <= c - 2 < len(art[r - 2]):
                cls[c] = art[r - 2][c - 2] or ("sky" if ch != " " else None)
            elif ch != " ":
                cls[c] = "sky"
        grid.append(cls)
    return lines, grid


def colorize(lines, grid, pal):
    out = []
    for line, cls in zip(lines, grid):
        row, cur = [], None
        for c, ch in enumerate(line):
            if ch != " " and cls[c] != cur:
                row.append(pal[cls[c]])
                cur = cls[c]
            row.append(ch)
        row.append(RESET)
        out.append("".join(row))
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    for card, stem in (("small", "17-star"), ("large", "17-star-lg")):
        lines, grid = load(card)
        for name, pal in PALETTES.items():
            path = os.path.join(HERE, "..", "drafts", f"{stem}-{name}.ans")
            with open(path, "w") as f:
                f.write(colorize(lines, grid, pal))
            print(f"wrote {stem}-{name}.ans")
