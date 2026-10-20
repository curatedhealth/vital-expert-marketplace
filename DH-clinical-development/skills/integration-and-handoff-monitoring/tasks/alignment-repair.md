# B1 Alignment repair

Framework task: DH-01.01.3.2, Part B, task B1. Replaces the earlier "Alignment repair" section (DH-01.01.3.2.3).

## What this task delivers

For each handoff that has not arrived: the owner who owes the work product, the decision that stays blocked, the open items it waits on, and the date the person sets to look again, listed in dependency order. Where an owner, a decision or a date is missing, the gap is shown and the person is asked. The repair list never unblocks a decision because a meeting happened.

Why it matters: a slipped handoff with no named owner and no look-again date tends to stay slipped, and the decision behind it waits without anyone saying so.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.01.3.2 Part B, Alignment repair |
| Workflow | The steps below |
| Knowledge | A2's score; `references/handoff-rules.md` (anchors, so each blocked decision is tied to its gate); `references/measurement-rules.md` section 2; rows PL1, PL5, PL25, PL80, PL82, CV29 |
| Tools | `scripts/handoff_log.py repair` |
| Prompt | This guide |
| Template | `assets/alignment-repair-output.md` |
| Input | The request and its context; A2's score or the person's log; owners and dates the person names |
| Governance | `references/governance.md`; owners, dates and any decision to proceed are the person's |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person names who owes each work product and when to look again. The model lists, orders and routes. It never names an owner the person has not named, never sets a date, and never decides that a blocked decision may proceed without its work product.

## Workflow

### Step 1. Take the items that did not arrive

From A2 (open, and not measurable items the person confirms are still owed; an item with no named receiver is listed with "receiver not named `[GAP]`" and the person is asked who receives it), or run `python3 scripts/handoff_log.py repair LOG.csv --as-of YYYY-MM-DD`. Late items already received are not repairs; they stay in the score.

### Step 2. Owner who owes it

For each item, the owner the person named. If none, write "owner not named" and ask. Never suggest a job title.

### Step 3. Decision that stays blocked

State the blocked decision from the log, in the person's words. Where it is a sourced gate, add the anchor: a design review held at a major decision point (PL5) with the functions concerned (PL1); design validation that needs each other-function impact assessment documented (PL25); a DiGA application that needs all §§ 3 to 6 evidence at filing (PL80). Say plainly: the decision stays blocked until the work product is received by the named receiver; a meeting does not unblock it (old framework rule).

### Step 4. Dependency order

List items so that each comes after the open items it waits on (the script's order). Show circular waits and ask the person which goes first. Do not reorder by lateness or by who is senior.

### Step 5. Look-again date

The date the person sets for each item. If none, show `[GAP]` and ask. Where a sourced clock bears on the item (for example a DiGA trial extension request at least three months before the trial ends, PL82), state it as a fact with its instrument; it is not a reason to rush.

### Step 6. Route what is not a handoff problem

- No integration point or late path recorded: cross-functional product integration (DH-01.01.3.1) A1 or A2.
- A disagreement between functions, not a missing work product: cross-functional product integration B1 joint decision record.
- A recurring miss the person the user names for quality wants to investigate (or owner not named): `dh-regulatory-and-quality` audit-capa-and-complaints.
- A slip that may affect a submission or a regulatory clock: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- A slip in a critical-to-quality study handoff (CV29): `dh-clinical-development` trial-operations-monitoring.

## Build the output

Follow `assets/alignment-repair-output.md`. Short mode for a direct question: items not received, each with owner, blocked decision, waits-on and look-again date, in dependency order, and the gaps to fill. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every owner and date is the person's; missing ones are visible.
- Order is by dependency, stated as such.
- No decision is shown as unblocked without its work product received.
- No person or team is rated.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model does not chase, escalate or message anyone; it drafts the list for the person.
- Portfolio trade-offs between products competing for the same people: `dh-cross-functional-leadership` (old pack, heading DH-01.03.3 Governance & Portfolio).
- How a team or a lead is performing: `dh-cross-functional-leadership` (old pack, heading DH-01.03.4 Matrix Leadership). This skill rates no one.
