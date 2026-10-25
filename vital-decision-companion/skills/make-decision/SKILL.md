---
name: make-decision
description: "This skill should be used when the user asks to \"Record the option we chose, under my name.\", \"We have decided; store the choice.\", \"Make sure the assistant does not decide this for us.\". Do not use it to pick an option, to set authored_by to the assistant, or to treat a matrix as the choice."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_run_stage when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-4.4"
  register_code: "DC-4.4"
  framework_path: "Decision Companion > Make the decision"
  family: "make-decision"
  worker: "Decision coach (choice recorder)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "store the choice we made"
    - "record the choice we stated"
    - "don't let the assistant decide"
    - "the grid is not our choice"
    - "who is stating the choice"
    - "store it under my name"
    - "authored by a person"
    - "say the choice back"
    - "leave it blank until we speak"
    - "make the decision stage"
---

# Make the decision

Method DC-4.4. Primary tool `decision_run_stage`. Leave a missing field as `[GAP]`.

## How to do this work

Record the sentence the person said. Refuse to author the choice. A missing name stops the stage. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Record the person's choice | A named person stated the choice in this conversation. | `tasks/record.md` |
| Final check before storing | Rigor is tradeoff or above and the person is about to state the choice. | `tasks/final-check.md` |

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

- Payload keys choice, chosen_option, decision, or winner with authored_by ai, model, or assistant are refused.
- The stage completes only when chosen_option is present and the author was not refused.
- Default author in the tool is owner only when a human choice was accepted. Prefer the name the person gave.
- Read the option back. Ask if that is the choice. Then store.
- A matrix winner is always null. It cannot fill chosen_option.
- Speak Make the decision. The stage id stays make_decision.

Primary tool: `decision_run_stage`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: daii.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/record.md` | Record the person's choice |
| `tasks/final-check.md` | Final check before storing |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
