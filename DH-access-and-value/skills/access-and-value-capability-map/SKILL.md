---
name: access-and-value-capability-map
description: >
  The map of the VITAL Access & Value pack for digital health products (SaMD, DTx,
  DiGA, remote monitoring): market access and reimbursement plus health economics and
  value demonstration. Use it whenever someone asks "what can the access and
  value pack do", "which skill do I need", "where do I start with reimbursement" or "with
  our value case", names a heading such as DH-03.01 or DH-01.07, or names a topic
  (coverage, reimbursement status, DiGA or PECAN, codes, payer price, HTA submission,
  outcomes contract, risk share, cost-effectiveness, budget impact, price anchor, QALY,
  model validation, outcomes study, value narrative, value dossier) without naming a
  skill. It routes to one competency skill, task or catalogue job. Not for doing the
  work: it never builds a model, sets a threshold or price, judges a model or
  dossier, or says a product is cost-effective. Not for literature review
  method (dh-clinical-development), device status (dh-regulatory-and-quality), offer
  price or marketing claims (dh-go-to-market).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector and calls no tool. The competency skills it routes to
  use the VITAL Digital Health Library connector (mcp.vital.expert), mainly the market
  access suite, the analytics calculators, the literature suite and Verify, for their
  evidence tasks.
metadata:
  framework_code: "DH-03.01; DH-01.07"
  register_code: "CF-12.03.01; CF-12.01.07"
  framework_path: "DH-03 > DH-03.01 Market Access & Reimbursement; DH-01 > DH-01.07 Health Economics & Value Demonstration"
  pack: "dh-access-and-value"
  version: "0.1.0-draft"
  replaces: "health-economics-capability-map; DH-03.01 Market Access & Reimbursement; DH-03.01.1 Value-Based Care & Outcomes Contracts; DH-03.01.2 Coding, Pricing & Contracting; DH-03.01.3 Payer & HTA Engagement; DH-03.01.4 Coverage & Access Strategy; DH-01.07 Health Economics & Value Demonstration; DH-01.07.1 Market Access Support; DH-01.07.2 Economic Modeling; DH-01.07.3 Outcomes Research; DH-01.07.4 Value Communication; Download a digital health expert; Download one digital health expert; Find digital health experts; dh-01-07-download-expert; dh-01-07-download-one-expert; dh-01-07-find-experts"
---

# Access & Value: capability map

Framework position: two cores of the VITAL Digital Health capability framework, **DH-03.01 Market Access & Reimbursement** and **DH-01.07 Health Economics & Value Demonstration**. This pack replaces `dh-market-access` and `dh-health-economics`. This skill replaces the old health economics map, the old market access core menu, both cores' heading menus and the expert shims. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the access or economic question itself, call a connector, or state any reimbursement status, code, price, threshold, model result, HTA rule or method requirement. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-access-and-value`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria and thresholds the person sets; it never sets its own pass rule.

**DH-03.01 Market Access & Reimbursement** (what a payer lists, codes, prices, contracts or reimburses)

- **DH-03.01.1 Value-Based Care & Outcomes Contracts**
  - `outcomes-based-contracting` (DH-03.01.1.1). Which outcome measures could carry payment, which risk-share designs fit, and what must the term sheet say? Tasks: A1 Outcome metric definition, A2 Risk-share options, B1 Contract structuring.
  - `outcomes-contract-monitoring` (DH-03.01.1.2). Against the contract's own rules, what is attainment per measure and per patient, what do missing data cost, and is the contract on track? Tasks: A1 Outcome attainment tracking, A2 Data completeness check, B1 Performance review.
- **DH-03.01.2 Coding, Pricing & Contracting**
  - `coding-pricing-and-payer-contracting` (DH-03.01.2.1). Which codes or payment routes could pay, what do price rules and registered prices say, and how is a payer or provider negotiation prepared? Tasks: A1 Coding pathway map, A2 Price evidence, B1 Contract negotiation preparation.
  - `coding-pricing-and-contract-monitoring` (DH-03.01.2.2). What changed in the codes and price rules, is the contract paying what was agreed, and which contracts are off track against the person's rules? Tasks: A1 Code and price change tracking, A2 Contract performance, B1 Performance review.
- **DH-03.01.3 Payer & HTA Engagement**
  - `payer-engagement-and-hta-submission` (DH-03.01.3.1). What does BfArM, the HAS CNEDiMTS or NICE require, which studies meet it, is the file ready, and whom to engage in what order? Tasks: A1 Evidence requirement map, A2 Submission readiness, B1 Engagement plan and value narrative.
  - `hta-submission-and-payer-engagement-monitoring` (DH-03.01.3.2). Is the draft dossier complete against the body's checklist, what was decided on the person's and comparable submissions, and is engagement on track? Tasks: A1 Submission quality check, A2 Decision tracking, B1 Performance review.
- **DH-03.01.4 Coverage & Access Strategy**
  - `coverage-pathway-and-access-strategy` (DH-03.01.4.1). Where is the product paid today, where could it be paid, in which order, and how does coverage become a patient getting it? Tasks: A1 Reimbursement status check, A2 Coverage pathway mapping, B1 Access strategy design, B2 Benefit design.
  - `coverage-strategy-and-access-rate-monitoring` (DH-03.01.4.2). What changed in status, which clocks are running, is coverage turning into uptake, and which markets have stalled? Tasks: A1 Coverage status tracking, A2 Uptake measurement, B1 Performance review.

**DH-01.07 Health Economics & Value Demonstration** (the evidence and the economic case behind a decision)

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
| Whether a named product is reimbursed in a country or scheme, DiGA or PECAN status | `coverage-pathway-and-access-strategy` (A1) | Status today, read from the library |
| Where the product could be paid, which pathway first, access plan, prescription and onboarding after listing | `coverage-pathway-and-access-strategy` (A2, B1, B2) | Designing the coverage route |
| Status changes, DiGA trial period or other clocks, uptake from the person's data, stalled markets | `coverage-strategy-and-access-rate-monitoring` | Checking the coverage strategy over time |
| Which codes pay, "can we bill", fee schedule, DiGA group maximum, comparator prices, negotiation brief | `coding-pricing-and-payer-contracting` | Codes, price rules and negotiation preparation |
| Code or price rule changes, denials, realized versus agreed price, discount tiers | `coding-pricing-and-contract-monitoring` | Checking codes, prices and contracts over time |
| What BfArM, HAS or NICE requires, whether studies meet it, file readiness, fees, whom to engage | `payer-engagement-and-hta-submission` | Preparing the submission and engagement |
| "Is our dossier complete before we file", decisions on the person's or comparable submissions, engagement review | `hta-submission-and-payer-engagement-monitoring` | Checking the submission and engagement |
| Outcome measures that carry payment, risk share, ACCESS withhold, the German 20 percent outcome-linked price, term sheet | `outcomes-based-contracting` | Designing an outcomes contract |
| Attainment against a running outcomes contract, missing follow-up, reconciliation | `outcomes-contract-monitoring` | Checking a running outcomes contract |
| What evidence and economic case a reimbursement decision needs, readiness of the economic case, the economic dossier section | `reimbursement-evidence-support` | Building the evidence and economic case |
| How the evidence fared in decisions, what a committee accepted or doubted, evidence outcomes against the person's measures | `reimbursement-evidence-monitoring` | Checking the evidence case over time |
| Cost-effectiveness model, QALYs, budget impact, launch price ceiling per threshold, model inputs | `economic-model-development` | Building the model on the person's inputs |
| "Is our model valid", review against reporting standards, sensitivity, model repair | `economic-model-validity-monitoring` | Checking the model against the person's criteria |
| Real-world outcomes study, costs and resource use, PROs or utilities for value | `real-world-outcomes-research` | Generating outcomes evidence for value |
| "Is our outcomes study rigorous", study quality review, evidence repair | `outcomes-evidence-quality-monitoring` | Checking the outcomes study |
| Value narrative, value audience, payer value dossier outline | `value-narrative-and-dossier` | Telling the value story from checked evidence |
| How the value narrative is received, narrative repair | `value-communication-monitoring` | Checking value communication over time |

Tie-breakers:

1. The two halves split by subject. What a payer lists, codes, prices, contracts or reimburses, and the mechanics of filing with a body, are DH-03.01. The evidence and the economic case a decision rests on are DH-01.07. If a request mixes both, name both skills and the order.
2. Submission requirements: the file, fees, clocks and engagement are `payer-engagement-and-hta-submission`; the economic case inside the file is `reimbursement-evidence-support`. Decisions: listing status and clocks are `coverage-strategy-and-access-rate-monitoring` or `hta-submission-and-payer-engagement-monitoring`; how a decision treated the evidence is `reimbursement-evidence-monitoring`.
3. A value narrative for engagement with a named body is `payer-engagement-and-hta-submission` (B1); a value dossier for payers, formulary committees or commissioners is `value-narrative-and-dossier`.
4. Budget impact as an economic model is `economic-model-development`; budget impact as an input to a risk share is `outcomes-based-contracting` (A2). A price ceiling per threshold is `economic-model-development`; a payer price, price rule or negotiation is `coding-pricing-and-payer-contracting`.
5. Outcomes that carry payment in a contract are `outcomes-based-contracting` and `outcomes-contract-monitoring`; outcomes as value evidence are `real-world-outcomes-research` and `outcomes-evidence-quality-monitoring`.
6. Any literature review goes to `literature-and-real-world-evidence-review` in `dh-clinical-development`, always. A study whose main question is clinical efficacy or safety is `study-protocol-and-endpoint-design` in `dh-clinical-development`.
7. Design and execution come before monitoring. If no contract, file, model, study or narrative exists yet, the monitoring skill has nothing to check; send the person to its partner first.
8. A model is never more than its inputs. Thresholds, prices, whether a model is acceptable, whether a product is cost-effective and whether it will be reimbursed are the person's, the payer's or the HTA body's decision; the pack never states them.
9. If the request is vague ("help with access", "help with value"), ask one question: is this about coverage and status, codes and prices, an HTA submission, an outcomes contract, the evidence for a decision, an economic model, an outcomes study, or the value story? Then route.

## Old names: where each one goes now

The old menu skills and task sections no longer exist. When a person names one, route as below.

| Old name | Now |
|---|---|
| DH-03.01 Market Access & Reimbursement (core menu) | This map, DH-03.01 half of the tree |
| DH-03.01.1 Value-Based Care & Outcomes Contracts (heading menu) | Show `outcomes-based-contracting` and `outcomes-contract-monitoring`; ask which |
| DH-03.01.1.1 Outcomes-Based Contracting & Value-Based Care Integration | `outcomes-based-contracting` |
| DH-03.01.1.2 VBC Contract Effectiveness Assessment & Outcomes Achievement Monitoring | `outcomes-contract-monitoring` |
| DH-03.01.2 Coding, Pricing & Contracting (heading menu) | Show `coding-pricing-and-payer-contracting` and `coding-pricing-and-contract-monitoring`; ask which |
| DH-03.01.2.1 Coding Strategy Development & Payer/Provider Contracting | `coding-pricing-and-payer-contracting` |
| DH-03.01.2.2 Coding & Pricing Effectiveness Assessment & Contract Performance Monitoring | `coding-pricing-and-contract-monitoring` |
| DH-03.01.3 Payer & HTA Engagement (heading menu) | Show `payer-engagement-and-hta-submission` and `hta-submission-and-payer-engagement-monitoring`; ask which |
| DH-03.01.3.1 Payer Engagement & HTA Submission Execution | `payer-engagement-and-hta-submission` |
| DH-03.01.3.2 HTA Submission Quality Assessment & Payer Engagement Effectiveness Monitoring | `hta-submission-and-payer-engagement-monitoring` |
| DH-03.01.4 Coverage & Access Strategy (heading menu) | Show `coverage-pathway-and-access-strategy` and `coverage-strategy-and-access-rate-monitoring`; ask which |
| DH-03.01.4.1 Coverage Pathway Design & Benefit Access Strategy Execution | `coverage-pathway-and-access-strategy` |
| DH-03.01.4.2 Coverage Strategy Effectiveness Assessment & Access Rate Monitoring | `coverage-strategy-and-access-rate-monitoring` |
| Value Dossier Assembly; HTA Submission Preparation (task sections) | `payer-engagement-and-hta-submission` (A1 and A2) |
| Payer Negotiation (task section) | `coding-pricing-and-payer-contracting` (B1) |
| Payer Engagement Effectiveness Monitoring; HTA submission pass rule; HTA submission miss owner (task sections) | `hta-submission-and-payer-engagement-monitoring` (A2 and B1) |
| DH-01.07 Health Economics & Value Demonstration (core menu); `health-economics-capability-map` | This map, DH-01.07 half of the tree |
| DH-01.07.1 Market Access Support (heading menu) | Show `reimbursement-evidence-support` and `reimbursement-evidence-monitoring`; ask which |
| DH-01.07.1.1 Reimbursement Decision Support & Market Access Execution | `reimbursement-evidence-support` |
| DH-01.07.1.2 Market Access Effectiveness Assessment & Reimbursement Outcome Monitoring | `reimbursement-evidence-monitoring` |
| Access pathway; Submission readiness; Access dossier item (task sections) | `reimbursement-evidence-support` (A1, A2, B1). The pathway itself is `coverage-pathway-and-access-strategy`; file mechanics, fees and clocks are `payer-engagement-and-hta-submission` (A2) |
| Access outcome definition; Access score; Access miss (task sections) | `reimbursement-evidence-monitoring` (B1) |
| DH-01.07.2 Economic Modeling (heading menu) | Show `economic-model-development` and `economic-model-validity-monitoring`; ask which |
| DH-01.07.2.1 Digital Health Economic Model Development & Cost-Effectiveness Analysis | `economic-model-development` |
| DH-01.07.2.2 Economic Model Validity Assessment & Cost-Effectiveness Monitoring | `economic-model-validity-monitoring` |
| DH-01.07.3 Outcomes Research (heading menu) | Show `real-world-outcomes-research` and `outcomes-evidence-quality-monitoring`; ask which |
| DH-01.07.3.1 Real-World Outcomes Evidence Generation & Study Execution | `real-world-outcomes-research` |
| DH-01.07.3.2 Outcomes Evidence Quality Assessment & Study Rigor Monitoring | `outcomes-evidence-quality-monitoring` |
| DH-01.07.4 Value Communication (heading menu) | Show `value-narrative-and-dossier` and `value-communication-monitoring`; ask which |
| DH-01.07.4.1 Evidence-to-Stakeholder Translation & Value Narrative Development | `value-narrative-and-dossier` |
| DH-01.07.4.2 Value Communication Effectiveness Assessment & Stakeholder Reception Monitoring | `value-communication-monitoring` |
| Download a digital health expert; Find digital health experts; Download one digital health expert; dh-01-07-download-expert; dh-01-07-find-experts; dh-01-07-download-one-expert | `digital-health-expert` |

## Catalogue jobs: which skill and job a request goes to

The VITAL Digital Health Library lists one-call jobs (`list_jobs`, 19 October 2026). A job is the buyer's one-call option; `start_job` returns its steps and inputs and runs nothing, so the competency skill's task steps remain the method. This map names the job; it does not start it.

| Request | Catalogue job | Skill |
|---|---|---|
| Reimbursement status of a product by scheme or market | `reimbursement-matrix` (available) | `coverage-pathway-and-access-strategy` (A1) |
| Prior listings and decisions on a scheme | `scheme-precedents` (available) | `coverage-strategy-and-access-rate-monitoring` (A1) or `hta-submission-and-payer-engagement-monitoring` (A2); how the decisions treated the evidence is `reimbursement-evidence-monitoring`. A scheme watch is set only on the person's request, in `coverage-strategy-and-access-rate-monitoring`; watches are not separated by customer key |
| Multi-year net impact of a population on a payer's budget, from the person's inputs | `budget-impact` (available, buyer supplies inputs) | `economic-model-development`; `economic-model-validity-monitoring` to review the run |
| Price ceiling per willingness-to-pay threshold, from the person's comparator cost, QALYs and thresholds | `price-anchor` (available, buyer supplies inputs) | `economic-model-development`. The ceiling is an input to a decision, not a price; the offer price is `dh-go-to-market` and a payer price is `coding-pricing-and-payer-contracting` |
| Price a health-system conversation from the seller's numbers | `health-system-value-brief` (available, Commercial suite) | `economic-model-development` for the budget impact and price anchor; `pricing-and-value-proposition` (`dh-go-to-market`) for the offer |
| Payer value dossier outline | `value-dossier` (design partners, not startable) | `value-narrative-and-dossier`. The job cannot be started; the skill's own steps are the route |
| Graded evidence table for model inputs or a dossier | `evidence-table` (available) | `literature-and-real-world-evidence-review` (`dh-clinical-development`), then back here |
| Outcomes contract or risk share | None (`find_job` returned no job, as recorded in that skill's tool notes) | `outcomes-based-contracting` |

## Out of scope for this pack

Say so in one line and route where a home exists. Do not do the work from this map.

- Literature search, screening, grading and evidence tables: `dh-clinical-development` `literature-and-real-world-evidence-review`.
- Clinical study design for efficacy or safety: `dh-clinical-development` `study-protocol-and-endpoint-design`.
- The company's offer or list price and promotional value claims: `dh-go-to-market` (`pricing-and-value-proposition`; claims in `pricing-and-value-message-monitoring`). Clearance stops for the person's regulatory or legal owner.
- Device status, intended use and regulatory submissions: `dh-regulatory-and-quality` (start with `regulatory-and-quality-capability-map`; for device status, `regulatory-pathway-and-classification`).
- Value delivered to an existing customer after deployment (ROI notes, value realization): `dh-go-to-market` (`outcome-tracking-and-customer-health`, `value-realization-monitoring`).
- Drugs, biologics and wellness apps: not covered by the Digital Health packs.
- Investor diligence on a company's evidence: `dh-diligence`.

## Routing examples

- "Is our app reimbursed in France yet?" Route to `coverage-pathway-and-access-strategy`, task A1; catalogue job `reimbursement-matrix`. The status comes from the library, not from this map.
- "Our DiGA trial period is running; when does it end and how did similar apps fare?" Route to `coverage-strategy-and-access-rate-monitoring`, task A1.
- "We need a cost-effectiveness model for our heart failure monitoring service for NICE." Route to `economic-model-development`. It builds on the person's inputs and the sourced method rows; whether the result is acceptable is NICE's decision. The submission itself is `payer-engagement-and-hta-submission`.
- "A health system wants to know the three-year budget impact of our app." Route to `economic-model-development`; catalogue job `budget-impact`, with the population, mix, cost and uptake from the person.
- "Build us a value dossier for German payers." Route to `value-narrative-and-dossier`. The `value-dossier` job is for design partners and cannot be started; the evidence base comes from `literature-and-real-world-evidence-review` (`dh-clinical-development`), and the DiGA route and price sit with `coverage-pathway-and-access-strategy` and `coding-pricing-and-payer-contracting`.
- "Our model is done; which CPT codes apply and how do we negotiate with Medicare Advantage plans?" Two skills, in order: `economic-model-validity-monitoring` if the model still needs review, then `coding-pricing-and-payer-contracting` (A1 for codes, B1 for the negotiation).
- "Should we offer the payer a risk share on PHQ-9?" Route to `outcomes-based-contracting`.

## Related packs

Send the person to another pack when the question is not access or value:

- **Clinical Development** (`dh-clinical-development`): literature reviews, clinical study design and clinical evidence. Start with `clinical-development-capability-map`; for any review, `literature-and-real-world-evidence-review`.
- **Regulatory and Quality** (`dh-regulatory-and-quality`): device status, submissions and quality systems. Start with `regulatory-and-quality-capability-map`.
- **Go-to-Market** (`dh-go-to-market`): offer price, value messages in promotion, marketing claims, and value realized at an existing customer. Start with `go-to-market-capability-map`.

## Downloading an access or health economics expert

If the person wants a market access or health economics expert role on their own assistant, route to the shared skill `digital-health-expert`. It replaces the expert shims of both old packs (Find digital health experts, Download one digital health expert, Download a digital health expert).

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a threshold, a model input, a price, a code, a reimbursement status, a pass rule or a cost-effectiveness verdict, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- Catalogue job ids and statuses follow `list_jobs` as retrieved 19 October 2026, as recorded in the competency skills' tool notes.
- `evals/evals.json` routing tests: at least one per half of the pack, one request routed across both halves, one old heading name and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
