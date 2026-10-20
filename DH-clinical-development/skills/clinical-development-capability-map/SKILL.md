---
name: clinical-development-capability-map
description: >
  The map of the VITAL Clinical Development pack for digital health products: clinical
  product development and clinical validation. Use it when
  someone asks "what can the clinical development pack do", "which skill do I need",
  or names a topic without naming a skill:
  stage gate, mechanism of action, engagement mechanics, safety by design, dropout,
  handoffs, evidence-to-feature rules, fidelity, protocol, endpoint, decentralized trial,
  literature review, evidence table, real-world evidence, evidence summary. It routes to
  one competency skill, sorts requests between packs and never does the work, grades a
  study or says evidence proves a product works. Not for design records or device status (dh-regulatory-and-quality
  regulatory-and-quality-capability-map), payer routes or economic models
  (dh-access-and-value access-and-value-capability-map), marketing claims (dh-go-to-market
  go-to-market-capability-map), usability (dh-patient-and-user-experience
  patient-and-user-experience-capability-map) or drug trials.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to use the VITAL
  Digital Health Library connector (mcp.vital.expert), mainly regulatory-dh, the
  literature suite and Verify, for named products and published evidence.
metadata:
  name: "clinical-development-capability-map"
  pack: "dh-clinical-development"
  framework_code: "DH-01.01; DH-01.02"
  register_code: "CF-12.01.01; CF-12.01.02"
  framework_path: "DH-01 > DH-01.01 Clinical Product Development; DH-01 > DH-01.02 Clinical Validation & Evidence"
  version: "0.1.0-draft"
  replaces: "clinical-product-capability-map; clinical-validation-capability-map; DH-01.01 Clinical Product Development; DH-01.01.1 Product Development; DH-01.01.2 Therapeutic Design; DH-01.01.3 Cross-Functional Integration; DH-01.01.4 Clinical Science Translation; dh-01-01-download-expert; dh-01-01-download-one-expert; dh-01-01-find-experts; DH-01.02 Clinical Validation & Evidence; DH-01.02.1 Clinical Study Design; DH-01.02.2 Evidence Communication; DH-01.02.3 Clinical Operations; DH-01.02.4 Digital Evidence Generation; dh-01-02-download-expert; dh-01-02-download-one-expert; dh-01-02-find-experts"
  replaces_packs: "dh-clinical-product-development; dh-clinical-validation"
  folds:
    - "DH-01.06.2 Safety & Efficacy (CF-12.01.06.2), heading menu and its two competencies DH-01.06.2.1 and DH-01.06.2.2, folded 20 October 2026"
    - "DH-01.06.3 Engagement Mechanics (CF-12.01.06.3), heading menu and its two competencies DH-01.06.3.1 and DH-01.06.3.2, folded 20 October 2026"
---

# Clinical Development: capability map

Framework position: two cores of the VITAL Digital Health capability framework, **DH-01.01 Clinical Product Development** and **DH-01.02 Clinical Validation & Evidence**, merged into one pack on 20 October 2026. This skill replaces the two old maps (`clinical-product-capability-map` and `clinical-validation-capability-map`), the old core menus, their eight heading menus and the six expert shims. It also routes two headings folded in from DH-01.06 Digital Therapeutic Design: DH-01.06.2 Safety & Efficacy and DH-01.06.3 Engagement Mechanics (no new skills; see "Folded DH-01.06 headings"). It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the product or evidence question itself, call a connector, or state any regulation, guidance, framework element, register fact, study result, reporting checklist item or certainty rating. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-clinical-development`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from measures, criteria and thresholds the person sets; it never sets its own pass rule and never scores a team.

**DH-01.01 Clinical Product Development**

- **DH-01.01.1 Product Development**
  - `clinical-product-lifecycle-and-stage-gates` (DH-01.01.1.1). Run the lifecycle of a clinical digital health product (DTx, DiGA, SaMD): name the stage and what it owes, define the next increment and what each gate needs, and write the stage gate record against the team's criteria.
  - `lifecycle-quality-monitoring` (DH-01.01.1.2). Watch the health of the lifecycle against measures the team sets: define a healthy stage move, read the gate log per stage (owed items present or missing, days open, accepted with no evidence, next stage started while blocked), list post-market register events as the records state them, and review each miss with its owner, block and reread date.
- **DH-01.01.2 Therapeutic Design**
  - `therapeutic-mechanism-and-intervention-design` (DH-01.01.2.1). Design how a digital therapeutic, DiGA, behavioral app or software therapy is meant to work: the mechanism (user action, change, outcome, for whom, not for whom), each component tied to one link (TIDieR, COM-B functions, adaptive decision rules, permitted variation), engagement mechanics, loops and adherence features tied to a mechanism link, safety by design (risks to health the mechanism and mechanics create, mitigations, labeling elements the special controls name), and the assumptions that would stop the product, with the signal and who stops it.
  - `mechanism-validation-monitoring` (DH-01.01.2.2). Check whether the therapy works the way it was designed: what counts as evidence each mechanism link happened, one study or live cohort checked link by link against thresholds set in advance, usage and dropout read against the person's definitions (DiGAV § 23c for a DiGA), complaints, events, use errors and efficacy drift read against thresholds set before launch, and a missed link or crossed signal handled with the owner the team names.
- **DH-01.01.3 Cross-Functional Integration**
  - `cross-functional-product-integration` (DH-01.01.3.1). Map the handoffs between clinical science, software, quality, regulatory, operations and implementation: what moves from whom to whom, which decision waits on it, who attends the design review, which dependencies are open with a late path, and a record of decisions that needed more than one function.
  - `integration-and-handoff-monitoring` (DH-01.01.3.2). Check how those handoffs are going: write down what counts as received before scoring, score every handoff due in a period as received, late, open or not measurable with critical ones kept apart, and for each one that did not arrive name the owner who owes it, the blocked decision and the date to look again.
- **DH-01.01.4 Clinical Science Translation**
  - `evidence-to-intervention-translation` (DH-01.01.4.1). Turn clinical evidence into what the product does and says: map each product claim to the passage that supports it or mark it [GAP], write the intervention as a buildable specification (program theory, TIDieR items, behavior change functions, decision rules with tailoring variables and missing-data behavior, dose), and write the translation limits.
  - `translation-fidelity-monitoring` (DH-01.01.4.2). Check that the product still says and does what its evidence supports, release after release: fidelity rules, shipped claims and decision rules sampled with every differing word quoted, delivered dose against the regimen, and each failure routed to the owner the person names with the version that must not ship it.

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
| Lifecycle stage, phase gates, stage-gate process, MVP or release increment, what a design review or DiGA application needs, writing up a gate decision, how a named product moved through FDA | `clinical-product-lifecycle-and-stage-gates` | Running the stages and gates |
| "Are our gates healthy", stuck stages, days open, skipped gates, open gate items, a recall or post-market change against a stage | `lifecycle-quality-monitoring` | Checking stage health against the person's measures |
| Mechanism of action, program theory, logic model, behavior change design, intervention components, assumptions to test | `therapeutic-mechanism-and-intervention-design` | Designing what the therapy does and why |
| Engagement mechanics, engagement loops, streaks, rewards, reminders, adherence features, gamification, "is this a dark pattern", safety by design, risks to health from the design, warnings and labeling elements | `therapeutic-mechanism-and-intervention-design` | Folded DH-01.06.3.1 and DH-01.06.2.1: mechanics and safety are designed against the mechanism |
| "Does our mechanism still hold", checking assumptions against new evidence or product data | `mechanism-validation-monitoring` | Checking the mechanism over time |
| Usage, dropout, retention, DiGA usage reporting, complaints, adverse events, use errors, efficacy drift against the team's thresholds | `mechanism-validation-monitoring` | Folded DH-01.06.3.2 and DH-01.06.2.2: reads after release against the person's definitions and thresholds |
| Handoffs between clinical, engineering, regulatory, quality and commercial, open dependencies, joint decisions | `cross-functional-product-integration` | Coordinating the functions around one product |
| "Are our handoffs working", misalignment, handoff delays against the person's measures | `integration-and-handoff-monitoring` | Checking integration over time |
| Turning guidelines or trial evidence into product rules or content, what a feature may claim, translation limits | `evidence-to-intervention-translation` | Linking evidence to the intervention |
| Fidelity, dose, adherence to the intended intervention, drift from the protocol version, permitted variation | `translation-fidelity-monitoring` | Checking delivery against intent |
| Study design, protocol, estimand, endpoints, COA or PRO choice, digital endpoint choice, sample size, SAP | `study-protocol-and-endpoint-design` | Designing the study |
| "Is our protocol robust", protocol review against reporting checklists, design gaps | `study-design-quality-monitoring` | Checking the design against the person's criteria |
| Evidence summary for clinicians or partners, publication plan, manuscript, evidence section of a regulatory file | `evidence-translation-and-communication` | Turning evidence into a sourced message |
| "Do our evidence summaries still hold", message drift, reception of evidence communications | `evidence-communication-monitoring` | Checking evidence communications over time |
| Decentralized or hybrid trial setup, eConsent, remote visits, remote data capture, trial data integrity | `decentralized-trial-operations` | Running the trial |
| Enrollment, retention in a trial, data completeness, protocol deviations, trial KPIs | `trial-operations-monitoring` | Checking trial operations |
| Literature search, systematic or rapid review, evidence table, grading, citations, retraction check, RWD source, digital endpoint capture | `literature-and-real-world-evidence-review` | Building the evidence base |
| "Is our evidence base still current", new studies or retractions since the review, real-world signals | `evidence-quality-and-signal-monitoring` | Watching the evidence base against the person's pass rule |

Tie-breakers:

1. Mechanism before increment: if the person cannot say what the product is meant to change and how, start with `therapeutic-mechanism-and-intervention-design` before planning gates.
2. Design before operations: if no protocol exists yet, start with `study-protocol-and-endpoint-design` before `decentralized-trial-operations`.
3. Design and execution come before monitoring. If nothing has been staged, designed, coordinated, translated, run or reviewed yet, the monitoring skill has nothing to check; send the person to its partner first.
4. A gate needs evidence; the evidence is built in the validation half of this pack. Literature reviews go to `literature-and-real-world-evidence-review`, study protocols to `study-protocol-and-endpoint-design`. The product skills call them, never repeat them. Any literature review, from any pack, goes to `literature-and-real-world-evidence-review`.
5. Two kinds of dropout. Dropout from a trial is `trial-operations-monitoring`; dropout or usage of a released product is `mechanism-validation-monitoring`.
6. Two kinds of evidence-to-words. What the product itself does and may claim is `evidence-to-intervention-translation`; a summary of the evidence written for clinicians, regulators or partners is `evidence-translation-and-communication`.
7. The record of a gate in the quality system (design review, design and development file, risk file) is `dh-regulatory-and-quality` design-controls-and-risk-management; change control is `dh-regulatory-and-quality` document-and-change-control. This pack names the gate and its evidence and routes the record.
8. Whether a product is a device is `dh-regulatory-and-quality` regulatory-pathway-and-classification; whether a change needs a submission is `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control; submission content is `dh-regulatory-and-quality` regulatory-submission-and-dossier. Regulation facts in this pack are context for design only.
9. A study whose main question is cost, resource use or value for a payer is `dh-access-and-value` real-world-outcomes-research; a study whose main question is clinical performance, efficacy or safety is here.
10. Certainty ratings, thresholds and conclusions belong to the person or the HTA body. The pack lays out the evidence; it never says the evidence proves the product works.
11. If the request is vague ("help with our product" or "help with evidence"), ask one question: is this about where the product is in its lifecycle, what the therapy does, how the teams hand work to each other, how evidence becomes product rules, designing or running a study, reviewing what is published, or communicating the evidence? Then route.

## Folded DH-01.06 headings

On 20 October 2026 two headings of DH-01.06 Digital Therapeutic Design were folded into this pack without adding skills. When a person names an old heading or an old task (old names quoted as they were, in their original spelling), route as follows.

| Old heading or task (code) | Go to | Task there |
|---|---|---|
| "DH-01.06.2 Safety & Efficacy" (heading menu) | ask which: design or monitoring, then route below | none |
| "Mechanism-of-Action Specification" (DH-01.06.2.1.1) | `therapeutic-mechanism-and-intervention-design` | A1 Mechanism statement |
| "Safety-by-Design Implementation" (DH-01.06.2.1.2) | `therapeutic-mechanism-and-intervention-design` | A4 Safety by design |
| "Efficacy Evidence Linkage" (DH-01.06.2.1.3) | `evidence-to-intervention-translation` | A1 Evidence claim map |
| "Therapeutic Safety & Efficacy Monitoring" (DH-01.06.2.2.1) and "therapeutic safety pass rule" (DH-01.06.2.2.2) | `mechanism-validation-monitoring` | A4 Safety and efficacy signal read |
| "therapeutic safety miss owner" (DH-01.06.2.2.3) | `mechanism-validation-monitoring` | B1 Mechanism miss review |
| "DH-01.06.3 Engagement Mechanics" (heading menu) | ask which: design or monitoring, then route below | none |
| "Behavioural Mechanics Design" (DH-01.06.3.1.1), "Engagement Loop Construction" (DH-01.06.3.1.2), "Adherence Optimisation" (DH-01.06.3.1.3) | `therapeutic-mechanism-and-intervention-design` | A3 Engagement mechanics design |
| "Engagement & Retention Monitoring" (DH-01.06.3.2.1) and "engagement retention pass rule" (DH-01.06.3.2.2) | `mechanism-validation-monitoring` | A3 Engagement and retention read |
| "engagement retention miss owner" (DH-01.06.3.2.3) | `mechanism-validation-monitoring` | B1 Mechanism miss review |

DH-01.06.1 Personalization Engine and DH-01.06.4 DTx Architecture stay in the old pack `dh-digital-therapeutic-design` (see "Out of scope"). Whether an event is reportable is never this pack's call: `dh-regulatory-and-quality` audit-capa-and-complaints.

## Catalogue jobs

The VITAL Digital Health Library lists one-call jobs (`list_jobs`, retrieved 19 October 2026 for the validation half and 20 October 2026 for the product half). A job is the buyer's one-call option; `start_job` returns its steps and inputs and runs nothing, so the competency skill's task steps remain the method. This map names the job; it does not start it.

| Request | Catalogue job | Skill |
|---|---|---|
| Graded studies for a product's claims, with retractions flagged | `evidence-table` (available) | `literature-and-real-world-evidence-review`; `evidence-quality-and-signal-monitoring` for a rerun against the person's pass rule |
| Evidence table to support a value or payer dossier | `evidence-table` (available) | `literature-and-real-world-evidence-review`, then `dh-access-and-value` value-narrative-and-dossier |
| Payer value dossier outline | `value-dossier` (design partners, not startable) | `dh-access-and-value` value-narrative-and-dossier; the evidence base comes from `literature-and-real-world-evidence-review` |

No other job in the library belongs to this pack. `find_job {query: "product lifecycle stage gate"}` returned no match on 20 October 2026. Product development, study design, trial operations and evidence communication have no catalogue job; the competency skill is the only route. Nearby jobs of other packs are named only when routing: `pathway-assessment` and `predicate-chain` (`dh-regulatory-and-quality` regulatory-pathway-and-classification) and `post-market-watch` (`dh-regulatory-and-quality` regulatory-pathway-monitoring).

## Out of scope for this pack

Say so in one line and route where a home exists, naming the pack and the skill (or, for an old pack, the heading), never the pack alone. Do not do the work from this map.

- Drug or biologic clinical development: not covered by the Digital Health packs.
- Design controls, risk management files, design history, document and change control, complaints and CAPA: `dh-regulatory-and-quality` (start with `regulatory-and-quality-capability-map`; for complaint records, audit-capa-and-complaints).
- Device status, classification, pathway, submissions, Pre-Sub wording, PCCP, human-factors validation: `dh-regulatory-and-quality` (start with `regulatory-and-quality-capability-map`; for the dossier, regulatory-submission-and-dossier). The evidence behind a submission is built here; the submission is there.
- Economic models, budget impact, price anchors and payer value dossiers: `dh-access-and-value` economic-model-development and value-narrative-and-dossier (start with `access-and-value-capability-map`).
- Payer routes, coverage schemes, DiGA listing as reimbursement, codes, prices, HTA submission mechanics and contracts: `dh-access-and-value` coverage-pathway-and-access-strategy and payer-engagement-and-hta-submission.
- Marketing and promotional claims: `dh-go-to-market` pricing-and-value-message-monitoring (start with `go-to-market-capability-map`). Clearance stops for the person's regulatory or legal owner.
- Usability research, workflow design, accessibility, patient co-design and advocacy partners around a study: `dh-patient-and-user-experience` (start with `patient-and-user-experience-capability-map`).
- Algorithms and personalization engines: `dh-digital-therapeutic-design` (old pack, not yet rebuilt), heading DH-01.06.1 Personalization Engine. Platform architecture: `dh-digital-therapeutic-design`, heading DH-01.06.4 DTx Architecture.
- Portfolio governance and prioritization across products: `dh-cross-functional-leadership` (old pack), heading DH-01.03.3 Governance & Portfolio. Leadership across teams: heading DH-01.03.4 Matrix Leadership.
- Building or validating a clinical ML model's performance: `dh-data-science`, heading DH-01.04.3 Model Development & Validation. The clinical study that tests the model in use is here.
- Statistical analysis run on the person's patient-level data: `dh-advanced-analytics`, heading DH-05.01.1 Statistical Modeling & Inference. The analysis plan is here.

## Routing examples

- "We have a prototype of an ADHD game therapy. What stage are we in and what do we need before feasibility?" Route to `clinical-product-lifecycle-and-stage-gates`. It maps the stage and what it owes; the person decides the stage and the criteria.
- "Which behavior change techniques should our app use for medication adherence, and why?" Route to `therapeutic-mechanism-and-intervention-design`. The mechanism stays a hypothesis until tested.
- "Turn the national insomnia guideline into rules for our CBT-I app." Route to `literature-and-real-world-evidence-review` for the evidence itself if it has not been reviewed, then `evidence-to-intervention-translation` for the rules.
- "Our DiGA's three-week dropout is climbing and we had two complaints about a reward glitch. Is that a safety problem?" Route to `mechanism-validation-monitoring` (A3 for dropout, A4 for the complaints against the person's thresholds); reportability goes to `dh-regulatory-and-quality` audit-capa-and-complaints.
- "Run Behavioural Mechanics Design for our streaks feature." Route to `therapeutic-mechanism-and-intervention-design` A3; each mechanic is tied to a mechanism link and never called safe or effective.
- "We need a pivotal study for our CBT-I app. Which endpoints and what design?" Route to `study-protocol-and-endpoint-design`. It lays out options for the person's clinical owner; it does not pick one.
- "Find and grade everything published on remote monitoring for heart failure and give me an evidence table." Route to `literature-and-real-world-evidence-review`; catalogue job `evidence-table`. The certainty ratings it drafts stay the person's call.
- "Our hybrid trial is losing participants at week 8. What now?" Route to `trial-operations-monitoring`, working from the retention measure the person set.
- "Our health economist needs a literature review for model inputs." Route to `literature-and-real-world-evidence-review`; the model itself is `dh-access-and-value` economic-model-development.

## Related packs

- **Regulatory and quality** (`dh-regulatory-and-quality`): design-controls-and-risk-management, document-and-change-control, audit-capa-and-complaints, regulatory-pathway-and-classification, ai-ml-device-pathway-and-change-control, regulatory-submission-and-dossier, and their monitoring skills. Start with `regulatory-and-quality-capability-map`.
- **Access and value** (`dh-access-and-value`): economic models, outcomes research for value, value narratives and dossiers, coverage, coding, pricing, payer and HTA engagement, outcomes-based contracts. Start with `access-and-value-capability-map`. Its literature reviews come back here.
- **Go to market** (`dh-go-to-market`): marketing claims and value messages used in promotion. Start with `go-to-market-capability-map`; for claims, pricing-and-value-message-monitoring.
- **Patient and user experience** (`dh-patient-and-user-experience`): patient-and-clinician-user-research, clinical-workflow-ux-design, usability-monitoring, patient co-design. Start with `patient-and-user-experience-capability-map`.
- Old packs, not yet rebuilt, named by heading: `dh-digital-therapeutic-design` DH-01.06.1 Personalization Engine and DH-01.06.4 DTx Architecture (DH-01.06.2 and DH-01.06.3 folded here); `dh-cross-functional-leadership` DH-01.03.3 Governance & Portfolio and DH-01.03.4 Matrix Leadership; `dh-data-science` (model development and validation); `dh-advanced-analytics` (statistical analysis). Use each pack's own menu.

## Downloading a clinical development expert

If the person wants a clinical product or clinical evidence expert role on their own assistant, route to the shared skill `digital-health-expert`. It replaces the six old expert shims of the two old packs.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a stage, a gate criterion, a mechanism, an endpoint, a design, a measure, a certainty rating, a pass rule, a conclusion or an owner, even as an example. A mechanism is a hypothesis until tested. A review is never more than its sources.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- Catalogue job ids and statuses follow `list_jobs` as retrieved 19 and 20 October 2026.
- `evals/evals.json` routing tests: one per old half, the folded DH-01.06 routing, one routing across the two halves, one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
