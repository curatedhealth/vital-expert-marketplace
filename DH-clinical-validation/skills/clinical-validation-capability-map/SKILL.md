---
name: clinical-validation-capability-map
description: >
  The map of the VITAL Clinical Validation & Evidence pack for digital health products
  (SaMD, AI/ML devices, DTx, DiGA-type apps). Use it whenever someone asks "what can the clinical evidence pack do", "which evidence skill do I need", "where
  do I start with our clinical study", or names an evidence topic (protocol, endpoint,
  estimand, decentralized trial, literature review, evidence table, real-world
  evidence, digital endpoint, evidence summary) without
  naming a skill. It routes the person to one competency skill and its catalogue job,
  and sorts requests between packs. Not for doing the evidence work itself: it never
  grades a study, rates certainty, picks an endpoint or says evidence proves a product
  works. Not for drug or biologic trials, device status or submissions
  (dh-regulatory-strategy), payer routes (dh-market-access), economic models
  (dh-health-economics) or marketing claims (dh-commercial).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to use the VITAL
  Digital Health Library connector (mcp.vital.expert), mainly the literature suite and
  Verify, for their evidence tasks.
metadata:
  framework_code: "DH-01.02"
  register_code: "CF-12.01.02"
  framework_path: "DH-01 > DH-01.02 Clinical Validation & Evidence"
  pack: "dh-clinical-validation"
  version: "0.1.0-draft"
  replaces: "DH-01.02 Clinical Validation & Evidence; DH-01.02.1 Clinical Study Design; DH-01.02.2 Evidence Communication; DH-01.02.3 Clinical Operations; DH-01.02.4 Digital Evidence Generation; dh-01-02-download-expert; dh-01-02-download-one-expert; dh-01-02-find-experts"
---

# Clinical Validation & Evidence: capability map

Framework position: **DH-01.02 Clinical Validation & Evidence**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu, its four heading menus and the three expert shims. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the evidence question itself, call a connector, or state any study result, guideline rule, reporting checklist item or certainty rating. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-clinical-validation`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria and thresholds the person sets; it never sets its own pass rule.

**DH-01.02 Clinical Validation & Evidence**

- **DH-01.02.1 Clinical Study Design**
  - `study-protocol-and-endpoint-design` (DH-01.02.1.1). What question does the study answer, which design, estimand and endpoints fit, how are clinical outcome assessments and digital endpoints chosen, and what goes into the protocol and statistical analysis plan?
  - `study-design-quality-monitoring` (DH-01.02.1.2). Against the criteria the person sets, how robust is the protocol, what do the reporting checklists show is missing, and who owns each gap?
- **DH-01.02.2 Evidence Communication**
  - `evidence-translation-and-communication` (DH-01.02.2.1). How is the clinical evidence summarized for clinicians, regulators, publications and partners, with every statement traced to its source?
  - `evidence-communication-monitoring` (DH-01.02.2.2). Against the measures the person set, do the evidence summaries still match the sources, and how are they received?
- **DH-01.02.3 Clinical Operations**
  - `decentralized-trial-operations` (DH-01.02.3.1). How is a decentralized or hybrid trial set up, how is remote data captured, and how is trial data integrity kept?
  - `trial-operations-monitoring` (DH-01.02.3.2). Against the operational measures the person set, how is the trial running (enrollment, retention, data completeness, deviations), and who owns a miss?
- **DH-01.02.4 Digital Evidence Generation**
  - `literature-and-real-world-evidence-review` (DH-01.02.4.1). How is the literature searched, deduplicated, screened, classified, graded and tabled, how are trials linked and retractions checked, and how are real-world data and digital endpoints captured as evidence? This is the one home of the literature review method for every Digital Health pack.
  - `evidence-quality-and-signal-monitoring` (DH-01.02.4.2). Against the pass rule the person set, is the evidence base still current and sound (new studies, retractions, signals in real-world data), and who owns each miss?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Study design, protocol, estimand, endpoints, COA or PRO choice, digital endpoint choice, sample size, SAP | `study-protocol-and-endpoint-design` | Designing the study |
| "Is our protocol robust", protocol review against reporting checklists, design gaps | `study-design-quality-monitoring` | Checking the design against the person's criteria |
| Evidence summary for clinicians or partners, publication plan, manuscript, evidence section of a regulatory file | `evidence-translation-and-communication` | Turning evidence into a sourced message |
| "Do our evidence summaries still hold", message drift, reception of evidence communications | `evidence-communication-monitoring` | Checking evidence communications over time |
| Decentralized or hybrid trial setup, eConsent, remote visits, remote data capture, trial data integrity | `decentralized-trial-operations` | Running the trial |
| Enrollment, retention, data completeness, protocol deviations, trial KPIs | `trial-operations-monitoring` | Checking trial operations |
| Literature search, systematic or rapid review, evidence table, grading, citations, retraction check, RWD source, digital endpoint capture | `literature-and-real-world-evidence-review` | Building the evidence base |
| "Is our evidence base still current", new studies or retractions since the review, real-world signals | `evidence-quality-and-signal-monitoring` | Watching the evidence base against the person's pass rule |

Tie-breakers:

1. Design before operations: if no protocol exists yet, start with `study-protocol-and-endpoint-design` before `decentralized-trial-operations`.
2. Design and execution come before monitoring. If nothing has been designed, run or reviewed yet, the monitoring skill has nothing to check; send the person to its partner first.
3. Any literature review, from any pack, goes to `literature-and-real-world-evidence-review`. Health economics inputs, value dossiers and evidence summaries point to it rather than repeating the method.
4. A study whose main question is cost, resource use or value for a payer is `real-world-outcomes-research` in `dh-health-economics`; a study whose main question is clinical performance, efficacy or safety is here.
5. Certainty ratings, thresholds and conclusions belong to the person or the HTA body. The pack lays out the evidence; it never says the evidence proves the product works.
6. If the request is vague ("help with evidence"), ask one question: is this about designing a study, running one, reviewing what is already published, or communicating the evidence? Then route.

## Catalogue jobs: which skill and job a request goes to

The VITAL Digital Health Library lists one-call jobs (`list_jobs`, 19 October 2026). A job is the buyer's one-call option; `start_job` returns its steps and inputs and runs nothing, so the competency skill's task steps remain the method. This map names the job; it does not start it.

| Request | Catalogue job | Skill |
|---|---|---|
| Graded studies for a product's claims, with retractions flagged | `evidence-table` (available) | `literature-and-real-world-evidence-review`; `evidence-quality-and-signal-monitoring` for a rerun against the person's pass rule |
| Evidence table to support a value or payer dossier | `evidence-table` (available) | `literature-and-real-world-evidence-review`, then `value-narrative-and-dossier` (`dh-health-economics`) |
| Payer value dossier outline | `value-dossier` (design partners, not startable) | `value-narrative-and-dossier` (`dh-health-economics`); the evidence base comes from `literature-and-real-world-evidence-review` |

No other job in the library belongs to this pack. Study design, trial operations and evidence communication have no catalogue job; the competency skill is the only route.

## Out of scope for this pack

Say so in one line and route where a home exists. Do not do the work from this map.

- Drug or biologic clinical development: not covered by the Digital Health packs.
- Device classification, regulatory status, submissions and human-factors validation: `dh-regulatory-strategy` (start with `regulatory-strategy-capability-map`). The evidence behind a submission is built here; the submission is there.
- Complaint handling and vigilance reporting for a marketed product: `dh-quality` `audit-capa-and-complaints` for the record; the reporting route sits with `dh-regulatory-strategy`.
- Economic models, budget impact, price anchors and payer value dossiers: `dh-health-economics` (start with `health-economics-capability-map`).
- Payer routes, coverage schemes, codes, HTA submission mechanics and contracts: `dh-market-access`.
- Marketing and promotional claims: `dh-commercial` (`pricing-and-value-message-monitoring`). Clearance stops for the person's regulatory or legal owner.
- Building or validating a clinical ML model's performance: `dh-data-science`. The clinical study that tests the model in use is here.
- Statistical analysis run on the person's patient-level data: `dh-advanced-analytics`. The analysis plan is here.

## Routing examples

- "We need a pivotal study for our CBT-I app. Which endpoints and what design?" Route to `study-protocol-and-endpoint-design`. It lays out the design and endpoint options for the person's clinical owner; it does not pick one.
- "Find and grade everything published on remote monitoring for heart failure and give me an evidence table." Route to `literature-and-real-world-evidence-review`; catalogue job `evidence-table`. The certainty ratings it drafts are checked against the papers and stay the person's call.
- "Our hybrid trial is losing participants at week 8. What now?" Route to `trial-operations-monitoring`, working from the retention measure the person set.
- "Write a one-page evidence summary for hospital clinicians." Route to `evidence-translation-and-communication`. If the page will be used to promote the product, the promotional side stops for the person's regulatory or legal owner and `dh-commercial`.
- "Our health economist needs a literature review for model inputs." Route to `literature-and-real-world-evidence-review`; the model itself is `economic-model-development` in `dh-health-economics`.

## Related packs

Send the person to another pack when the question is not clinical evidence:

- **Health Economics** (`dh-health-economics`): economic models, outcomes research for value, value narratives and dossiers. Start with `health-economics-capability-map`. Its literature reviews come back here.
- **Market Access** (`dh-market-access`): anything a payer sets, codes, negotiates or reimburses, and HTA submission mechanics. Skills: `coverage-pathway-and-access-strategy`, `coverage-strategy-and-access-rate-monitoring`, `payer-engagement-and-hta-submission`, `hta-submission-and-payer-engagement-monitoring`, `coding-pricing-and-payer-contracting`, `coding-pricing-and-contract-monitoring`, `outcomes-based-contracting`, `outcomes-contract-monitoring`.
- **Regulatory** (`dh-regulatory-strategy`): device status, intended use, submissions, human-factors validation. Start with `regulatory-strategy-capability-map`; for the dossier, `regulatory-submission-and-dossier`.
- **Commercial** (`dh-commercial`): marketing claims and value messages used in promotion. Start with `commercial-gtm-capability-map`; for claims, `pricing-and-value-message-monitoring`.
- **Patient Engagement** (`dh-patient-engagement`): patient co-design and advocacy partners around a study. Start with `patient-engagement-capability-map`.
- Other Digital Health packs, by pack name: `dh-data-science` (model development and validation), `dh-advanced-analytics` (statistical analysis), `dh-quality` (complaints and CAPA). Use each pack's own map or skill list.

## Downloading the clinical evidence expert

If the person wants a clinical evidence expert role on their own assistant, route to the shared skill `digital-health-expert`. It replaces the three old expert shims of this pack.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes an endpoint, a design, a certainty rating, a pass rule or a conclusion, even as an example. A review is never more than its sources.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- Catalogue job ids and statuses follow `list_jobs` as retrieved 19 October 2026.
- `evals/evals.json` routing tests, including one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
