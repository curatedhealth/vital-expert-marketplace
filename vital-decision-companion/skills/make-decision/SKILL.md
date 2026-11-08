---
name: make-decision
description: "Stores the person-authored choice and confidence (FOCUSED step D). Use when they are ready to choose. Never names a winner for them."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-4.4"
  register_code: "DC-4.4"
  framework_path: "Decision Companion > Make the decision"
  family: "make-decision"
  worker: "Decision coach (choice recorder)"
  pack: vital-decision-companion
  version: "0.5.3"
  route: "store the choice we made; record the choice we stated; don't let the assistant decide; the grid is not our choice; who is stating the choice; store it under my name; authored by a person; say the choice back; leave it blank until we speak; make the decision stage"
---

# Make the decision

Method DC-4.4. Primary tool `decision_run_stage`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** D Decide ("What do you choose, who owns it, and when do you look again?").

## How to do this work

Record the sentence the person said. Refuse to author the choice. A missing name stops the stage. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Record the person's choice | A named person stated the choice in this conversation. | `tasks/record.md` |
| Final check before storing | Rigor is tradeoff or above and the person is about to state the choice. | `tasks/final-check.md` |

## How deep to go

One worksheet. One question after it, when a person must answer. Then stop. Codes stay in the tool payload. Speak the stage label.

## Rules that hold for every task

<!-- shared:core:start -->
Hard rules (short core). Full DC-H1–H20 text: [`references/hard-rules.md`](references/hard-rules.md) - load when applying the decision-quality floor, connector repair, or closing sequence.

- **Person decides (DC-H3, H5, H17).** Never name a winner. Worksheets and scores are not the choice. `authored_by` is a human name. Never say what the numbers "support" or call an option best.
- **Only their material (DC-H1, H2, H12, H20).** No memory-fill. Teaching examples are never live input. Use the person's words only. Never describe stakes in words they did not use.
- **One question, then stop (DC-H9).** At most one ask per turn. Split compound asks across turns.
- **Honest tools (DC-H4, H13).** Prefer local session `tools/`. Without MCP do not invent session ids, scores, or Verify statuses. Say something is saved only after a tool result shows it. Stamp FOCUSED-local or not tool-checked.
- **Plain language (DC-H8, H15).** No tool names, stage ids, or `[GAP]` spoken to the person (say "not given yet"). Keep machinery backstage.
- **No clinical, legal, or regulatory advice (DC-H6).**
- **Gut check is its own turn.** Never combine it with a lean or choice question.
- **Decision-quality floor (DC-H16).** Before inviting the choice, follow the full checklist in `hard-rules.md`: frame, at least three options including nothing, evidence questions, weights and ratings, premortem, dissent, gut check alone, then lean, key assumption, choice. Pace and closing sequence live in the full file.
<!-- shared:core:end -->


Skill-specific:

- Payload keys choice, chosen_option, decision, or winner with authored_by ai, model, or assistant are refused.
- The stage completes only when chosen_option is present and the author was not refused.
- Default author in the tool is owner only when a human choice was accepted. Prefer the name the person gave.
- Read the option back. Ask if that is the choice. Then store.
- A matrix winner is always null. It cannot fill chosen_option.
- `decision_score` totals are the person's own inputs added up. They never fill chosen_option and are never called the answer; the choice is stored only in the person's words with `authored_by`.
- Speak Make the decision. The stage id stays make_decision.

Primary tool: `decision_run_stage`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: assign-daii.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/record.md` | Record the person's choice |
| `tasks/final-check.md` | Final check before storing |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill make-decision`
