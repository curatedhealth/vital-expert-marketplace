---
name: mlr-channel-intent
description: "This skill should be used when operating the mlr-channel-intent step of READY MLR board prep. Do not use to approve copy or invent clearance."
compatibility: "Runs with Agent Skills offline. Optional vmlr_/vvfy_ MCP when `.mcp.json` is configured. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.4"
  register_code: "MLR-0.4"
  framework_path: "MLR Review > mlr-channel-intent"
  worker: "MLR channel intent"
  pack: "vital-mlr-review"
  product: "READY"
  version: "0.4.1"
  release_state: Released
  route:
    - "Classify promo versus scientific exchange for MLR"
    - "Channel intent gate before MLR chairs"
    - "Is this scientific exchange or promotional leave-behind"
    - "Unsolicited med info versus branded efficacy PDF"
    - "mlr-channel-intent for DE HCP material"
    - "Gate proactive off-label as scientific exchange"
    - "Channel unknown mixed branding and MI letter"
    - "Treat as promo after channel intent conflict"
    - "Scientific exchange without MI request record"
    - "Channel intent human_gate_required for MLR"
---
    # MLR channel intent

    This skill should be used when classifying whether material is promotional, scientific exchange, or medical information before MLR chairs run. It gates ruleset choice and never approves.

    ## When to use
    After `mlr-capability-map` (and after `mlr-channel-intent` when channel is disputed). Before or beside chairs as the funnel dictates. Never as approval.

    ## Instructions

Follow steps below.

## Steps
    1. Read `intake.md` and gather missing fields only.
    2. Follow `references/method.md`.
    3. Prefer offline tools in `references/tools.md`.
    4. Fill Output cards.
    5. Stamp: `python ../../tools/stamp_ready_line.py --skill mlr-channel-intent --letter-lines`

    ## Output cards (required)
    - `../../templates/channel-intent-card.md`
    - `../../templates/liability-line.md`
    - `../../templates/check-line-stamp.md`
    - `../../templates/gap-list.md` when gaps exist

    ## Tasks
    - `classify-channel.md` — Classify promo vs scientific_exchange vs med_info
- `record-reactive-posture.md` — Capture proactive vs unsolicited reactive facts

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
- `examples/poor-proactive-offlabel-as-sciex.md`

## Hard rules
- Never approve. Never invent locators or markets.
- Jurisdiction required when markets are in scope — no US default.
- Compose VERIFY; do not fork.
