---
name: premortem
description: "This skill should be used when the user asks to \"What would look wrong in six months if we pick this option?\", \"Capture the failure hypothesis in our words.\", \"What early signal for this failure did we name?\". Do not use it to turn the list into a recommendation or to drop a hypothesis that embarrasses the favorite."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_premortem when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-4.2"
  register_code: "DC-4.2"
  framework_path: "Decision Companion > Pre-mortem"
  family: "make-decision"
  worker: "Decision coach (failure hypotheses)"
  pack: vital-decision-companion
  version: 0.3.3
  route:
    - "look wrong in six months"
    - "capture the failure hypothesis"
    - "early signal for this failure"
    - "don't turn this into advice"
    - "keep the embarrassing failure"
    - "mitigation in our words"
    - "before we treat it as final"
    - "ways this fails"
    - "six month lookback"
    - "store the hypotheses and stop"
---

# Pre-mortem

Method DC-4.2. Primary tool `decision_premortem`. Leave a missing field as `[GAP]`.

## How to do this work

Ask what would make this decision look wrong in six months. Refuse to convert the list into advice. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Capture the hypotheses | The person is looking at how the choice could fail. | `tasks/capture.md` |

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

- Ask for failure, early signal, and mitigation. Leave a missing field as [GAP].
- Store the list with decision_premortem. Do not rank the hypotheses.
- Dig deep and full process require this list before the choice is treated as final.
- A hypothesis the person regrets saying stays on the list.
- The list does not set chosen_option.
- Six months is the prompt. If the person names another horizon, use theirs.

Primary tool: `decision_premortem`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: bias, then make-decision.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/capture.md` | Capture the hypotheses |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
