#!/usr/bin/env python3
"""auto-blog end-to-end orchestrator: keyword → article → affiliate → publish."""
from __future__ import annotations
import subprocess
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "logs" / "pipeline.log"
LOG.parent.mkdir(exist_ok=True)


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


STAGES = [
    ("keyword", ROOT / "scripts" / "keyword_picker.py"),
    ("article", ROOT / "scripts" / "article_writer.py"),
    ("affiliate", ROOT / "scripts" / "affiliate_inserter.py"),
    ("publish", ROOT / "scripts" / "publisher.py"),
]


def run(stage: str, script: Path) -> int:
    log(f"--- stage {stage}: {script.name} ---")
    t0 = time.time()
    r = subprocess.run([sys.executable, str(script)], capture_output=True, text=True)
    dt = time.time() - t0
    for line in (r.stdout or "").rstrip().splitlines()[-15:]:
        log(f"  {stage}: {line}")
    if r.returncode != 0:
        log(f"!! {stage} FAILED rc={r.returncode} in {dt:.1f}s")
        for line in (r.stderr or "").rstrip().splitlines()[-6:]:
            log(f"  {stage} ERR: {line}")
    else:
        log(f"OK {stage} in {dt:.1f}s")
    return r.returncode


def main() -> int:
    log("============================================================")
    log("=== auto-blog pipeline run ===")
    for stage, script in STAGES:
        rc = run(stage, script)
        if rc != 0:
            log(f"abort at {stage}")
            return rc
    log("=== pipeline complete ===\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
