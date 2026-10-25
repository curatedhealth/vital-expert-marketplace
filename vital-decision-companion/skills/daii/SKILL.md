---
name: daii
description: "This skill should be used when the user asks to \"Who decides in the words of the room?\", \"Who advises, and who only inputs?\", \"Who must be informed after the choice?\". Do not use it to assign a role to a model, to leave Decide empty, or to invent a job title."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_daii_plan when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-5.1"
  register_code: "DC-5.1"
  framework_path: "Decision Companion > DAI-I"
  family: "implement"
  worker: "Decision coach (roles)"
  pack: vital-decision-companion
  version: 0.3.3
  route:
    - "who decides in the words of the room"
    - "who advises"
    - "who must be informed"
    - "four roles"
    - "don't put a model in decide"
    - "empty role stays empty"
    - "assign the names we gave"
    - "dai-i card"
    - "informed is not the decider"
    - "refuse an ai decider"
---

# DAI-I

Method DC-5.1. Primary tool `decision_daii_plan`. Leave a missing field as `[GAP]`.

## How to do this work

Write the names the person said into the four roles. Refuse to put a model in Decide. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Assign the four roles | The person named who decides, advises, inputs, or must be informed. | `tasks/assign.md` |

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

- roles.decide must be a display name the person gave. An empty decide returns the gap decide role empty.
- When reading advise/inform/implement, accept a string or `{name, status}`; print unverified_person entries as "<name> (unverified, role not person)".
- Do not assign ai, model, or assistant to any role.
- Do not invent a job title. If they gave a name, use the name. If they gave none, write owner not named and ask.
- Advise, Inform, and Implement may be empty. Say they are empty.
- Call decision_run_stage on implement with the same roles after the person confirms.
- The implement stage completes when roles.decide is non-empty.

Primary tool: `decision_daii_plan`. Also named, and not copied: `decision_run_stage`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: learning-loop when the rigor requires it; otherwise brief.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/assign.md` | Assign the four roles |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
