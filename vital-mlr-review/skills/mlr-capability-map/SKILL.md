---
name: mlr-capability-map
description: "This skill should be used when the person asks what MLR Review can do, which skill to run, how TRUSTED differs from VERIFY and MLR, whether Medical versus Legal versus Regulatory applies, how to set up vmlr_/vvfy_, or whether a piece is ready for the MLR board. Routes to intake, chairs, compile, verify-handoff, or board-prep. Do not use to approve copy or replace the company MLR committee."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Needs the MLR Review connector (vmlr_) for tool-checked work. VERIFY (vvfy_) optional where named. Without keys, run by hand and label not tool-checked."
metadata:
  framework_code: "MLR-0.0"
  register_code: "MLR-0.0"
  framework_path: "MLR Review > Capability map"
  family: "mlr-core"
  worker: "Cross-functional MLR coordinator"
  pack: "vital-mlr-review"
  version: "0.3.1"
  route:
    - "What can MLR Review do on this host"
    - "Route me to the right MLR skill"
    - "TRUSTED versus VERIFY versus MLR Review"
    - "When do I use Medical versus Legal versus Regulatory chairs"
    - "Is this piece ready for the MLR board"
    - "How do I set up the vmlr key for MLR"
    - "Capability map for MLR board prep"
    - "Do not blend the three MLR chairs"
    - "MLR Review never approves promotional copy"
    - "Start with the MLR capability map"
---

# Capability map

Routeboard for VITAL MLR Review. Explain prep-only scope. Point to the next skill. Never stamp compliance.

## Instructions

1. Read `references/governance.md` stop rules before any user-facing text.
2. Pick the matching task below; follow its Formula and Companion slots.
3. Call tools only with fully qualified names from `references/tools.md`.
4. Run listed scripts for deterministic checks when inputs are files/JSON.
5. Match `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| explain and route | Explain scope and route to the next skill | `tasks/explain-and-route.md` |
| companions | Explain vmlr_/vvfy_ and TRUSTED/VERIFY/MLR | `tasks/companions.md` |
| choose depth | Choose light / short / full review depth | `tasks/choose-depth.md` |

## Scripts

`scripts/check_forbidden_phrases.py`

Run with the host Python. Prefer tool-checked connector results when `vmlr_` / `vvfy_` are present; scripts never replace approval judgment.

## Standard table

| Skill | Own question |
|---|---|
| `mlr-intake` | Markets, audience, channel, artefact version, authorized use per market |
| `mlr-medical-chair` | **M** — clinical/label accuracy, fair balance, clinical evidence |
| `mlr-legal-chair` | **L** — misleading impression, comparative-ad, privacy/IP |
| `mlr-regulatory-chair` | **R** — ISI/format, pre-approval gates, code process, audience/channel |
| `mlr-compile` | Align three chairs; validate; conflict slots |
| `mlr-verify-handoff` | Admit sources / check claims on VERIFY |
| `mlr-board-prep` | Named-human prep record for the committee |

Hard rules detail: `references/hard-rules.md`. Chair MECE: `references/chair-index.md`.

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
| `references/hard-rules.md` | Preserved domain reference |
| `references/chair-index.md` | Preserved domain reference |
| `references/companions.md` | Preserved domain reference |
