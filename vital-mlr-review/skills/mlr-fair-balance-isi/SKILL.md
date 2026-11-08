---
name: mlr-fair-balance-isi
description: "This skill should be used when operating the mlr-fair-balance-isi step of READY MLR board prep. Do not use to approve copy or invent clearance."
compatibility: "Runs with Agent Skills offline. Optional vmlr_/vvfy_ MCP when `.mcp.json` is configured. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.4"
  register_code: "MLR-0.4"
  framework_path: "MLR Review > mlr-fair-balance-isi"
  worker: "MLR fair balance isi"
  pack: "vital-mlr-review"
  product: "READY"
  version: "0.4.1"
  release_state: Released
  route:
    - "Check fair balance and ISI prominence for MLR"
    - "ISI present but tiny type versus benefit headlines"
    - "mlr-fair-balance-isi US and DE panels"
    - "Score ISI proximity and typography contrast"
    - "Fair balance checklist before regulatory chair"
    - "Do not draft final approved ISI"
    - "DE panel incomplete versus Fachinformation safety"
    - "Important Safety Information placement review"
    - "Fair balance revise when prominence weak"
    - "standards-by-market fair balance scoring"
---
    # MLR fair balance and ISI

    This skill should be used when checking fair balance, Important Safety Information placement, indication prominence, and net impression risks for promotional materials. It prepares Regulatory-facing findings and never approves.

    ## When to use
    After `mlr-capability-map` (and after `mlr-channel-intent` when channel is disputed). Before or beside chairs as the funnel dictates. Never as approval.

    ## Instructions

Follow steps below.

## Steps
    1. Read `intake.md` and gather missing fields only.
    2. Follow `references/method.md`.
    3. Prefer offline tools in `references/tools.md`.
    4. Fill Output cards.
    5. Stamp: `python ../../tools/stamp_ready_line.py --skill mlr-fair-balance-isi --letter-lines`

    ## Output cards (required)
    - `../../templates/isi-fair-balance-checklist.md`
    - `../../templates/liability-line.md`
    - `../../templates/check-line-stamp.md`
    - `../../templates/gap-list.md` when gaps exist

    ## Tasks
    - `scan-isi-presence.md` — Scan for ISI / brief summary / PI pointers
- `score-prominence.md` — Compare benefit vs risk prominence factors
- `write-fair-balance-findings.md` — Write findings_only / revise cards

## References
| Path | Role |
|---|---|
| `references/method.md` | How to run |
| `references/method-standards.md` | WC-* citations |
| `references/knowledge.md` | Domain knowledge |
| `references/failure-modes.md` | Failure library |
| `references/tools.md` | Offline + optional MCP |
| `references/without-connector.md` | No-keys path |
| `governance.md` | Never-approve law |

## Examples
- `examples/good-sourced-draft.md`
- `examples/poor-indication-only-in-isi.md`

## Hard rules
- Never approve. Never invent locators or markets.
- Jurisdiction required when markets are in scope — no US default.
- Compose VERIFY; do not fork.
