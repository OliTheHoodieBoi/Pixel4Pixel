from PIL import Image
import os

with Image.open("in.png") as im:
    pixels = im.getdata()
    size = im.size
lines: list[str] = []

lines.append(f'<svg width="{size[0]}" height="{size[1]}">')
for i, rgba in enumerate(pixels):
    if rgba[3] == 0:
        continue

    x = i % size[0]
    y = i // size[0]
    lines.append(f'    <rect fill="rgba{rgba}" x="{x}" y="{y}" width="1" height="1" stroke="rgba{rgba}" stroke-width="0.1" />')
lines.append('</svg>')

with open('out.svg', 'w') as f:
    f.write('\n'.join(lines))