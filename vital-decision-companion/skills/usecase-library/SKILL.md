---
name: usecase-library
description: "This skill should be used when the user asks to \"Show me UC01, the competitive launch card.\", \"Walk UC02 beat by beat.\", \"Open the vendor card UC05.\". Do not use it to invent a fourth card or to treat the example as the person's decision."
license: "[CHECK] VITAL Decision Companion terms, to be set by the owner"
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_usecase_card when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-8.1"
  register_code: "DC-8.1"
  framework_path: "Decision Companion > Use-case library"
  family: "library"
  worker: "Decision coach (examples)"
  pack: vital-decision-companion
  version: 0.2.0
  route:
    - "show me uc01"
    - "walk uc02"
    - "vendor card uc05"
    - "don't invent uc03"
    - "gold example only"
    - "which gold card fits"
    - "read the beats"
    - "unknown card stays empty"
    - "use the library not our session"
    - "teaching card"
---

# Use-case library

Method DC-8.1. Primary tool `decision_usecase_card`. Leave a missing field as `[GAP]`.

## How to do this work

Walk the beats of one gold card. Refuse to invent UC03 or to copy the example's choice onto the person's session. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Walk one gold card | The person names UC01, UC02, or UC05, or asks which card fits. | `tasks/walk.md` |

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

- Gold ids are UC01, UC02, and UC05. Any other id returns card null and the gold set.
- Walk beats in order. One beat, then a question.
- The card's decision_type and rigor are applied to the session only when session_id is passed and those fields are still empty.
- Do not treat a beat as the person's choice.
- leverage_packages name other connectors. This skill does not call them.
- Playbook content version is 2026-10-24.1.

Primary tool: `decision_usecase_card`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

Next skill: where-to-start if they want a real session, using the card only as the walk.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/walk.md` | Walk one gold card |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
