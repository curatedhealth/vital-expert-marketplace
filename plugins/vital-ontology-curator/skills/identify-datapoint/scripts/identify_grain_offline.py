#!/usr/bin/env python3
"""Offline identify_grain (no MCP). PYTHONPATH must include mcps/."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]  # mcps/
sys.path.insert(0, str(ROOT))

from ontology_curator.identify_grain import identify_grain  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--quote", default="")
    p.add_argument("--url", default="")
    p.add_argument("--subject", default="")
    p.add_argument("--vp", default="")
    args = p.parse_args()
    print(json.dumps(identify_grain(
        quote=args.quote, url=args.url, subject_hint=args.subject, vp_hint=args.vp
    ), indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
