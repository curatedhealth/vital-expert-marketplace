---
name: decision-brief
description: "Compiles the decision brief with [GAP] for missing fields (FOCUSED step D). Use when they ask for the brief or record. Do not fill gaps from memory."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-7.1"
  register_code: "DC-7.1"
  framework_path: "Decision Companion > Brief"
  family: "record"
  worker: "Decision coach (drafter)"
  pack: vital-focused
  version: "0.5.4"
  route: "compile what we stored; don't sign the brief; brief is still a draft; no prose we did not store; gaps stay visible; compile and stop; worksheet into a brief; unsigned decision record; leave the choice line blank; draft brief only"
---

# Brief

Method DC-7.1. Primary tool `decision_build_brief`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** D Decide ("What do you choose, who owns it, and when do you look again?").

## How to do this work

Compile what was stored. If the brief has a block of added-up totals, read it as the person's own weights and ratings added up, never as a recommendation. Refuse to sign. A brief with no human choice is still a draft. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Compile the draft | The person wants the stored session in one brief. | `tasks/compile.md` |

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

- Call decision_build_brief with session_id.
- A complete stage is rendered from its stored payload. An incomplete stage is the line [GAP].
- Do not rewrite a [GAP] into a plausible paragraph.
- watermark SIMULATED means practice. Say so at the top.
- The brief is a draft. It is not a signature and it is not clearance.
- Compile when the person asks, or when every stage required by the confirmed rigor is complete or explicitly skipped.

Primary tool: `decision_build_brief`. Also named, and not copied: none.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: The open stage, if the person wants to continue. Otherwise stop.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/compile.md` | Compile the draft |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill decision-brief`
