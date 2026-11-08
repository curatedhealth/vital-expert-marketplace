---
name: handoff-verify
description: "Builds a Verify handoff packet for claim checks the person requested (FOCUSED step U). Use when they want source/claim checks. Do not invent Verify statuses without a key."
license: "LicenseRef-CrossroadsCatalyst-Proprietary. Product of Crossroads Catalyst GmbH (Vital Expert)."
compatibility: >
  Runs on any assistant that loads Agent Skills. Default is local FOCUSED
  session tools (no MCP). Optional vdec_/vont_/vvfy_ only for special services.
metadata:
  framework_code: "DC-9.2"
  register_code: "DC-9.2"
  framework_path: "Decision Companion > Handoff to Verify"
  family: "handoff"
  worker: "Decision coach (verify handoff)"
  pack: vital-focused
  version: "0.5.4"
  route: "check this claim; is this supported; don't mark it supported; verify packet; passage is missing; claim check belongs to verify; hand the sentence across; no support status here; quote the passage or stop; verify decides support"
---

# Handoff to Verify

Method DC-9.2. Primary tool `decision_handoff_verify`. Leave a missing field out of the payload (never store `[GAP]` as a value); say "not given yet" to the person.

**FOCUSED step:** U Unknowns ("What do we know, and what is still unknown?").

## How to do this work

List the claims and the next tools. Refuse to decide support. Verify's skills do that work. Leave the field out ("not given yet") rather than invent a session field, a score, or a claim status.

## Pick the task

| Task | Use it when | Guide |
|---|---|---|
| Build the packet | The person wants a claim checked. | `tasks/packet.md` |
| Call Verify | The packet is ready and `vvfy_` is connected. | `tasks/call.md` |

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

- Call decision_handoff_verify with session_id and the claims the person listed. called_verify is false.
- next_tools are qualify_source and check_claim. Call them on vital-verify, in that order.
- check_claim needs the admitted source object and a quoted passage. A passage the coach wrote does not count.
- Without a vvfy_ key, say Verify is not connected. Do not invent a status.
- Do not restate source grading, claim decomposition, currency, honesty, or the Verify record. Those skills live in vital-verify.
- An unverifiable sentence stays out of the brief. It is not replaced with a guess.

Primary tool: `decision_handoff_verify`. Also named, and not copied: `qualify_source`, `check_claim`.


## What to return

The sections in `templates/worksheet-output.md`. The closing line follows `references/governance.md`.

Next skill: decision-brief, with unsupported sentences left out.

Leave every other stage, score, and claim check to its own skill. The plugin README names them. Do not paste that map into this file.

## Files

| File | Role |
|---|---|
| `tasks/packet.md` | Build the packet |
| `tasks/call.md` | Call Verify |
| `references/tools.md` | Arguments and return fields |
| `references/governance.md` | Stop rules and the closing line |
| `templates/worksheet-output.md` | Sections to return |
| `examples/worked.md` | Teaching shape |

## Output cards (required)

Use shared templates under plugin `templates/`:

- `frame-card.md`, `options-card.md`, `criteria-card.md`, `score-grid.md`, `unknowns-card.md`, `examine-card.md`, `decision-record.md`, `brief-card.md`, `gap-list.md`, `check-line-stamp.md`

Offline path: [`references/without-connector.md`](references/without-connector.md).  
Method: [`references/method.md`](references/method.md).

Stamp: `python tools/stamp_focused_line.py --mode local --skill handoff-verify`
