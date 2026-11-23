"""Render the Tipline lockup (icon + "Tipline") as the Cal.diy email footer logo.

Cal.diy's EmailBodyLogo shows /emails/logo.png stretched to exactly 89x19 CSS px, so the
PNG must have that aspect ratio. Rendered at 3x (267x57) for sharp display, transparent
background (the footer sits on #F3F4F6). Lockup proportions follow tipline.ai's .lockup:
icon 1em square, gap 12/26 em, weight 600, letter-spacing -0.03em.

Usage: python3 make_email_logo.py <assets-dir> public/emails/logo.png
<assets-dir> holds tipline-icon-256.png (https://tipline.ai/assets/tipline-icon-256.png)
and PlusJakartaSans.ttf (google/fonts: ofl/plusjakartasans/PlusJakartaSans[wght].ttf). Needs Pillow.
"""
import sys
from PIL import Image, ImageDraw, ImageFont

ASSETS = sys.argv[1]
OUT = sys.argv[2]
SCALE = 3
W, H = 89 * SCALE, 19 * SCALE
INK = (11, 12, 14, 255)  # tipline.ai --raised (#0B0C0E): its near-black, for a light background

em = 17 * SCALE  # icon height = 1em, leaves 1px top/bottom at 1x
gap = round(em * 12 / 26)
tracking = -0.03 * em

font = ImageFont.truetype(f"{ASSETS}/PlusJakartaSans.ttf", em)
font.set_variation_by_axes([600])

text = "Tipline"
advances = [font.getlength(ch) + tracking for ch in text]
text_w = sum(advances) - tracking
total_w = em + gap + text_w
x0 = (W - total_w) / 2

img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
icon = Image.open(f"{ASSETS}/tipline-icon-256.png").convert("RGBA").resize((em, em), Image.LANCZOS)
img.alpha_composite(icon, (round(x0), (H - em) // 2))

draw = ImageDraw.Draw(img)
x = x0 + em + gap
for ch, adv in zip(text, advances):
    draw.text((x, H / 2), ch, font=font, fill=INK, anchor="lm")
    x += adv

img.save(OUT, optimize=True)
print(OUT, img.size, f"content width {total_w / SCALE:.1f}px of 89")
