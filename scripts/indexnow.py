#!/usr/bin/env python3
"""Submit newly-published article URLs to IndexNow (Bing/Yandex)."""
from __future__ import annotations
import json
import hashlib
import urllib.request
import urllib.error
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
LOG = ROOT / "logs" / "indexnow.log"
LOG.parent.mkdir(exist_ok=True)
CONFIG = json.loads((ROOT / "config.json").read_text())
SITE = CONFIG.get("site_url", "https://nayo126.github.io/auto-blog").rstrip("/")
HOST = SITE.split("//", 1)[1].split("/", 1)[0]
SITE_BASE = SITE if not SITE.endswith(HOST) else SITE  # full URL with base path


def log(msg: str) -> None:
    line = f"[{datetime.now().isoformat(timespec='seconds')}] {msg}"
    print(line)
    with LOG.open("a") as f:
        f.write(line + "\n")


def get_or_create_key() -> str:
    key_path = ROOT / "site" / "public" / ".indexnow.txt"
    if key_path.exists():
        k = key_path.read_text().strip()
        if k:
            return k
    # Stable key derived from host (32+ hex chars)
    k = hashlib.sha256(HOST.encode()).hexdigest()[:32]
    key_path.write_text(k)
    # also expose at /KEY.txt as IndexNow requires
    (ROOT / "site" / "public" / f"{k}.txt").write_text(k)
    return k


def submit(urls: list[str]) -> bool:
    if not urls:
        log("no urls to submit")
        return False
    key = get_or_create_key()
    payload = {
        "host": HOST,
        "key": key,
        "keyLocation": f"https://{HOST}{SITE.split(HOST,1)[1]}/{key}.txt",
        "urlList": urls,
    }
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        "https://api.indexnow.org/IndexNow",
        data=body, method="POST",
        headers={"Content-Type": "application/json; charset=utf-8"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            log(f"IndexNow HTTP {r.status} for {len(urls)} urls")
            return r.status in (200, 202)
    except urllib.error.HTTPError as e:
        log(f"IndexNow HTTPError {e.code}: {e.read().decode('utf-8', errors='ignore')[:200]}")
        return False
    except urllib.error.URLError as e:
        log(f"IndexNow URLError: {e}")
        return False


def main() -> int:
    last = DATA / "last_written.json"
    if not last.exists():
        log("no last_written.json")
        return 0
    ld = json.loads(last.read_text())
    urls: list[str] = []
    for rel in ld.get("files", []):
        slug = Path(rel).stem
        urls.append(f"{SITE}/blog/{slug}/")
    # also include the index
    urls.append(f"{SITE}/")
    ok = submit(urls)
    log(f"indexnow submit ok={ok}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
