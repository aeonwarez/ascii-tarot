#!/usr/bin/env python3
"""Frame a raw ASCII art file into the standard ascii-tarot card.

Usage:
  python3 frame.py <art.txt> "<TITLE>" "<attribution>" [-o out.txt]

Card spec: 40 cols x variable rows. Interior 37 cols. Art is centered
horizontally as a block. Title bar at the bottom, jgs-style dashes.
Fails loudly if any art line exceeds the interior width or contains
non-printable-ASCII characters.
"""
import sys

W = 37  # default interior width; -w overrides (detailed cards: 47)

# Project palette rule (Stone Story tutorial kit + full jgs kit, per user
# 2026-08-01): art may use ONLY these characters.
BASIC = "`~!^()-_+=;:'\",.\\/|<>[]{}"
EXTENDED = "´‾¡·"  # ´ ‾ ¡ ·
LETTERFORMS = "oOvVTL7UcCxX"      # Stone Story shape letters
JGS_LETTERS = "sSwWmMei6"         # jgs texture/eye letters
JGS_ACCENTS = "*@#%&"             # jgs stars, centers, dense accents
ALLOWED = (set(BASIC) | set(EXTENDED) | set(LETTERFORMS)
           | set(JGS_LETTERS) | set(JGS_ACCENTS) | {" "})


# corner sigils: majors (+) · disks (o) · wands \!/ · cups (~) · swords >+<
SIGILS = {"majors": "(+)", "disks": "(o)", "wands": "\\!/",
          "cups": "(~)", "swords": ">+<"}


def frame(art_lines, title, attrib, W=W, sigil="(+)", numeral=None):
    # trim trailing blank lines, keep internal ones
    while art_lines and not art_lines[-1].strip():
        art_lines.pop()
    while art_lines and not art_lines[0].strip():
        art_lines.pop(0)

    for i, l in enumerate(art_lines, 1):
        # the 'aw' signature is exempt from the palette rule
        bad = sorted({c for c in l.replace("aw", "") if c not in ALLOWED})
        if bad:
            sys.exit(f"line {i}: chars outside palette {bad!r}")
        if len(l.rstrip()) > W:
            sys.exit(f"line {i}: too wide ({len(l.rstrip())} > {W})")

    # center the art as a block: common shift preserving internal alignment
    stripped = [l.rstrip() for l in art_lines]
    maxw = max(len(l) for l in stripped if l) if stripped else 0
    minlead = min((len(l) - len(l.lstrip()) for l in stripped if l.strip()),
                  default=0)
    shift = (W - (maxw - 0)) // 2 - 0
    shift = max(0, (W - maxw + minlead) // 2 - minlead + minlead)  # keep simple
    shift = max(0, (W - maxw) // 2)

    def center(s):
        pad = W - len(s)
        return " " * (pad // 2) + s + " " * (pad - pad // 2)

    # art-deco frame: double side-rails, corner sigil medallions, title plate;
    # the numeral sits in a plaque set into the top rule (as on Harris's cards)
    rule_len = W - 2 * len(sigil)
    if numeral:
        plaque = f"[ {numeral} ]"
        left = (rule_len - len(plaque)) // 2
        rule = "=" * left + plaque + "=" * (rule_len - len(plaque) - left)
    else:
        rule = "=" * rule_len
    out = [".=" + sigil + rule + sigil + "=."]
    out.append("||" + " " * W + "||")
    for l in stripped:
        out.append("||" + (" " * shift + l).ljust(W) + "||")
    out.append("||" + " " * W + "||")
    out.append("|>" + ("- " * (W // 2 + 1))[:W] + "<|")
    out.append("||" + center(title) + "||")
    out.append("||" + center(attrib) + "||")
    out.append("`=" + sigil + "=" * rule_len + sigil + "=´")
    return "\n".join(out) + "\n"


if __name__ == "__main__":
    args = sys.argv[1:]
    out_path, width = None, W
    if "-o" in args:
        i = args.index("-o")
        out_path = args[i + 1]
        del args[i:i + 2]
    if "-w" in args:
        i = args.index("-w")
        width = int(args[i + 1])
        del args[i:i + 2]
    sigil = SIGILS["majors"]
    if "-s" in args:
        i = args.index("-s")
        sigil = SIGILS.get(args[i + 1], args[i + 1])
        del args[i:i + 2]
    numeral = None
    if "-n" in args:
        i = args.index("-n")
        numeral = args[i + 1]
        del args[i:i + 2]
    if len(args) != 3:
        sys.exit(__doc__)
    art_path, title, attrib = args
    with open(art_path) as f:
        art = f.read().splitlines()
    card = frame(art, title, attrib, width, sigil, numeral)
    if out_path:
        with open(out_path, "w") as f:
            f.write(card)
    print(card)
