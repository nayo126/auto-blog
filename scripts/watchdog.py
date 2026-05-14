#!/usr/bin/env python3
"""Watchdog: detect a stalled or rate-limited auto-blog pipeline and re-run when safe.

Runs every hour (via cron/launchd). If today's run did NOT happen successfully,
attempts a recovery pipeline. Detects claude rate-limit failure and waits for the
next hour before retry.
"""
from __future__ import annotations
import json
import subprocess
import sys
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "watchdog.log"
LOG.parent.mkdir(exist_ok=True)
STATE = DATA / "watchdog_state.json"


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line, flush=True)
    with LOG.open("a") as f:
        f.write(line + "\n")


def load_state() -> dict:
    if STATE.exists():
        try:
            return json.loads(STATE.read_text())
        except Exception:
            pass
    return {}


def save_state(s: dict) -> None:
    STATE.write_text(json.dumps(s, ensure_ascii=False, indent=2))


def today_pipeline_succeeded() -> bool:
    last = DATA / "last_written.json"
    if not last.exists():
        return False
    try:
        ld = json.loads(last.read_text())
        ts = ld.get("written_at")
        if not ts:
            return False
        dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        today = datetime.now(dt.tzinfo).date()
        return dt.date() == today and ld.get("count", 0) > 0
    except Exception as e:
        log(f"state read err: {e}")
        return False


def try_claude_ping() -> bool:
    try:
        r = subprocess.run(
            ["claude", "-p", "Reply with just OK.", "--output-format", "text"],
            capture_output=True, text=True, timeout=60,
        )
        out = (r.stdout or "").lower()
        err = (r.stderr or "").lower()
        if "rate" in err or "limit" in err or "429" in err:
            return False
        return r.returncode == 0 and bool(out.strip())
    except Exception as e:
        log(f"claude ping error: {e}")
        return False


def run_pipeline() -> int:
    p = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "run_pipeline.py")],
        capture_output=True, text=True, timeout=3600,
    )
    log(f"pipeline rc={p.returncode}")
    for line in (p.stdout or "").rstrip().splitlines()[-8:]:
        log(f"  out: {line}")
    return p.returncode


def main() -> int:
    state = load_state()
    now = datetime.now()
    if today_pipeline_succeeded():
        log("today's pipeline already succeeded; skipping")
        return 0

    cooldown_until = state.get("cooldown_until")
    if cooldown_until:
        try:
            until = datetime.fromisoformat(cooldown_until)
            if now < until:
                log(f"in cooldown until {until.isoformat()}")
                return 0
        except Exception:
            pass

    if not try_claude_ping():
        log("claude unavailable (likely rate-limited); cooling down 90 minutes")
        state["cooldown_until"] = (now + timedelta(minutes=90)).isoformat()
        save_state(state)
        return 1

    log("claude OK; running recovery pipeline")
    rc = run_pipeline()
    if rc != 0:
        log(f"pipeline failed rc={rc}; cooldown 60 minutes")
        state["cooldown_until"] = (now + timedelta(minutes=60)).isoformat()
        save_state(state)
    else:
        log("pipeline recovered successfully")
        state.pop("cooldown_until", None)
        save_state(state)
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
