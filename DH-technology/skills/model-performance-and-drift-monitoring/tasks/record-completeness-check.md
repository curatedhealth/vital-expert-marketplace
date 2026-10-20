# A1 Record completeness check

Framework task: DH-01.04.3.2 and DH-01.04.2.2, Part A, task A1. Carries the old tasks "DH-01.04.3.2.1 Validation completeness", "DH-01.04.3.2.2 Validation score", "DH-01.04.2.2.1 MLOps check" and "DH-01.04.2.2.2 Promotion score".

## What this task delivers

For every model version in the person's register: whether its validation and promotion record holds the elements the person's pass rule requires (intended use with the decision named, an independent locked test set, a metric named before the run, subgroup results, a run id, an approver, a drift watch for production models), each failed element named, and every fired watch with or without a recorded action. Built with `scripts/drift_check.py records`. It answers "which of our models in production could not defend their validation record today, and which fired watches are still open?"

Why it matters: the old tasks were blunt: "Do not pass on an internal demo"; "Do not treat a high metric as completeness"; "A fail is a production model with no run id". A register that counts models as validated because someone once reported a good AUROC is the gap a reviewer finds first.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `clinical-algorithm-validator` (old DH-01.04.3.2.1 and .2, DH-01.04.2.2.1 and .2). Work as a model record analyst who checks records against the person's rule |
| Skill | DH-01.04.3.2 and DH-01.04.2.2 Part A, Record completeness check |
| Workflow | The steps below |
| Knowledge | `references/monitoring-rules.md` sections 1 to 3; rows DA-10, DA-11, DA-13, DA-14, DA-38 to DA-44, US-36 to US-38; `references/governance.md` |
| Tools | `regulatory-dh.search_devices` only to confirm a named authorization; `scripts/drift_check.py records`, `words` |
| Prompt | This guide |
| Template | `assets/record-completeness-check-output.md` |
| Input | The request and its context: the model register (CSV: model_id, version, in_production, intended_use, decision_named, decision_excluded, test_set_id, test_set_independent, metric_prenamed, metric_named_on, run_date, run_id, approver, subgroup_reported, absent_population, watch_signal, watch_threshold, watch_action, watch_owner, watch_fired_on, action_taken), the person's pass rule (JSON: required elements, date written), the read date |
| Governance | `references/governance.md`; the person writes the rule |
| Catalogue job | none (no saved `list_jobs` entry for model monitoring; needs a live check) |

## The rule that shapes this task: no rule, no score

The old tasks put the rule first ("Define a complete validation"; "Define a healthy promotion"). The model offers the old tasks' elements as a starting list, labeled "proposed" until the person confirms them, and scores nothing against a proposed rule. Flags are facts about the record either way.

## Workflow

### Step 1. Confirm the pass rule (old "Validation completeness", "MLOps check")

Write the person's rule back verbatim with the date written. If none was given, offer the elements from the old tasks and the rows as a "proposed" list (`monitoring-rules.md` section 2: intended use with decision named; locked test set not the training set; metric named before the run; subgroup results with absent populations marked; run id, holdout metric and approver; a watch for each production model) and ask the person to confirm, change or reject it. Name the period and the models in scope (old task DH-01.04.2.2.1 step 3). The read date is the person's; if not given, "read date: not given" and ask.

### Step 2. Read each record (old "Validation score", "Promotion score")

With code execution: `python3 scripts/drift_check.py records --register REGISTER.csv --as-of READ_DATE --rule RULE.json`. Report flags verbatim: V1 no intended use or decision named; V2 test set independence none or not given (FDA draft, January 2025, DA-39 to DA-41); V3 no metric named before the run, or named after it; V4 no subgroup result (DA-38, DA-43); P1 no run id (on a production model, a fail under the old task); P2 no approver; W1 production model with no drift watch; W2 watch threshold not given; W3 watch fired with no action recorded (open); W4 watch fired with action recorded. Pass or fail is printed only against the person's confirmed rule. Quote metric and dataset version where the register has them; mark absent populations "not validated" (old task DH-01.04.3.2.2).

### Step 3. Open fired watches

List every W3 as open with its fired date, the action the watch specified and the watch owner the register names. A fired watch is never closed because the average metric is fine (old task DH-01.04.2.2.2). The action is B1's and the person's.

### Step 4. Context the person may want

If a production model is part of an authorized device, the draft recommends a postmarket performance monitoring plan within the quality system and says it is generally not required for a 510(k) unless a special control (FDA draft, January 2025, DA-44, US-37, US-38; draft). Under an authorized PCCP, FDA anticipates monitoring as changes are made (US-36, final). Confirm the authorization only if the person names it: `regulatory-dh.search_devices {query: "NAME", jurisdiction: "all", limit: 10}`; quote the record and "library, retrieved DATE".

## Build the output

Follow `assets/record-completeness-check-output.md`. Answer first: the counts against the person's rule (or "pass rule not given"), the production models that fail and on which elements, and the open fired watches. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The pass rule is the person's, with its date; a proposed rule was not used to score.
- Every flag and every pass or fail comes from the script output.
- Open fired watches are listed, none closed.
- No model is called validated; absent populations are "not validated".
- Every fact names its source and date in plain words with the row id after it.
- `python3 scripts/drift_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Rewriting an incomplete record (intended use, test set, metrics): `clinical-ml-model-development-and-validation` (this pack).
- Governance evidence for responsible AI: `responsible-ai-compliance-monitoring` (this pack).
- AI-enabled device readiness after authorization: `dh-regulatory-and-quality` ai-ml-readiness-monitoring.
