#!/usr/bin/env python3
"""Closing stamp for READY skills. Never emits approval language."""

from __future__ import annotations

import argparse
from datetime import date

from contract import LIABILITY_LINE, MLR_STATUSES


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--skill", required=True, help="Skill slug, e.g. mlr-intake")
    p.add_argument(
        "--status",
        default="findings_only",
        choices=list(MLR_STATUSES),
    )
    p.add_argument("--tool-checked", action="store_true")
    p.add_argument("--metered", action="store_true")
    p.add_argument("--letter-lines", action="store_true", help="Also print liability line")
    ns = p.parse_args()
    mode = "READY" if ns.tool_checked else "READY-local"
    checked = "tool-checked" if ns.tool_checked else "not tool-checked"
    meter = "metered" if ns.metered else "not metered"
    line = f"{mode} / {ns.skill}: {checked} · {ns.status} · {meter} · {date.today().isoformat()}"
    print(line)
    if ns.letter_lines:
        print(LIABILITY_LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
