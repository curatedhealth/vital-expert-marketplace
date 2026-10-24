---
name: mlr-compile
description: "This skill should be used when aligning medical, legal, and regulatory chair packets, calling compile/validate tools, and surfacing conflicts for the board. Trigger when three chairs exist or the person asks to compile the MLR pack. Do not use to invent chair findings or to approve copy."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-4.1"
  register_code: "MLR-4.1"
  framework_path: "MLR Review > Compile"
  family: "mlr-prep"
  worker: "MLR compile lead"
  pack: "vital-mlr-review"
  version: "0.3.1"
  route:
    - "Compile the three MLR chair packets"
    - "Validate the MLR packet for the board"
    - "mlr_validate_packet after chair alignment"
    - "Cross-chair conflict matrix for MLR"
    - "Same artefact_version across MLR chairs"
    - "Fail-close finding forces human_gate_required"
    - "Forbidden approval phrases fail MLR validation"
    - "Stub market gap stays visible at compile"
    - "Chair approve means not blocking human handoff"
    - "Send the compiled MLR pack to committee prep"
---

# Compile

Align three separate advisory chairs and the markets in scope. Refuse a blended single-reviewer packet. Never approve the copy.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| align chairs | Build conflict matrix across chairs and markets | `tasks/align-chairs.md` |
| validate for board | Validate packet and set prep status | `tasks/validate-for-board.md` |

## Scripts

`scripts/validate_packet_shape.py`, `scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Tool path

1. Run `scripts/validate_packet_shape.py` locally.
2. Call `vital-mlr-review:mlr_compile_checklist` then `vital-mlr-review:mlr_validate_packet`.
3. Run `scripts/check_forbidden_phrases.py` on any summary text.
4. Optional next: `mlr-verify-handoff`, then `mlr-board-prep`.

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
| `scripts/validate_packet_shape.py` | Deterministic check — run, do not re-implement |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/status-vocab.md` | Preserved domain reference |
