---
name: dd-handoff-to-navigator
description: Close the DD→ON loop — fill return packet for Ontology Navigator compare-options / handoff-verify / IC close. Use after IR assemble or scoped workstream grades.
---

# Handoff to Ontology Navigator (return)

## When

DD registers (full or scoped) exist; deal lead needs ON to compare options / close the record. UC02 default; also WF-BR-06 / WF-BR-08 bridges.

## Flow

1. Confirm session contract (`templates/on-dd-session-contract.md`).
2. Fill `templates/handoff-to-navigator-return-packet.md` — graded claims, gaps, conflicts, options with `recommended=false`.
3. Attach IR pointer + `templates/gap-list.md`.
4. Run `scripts/preflight_refuse_scan.py` on the packet prose.
5. Stamp: `python3 tools/stamp_check_line.py --skill handoff-to-navigator --mode assemble`.
6. Tell ON next: `handoff-verify` → `compare-options` → board integrity → `close-the-decision`.

## Hard don'ts

- Do not value the asset / invent rNPV in this packet
- Do not recommend sign
- Do not claim Marketplace Done or enable ASC/FC/Full
- Teaching goldens in `examples/on-dd-use-cases/` stay out of live packs

## Examples

See `examples/on-dd-use-cases/README.md` and workflow twins under `templates/workflows/`.
