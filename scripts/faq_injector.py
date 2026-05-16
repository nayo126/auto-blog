#!/usr/bin/env python3
"""FAQセクション + JSON-LD FAQPage schema を記事末尾に注入。

GoogleのFeatured Snippet/People Also Ask 表示を狙う。
1ページ位置0表示でCTRが10倍になることが実証されている。

- AI生成によるFAQ3-5問
- 末尾に <!-- FAQ_START --> ~ <!-- FAQ_END --> でべき等更新
- JSON-LD FAQPage schemaも同時生成
"""
from __future__ import annotations
import json
import re
import subprocess
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "faq.log"
BLOG_DIR = ROOT / "site" / "src" / "content" / "blog"
LOG.parent.mkdir(exist_ok=True)

sys.path.insert(0, "/Users/tsukaking/.claude/lib")
try:
    from rate_limit_helper import (
        looks_like_rate_limit, mark_rate_limited,
        is_currently_blocked, looks_like_native_binary_missing
    )
except ImportError:
    looks_like_rate_limit = lambda x: False
    mark_rate_limited = lambda *a, **k: None
    is_currently_blocked = lambda x: False
    looks_like_native_binary_missing = lambda x: False


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


FAQ_MARK_START = "<!-- FAQ_START -->"
FAQ_MARK_END = "<!-- FAQ_END -->"


FAQ_PROMPT = """あなたは日本のSEOブログのFAQ作者です。以下の記事を読んで、読者が検索しそうな質問4つとその答えを生成してください。

重要ルール:
1. 質問は実際にGoogleで検索されているような自然な質問形式
2. 質問は記事に関連するが、記事タイトルとは違う角度から
3. 答えは50〜150字の簡潔な日本語
4. 答えは具体的・実用的（曖昧な「人それぞれ」「ケースバイケース」NG）
5. 答えに数字や具体例を入れる
6. 「〜と言えるでしょう」「〜ではないでしょうか」を使わない
7. **厳密にこのJSON形式のみで出力（前後に何も書かない）**

```json
{{
  "faqs": [
    {{"q": "質問1", "a": "答え1"}},
    {{"q": "質問2", "a": "答え2"}},
    {{"q": "質問3", "a": "答え3"}},
    {{"q": "質問4", "a": "答え4"}}
  ]
}}
```

記事タイトル: {title}
記事の冒頭: {intro}
"""


def run_claude(prompt: str) -> tuple[str, str]:
    try:
        r = subprocess.run(
            ["claude", "-p", prompt, "--output-format", "text"],
            capture_output=True, text=True, timeout=180,
        )
        return r.stdout or "", r.stderr or ""
    except subprocess.TimeoutExpired:
        return "", "claude timeout"
    except FileNotFoundError:
        return "", "claude binary missing"


def parse_faq_json(raw: str) -> list[dict] | None:
    # Extract JSON block
    m = re.search(r"\{[\s\S]*\"faqs\"[\s\S]*\}", raw)
    if not m:
        return None
    try:
        data = json.loads(m.group(0))
        faqs = data.get("faqs", [])
        if len(faqs) >= 3 and all("q" in f and "a" in f for f in faqs):
            return faqs
    except json.JSONDecodeError:
        pass
    return None


def render_faq_block(faqs: list[dict]) -> str:
    md_parts = [FAQ_MARK_START, "", "## よくある質問", ""]
    for f in faqs:
        md_parts.append(f"### {f['q']}")
        md_parts.append("")
        md_parts.append(f["a"])
        md_parts.append("")

    schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f["q"],
                "acceptedAnswer": {"@type": "Answer", "text": f["a"]},
            }
            for f in faqs
        ],
    }
    md_parts.append('<script type="application/ld+json">')
    md_parts.append(json.dumps(schema, ensure_ascii=False))
    md_parts.append("</script>")
    md_parts.append("")
    md_parts.append(FAQ_MARK_END)
    return "\n".join(md_parts)


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
            fm[k.strip()] = v.strip()
    return fm, m.group(2)


def upsert_faq(file_path: Path, block: str) -> bool:
    text = file_path.read_text()
    pattern = re.compile(re.escape(FAQ_MARK_START) + r".*?" + re.escape(FAQ_MARK_END), re.DOTALL)
    if pattern.search(text):
        new = pattern.sub(block, text)
    else:
        new = text.rstrip() + "\n\n" + block + "\n"
    if new != text:
        file_path.write_text(new)
        return True
    return False


def main() -> int:
    log("=== faq injector start ===")
    if is_currently_blocked("claude_cli"):
        log("claude_cli is blocked; skip this run")
        return 0

    if not BLOG_DIR.exists():
        log("blog dir missing")
        return 1

    posts = sorted(BLOG_DIR.glob("*.md"))
    max_per_run = 4
    done = 0
    for md in posts:
        text = md.read_text()
        if FAQ_MARK_START in text:
            continue
        fm, body = parse_fm(text)
        title = fm.get("title", "").strip('"')
        intro = body[:600]
        prompt = FAQ_PROMPT.format(title=title, intro=intro)
        out, err = run_claude(prompt)
        combined = out + err

        if looks_like_rate_limit(combined) or looks_like_native_binary_missing(combined):
            mark_rate_limited("claude_cli", combined[:300])
            log("rate-limited; bailing")
            return 0

        if not out:
            log(f"  empty response, skip {md.name}: {err[:150]}")
            continue

        faqs = parse_faq_json(out)
        if not faqs:
            log(f"  parse fail {md.name}")
            continue

        block = render_faq_block(faqs)
        if upsert_faq(md, block):
            log(f"  FAQ added: {md.name} ({len(faqs)} questions)")
            done += 1

        if done >= max_per_run:
            log(f"  batch limit ({max_per_run}) reached")
            break

    log(f"=== done: {done} FAQs injected ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
