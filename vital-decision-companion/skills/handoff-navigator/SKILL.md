---
name: handoff-navigator
description: "This skill should be used when the user asks to \"Score this on Navigator. Do not score it here.\", \"Put the weighted rank elsewhere, on Navigator.\", \"Hand the cells across to Ontology Navigator.\". Do not use it to recompute ODI, MCDA, a scenario, or a tornado inside Decision Companion."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_handoff_navigator when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-9.1"
  register_code: "DC-9.1"
  framework_path: "Decision Companion > Handoff to Navigator"
  family: "handoff"
  worker: "Decision coach (navigator handoff)"
  pack: vital-decision-companion
  version: 0.3.0
  route:
    - "score this on navigator"
    - "weighted rank elsewhere"
    - "hand the cells across"
    - "speak approach"
    - "don't compute mcda here"
    - "navigator packet"
    - "ontology score not ours"
    - "call navigator next"
    - "no rank in the companion"
    - "methods stay on navigator"
---

# Handoff to Navigator

Method DC-9.1. Primary tool `decision_handoff_navigator`. Leave a missing field as `[GAP]`.

## How to do this work

Hand the cells across. Refuse to score them here. Speak Approach. The Navigator stage id stays options. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Build the packet | The person wants a score and the cells are already stored. | `tasks/packet.md` |
| Call Navigator | The packet is ready and `vont_` is connected. | `tasks/call.md` |

## How deep to go

One worksheet. One question after it, when a person must answer. Then stop. Codes stay in the tool payload. Speak the stage label.

## Rules that hold for every task

These apply on every Decision Companion skill. Plain words go to the person. Ids stay here.

- **Only stored material counts (DC-H1).** Fields come from the person or from a tool result in this conversation.
- **Teaching material is never input (DC-H2).** Names and figures in `examples/` and `references/patterns.md` are invented for shape. Do not copy them into a live answer.
- **A worksheet is not a decision (DC-H3).** A matrix, a bias card, a type draft, and a brief do not choose the option.
- **Never simulate the connector (DC-H4).** Without `vdec_`, run the method by hand, label the turn **not tool-checked**, and do not invent a session id, a Verify status, or a Navigator score.
- **A named person decides (DC-H5).** `authored_by` is a human name. Values `ai`, `model`, and `assistant` are refused on choice fields.
- **No clinical, legal, or regulatory advice (DC-H6).**
- **Ask for what changes the answer (DC-H7).**
- **Plain language (DC-H8).** Speak stage labels. Keep stage ids in the payload.

Skill-specific:

- Call decision_handoff_navigator first. called_navigator is false. This connector does not call Navigator over HTTP.
- Speak Approach. suggested_stage_entry is options. compile_key is 4_options.
- Then call the named tool on vital-ontology-navigator: decide_start or a methods_* tool.
- methods_mcda_rank receives the same human cells. Decision Companion does not average them.
- Without a vont_ key, say the shared tool is not connected.
- People supply scores. The coach does not.

Primary tool: `decision_handoff_navigator`. Also named, and not copied: `decide_start`, `methods_odi_score`, `methods_opportunity_score`, `methods_mcda_rank`, `methods_nav_compute`, `methods_scenario`, `methods_risk_tornado`, `methods_capability_gap`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision once a person states a choice. The rank is an input, not the choice.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/packet.md` | Build the packet |
| `tasks/call.md` | Call Navigator |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
