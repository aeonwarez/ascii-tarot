#!/usr/bin/env python3
"""Shared card rendering kit: framed-txt + classes-json -> HTML spans / ANSI.

Each card registers a config: files, default class, truecolor palette,
optional 256/16 palettes (derived crudely from truecolor when absent).
Usage:
  python3 cardkit.py <card>        emit preview html + .ans files for card
Cards register in CONFIGS below (star/fool/moon keep their legacy modules).
"""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__))
DRAFTS = os.path.join(HERE, "..", "drafts")
RESET = "\033[0m"


def load_grid(txt_path, classes_path, default_cls):
    with open(txt_path) as f:
        lines = f.read().splitlines()
    with open(classes_path) as f:
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
                cls[c] = art[r - 2][c - 2] or (default_cls if ch != " " else None)
            elif ch != " ":
                cls[c] = default_cls
        grid.append(cls)
    return lines, grid


def esc(ch):
    return ch.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def html_card(lines, grid, pal):
    out = []
    for line, cls in zip(lines, grid):
        row, cur, buf = [], None, []
        for c, ch in enumerate(line):
            k = cls[c] if ch != " " else cur
            if k != cur and buf:
                row.append(f'<span style="color:{pal[cur]}">{"".join(buf)}</span>'
                           if cur else "".join(buf))
                buf = []
            cur = k if ch != " " else cur
            buf.append(esc(ch))
        if buf:
            row.append(f'<span style="color:{pal[cur]}">{"".join(buf)}</span>'
                       if cur else "".join(buf))
        out.append("".join(row))
    return "\n".join(out)


def ans_card(lines, grid, pal):
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


def hex_to_256(h):
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    if abs(r - g) < 12 and abs(g - b) < 12:
        v = (r + g + b) // 3
        idx = 232 + min(23, max(0, (v - 8) // 10))
    else:
        idx = (16 + 36 * round(r / 51) + 6 * round(g / 51) + round(b / 51))
    return f"\033[38;5;{idx}m"


def hex_to_16(h):
    r, g, b = (int(h[i:i + 2], 16) for i in (1, 3, 5))
    bright = max(r, g, b) > 170
    base = (1 if r > g and r > b else
            2 if g > r and g > b else
            4 if b > r and b > g else
            3 if r > 150 and g > 150 else 7)
    if abs(r - g) < 25 and abs(g - b) < 25:
        base = 7 if bright else 0 if max(r, g, b) < 90 else 7
        return f"\033[{90 + base if bright else 30 + base}m" if base else "\033[90m"
    if r > 150 and g > 150 and b < 120:
        base = 3
    return f"\033[{(90 if bright else 30) + base}m"


def preview_page(title, img, card_html, heb):
    return f"""<!DOCTYPE html>
<html><head><meta charset="utf-8"><title>{title}</title>
<style>
  body {{ background: #000; margin: 2rem; display: flex; flex-direction: row;
         justify-content: center; align-items: flex-start; gap: 3rem;
         flex-wrap: wrap; }}
  figure {{ margin: 0; }}
  img {{ max-height: 44rem; border-radius: 8px; }}
  pre {{ font-family: "Courier New", Courier, monospace; font-weight: bold;
        font-size: 15px; line-height: 1.2; }}
  figcaption {{ color: #666; font-family: monospace; text-align: center;
               margin-top: .8rem; }}
</style></head><body>
<figure><img src="../reference/{img}" alt="{title} (Harris)">
<figcaption>Harris original (reference)</figcaption></figure>
<figure><pre>{card_html}</pre>
<figcaption>{heb} · ascii-tarot truecolor (after jgs)</figcaption></figure>
</body></html>
"""


def emit(card, cfg):
    lines, grid = load_grid(
        os.path.join(DRAFTS, cfg["txt"]), os.path.join(DRAFTS, cfg["classes"]),
        cfg["default"])
    pal = cfg["true"]
    html = html_card(lines, grid, pal)
    out_html = os.path.join(DRAFTS, f"{card}-preview.html")
    with open(out_html, "w") as f:
        f.write(preview_page(cfg["title"], cfg["img"], html, cfg["heb"]))
    pal256 = {k: hex_to_256(v) for k, v in pal.items()}
    pal16 = {k: hex_to_16(v) for k, v in pal.items()}
    for name, p in (("256", pal256), ("16", pal16)):
        with open(os.path.join(DRAFTS, f"{card}-lg-{name}.ans"), "w") as f:
            f.write(ans_card(lines, grid, p))
    print(f"emitted {card}: preview + 16/256 ans")


_STAR_TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "sky": "#7a6fc0", "star": "#f0ecff", "babalon": "#e8e4f8",
    "globe": "#d9a0b8", "gold": "#c9a23a", "nuith": "#b8c4e8",
    "silver": "#a8d4e0", "fly": "#c09040", "rose": "#8f2f3f",
    "crystal": "#c8c0e0", "earth": "#b8a8c8", "pyramid": "#c090a8",
    "water": "#8fa8c8", "sig": "#55558a",
}

def _star_cfg(stem):
    return {
        "txt": f"{stem}-lg-v1.txt", "classes": f"{stem}-lg-classes.json",
        "img": "17-star-card.jpg", "title": "XVII . The Star",
        "heb": "&#x5D4;", "default": "sky", "true": dict(_STAR_TRUE),
    }

_FOOL_TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "bg": "#c9a840", "sky": "#6a8fd4", "ring0": "#d8d8e8",
    "ring1": "#c8a8d8", "ring2": "#a8d8c8", "fool": "#4a9950",
    "gold": "#e8c84a", "sun": "#ffaf2a", "flower": "#d8e8f5",
    "dove": "#f0f0f8", "fly": "#e09520", "tiger": "#e87830",
    "croc": "#6a8f4a", "grapes": "#3a5a8f", "coins": "#a8c8e0",
    "sig": "#8a7a4a",
    # rainbow vortex bands (fable5: warm core -> blue -> red -> violet)
    "vy": "#f5c842", "vo": "#f09838", "vb": "#5878d0",
    "vr": "#d85040", "vv": "#9a70d0", "vg": "#68b060",
    "water": "#8fa8c8", "dew": "#f5f0dc",
}

def _fool_cfg(stem):
    return {
        "txt": f"{stem}-lg-v1.txt", "classes": f"{stem}-lg-classes.json",
        "img": "00-fool-card.jpg", "title": "0 . The Fool",
        "heb": "&#x5D0;", "default": "bg", "true": dict(_FOOL_TRUE),
    }

_MAGUS_TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "field": "#3a5a80", "rays": "#4a7a9a", "indigo": "#3a3a68",
    "kether": "#f0eef8", "lilac": "#c8b8d8", "web": "#8fa8c8",
    "figure": "#e8c040", "gold": "#ffd75a", "caduceus": "#e0b040",
    "serpent": "#c8a030", "wings": "#e09520", "dove": "#f0f0f8",
    "ape": "#9a9a7a", "obj": "#e8d08a", "flame": "#f09838",
    "egg": "#d8d8e8", "sun": "#ffd700", "sig": "#55558a",
}

def _magus_cfg(stem):
    return {
        "txt": f"{stem}-lg-v1.txt", "classes": f"{stem}-lg-classes.json",
        "img": "01-magus-card.jpg", "title": "I . The Magus",
        "heb": "&#x5D1;", "default": "field", "true": dict(_MAGUS_TRUE),
    }

_HIER_TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "field": "#2a3a6a", "stars": "#c8d0f0",
    "robe": "#c23a2a", "orange": "#e07038", "face": "#e8b890",
    "crown": "#e0c04a", "hex": "#e8d44a", "penta": "#f0ecd8",
    "child": "#a8d8c8", "woman": "#e8d0d8", "sword": "#c8c8d8",
    "moon": "#d8d8e8", "bull": "#8a6a4a", "throne": "#7a5a3a",
    "olive": "#8a8a5a", "eleph": "#c8874a", "kerub": "#d8c090",
    "oriel": "#c8b8d8", "rose": "#d87a8a", "snake": "#68b060",
    "dove": "#f0f0f8", "nails": "#c8c8d8", "wand": "#e0c04a",
    "ringr": "#d85040", "ringg": "#68b060", "ringy": "#e8e0a0",
    "sig": "#55558a",
}

def _hier_cfg(stem):
    return {
        "txt": f"{stem}-lg-v1.txt", "classes": f"{stem}-lg-classes.json",
        "img": "05-hierophant-card.jpg", "title": "V . The Hierophant",
        "heb": "&#x5D5;", "default": "field", "true": dict(_HIER_TRUE),
    }

_MOON_TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "moon": "#e8d8a0", "blood": "#c23a4a", "tower": "#4a5288",
    "cone": "#b8c8d8", "anubis": "#d4884a", "jackal": "#7a7a8a",
    "flame": "#e07840", "water": "#8a98b0", "wavered": "#c25a5a",
    "waveblue": "#5a78c2", "aura": "#e8ce7a", "sun": "#ffaf2a",
    "scarab": "#9a9aa8", "sig": "#55558a",
}

def _moon_cfg(stem):
    return {
        "txt": f"{stem}-lg-v1.txt", "classes": f"{stem}-lg-classes.json",
        "img": "18-moon-card.jpg", "title": "XVIII . The Moon",
        "heb": "&#x5E7;", "default": "tower", "true": dict(_MOON_TRUE),
    }

_PRIESTESS_TRUE = {
    "frame": "#8f8fb8", "title": "#c8c8d8",
    "veil": "#cfe8f0", "lattice": "#9fd8e8", "field": "#3a5aa8",
    "figure": "#f0ecd8", "crown": "#cfd85a", "wings": "#8fd8c8",
    "cup": "#e8ce7a", "pillar": "#6a78b8", "camel": "#f5f5f5",
    "crystal": "#d8c8e8", "flower": "#b08a6a", "cone": "#6a9950",
    "grapes": "#8a5fb8", "shell": "#e0c04a", "pyramid": "#e09a9a",
    "sig": "#55558a",
}

def _priestess_cfg(stem):
    return {
        "txt": f"{stem}-lg-v1.txt", "classes": f"{stem}-lg-classes.json",
        "img": "02-priestess-card.jpg", "title": "II . The Priestess",
        "heb": "&#x5D2;", "default": "veil", "true": dict(_PRIESTESS_TRUE),
    }

CONFIGS = {
    # Star baseline + ultracode-panel candidate slots
    "17-star": _star_cfg("17-star"),
    "17-star-v3a": _star_cfg("17-star-v3a"),
    "17-star-v3b": _star_cfg("17-star-v3b"),
    "17-star-v3c": _star_cfg("17-star-v3c"),
    "17-star-final": _star_cfg("17-star-final"),
    # Fool baseline + ultracode-panel candidate slots + synthesis
    "00-fool": _fool_cfg("00-fool"),
    "00-fool-v3a": _fool_cfg("00-fool-v3a"),
    "00-fool-v3b": _fool_cfg("00-fool-v3b"),
    "00-fool-v3c": _fool_cfg("00-fool-v3c"),
    "00-fool-final": _fool_cfg("00-fool-final"),
    # Magus panel slots
    "01-magus": _magus_cfg("01-magus"),
    "01-magus-v3a": _magus_cfg("01-magus-v3a"),
    "01-magus-v3b": _magus_cfg("01-magus-v3b"),
    "01-magus-v3c": _magus_cfg("01-magus-v3c"),
    "01-magus-final": _magus_cfg("01-magus-final"),
    # Hierophant panel slots (no reference scan yet; palette from the prompt)
    "05-hierophant": _hier_cfg("05-hierophant"),
    "05-hierophant-v3a": _hier_cfg("05-hierophant-v3a"),
    "05-hierophant-v3b": _hier_cfg("05-hierophant-v3b"),
    "05-hierophant-v3c": _hier_cfg("05-hierophant-v3c"),
    "05-hierophant-final": _hier_cfg("05-hierophant-final"),
    # Priestess baseline + panel slots
    "02-priestess": _priestess_cfg("02-priestess"),
    "02-priestess-v3a": _priestess_cfg("02-priestess-v3a"),
    "02-priestess-v3b": _priestess_cfg("02-priestess-v3b"),
    "02-priestess-v3c": _priestess_cfg("02-priestess-v3c"),
    "02-priestess-final": _priestess_cfg("02-priestess-final"),
    # Moon baseline + panel slots (palette ported from legacy moon_html.py)
    "18-moon": _moon_cfg("18-moon"),
    "18-moon-v3a": _moon_cfg("18-moon-v3a"),
    "18-moon-v3b": _moon_cfg("18-moon-v3b"),
    "18-moon-v3c": _moon_cfg("18-moon-v3c"),
    "18-moon-final": _moon_cfg("18-moon-final"),
    "03-empress": {
        "txt": "03-empress-lg-v1.txt", "classes": "03-empress-lg-classes.json",
        "img": "03-empress-card.jpg", "title": "III . The Empress",
        "heb": "&#x5D3;", "default": "field",
        "true": {
            "frame": "#8f8fb8", "title": "#c8c8d8",
            "field": "#69a860", "arch": "#5a88c8", "reeds": "#4a78b8",
            "crown": "#5a9950", "cross": "#e0c04a", "face": "#e8cdb0",
            "hair": "#e8e0d0", "blouse": "#d86a6a", "lotus": "#5a78d8",
            "stems": "#69a860", "skirt": "#69b868", "belt": "#e0c04a",
            "moon": "#b8b8c8", "throne": "#5a88c8", "pelican": "#f0ece0",
            "shield": "#d8d060", "eagle": "#f5f5ef", "rose": "#f0e8e8",
            "floor": "#4a9a98", "fleur": "#8fb8d8", "bird": "#c8c8d8",
            "sig": "#55558a",
        },
    },
    "04-emperor": {
        "txt": "04-emperor-lg-v1.txt", "classes": "04-emperor-lg-classes.json",
        "img": "04-emperor-card.jpg", "title": "IV . The Emperor",
        "heb": "&#x5E6;", "default": "field",
        "true": {
            "frame": "#8f8fb8", "title": "#c8c8d8",
            "field": "#c23a2a", "flames": "#e05a3a", "sunrays": "#ffc832",
            "cross": "#ffd700",
            "ram": "#e8d0c0", "crown": "#ffc832", "face": "#e8b890",
            "robe": "#c8452a", "pattern": "#e8a04a", "sceptre": "#e0c04a",
            "light": "#f0f0e8", "orb": "#a82a3a", "star": "#ffd700",
            "skin": "#e8b890", "shield": "#e8d44a", "eagle": "#c85a2a",
            "lamb": "#f0ecd8", "floor": "#8a2a30", "fleur": "#e0a84a",
            "sig": "#55558a",
        },
    },
}

if __name__ == "__main__":
    import sys
    card = sys.argv[1]
    emit(card, CONFIGS[card])
