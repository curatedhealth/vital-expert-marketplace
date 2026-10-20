# A1 Evidence measures

Framework task: DH-DIL.2.2, Part A, task A1. New in this suite: the old dh-diligence skills read evidence maturity once and had no monitoring step.

## What this task delivers

The measures the person will use to watch a company's evidence over time, written with the person: which record events count as movement for their thesis (each with the record that would show it and the row behind it), which framework level they track and its confirmed baseline, which changes do not count (method, coverage, resolution, unconfirmed levels, funding), the fields to save at each run, and the reread date the person sets.

Why it matters: a score that moves from 67 to 78 reads like progress. Under the library's own formula a score can move because a source was loaded or the rubric changed (`monitoring-signals.md` section 1). Measures written in advance say which movements the person will act on and which they will not.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old skill "Worker: not bound"); see `references/governance.md` |
| Skill | DH-DIL.2.2 Part A, Evidence measures |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md`; `references/evidence-frameworks.md`; `references/company-status.md` (DL-135 to DL-168); rows DE19, DE25, CV132, CV140, CV141, CV144 to CV146, DE1, DE14, DE15, DE30 to DE32, DL-113 (DOI 10.1038/s41746-023-00836-5), DL-117 (DOI 10.2196/37677), DL-124 (DOI 10.1371/journal.pone.0323390), CS56 |
| Tools | None |
| Prompt | This guide |
| Template | `assets/evidence-measures-output.md` |
| Input | The request and its context: the companies tracked (exact references), the person's thesis in their words, the framework and level they confirmed (if any), what they want to act on, the reread date |
| Governance | `references/governance.md`; the person sets measures, triggers and dates |
| Catalogue job | none |

## Read the request

- **Companies and references.** One exact reference per company, kept the same at every run (`tools.md`: a different reference can resolve to a different set of products).
- **Thesis.** In the person's words. Measures tie to it; the model does not write a thesis.
- **Baseline level.** A framework level the person confirmed, with its date. A level only proposed by `company-and-evidence-assessment` is not a baseline until confirmed.
- **Triggers.** What the person will do something about. If they ask for a target pace ("how fast should evidence mature"), no benchmark is sourced `[GAP]`.

## Workflow

### Step 1. Name the record events that count

From `monitoring-signals.md` section 2, list the events that bear on the person's thesis, each with the record that shows it and its row (new authorization, DL-128 and US-66; new registered trial, CV132 and CV141; results posted, CV145, CV146, CV140; trial terminated or withdrawn, library risk flag; DiGA listing change, DE31; DiGA trial-listing extension requested or granted (an extension exists: DE25 sets its fee; trial listing up to 12 months, DE19); DiGA usage data, DE1 and DE15; a change in company status read from a filing or register, `company-status.md`: 8-K Items 1.03, 2.01, 3.01, 5.01, Form 25, Form 15, Companies House status, German insolvency notices, DL-136 to DL-168). Label any the person did not ask for as "proposed". A Form 15 or Form 25 is not dissolution (DL-144; DL-149 (inference)).

### Step 2. Name what does not count

State, for the person to confirm: METHOD, COVERAGE and RESOLUTION changes; an unconfirmed level; a new Form D (a filing, not evidence; DL-117 and DL-124 found funding did not track evidence); vendor funding totals (DL-125 (inference)); press or deck claims without a record (skill rule, no row).

### Step 3. Fix the framework baseline

If the person confirmed a level, write it with framework, date and who confirmed it. Add what to check at each reread (`monitoring-signals.md` section 3: NICE ESF version, CS56; Evidence DEFINED update cycle, DL-113). If no level is confirmed, write "baseline level not confirmed `[GAP]`" and point to `company-and-evidence-assessment` (this pack) A2.

### Step 4. Fields to save at each run

Proposed, for the person to confirm: the full `get_evidence_maturity` response (not trimmed), the exact `company` argument, the retrieval date, the `list_sources` perimeter, any saved safety events and recall flags (`compare_portfolio`), the company status as read with its filing or register and date (or "[GAP]: not read"), and any record read behind a change. These let `scripts/maturity_diff.py` classify every difference.

### Step 5. Triggers, owners and reread date

Write each trigger in the person's words with the owner they name (or "owner not named") and the reread date they set (or "not given"; ask). Never supply a date or a threshold.

## Build the output

Follow `assets/evidence-measures-output.md`. Answer first: the events that count for the thesis, what does not count, and the baseline. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every measure is the person's or labeled "proposed"; each carries its row.
- No target pace or benchmark; "no benchmark in the sources" where asked.
- No value statement attached to any measure.
- Status events come from filings or registers only; no status from press or memory.
- Word count: run `python3 scripts/maturity_diff.py --count ANSWER.md` on the short answer; at or under 450 words, counted without the calls list and source columns.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The first evidence read and the proposed level: `company-and-evidence-assessment` (this pack).
- Market-wide change tracking: `pipeline-and-market-monitoring` (this pack).
