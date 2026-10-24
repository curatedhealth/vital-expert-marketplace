---
name: mlr-board-prep
description: "This skill should be used when producing the reviewer-facing MLR board packet and calling mlr_build_prep_record with a named human owner after compile. Do not use to stamp approved or mlr_reviewed, to write chair findings, or to run VERIFY alone."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-6.1"
  register_code: "MLR-6.1"
  framework_path: "MLR Review > Board prep"
  family: "mlr-prep"
  worker: "MLR coordinator"
  pack: "vital-mlr-review"
  version: "0.3.1"
  route:
    - "Assemble the MLR board pack for the committee"
    - "Build the MLR prep record with a named human"
    - "mlr_build_prep_record requires cleared_by name"
    - "prep_cleared_for_human_mlr is not approved for use"
    - "mlr_reviewed stays false on the prep record"
    - "Refuse system as cleared_by for MLR prep"
    - "Surface stub market gaps on the board cover"
    - "Keep chair disagreements visible in the board pack"
    - "Point the board pack at the company MLR SOP"
    - "Send the prep record to tomorrow's MLR committee"
---

# Board prep

Assemble what humans on the MLR committee will read. `prep_cleared_for_human_mlr` means ready for their process — not cleared for use. Require a named human owner.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| assemble board pack | Assemble reviewer-facing board cover | `tasks/assemble-board-pack.md` |
| build prep record | Build prep record with named human | `tasks/build-prep-record.md` |

## Scripts

`scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Tool path

1. Confirm prior `vital-mlr-review:mlr_validate_packet` (or explicit gate).
2. Call `vital-mlr-review:mlr_build_prep_record` with `cleared_by.name` set to a human.
3. Run `scripts/check_forbidden_phrases.py` on the board cover.

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
| `references/board-pack-shape.md` | Preserved domain reference |
| `references/status-vocab.md` | Preserved domain reference |
