#!/usr/bin/env python3
"""Assemble reviewer-facing markdown from a compile packet (schema `compile_packet`).

Reads the schema's own fields (TEH-RDY-041): chair `decision`, `comments`, `findings`
(`rule_id`, `severity`, `claim_span`, `issue`, `recommended_action`, `applies_to`) and `gaps`,
and the packet's own `mlr_status`. Accepts a bare compile packet, a `{"packet": ...}` wrapper
or a prep record (`{"compile": ...}`). A missing value prints `[GAP]`; nothing is defaulted.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from contract import LIABILITY_LINE, CHAIRS

DEFERRED_2253 = "[DEFERRED] Form 2253 — out of READY scope"


def _unwrap(doc: object) -> dict:
    if not isinstance(doc, dict):
        return {}
    if isinstance(doc.get("packet"), dict):
        return doc["packet"]
    if isinstance(doc.get("compile"), dict):
        return doc["compile"]
    return doc


def _join(values: object) -> str:
    return ", ".join(str(v) for v in (values or []) if str(v).strip()) if isinstance(values, list) else ""


def _version_mismatches(packet: dict, chairs: dict) -> list[str]:
    """TEH-RDY-046: each chair's artefact_version against the packet header, exactly as supplied."""
    header = str(packet.get("artefact_version") or "").strip()
    out = []
    for name in CHAIRS:
        chair = chairs.get(name) if isinstance(chairs.get(name), dict) else {}
        ver = str(chair.get("artefact_version") or "").strip()
        if header and ver and ver != header:
            out.append(f"packet header {header} vs {name} {ver}")
    return out


def render(doc: object) -> str:
    packet = _unwrap(doc)
    chairs = packet.get("chairs") if isinstance(packet.get("chairs"), dict) else {}
    status = packet.get("mlr_status") or "[GAP]"
    mismatches = _version_mismatches(packet, chairs)
    if mismatches and status in ("prep_complete", "findings_only", "[GAP]"):
        # A packet whose chair versions differ from its header fails validation; never prep_complete.
        # The mismatch is a correctable validation problem, so the status is at least revise; any
        # reject / abstain chair decision makes it human_gate_required (TEH-RDY-050).
        decisions = {str((chairs.get(c) or {}).get("decision") or "") for c in CHAIRS if isinstance(chairs.get(c), dict)}
        status = "human_gate_required" if decisions & {"reject", "abstain"} else "revise"
    lines = [
        "# MLR board pack (prep only)",
        "",
        f"- Jurisdictions: {_join(packet.get('jurisdictions')) or '[GAP]'}",
        f"- Artefact version: {packet.get('artefact_version') or '[GAP]'}",
        f"- Status: {status}",
        f"- Ruleset ids: {_join(packet.get('ruleset_ids')) or '[GAP]'}",
        "",
        "## Chair summaries",
        "",
    ]
    for name in CHAIRS:
        chair = chairs.get(name) if isinstance(chairs.get(name), dict) else {}
        lines.append(f"### {name.title()}")
        if not chair:
            lines.append("- [GAP] chair packet not supplied")
            lines.append("")
            continue
        lines.append(f"- Artefact version: {chair.get('artefact_version') or '[GAP]'}")
        lines.append(f"- Decision: {chair.get('decision') or '[GAP]'}")
        lines.append(f"- Ruleset: {chair.get('ruleset_id') or '[GAP]'}")
        comments = [str(c) for c in (chair.get("comments") or []) if str(c).strip()]
        lines.append(f"- Comments: {' '.join(comments) if comments else 'none recorded'}")
        findings = [f for f in (chair.get("findings") or []) if isinstance(f, dict)]
        if not findings:
            lines.append("- Findings: none recorded")
        for f in findings:
            lines.append(
                f"- Finding {f.get('id') or '[GAP]'} ({f.get('severity') or '[GAP]'}, "
                f"{f.get('rule_id') or '[GAP]'}): \"{f.get('claim_span') or '[GAP]'}\" — "
                f"{f.get('issue') or '[GAP]'} → {f.get('recommended_action') or '[GAP]'} "
                f"(applies_to: {_join(f.get('applies_to')) or '[GAP]'})"
            )
        for g in (chair.get("gaps") or []):
            if isinstance(g, dict):
                lines.append(f"- Gap {g.get('code') or '[GAP]'}: {g.get('detail') or '[GAP]'}")
        lines.append("")
    conflicts = [c for c in (packet.get("conflicts") or []) if isinstance(c, dict)]
    if conflicts:
        lines.extend(["## Conflicts", ""])
        for c in conflicts:
            lines.append(f"- {c.get('topic') or '[GAP]'}: {c.get('detail') or '[GAP]'}")
        lines.append("")
    if mismatches:
        lines.extend(["## Version check", "",
                      "- Artefact version mismatch — validation fails; the board pack is not ready:"])
        lines.extend(f"  - {m}" for m in mismatches)
        lines.append("")
    jurisdictions = [str(j).upper() for j in (packet.get("jurisdictions") or [])]
    lines.extend(["## Human gate reminders", "",
                  "- READY does not approve copy. Named humans and company MLR own clearance."])
    if "US" in jurisdictions:
        lines.append(f"- {DEFERRED_2253}")
    lines.extend(["", "## Liability", "", LIABILITY_LINE, "",
                  f"READY-local · not tool-checked · {status} · humans approve", ""])
    return "\n".join(lines)


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--file", required=True, help="Packet JSON path")
    p.add_argument("--out", help="Optional markdown output path")
    ns = p.parse_args()
    text = render(json.loads(Path(ns.file).read_text(encoding="utf-8")))
    if ns.out:
        Path(ns.out).write_text(text, encoding="utf-8")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
