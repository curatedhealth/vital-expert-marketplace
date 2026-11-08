#!/usr/bin/env python3
"""Structural channel-intent gate (offline). Never approves. Never invents facts."""

from __future__ import annotations

import argparse
import json
import sys

PROMO_SIGNALS = (
    "prescribe",
    "buy",
    "order now",
    "superior",
    "best in class",
    "only therapy",
)
SCIEX_OK = ("unsolicited", "reactive", "response to enquiry", "scientific exchange")


def gate(args: dict) -> dict:
    channel = str(args.get("channel") or "").strip().lower()
    intent = str(args.get("intent") or "").strip().lower()
    proactive = str(args.get("proactive_or_reactive") or "").strip().lower()
    offlabel = str(args.get("offlabel_or_unlicensed") or "").strip().lower()
    body = str(args.get("body") or "").lower()
    gaps: list[str] = []
    if not channel:
        gaps.append("channel")
    if not proactive:
        gaps.append("proactive_or_reactive")

    decision = "human_gate_required"
    rationale = []

    if channel in {"promo", "digital"} or "promo" in intent:
        decision = "treat_as_promo"
        rationale.append("Declared promotional channel/intent.")
    elif channel in {"scientific_exchange", "med_info"} or "scientific" in intent or "med_info" in intent:
        if offlabel in {"yes", "true", "y"} and proactive in {"proactive", "push"}:
            decision = "human_gate_required"
            rationale.append(
                "Proactive off-label / unlicensed content often fails scientific-exchange tests; human gate."
            )
        elif proactive in {"reactive", "unsolicited"} or any(s in body for s in SCIEX_OK):
            decision = (
                "treat_as_scientific_exchange"
                if "med_info" not in channel and "med_info" not in intent
                else "treat_as_med_info"
            )
            rationale.append("Reactive / unsolicited path declared; still not approval.")
        else:
            decision = "human_gate_required"
            rationale.append("Scientific exchange / med_info without clear reactive posture.")
    else:
        gaps.append("unrecognised_channel_or_intent")

    if any(s in body for s in PROMO_SIGNALS) and decision != "treat_as_promo":
        rationale.append("Promotional phrasing detected in body — reconsider channel.")
        if decision.startswith("treat_as_"):
            decision = "human_gate_required"

    return {
        "tool": "channel_intent_gate",
        "ok": not gaps,
        "decision": decision,
        "rationale": rationale,
        "gaps": gaps,
        "mode": "READY-local",
        "tool_checked": False,
        "metered": False,
        "note": "Structural gate only. Humans still classify and approve nothing here.",
        "liability_line": (
            "This prepares material for human MLR review. "
            "It is not medical, legal, or regulatory approval."
        ),
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--args-json", default="-")
    p.add_argument("--file")
    ns = p.parse_args()
    raw = open(ns.file, encoding="utf-8").read() if ns.file else (sys.stdin.read() if ns.args_json == "-" else ns.args_json)
    args = json.loads(raw or "{}")
    out = gate(args if isinstance(args, dict) else {})
    print(json.dumps(out, indent=2, ensure_ascii=False))
    return 0 if out.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
