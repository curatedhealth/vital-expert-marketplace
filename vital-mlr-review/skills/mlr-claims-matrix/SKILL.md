---
name: mlr-claims-matrix
description: "This skill should be used when operating the mlr-claims-matrix step of READY MLR board prep. Do not use to approve copy or invent clearance."
compatibility: "Runs with Agent Skills offline. Optional vmlr_/vvfy_ MCP when `.mcp.json` is configured. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.4"
  register_code: "MLR-0.4"
  framework_path: "MLR Review > mlr-claims-matrix"
  worker: "MLR claims matrix"
  pack: "vital-mlr-review"
  product: "READY"
  version: "0.4.1"
  release_state: Released
  route:
    - "Run mlr claims matrix on this artefact"
    - "Build pre-chair claims matrix with evidence locators"
    - "Bind each claim to CSR passage or mark GAP"
    - "Claims matrix for comparative and numeric claims"
    - "mlr-claims-matrix DE CH leave-behind"
    - "Align claims against authorized-use text"
    - "Inventory claims before medical legal regulatory chairs"
    - "Atomic claim rows with locators for MLR"
    - "Flag comparative claim for Legal in claims matrix"
    - "Claims matrix revise while locators missing"
---
    # MLR claims matrix

    This skill should be used when building a pre-chair claims matrix that binds verbatim claims to authorised-use text and evidence locators before Medical/Legal/Regulatory write findings. Never approves.

    ## When to use
    After `mlr-capability-map` (and after `mlr-channel-intent` when channel is disputed). Before or beside chairs as the funnel dictates. Never as approval.

    ## Instructions

Follow steps below.

## Steps
    1. Read `intake.md` and gather missing fields only.
    2. Follow `references/method.md`.
    3. Prefer offline tools in `references/tools.md`.
    4. Fill Output cards.
    5. Stamp: `python ../../tools/stamp_ready_line.py --skill mlr-claims-matrix --letter-lines`

    ## Output cards (required)
    - `../../templates/claims-matrix-card.md`
    - `../../templates/liability-line.md`
    - `../../templates/check-line-stamp.md`
    - `../../templates/gap-list.md` when gaps exist

    ## Tasks
    - `inventory-claims.md` — Extract verbatim claims with stable IDs
- `bind-authorised-use.md` — Bind each claim to authorised-use per jurisdiction
- `attach-locators.md` — Require paragraph-level locators or [GAP]

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
- `examples/poor-invented-locators.md`

## Hard rules
- Never approve. Never invent locators or markets.
- Jurisdiction required when markets are in scope — no US default.
- Compose VERIFY; do not fork.
