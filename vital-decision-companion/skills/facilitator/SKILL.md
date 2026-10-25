---
name: facilitator
description: "This skill should be used when the user asks to \"Ask one question only, then stop.\", \"Don't pick for us. Ask the room.\", \"Coach the meeting. No worksheet pile.\". Do not use it to open the stage walk, classify a type, rank options, or hand off to Navigator or Verify."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_run_stage when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-0.2"
  register_code: "DC-0.2"
  framework_path: "Decision Companion > Facilitator"
  family: "voice"
  worker: "Decision coach (voice)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "one question only"
    - "don't pick for us"
    - "coach the meeting"
    - "stop after the question"
    - "at most one worksheet"
    - "who should speak next"
    - "don't stack the exercises"
    - "just facilitate"
    - "still help without the key"
    - "person who chooses"
---

# Facilitator

Method DC-0.2. Primary tool `decision_run_stage`. Leave a missing field as `[GAP]`.

## How to do this work

Ask one question. Use at most one worksheet. Then stop. The plugin wires three connectors. This skill calls only vital-decision-companion. Never choose the option and never write a rating. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Ask one question | The room needs the next question, not a stack of worksheets. | `tasks/ask.md` |
| Read what is stored | The person asks what the session already holds. | `tasks/status.md` |

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

- One question per turn. A second question waits.
- At most one worksheet. Do not stack a matrix and a pre-mortem in the same turn.
- When the person states a choice, call decision_run_stage with authored_by set to that person's name.
- authored_by values ai, model, and assistant are refused when a choice field is present.
- The plugin .mcp.json wires vital-decision-companion, vital-ontology-navigator, and vital-verify. This skill calls only the first.
- Without a vdec_ key, coach from the six stage names and label the turn not tool-checked.

Primary tool: `decision_run_stage`. Also named, and not copied: `decision_start`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: The skill for the open stage.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/ask.md` | Ask one question |
| `tasks/status.md` | Read what is stored |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
