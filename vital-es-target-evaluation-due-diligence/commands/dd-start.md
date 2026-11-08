---
name: dd-start
description: Session router for Target Evaluation & Due Diligence (CF-01.02.06). Use at session start or when unsure which DD skill to open.
---

# DD start (session router)

Craft **A05**. Load capability-map first; then branch.

## Route

| User intent | Next |
|---|---|
| New engagement / intake | `/dd-intake` → `templates/workstream-intake.md` |
| Single workstream | Matching skill (F/A/B/C/D/E/G/R/H) via hooks phrases |
| Integrated report | `commands/dd-integrated-report.md` + `assemble_report` |
| Preflight / share draft | `/dd-preflight-refuse` |
| Release claim language | Read `evals/RELEASE_GATE.md` — eng ≠ Pass ≠ Marketplace |
| Return grades to Ontology Navigator | `/dd-handoff-to-navigator` + `examples/on-dd-use-cases/` |
| Joint UC workflows | `templates/workflows/README.md` (UC02 + UC06/UC08 bridges) |

## Inject standing context

- ASC / FC-* / Full = Accepted Deferred (disabled)
- FTO / tax / QoE / GO–NO-GO = HUMAN ONLY
- COI disclosure ≠ clearance
- `scripts/preflight_refuse_scan.py` before external share

## Hard don'ts

No self-Pass of Standard KA; no Studio Marketplace Done; no inventing exclusivity end dates for US-NCE1-4Y.
