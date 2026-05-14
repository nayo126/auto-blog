#!/usr/bin/env python3
"""Cross-post freshly-published auto-blog articles to the existing Threads queue.

For each new article:
- Generate a 180-character teaser via `claude -p`
- Post to the existing Threads API App with the article URL in the first comment
- Auto-schedule using existing schedule-bulk endpoint
"""
from __future__ import annotations
import json
import re
import subprocess
import sys
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "threads_promote.log"
LOG.parent.mkdir(exist_ok=True)
CONFIG = json.loads((ROOT / "config.json").read_text())

THREADS_APP = "https://threads-api-app.onrender.com"
SITE = CONFIG.get("site_url", "https://nayo126.github.io/auto-blog").rstrip("/")
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"


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
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, m.group(2)


def call_claude(prompt: str) -> str:
    cli = CONFIG.get("claude_cli", "claude")
    try:
        r = subprocess.run(
            [cli, "-p", prompt, "--output-format", "text"],
            capture_output=True, text=True, timeout=180,
        )
        if r.returncode == 0:
            return r.stdout.strip()
        log(f"claude rc={r.returncode}: {r.stderr[:160]}")
    except Exception as e:
        log(f"claude error: {e}")
    return ""


PROMPT = """あなたはThreadsで投稿する文章を作るゴーストライターです。

## 必達ルール
- **本文は170字以内**（必達）
- 1行目に数字・固有名詞・問いかけのいずれかで読者の手を止める
- 1行目の後に空行1行
- 「いいね/フォローして」など露骨な乞いNG
- AIっぽい整い方禁止、改行・短文・口語を混ぜる
- 最後の1行は記事への自然な誘導（「↓詳しくは記事に書きました」「↓まとめてみた」など）
- 「すげー」「やばい」「マジで」など若い口語OK、ただし1回まで
- ハッシュタグは末尾に2つだけ
- **書き手は18歳前の高校生。金額の実績(「○○円稼げた」)は絶対に書かない**。海外事例なら「海外で〇〇円稼いだ人がいる」のように一般化
- 「僕は副業で稼いだ」など虚偽の収益自慢は禁止。代わりに「学んだ」「調べた」「気づいた」を使う

## 投稿の元ネタ
- 記事タイトル: {title}
- 記事のディスクリプション: {description}
- カテゴリ: {category}
- タグ: {tags}

このネタを **170字以内のThreads本文1個** に変換してください。
出力はThreads投稿の本文だけ（前置きや説明、引用符は不要）。"""


def teaser_for(post: dict) -> str:
    p = PROMPT.format(
        title=post.get("title", ""),
        description=post.get("description", ""),
        category=post.get("category", ""),
        tags=", ".join(post.get("tags", []) if isinstance(post.get("tags"), list) else []),
    )
    out = call_claude(p).strip()
    out = out.strip('"').strip("「").strip("」")
    if len(out) > 200:
        out = out[:197] + "…"
    return out


def post_bulk(items: list[dict]) -> list[str]:
    body = json.dumps({"items": items}).encode("utf-8")
    req = urllib.request.Request(
        f"{THREADS_APP}/api/claude-posts/bulk", data=body, method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            resp = json.loads(r.read())
            return [e.get("id") for e in resp.get("entries", []) if e.get("id")]
    except urllib.error.HTTPError as e:
        log(f"bulk HTTPError {e.code}: {e.read().decode('utf-8', errors='ignore')[:200]}")
    except urllib.error.URLError as e:
        log(f"bulk URLError: {e}")
    return []


def schedule(ids: list[str]) -> None:
    if not ids:
        return
    body = json.dumps({
        "ids": ids,
        "timeSlotsPerDay": 3,
        "startDate": datetime.now().strftime("%Y-%m-%d"),
    }).encode("utf-8")
    req = urllib.request.Request(
        f"{THREADS_APP}/api/claude-posts/schedule-bulk", data=body, method="POST",
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as r:
            log(f"schedule HTTP {r.status}")
    except Exception as e:
        log(f"schedule error: {e}")


def main() -> int:
    last = DATA / "last_written.json"
    if not last.exists():
        log("no last_written.json — nothing to promote")
        return 0
    files: list[Path] = []
    for rel in json.loads(last.read_text()).get("files", []):
        p = ROOT / rel
        if p.exists():
            files.append(p)
    if not files:
        log("no fresh articles")
        return 0

    items_for_bulk = []
    for f in files:
        text = f.read_text()
        fm, _ = parse_frontmatter(text)
        if not fm.get("title"):
            continue
        # parse tags from frontmatter "[a, b]" style
        tags_raw = fm.get("tags", "")
        tags = []
        if isinstance(tags_raw, str) and tags_raw.startswith("["):
            tags = [t.strip().strip('"').strip("'") for t in tags_raw[1:-1].split(",") if t.strip()]
        post = {
            "title": fm["title"],
            "description": fm.get("description", ""),
            "category": fm.get("category", ""),
            "tags": tags,
        }
        teaser = teaser_for(post)
        if not teaser:
            continue
        article_url = f"{SITE}/blog/{f.stem}/"
        comment = f"記事はこちら ↓\n{article_url}"
        items_for_bulk.append({
            "texts": [teaser, comment],
            "label": f"blog: {fm['title'][:30]}",
            "type": "ブログ告知",
            "format": "情報型",
        })
        log(f"prepared teaser for: {fm['title']}")

    if not items_for_bulk:
        log("no teasers to post")
        return 0

    if "--dry" in sys.argv:
        (DATA / "would_promote.json").write_text(json.dumps({"items": items_for_bulk}, ensure_ascii=False, indent=2))
        log(f"DRY: would post {len(items_for_bulk)} items")
        return 0

    ids = post_bulk(items_for_bulk)
    log(f"posted {len(ids)} items to Threads queue")
    schedule(ids)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
