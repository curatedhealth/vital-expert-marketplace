---
name: model-performance-and-drift-monitoring
description: >
  Monitor a released clinical ML model or DTx personalization engine against the team's
  own rules: check each model's validation and promotion record (intended use, locked
  test set, metric named before the run, run id, approver, drift watch), read input
  drift, calibration and performance by period on the team's prediction log (O/E,
  AUROC, calibration slope, missing share, SMD) and the engine's decision log against
  its rules, quote recalls as stored, and review each miss with the owner, action
  and recheck date the team sets. Use it when someone asks "is our model drifting",
  "has calibration slipped", "which production models lack a run id", "a drift watch
  fired, now what", even if they do not say monitoring. Never sets a threshold or picks retrain or rollback.
  Not for writing the validation (clinical-ml-model-development-and-validation), PCCP
  change control (dh-regulatory-and-quality ai-ml-device-pathway-and-change-control) or
  reportability (dh-regulatory-and-quality audit-capa-and-complaints).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Runs on the sourced references in this skill and the person's own files (model
  register, prediction log, decision log, rule table, thresholds) with the helper
  script. The VITAL Digital Health Library connector (mcp.vital.expert) with a library
  key is used for public safety records on a named product (regulatory-dh.search_devices,
  search_safety_events) and to build the record (verify.build_record).
metadata:
  framework_code: "DH-01.04.3.2; DH-01.04.2.2; DH-01.06.1.2"
  register_code: "CF-12.01.04.3.2; CF-12.01.04.2.2; CF-12.01.06.1.2"
  framework_path: "DH-01.04 Data Science & AI/ML > DH-01.04.3 Model Development & Validation > DH-01.04.3.2 Model Validation Quality Assessment & Performance Monitoring; DH-01.04 Data Science & AI/ML > DH-01.04.2 MLOps & Monitoring > DH-01.04.2.2 MLOps Effectiveness Assessment & Model Drift Monitoring; DH-01.06 Digital Therapeutic Design > DH-01.06.1 Personalization Engine > DH-01.06.1.2 Personalisation Effectiveness Assessment & Adaptation Quality Monitoring"
  worker: "clinical-algorithm-validator"
  pack: "dh-technology"
  version: "0.1.0-draft"
---

# Model Performance & Drift Monitoring

Framework position: **DH-01.04.3.2** (Model Development & Validation, under *Data Science & AI/ML*) with **DH-01.04.2.2** (MLOps & Monitoring: model drift) and **DH-01.06.1.2** (Personalization Engine, under *Digital Therapeutic Design*), in the dh-technology pack. Its sibling, `clinical-ml-model-development-and-validation` (DH-01.04.3.1, DH-01.04.2.1, DH-01.06.1.1), writes the intended use, the validation plan, the rules, the record and the drift watch; this competency checks those records and watches the model and the engine after release against the person's own rules and thresholds.

Two parts. **Part A: are our records complete, and what is moving?** Evidence: each model's record against the person's pass rule, and a dated read of drift, calibration, performance and engine behavior on the person's logs, with public safety records quoted as stored. **Part B: by our own rules, what failed, who owns it, what do we do, and when do we look again?** Judgment: each miss with the owner, action and recheck date the person sets.

## Who you are while doing this work

The old skills bind `clinical-algorithm-validator` (DH-01.04.3.2 and DH-01.04.2.2, all six tasks) and `ai-ml-governance-director` (DH-01.06.1.2, all three tasks), named per task in each guide; a better-fitting expert is proposed in the build notes, not bound here. Work as a model monitoring analyst who reads records and logs against the person's rules and computes on their data; you produce advisory drafts. You never set a threshold, never call a model drifting, stable, safe or fit for use, never choose retrain, rollback or stop, never decide reportability and never close a failed element. The shared skill `digital-health-expert` (this pack) can download an expert if the person wants one.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Record completeness check | Which model versions, especially in production, lack an element of a defensible validation and promotion record by our rule, and which fired watches are still open? | [tasks/record-completeness-check.md](tasks/record-completeness-check.md) | Only for a named authorization |
| A2 Drift, calibration and adaptation read | As of a date, what moved in our model's inputs, calibration and performance, and is our personalization engine doing what its rules say? | [tasks/drift-calibration-and-adaptation-read.md](tasks/drift-calibration-and-adaptation-read.md) | Only for public safety records on a named product |
| B1 Performance review and miss owners | By our rules, what failed, who owns each miss, what action do we take, and when do we recheck? | [tasks/performance-review-and-miss-owners.md](tasks/performance-review-and-miss-owners.md) | Only for `verify.build_record` |

Routing hints: "validation completeness", "validation score", "MLOps check", "promotion score", "which models lack a run id", "model inventory audit" is A1. "Drift", "calibration", "data shift", "input change", "monitoring report", "Personalisation Adaptation Monitoring", "is the engine following its rules" is A2. "Drift response", "validation miss", "personalisation miss owner", "pass rule", "who owns this", "retrain or roll back" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the model register (CSV: model_id, version, in_production, intended_use, decision_named, decision_excluded, test_set_id, test_set_independent, metric_prenamed, metric_named_on, run_date, run_id, approver, subgroup_reported, absent_population, watch_signal, watch_threshold, watch_action, watch_owner, watch_fired_on, action_taken), the pass rule (JSON: required elements, date written), the prediction log (CSV: period, id, p, y where known, inputs, groups), the reference period, the thresholds file (date written), the decision log and rule table, the read date, named products, and the owners, actions and recheck dates the person sets. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/drift_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the calls list and the one-line offer of the full version come before the record block, never after it and never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/`, live connector output and the person's own material, never from memory. Every rule carries its row id. In answers, every fact names its source and date in plain words with the row id after it ("FDA AI-enabled device software functions draft guidance, January 2025 (DA-44)", "FUJIFILM Synapse PACS recall, 22 July 2026, library, retrieved 19 October 2026"); never a row id alone (`references/gap-rules.md`, "How to cite"). Row prefixes used in this skill: DA (data and AI research: DA-02, DA-10 to DA-16, DA-29, DA-33, DA-35 to DA-46, DA-48, DA-54, DA-55, DA-63, DA-65 to DA-67, DA-87 to DA-93, DA-113 to DA-120), US, EU and UK (AI/ML device regulation research: US-12, US-13, US-19, US-21, US-22, US-36 to US-39, EU-05, EU-19, EU-25, EU-32 to EU-36, UK-10) and TM (TM79 to TM93: adaptive interventions, process evaluation). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: Sahiner 2023 DA-87 to DA-90, DOI 10.1259/bjr.20220878; Davis 2017 DA-91, DA-92, DOI 10.1093/jamia/ocx030; Finlayson 2021 DA-93 [WF], DOI 10.1056/NEJMc2104626; Rajkomar 2018 DA-113 to DA-115, DOI 10.7326/M18-1990; Paulus and Kent 2020 DA-116 to DA-120, DOI 10.1038/s41746-020-0304-9; Nahum-Shani 2018 TM79 to TM90, DOI 10.1007/s12160-016-9830-8; Moore 2015 TM91 to TM93, DOI 10.1136/bmj.h1258. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id. Rows marked [WF] were read through a summarizing fetch (DA-93, IM-04): say so when a fact rests on one. Cite only the rows for the market in the request (EU AI Act rows for the EU; FDA rows for the US); where a rule from one market is used as context for another, say so. A fact not sourced is `[GAP]` (`references/gap-rules.md`).

**Draft versus final.** The FDA AI-enabled device software functions guidance, including its postmarket performance monitoring plan, is a draft (7 January 2025, still draft on 19 October 2026; DA-35, DA-44, US-21); the FDA request for comment FDA-2025-N-4203 is not guidance (US-39): never "FDA requires". The FDA PCCP guidance is final (18 August 2025, US-01). EU AI Act Articles 12, 15 and 72 apply from 2 August 2028 for AI in Annex I devices, as amended by Regulation (EU) 2026/1744 (DA-67, EU-19); MDCG 2025-6 still uses the pre-omnibus date (EU-32).

**No thresholds from the model.** No source in this skill sets a drift, calibration, AUROC, missing-data, fairness or engagement threshold, a standardized mean difference cut-off or a review cadence (DATA_AND_AI.md, "Not sourced"). Never supply one. The script raises a flag only on the person's thresholds file; without it, values and changes are reported and no flag is raised. **Fairness:** when the person watches calibration and equal error rates across groups with different outcome rates, state the impossibility row (Paulus and Kent 2020, DOI 10.1038/s41746-020-0304-9, DA-119).

**Public records.** Describe a recall, alert or MAUDE count only by what the record states; never judge its relevance to the person's product; never attribute MAUDE counts to one manufacturer; an empty result is not evidence of safety. The library's change log needs a watch, and no `watch_*` tool is called: compare dated reruns instead.

**People judge.** Pass rules, thresholds, the reference period, the read date, the cadence, owners, actions (retrain, recalibrate, roll back, stop the decision, keep running), replacement versions, stop durations, whether an incomplete model may influence a decision, and recheck dates are the person's. The model reads, computes with `scripts/drift_check.py`, labels any proposal "proposed", and never applies a proposal until the person confirms. A failed element is a fact against the person's rule, never a verdict on the model. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. Never supply a date, data cut, threshold or status the person did not give; write "not given" and ask.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Verdicts, actions, reportability, change control and any wording for a regulator, customer or clinicians stop for the owner the person names. A refusal still offers a facts-only draft labeled "draft for the owner", with no recommendation. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every library fact is "as of" its retrieval date; every threshold and rule carries the date the person wrote it; a recheck date earlier than the read date is stated as a fact, never as urgency. Sequence the responding work by dependency.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| Writing the intended use, validation plan, rule specification, validation record, promotion rule or drift watch | `clinical-ml-model-development-and-validation` (this pack) |
| Responsible AI governance evidence and release scoring | `responsible-ai-compliance-monitoring` (this pack) |
| Input data quality checks | `data-quality-monitoring` (this pack) |
| Release pipeline and platform performance | `software-quality-and-delivery-monitoring` (this pack) |
| Security incidents | `security-and-privacy-operations-monitoring` (this pack) |
| Device status, PCCP, AI-enabled device change control | `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control |
| AI-enabled device readiness and post-authorization tracking | `dh-regulatory-and-quality` ai-ml-readiness-monitoring |
| Complaints, events, reportability, CAPA | `dh-regulatory-and-quality` audit-capa-and-complaints |
| Therapeutic safety and efficacy signals, engagement and retention against the mechanism | `dh-clinical-development` mechanism-validation-monitoring |
| Use errors and usability | `dh-patient-and-user-experience` usability-monitoring |

Every route names the pack and the skill, never the pack alone. This skill reads, computes and records; it calls the routed skills, never repeats them.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/monitoring-rules.md` source status, what a complete record holds, why watch after release, kinds of drift, what the script computes, subgroups and fairness, personalization engines in use, responding to a fired watch, public safety records, with rows. Needed for every task.
- `references/DATA_AND_AI.md`, `references/AI_ML_REGULATION.md` and `references/THERAPEUTIC_MECHANISM_AND_TRANSLATION.md` the shared research files (copied unchanged) that every rule cites.
- `references/tools.md` every library call used here, from saved live outputs, with pitfalls and the steps that need a live check.
- `references/gap-rules.md` how to word a gap and how to cite. `references/governance.md` stop rules, routing and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/monitoring-review-illustrative.md` a worked A1, A2 and B1 run on illustrative logs with the script outputs; `examples/sample-data/` the illustrative files; `examples/live/` saved library outputs (19 October 2026).
- `scripts/drift_check.py` checks a model register against the person's pass rule (`records`), computes performance, calibration and input drift by period with flags only on the person's thresholds (`drift`), reads a personalization decision log against its rule table (`adaptation`), and counts a short answer against the cap (`words`).
