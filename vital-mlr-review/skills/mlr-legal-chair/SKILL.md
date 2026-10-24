---
name: mlr-legal-chair
description: "This skill should be used for the legal chair only — misleading impression, comparative-advertising risk, privacy/IP — grounded in legal ruleset rows. Do not use for clinical label truth (mlr-medical-chair), ISI/format process (mlr-regulatory-chair), or approving copy. Not a substitute for external counsel."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-L.1"
  register_code: "MLR-L.1"
  framework_path: "MLR Review > Legal chair"
  family: "mlr-chair"
  worker: "Legal reviewer (host-reasoner)"
  pack: "vital-mlr-review"
  version: "0.3.1"
  chair: "legal"
  route:
    - "Run the legal chair on misleading impression"
    - "Comparative advertising legal risk for MLR"
    - "Load only chairs legal from the ruleset"
    - "Reminder versus product claim legal character"
    - "Privacy and testimonial rights for the legal chair"
    - "Legal findings cite source_ref and claim_span"
    - "Disparagement of Competitor X is a legal chair issue"
    - "Legal chair is not a court determination"
    - "Hand SmPC clinical truth away from legal chair"
    - "Legal chair decision revise is not counsel clearance"
---

# Legal chair

Own misleadingness, comparative and commercial-statement risk, and privacy/IP exposure for board prep. Flag risk for counsel. Never clear copy. Not a court determination.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| load legal rules | Load chairs.legal checklist rows | `tasks/load-legal-rules.md` |
| review misleadingness | Review misleading impression and comparative risk | `tasks/review-misleadingness.md` |
| write legal findings | Emit legal chair packet JSON | `tasks/write-legal-findings.md` |

## Scripts

`scripts/check_finding_shape.py`, `scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Chair boundary (MECE)

| Own (Legal) | Hand off |
|---|---|
| False or misleading impression | Medical label science → `mlr-medical-chair` |
| Comparative advertising / disparagement | Medical evidence adequacy → `mlr-medical-chair` |
| Reminder vs product-claim character | Regulatory ISI requirements → `mlr-regulatory-chair` |
| Privacy, consent, testimonials, IP | — |

See `references/chair-boundaries.md`.

## Tool path

1. Call `vital-mlr-review:mlr_get_ruleset`; apply only `chairs.legal`.
2. Run `scripts/check_finding_shape.py` then `scripts/check_forbidden_phrases.py`.

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
