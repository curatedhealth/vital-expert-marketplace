# A2 Governance effectiveness indicators

Framework task: DH-03.02.3.2, Part A, task A2.

## What this task delivers

A set of indicators computed from the person's own data: management review coverage and action closure, audit finding closure and repeats, CAPA ageing and effectiveness verification, and reporting timeliness where they supply event dates. Beside them, external context: FDA's FY 2025 Form 483 citation categories, labeled pre-QMSR, and safety events for the person's own product from the library. It answers "is our quality governance doing its job, in numbers?"

Why it matters: CAPA procedures and complaint procedures were the two most cited device observations on FY 2025 483s (279 and 211 citations, QS53), and management review and audit records are now inspectable (QS15). Indicators built from the person's own records show whether governance is closing what it opens.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Quality & Software Lifecycle Director (`quality-systems-director-software`) |
| Skill | DH-03.02.3.2 Part A, Governance effectiveness indicators |
| Workflow | The steps below |
| Knowledge | `references/indicators.md`; `references/quality-systems-research.md` (QS51 to QS54, VG rows); `references/data/fda_483_fy2025_devices.csv` |
| Tools | `regulatory-dh.list_jurisdictions` (free), `regulatory-dh.search_safety_events` (counted, optional); `scripts/qms_indicators.py` (optional) |
| Prompt | This guide |
| Template | `assets/indicators-output.md` |
| Input | The request and its context: the person's management review list, audit finding log, CAPA log, event log (aggregates or CSV), the as-of date, any thresholds they set |
| Governance | `references/governance.md`; the person's data stays in the conversation; FDA-wide figures are context, never targets |

## Read the request

- **Data.** Ask for the logs they hold, in the columns `scripts/qms_indicators.py` reads (listed in its header), or as a table in the message. Aggregates are enough.
- **As-of date.** Every age is counted to it. Default to the date of the conversation and say so.
- **Their rules.** Ask whether they have thresholds (for example an age by which a CAPA should close). Without rules, report numbers and no verdict.
- **Mode.** Short for a direct question; full for a management review input pack.

## Workflow

### Step 1. Take the data

Put the person's records into the indicator tables. Check consistency (a close date before an open date, a due date missing). Blank means not measured: mark `[GAP]` and name the log that would hold it.

### Step 2. Compute the indicators

With code execution, run:

- `python3 scripts/qms_indicators.py capa CAPA.csv --as-of YYYY-MM-DD` (add `--bins` only with bins the person chose)
- `python3 scripts/qms_indicators.py findings FINDINGS.csv --as-of YYYY-MM-DD`
- `python3 scripts/qms_indicators.py mr REVIEWS.csv --required "their;input;list"`

Without code execution, compute the same by hand. Report: open CAPA count, median and oldest age, open past their own due date, closed without a recorded effectiveness verification (EU4); findings closed share, open past due, repeats within three years by MDSAP's definition from the links they give (QS47); review inputs missing against their own list, review actions closed. For reporting timeliness, count calendar days from the awareness date as day 0 for the EU (VG12) and compare with 15, 10 or 2 days (VG4 to VG6), or 30 days or 5 work days for the US (VG17, VG18).

### Step 3. Check against their rules, if any

For each rule the person set, mark the number pass or miss. Without a rule, no verdict: "no rule set".

### Step 4. FDA 483 context (pre-QMSR)

Add, labeled "FY 2025, pre-QMSR", the citation categories from `references/indicators.md`: 791 device 483s (QS52); top five citations with counts (QS53); management review 820.20(c) 49, quality audits 820.22 57, MDR procedures 803.17 63 (QS54). With code execution, `qms_indicators.py fda483 references/data/fda_483_fy2025_devices.csv` gives the grouping by section. Say once: FY 2025 ended before the QMSR took effect on 2 February 2026, so the sections are the retired numbering; the spreadsheet is not a complete list of observations (QS51). Use it to show which areas FDA cited most across all device firms, never as a benchmark for the person.

### Step 5. Safety events for their product (optional)

Call `regulatory-dh.list_jurisdictions` (free), then `regulatory-dh.search_safety_events` with the person's `manufacturer` or `product`, a `since` date they choose and `limit` 10. Read `references/tools.md` first (the product-code filter did not filter; recall source URLs point to the API). Report each event only by its record. If an event's summary names a process (complaints, a software change), add "process touched, per the summary". No event is not evidence of no events.

### Step 6. What it means for the person

Two or three consequences from the rows only, stated conditionally. Examples: "Two repeat findings within three years would count as repeats under MDSAP grading, which adds a point to a nonconformity's grade (QS45, QS47)." "Management review records with missing inputs are now readable by an investigator (QS15)."

## Build the output

Follow `assets/indicators-output.md`. Answer first: the two or three indicators that moved most or sit furthest from the person's rules, with the numbers. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every number is from the person's data, a research row, or a saved tool output.
- The FY 2025 483 figures are labeled pre-QMSR and context only.
- No cause is stated for any indicator; causes are hypotheses for B1.
- No verdict without the person's rule.
- The person's data went into no library call.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Measurement only. Repair and ownership are B1. Evidence per process is A1.
- No prediction of inspection outcomes.
- Drugs, biologics and wellness apps are out of scope.
