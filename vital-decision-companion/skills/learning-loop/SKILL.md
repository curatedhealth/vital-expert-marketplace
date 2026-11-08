---
name: learning-loop
description: "Sets review date and success signal, then supports a later retro (FOCUSED step D). Use when they ask when to look again. Do not invent a success metric."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-6.1"
  register_code: "DC-6.1"
  framework_path: "Decision Companion > Learning loop"
  family: "learning-loop"
  worker: "Decision coach (review)"
  pack: vital-decision-companion
  version: "0.5.3"
  route: "when do we review; what signal would change it; don't invent a kpi; store the review date; learning loop only; signal stays a gap; revisit in ninety days; who owns the review; don't backfill a metric; capture the after-action"
---

# Learning loop

Method DC-6.1. Primary tool `decision_run_stage`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** D Decide ("What do you choose, who owns it, and when do you look again?").

## How to do this work

Capture the review the person named. Refuse to invent a KPI. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Store the review | The person named a review date or a signal. | `tasks/review.md` |
| Run the retrospective | The review date has come and the outcome is known. | `tasks/retro.md` |

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

- The stage completes only when review_date and success_signal are both present.
- If either is missing, store nothing for that field and say "not given yet".
- Dates are spoken in full, such as 24 October 2026.
- full_process requires this stage. Other levels may skip it only when the person says so.
- The signal is their words. Do not translate it into a target they did not set.
- This stage does not change chosen_option.

Primary tool: `decision_run_stage`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: decision-brief.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/review.md` | Store the review |
| `tasks/retro.md` | Run the retrospective |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill learning-loop`
