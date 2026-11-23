#!/usr/bin/env python3
"""The World Today - front page for Monday 23 November 2026.

Deterministic renderer: no network, no randomness, no timestamps.
Draws a 1024x1024 newspaper front page with eight verified stories
from 23 November 2026, every illustration drawn from code.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 241, 230)
INK = (17, 17, 17)
RED = (176, 30, 30)
BLUE = (31, 78, 121)
GREY = (110, 105, 95)
LIGHT = (232, 226, 212)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"


def font(name, size):
    return ImageFont.truetype(os.path.join(FONT_DIR, name), size)


SERIF_B = lambda s: font("DejaVuSerif-Bold.ttf", s)
SERIF = lambda s: font("DejaVuSerif.ttf", s)
SANS_B = lambda s: font("DejaVuSans-Bold.ttf", s)
SANS = lambda s: font("DejaVuSans.ttf", s)
SANS_I = lambda s: font("DejaVuSans.ttf", s)  # no oblique face shipped; regular sans


def wrap(draw, text, fnt, max_w):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def para(draw, x, y, text, fnt, max_w, leading, color=INK):
    for line in wrap(draw, text, fnt, max_w):
        draw.text((x, y), line, font=fnt, fill=color)
        y += leading
    return y


def rule(draw, x0, x1, y, width=2, color=INK):
    draw.line([(x0, y), (x1, y)], fill=color, width=width)


# ---------------------------------------------------------------- illustrations
def draw_globe(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    cx, cy, r = x + w // 2, y + h // 2 + 8, 96
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(52, 120, 180),
              outline=(20, 60, 110), width=3)
    d.ellipse([cx - 62, cy - 58, cx - 8, cy - 6], fill=(74, 150, 80))
    d.ellipse([cx - 12, cy + 18, cx + 66, cy + 66], fill=(74, 150, 80))
    d.ellipse([cx + 28, cy - 72, cx + 78, cy - 22], fill=(74, 150, 80))
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(200, 225, 240), width=2)
    d.arc([cx - r, cy - r, cx + r, cy + r], 20, 160, fill=(200, 225, 240), width=2)
    d.line([(cx - r, cy), (cx + r, cy)], fill=(200, 225, 240), width=2)
    crack = [(cx + 6, cy - 88), (cx - 12, cy - 52), (cx + 14, cy - 18),
             (cx - 16, cy + 22), (cx + 8, cy + 58), (cx - 6, cy + 92)]
    d.line(crack, fill=(176, 30, 30), width=6, joint="curve")
    d.ellipse([x + w - 52, y + 10, x + w - 12, y + 50], fill=(240, 140, 40))
    for a in range(8):
        import math
        ang = a * math.pi / 4
        sx, sy = x + w - 32 + 30 * math.cos(ang), y + 30 + 30 * math.sin(ang)
        ex, ey = x + w - 32 + 40 * math.cos(ang), y + 30 + 40 * math.sin(ang)
        d.line([(sx, sy), (ex, ey)], fill=(240, 140, 40), width=3)


def draw_capitol(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(226, 232, 238))
    d.rectangle([x + 10, y + 8, x + 74, y + 30], fill=(176, 30, 30))
    d.text((x + 18, y + 13), "258", font=SANS_B(16), fill=(255, 255, 255))
    d.text((x + 80, y + 12), "SEATS", font=SANS_B(15), fill=(31, 78, 121))
    d.rectangle([x + 90, y + 88, x + 292, y + 96], fill=(90, 90, 90))
    d.rectangle([x + 100, y + 70, x + 282, y + 78], fill=(245, 245, 240))
    for i in range(6):
        cx = x + 116 + i * 28
        d.line([(cx, y + 78), (cx, y + 88)], fill=(120, 120, 120), width=3)
    d.pieslice([x + 160, y + 34, x + 222, y + 72], 180, 360, fill=(245, 245, 240),
               outline=(90, 90, 90), width=2)
    d.rectangle([x + 186, y + 22, x + 196, y + 36], fill=(245, 245, 240))
    d.line([(x + 191, y + 10), (x + 191, y + 22)], fill=(60, 60, 60), width=3)
    d.polygon([(x + 191, y + 10), (x + 209, y + 14), (x + 191, y + 18)],
              fill=(176, 30, 30))


def draw_handcuffs(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 44, 52))
    d.rectangle([x + 86, y + 6, x + 226, y + 26], fill=(176, 30, 30))
    d.text((x + 96, y + 10), "FBI MOST WANTED", font=SANS_B(13), fill=(255, 255, 255))
    d.text((x + 20, y + 30), "SINALOA, MEXICO", font=SANS_B(13), fill=(220, 220, 220))
    d.ellipse([x + 56, y + 44, x + 116, y + 100], outline=(200, 200, 200), width=8)
    d.ellipse([x + 196, y + 44, x + 256, y + 100], outline=(200, 200, 200), width=8)
    d.line([(x + 116, y + 72), (x + 196, y + 72)], fill=(200, 200, 200), width=6)
    d.ellipse([x + 148, y + 64, x + 164, y + 80], fill=(200, 200, 200))


def draw_ship(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(214, 232, 240))
    d.ellipse([x + 30, y + 6, x + 66, y + 34], fill=(140, 140, 140))
    d.ellipse([x + 56, y + 2, x + 88, y + 28], fill=(160, 160, 160))
    d.polygon([(x + 226, y + 50), (x + 240, y + 24), (x + 254, y + 50)],
              fill=(240, 120, 20))
    d.ellipse([x + 228, y + 8, x + 248, y + 28], fill=(240, 160, 40))
    d.rectangle([x + 66, y + 50, x + 104, y + 68], fill=(31, 78, 121))
    d.rectangle([x + 110, y + 50, x + 148, y + 68], fill=(200, 120, 40))
    d.rectangle([x + 154, y + 50, x + 192, y + 68], fill=(74, 150, 80))
    d.rectangle([x + 198, y + 56, x + 226, y + 68], fill=(230, 230, 230))
    d.polygon([(x + 28, y + 68), (x + 56, y + 68), (x + 48, y + 92),
               (x + 262, y + 92), (x + 284, y + 68), (x + 252, y + 68)],
              fill=(120, 60, 50))
    for i in range(4):
        wx = x + 20 + i * 72
        d.arc([wx, y + 92, wx + 56, y + 100], 180, 360, fill=(31, 78, 121), width=3)


def draw_factory(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(240, 228, 210))
    d.ellipse([x + 240, y + 4, x + 272, y + 30], fill=(150, 150, 150))
    d.ellipse([x + 262, y + 0, x + 290, y + 22], fill=(170, 170, 170))
    d.polygon([(x + 56, y + 52), (x + 72, y + 26), (x + 88, y + 52)],
              fill=(240, 120, 20))
    d.polygon([(x + 92, y + 52), (x + 112, y + 20), (x + 132, y + 52)],
              fill=(240, 160, 40))
    d.polygon([(x + 136, y + 52), (x + 152, y + 30), (x + 168, y + 52)],
              fill=(240, 120, 20))
    d.rectangle([x + 28, y + 52, x + 222, y + 100], fill=(150, 90, 70))
    d.rectangle([x + 28, y + 52, x + 222, y + 60], fill=(110, 60, 50))
    d.rectangle([x + 228, y + 22, x + 246, y + 100], fill=(120, 120, 120))
    for i in range(4):
        d.rectangle([x + 44 + i * 44, y + 68, x + 70 + i * 44, y + 88],
                    fill=(240, 200, 60))


def draw_chart(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255))
    d.line([(x + 30, y + 12), (x + 30, y + h - 14)], fill=(60, 60, 60), width=2)
    d.line([(x + 30, y + h - 14), (x + w - 16, y + h - 14)], fill=(60, 60, 60), width=2)
    pts = [(x + 44, y + 24), (x + 92, y + 32), (x + 140, y + 28),
           (x + 188, y + 48), (x + 236, y + 66), (x + 272, y + 80)]
    for i in range(len(pts) - 1):
        d.line([pts[i], pts[i + 1]], fill=(176, 30, 30), width=5)
    for p in pts:
        d.ellipse([p[0] - 5, p[1] - 5, p[0] + 5, p[1] + 5], fill=(176, 30, 30))
    d.polygon([(x + 272, y + 80), (x + 292, y + 74), (x + 288, y + 94)],
              fill=(176, 30, 30))
    d.text((x + 40, y + h - 24), "-3.7%", font=SANS_B(15), fill=(176, 30, 30))
    d.text((x + 190, y + 8), "S&P 500", font=SANS_B(13), fill=(90, 90, 90))


def draw_cricket(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(196, 222, 170))
    d.text((x + 190, y + 10), "720/9d", font=SANS_B(26), fill=(31, 78, 121))
    d.polygon([(x + 112, y + 12), (x + 132, y + 20), (x + 106, y + 90),
               (x + 86, y + 82)], fill=(210, 180, 120), outline=(120, 90, 50))
    d.polygon([(x + 102, y + 86), (x + 110, y + 90), (x + 96, y + 102),
               (x + 88, y + 98)], fill=(180, 150, 100))
    d.ellipse([x + 208, y + 58, x + 248, y + 98], fill=(176, 30, 30))
    d.arc([x + 208, y + 58, x + 248, y + 98], 60, 300, fill=(255, 255, 255), width=2)
    for i, sx in enumerate((x + 34, x + 50, x + 66)):
        d.line([(sx, y + 66), (sx, y + 98)], fill=(230, 200, 60), width=5)
    d.line([(x + 32, y + 64), (x + 72, y + 64)], fill=(230, 200, 60), width=4)


def draw_tennis(d, x, y, w, h):
    # small strip illustration, fits a 180x48 box
    d.rectangle([x, y, x + w, y + h], fill=(60, 120, 90))
    d.rectangle([x + 6, y + 5, x + w - 6, y + h - 5], outline=(255, 255, 255), width=2)
    d.line([(x + w // 2, y + 5), (x + w // 2, y + h - 5)], fill=(255, 255, 255), width=2)
    d.ellipse([x + 18, y + 8, x + 52, y + 40], outline=(220, 220, 220), width=4)
    d.line([(x + 52, y + 24), (x + 76, y + 40)], fill=(220, 220, 220), width=4)
    d.ellipse([x + 128, y + 12, x + 156, y + 40], fill=(210, 220, 60),
              outline=(255, 255, 255), width=2)


STORIES = [
    dict(kicker="CLIMATE — ANTALYA, TURKEY", source="Reuters",
         art=draw_globe, lead=True,
         head="COP31 collapses with no deal",
         body="UN climate talks end in failure after the EU rejects a final draft that omits fossil fuels — the first time talks have collapsed since Copenhagen in 2009."),
    dict(kicker="UNITED STATES", source="Associated Press", art=draw_capitol,
         head="Democrats win 258 House seats",
         body="The party's biggest House majority since 1992 sets up divided government under a Republican president."),
    dict(kicker="MEXICO", source="Associated Press", art=draw_handcuffs,
         head="'El Chapo Isidro' captured",
         body="Mexico seizes FBI most-wanted cartel boss Fausto Isidro Meza Flores in a Sinaloa raid that leaves 11 dead."),
    dict(kicker="EUROPE & AFRICA", source="Reuters", art=draw_ship,
         head="Russian ships hit in two seas",
         body="A cargo ship burns off Finland and a vessel is struck in Libya's Benghazi port in suspected drone attacks."),
    dict(kicker="INDONESIA", source="Reuters", art=draw_factory,
         head="Factory fire: 50 missing in Java",
         body="Seven body bags are recovered after a blaze tears through a candy factory in Banten; rescuers search for dozens."),
    dict(kicker="MARKETS", source="Associated Press", art=draw_chart,
         head="AI stocks drag Wall Street down",
         body="The S&P 500 falls 3.7% in its worst week in 18 months as investors doubt AI spending will pay off soon."),
    dict(kicker="SPORT — CRICKET", source="Associated Press", art=draw_cricket,
         head="India's record 720 in Wellington",
         body="India declares on 720 for 9, a record total, on day four of the first Test against New Zealand."),
    dict(kicker="SPORT — TENNIS", source="Reuters", art=draw_tennis,
         head="Alcaraz wins ATP Finals",
         body="Carlos Alcaraz beats world No. 1 Alexander Zverev."),
]


def main():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    mx = 28
    # --- masthead
    rule(d, mx, W - mx, 16, 3)
    rule(d, mx, W - mx, 22, 1)
    title = "The World Today"
    tw = d.textlength(title, font=SERIF_B(64))
    d.text(((W - tw) / 2, 30), title, font=SERIF_B(64), fill=INK)
    date = "MONDAY 23 NOVEMBER 2026"
    dw = d.textlength(date, font=SANS_B(21))
    d.text(((W - dw) / 2, 108), date, font=SANS_B(21), fill=RED)
    sub = "EIGHT STORIES FROM AROUND THE WORLD  •  ALL REPORTED TODAY"
    sw = d.textlength(sub, font=SANS_B(12))
    d.text(((W - sw) / 2, 138), sub, font=SANS_B(12), fill=GREY)
    rule(d, mx, W - mx, 160, 2)

    # --- lead story
    lead = STORIES[0]
    lx, ly = mx, 176
    d.text((lx, ly), lead["kicker"], font=SANS_B(14), fill=RED)
    y = para(d, lx, ly + 26, lead["head"], SERIF_B(33), 590, 40)
    y = para(d, lx, y + 8, lead["body"], SANS(16), 590, 22)
    d.text((lx, y + 10), "Source: " + lead["source"], font=SANS_I(12), fill=GREY)
    lead["art"](d, 648, 176, 348, 268)
    rule(d, mx, W - mx, 462, 2)

    # --- seven more stories: two rows of three, then one wide strip
    cols = [mx, 356, 684]
    cw = 312
    rows = [(478, 0), (726, 3)]
    for (ry, start) in rows:
        for i in range(3):
            s = STORIES[1 + start + i]
            cx = cols[i]
            s["art"](d, cx, ry, cw, 100)
            d.text((cx, ry + 108), s["kicker"], font=SANS_B(11), fill=RED)
            y = para(d, cx, ry + 126, s["head"], SERIF_B(17), cw, 21)
            y = para(d, cx, y + 3, s["body"], SANS(12), cw, 16)
            d.text((cx, y + 3), "Source: " + s["source"], font=SANS_I(10), fill=GREY)
        if start == 0:
            rule(d, mx, W - mx, 710, 1, GREY)
    # --- seventh story as a bottom strip
    s = STORIES[7]
    sy = 960
    s["art"](d, mx, sy, 180, 48)
    d.text((226, sy), s["kicker"], font=SANS_B(11), fill=RED)
    d.text((226, sy + 17), s["head"] + " — " + s["body"], font=SANS_B(13), fill=INK)
    d.text((226, sy + 36), "Source: " + s["source"], font=SANS_I(10), fill=GREY)
    rule(d, mx, W - mx, 1010, 2)
    img.save("entry.png", optimize=True)
    print("wrote entry.png", img.size)


if __name__ == "__main__":
    main()
