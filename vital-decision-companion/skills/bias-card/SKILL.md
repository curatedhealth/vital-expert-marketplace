---
name: bias-card
description: "Reads a bias card and asks the person to apply the countermeasure (FOCUSED step E). Use when they name anchoring, confirmation, sunk cost, or groupthink, or ask which bias is in the room. Do not declare the room unbiased or pick for them."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-4.3"
  register_code: "DC-4.3"
  framework_path: "Decision Companion > Bias"
  family: "make-decision"
  worker: "Decision coach (bias card)"
  pack: vital-decision-companion
  version: "0.5.3"
  route: "which bias is in the room; confirmation bias card; anchoring on the first number; sunk cost card; groupthink countermeasure; don't say we are unbiased; name the bias we see; bias card only; countermeasure we can do now; refuse a clean bill"
---

# Bias

Method DC-4.3. Primary tool `decision_bias_check`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** E Examine ("How does this sit with your gut, what could go wrong, and who disagrees?").

## How to do this work

Read the countermeasure and ask the person to do it. Refuse to declare the room unbiased. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Read the bias card | The person names a bias or asks which bias is in the room. | `tasks/read.md` |
| By-hand bias prompts by stage | The tool card has no item for this stage or type. | `tasks/by-stage.md` |

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

- Pass decision_type or session_id. With a session and no type, the tool uses the stored type.
- Matched items are those whose types include the decision type. With no type, the full card returns.
- The four items in pack 2026-10-24.1 are confirmation, anchoring, sunk_cost, and groupthink.
- draft is true. Do not say the decision is unbiased.
- Read the countermeasure. Ask the person to do that step. Do not do it for them.
- This skill does not set chosen_option.

Primary tool: `decision_bias_check`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: make-decision after the person has answered the countermeasure they choose to answer.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/read.md` | Read the bias card |
| `tasks/by-stage.md` | By-hand bias prompts by stage |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill bias-card`
