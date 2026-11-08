---
name: rigor-checklist
description: "Reads the checklist for the confirmed depth of work (FOCUSED step F). Use when they ask how thorough to be or what the depth checklist requires. Do not offer a menu of rigor names or pick for them."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-1.2"
  register_code: "DC-1.2"
  framework_path: "Decision Companion > Rigor"
  family: "how-to-decide"
  worker: "Decision coach (process depth)"
  pack: vital-decision-companion
  version: "0.5.3"
  route: "how rigorous should this be; can we skip a stage; what does dig deep require; full process checklist; decide quickly checklist; trade-off checklist; don't drop a required stage; which stages are skippable; pre-mortem required or not; read the level we confirmed"
---

# Rigor

Method DC-1.2. Primary tool `decision_rigor_guide`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** F Frame ("What exactly are we deciding, who decides, and by when?").

## How to do this work

Read the level the person confirmed. Refuse to drop a required stage because the room is in a hurry. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Read the checklist | The person wants the stages for the confirmed level. | `tasks/read.md` |
| Record an allowed skip | The person wants to skip a stage the guide marks skippable. | `tasks/skip.md` |

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

- Levels are decide_quickly, tradeoff, dig_deep, and full_process. Any other value is an unknown rigor error.
- Read required, skippable, and checklist from the tool. Do not invent a fifth level.
- A skippable stage is skipped only when the person says so. Say the stage was skipped.
- decide_quickly still requires how_to_decide, widen_options, and make_decision.
- dig_deep requires gather_intelligence. full_process has an empty skippable list.
- The guide does not choose the option.

Primary tool: `decision_rigor_guide`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: widen-options, unless that stage is already complete.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/read.md` | Read the checklist |
| `tasks/skip.md` | Record an allowed skip |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill rigor-checklist`
