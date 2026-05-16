#!/usr/bin/env python3
"""Cross-blog linker: append links to ai-news-jp articles in newly-written auto-blog posts.

SEOパワーを2サイト間で循環させる。タグ重複度で関連記事を選び、自然な文脈で末尾に追加。
"""
from __future__ import annotations
import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "cross_link.log"
LOG.parent.mkdir(exist_ok=True)
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"
NEWS_DIR = Path.home() / "ai-news-jp" / "content" / "posts"
NEWS_BASE = "https://nayo126.github.io/ai-news-jp"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def parse_yaml_fm(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm: dict = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            fm[k.strip()] = [t.strip().strip('"').strip("'") for t in v[1:-1].split(",") if t.strip()]
        else:
            fm[k.strip()] = v.strip('"').strip("'")
    return fm, m.group(2)


def parse_json_fm(text: str) -> tuple[dict, str]:
    """ai-news-jp uses --- + JSON object + --- frontmatter."""
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(\{.*?\n\})\s*\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        # fallback to yaml
        return parse_yaml_fm(text)
    try:
        return json.loads(m.group(1)), m.group(2)
    except json.JSONDecodeError:
        return {}, text


def load_news_articles() -> list[dict]:
    if not NEWS_DIR.exists():
        return []
    out = []
    for f in NEWS_DIR.glob("*.md"):
        try:
            fm, _ = parse_json_fm(f.read_text())
        except Exception:
            continue
        if not fm.get("title"):
            continue
        # ai-news-jp's published URL uses the frontmatter `slug` field
        # (e.g. "sea-limited-openai-codex") and the path is `/posts/{slug}.html`.
        # Falling back to f.stem produces broken links because the filename has
        # a `YYYY-MM-DD-` date prefix that the static-site builder strips off.
        slug = fm.get("slug") or f.stem
        out.append({
            "slug": slug,
            "title": fm.get("title", ""),
            "category": fm.get("category", ""),
            "tags": fm.get("tags") if isinstance(fm.get("tags"), list) else [],
            "url": f"{NEWS_BASE}/posts/{slug}.html",
        })
    return out


def relevance(target_tags: list[str], target_cat: str, candidate: dict) -> int:
    score = 0
    if target_cat and target_cat == candidate.get("category"):
        score += 2
    cand_tags = set(candidate.get("tags") or [])
    target_set = {t.lower() for t in (target_tags or [])}
    for t in cand_tags:
        if t.lower() in target_set:
            score += 2
        else:
            # partial match
            for tt in target_set:
                if t.lower() in tt or tt in t.lower():
                    score += 1
                    break
    return score


def update_auto_blog_file(path: Path, news_posts: list[dict]) -> bool:
    text = path.read_text()
    if "<!-- CROSS_LINKS -->" in text or "## 他サイトの最新記事" in text:
        return False
    fm, body = parse_yaml_fm(text)
    tags = fm.get("tags") if isinstance(fm.get("tags"), list) else []
    cat = fm.get("category", "")
    ranked = sorted(news_posts, key=lambda p: relevance(tags, cat, p), reverse=True)
    picks = [p for p in ranked if relevance(tags, cat, p) > 0][:3]
    if not picks:
        return False
    block = ["", "<!-- CROSS_LINKS -->", "## 他サイトの最新AI記事", ""]
    for p in picks:
        block.append(f"- [{p['title']}]({p['url']})")
    block.append("")
    new_body = body.rstrip() + "\n" + "\n".join(block)
    path.write_text(text[: text.index(body)] + new_body)
    return True


def main() -> int:
    log("=== cross-blog linker ===")
    if not NEWS_DIR.exists():
        log("ai-news-jp not found; skipping")
        return 0
    news_posts = load_news_articles()
    log(f"news pool: {len(news_posts)}")
    if not news_posts:
        return 0
    last = DATA / "last_written.json"
    targets: list[Path] = []
    if last.exists():
        for rel in json.loads(last.read_text()).get("files", []):
            p = ROOT / rel
            if p.exists():
                targets.append(p)
    else:
        targets = list(BLOG_DIR.glob("*.md"))
    touched = 0
    for t in targets:
        if update_auto_blog_file(t, news_posts):
            touched += 1
    log(f"cross-linked {touched}/{len(targets)} auto-blog posts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
