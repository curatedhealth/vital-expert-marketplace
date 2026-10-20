# A2 Stage status read

Framework task: DH-01.01.1.2, Part A, task A2. Replaces the earlier "Stage score" section (DH-01.01.1.2.2). The score becomes counts and flags; the person's rules judge them in B1.

## What this task delivers

A stage-by-stage read of the person's gate log as of a stated date: owed items accepted, missing, in progress and waived; days open; flags (accepted with no evidence reference, accepted with no named decision, missing with no owner, next stage started while an item is open, open with no reread date). For a marketed product, the post-market events the register holds (recalls, MAUDE report counts, later authorizations), dated against the last gate decision, described only as the records state them, with the stage the person names for each (their call) and where the change question goes.

Why it matters: a stage can look closed on a roadmap while its log shows an item accepted with nothing behind it, or the next stage already running while an item is missing. And a marketed product's lifecycle continues: a software change is a design change (CH9), and post-market data feed the clinical evaluation (PL76).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Product Manager (`digital-health-product-manager`) |
| Skill | DH-01.01.1.2 Part A, Stage status read |
| Workflow | The steps below |
| Knowledge | `references/lifecycle-measures.md` sections 2 and 3; A1 measures if they exist; rows PL59, PL68, PL75, PL76, PL95, PL96, CH4, CH5, CH9, CH11, QS22, QS34 |
| Tools | `scripts/gate_log_check.py`; for a marketed product: `regulatory-dh.search_safety_events {product}` or `{product_code}`, `regulatory-dh.get_authorization {reference}`, `regulatory-dh.search_devices {query}` |
| Prompt | This guide |
| Template | `assets/stage-status-output.md` |
| Input | The request and its context: the gate log, the read date, the stage model, A1 measures, the product's register references if marketed |
| Governance | `references/governance.md`; counts are facts, the person judges them |
| Catalogue job | none (`post-market-watch` belongs to `dh-regulatory-and-quality` regulatory-pathway-monitoring; no watch tool is called here) |

## Read the request

- **Log.** CSV or table with the fields in SKILL.md Input. Missing fields reduce what can be counted; say which.
- **Read date.** The "as of" date the person gives for days open ("today" counts, written as the full date). If none is given, write "read date not given" and ask.
- **Marketed?** If yes, the register reference (K, DEN or P number) or product code. Ask before sending an unpublished name.

## Workflow

### Step 1. Run the log check

Save the log as CSV and run `python3 scripts/gate_log_check.py LOG.csv --as-of YYYY-MM-DD`. Report the table and the flags as printed. Do not restate counts in your own arithmetic.

### Step 2. Read each flag against the sources

For each flag, one line on what the source says it means: F1 (a status with no work product does not show the record, PL9, QS24); F4 (TM3, DOI 10.1136/bmj.n2061: repeat rather than progress automatically while uncertainties remain); F2 (decisions at reviews, PL5). This is context; whether a flag is a miss is the person's rule (B1).

### Step 3. Apply A1 measures if they exist

Mark each measure: met, not met or not measurable with this log, citing the count or flag. Without A1 measures, report counts and flags only and say B1 needs the person's rules.

### Step 4. Post-market inputs (marketed product only)

1. `regulatory-dh.search_safety_events {product: "<name>"}` and, if the product code is known, `{product_code: "<code>"}`.
2. `regulatory-dh.search_devices {query: "<name or maker>"}` for later authorizations.
3. Save the output and rerun the script with `--events FILE.json --product <name>`.

List each event with its date, type, severity, the record's own summary, source and retrieval date, and whether it falls after the last gate decision in the log. Describe each event only by what the record states; do not judge its relevance to the person's product. As context, give the rows that govern any change the person decides to make (software change CH9, CH11; DiGA significant change PL95; clinical evaluation update PL76; risk file update QS22). Whether it reopens a stage, and which, is the person's call: write the stage they name, or "stage not named; your call". Whether it needs a submission or notification: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. MAUDE counts are reports, not confirmed events; an empty result is a gap in the store, not evidence of no event.

## Build the output

Follow `assets/stage-status-output.md`. Answer first: stages with missing or in-progress items, the longest-open stage with its days, and the flags that bear on the person's measures. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Counts come from the script output; nothing is scored or ranked.
- Every register fact has a reference and a retrieval date; recall causes and fixes are not inferred.
- No days-open figure is compared with a benchmark.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Complaint handling and CAPA for a recall: `dh-regulatory-and-quality` audit-capa-and-complaints.
- Register watches: `dh-regulatory-and-quality` regulatory-pathway-monitoring. Change-submission questions: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
