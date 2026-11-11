"""Recolor the language pie of profile-red.svg to the red palette.

github-profile-3d-contrib paints pie slices and legend swatches with each
language's GitHub color and offers no setting for it, so we swap those colors
after generation. Slices are ranked by first appearance; "other" stays gray.
"""
import re
import sys
from pathlib import Path

RED_RAMP = ["#df2531", "#911820", "#ff5c66", "#640f16", "#b51d28", "#ff8a91"]
OTHER = "#444444"

path = Path(sys.argv[1])
svg = path.read_text(encoding="utf-8")
langs = []
for color in re.findall(r'(?:fill="|fill: )(#[0-9a-fA-F]{6})(?:;)?"\s+class="stroke-bg"', svg):
    if color.lower() != OTHER and color.lower() not in langs:
        langs.append(color.lower())
for i, color in enumerate(langs):
    svg = re.sub(re.escape(color), RED_RAMP[i % len(RED_RAMP)], svg, flags=re.IGNORECASE)
path.write_text(svg, encoding="utf-8")
print(f"recolored {len(langs)} language color(s): {', '.join(langs) or 'none'}")
