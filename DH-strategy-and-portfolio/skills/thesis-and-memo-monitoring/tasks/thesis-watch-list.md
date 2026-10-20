# A1 Thesis watch list

Framework task: DH-DIL.4.2, Part A, task A1. New in this version; it turns the old "Watch companies" tool skill into a watch list the person keeps, with no watch tool called.

## What this task delivers

For each thesis assumption and each load-bearing memo fact, in the person's words: the public signal that can carry it (if any), the source and library call that reads it, what that signal cannot show, the value at the memo date as the memo recorded it, the person's trigger, owner and reread date. Assumptions no public signal can carry are named as "not measurable from the record". The result is an assumption register the person can rerun (`scripts/thesis_check.py`). It answers "what exactly do we re-check, and against what?"

Why it matters: a thesis like "the product holds FDA clearance" or "the company is funded" sounds checkable, but the record stores authorizations with decision dates and no marketing status, and a Form D shows no valuation or investors (DL-016, DL-018). Writing the signal and its limit beside each assumption keeps the later review honest.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (diligence suite); work as a diligence analyst who re-reads and checks |
| Skill | DH-DIL.4.2 Part A, Thesis watch list |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 1 to 3; rows DL-002, DL-005, DL-006, DL-016, DL-018 to DL-024, DL-034 to DL-043, DL-089, DL-092, DL-095 to DL-097, DL-116, DL-118 (DOI 10.2196/37677), DL-126 to DL-133, CP-US-49, CP-US-56 |
| Tools | None by default. `scripts/thesis_check.py` to test the register once written |
| Prompt | This guide |
| Template | `assets/watch-list-output.md` |
| Input | The request and its context: the memo or decision record and its date, the thesis assumptions, the companies (exact references), the person's triggers, owners and reread dates |
| Governance | `references/governance.md`; the person sets every trigger, owner and reread date |
| Catalogue job | none (the old menu placed Watch companies under `market-screen`; no job is started) |

## Read the request

- **Memo date.** The date of the memo or decision record. If not given, ask; never pick one.
- **Assumptions.** The person's words, numbered. If the person brings only a memo, list the thesis claims and memo facts it states and ask which to watch; propose none as chosen.
- **Triggers.** In the person's words. A machine form (">N", "changes", "after:DATE") is written only when the person's words fix it; otherwise "trigger rule not given" and ask.
- **Companies.** Exact references as the library holds them (for example "Pear Therapeutics, Inc.", "Akili Interactive Labs, Inc.").

## Workflow

### Step 1. Write each assumption back

Numbered, verbatim, with the company it concerns and the memo date.

### Step 2. Match a public signal

From `monitoring-signals.md` section 1, give each assumption its signal, its source and call, and what the signal cannot show. Where none fits, write "not measurable from the record (T3)" and say the person's own data would be needed, labeled non-public. Never stretch a signal: an authorization count does not show that a product is marketed; a filing count does not show funding; evidence maturity is the library's convention, not evidence quality.

### Step 3. Value at the memo

Take the value from the memo's fact base (from `investment-memo-and-decision-record` A1, or the person) with its retrieval date. If the memo did not record it, write "not recorded at memo" and say a rerun now gives a baseline, not a change. For evidence maturity, record the rubric version at the memo (rubric v1 is dated 7 October 2026 in the saved run); without it, later comparison is flagged T4. If the memo date is before 7 October 2026 (the rubric v1 date in the saved run), flag T4 even when no value was recorded at the memo.

### Step 4. Trigger, owner, reread date

Write the person's trigger, owner and reread date. Missing owner: "owner not named" (T1), ask. Missing reread date: "not given" (T2), ask. Never suggest a job title. If asked for proposed triggers, label each "proposed" with the row or file behind it, and apply none until confirmed.

### Step 5. Note when a change can appear

From `monitoring-signals.md` section 3, the filing clocks that bear on each signal (for example 8-K within four business days, DL-019; Form D within 15 days of first sale, DL-002), as facts about when a record can exist. Note the library change log's start (12 October 2026 in the saved run): a memo dated earlier cannot be checked for the gap through `get_deltas` (T5).

### Step 6. Write the register

With code execution, write the register CSV in the shape of `evals/files/assumption_register_illustrative.csv` and, if saved library outputs exist, run `python3 scripts/thesis_check.py --register REGISTER.csv --as-of DATE ...` to test that each signal resolves.

## Build the output

Follow `assets/watch-list-output.md`. Answer first: how many assumptions can be watched from the record, which cannot, and what the person still has to give (triggers, owners, reread dates). Short mode: 450 words maximum, counted without the calls list and the Source, Source of now and Rows columns. Before handing over, count the words with `python3 scripts/thesis_check.py --words ANSWER.md` (counts the body above the calls list and leaves out Source, Source of now and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Assumptions, triggers, owners and reread dates are the person's words; proposals are labeled.
- Each signal names what it cannot show.
- No watch tool is called or offered as set.
- An assumption that the company is operating is tied to the company status step (`monitoring-signals.md` section 6), never to the filing count.
- `python3 scripts/thesis_check.py --words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Evidence maturity over time with a named framework: `evidence-maturity-monitoring` (this pack).
- Several holdings at once: `investment-portfolio-monitoring` (this pack).
- Device status signals and register watches: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
