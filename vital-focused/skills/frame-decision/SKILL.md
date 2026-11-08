---
name: frame-decision
description: "Frames what is being decided, who decides, and by when (FOCUSED step F). Use when they ask to frame the decision, set rigor depth, or name decider and deadline. Do not use to list options, score a matrix, or record the choice."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-1.0"
  register_code: "DC-1.0"
  framework_path: "Decision Companion > Frame the decision"
  family: "how-to-decide"
  worker: "Decision coach (framing)"
  pack: vital-focused
  version: "0.5.4"
  route: "frame this decision; how much rigor; who decides and by when; what is the goal; core of the issue; consequence and reversibility; decide how to decide; is now the right time; what criteria will we use; how should we decide this"
---

# Frame the decision

Method DC-1.0. Primary tool `decision_run_stage`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** F Frame ("What exactly are we deciding, who decides, and by when?").

## How to do this work

Frame before solving. Ask the Playbook's framing questions one at a time, size the decision on consequence and reversibility, let the person pick the rigor, and store the Decide how to decide stage. Leave the field out ("not given yet") rather than invent a goal, a deadline, or a decider.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Frame the decision | No decision statement, goal, or decider is stored yet. | `tasks/frame.md` |
| Size it and set rigor | The statement exists and the rigor is not confirmed. | `tasks/size.md` |

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

- The connector completes how_to_decide only with statement, goal, and rigor. Send decider, deadline, core_issue, consequence, reversibility, criteria, and authority_mode when the person gave them.
- Rigor is one of decide_quickly, tradeoff, dig_deep, full_process (ids stay backstage). Propose it from the 2x2 in plain words; the person's preference wins.
- Ask one framing question per turn. Stop when the next answer must come from a person.
- A decision about hiring, promotion, performance, or termination of a named person: send `people_decision: true`, say only that it is flagged and the connector notice will follow, then read the connector warning (or R7 if silent); never invent HR/legal/AI Act wording ahead of the tool.
- Criteria are named here, before any option is rated.

Primary tool: `decision_run_stage`. Also named, and not copied: `decision_classify`, `decision_rigor_guide`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: widen-options.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/frame.md` | Frame the decision |
| `tasks/size.md` | Size it and set rigor |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill frame-decision`
