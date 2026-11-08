"""Format Chicago/Harvard citation lines from supplied source fields (no network).

Ported from mcps/verify/cite.py for TRUSTED. Label outputs not tool-checked.
"""

from __future__ import annotations

import re
from datetime import datetime, timezone

_MONTHS = (
    "",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)


def _year(date: str | None) -> str | None:
    if not date:
        return None
    match = re.match(r"^(\d{4})", str(date))
    return match.group(1) if match else None


def _long_date(date: str | None) -> str | None:
    if not date:
        return None
    text = str(date)
    match = re.match(r"^(\d{4})-(\d{2})-(\d{2})", text)
    if match:
        year, month, day = int(match.group(1)), int(match.group(2)), int(match.group(3))
        if 1 <= month <= 12:
            return f"{_MONTHS[month]} {day}, {year}"
    match = re.match(r"^(\d{4})-(\d{2})", text)
    if match:
        year, month = int(match.group(1)), int(match.group(2))
        if 1 <= month <= 12:
            return f"{_MONTHS[month]} {year}"
    year = _year(text)
    return year


def _author(source: dict) -> str:
    return (source.get("publisher") or source.get("authority") or source.get("author") or "").strip()


def format_chicago(source: dict) -> str:
    author = _author(source)
    year = _year(source.get("date"))
    title = (source.get("title") or "").strip()
    url = (source.get("official_url") or source.get("url") or "").strip()
    long_date = _long_date(source.get("date"))
    parts: list[str] = []
    if author and year:
        parts.append(f"{author}. {year}.")
    elif author:
        parts.append(f"{author}.")
    elif year:
        parts.append(f"{year}.")
    if title:
        parts.append(f'"{title}."')
    if long_date and long_date != year:
        parts.append(f"{long_date}.")
    if url:
        parts.append(url + ("" if url.endswith(".") else "."))
    return " ".join(parts).strip()


def format_harvard(source: dict, *, accessed: str | None = None) -> str:
    author = _author(source) or "Unknown"
    year = _year(source.get("date")) or "n.d."
    title = (source.get("title") or "").strip()
    url = (source.get("official_url") or source.get("url") or "").strip()
    if accessed is None:
        today = datetime.now(timezone.utc).date()
        accessed = f"{today.day} {_MONTHS[today.month]} {today.year}"
    line = f"{author} ({year}) {title}." if title else f"{author} ({year})."
    if url:
        line += f" Available at: {url} (Accessed: {accessed})."
    return line


def format_citation(source: dict, style: str) -> str:
    if style == "harvard":
        return format_harvard(source)
    return format_chicago(source)


def main() -> None:
    import argparse
    import json
    import sys

    ap = argparse.ArgumentParser(
        description="Format a citation from supplied fields (no network). Label not tool-checked."
    )
    ap.add_argument("--title", default="")
    ap.add_argument("--authors", default="", help="Author or publisher string")
    ap.add_argument("--publisher", default="")
    ap.add_argument("--year", default="")
    ap.add_argument("--date", default="", help="ISO date preferred; year alone accepted")
    ap.add_argument("--url", default="")
    ap.add_argument("--style", choices=("chicago", "harvard"), default="chicago")
    ap.add_argument("--json-file", help="Source object JSON file or - for stdin")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    if args.json_file:
        raw = sys.stdin.read() if args.json_file == "-" else open(args.json_file, encoding="utf-8").read()
        source = json.loads(raw)
    else:
        source = {
            "title": args.title,
            "author": args.authors,
            "publisher": args.publisher or args.authors,
            "date": args.date or args.year,
            "url": args.url,
            "official_url": args.url,
        }
    line = format_citation(source, args.style)
    out = {
        "citation": line,
        "style": args.style,
        "label": "not tool-checked",
    }
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(line)
        print("not tool-checked")


if __name__ == "__main__":
    main()
