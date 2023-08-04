from PIL import Image, UnidentifiedImageError
import os
import argparse

parser = argparse.ArgumentParser('Pixel4Pixel', description='Convert an image to ')
parser.add_argument('filename', help='provide an image to convert')

args = parser.parse_args()
path = args.filename

try:
    with Image.open(path) as im:
        pixels = im.getdata()
        size = im.size
except FileNotFoundError:
    print("File does not exist")
    exit()
except UnidentifiedImageError:
    print("Could not open image")
    exit()

lines: list[str] = []
lines.append(f'<svg width="{size[0]}" height="{size[1]}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">')
for i, rgba in enumerate(pixels):
    x = i % size[0]
    y = i // size[0]

    if len(rgba) > 3 and rgba[3] < 255:
        if rgba[3] == 0:
            continue
        lines.append(f'    <rect fill="rgba{rgba}" x="{x}" y="{y}" width="1" height="1" stroke="rgba{rgba}" stroke-width="0.1" />')
    else:
        rgb = rgba[:3]
        lines.append(f'    <rect fill="rgb{rgb}" x="{x}" y="{y}" width="1" height="1" stroke="rgb{rgb}" stroke-width="0.1" />')

lines.append('</svg>')

with open(path + '.svg', 'w') as f:
    f.write('\n'.join(lines))
