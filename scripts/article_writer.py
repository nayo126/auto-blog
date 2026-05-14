#!/usr/bin/env python3
"""Generate SEO articles via `claude -p`."""
from __future__ import annotations
import json
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "writer.log"
LOG.parent.mkdir(exist_ok=True)

CONFIG = json.loads((ROOT / "config.json").read_text())
PROMPT_TEMPLATE = (ROOT / "prompts" / "article_writer_prompt.txt").read_text()
OUT_DIR = ROOT / "site" / "src" / "content" / "blog"
OUT_DIR.mkdir(parents=True, exist_ok=True)


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def call_claude(prompt: str, retries: int = 2) -> str:
    import sys
    sys.path.insert(0, "/Users/tsukaking/.claude/lib")
    try:
        from rate_limit_helper import (
            looks_like_rate_limit, looks_like_native_binary_missing,
            mark_rate_limited, mark_clear, is_currently_blocked,
        )
    except ImportError:
        looks_like_rate_limit = lambda t: False
        looks_like_native_binary_missing = lambda t: False
        mark_rate_limited = lambda c, h="", reason="": None
        mark_clear = lambda c: None
        is_currently_blocked = lambda c: False

    if is_currently_blocked("claude_cli"):
        log("claude_cli currently blocked; skip (watchdog retries)")
        return ""

    cli = CONFIG.get("claude_cli", "claude")
    for attempt in range(retries + 1):
        try:
            r = subprocess.run(
                [cli, "-p", prompt, "--output-format", "text"],
                capture_output=True, text=True, timeout=480,
            )
            if r.returncode == 0 and r.stdout.strip():
                mark_clear("claude_cli")
                return r.stdout.strip()
            combined = (r.stderr or "") + " " + (r.stdout or "")
            log(f"claude attempt {attempt+1} rc={r.returncode} err={combined[:200]}")
            if looks_like_native_binary_missing(combined):
                mark_rate_limited("claude_cli", combined[:300], reason="native_missing")
                return ""
            if looks_like_rate_limit(combined):
                mark_rate_limited("claude_cli", combined[:300], reason="rate_limit")
                return ""
        except subprocess.TimeoutExpired:
            log(f"claude attempt {attempt+1} timed out")
        except Exception as e:
            log(f"claude attempt {attempt+1} error: {e}")
    return ""


def slugify(text: str) -> str:
    text = re.sub(r"[^\w\s-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text.strip())
    return text.lower()[:60]


def parse_frontmatter(md: str) -> tuple[dict, str]:
    if not md.startswith("---"):
        return {}, md
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", md, re.DOTALL)
    if not m:
        return {}, md
    body = m.group(2)
    fm = {}
    for line in m.group(1).splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm, body


def looks_valid(md: str) -> tuple[bool, str]:
    if "---" not in md.split("\n", 1)[0] + md[: 50]:
        return False, "no frontmatter"
    fm, body = parse_frontmatter(md)
    if not fm.get("title"):
        return False, "no title"
    word_count = len(body.replace(" ", "").replace("\n", ""))
    if word_count < CONFIG.get("min_words", 1800):
        return False, f"too short ({word_count} chars)"
    # check ban words
    for bad in CONFIG.get("publish_filter", {}).get("ban_words", []):
        if bad in body:
            return False, f"contains banned word: {bad}"
    return True, "ok"


def write_article(category: str, keyword: str) -> Path | None:
    today = datetime.now().strftime("%Y-%m-%d")
    user_block = f"""## 今回の記事
- カテゴリ: {category}
- ターゲットキーワード: {keyword}
- 公開日: {today}

このキーワードで上位表示を狙えるSEOアフィブログ記事を書いてください。
"""
    full_prompt = PROMPT_TEMPLATE + "\n\n" + user_block
    log(f"writing: [{category}] {keyword}")
    raw = call_claude(full_prompt)
    if not raw:
        log("claude returned empty")
        return None
    # strip stray code fences
    raw = re.sub(r"^```(?:markdown|md)?\s*\n", "", raw)
    raw = re.sub(r"\n```\s*$", "", raw)
    ok, why = looks_valid(raw)
    if not ok:
        log(f"rejected: {why}")
        (DATA / f"reject_{slugify(keyword)}.md").write_text(raw)
        return None
    fm, _ = parse_frontmatter(raw)
    slug = slugify(fm.get("title") or keyword) or datetime.now().strftime("%Y%m%d-%H%M%S")
    # ensure unique
    base = slug
    n = 0
    while (OUT_DIR / f"{slug}.md").exists():
        n += 1
        slug = f"{base}-{n}"
    out_path = OUT_DIR / f"{slug}.md"
    out_path.write_text(raw)
    log(f"wrote: {out_path.relative_to(ROOT)}")
    return out_path


def main() -> int:
    today_path = DATA / "today_keywords.json"
    if not today_path.exists():
        log("no today_keywords.json — run keyword_picker first")
        return 1
    today = json.loads(today_path.read_text())
    items = today.get("items", [])
    if not items:
        log("no keywords picked")
        return 0
    written: list[str] = []
    for it in items:
        p = write_article(it["category"], it["keyword"])
        if p:
            written.append(str(p.relative_to(ROOT)))
    (DATA / "last_written.json").write_text(json.dumps({
        "written_at": datetime.now(timezone.utc).isoformat(),
        "count": len(written),
        "files": written,
    }, ensure_ascii=False, indent=2))
    log(f"wrote {len(written)}/{len(items)} articles")
    return 0 if written else 2


if __name__ == "__main__":
    raise SystemExit(main())
