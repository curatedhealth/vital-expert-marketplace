#!/usr/bin/env python3
"""Stamp a consistent TRUSTED check-line for offline or live Prove runs.

Usage:
  python stamp_check_line.py --mode offline --skill claim-assessment
  python stamp_check_line.py --mode local --skill source-assessment --extra "3 sources scored"
  python stamp_check_line.py --mode verify --skill claim-assessment

Letter summary (trusted-check grammar — matches templates/check-line-stamp.md):
  python stamp_check_line.py --letter-lines \\
    --letter 'T|grounded/sourced|flag|causal verb' \\
    --letter 'R|claims/label|flag|press not substantiation' \\
    --letter 'D|work-record|gap|uncleared draft' \\
    --mode offline
"""

from __future__ import annotations

import argparse
import json

MODES = {
    "offline": "not tool-checked (offline tools)",
    "local": "local support, not tool-checked",
    "method": "method only, not tool-checked",
    "verify": "tool-checked via Prove live MCP",
}

LETTER_CODES = ("T", "R", "U", "S", "E", "D")


def stamp(*, mode: str, skill: str, extra: str = "") -> dict:
    if mode not in MODES:
        raise SystemExit(f"Unknown mode {mode!r}; expected one of {', '.join(MODES)}")
    line = f"TRUSTED / {skill}: {MODES[mode]}"
    if extra.strip():
        line = f"{line}; {extra.strip()}"
    return {"check_line": line, "mode": mode, "skill": skill, "label": MODES[mode]}


def _parse_letter_spec(spec: str) -> dict:
    """Parse CODE|aspect|status|optional note (pipe-separated)."""
    parts = [p.strip() for p in spec.split("|")]
    if len(parts) < 3:
        raise SystemExit(
            f"Letter spec needs CODE|aspect|status[|note]; got {spec!r}"
        )
    code, aspect, status = parts[0], parts[1], parts[2]
    note = parts[3] if len(parts) > 3 else ""
    if code not in LETTER_CODES:
        raise SystemExit(
            f"Unknown letter code {code!r}; expected one of {', '.join(LETTER_CODES)}"
        )
    return {"code": code, "aspect": aspect, "status": status, "note": note}


def letter_summary(*, letters: list[dict], mode: str) -> dict:
    """Emit T/R/U/S/E/D lines plus closing Stamp for trusted-check."""
    if mode not in MODES:
        raise SystemExit(f"Unknown mode {mode!r}; expected one of {', '.join(MODES)}")
    tool_checked = mode == "verify"
    stamp_status = "tool-checked" if tool_checked else "not tool-checked"
    lines: list[str] = []
    for item in letters:
        code = item["code"]
        aspect = item.get("aspect") or ""
        status = item.get("status") or ""
        note = (item.get("note") or "").strip()
        line = f"{code} · {aspect}: {status}"
        if note:
            line = f"{line} · {note}"
        lines.append(line)
    closing = f"Stamp: TRUSTED / trusted-check: {stamp_status}"
    lines.append(closing)
    return {
        "letter_lines": lines,
        "text": "\n".join(lines),
        "mode": mode,
        "skill": "trusted-check",
        "label": stamp_status,
        "check_line": closing,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument(
        "--mode",
        default="offline",
        choices=sorted(MODES),
        help="Prove/offline mode; for --letter-lines drives Stamp tool-checked vs not",
    )
    ap.add_argument("--skill", default="", help="Skill id (required unless --letter-lines)")
    ap.add_argument("--extra", default="")
    ap.add_argument("--json", action="store_true")
    ap.add_argument(
        "--letter-lines",
        action="store_true",
        help="Emit trusted-check letter summary (T·… / R·… / … / Stamp: …)",
    )
    ap.add_argument(
        "--letter",
        action="append",
        default=[],
        metavar="CODE|aspect|status|note",
        help="Repeatable letter row for --letter-lines",
    )
    args = ap.parse_args()

    if args.letter_lines:
        if not args.letter:
            raise SystemExit("--letter-lines requires at least one --letter CODE|aspect|status|note")
        letters = [_parse_letter_spec(s) for s in args.letter]
        out = letter_summary(letters=letters, mode=args.mode)
        if args.json:
            print(json.dumps(out, indent=2))
        else:
            print(out["text"])
        return

    if not args.skill:
        raise SystemExit("--skill is required unless --letter-lines is set")
    out = stamp(mode=args.mode, skill=args.skill, extra=args.extra)
    if args.json:
        print(json.dumps(out, indent=2))
    else:
        print(out["check_line"])


if __name__ == "__main__":
    main()
