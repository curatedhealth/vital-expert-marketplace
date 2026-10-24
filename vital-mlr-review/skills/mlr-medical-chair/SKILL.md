---
name: mlr-medical-chair
description: "This skill should be used for the medical chair only — scientific and clinical accuracy against authorized labeling (PI, SmPC, Fachinformation), fair balance, and clinical substantiation grounded in medical ruleset rows. Do not use for legal misleadingness, ISI/format gates, or approving copy."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-M.1"
  register_code: "MLR-M.1"
  framework_path: "MLR Review > Medical chair"
  family: "mlr-chair"
  worker: "Medical reviewer (host-reasoner)"
  pack: "vital-mlr-review"
  version: "0.3.1"
  chair: "medical"
  route:
    - "Run the medical chair against the Fachinformation"
    - "Medical chair fair balance of benefit and risk"
    - "Clinical accuracy versus authorized labeling for MLR"
    - "Load only chairs medical from the ruleset"
    - "Medical findings cite source_ref and claim_span"
    - "Off-label scientific framing for the medical chair"
    - "Invented efficacy figure stays a medical gap"
    - "SmPC consistency check by the medical chair"
    - "Medical chair decision revise is not board clearance"
    - "Hand ISI format questions away from medical chair"
---

# Medical chair

Own scientific and clinical accuracy for MLR board preparation. Leave legal misleadingness and regulatory format/process to sibling chairs. Never clear copy.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| load medical rules | Load chairs.medical checklist rows | `tasks/load-medical-rules.md` |
| review against label | Review claims against authorized use | `tasks/review-against-label.md` |
| write medical findings | Emit medical chair packet JSON | `tasks/write-medical-findings.md` |

## Scripts

`scripts/check_finding_shape.py`, `scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Chair boundary (MECE)

| Own (Medical) | Hand off |
|---|---|
| Consistency with authorized labeling / SmPC / PI / FI | Legal → `mlr-legal-chair` |
| Clinical fair balance of benefit vs risk | Regulatory ISI/process → `mlr-regulatory-chair` |
| Adequacy of clinical evidence for comparative claims | Legal comparative-ad → `mlr-legal-chair` |
| Off-label scientific framing | Regulatory pre-approval control → `mlr-regulatory-chair` |
| Invented efficacy/safety figures | VERIFY → `mlr-verify-handoff` |

See `references/chair-boundaries.md` and `references/standards-by-market.md`.

## Tool path

1. Call `vital-mlr-review:mlr_get_ruleset`; apply only `chairs.medical`.
2. Optional `vital-mlr-review:mlr_align_claims` when authorized-use text exists.
3. Run `scripts/check_finding_shape.py` before emit.
4. Run `scripts/check_forbidden_phrases.py` on the summary.

## Boundaries

| Question | Where it goes |
|---|---|
| What can this pack do / which skill | `mlr-capability-map` |
| Markets and ruleset load | `mlr-intake` |
| Clinical / label accuracy | `mlr-medical-chair` |
| Misleadingness / comparative-ad / privacy | `mlr-legal-chair` |
| ISI / format / pre-approval process | `mlr-regulatory-chair` |
| Align + validate | `mlr-compile` |
| Passage / source proof | `mlr-verify-handoff` |
| Named-human prep record | `mlr-board-prep` |


## Hard rules (every MLR skill)

- **MLR-H1.** Only stored material counts — fields from the person or a tool result.
- **MLR-H2.** Teaching material is never input — examples/ and patterns.md are invented for shape.
- **MLR-H3.** Never approve — no approved-for-use, mlr_reviewed, or regulator-compliant stamp.
- **MLR-H4.** Never simulate the connector — without vmlr_/vvfy_ label not tool-checked.
- **MLR-H5.** A named human owns prep records — refuse ai/model/assistant/system as cleared_by.
- **MLR-H6.** Markets explicit — never default jurisdictions to the US.
- **MLR-H7.** Keep M / L / R MECE — do not blend chairs or substitute another market's rules.
- **MLR-H8.** Plain liability — every user-facing result ends with the closing line.

## What to return

Sections in `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Files

| File | Role |
|---|---|
| `tasks/` | Formula tasks for this skill |
| `references/tools.md` | Fully qualified MCP tool names |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Route and refuse cases |
| `scripts/check_finding_shape.py` | Deterministic check — run, do not re-implement |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/chair-boundaries.md` | Preserved domain reference |
| `references/finding-shape.md` | Preserved domain reference |
| `references/standards-by-market.md` | Preserved domain reference |
