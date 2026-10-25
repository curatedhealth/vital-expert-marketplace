---
name: classify
description: "This skill should be used when the user asks to \"What kind of decision is a mid-year budget reallocation?\", \"Is this a quick call or a long process? Draft it and wait.\", \"Draft the decision type from what I just said.\". Do not use it to read the rigor checklist, widen options, or store a choice."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_classify when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-1.1"
  register_code: "DC-1.1"
  framework_path: "Decision Companion > Classify"
  family: "how-to-decide"
  worker: "Decision coach (type draft)"
  pack: vital-decision-companion
  version: 0.3.3
  route:
    - "what kind of decision"
    - "is this a quick call"
    - "draft the decision type"
    - "don't lock the type yet"
    - "budget reallocation type"
    - "no type in the pack"
    - "confirm the draft type"
    - "keyword type only"
    - "what type of choice is this"
    - "wait for my yes on the type"
---

# Classify

Method DC-1.1. Primary tool `decision_classify`. Leave a missing field as `[GAP]`.

## How to do this work

Draft a type from keywords and read it back in one sentence. Refuse to treat the draft as the person's confirmed type. Leave `[GAP]` rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Draft the type | The person described a decision and has not confirmed a type. | `tasks/draft.md` |
| Store the confirmed type | The person said yes and gave their name. | `tasks/confirm.md` |

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

- decision_classify is a keyword draft. rationale says so. draft is true.
- Read decision_type and recommended_rigor back in one sentence. Ask the person to confirm.
- Store rigor on how_to_decide with decision_run_stage only after the person confirms.
- A statement with no keyword returns decision_type null and a gap. Say the pack has no row.
- Types in this pack: response_customer, tradeoff_resource, sequence_strategic, go_nogo_people, prioritization_operational, pivot_strategic, escalation_risk, standard_setting.
- how_to_decide is complete only when statement, goal, and rigor are all present.

Primary tool: `decision_classify`. Also named, and not copied: `decision_run_stage`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: rigor after confirmation, to read the checklist for that level.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/draft.md` | Draft the type |
| `tasks/confirm.md` | Store the confirmed type |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
