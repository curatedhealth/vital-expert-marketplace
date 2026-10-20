# A2 Drift, calibration and adaptation read

Framework task: DH-01.04.2.2 and DH-01.06.1.2, Part A, task A2. Carries the old task "DH-01.06.1.2.1 Personalisation Adaptation Monitoring" (old title in its original spelling) and the reading half of "DH-01.04.2.1.3 Drift watch" and "DH-01.04.2.2.2 Promotion score" (whether the watch has fired).

## What this task delivers

A dated read of a released model on the person's own prediction log: per period, event rate, mean predicted risk, observed to expected ratio, AUROC, calibration slope and sensitivity at the person's threshold; each input against the person's reference period (mean, missing share, standardized mean difference); groups in the latest period; and, for a personalization engine, the decision log against the rule table (decisions outside the allowed options, missing tailoring data handled other than the rule says, per-option proximal outcome and engagement rates, engagement by week). Flags are raised only on the person's thresholds. Public safety records for the person's named product are read and quoted as stored. It answers "as of a date, what moved in our model's inputs, calibration and performance, and is our engine doing what its rules say?"

Why it matters: the FDA draft notes performance may change with patient populations, disease patterns or data drift, and automation may hide it from users (FDA AI-enabled device software functions draft guidance, January 2025, DA-45). A read that raises flags on thresholds nobody chose, or that compares options the rule itself picked as if they were randomized, tells the team something false.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-01.04.2.2); `ai-ml-governance-director` (old DH-01.06.1.2.1). Work as a monitoring analyst who computes on the person's logs and quotes public records as stored |
| Skill | DH-01.04.2.2 and DH-01.06.1.2 Part A, Drift, calibration and adaptation read |
| Workflow | The steps below |
| Knowledge | `references/monitoring-rules.md` sections 3 to 7 and 9; rows DA-37, DA-38, DA-43 to DA-45, DA-63, DA-87 to DA-93, DA-119, TM79, TM84, TM87, TM89, TM90, TM93; `references/tools.md` |
| Tools | `scripts/drift_check.py drift`, `adaptation`, `words`; `regulatory-dh.search_devices` and `regulatory-dh.search_safety_events` for the person's named product |
| Prompt | This guide |
| Template | `assets/drift-calibration-and-adaptation-read-output.md` |
| Input | The request and its context: the prediction log (CSV: period, id, p, y where known, input columns, group columns), the reference period, the person's thresholds file (operating threshold, O/E range, AUROC floor, SMD and missing-share limits, date written), the decision log (date, decision_point, user_id, tailoring_missing, option_delivered, proximal_outcome, engaged) and the rule table, the read date, the named product and manufacturer |
| Governance | `references/governance.md`; thresholds and readings are the person's |
| Catalogue job | none (no saved `list_jobs` entry for model monitoring; needs a live check) |

## The rule that shapes this task: compute everything, flag only on their thresholds

The script computes the values. A value becomes a flag only against a threshold the person wrote, with its date. Without thresholds, write "thresholds not given; no flag raised" and report the changes as facts. The model never says a model "is drifting" or "is stable".

## Workflow

### Step 1. Scope and dates

Write back the model and version, the reference period, the periods read, the read date and the thresholds file with the date written (or "not given"). Name the kind of drift the person asks about, using the rows' terms: input drift (covariate shift), concept drift, calibration drift (Sahiner et al. 2023, DOI 10.1259/bjr.20220878, DA-87 to DA-89; Davis et al. 2017, DOI 10.1093/jamia/ocx030, DA-91).

### Step 2. Performance and calibration by period

With code execution: `python3 scripts/drift_check.py drift --log LOG.csv --reference PERIOD --thresholds TH.json --inputs COL1,COL2 --groups COL`. Report the period table and the flags on the person's thresholds. Count predictions without an outcome and say the period is read on outcomes known only. Report the movement between the reference and the latest period as facts, and quote the Davis pattern: recalibration fits calibration drift with event-rate shift and stable discrimination; association or case-mix shifts need more (DA-92). Whether discrimination is "stable" is the person's reading on their own threshold.

### Step 3. Inputs

Report each input's mean, SD, missing share and standardized mean difference against the reference period, with flags on the person's limits only. An input change is a fact about the data; its cause (a new assay, a new device, a population change) is the person's to establish. Acquisition devices are a common cause of input drift (DA-88).

### Step 4. Groups

Report the latest period by group. Overall performance can mask subgroup performance (FDA draft, DA-43). Where the person watches calibration and equal error rates across groups with different outcome rates, state the impossibility row (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119).

### Step 5. Personalization engine (old "Personalisation Adaptation Monitoring")

With code execution: `python3 scripts/drift_check.py adaptation --log DECISIONS.csv --rules RULES.csv`. Report decisions outside the allowed options with their dates and options (TM79), decisions with missing tailoring data delivered other than the rule says (TM89), per-option proximal outcome and engagement rates (TM84, TM87) and engagement by week. Say the option comparisons are descriptive because the rule chose the option; causal effects need a micro-randomized trial (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM90). Whether personalization improves outcomes is not answered by this log; list it as a gap with what would answer it. If the engine learns after release, note the EU AI Act duty on feedback loops (Article 15(4), DA-63; 2 August 2028 for Annex I devices, DA-67).

### Step 6. Public safety records (only for a named product)

Call `regulatory-dh.search_devices {query: "NAME", jurisdiction: "all", limit: 10}` to get the stored manufacturer spelling, then `regulatory-dh.search_safety_events {manufacturer: "STORED NAME", since: "YYYY-MM-DD", limit: 10}` with the person's since date (or "not given"; ask). Quote each recall or alert by title, date, severity and manufacturer as stored; MAUDE counts carry no manufacturer and are not attributed (`tools.md`). Do not judge relevance. An empty result is not evidence of safety. `get_deltas` has no change log without a watch, and no watch is ever set: compare dated reruns instead.

## Build the output

Follow `assets/drift-calibration-and-adaptation-read-output.md`. Answer first: what moved between the reference and the latest period, which of the person's thresholds were crossed (or "thresholds not given"), outcomes still pending, and for an engine the decisions outside its rules. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every value comes from the script output on the person's log.
- Every flag rests on a threshold the person wrote, with its date; none supplied.
- No "drifting", "stable", "safe" or "fit for use".
- Pending outcomes are counted.
- Option comparisons are called descriptive.
- Safety records are quoted as stored, without relevance judgments.
- `python3 scripts/drift_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Input data quality (conformance, completeness, plausibility): `data-quality-monitoring` (this pack).
- Therapeutic efficacy and safety signals against the mechanism: `dh-clinical-development` mechanism-validation-monitoring.
- Reportability of an event: `dh-regulatory-and-quality` audit-capa-and-complaints.
