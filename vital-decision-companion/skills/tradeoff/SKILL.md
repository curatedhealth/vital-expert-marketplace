---
name: tradeoff
description: "This skill should be used when the user asks to \"Build the comparison grid from the criteria we named.\", \"Don't name a winner from the cells.\", \"Store ratings from named people only.\". Do not use it to declare a winner inside Decision Companion."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_tradeoff_matrix when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-4.1"
  register_code: "DC-4.1"
  framework_path: "Decision Companion > Trade-off"
  family: "make-decision"
  worker: "Decision coach (matrix)"
  pack: vital-decision-companion
  version: 0.3.3
  route:
    - "build the comparison grid"
    - "don't name a winner"
    - "ratings from named people"
    - "criteria before scores"
    - "send the cells onward"
    - "the grid is not the choice"
    - "i scored cost"
    - "winner stays empty"
    - "don't average the cells"
    - "store the matrix only"
---

# Trade-off

Method DC-4.1. Primary tool `decision_tradeoff_matrix`. Leave a missing field as `[GAP]`.

## How to do this work

Hold the grid. Refuse to compute a winner. The result keeps winner null. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Store the matrix | The person named criteria and ratings. | `tasks/grid.md` |
| Point a weighted rank elsewhere | The person wants a weighted rank or an MCDA score. | `tasks/handoff.md` |

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

- decision_tradeoff_matrix returns winner null. Speak that. Do not replace it.
- A cell with authored_by ai, model, or assistant is refused.
- Criteria are named before ratings. If the person rates first, stop and ask for criteria.
- A weighted rank is methods_mcda_rank on vital-ontology-navigator with the same human cells and a vont_ key.
- If the vont_ key is missing, say the shared rank is not connected. Do not compute the rank here.
- The matrix does not set chosen_option. That is make-decision.

Primary tool: `decision_tradeoff_matrix`. Also named, and not copied: `methods_mcda_rank`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision when a person states a choice. handoff-navigator when they ask for a weighted rank.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/grid.md` | Store the matrix |
| `tasks/handoff.md` | Point a weighted rank elsewhere |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
