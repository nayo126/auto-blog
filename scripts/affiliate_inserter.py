#!/usr/bin/env python3
"""Replace <!-- AFFILIATE_SLOT:キーワード --> with actual affiliate cards."""
from __future__ import annotations
import json
import re
import urllib.parse
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "affiliate.log"
LOG.parent.mkdir(exist_ok=True)
CONFIG = json.loads((ROOT / "config.json").read_text())
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def build_rakuten_search(keyword: str) -> str:
    """Build a Rakuten search URL (replace with affiliate-wrapped URL once approved)."""
    q = urllib.parse.quote(keyword)
    return f"https://search.rakuten.co.jp/search/mall/{q}/"


def build_amazon_search(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    return f"https://www.amazon.co.jp/s?k={q}"


def render_card(keyword: str, soft_only: bool) -> str:
    if soft_only or not CONFIG["affiliate"]["enabled_links"]:
        # soft CTA only, no live affiliate link
        return (
            "\n<aside class=\"affiliate-card\">\n"
            f"<div class=\"label\">{keyword} に関連する情報</div>\n"
            f"<p>{keyword} を実際に試してみたい方は、まず無料プランから始めるのがおすすめです。"
            "本サイトでは将来的に、関連する書籍・ツールのレビューをまとめる予定です。</p>\n"
            "</aside>\n"
        )
    rakuten = build_rakuten_search(keyword)
    amazon = build_amazon_search(keyword)
    return (
        "\n<aside class=\"affiliate-card\">\n"
        f"<div class=\"label\">{keyword} の関連商品</div>\n"
        f"<p>「{keyword}」について、より深く学ぶための書籍やツールをまとめました。</p>\n"
        f"<p><a href=\"{rakuten}\" target=\"_blank\" rel=\"sponsored noopener\">▶ 楽天市場で「{keyword}」関連商品を見る</a></p>\n"
        f"<p><a href=\"{amazon}\" target=\"_blank\" rel=\"sponsored noopener\">▶ Amazonで「{keyword}」関連商品を見る</a></p>\n"
        "</aside>\n"
    )


def process_file(path: Path) -> bool:
    text = path.read_text()
    soft_only = CONFIG["affiliate"].get("soft_cta_only", True)
    found = list(re.finditer(r"<!--\s*AFFILIATE_SLOT:(.+?)\s*-->", text))
    if not found:
        return False
    new = text
    for m in reversed(found):
        kw = m.group(1).strip()
        replacement = render_card(kw, soft_only)
        new = new[: m.start()] + replacement + new[m.end():]
    path.write_text(new)
    log(f"injected {len(found)} affiliate slot(s) -> {path.name}")
    return True


def main() -> int:
    if not BLOG_DIR.exists():
        log("blog dir missing")
        return 1
    # process only the freshly written articles from this run
    last = DATA / "last_written.json"
    files: list[Path] = []
    if last.exists():
        ld = json.loads(last.read_text())
        for rel in ld.get("files", []):
            p = ROOT / rel
            if p.exists():
                files.append(p)
    else:
        files = list(BLOG_DIR.glob("*.md"))
    touched = 0
    for f in files:
        if process_file(f):
            touched += 1
    log(f"affiliate insertion done: {touched}/{len(files)} files modified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
