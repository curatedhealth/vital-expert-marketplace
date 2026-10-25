---
name: where-to-start
description: "This skill should be used when the user asks to \"Can we open a session for the agency award?\", \"Where do we start on this leadership choice?\", \"Which stage is next in the coaching session?\". Do not use it to classify a statement, score a matrix, check a claim, or write the brief."
license: "[CHECK] VITAL Decision Companion terms, to be set by the owner"
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_start when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-0.1"
  register_code: "DC-0.1"
  framework_path: "Decision Companion > Where to start"
  family: "session"
  worker: "Decision coach (session opener)"
  pack: vital-decision-companion
  version: 0.2.0
  route:
    - "open a session"
    - "where do we start"
    - "which stage is next"
    - "walk me through the decision"
    - "what intent should we use"
    - "show me the stage list"
    - "is this practice mode"
    - "session has not been opened"
    - "carry this session forward"
    - "stages still to do"
---

# Where to start

Method DC-0.1. Primary tool `decision_start`. Leave a missing field as `[GAP]`.

## How to do this work

Open the session and keep the stage list honest. Refuse an invented session id. Show the template menu when the intent is missing. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Open the session | No session exists yet, or the title or intent is missing. | `tasks/open.md` |
| Walk the open stage | A session id already exists. | `tasks/walk.md` |

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

- Intents are quick, tradeoff, deep, full, and classify_first. An unknown intent is refused.
- Without an intent, decision_start returns opened false and the template menu. Ask which intent.
- Pass session_id on every later call. Chat memory is not the session.
- decision_status names the open stage. Speak the label. Keep the stage id in the tool payload.
- Practice mode returns watermark SIMULATED. Say the session is practice.
- Persistence in this build is process memory. durable_connected is false. Do not claim the row was saved to a database.

Primary tool: `decision_start`. Also named, and not copied: `decision_status`, `decision_run_stage`.

## What to return

The sections in `assets/worksheet-output.md`. End with the closing line in `references/governance.md`.

Next skill: classify when the person is unsure of the type; otherwise the open stage's skill.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/open.md` | Open the session |
| `tasks/walk.md` | Walk the open stage |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
