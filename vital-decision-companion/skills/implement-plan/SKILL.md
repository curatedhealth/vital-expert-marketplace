---
name: implement-plan
description: "This skill should be used when the user asks to \"Turn our decision into an implementation plan.\", \"Who owns this and what happens in the next 48 hours?\", \"When do we review it and what would make us revisit?\". Do not use it to choose the option, assign DAI-I roles alone, or score progress."
license: "UNLICENSED. Proprietary to Vital.Expert; terms set by the owner."
compatibility: >
  Runs on any assistant that loads Agent Skills. The Decision Companion connector
  adds decision_run_stage when a vdec_ key is present. Without it the same method runs
  by hand and the turn is labeled not tool-checked.
metadata:
  framework_code: "DC-5.2"
  register_code: "DC-5.2"
  framework_path: "Decision Companion > Implementation plan"
  family: "implement"
  worker: "Decision coach (implementation)"
  pack: vital-decision-companion
  version: 0.3.2
  route:
    - "implementation plan"
    - "next 48 hours"
    - "who owns the rollout"
    - "review trigger"
    - "progress review date"
    - "communication plan"
    - "if then plan"
    - "turn the premortem into actions"
    - "what would make us revisit"
    - "first milestone"
---

# Implementation plan

Method DC-5.2. Primary tool `decision_run_stage`. Leave a missing field as `[GAP]`.

## How to do this work

Turn the recorded choice into accountable action. Ask for one owner, the first milestone, the review date, and the review trigger; turn each pre-mortem failure into an if–then plan; store the Implement stage. Leave `[GAP]` rather than invent an owner, a date, or a metric.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Build the plan | A choice is recorded and the Implement stage is open. | `tasks/plan.md` |
| Turn risks into if–then plans | A pre-mortem list exists or the person names risks. | `tasks/if-then.md` |

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

- The connector completes implement only when roles.decide (or the session DAI-I decide) is a name. Run daii first if it is empty.
- Send owner, first_milestone, review_date, review_trigger, communication_plan, key_actions, and if_then_plans when the person gave them.
- One owner. Several contributors are fine; one person is accountable.
- An if–then plan names a situation, an action, and an owner: if this happens, then this person does this.
- This skill does not decide whether the choice was right. The learning loop reviews that.

Primary tool: `decision_run_stage`. Also named, and not copied: `decision_daii_plan`, `decision_premortem`.

## What to return

The sections in `assets/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: learning-loop.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/plan.md` | Build the plan |
| `tasks/if-then.md` | Turn risks into if–then plans |
| `references/tools.md` | Arguments and return fields |
| `references/rules.md` | Skill rules |
| `references/patterns.md` | Shapes, not facts |
| `references/gap-rules.md` | How a miss is worded |
| `references/governance.md` | Stop rules and the closing line |
| `assets/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |
| `evals/evals.json` | Spoken requests and the refuse case |
