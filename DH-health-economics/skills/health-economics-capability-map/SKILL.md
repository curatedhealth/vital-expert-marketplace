---
name: health-economics-capability-map
description: >
  The map of the VITAL Health Economics & Value Demonstration pack for digital health
  products (SaMD, DTx, DiGA-type apps). Use it
  whenever someone asks "what can the health economics pack do", "which HEOR skill do I
  need", "where do I start with our value case", or names a value topic (cost-
  effectiveness, budget impact, price anchor, QALY, model validation, outcomes study, value narrative, value dossier, evidence for a reimbursement decision)
  without naming a skill. It routes the person to one competency skill and its catalogue
  job, and sorts requests between packs. Not for doing the economic work itself: it never
  builds a model, sets a threshold, judges a model acceptable or says a product is
  cost-effective. Not for literature review method (dh-clinical-validation), payer
  routes, codes, HTA submission mechanics or contracts (dh-market-access), device status
  (dh-regulatory-strategy) or marketing claims (dh-commercial).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to use the VITAL
  Digital Health Library connector (mcp.vital.expert), mainly the analytics calculators,
  the literature suite and Verify, for their evidence tasks.
metadata:
  framework_code: "DH-01.07"
  register_code: "CF-12.01.07"
  framework_path: "DH-01 > DH-01.07 Health Economics & Value Demonstration"
  pack: "dh-health-economics"
  version: "0.1.0-draft"
  replaces: "DH-01.07 Health Economics & Value Demonstration; DH-01.07.1 Market Access Support; DH-01.07.2 Economic Modeling; DH-01.07.3 Outcomes Research; DH-01.07.4 Value Communication; dh-01-07-download-expert; dh-01-07-download-one-expert; dh-01-07-find-experts"
---

# Health Economics & Value Demonstration: capability map

Framework position: **DH-01.07 Health Economics & Value Demonstration**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu, its four heading menus and the three expert shims. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the economic question itself, call a connector, or state any threshold, model result, price, HTA rule or method requirement. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-health-economics`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria and thresholds the person sets; it never sets its own pass rule.

**DH-01.07 Health Economics & Value Demonstration**

- **DH-01.07.1 Market Access Support**
  - `reimbursement-evidence-support` (DH-01.07.1.1). What evidence and economic case does a reimbursement decision need, which dossier items does it feed, and how ready is that evidence package?
  - `reimbursement-evidence-monitoring` (DH-01.07.1.2). Against the outcome measures the person set, how did the evidence package fare in reimbursement decisions, and who owns each miss?
- **DH-01.07.2 Economic Modeling**
  - `economic-model-development` (DH-01.07.2.1). What is the economic question, which model structure and inputs fit, and what do a cost-effectiveness model, a budget impact model or a launch price anchor return on the person's numbers?
  - `economic-model-validity-monitoring` (DH-01.07.2.2). Against the criteria the person sets, is the model valid and transparent, how sensitive is the result, and what needs repair?
- **DH-01.07.3 Outcomes Research**
  - `real-world-outcomes-research` (DH-01.07.3.1). Which outcomes question matters for value (costs, resource use, patient-reported outcomes, utilities), how is a real-world outcomes study designed and run, and what does it return?
  - `outcomes-evidence-quality-monitoring` (DH-01.07.3.2). Against the criteria the person sets, how rigorous is the outcomes study, and what needs repair?
- **DH-01.07.4 Value Communication**
  - `value-narrative-and-dossier` (DH-01.07.4.1). Who is the value audience, what is the value narrative, and how is the value dossier outlined, with every claim checked against its source?
  - `value-communication-monitoring` (DH-01.07.4.2). Against the reception measures the person set, how is the value narrative received, and where does it need repair?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| What evidence a reimbursement decision needs, dossier items, evidence readiness for a payer or HTA decision | `reimbursement-evidence-support` | Building the evidence and economic case |
| "How did our evidence fare with payers", decision outcomes against the person's measures | `reimbursement-evidence-monitoring` | Checking the evidence case over time |
| Cost-effectiveness model, QALYs, budget impact, launch price ceiling per threshold, model inputs | `economic-model-development` | Building the model on the person's inputs |
| "Is our model valid", model review against reporting standards, sensitivity, model repair | `economic-model-validity-monitoring` | Checking the model against the person's criteria |
| Real-world outcomes study, costs and resource use, PROs or utilities for value | `real-world-outcomes-research` | Generating outcomes evidence for value |
| "Is our outcomes study rigorous", study quality review, evidence repair | `outcomes-evidence-quality-monitoring` | Checking the outcomes study |
| Value narrative, value audience, payer value dossier outline | `value-narrative-and-dossier` | Telling the value story from checked evidence |
| How the value narrative is received, narrative repair | `value-communication-monitoring` | Checking value communication over time |

Tie-breakers:

1. Any literature review goes to `literature-and-real-world-evidence-review` in `dh-clinical-validation`, always. Model inputs, dossiers and outcomes studies point to it rather than repeating the method.
2. The evidence and the economic case for a reimbursement decision are here. Which payer route or scheme, codes, payer prices, HTA submission mechanics and contracts are `dh-market-access`. If a request mixes both, name both and the order.
3. A study whose main question is cost, resource use or value is `real-world-outcomes-research`; a study whose main question is clinical efficacy or safety is `study-protocol-and-endpoint-design` in `dh-clinical-validation`.
4. Design and execution come before monitoring. If no model, study or narrative exists yet, the monitoring skill has nothing to check; send the person to its partner first.
5. A model is never more than its inputs. Thresholds, whether a model is acceptable and whether a product is cost-effective are the person's or the HTA body's decision; the pack never states them.
6. If the request is vague ("help with value"), ask one question: is this about the evidence for a reimbursement decision, an economic model, an outcomes study, or the value story? Then route.

## Catalogue jobs: which skill and job a request goes to

The VITAL Digital Health Library lists one-call jobs (`list_jobs`, 19 October 2026). A job is the buyer's one-call option; `start_job` returns its steps and inputs and runs nothing, so the competency skill's task steps remain the method. This map names the job; it does not start it.

| Request | Catalogue job | Skill |
|---|---|---|
| Multi-year net impact of a population on a payer's budget, from the person's inputs | `budget-impact` (available, buyer supplies inputs) | `economic-model-development`; `economic-model-validity-monitoring` to review the run |
| Price ceiling per willingness-to-pay threshold, from the person's comparator cost, QALYs and thresholds | `price-anchor` (available, buyer supplies inputs) | `economic-model-development`. The ceiling is an input to a decision, not a price; the offer price is `dh-commercial` and a payer price is `dh-market-access` |
| Price a health-system conversation from the seller's numbers | `health-system-value-brief` (available, Commercial suite) | `economic-model-development` for the budget impact and price anchor; `pricing-and-value-proposition` (`dh-commercial`) for the offer |
| Payer value dossier outline | `value-dossier` (design partners, not startable) | `value-narrative-and-dossier`. The job cannot be started; the skill's own steps are the route |
| Graded evidence table for model inputs or a dossier | `evidence-table` (available) | `literature-and-real-world-evidence-review` (`dh-clinical-validation`), then back here |
| Reimbursement status by scheme, or prior listings on a scheme | `reimbursement-matrix`, `scheme-precedents` | `dh-market-access` (`coverage-pathway-and-access-strategy`), not this pack |

## Out of scope for this pack

Say so in one line and route where a home exists. Do not do the work from this map.

- Literature search, screening, grading and evidence tables: `dh-clinical-validation` `literature-and-real-world-evidence-review`.
- Payer routes, coverage schemes, coding, payer prices, HTA submission mechanics and payer contracts: `dh-market-access`. For an HTA submission, `payer-engagement-and-hta-submission`; for payment tied to outcomes, `outcomes-based-contracting`.
- The company's offer or list price and promotional value claims: `dh-commercial` (`pricing-and-value-proposition`; claims in `pricing-and-value-message-monitoring`). Clearance stops for the person's regulatory or legal owner.
- Device status, intended use and submissions: `dh-regulatory-strategy` (start with `regulatory-strategy-capability-map`).
- Value delivered to an existing customer after deployment (ROI notes, value realization): `dh-customer-success` (`outcome-tracking-and-customer-health`, `value-realization-monitoring`).
- Health economics for medicines: not covered by the Digital Health packs.
- Investor diligence on a company's evidence: `dh-diligence`.

## Routing examples

- "We need a cost-effectiveness model for our heart failure monitoring service for NICE." Route to `economic-model-development`. It builds on the person's inputs and the sourced method rows; whether the result is acceptable is NICE's decision. The submission itself is `payer-engagement-and-hta-submission` in `dh-market-access`.
- "A health system wants to know the three-year budget impact of our app." Route to `economic-model-development`; catalogue job `budget-impact`, with the population, mix, cost and uptake from the person.
- "Build us a value dossier for German payers." Route to `value-narrative-and-dossier`. The `value-dossier` job is for design partners and cannot be started; the evidence base comes from `literature-and-real-world-evidence-review`, and the DiGA route and pricing sit with `dh-market-access`.
- "Our reviewer says the model's utility values are weak. What now?" Route to `economic-model-validity-monitoring`, against the criteria the person sets.
- "Collect real-world cost data from our users to show savings." Route to `real-world-outcomes-research`.

## Related packs

Send the person to another pack when the question is not health economics:

- **Clinical Validation** (`dh-clinical-validation`): literature reviews, clinical study design and clinical evidence. Start with `clinical-validation-capability-map`; for any review, `literature-and-real-world-evidence-review`.
- **Market Access** (`dh-market-access`): anything a payer sets, codes, negotiates or reimburses. Skills: `coverage-pathway-and-access-strategy`, `coverage-strategy-and-access-rate-monitoring`, `payer-engagement-and-hta-submission`, `hta-submission-and-payer-engagement-monitoring`, `coding-pricing-and-payer-contracting`, `coding-pricing-and-contract-monitoring`, `outcomes-based-contracting`, `outcomes-contract-monitoring`.
- **Regulatory** (`dh-regulatory-strategy`): device status and submissions. Start with `regulatory-strategy-capability-map`.
- **Commercial** (`dh-commercial`): offer price, value messages in promotion and marketing claims. Start with `commercial-gtm-capability-map`.
- **Customer Success** (`dh-customer-success`): value realized at an existing customer. Start with `customer-success-capability-map`.

## Downloading the health economics expert

If the person wants a health economics expert role on their own assistant, route to the shared skill `digital-health-expert`. It replaces the three old expert shims of this pack.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a threshold, a model input, a price, a pass rule or a cost-effectiveness verdict, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- Catalogue job ids and statuses follow `list_jobs` as retrieved 19 October 2026.
- `evals/evals.json` routing tests, including one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
