---
name: widen-options
description: "Widens the option set, including doing nothing (FOCUSED step O). Use when they ask what else they could do or to store options. Do not score or choose."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-2.1"
  register_code: "DC-2.1"
  framework_path: "Decision Companion > Widen options"
  family: "widen-options"
  worker: "Decision coach (option list)"
  pack: vital-focused
  version: "0.5.4"
  route: "we only have two options; add do nothing; doing it internally; don't invent a third option; widen the list we named; the favorite is not the list; fewer than three choices; store only what we said; an option is missing; missing option yourself"
---

# Widen options

Method DC-2.1. Primary tool `decision_widen_options`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** O Options ("What else could we do, including nothing?").

## How to do this work

Keep the list wide. Refuse to invent a third option to silence a warning. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Store the named options | The person named the options in their own words. | `tasks/store.md` |
| Ask about a missing option | The tool returned a warning that the list is narrow. | `tasks/warning.md` |

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

- Pass options as a list of objects with name. Empty names are refused.
- Warnings, not errors: fewer than 3 options; do-nothing missing; do-it-internally missing.
- If a warning is present, ask the person for that option. Do not insert one.
- The stage is complete when the stored list has at least three options.
- Ids may be omitted. The tool assigns opt-1 and onward.
- This skill does not rate and does not rank.

Primary tool: `decision_widen_options`. Also named, and not copied: `decision_run_stage`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: gather-intelligence when the rigor requires it; otherwise tradeoff-score or make-decision.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/store.md` | Store the named options |
| `tasks/warning.md` | Ask about a missing option |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill widen-options`
