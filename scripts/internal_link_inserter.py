#!/usr/bin/env python3
"""Insert related-article internal links at the end of each new article.

SEO で重要な内部リンクを自動生成。タグ/カテゴリの重複が多い記事を「関連記事」セクションとして末尾に追加。
"""
from __future__ import annotations
import json
import re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "internal_link.log"
LOG.parent.mkdir(exist_ok=True)
CONFIG = json.loads((ROOT / "config.json").read_text())
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"
BASE = "/auto-blog"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def parse_frontmatter(text: str) -> tuple[dict, str]:
    if not text.startswith("---"):
        return {}, text
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", text, re.DOTALL)
    if not m:
        return {}, text
    fm: dict = {}
    body = m.group(2)
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            inner = v[1:-1]
            fm[k.strip()] = [t.strip().strip('"').strip("'") for t in inner.split(",") if t.strip()]
        else:
            fm[k.strip()] = v.strip('"').strip("'")
    return fm, body


def gather_all() -> list[dict]:
    posts = []
    for f in BLOG_DIR.glob("*.md"):
        fm, body = parse_frontmatter(f.read_text())
        if not fm:
            continue
        if str(fm.get("draft", "false")).lower() == "true":
            continue
        slug = f.stem
        posts.append({
            "slug": slug,
            "path": f,
            "title": fm.get("title", slug),
            "category": fm.get("category", ""),
            "tags": fm.get("tags", []) if isinstance(fm.get("tags"), list) else [],
            "body": body,
        })
    return posts


def relevance(a: dict, b: dict) -> int:
    score = 0
    if a["category"] == b["category"]:
        score += 3
    tags_a = set(a.get("tags", []) or [])
    tags_b = set(b.get("tags", []) or [])
    score += len(tags_a & tags_b)
    return score


def has_related_section(body: str) -> bool:
    return "## 関連記事" in body or "<!-- RELATED -->" in body


def build_related(target: dict, all_posts: list[dict], n: int = 3) -> str:
    candidates = [p for p in all_posts if p["slug"] != target["slug"]]
    ranked = sorted(candidates, key=lambda p: relevance(target, p), reverse=True)
    picks = [p for p in ranked if relevance(target, p) > 0][:n]
    if not picks:
        return ""
    lines = ["", "## 関連記事", ""]
    for p in picks:
        lines.append(f"- [{p['title']}]({BASE}/blog/{p['slug']}/)")
    lines.append("")
    return "\n".join(lines)


def update_file(post: dict, all_posts: list[dict]) -> bool:
    text = post["path"].read_text()
    fm, body = parse_frontmatter(text)
    if has_related_section(body):
        return False
    block = build_related(post, all_posts, n=3)
    if not block:
        return False
    new_body = body.rstrip() + "\n" + block
    # rebuild file (preserve types: bool/date stay unquoted, strings quoted, lists as YAML)
    BOOL_KEYS = {"draft"}
    DATE_KEYS = {"pubDate", "updatedDate"}
    fm_yaml = "---\n"
    for k, v in fm.items():
        if isinstance(v, list):
            fm_yaml += f'{k}: [{", ".join([chr(34)+x+chr(34) for x in v])}]\n'
        elif k in BOOL_KEYS:
            val = str(v).lower()
            fm_yaml += f"{k}: {'true' if val in ('true','1','yes') else 'false'}\n"
        elif k in DATE_KEYS:
            fm_yaml += f"{k}: {v}\n"
        else:
            fm_yaml += f'{k}: "{v}"\n'
    fm_yaml += "---\n\n"
    post["path"].write_text(fm_yaml + new_body)
    return True


def main() -> int:
    posts = gather_all()
    if not posts:
        log("no posts found")
        return 0
    last = DATA / "last_written.json"
    targets: list[dict] = []
    if last.exists():
        wanted = {Path(p).stem for p in json.loads(last.read_text()).get("files", [])}
        targets = [p for p in posts if p["slug"] in wanted]
    if not targets:
        targets = posts  # bootstrap pass on first run
    touched = 0
    for t in targets:
        if update_file(t, posts):
            touched += 1
    log(f"internal links inserted on {touched}/{len(targets)} posts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
