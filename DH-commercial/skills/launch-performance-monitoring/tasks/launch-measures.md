# A2 Launch measures

Framework task: DH-02.01.1.2, Part A, task A2. Replaces the earlier "Launch measure definition" and "Launch week score" sections.

## What this task delivers

The person's launch measure sheet, written down plainly (what is counted, from which record, for which period, against which threshold), and the measures computed from the person's own records: accounts reached, meetings held and cancelled, briefings delivered against the roster, leave-behinds, claim ids used, and unapproved claim ids used. Each number states its basis. Briefing misses and meeting misses are kept apart.

Why it matters: a launch week read from impressions, or from revenue alone when contracts take months, hides the two things that break a digital health launch early: people selling before they were briefed, and claims in the field that were never approved. Oral statements by representatives show intended use (PC-US-17), so claim use is a regulatory fact, not only a sales metric.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.01.1.2 Part A, Launch measures |
| Workflow | The steps below |
| Knowledge | `references/launch-measures.md`; the approved claim list and roster from the sibling skill |
| Tools | `scripts/launch_measures.py`; no library call |
| Prompt | This guide |
| Template | `assets/launch-measures-output.md` |
| Input | The request and its context: the person's measure sheet or the counts they care about, their thresholds, the period, the activity log export, the roster with due dates, the approved claim list |
| Governance | `references/governance.md`; thresholds are the person's |
| Catalogue job | none. The measures run on the person's own data with `scripts/launch_measures.py`. |

## Read the request

- **Measures.** Take the person's. If they have none, offer the metric names in `references/launch-measures.md` as a starting list, labeled "starting list", and ask which to keep and what threshold each has. Exclude counts nobody will act on (old task rule). Revenue is never the only launch-week measure when the contract cycle is longer (old task rule).
- **Thresholds.** The person's. Without one, the measure is reported without a verdict.
- **Period and as-of date.** Ask if missing.
- **Records.** An export from the system of record (CRM activity log, briefing log). Pseudonymous rep ids are enough. Never ask for patient data.
- **Approved claim list and roster.** From the sibling skill or the person. Without the list, unapproved claim use is "not measured".

## Workflow

### Step 1. Write the measure sheet back

One line per measure: id, label, metric, record, period, comparison, threshold, owner. Ask the person to confirm. A measure without a record that can count it is "not measured `[GAP]`", naming the record that would hold it.

### Step 2. Prepare the files

Map the person's export to the script's columns (`date,role,person,account,activity,claim_ids,outcome`; roster `role,person,briefer,briefing_due`; claims `id,claim,status`; measures JSON). Keep the mapping in the output so the numbers can be traced. Never fill a missing count with an estimate (old task rule).

### Step 3. Compute

With code execution, run `scripts/launch_measures.py --activity ... --roster ... --claims ... --measures ... --start ... --end ... --as-of ...`. Without code execution, compute the same counts by hand and show the arithmetic. Report every number with its period, denominator and as-of date.

### Step 4. Keep the two kinds of miss apart

Report briefing status per roster person (briefed, past the person's due date, due date not reached, no due date) separately from meeting outcomes per person (old task rule). A rep who met customers before being briefed is a fact to report, not a judgment.

### Step 5. Flag what touches a rule

For each unapproved claim id used, record date, rep id and account, and point to `references/launch-measures.md` (PC-US-17, PC-EU-03). For any free item or code recorded as an activity, point to the CP rows. These are stops for B1, not verdicts.

## Build the output

Follow `assets/launch-measures-output.md`. Answer first: the measures against the person's thresholds (met, missed, not measured, no threshold), then the unapproved claim uses and the briefing gaps. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every threshold is the person's and the output says so.
- Every number has its basis; no estimate fills a gap.
- No cause is stated for a miss.
- The person's records were not sent to any library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Payer uptake and coverage rates: Market Access. Customer outcomes: Customer Success.
- Uptake, activations or prescriptions are never clinical evidence.
- Whether a field statement was lawful: the person's regulatory or legal owner.
