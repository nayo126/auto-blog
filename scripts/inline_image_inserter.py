#!/usr/bin/env python3
"""記事本文にAI生成画像を自動挿入。Pollinations.ai (認証不要・無料・無制限) を使用。

- 各記事のH2見出しの直前/直後に画像を1〜2枚挿入
- AltテキストはH2タイトルから自動生成 (SEO効果)
- 画像URLはPollinations.aiの永続URL (キャッシュなしでもOK)
"""
from __future__ import annotations
import json
import re
import time
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "inline_image.log"
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"
STATE_FILE = ROOT / "data" / "inline_image_state.json"
IMG_DIR = ROOT / "site" / "public" / "inline-images"
IMG_DIR.mkdir(parents=True, exist_ok=True)
LOG.parent.mkdir(exist_ok=True)
STATE_FILE.parent.mkdir(exist_ok=True)

INLINE_MARK = "<!-- INLINE_IMG -->"

ARTICLE_TO_PROMPT = {
    "ChatGPT": "stylish illustration, modern tech, ChatGPT working on a laptop, clean minimal design",
    "Claude": "stylish illustration, modern tech, Claude AI assistant, soft purple gradient",
    "副業": "freelancer working on a laptop in a cafe, modern Tokyo, productive vibe, illustration",
    "AI": "futuristic AI brain illustration, gradient blue purple, modern style",
    "プロンプト": "abstract neural network visualization, clean minimal design",
    "個人開発": "indie developer at desk, multi-monitor setup, anime style illustration",
    "画像生成": "AI generating colorful art, abstract digital art, vibrant gradient",
    "動画": "video editing on dual monitors, modern minimal style, dark theme",
    "ブログ": "person writing blog post on laptop, cozy desk, soft lighting, illustration",
}


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_state(d: dict) -> None:
    STATE_FILE.write_text(json.dumps(d, ensure_ascii=False, indent=2))


def parse_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm = {}
    for line in m.group(1).split("\n"):
        if ":" in line:
            k, v = line.split(":", 1)
            fm[k.strip()] = v.strip().strip('"')
    return fm, m.group(2)


def derive_prompt(title: str, h2_text: str) -> str:
    """Pick a base prompt by keyword match, then refine with H2 text."""
    matched = "modern tech illustration, soft gradient, clean minimal style"
    for kw, p in ARTICLE_TO_PROMPT.items():
        if kw in title or kw in h2_text:
            matched = p
            break
    # Translate Japanese H2 to English-ish prompt context
    cleaned = re.sub(r"[「」『』、。！？!?]", " ", h2_text).strip()
    # Limit length so URL doesn't blow up
    cleaned_short = cleaned[:50]
    return f"{matched}, theme: {cleaned_short}, high quality, illustration"


def download_pollinations(prompt: str, slug: str, idx: int) -> str | None:
    """Download a free stock image. Tries loremflickr.com (free, follows redirect).

    Pollinations.ai went paid (HTTP 402) so we use loremflickr by keyword instead.
    """
    # Extract a single English-ish keyword from prompt for loremflickr
    keywords = ["ai", "computer", "office", "laptop", "code", "technology", "abstract", "minimal"]
    chosen = keywords[abs(hash(slug + str(idx))) % len(keywords)]
    if "副業" in prompt or "freelance" in prompt.lower():
        chosen = "office,desk"
    elif "AI" in prompt or "ai" in prompt:
        chosen = "abstract,technology"
    elif "画像生成" in prompt or "image" in prompt.lower():
        chosen = "art,abstract"
    elif "動画" in prompt or "video" in prompt.lower():
        chosen = "screen,computer"

    url = f"https://loremflickr.com/800/400/{urllib.parse.quote(chosen)}"
    safe_slug = re.sub(r"[^a-z0-9]+", "-", slug.lower())[:40]
    local_name = f"{safe_slug}-{idx}.jpg"
    local_path = IMG_DIR / local_name
    if local_path.exists():
        return f"/auto-blog/inline-images/{local_name}"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 auto-blog-image/2.0"})
    try:
        # urlopen follows redirects automatically
        with urllib.request.urlopen(req, timeout=30) as r:
            data = r.read()
        if len(data) < 5000:
            return None
        local_path.write_bytes(data)
        return f"/auto-blog/inline-images/{local_name}"
    except Exception:
        return None


def inject_images(body: str, title: str, slug: str) -> tuple[str, int]:
    """Insert <!-- INLINE_IMG --> markers after the first 2 H2 sections."""
    lines = body.split("\n")
    new_lines: list[str] = []
    inserted = 0
    max_inserts = 2

    for i, line in enumerate(lines):
        new_lines.append(line)
        if inserted >= max_inserts:
            continue
        if line.startswith("## ") and INLINE_MARK not in body:
            h2_text = line[3:].strip()
            # Skip "よくある質問" / "関連" sections
            if any(k in h2_text for k in ["よくある質問", "関連", "FAQ", "Related"]):
                continue
            prompt = derive_prompt(title, h2_text)
            img_url = download_pollinations(prompt, slug, inserted)
            if img_url:
                alt = f"{title} - {h2_text}"
                new_lines.append("")
                new_lines.append(INLINE_MARK)
                new_lines.append(f"![{alt}]({img_url})")
                new_lines.append("")
                inserted += 1
                time.sleep(1)  # rate respect
    return "\n".join(new_lines), inserted


def main() -> int:
    log("=== inline image inserter start ===")
    if not BLOG_DIR.exists():
        log("blog dir missing")
        return 1

    state = load_state()
    state.setdefault("processed", [])
    processed_set = set(state["processed"])

    max_per_run = 5
    done = 0
    for md in BLOG_DIR.glob("*.md"):
        if str(md) in processed_set:
            continue
        text = md.read_text()
        if INLINE_MARK in text:
            continue
        fm, body = parse_fm(text)
        title = fm.get("title", md.stem)
        slug = md.stem

        new_body, n = inject_images(body, title, slug)
        if n == 0:
            log(f"  no insertions for {md.name}")
            state["processed"].append(str(md))
            save_state(state)
            continue

        # rebuild full file
        fm_part = re.match(r"^---\s*\n.*?\n---\s*\n", text, re.DOTALL).group(0)
        md.write_text(fm_part + new_body)
        state["processed"].append(str(md))
        save_state(state)
        log(f"  inserted {n} images: {md.name}")
        done += 1

        if done >= max_per_run:
            log(f"  batch limit ({max_per_run}) reached")
            break

    log(f"=== done: {done} articles updated ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
