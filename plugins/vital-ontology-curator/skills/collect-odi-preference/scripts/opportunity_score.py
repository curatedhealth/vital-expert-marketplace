#!/usr/bin/env python3
"""Ulwick opportunity = I + max(I - S, 0)."""

from __future__ import annotations

import argparse
import json


def opportunity(importance: float, satisfaction: float) -> float:
    return float(importance) + max(float(importance) - float(satisfaction), 0.0)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--importance", type=float, required=True)
    p.add_argument("--satisfaction", type=float, required=True)
    args = p.parse_args()
    opp = opportunity(args.importance, args.satisfaction)
    print(json.dumps({"importance": args.importance, "satisfaction": args.satisfaction, "opportunity": opp}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
