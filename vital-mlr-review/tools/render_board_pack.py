#!/usr/bin/env python3
"""Assemble reviewer-facing markdown from a compile packet + optional chairs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from contract import LIABILITY_LINE, CHAIRS


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True, help="Packet JSON path")
    p.add_argument("--out", help="Optional markdown output path")
    ns = p.parse_args()
    packet = json.loads(Path(ns.file).read_text(encoding="utf-8"))
    chairs = packet.get("chairs") if isinstance(packet.get("chairs"), dict) else {}
    lines = [
        "# MLR board pack (prep only)",
        "",
        f"- Jurisdictions: {', '.join(packet.get('jurisdictions') or []) or '[GAP]'}",
        f"- Audience / channel: {packet.get('audience') or '[GAP]'} / {packet.get('channel') or '[GAP]'}",
        f"- Artefact version: {packet.get('artefact_version') or '[GAP]'}",
        f"- Status: {packet.get('mlr_status') or 'findings_only'}",
        f"- Ruleset ids: {', '.join(packet.get('ruleset_ids') or []) or '[GAP]'}",
        "",
        "## Chair summaries",
        "",
    ]
    for name in CHAIRS:
        chair = chairs.get(name) or {}
        lines.append(f"### {name.title()}")
        lines.append(f"- Decision: {chair.get('decision') or '[GAP]'}")
        lines.append(f"- Summary: {chair.get('summary') or '[GAP]'}")
        findings = chair.get("findings") or []
        if not findings:
            lines.append("- Findings: none recorded")
        else:
            for f in findings:
                if not isinstance(f, dict):
                    continue
                lines.append(
                    f"- Finding ({f.get('severity') or 'unspecified'}): "
                    f"{f.get('claim_span') or '[GAP]'} — {f.get('rationale') or '[GAP]'} "
                    f"(applies_to: {', '.join(map(str, f.get('applies_to') or [])) or '[GAP]'})"
                )
        lines.append("")
    jurisdictions = [str(j).upper() for j in (packet.get("jurisdictions") or [])]
    channel = str(packet.get("channel") or "").lower()
    lines.extend(
        [
            "## Human gate reminders",
            "",
            "- READY does not approve copy. Named humans and company MLR own clearance.",
        ]
    )
    if "US" in jurisdictions and channel in {"promo", "digital", ""}:
        lines.append(
            "- If company SOP requires FDA Form 2253 after human clearance for US promo: "
            "**human owns filing**. READY does not file or invent a submission id "
            "(see references/post-clearance-deferred.md)."
        )
    lines.extend(
        [
            "",
            "## Liability",
            "",
            LIABILITY_LINE,
            "",
            "READY-local · not tool-checked · findings_only · humans approve",
            "",
        ]
    )
    text = "\n".join(lines)
    if ns.out:
        Path(ns.out).write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
