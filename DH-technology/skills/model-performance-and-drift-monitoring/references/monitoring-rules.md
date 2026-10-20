# Monitoring rules for a released clinical model or personalization engine

What the sourced rows say about checking a model's records, watching its performance, calibration, inputs and adaptive rules after release, and responding to a fired watch. Rows (URL, verbatim quote, read date) are in `DATA_AND_AI.md` (DA), `AI_ML_REGULATION.md` (US, EU, UK, IM) and `THERAPEUTIC_MECHANISM_AND_TRANSLATION.md` (TM). No source here sets a drift threshold, an acceptable calibration range, an AUROC floor, a fairness tolerance, a missing-data share or a review cadence (DATA_AND_AI.md, "Not sourced"). Those are the person's.

## 1. Status of each source

| Source | Status as read | Rows |
|---|---|---|
| FDA, AI-Enabled Device Software Functions draft guidance | Draft, 7 January 2025; still draft on 19 October 2026; on CDRH's FY 2027 A-list | DA-35, US-19, US-21, US-22 |
| FDA PCCP final guidance | Final, reissued 18 August 2025 | US-01 to US-14, US-36 |
| FDA request for comment on real-world performance and drift (FDA-2025-N-4203, comments by 1 December 2025) | Not guidance | US-39 |
| EU AI Act Articles 12, 15 and 72 | Law; Chapter III Sections 1 to 3 apply from 2 August 2028 for AI in Annex I devices, 2 December 2027 for Annex III, as amended by Regulation (EU) 2026/1744; Article 72(3) template now Commission guidance by 2 September 2027 | DA-54, DA-55, DA-63, DA-65 to DA-67, EU-19, EU-33 to EU-36 |
| MDCG 2025-6 FAQ | Not legally binding; uses the pre-omnibus date 2 August 2027 | EU-25, EU-32, EU-36 |
| NIST AI RMF 1.0 | Voluntary | DA-02, DA-14, DA-16 |
| GMLP principle 10 | Principle | UK-10 |
| WHO 2021 and LMM guidance | Publication pages and news releases only | DA-29, DA-33 |

## 2. What a complete model record holds

The old tasks define the elements; the rows explain why each matters. They become the person's pass rule only when the person confirms them.

| Element | Old task | Rows |
|---|---|---|
| Intended use with the decision named (not "clinical decision support" alone) | DH-01.04.3.1.1, DH-01.04.3.2.1 | DA-10, DA-11 |
| A locked test set that is not the training set, with its independence (site, time) stated | DH-01.04.3.1.2, DH-01.04.3.2.1 | DA-39 to DA-41 (draft) |
| A metric named before the run | DH-01.04.3.1.3, DH-01.04.3.2.1 | DA-13 |
| Subgroup results; absent populations marked not validated | DH-01.04.3.2.2 | DA-38, DA-43 (draft) |
| A run id, a holdout metric and an approver for each production model | DH-01.04.2.2.1 | DA-13 |
| A drift watch for each production model, with signal, threshold and action | DH-01.04.2.2.2 | DA-44 (draft), DA-14 |

"Do not pass on an internal demo"; "do not treat a high metric as completeness" (old tasks DH-01.04.3.2.1, .2). `scripts/drift_check.py records` prints flags V1 to V4, P1, P2, W1 to W4 against these elements, and pass or fail only against the rule the person wrote.

## 3. Why watch after release

- Input data drift between development and deployment (FDA draft, DA-37); performance may change with patient populations, disease patterns or data drift, and automation may hide it from users (DA-45); the draft recommends a postmarket performance monitoring plan within the quality system (DA-44, US-37), generally not required for a 510(k) unless a special control, possibly a PMA condition of approval (US-38). Draft: never "required".
- Under an authorized PCCP, FDA anticipates manufacturers will monitor safety and performance as changes are made; the Modification Protocol describes post-market surveillance plans (US-36, final).
- EU AI Act: automatic logs over the lifetime that support post-market monitoring (Article 12(1) and (2), DA-54, DA-55); post-market monitoring actively and systematically collects and analyzes performance data (Article 72(2), DA-65, EU-33); for MDR or IVDR devices it may be integrated into the existing post-market surveillance system (Article 72(4), EU-34). Dates as amended (DA-67).
- NIST MEASURE 3.1: track risks on intended versus actual performance in deployment; MANAGE 4: response, recovery and post-deployment monitoring plans (DA-14, DA-16; voluntary). WHO principle 6: continuous, transparent assessment during actual use (DA-29). GMLP principle 10: deployed models are monitored and retraining risk is managed (UK-10).

## 4. Kinds of drift (Sahiner et al. 2023, DOI 10.1259/bjr.20220878; Davis et al. 2017, DOI 10.1093/jamia/ocx030)

| Kind | Meaning | Row |
|---|---|---|
| Data drift | A mismatch between the conditions of training and clinical use | DA-87 |
| Input drift (covariate shift) | A change in the characteristics of input data; acquisition devices are a common cause | DA-88 |
| Concept drift | A change in the relationship between inputs and targets | DA-89 |
| Calibration drift | Calibration deteriorates over time; updating should respond to rapid drift, not only fixed annual or biannual schedules | DA-91 |

Responses range from a warning to retraining or an architecture change (DA-90). Recalibration fits calibration drift with event-rate shift and stable discrimination; association or case-mix shifts need more (DA-92). Clinicians should note misalignment between model predictions and their judgment (Finlayson et al. 2021 [WF], DOI 10.1056/NEJMc2104626, DA-93).

## 5. What the script computes (methods, not thresholds)

`scripts/drift_check.py drift` computes, per period and on outcomes known only: event rate, mean predicted risk, observed to expected ratio, AUROC, calibration slope, and sensitivity at the person's threshold; per input: mean, SD, missing share and standardized mean difference against the person's reference period; by group in the latest period. These are computation methods. The thresholds that turn a value into a flag come only from the person's thresholds file, with the date they wrote it; without one, values and changes are reported and no flag is raised. Predictions whose outcomes are not yet known are counted and left out of the period's performance.

## 6. Subgroups and fairness over time

Representativeness for monitoring and subgroup evaluation (FDA draft, DA-38); overall performance can mask subgroup performance (DA-43). For any single threshold, a well-calibrated model will never have the same sensitivity and specificity for two groups with different outcome rates (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119): when the person watches both, say so. Fairness tolerances are the person's; governance of bias is `responsible-ai-governance` (this pack).

## 7. Personalization engines in use

- Watch the allowed options, the missing-data rule, proximal outcomes, and engagement and fatigue (Nahum-Shani et al. 2018, DOI 10.1007/s12160-016-9830-8, TM79, TM84, TM87, TM89). `scripts/drift_check.py adaptation` counts decisions outside the allowed options, decisions with missing tailoring data delivered other than the rule says, and per-option outcome and engagement rates.
- Option comparisons from a log where the rule chose the option are descriptive; the micro-randomized trial estimates causal effects on proximal outcomes (TM90).
- Comparing what is delivered with the intervention theory separates adaptations that fit context from changes that undermine fidelity (Moore et al. 2015, DOI 10.1136/bmj.h1258, TM93).
- A system that keeps learning must reduce biased outputs feeding future inputs (EU AI Act Article 15(4), DA-63).

## 8. Responding to a fired watch or a failed element

- Name the owner; state retrain, roll back, or stop the decision; name the version that replaces the current one, or the time the decision stays stopped; never leave a fired watch with no action; never ignore a fired watch because the average metric is fine (old tasks DH-01.04.2.2.2, DH-01.04.2.2.3).
- For an incomplete validation: name the missing item and the owner, state whether the model may influence the decision, name the date the record will be complete; an incomplete model does not influence the named decision (old task DH-01.04.3.2.3).
- For personalization: write the pass rule before scoring (rule, population, outcome watched; the element that blocks release); for each failed element the owner and the recheck date, or the unit stopped; never close a failed element because an assessment already described it (old tasks DH-01.06.1.2.2, .3).
- All of these are the person's decisions. The model lays out the facts and writes down what the person decides.
- Change control: a change specified in an authorized PCCP and done per its Modification Protocol needs no new submission but is documented in the quality system (US-12); deviating from an authorized PCCP would generally make the device adulterated and misbranded (US-13); EU pre-determined changes (Article 43(4), EU-05). Whether a retrain fits is `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Whether an event is reportable (MDR, vigilance, recall) is `dh-regulatory-and-quality` audit-capa-and-complaints; the model never decides reportability.

## 9. Public safety records

Recalls, MAUDE counts and MHRA alerts from the library are described only by what each record states: title, date, severity and manufacturer as stored (`tools.md`). The model does not judge a record's relevance to the person's product; that reading is the person's. MAUDE counts carry no manufacturer and are never attributed to one company. An empty result is not evidence of safety.
