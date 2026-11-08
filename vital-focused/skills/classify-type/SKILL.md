---
name: classify-type
description: "Drafts and confirms a decision type from the person's words (FOCUSED step F). Use when they ask what kind of decision this is or to confirm the type. Do not use to choose an option or clear bias."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-1.1"
  register_code: "DC-1.1"
  framework_path: "Decision Companion > Classify"
  family: "how-to-decide"
  worker: "Decision coach (type draft)"
  pack: vital-focused
  version: "0.5.4"
  route: "what kind of decision; is this a quick call; draft the decision type; don't lock the type yet; budget reallocation type; no type in the pack; confirm the draft type; keyword type only; what type of choice is this; wait for my yes on the type"
---

# Classify

Method DC-1.1. Primary tool `decision_classify`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** F Frame ("What exactly are we deciding, who decides, and by when?").

## How to do this work

Draft a type from keywords and read it back in one sentence. Refuse to treat the draft as the person's confirmed type. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Draft the type | The person described a decision and has not confirmed a type. | `tasks/draft.md` |
| Store the confirmed type | The person said yes and gave their name. | `tasks/confirm.md` |

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

- decision_classify is a keyword draft. rationale says so. draft is true.
- Read decision_type and recommended_rigor back in one sentence. Ask the person to confirm.
- Store rigor on how_to_decide with decision_run_stage only after the person confirms.
- A statement with no keyword returns decision_type null and a gap. Say the pack has no row.
- Types in this pack: response_customer, tradeoff_resource, sequence_strategic, go_nogo_people, prioritization_operational, pivot_strategic, escalation_risk, standard_setting.
- how_to_decide is complete only when statement, goal, and rigor are all present.

Primary tool: `decision_classify`. Also named, and not copied: `decision_run_stage`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: rigor-checklist after confirmation, to read the checklist for that level.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/draft.md` | Draft the type |
| `tasks/confirm.md` | Store the confirmed type |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill classify-type`
