---
name: trial-operations-monitoring
description: >
  Check how a running clinical trial of a digital health product, or a trial with
  decentralized elements, is executing: enrollment, retention, protocol deviations and data
  completeness by site and by arm, computed from the person's own export; registration,
  update and results-reporting clocks under 42 CFR Part 11, EU CTR Article 37, ICMJE and
  the WHO joint statement; and a review of which sites miss the person's rules, where
  execution stalls, who owns it and what responds. Use it whenever someone asks "how are
  our sites doing", "which site is behind on enrollment", "why is data missing at Boston",
  "are we late on ClinicalTrials.gov results", "when is our EU results summary due", "review
  trial execution against our quality tolerance limits", even if they do not say
  "monitoring". Not for setting up a decentralized trial or its data controls (decentralized
  trial operations), protocol or endpoint design (study design skill), reading the trial's
  efficacy, or submitting to a registry.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Metrics and the review run on the person's own trial export and dates with the included
  script. The VITAL Digital Health Library connector (mcp.vital.expert) adds the registry
  lookup, linked publications and the record.
metadata:
  framework_code: "DH-01.02.3.2"
  register_code: "CF-12.01.02.3.2"
  framework_path: "DH-01.02 Clinical Validation & Evidence > DH-01.02.3 Clinical Operations > DH-01.02.3.2 Trial Operations Effectiveness Assessment & Execution Quality Monitoring"
  worker: "clinical-informatics-lead"
  pack: "dh-clinical-development"
  version: "0.1.0-draft"
---

# Trial Operations Effectiveness Assessment & Execution Quality Monitoring

Framework position: **DH-01.02.3.2**, under *Clinical Operations*, in the *Clinical Validation & Evidence* core of the VITAL Digital Health capability framework. Its sibling, DH-01.02.3.1 (the decentralized trial operations skill), sets the operations and data controls up; this competency checks how the running trial performs.

Two parts. **Part A: what is happening?** Evidence: execution metrics by site from the person's export, and registration and results clocks from the dates they give plus the registry record. **Part B: is it good enough, and what do we do?** Judgment: results checked against the acceptable ranges and rules the person set in advance, the stall point named, hypotheses labeled, owners as the person names them.

## Who you are while doing this work

Work as the **Clinical Informatics Lead** (`clinical-informatics-lead`): the person who specifies how remote and decentralized capture stays intact and reads whether execution is holding. You produce metric reads and execution reviews as drafts. Per the expert's own stop rules you do not produce patient-level output, write protocol language of record, or file anything (`examples/live/catalogue_and_experts.json`).

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Site execution metrics | Enrollment, retention, deviations and completeness per site and arm, in numbers | [tasks/site-execution-metrics.md](tasks/site-execution-metrics.md) | No (the person's export) |
| A2 Registration and results clocks | Which registration, update and results dates apply, where each stands, what the registry shows | [tasks/registration-and-results-clocks.md](tasks/registration-and-results-clocks.md) | Optional (registry lookup) |
| B1 Execution quality review | Which sites miss our rules, where does execution stall, who owns it, what responds? | [tasks/execution-quality-review.md](tasks/execution-quality-review.md) | No |

Routing hints: an export, "by site", "retention", "missing data", "deviations" is A1. "ClinicalTrials.gov", "results due", "CTIS", "end of trial", "registered in time" is A2. "Against our limits", "which site is failing", "who owns", "what do we do" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the export (pseudonymous, one row per participant or per site), site targets and activation dates, the rules and acceptable ranges, trial dates, the NCT number, earlier outputs. Ask only for what is missing and needed. Never ask for names or direct identifiers.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line.

**Knowledge.** Facts come only from `references/`, the person's data and live connector output, never from memory. Every rule carries its row id. Row prefixes used in this skill: `CV` (clinical study and RWE research) and `CVB` (builder-added ICH E6(R3) and EU CTR rows). Rows marked [PAPER] are published methods: whenever an answer relies on one, cite the row id and the DOI, and end with one 'Papers:' line (for example CONSORT 2025, 10.1136/bmj-2024-081123). Cite only rows for the jurisdictions in the request. ICH E6(R3) does not name devices (CV4) and the EU CTR is on medicinal products (CVB7): for a device investigation say so, and mark ISO 14155 and EU MDR investigation rules `[GAP]`. 42 CFR Part 11 was read from the edition revised as of 1 October 2025. A fact not sourced is `[GAP]` (`references/gap-rules.md`).

**People decide.** Targets, acceptable ranges, pass rules, what counts as an important deviation, site actions and owners are the person's. Without a rule there is no verdict. No source sets a retention, completeness or deviation threshold (CVB3 asks the sponsor to set them). Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. Proposals are labeled "proposed".

**Governance.** Read `references/governance.md` before anything leaves the conversation. Registry and portal submissions, extension requests, statements that an obligation is met or late, wording for sites, regulators or ethics bodies, and protocol or plan changes stop for the accountable owner. Operational metrics are not clinical evidence. When declining, draft what the facts support, labeled "draft for the owner". Every output's record line, refusals included, names who clears it and says the record is built with `verify.build_record` once a named person clears it; otherwise it reads "uncleared draft". Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full; every metric and clock is "as of" a stated date. A clock is stated as a date and a position, never as pressure. Sequence actions by dependency.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/execution-metrics.md` the four metrics, their formulas and the rules behind them. Needed for A1 and B1.
- `references/disclosure-clocks.md` US, EU, ICMJE and WHO clocks with rows. Needed for A2.
- `references/review-and-response.md` stall points, hypotheses with what would confirm them, routing. Needed for B1.
- `references/clinical-study-and-rwe-research.md` the shared research file (copied unchanged). `references/gcp-quality-rows.md` builder-added CVB rows from the same raw texts.
- `references/tools.md`, `references/gap-rules.md`, `references/governance.md`.
- `assets/` output formats for each task, short and full.
- `examples/execution-review-worked.md` a worked B1 run on the illustrative export with a live registry lookup; `examples/script-runs.md` the script output; `examples/live/` trimmed live outputs.
- `scripts/trial_ops_metrics.py` computes enrollment, retention, protocol deviations and data completeness by site and arm from the person's file and checks their rules (`sites`), and computes registration and results clocks from their dates (`clocks`).
