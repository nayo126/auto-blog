#!/usr/bin/env python3
"""Pick N keywords for today's articles, avoiding past keywords."""
from __future__ import annotations
import json
import random
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "keyword.log"
LOG.parent.mkdir(exist_ok=True)

CONFIG = json.loads((ROOT / "config.json").read_text())
SEED = json.loads((DATA / "seed_keywords.json").read_text())
HIST_PATH = DATA / "used_keywords.json"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_history() -> set[str]:
    if HIST_PATH.exists():
        try:
            return set(json.loads(HIST_PATH.read_text()))
        except Exception:
            return set()
    return set()


def save_history(used: set[str]) -> None:
    HIST_PATH.write_text(json.dumps(sorted(used), ensure_ascii=False, indent=2))


def pick(n: int) -> list[dict]:
    used = load_history()
    pool: list[tuple[str, str]] = []
    for cat, kws in SEED.items():
        for k in kws:
            if k not in used:
                pool.append((cat, k))
    if not pool:
        log("all keywords exhausted; resetting history")
        used = set()
        for cat, kws in SEED.items():
            for k in kws:
                pool.append((cat, k))
    random.shuffle(pool)

    # spread categories
    chosen: list[dict] = []
    cats_taken: set[str] = set()
    for cat, k in pool:
        if cat in cats_taken and len(chosen) < n:
            continue
        chosen.append({"category": cat, "keyword": k})
        cats_taken.add(cat)
        if len(chosen) >= n:
            break
    if len(chosen) < n:
        for cat, k in pool:
            if {"category": cat, "keyword": k} not in chosen:
                chosen.append({"category": cat, "keyword": k})
                if len(chosen) >= n:
                    break

    for c in chosen:
        used.add(c["keyword"])
    save_history(used)
    return chosen[:n]


def main() -> int:
    n = CONFIG.get("articles_per_run", 3)
    if len(sys.argv) > 1:
        try:
            n = int(sys.argv[1])
        except ValueError:
            pass
    chosen = pick(n)
    out = {
        "picked_at": datetime.now(timezone.utc).isoformat(),
        "count": len(chosen),
        "items": chosen,
    }
    (DATA / "today_keywords.json").write_text(json.dumps(out, ensure_ascii=False, indent=2))
    log(f"picked {len(chosen)} keywords -> data/today_keywords.json")
    for c in chosen:
        log(f"  [{c['category']}] {c['keyword']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
