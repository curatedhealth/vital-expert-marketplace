# A2 Handoff score

Framework task: DH-01.01.3.2, Part A, task A2. Replaces the earlier "Handoff score" section (DH-01.01.3.2.2).

## What this task delivers

Every handoff due in the period, plus earlier ones still open, scored against the person's confirmed rule as received, late, open or not measurable, with the work product name kept, the fact behind each status, counts by the person's categories, and critical-to-quality handoffs reported apart. Nothing is dropped.

Why it matters: a list that quietly loses its open items always looks better than the work did. Keeping a late clinical evidence handoff apart from a late copy handoff (the old framework's rule) shows where a slip touches participants, results or the device file.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.01.3.2 Part A, Handoff score |
| Workflow | The steps below |
| Knowledge | A1's confirmed measure; `references/measurement-rules.md`; rows CS27, CS28, CV29, CS9, CS44 |
| Tools | `scripts/handoff_log.py score`; optional `regulatory-dh.search_safety_events` only when the person asks about a named product's public events |
| Prompt | This guide |
| Template | `assets/handoff-score-output.md` |
| Input | The request and its context; the person's log; A1's measure and period |
| Governance | `references/governance.md`; the score applies the person's rule and rates no one |
| Catalogue job | none |

## Workflow

### Step 1. Confirm the measure

Use A1 from the conversation. If there is none, run A1 in short mode first, or score with the default rule only after the person confirms it in one line. Say which rule is applied and its date.

### Step 2. Score

With code execution: `python3 scripts/handoff_log.py score LOG.csv --from YYYY-MM-DD --to YYYY-MM-DD`. Without it, apply the same rule by hand:
- **received:** received on or before the period end, by the named receiver, on or before the due date;
- **late:** received by the named receiver after the due date (days after stated);
- **open:** not received by the period end;
- **not measurable:** no due date, no named receiver (checked before open or received, as `references/measurement-rules.md` section 3 says), a received date with no named recipient, or a recipient other than the named receiver. Each says what is missing, `[GAP]`, and the answer asks the person; the model never rules on it.

If the person's rule differs from the script's default, apply the person's rule and say so; do not bend the data to fit the script.

### Step 3. Counts, kept apart

Report counts by status, and by the person's category and CTQ mark, each separately. Report "received on time over measurable handoffs" only with its denominator stated and the not-measurable items listed beside it. Never merge categories into one score unless the person's measure does.

### Step 4. Facts, not causes

For each late or open item, state the fact (dates, names) from the log. Do not say why it slipped unless the person says so, and then in their words. Lateness is one dimension of execution quality (CS9), not a judgment of a team.

### Step 5. Public events, only if asked

If the person asks whether a public event bears on a handoff they track (for example a recall on a comparable product), call `regulatory-dh.search_safety_events {product_code}` or `{manufacturer}` and quote the library row's summary with date, severity and source. Describe it only by what the row states; say the library row states no cause beyond the quote (FDA's recall page not read `[GAP]`), and do not judge whether it bears on the person's product or handoff.

### Step 6. Feed back

Offer the score to the functions it counts, for the period it names (audit and feedback, CS44, a labeled pattern). Who receives it is the person's choice.

## Build the output

Follow `assets/handoff-score-output.md`. Answer first: counts by status, the critical-to-quality handoffs that are late or open, the not-measurable items and what each lacks. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every handoff due in the period, and every earlier open one, is listed with its work product name.
- The rule applied is the person's, named and dated.
- Categories and CTQ handoffs are counted apart; any rate shows its denominator.
- No cause, fault or rating is stated beyond the person's words; public records are quoted, not interpreted.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Repairs for what did not arrive: B1 alignment repair.
- Whether a late clinical evidence handoff affects a submission or a study: `dh-regulatory-and-quality` regulatory-submission-and-dossier and `dh-clinical-development` trial-operations-monitoring.
- CAPA for a recurring miss: `dh-regulatory-and-quality` audit-capa-and-complaints, if the person the user names for quality opens one.
