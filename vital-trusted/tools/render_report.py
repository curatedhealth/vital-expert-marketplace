#!/usr/bin/env python3
"""Render Prove report shapes from findings JSON (offline; no network).

Templates: verify-brief, evidence-table, gap-list, source-register, finding-card.
Does not clear a record. Does not invent world facts. Label not tool-checked.

Usage:
  python render_report.py --template evidence-table --json-file findings.json
  python render_report.py --template verify-brief --json-file findings.json --sources sources.json
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any

TEMPLATES = (
    "verify-brief",
    "evidence-table",
    "gap-list",
    "source-register",
    "finding-card",
)
OPEN = ("partial", "unsupported", "contradicted", "unverifiable")
LABEL = "rendered offline, not tool-checked"


def _text(value: Any) -> str:
    return "" if value is None else str(value).strip()


def _summary(findings: list[dict[str, Any]]) -> dict[str, Any]:
    by_status: dict[str, int] = {}
    for finding in findings:
        status = _text(finding.get("status"))
        if not status or status in {"out_of_scope", "not_checked"}:
            continue
        by_status[status] = by_status.get(status, 0) + 1
    open_items = sum(by_status.get(s, 0) for s in OPEN)
    return {"by_status": by_status, "open_items": open_items, "n": len(findings)}


def evidence_table(findings: list[dict[str, Any]]) -> str:
    lines = [
        "| Claim | Status | Source | Locator | Note |",
        "|---|---|---|---|---|",
    ]
    for f in findings:
        claim = _text(f.get("claim") or (f.get("claim_obj") or {}).get("text"))
        status = _text(f.get("status"))
        source = _text((f.get("source") or {}).get("title") or f.get("source_id"))
        locator = _text(f.get("locator") or (f.get("passage") or {}).get("locator"))
        note = _text(f.get("rationale") or f.get("label") or LABEL)
        lines.append(f"| {claim[:120]} | {status} | {source[:60]} | {locator[:40]} | {note[:80]} |")
    if len(findings) == 0:
        lines.append("| (none) | | | | |")
    lines.append("")
    lines.append(f"_{LABEL}_")
    return "\n".join(lines)


def gap_list(findings: list[dict[str, Any]]) -> str:
    gaps = [f for f in findings if _text(f.get("status")) in OPEN]
    lines = ["# Open items", ""]
    if not gaps:
        lines.append("No open support gaps in the supplied findings.")
    for i, f in enumerate(gaps, 1):
        claim = _text(f.get("claim") or (f.get("claim_obj") or {}).get("text"))
        lines.append(f"{i}. **{_text(f.get('status'))}** — {claim}")
        if f.get("rationale"):
            lines.append(f"   - {_text(f.get('rationale'))}")
    lines.extend(["", f"_{LABEL}_"])
    return "\n".join(lines)


def verify_brief(findings: list[dict[str, Any]], sources: list[dict[str, Any]] | None = None) -> str:
    summary = _summary(findings)
    lines = [
        "# Verify brief (offline)",
        "",
        f"- Findings: {summary['n']}",
        f"- Open items: {summary['open_items']}",
        f"- By status: {summary['by_status']}",
        "",
        "## Evidence table",
        "",
        evidence_table(findings),
        "",
        "## Gaps",
        "",
        gap_list(findings),
    ]
    if sources:
        lines.extend(["", "## Sources", ""])
        for s in sources:
            title = _text(s.get("title") or s.get("publisher") or s.get("source_id"))
            lines.append(f"- {title}")
    lines.extend(["", f"_{LABEL}_"])
    return "\n".join(lines)


def source_register(sources: list[dict[str, Any]]) -> str:
    lines = [
        "| Source | Publisher | Date | Tier | Note |",
        "|---|---|---|---|---|",
    ]
    for s in sources:
        lines.append(
            "| {title} | {pub} | {date} | {tier} | {note} |".format(
                title=_text(s.get("title"))[:80],
                pub=_text(s.get("publisher") or s.get("authority"))[:40],
                date=_text(s.get("date"))[:20],
                tier=_text(s.get("tier"))[:20],
                note=_text(s.get("note") or LABEL)[:60],
            )
        )
    if not sources:
        lines.append("| (none) | | | | |")
    lines.extend(["", f"_{LABEL}_"])
    return "\n".join(lines)


def finding_cards(findings: list[dict[str, Any]]) -> str:
    blocks = []
    for i, f in enumerate(findings, 1):
        claim = _text(f.get("claim") or (f.get("claim_obj") or {}).get("text"))
        blocks.append(
            f"### Finding {i}\n"
            f"- Status: {_text(f.get('status'))}\n"
            f"- Claim: {claim}\n"
            f"- Rationale: {_text(f.get('rationale'))}\n"
        )
    if not blocks:
        blocks.append("(no findings)\n")
    return "\n".join(blocks) + f"\n_{LABEL}_\n"


def generate_report(
    *,
    template: str,
    findings: list[dict[str, Any]],
    sources: list[dict[str, Any]] | None = None,
) -> dict[str, Any]:
    if template not in TEMPLATES:
        return {"error": f"Unknown template {template!r}", "templates": list(TEMPLATES)}
    sources = sources or []
    if template == "evidence-table":
        markdown = evidence_table(findings)
    elif template == "gap-list":
        markdown = gap_list(findings)
    elif template == "verify-brief":
        markdown = verify_brief(findings, sources)
    elif template == "source-register":
        markdown = source_register(sources)
    else:
        markdown = finding_cards(findings)
    return {
        "template": template,
        "markdown": markdown,
        "summary": _summary(findings),
        "label": LABEL,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--template", required=True, choices=TEMPLATES)
    ap.add_argument("--json-file", required=True, help="findings JSON file or -")
    ap.add_argument("--sources", default="", help="optional sources JSON file")
    args = ap.parse_args()
    findings = json.load(sys.stdin if args.json_file == "-" else open(args.json_file, encoding="utf-8"))
    if isinstance(findings, dict) and "findings" in findings:
        findings = findings["findings"]
    sources = []
    if args.sources:
        sources = json.load(open(args.sources, encoding="utf-8"))
        if isinstance(sources, dict) and "sources" in sources:
            sources = sources["sources"]
    out = generate_report(template=args.template, findings=list(findings), sources=list(sources))
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
