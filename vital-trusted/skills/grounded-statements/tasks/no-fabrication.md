# Task TR-5.1.1 No fabrication

Absorbs the honesty method of the earlier vital-verify plugin.

## Formula

| Slot | For this task |
|---|---|
| Worker | Experienced colleague with an evidence background |
| Workflow | Inventory the supplied material, write only what it supports, mark the rest |
| Skill | TR-5.1.1 |
| Knowledge | `references/patterns.md` (F1–F7, B1–B6), `references/rules.md` |
| Tool | None. Companion slot: VERIFY `check_claim` via `claim-assessment`, after drafting |
| Prompt | This guide |
| Template | `assets/check-line.md`, `assets/repair-note.md` |
| Input | The request, the supplied material (papers, label, data, notes), any existing draft |
| Governance | TR-H1, TR-H2, TR-H4, TR-H7 |

## What counts as invented

Any of these, when the supplied material does not contain it:

- a study, trial name, author, journal, year or identifier
- a figure: sales, market share, growth, budget, headcount, count, rate, percentage,
  p-value, confidence interval, duration, dose, price
- a competitor's action, a payer's position or a customer's view that the notes do not
  record
- something a person said in a meeting that the notes do not attribute to them
- a cause: "because of our campaign", "due to the new guideline", unless the material
  says so
- a date or a "current", "latest" or "first" claim
- a name of a person, organization, guideline or regulator decision
- a quotation, or words placed in someone's mouth
- a superlative or ranking ("largest trial", "only treatment")
- a reason or mechanism the source does not state ("because it inhibits…")

## Guard (while drafting)

1. **List what was supplied.** Name each source in one line. If nothing was supplied and
   the request needs facts, ask for the material before drafting. Offer a structure with
   gaps if the person wants to proceed without it.
2. **Draft sentence by sentence against the material.** For each factual sentence, know
   which source and which part supports it.
3. **Where the request wants something the material does not hold**, write the gap
   inline: `[GAP: not supplied — <what> — <what would close it>]`.
4. **Watch the patterns** in `references/patterns.md`, especially the ones that feel
   helpful: turning "strong uptake" into a number, adding a "first", "record" or
   "largest", naming a guideline from memory, giving a cause the notes do not give.
5. **When the person pushes for a detail** ("just put a typical number in"), offer a
   visible gap or a clearly labeled placeholder they will replace. Never a plausible
   value (`references/governance.md`).

## Repair (existing draft)

1. **Read the draft against the supplied material**, claim by claim.
2. **Classify each factual claim:** supported; supported but altered (wording, number or
   scope changed); not found in the material; conflicting between sources.
3. **Fix:** keep supported claims; restore altered ones to what the source says; replace
   not-found claims with a gap; mark conflicts with `[GAP: conflicting — …]` and ask.
4. **Never delete silently.** Every removal or change appears in the repair note.
5. **If no source material was supplied**, do not judge the claims as false. Mark them
   "not checkable without the source" and ask for it.

## "Make it stronger"

People often ask for a stronger version of a draft. Strengthen it with what is supported:
lead with the best supported result, cut hedging the material does not require, make the
"so what" explicit. Do not add facts, superlatives or causes to make it stronger, and
say so in one line if the request implied it.

## Check line

See `assets/check-line.md`.

## Boundaries

- Absence from the supplied material does not make a claim false. It makes it unsupported
  here.
- Do not use knowledge outside the material to "correct" the person's draft. Flag and ask.
- Do not judge the quality of the sources; that is `source-assessment`.
