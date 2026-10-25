---
name: bias
description: "This skill should be used when the user asks to \"Which bias is in the room, if we can name it?\", \"Read the confirmation bias card and the countermeasure.\", \"We are anchoring on the first number. What do we do?\". Do not use it to clear a bias, ignore a flagged risk, or pick the favorite option."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_bias_check when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-4.3"
  register_code: "DC-4.3"
  framework_path: "Decision Companion > Bias"
  family: "make-decision"
  worker: "Decision coach (bias card)"
  pack: vital-decision-companion
  version: 0.3.0
  route:
    - "which bias is in the room"
    - "confirmation bias card"
    - "anchoring on the first number"
    - "sunk cost card"
    - "groupthink countermeasure"
    - "don't say we are unbiased"
    - "name the bias we see"
    - "bias card only"
    - "countermeasure we can do now"
    - "refuse a clean bill"
---

# Bias

Method DC-4.3. Primary tool `decision_bias_check`. Leave a missing field as `[GAP]`.

## How to do this work

Read the countermeasure and ask the person to do it. Refuse to declare the room unbiased. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Read the bias card | The person names a bias or asks which bias is in the room. | `tasks/read.md` |
| By-hand bias prompts by stage | The tool card has no item for this stage or type. | `tasks/by-stage.md` |

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

- Pass decision_type or session_id. With a session and no type, the tool uses the stored type.
- Matched items are those whose types include the decision type. With no type, the full card returns.
- The four items in pack 2026-10-24.1 are confirmation, anchoring, sunk_cost, and groupthink.
- draft is true. Do not say the decision is unbiased.
- Read the countermeasure. Ask the person to do that step. Do not do it for them.
- This skill does not set chosen_option.

Primary tool: `decision_bias_check`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision after the person has answered the countermeasure they choose to answer.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/read.md` | Read the bias card |
| `tasks/by-stage.md` | By-hand bias prompts by stage |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
