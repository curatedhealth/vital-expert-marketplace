---
name: brief
description: "This skill should be used when the user asks to \"Compile what we stored into a draft brief.\", \"Don't sign the brief or add a signature block.\", \"The brief is still a draft until a person owns it.\". Do not use it to sign the brief, clear the decision, or fill a gap with prose."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_build_brief when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-7.1"
  register_code: "DC-7.1"
  framework_path: "Decision Companion > Brief"
  family: "record"
  worker: "Decision coach (drafter)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "compile what we stored"
    - "don't sign the brief"
    - "brief is still a draft"
    - "no prose we did not store"
    - "gaps stay visible"
    - "compile and stop"
    - "worksheet into a brief"
    - "unsigned decision record"
    - "leave the choice line blank"
    - "draft brief only"
---

# Brief

Method DC-7.1. Primary tool `decision_build_brief`. Leave a missing field as `[GAP]`.

## How to do this work

Compile what was stored. Refuse to sign. A brief with no human choice is still a draft. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Compile the draft | The person wants the stored session in one brief. | `tasks/compile.md` |

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

- Call decision_build_brief with session_id.
- A complete stage is rendered from its stored payload. An incomplete stage is the line [GAP].
- Do not rewrite a [GAP] into a plausible paragraph.
- watermark SIMULATED means practice. Say so at the top.
- The brief is a draft. It is not a signature and it is not clearance.
- Compile when the person asks, or when every stage required by the confirmed rigor is complete or explicitly skipped.

Primary tool: `decision_build_brief`. Also named, and not copied: none.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: The open stage, if the person wants to continue. Otherwise stop.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/compile.md` | Compile the draft |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
