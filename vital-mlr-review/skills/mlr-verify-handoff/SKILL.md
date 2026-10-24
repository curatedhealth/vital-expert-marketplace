---
name: mlr-verify-handoff
description: "This skill should be used when handing claim/source checks from an MLR packet to Vital Verify: build handoff steps, then qualify_source and check_claim on vvfy_. Trigger when a chair cites a source that must be admitted. Do not use to write M/L/R findings or to approve copy. Without vvfy_, mark not tool-checked."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-5.1"
  register_code: "MLR-5.1"
  framework_path: "MLR Review > Verify handoff"
  family: "mlr-prep"
  worker: "MLR evidence handoff"
  pack: "vital-mlr-review"
  version: "0.3.1"
  route:
    - "Build the MLR verify handoff steps"
    - "mlr_handoff_verify then qualify_source"
    - "check_claim on the admitted source for MLR"
    - "VERIFY happy path from the MLR packet"
    - "One vvfy key only for MLR verify handoff"
    - "Do not invent VERIFY statuses without tools"
    - "Unverifiable claim stays out of the board summary"
    - "Mark MLR verify handoff not tool-checked"
    - "Return VERIFY results into MLR packet notes"
    - "VERIFY pass is not MLR approval"
---

# Verify handoff

Prepare VERIFY call lists and paste results into MLR notes. A VERIFY pass is not MLR approval. Never invent statuses without tools.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| build handoff | Build handoff steps via mlr_handoff_verify | `tasks/build-handoff.md` |
| run verify path | Run qualify_source then check_claim | `tasks/run-verify-path.md` |
| mark unchecked | Mark not tool-checked when vvfy_ absent | `tasks/mark-unchecked.md` |

## Scripts

`scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Tool path

1. Call `vital-mlr-review:mlr_handoff_verify`.
2. With `vvfy_`: `vital-verify:qualify_source` then `vital-verify:check_claim` with admitted source + quoted passage.
3. Without `vvfy_`: run `tasks/mark-unchecked.md`.
4. Run `scripts/check_forbidden_phrases.py` on notes before return.

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
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/verify-compose.md` | Preserved domain reference |
