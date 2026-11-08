"""Offline source_score when provenance fields are supplied by hand (no network).

Ported from mcps/verify/source_score.py for TRUSTED Prove. Label outputs not tool-checked.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone

_WEIGHTS = {
    "authority": 25,
    "recency": 25,
    "relevance": 30,
    "provenance": 10,
    "currency": 10,
}
_OFFICIAL = (
    "fda",
    "ema",
    "federal register",
    "european medicines",
    "u.s. food",
    "department of health",
    "nice",
    "mhra",
    "health canada",
    "ich",
)
_STOP = {
    "the",
    "and",
    "for",
    "with",
    "that",
    "this",
    "from",
    "what",
    "does",
    "about",
    "into",
    "your",
    "have",
    "been",
}


def _months_old(date: str | None) -> int | None:
    if not date:
        return None
    match = re.match(r"^(\d{4})(?:-(\d{2}))?(?:-(\d{2}))?", str(date))
    if not match:
        return None
    year = int(match.group(1))
    month = int(match.group(2) or 1)
    day = int(match.group(3) or 1)
    try:
        then = datetime(year, month, day, tzinfo=timezone.utc)
    except ValueError:
        return None
    return max(0, int((datetime.now(timezone.utc) - then).days / 30))


def _authority(source: dict) -> int:
    if (source.get("source_type") or "") == "supplied":
        return 0
    publisher = (source.get("publisher") or source.get("authority") or "").lower()
    host = (source.get("official_url") or "").lower()
    if any(name in publisher or name in host for name in _OFFICIAL) or host.endswith(".gov") or ".gov/" in host or host.endswith(".europa.eu") or ".europa.eu/" in host:
        return 25
    if publisher:
        return 15
    return 0


def _recency(source: dict) -> int:
    months = _months_old(source.get("date"))
    if months is None:
        return 0
    if months <= 18:
        return 25
    if months <= 36:
        return 15
    return 5


def _provenance(source: dict) -> int:
    if (source.get("source_type") or "") == "supplied":
        return 0
    return {"gold": 10, "silver": 7, "bronze": 3}.get(source.get("tier") or "", 0)


def _relevance(source: dict, question: str | None) -> int | None:
    if not question or not question.strip():
        return None
    words = [w for w in re.findall(r"[a-z0-9]{4,}", question.lower()) if w not in _STOP]
    if not words:
        return None
    hay = " ".join(
        str(source.get(key) or "")
        for key in ("title", "publisher", "authority")
    ).lower()
    passage = source.get("passage")
    if isinstance(passage, dict):
        hay += " " + str(passage.get("text") or "")
    elif isinstance(passage, str):
        hay += " " + passage
    hit = sum(1 for word in words if word in hay)
    ratio = hit / len(words)
    if ratio >= 0.5:
        return 30
    if ratio >= 0.2:
        return 15
    return 5


def _currency(currency: str | None) -> int | None:
    if currency in {None, "", "not_checked"}:
        return None
    if currency in {"retracted", "superseded", "withdrawn"}:
        return 0
    return 10


def score_source(source: dict, *, question: str | None = None, currency: str | None = "not_checked") -> dict:
    axes = {
        "authority": _authority(source),
        "recency": _recency(source),
        "relevance": _relevance(source, question),
        "provenance": _provenance(source),
        "currency": _currency(currency),
    }
    included = {name: value for name, value in axes.items() if value is not None}
    weight = sum(_WEIGHTS[name] for name in included)
    raw = sum(included.values())
    total = round(100 * raw / weight) if weight else 0
    return {"total": total, "axes": axes, "label": "not tool-checked"}


def main() -> None:
    import argparse
    import json
    import sys

    ap = argparse.ArgumentParser(
        description="Score a source from supplied metadata only (no fetch). Label not tool-checked."
    )
    ap.add_argument("--title", default="")
    ap.add_argument("--publisher", default="")
    ap.add_argument("--year", default="")
    ap.add_argument("--date", default="")
    ap.add_argument("--url", default="")
    ap.add_argument("--tier", default="", help="gold|silver|bronze")
    ap.add_argument("--question", default="")
    ap.add_argument("--currency", default="not_checked")
    ap.add_argument("--json-file", help="Source object JSON file or -")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.json_file:
        raw = sys.stdin.read() if args.json_file == "-" else open(args.json_file, encoding="utf-8").read()
        source = json.loads(raw)
    else:
        source = {
            "title": args.title,
            "publisher": args.publisher,
            "date": args.date or args.year,
            "official_url": args.url,
            "tier": args.tier or None,
        }
    out = score_source(source, question=args.question or None, currency=args.currency)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(f"total={out['total']} axes={out['axes']} not tool-checked")


if __name__ == "__main__":
    main()
