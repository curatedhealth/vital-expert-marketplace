---
name: frame-decision
description: "This skill should be used when the user asks to \"Help us frame this decision before we look at options.\", \"How much rigor does this deserve?\", \"Who decides, by when, and what is the goal?\". Do not use it to list options, score a matrix, record the choice, or write the brief."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_run_stage when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-1.0"
  register_code: "DC-1.0"
  framework_path: "Decision Companion > Frame the decision"
  family: "how-to-decide"
  worker: "Decision coach (framing)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "frame this decision"
    - "how much rigor"
    - "who decides and by when"
    - "what is the goal"
    - "core of the issue"
    - "consequence and reversibility"
    - "decide how to decide"
    - "is now the right time"
    - "what criteria will we use"
    - "how should we decide this"
---

# Frame the decision

Method DC-1.0. Primary tool `decision_run_stage`. Leave a missing field as `[GAP]`.

## How to do this work

Frame before solving. Ask the Playbook's framing questions one at a time, size the decision on consequence and reversibility, let the person pick the rigor, and store the Decide how to decide stage. Leave `[GAP]` rather than invent a goal, a deadline, or a decider.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Frame the decision | No decision statement, goal, or decider is stored yet. | `tasks/frame.md` |
| Size it and set rigor | The statement exists and the rigor is not confirmed. | `tasks/size.md` |

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

- The connector completes how_to_decide only with statement, goal, and rigor. Send decider, deadline, core_issue, consequence, reversibility, criteria, and authority_mode when the person gave them.
- Rigor is one of decide_quickly, tradeoff, dig_deep, full_process. Suggest it from the 2x2. The person confirms it.
- Ask one framing question per turn. Stop when the next answer must come from a person.
- A decision about hiring, promotion, performance, or termination of a named person gets the people-decision notice (references/rules.md R7) before anything else.
- Criteria are named here, before any option is rated.

Primary tool: `decision_run_stage`. Also named, and not copied: `decision_classify`, `decision_rigor_guide`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: widen-options.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/frame.md` | Frame the decision |
| `tasks/size.md` | Size it and set rigor |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
