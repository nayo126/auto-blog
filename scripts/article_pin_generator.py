#!/usr/bin/env python3
"""記事用 Pinterest Pin 自動生成 (1000x1500 縦長)。

PIL only、外部API不要。各記事の title + category から
Pinterest最適サイズの縦長Pinを生成。
public/pins/{slug}.png に保存。

Pinterest高CTR要素を全て反映:
- 文字密度高め、3-5行
- 数字を強調（赤色オーバーレイ）
- カテゴリチップ
- サイトロゴ（小さく）
"""
from __future__ import annotations
import json
import re
import random
from datetime import datetime
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"
PIN_DIR = ROOT / "site" / "public" / "pins"
LOG = ROOT / "logs" / "pins.log"
PIN_DIR.mkdir(parents=True, exist_ok=True)
LOG.parent.mkdir(exist_ok=True)

FONT_BOLD = "/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc"
FONT_HEAVY = "/System/Library/Fonts/ヒラギノ角ゴシック W8.ttc"
FONT_FALLBACK = "/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc"

SIZE = (1000, 1500)
SITE_NAME = "AI副業ラボ"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    try:
        return ImageFont.truetype(path, size)
    except OSError:
        return ImageFont.truetype(FONT_FALLBACK, size)


def parse_fm(text: str) -> dict:
    if not text.startswith("---"):
        return {}
    m = re.match(r"^---\s*\n(.*?)\n---", text, re.DOTALL)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    lines: list[str] = []
    line = ""
    for char in text:
        test = line + char
        bbox = font.getbbox(test)
        w = bbox[2] - bbox[0]
        if w > max_width and line:
            lines.append(line)
            line = char
        else:
            line = test
    if line:
        lines.append(line)
    return lines


def color_palette(slug: str) -> dict:
    """Pinterest映えするカラーパレット。slug由来で安定。"""
    palettes = [
        # warm orange (highest engagement on pinterest per studies)
        {"bg_top": (252, 196, 99), "bg_bot": (228, 86, 71), "fg": (40, 20, 10), "accent": (200, 30, 30)},
        # mint+pink (female demographic, high save rate)
        {"bg_top": (255, 215, 220), "bg_bot": (180, 225, 215), "fg": (40, 30, 50), "accent": (220, 60, 100)},
        # dark navy + gold (professional)
        {"bg_top": (20, 30, 60), "bg_bot": (80, 70, 130), "fg": (255, 255, 255), "accent": (255, 200, 50)},
        # forest green (calm, productivity)
        {"bg_top": (40, 80, 60), "bg_bot": (140, 180, 130), "fg": (255, 255, 255), "accent": (255, 200, 80)},
        # rose gold
        {"bg_top": (240, 200, 200), "bg_bot": (220, 140, 130), "fg": (60, 30, 30), "accent": (180, 40, 80)},
        # deep purple
        {"bg_top": (60, 30, 80), "bg_bot": (130, 80, 160), "fg": (255, 240, 200), "accent": (255, 100, 150)},
    ]
    h = sum(ord(c) for c in slug)
    return palettes[h % len(palettes)]


def make_gradient(size: tuple[int, int], top, bot) -> Image.Image:
    img = Image.new("RGB", size, top)
    draw = ImageDraw.Draw(img)
    w, h = size
    for y in range(h):
        t = y / h
        r = int(top[0] * (1 - t) + bot[0] * t)
        g = int(top[1] * (1 - t) + bot[1] * t)
        b = int(top[2] * (1 - t) + bot[2] * t)
        draw.line([(0, y), (w, y)], fill=(r, g, b))
    return img


def find_number(text: str) -> tuple[str, tuple[int, int]] | None:
    """Find a numeric highlight in title (e.g. "5選", "月10万", "7ステップ")"""
    m = re.search(r"(\d+万?[円選個本日週月]?)", text)
    if m:
        return m.group(1), m.span()
    return None


def make_pin(title: str, slug: str, category: str = "") -> Image.Image:
    pal = color_palette(slug)
    img = make_gradient(SIZE, pal["bg_top"], pal["bg_bot"])

    # noise texture
    pixels = img.load()
    for _ in range(SIZE[0] * SIZE[1] // 150):
        x = random.randint(0, SIZE[0] - 1)
        y = random.randint(0, SIZE[1] - 1)
        r, g, b = pixels[x, y]
        n = random.randint(-12, 12)
        pixels[x, y] = (max(0, min(255, r + n)), max(0, min(255, g + n)), max(0, min(255, b + n)))

    draw = ImageDraw.Draw(img)
    margin = 70

    # Top stripe with category
    if category:
        cat_font = load_font(FONT_BOLD, 32)
        cat_bbox = cat_font.getbbox(category)
        cw = cat_bbox[2] - cat_bbox[0]
        draw.rounded_rectangle(
            [(margin, 60), (margin + cw + 50, 130)],
            radius=20,
            fill=pal["accent"],
        )
        draw.text((margin + 25, 75), category, font=cat_font, fill=(255, 255, 255))

    # Big title - vertically center, autoresize
    text_area_w = SIZE[0] - margin * 2
    title_clean = title.strip()
    # try multiple sizes until lines fit in 5 lines max
    for fs in (96, 84, 76, 68, 60, 54):
        font = load_font(FONT_HEAVY, fs)
        lines = wrap_text(title_clean, font, text_area_w)
        if len(lines) <= 6:
            break

    line_height = int(fs * 1.25)
    total_h = line_height * len(lines)
    start_y = (SIZE[1] - total_h) // 2 - 60

    for i, line in enumerate(lines):
        y = start_y + i * line_height
        # text shadow
        draw.text((margin + 3, y + 3), line, font=font, fill=(0, 0, 0, 100))
        draw.text((margin, y), line, font=font, fill=pal["fg"])

    # CTA at bottom
    cta_font = load_font(FONT_BOLD, 36)
    cta_text = "↓ 詳しくはサイトで"
    cta_bbox = cta_font.getbbox(cta_text)
    cw = cta_bbox[2] - cta_bbox[0]
    cta_y = SIZE[1] - 200
    draw.rounded_rectangle(
        [((SIZE[0] - cw - 60) // 2, cta_y), ((SIZE[0] + cw + 60) // 2, cta_y + 75)],
        radius=40,
        fill=pal["accent"],
    )
    draw.text(((SIZE[0] - cw) // 2, cta_y + 15), cta_text, font=cta_font, fill=(255, 255, 255))

    # Site brand at bottom
    site_font = load_font(FONT_BOLD, 28)
    s_bbox = site_font.getbbox(SITE_NAME)
    sw = s_bbox[2] - s_bbox[0]
    draw.text(((SIZE[0] - sw) // 2, SIZE[1] - 80), SITE_NAME, font=site_font, fill=pal["fg"])

    return img


def main() -> int:
    log("=== article-pin-generator start ===")
    if not BLOG_DIR.exists():
        log("blog dir missing")
        return 1

    processed = 0
    for md in BLOG_DIR.glob("*.md"):
        slug = md.stem
        pin_path = PIN_DIR / f"{slug}.png"
        if pin_path.exists():
            continue
        text = md.read_text()
        fm = parse_fm(text)
        title = fm.get("title", slug)
        category = fm.get("category", "")
        try:
            img = make_pin(title, slug, category)
            img.save(pin_path, "PNG", optimize=True)
            processed += 1
            log(f"  pin: {slug}")
        except Exception as e:
            log(f"  fail {slug}: {e}")
    log(f"=== done: {processed} pins generated ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
