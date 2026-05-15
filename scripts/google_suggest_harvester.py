#!/usr/bin/env python3
"""Google Suggest API から本物の検索クエリを採取して keyword pool に追加。

Google が「実際に検索されているクエリ」をくれるので、Claude が想像した
キーワードより遥かにSEO効果が高い。認証不要・無料・無制限。
"""
from __future__ import annotations
import json
import time
import urllib.request
import urllib.parse
import urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "suggest_harvester.log"
SEED = ROOT / "data" / "seed_keywords.json"
LOG.parent.mkdir(exist_ok=True)

SEED_ROOTS = {
    "ChatGPT活用": ["ChatGPT 副業", "ChatGPT 稼ぐ", "ChatGPT 使い方", "ChatGPT プロンプト", "ChatGPT API"],
    "Claude活用": ["Claude 副業", "Claude 使い方", "Claude プロンプト", "Claude Code", "Claude MCP"],
    "AI副業": ["AI 副業", "AI 稼ぐ方法", "AI 在宅", "AI フリーランス", "AI ブログ"],
    "プロンプトエンジニアリング": ["プロンプト 副業", "プロンプト 売る", "プロンプト 作り方", "プロンプト テンプレート"],
    "AIツール比較": ["AI ツール 比較", "AI 画像生成", "AI 動画", "AI ライティング", "AI 議事録"],
    "海外AIトレンド": ["海外 AI 副業", "OpenAI", "Anthropic", "AI スタートアップ"],
    "個人開発": ["個人開発 AI", "ノーコード 副業", "Bolt.new", "Cursor 使い方"],
    "AI画像生成": ["Midjourney 副業", "Stable Diffusion 稼ぐ", "DALL-E 使い方", "Leonardo AI"],
}


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def google_suggest(query: str) -> list[str]:
    """Google Suggest API (firefox client = JSON response)."""
    url = (
        "https://suggestqueries.google.com/complete/search"
        f"?client=firefox&hl=ja&q={urllib.parse.quote(query)}"
    )
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0)",
            "Accept-Charset": "utf-8",
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            raw = r.read()
            # Firefox client returns ISO-8859-1 sometimes; force-decode UTF-8
            try:
                text = raw.decode("utf-8")
            except UnicodeDecodeError:
                text = raw.decode("latin-1")
            data = json.loads(text)
            if len(data) >= 2 and isinstance(data[1], list):
                return [str(s) for s in data[1] if isinstance(s, str)]
    except (urllib.error.URLError, urllib.error.HTTPError, json.JSONDecodeError, TimeoutError) as e:
        log(f"  suggest failed {query}: {e}")
    return []


def expand_query(query: str, depth: int = 2) -> set[str]:
    """Recursively expand using a-z + あ-お modifiers."""
    results: set[str] = set()
    base = google_suggest(query)
    for b in base:
        results.add(b)
    time.sleep(0.8)

    # ひらがな1文字付加（日本語ロングテール採取）
    modifiers = ["", " 方法", " おすすめ", " 比較", " 無料", " 初心者", " やり方", " 始め方", " 稼ぐ"]
    for m in modifiers[:5]:  # 速度のため5個まで
        extended = google_suggest(query + m)
        for e in extended:
            results.add(e)
        time.sleep(0.8)

    return results


def main() -> int:
    log("=== google-suggest harvester start ===")

    if not SEED.exists():
        log("seed_keywords.json missing")
        return 1

    seed_data = json.loads(SEED.read_text())
    added_total = 0

    for category, seeds in SEED_ROOTS.items():
        existing = set(seed_data.get(category, []))
        new_set: set[str] = set()
        for seed in seeds:
            expanded = expand_query(seed)
            for kw in expanded:
                # uniqueness check, length filter
                kw_clean = kw.strip()
                if 6 <= len(kw_clean) <= 60 and kw_clean not in existing:
                    new_set.add(kw_clean)

        if new_set:
            merged = list(existing) + sorted(new_set)
            seed_data[category] = merged
            log(f"  [{category}] +{len(new_set)} new keywords")
            added_total += len(new_set)

    SEED.write_text(json.dumps(seed_data, ensure_ascii=False, indent=2))
    log(f"=== done: +{added_total} new keywords total ===")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
