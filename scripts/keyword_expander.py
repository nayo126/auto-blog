#!/usr/bin/env python3
"""Auto-expand seed keywords using claude when pool gets low.

Triggered when (total - used) < 30. Generates 30 fresh keywords per category
and merges into seed_keywords.json.
"""
from __future__ import annotations
import json
import re
import subprocess
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "expand.log"
LOG.parent.mkdir(exist_ok=True)
CONFIG = json.loads((ROOT / "config.json").read_text())
SEED_PATH = DATA / "seed_keywords.json"
USED_PATH = DATA / "used_keywords.json"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def call_claude(prompt: str) -> str:
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
        log("claude_cli currently blocked; skip")
        return ""
    try:
        r = subprocess.run(
            [CONFIG.get("claude_cli", "claude"), "-p", prompt, "--output-format", "text"],
            capture_output=True, text=True, timeout=180,
        )
        if r.returncode == 0 and r.stdout.strip():
            mark_clear("claude_cli")
            return r.stdout.strip()
        combined = (r.stderr or "") + " " + (r.stdout or "")
        if looks_like_native_binary_missing(combined):
            mark_rate_limited("claude_cli", combined[:300], reason="native_missing")
        elif looks_like_rate_limit(combined):
            mark_rate_limited("claude_cli", combined[:300], reason="rate_limit")
    except Exception as e:
        log(f"claude error: {e}")
    return ""


def main() -> int:
    seed = json.loads(SEED_PATH.read_text())
    used = set()
    if USED_PATH.exists():
        try:
            used = set(json.loads(USED_PATH.read_text()))
        except Exception:
            pass
    remaining = sum(len(v) for v in seed.values()) - len(used)
    log(f"remaining keywords: {remaining}")
    if remaining >= 30:
        log("pool healthy; no expansion needed")
        return 0

    log("expanding keyword pool via claude…")
    added_total = 0
    for cat in list(seed.keys()):
        existing = "\n".join(f"- {k}" for k in seed[cat])
        prompt = f"""あなたはSEOコンサルです。
カテゴリ「{cat}」で、2026年にロングテール検索ボリュームが見込めるキーワードを
**新たに20個** 出してください。

## 既存KW（重複NG）
{existing}

## 必達ルール
- 1行1KW、純粋なKWのみ
- 「2026」「副業」「初心者」「比較」「ランキング」「やり方」「月収」「無料」等の修飾語を組み合わせる
- 3〜5語のフレーズ
- 検索意図が明確なもの

出力はKWの箇条書きだけ。先頭の「- 」も不要。"""
        out = call_claude(prompt)
        if not out:
            continue
        new_kws = []
        for line in out.splitlines():
            line = re.sub(r"^[\-\*\d\.\)]+\s*", "", line.strip())
            if not line:
                continue
            if line in seed[cat]:
                continue
            if len(line) > 80 or len(line) < 6:
                continue
            new_kws.append(line)
        seed[cat].extend(new_kws[:20])
        added_total += len(new_kws[:20])
        log(f"  +{len(new_kws[:20])} for {cat} (total: {len(seed[cat])})")
    SEED_PATH.write_text(json.dumps(seed, ensure_ascii=False, indent=2))
    log(f"expansion done: +{added_total} keywords")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
