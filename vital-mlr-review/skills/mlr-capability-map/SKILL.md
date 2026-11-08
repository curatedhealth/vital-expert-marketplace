---
name: mlr-capability-map
description: "This skill should be used when the person asks what MLR Review can do, which skill to run, how TRUSTED differs from VERIFY and MLR, whether Medical versus Legal versus Regulatory applies, how to set up vmlr_/vvfy_, or whether a piece is ready for the MLR board. Routes to intake, chairs, compile, verify-handoff, or board-prep. Do not use to approve copy or replace the company MLR committee."
license: "[CHECK] VITAL MLR Review terms — set before marketplace publish"
compatibility: "Runs offline with skills + local tools. Optional vmlr_/vvfy_ when `.mcp.json` opted in. Without keys label not tool-checked and stamp READY-local."
metadata:
  framework_code: "MLR-0.0"
  register_code: "MLR-0.0"
  framework_path: "MLR Review > Capability map"
  family: "mlr-core"
  worker: "Cross-functional MLR coordinator"
  pack: "vital-mlr-review"
  version: "0.4.1"
  release_state: Released
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
5. Match `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

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
| `mlr-channel-intent` | Promo vs scientific exchange vs med_info gate |
| `mlr-intake` | Markets, audience, channel, artefact version, authorized use per market |
| `mlr-claims-matrix` | Pre-chair verbatim claims + locators + authorised-use bind |
| `mlr-medical-chair` | **M** — clinical/label accuracy, clinical evidence |
| `mlr-legal-chair` | **L** — misleading impression, comparative-ad, privacy/IP |
| `mlr-fair-balance-isi` | Fair balance / ISI / net impression (prep) |
| `mlr-regulatory-chair` | **R** — format, pre-approval gates, code process, audience/channel overlays |
| `mlr-compile` | Align chairs; validate; conflict slots; reconciliation |
| `mlr-verify-handoff` | Admit sources / check claims on VERIFY (or offline packet) |
| `mlr-board-prep` | Named-human prep record for the committee |

Hard rules detail: `references/hard-rules.md`. Chair MECE: `references/chair-index.md`. Funnel: `../../workflows/offline-prep-e2e.md`.

## Boundaries

| Question | Where it goes |
|---|---|
| What can this pack do / which skill | `mlr-capability-map` |
| Promo vs scientific exchange | `mlr-channel-intent` |
| Markets and ruleset load | `mlr-intake` |
| Claims matrix / locators | `mlr-claims-matrix` |
| Clinical / label accuracy | `mlr-medical-chair` |
| Misleadingness / comparative-ad / privacy | `mlr-legal-chair` |
| Fair balance / ISI prominence | `mlr-fair-balance-isi` |
| Format / pre-approval process | `mlr-regulatory-chair` |
| Align + validate | `mlr-compile` |
| Passage / source proof | `mlr-verify-handoff` |
| Named-human prep record | `mlr-board-prep` |



## Closing stamp

End every user-facing turn with `python tools/stamp_ready_line.py --skill mlr-capability-map --status <status>` (see `templates/check-line-stamp.md`). Optional `--letter-lines` prints the liability line.

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

Sections in `../../templates/` Output cards (see SKILL.md). End with the closing line in `references/governance.md`.

## Files

| File | Role |
|---|---|
| `tasks/` | Formula tasks for this skill |
| `references/tools.md` | Fully qualified MCP tool names |
| `references/knowledge.md` | Skill rules |
| `references/knowledge.md` | Shapes, not facts |
| `references/failure-modes.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `../../templates/` Output cards (see SKILL.md) | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Route and refuse cases |
| `scripts/check_forbidden_phrases.py` | Deterministic check — run, do not re-implement |
| `references/hard-rules.md` | Preserved domain reference |
| `references/chair-index.md` | Preserved domain reference |
| `references/companions.md` | Preserved domain reference |
