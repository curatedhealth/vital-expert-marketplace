# B1 Thesis review

Framework task: DH-DIL.4.2, Part B, task B1. New in this version; the old suite had no review task.

## What this task delivers

For each watched assumption: the value at the memo, the value now with its source and date, whether the person's own trigger rule is met, held, not measurable or not comparable, the owner the person names, what follows by the person's rule (for example "reopen the decision record", "ask the company"), and the date it is read again. Decisions to reopen, follow on, sell, hold or write down are listed as the person's, never answered. It answers "by our own triggers, does the thesis still hold, and who follows up on what?"

Why it matters: a thesis review that turns a quiet change log into "all good", or a new filing into "they are in trouble", says more than the record does. A review against the person's written triggers, with flags for what cannot be compared, leaves a trace the committee can follow later.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (diligence suite); work as a diligence analyst who checks against the person's rules |
| Skill | DH-DIL.4.2 Part B, Thesis review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/monitoring-signals.md`; `references/governance.md` |
| Tools | None beyond A2. `scripts/thesis_check.py` |
| Prompt | This guide |
| Template | `assets/thesis-review-output.md` |
| Input | The request and its context: the assumption register (A1 or the person's CSV), A2 output or saved library files, the person's triggers, owners, reread dates and follow-up rules, the read date |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the triggers and decides what a tripped trigger leads to. The model reads the data against those triggers and writes down the result. It never decides that the thesis is broken or intact overall, never advises a transaction or a write-down, and never names an owner the person has not named. Where a trigger's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the triggers

Write each assumption and its trigger back, numbered, verbatim, with the machine rule if the person gave one. Missing triggers: "trigger not given `[GAP]`"; report the value but mark nothing met or held.

### Step 2. Read each assumption

With code execution, run `python3 scripts/thesis_check.py --register REGISTER.csv --as-of DATE ...` on the saved A2 outputs; take values, rule results and flags from its output. For each assumption: value at memo, value now, source and date, rule met or not met, and flags: T1 owner not named, T2 reread date not given, T3 not measurable from the record, T4 evidence maturity not comparable, T5 change log began after the memo date, T6 reread date earlier than the read date. A "not met" with T5 is a statement about the log, not about the company; say so.

Check that each signal measures what the assumption says. `deltas.change_count` counts authorization, study, safety event and filing changes together (monitoring-signals.md section 2); for an assumption about recalls or safety events, say the signal is broader than the assumption, read the change types, and offer the narrower signal labeled proposed. An assumption that the company is operating rests on the company status line (monitoring-signals.md section 6); while status is "[GAP]: not read", the assumption is not measurable from what was read.

### Step 3. What the person's rule says follows

For each met trigger, write what the person's follow-up rule says (in their words), with the owner they named. If they gave no follow-up rule, write "follow-up not given; your call". Possible follow-ups the person may name: reopen the decision record (`investment-memo-and-decision-record`, this pack), ask the company for a document, read a filing at its URL, ask the owner the person names for legal or compliance about a rule change. Never add a transaction, a value or a write-down.

### Step 4. Owners and reread dates

List owners as named (or owner not named) and reread dates as set (or "not given"; ask). T6 is stated as a fact ("reread date 1 October 2026 is earlier than the read date 20 October 2026"), never as urgency.

### Step 5. What the person must decide

List the decisions the review surfaces (whether to reopen, whether a T4 or T5 item needs a different check, whether a T3 assumption gets the person's own data), each with the facts behind it. Propose nothing unless asked; label any proposal "proposed".

## Build the output

Follow `assets/thesis-review-output.md`. Answer first: counts of assumptions whose trigger rule is met, not met, and not measurable or not comparable, the met triggers by name, and the flag that most limits the read. Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Triggers, follow-ups, owners and reread dates are the person's, and the record says so.
- No overall verdict on the thesis; no sell, hold, buy or write-down; no valuation.
- Every "not met" under T5 carries the log caveat.
- The review is labeled "thesis review draft for the owner".
- The company status line is present (from the script or the filings read).
- `python3 scripts/thesis_check.py --words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Reopening or rewriting the decision record: `investment-memo-and-decision-record` (this pack).
- Rule conclusions: the owner the person names for legal or compliance, or owner not named.
- Any wording for LPs, a board or the company: stops for the owner the person names.
