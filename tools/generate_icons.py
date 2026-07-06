#!/usr/bin/env python3
"""muff1n – App-Icon-Generator.

Erzeugt die PWA-Icons (icons/icon-192.png, icon-512.png, icon-maskable-512.png)
aus dem m-Monogramm auf dem muff1n-Farbverlauf. Passt zur Design-Palette in
styles.css (--accent / --accent-2).

Nutzung:
    pip install pillow
    python tools/generate_icons.py

Farben zentral hier anpassen -> Icons bleiben mit dem App-Design synchron.
"""

import os
from PIL import Image, ImageDraw, ImageFont

# --- Design-Palette (muss zu styles.css passen) ---
ACCENT = (139, 108, 255)   # --accent   #8b6cff
ACCENT_2 = (224, 90, 174)  # --accent-2 #e05aae

OUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "icons")

FONT_CANDIDATES = [
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
]


def load_font(size):
    for path in FONT_CANDIDATES:
        if os.path.exists(path):
            return ImageFont.truetype(path, size)
    return ImageFont.load_default()


def make_icon(size, path, maskable=False):
    """Rendert ein Icon mit 4x-Supersampling für saubere Kanten."""
    s = size * 4
    img = Image.new("RGBA", (s, s), (0, 0, 0, 0))

    pad = 0 if maskable else int(s * 0.06)   # maskable: randlos (Safe-Zone)
    radius = int(s * 0.225)

    # Diagonaler Verlauf accent -> accent_2
    grad = Image.new("RGB", (s, s))
    gd = ImageDraw.Draw(grad)
    for y in range(s):
        t = y / s
        col = tuple(int(ACCENT[i] + (ACCENT_2[i] - ACCENT[i]) * t) for i in range(3))
        gd.line([(0, y), (s, y)], fill=col)

    # Abgerundete Maske
    mask = Image.new("L", (s, s), 0)
    ImageDraw.Draw(mask).rounded_rectangle((pad, pad, s - pad, s - pad), radius=radius, fill=255)
    img.paste(grad, (0, 0), mask)

    # Glanz oben
    gloss = Image.new("L", (s, s), 0)
    ImageDraw.Draw(gloss).rounded_rectangle((pad, pad, s - pad, int(s * 0.5)), radius=radius, fill=40)
    white = Image.new("RGBA", (s, s), (255, 255, 255, 255))
    empty = Image.new("L", (s, s), 0)
    img.paste(white, (0, 0), Image.composite(gloss, empty, mask))

    # Monogramm "m" + kleiner "1"-Akzent
    d = ImageDraw.Draw(img)
    f = load_font(int(s * 0.5))
    bbox = d.textbbox((0, 0), "m", font=f)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    d.text(((s - tw) / 2 - bbox[0], (s - th) / 2 - bbox[1] - int(s * 0.02)),
           "m", font=f, fill=(255, 255, 255, 255))
    d.text((s * 0.62, s * 0.55), "1", font=load_font(int(s * 0.20)), fill=(255, 255, 255, 210))

    img.resize((size, size), Image.LANCZOS).save(path)
    print("wrote", path)


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    make_icon(192, os.path.join(OUT_DIR, "icon-192.png"))
    make_icon(512, os.path.join(OUT_DIR, "icon-512.png"))
    make_icon(512, os.path.join(OUT_DIR, "icon-maskable-512.png"), maskable=True)


if __name__ == "__main__":
    main()
