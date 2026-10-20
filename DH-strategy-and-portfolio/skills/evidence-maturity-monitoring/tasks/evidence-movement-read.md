# A2 Evidence movement read

Framework task: DH-DIL.2.2, Part A, task A2. New in this suite (see A1).

## What this task delivers

A comparison of two dated evidence maturity runs for each tracked company: the score and points on both dates, every difference classified (INPUT, METHOD, COVERAGE, RESOLUTION), the record behind each INPUT change once read, the change log's own limits where it is used to date an event, and the framework level unchanged unless the person confirms a new one. Counts and classes come from `scripts/maturity_diff.py`; the person's measures judge them in B1.

Why it matters: the same library function produces the score in every tool (compare_portfolio formula note, 19 October 2026), so a score difference can be real, an artifact of what was loaded, or a different company. The classes keep the three apart.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old skill "Worker: not bound"); see `references/governance.md` |
| Skill | DH-DIL.2.2 Part A, Evidence movement read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md` sections 1, 2 and 4; `references/company-status.md` (DL-135 to DL-168); A1 measures if they exist; rows CV140, CV144 to CV146, DE14, DE31, DE32, DL-128, DL-129 |
| Tools | `scripts/maturity_diff.py`; `diligence-dh.get_evidence_maturity` for a fresh run; `diligence-dh.list_sources` (free; needs a live check) for the perimeter; optionally `diligence-dh.get_deltas` to date an event |
| Prompt | This guide |
| Template | `assets/movement-output.md` |
| Input | The request and its context: the earlier saved run (file and date), the later run or permission to make one, the exact references, A1 measures |
| Governance | `references/governance.md`; differences are facts, the person judges them |
| Catalogue job | none (the old job `evidence-maturity` reads once; needs a live check) |

## Read the request

- **Two runs.** The earlier saved output with its date. If the person has only one, offer to save it as the baseline: "Earlier run not given `[GAP]`".
- **Same reference.** The later run must use the same `company` argument. If the person's files use different references, say so and compare like with like.
- **Full responses.** A trimmed output may lack the rubric version, maxima or excluded list; the script says what it could not compare.

## Workflow

### Step 1. Make or load the later run

If the person asks for a fresh read, call `diligence-dh.get_evidence_maturity {company: "<same reference as before>"}` and `diligence-dh.list_sources {}`; save both with the date.

### Step 2. Run the diff

`python3 scripts/maturity_diff.py EARLIER.json LATER.json [--company NAME]`

Report each company's block and the coverage block as printed. Do not restate differences in your own arithmetic.

### Step 3. Carry forward resolution flags

Carry forward every resolution risk flag from either run, verbatim (for example somnio, 19 October 2026: "2 filing names normalize to this company and are combined; the combination is a proposal until a person validates it"), classed RESOLUTION, until the person validates it. The script prints them under "Risk flags carried forward". Quote recall flags and safety events as stored in either run; a field one run lacks is "not in that run", never 0 or none.

### Step 4. Company status

The runs do not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. Run the status step in `references/company-status.md` for each company: read its filings or register entry where you can open them (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices) for the period between the runs; otherwise list the exact filings to open and write "Status: [GAP]: not read". Never infer status from press or memory; a Form 15 or Form 25 is not dissolution (DL-144; DL-149 (inference)). For SEC access, ask which contact the person's organization uses (DL-153 [WF]); never send the person's email address or name and never invent one.

### Step 5. Read the record behind each INPUT change

For each INPUT change, name the record type that would show it (`monitoring-signals.md` section 2) and, if the person wants, find it: a new authorization by its reference, a registered trial by its registry id, results by the registry entry. Optionally call `diligence-dh.get_deltas {companies: ["<name>"], since: "<earlier run date>"}` to date the event, and report its limits (log started 12 October 2026; event dates, not load dates; "no change recorded" is about the log). If the period starts before 12 October 2026, say the log does not cover the earlier part and offer the company's dated primary filings (EDGAR filing list) and authorization records (FDA decision dates) for it instead of reporting "no change". Until the record is read, write "record not yet read".

### Step 6. Say what METHOD, COVERAGE and RESOLUTION changes mean

One line each: the score moved because the convention, the loaded sources or the resolved company changed, not the evidence.

### Step 7. Apply A1 measures if they exist

Mark each measure: triggered, not triggered, or not measurable with these runs, citing the class and the record. Without A1 measures, report the classes only and say B1 needs the person's measures.

## Build the output

Follow `assets/movement-output.md`. Answer first: per company, score then and now, whether any difference is an INPUT change with its record, and status as read (or "[GAP]: not read"). Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every difference carries its class from the script; every resolution flag from either run is carried forward verbatim.
- Each company has a status line: read from a filing or register, or "Status: [GAP]: not read" with the filings to open.
- No missing field printed as 0 or "none".
- Word count: run `python3 scripts/maturity_diff.py --count ANSWER.md` on the short answer; at or under 450 words, counted without the calls list and source columns.
- No INPUT change is called new evidence before its record is read.
- "No change recorded" is reported with the log's limits.
- No score is compared with a benchmark; no company is rated or ranked.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Grading a new study: `dh-clinical-development` literature-and-real-world-evidence-review.
- Regulatory meaning of a new authorization: `dh-regulatory-and-quality` regulatory-pathway-monitoring.
- Change tracking across a market: `pipeline-and-market-monitoring` (this pack).
