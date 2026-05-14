#!/usr/bin/env python3
"""Replace <!-- AFFILIATE_SLOT:keyword --> markers with real affiliate cards.

Reads ~/MONETIZATION_IDS.json (shared across all bots). When the user fills in
their actual IDs, this script automatically generates live affiliate links.
Until then, soft CTA cards are inserted so the layout is consistent.

Minor-friendly sources only:
- 楽天アフィリエイト
- もしもアフィリエイト
- 忍者AdMax
"""
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
MIDS_PATH = Path.home() / "MONETIZATION_IDS.json"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_ids() -> dict:
    if not MIDS_PATH.exists():
        return {}
    try:
        return json.loads(MIDS_PATH.read_text())
    except Exception as e:
        log(f"failed to load MIDS: {e}")
        return {}


IDS = load_ids()
RAKUTEN_ID = (IDS.get("rakuten_affiliate") or {}).get("affiliate_id")
RAKUTEN_OK = bool(RAKUTEN_ID) and RAKUTEN_ID != "TODO"
MOSHIMO_AID = (IDS.get("moshimo") or {}).get("a_id")
MOSHIMO_OK = bool(MOSHIMO_AID) and MOSHIMO_AID != "TODO"
NINJA_TAG = (IDS.get("ninja_admax") or {}).get("ad_tag_html")
NINJA_OK = bool(NINJA_TAG) and NINJA_TAG != "TODO"


def build_rakuten_link(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    search = f"https://search.rakuten.co.jp/search/mall/{q}/"
    if RAKUTEN_OK:
        return (
            f"https://hb.afl.rakuten.co.jp/hgc/{RAKUTEN_ID}/?pc="
            + urllib.parse.quote(search, safe="")
            + "&link_type=text&ut=eyJwYWdlIjoiYWZmaWxpYXRlIn0%3D"
        )
    return search


def build_amazon_link(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    return f"https://www.amazon.co.jp/s?k={q}"


def render_card(keyword: str) -> str:
    bits = [
        '\n<aside class="affiliate-card">',
        f'<div class="label">{keyword} に関連する書籍・ツール</div>',
        f'<p>「{keyword}」について実践的に学ぶための参考リソースを集めました。</p>',
        f'<p><a href="{build_rakuten_link(keyword)}" target="_blank" rel="sponsored noopener">▶ 楽天市場で「{keyword}」関連を見る</a></p>',
        f'<p><a href="{build_amazon_link(keyword)}" target="_blank" rel="sponsored noopener">▶ Amazonで「{keyword}」関連を見る</a></p>',
    ]
    # Optional 忍者AdMax inline ad
    if NINJA_OK:
        bits.append(NINJA_TAG)
    bits.append("</aside>\n")
    return "\n".join(bits)


def process_file(path: Path) -> bool:
    text = path.read_text()
    found = list(re.finditer(r"<!--\s*AFFILIATE_SLOT:(.+?)\s*-->", text))
    if not found:
        return False
    new = text
    for m in reversed(found):
        kw = m.group(1).strip()
        new = new[: m.start()] + render_card(kw) + new[m.end():]
    path.write_text(new)
    log(f"injected {len(found)} affiliate slot(s) -> {path.name}")
    return True


def main() -> int:
    log(f"=== affiliate insert (rakuten={RAKUTEN_OK} moshimo={MOSHIMO_OK} ninja={NINJA_OK}) ===")
    if not BLOG_DIR.exists():
        log("blog dir missing")
        return 1
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
    log(f"affiliate done: {touched}/{len(files)} files modified")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
