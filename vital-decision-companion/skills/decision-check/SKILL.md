---
name: decision-check
description: "This skill should be used when the user asks to \"Are we ready to decide?\", \"Run the decision quality checklist before the brief.\", \"What is still missing before we commit?\". Do not use it to choose the option, to score options, or to sign the brief."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_status when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-6.0"
  register_code: "DC-6.0"
  framework_path: "Decision Companion > Decision check"
  family: "brief"
  worker: "Decision coach (readiness check)"
  pack: vital-decision-companion
  version: 0.3.3
  route:
    - "are we ready to decide"
    - "decision quality checklist"
    - "what is still missing"
    - "readiness check"
    - "before we commit"
    - "check the six elements"
    - "weakest link"
    - "quality check before the brief"
    - "did we consider enough options"
    - "is this decision ready"
---

# Decision check

Method DC-6.0. Primary tool `decision_status`. Leave a missing field as `[GAP]`.

## How to do this work

Check readiness against the Playbook's decision quality checklist before the brief or the choice. Mark each item met, not met, or not known, from stored fields and the person's answers only. Show the weakest of the six quality elements. Never compute a single quality score and never say the decision is good.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Run the checklist | Before the choice is recorded or the brief is compiled. | `tasks/check.md` |

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

- Read the session with decision_status. Mark an item met only when a stored field or the person's answer shows it.
- The Playbook checklist has five sections: framing, information, options, reasoning, action.
- Report counts per section and the items not met. The Playbook's ready thresholds are guidance, labelled as such; there is no validated single score.
- Name the weakest of the six decision quality elements: frame, alternatives, information, values and trade-offs, reasoning, commitment to action.
- This skill does not decide whether to proceed. The named person does.

Primary tool: `decision_status`. Also named, and not copied: `decision_build_brief`, `decision_rigor_guide`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: the skill for the weakest item, or brief.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/check.md` | Run the checklist |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
