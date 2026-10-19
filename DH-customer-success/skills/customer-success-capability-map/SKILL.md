---
name: customer-success-capability-map
description: >
  The map of the VITAL Customer Success & Implementation pack for digital health products
  sold to health systems, clinics, payers, employers or pharma. Use it whenever someone
  asks "what can the customer success pack do", "which customer success skill do I need",
  "where do I start with this deployment", "help with renewals", or names a customer
  success topic (implementation plan, go-live, site rollout, deployment review, renewal,
  expansion, upsell, churn, customer health, outcome tracking, value realization, QBR,
  training, change management, adoption) without naming a skill. It shows the framework
  tree and routes the person to one competency skill by its portable name, and sorts
  requests that fall between customer success, commercial and market access.
  Not for doing the customer success work itself: it never sets a health score, judges
  renewal risk or picks a threshold. Not for outcomes-based payment contracts
  (dh-market-access outcomes-contract-monitoring), culture-change programs, or
  acquisition cost.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to are method skills
  that work on the person's own data; some use the VITAL Digital Health Library connector
  (mcp.vital.expert) for published sources.
metadata:
  framework_code: "DH-02.02"
  register_code: "CF-12.02.02"
  framework_path: "DH-02 > DH-02.02 Customer Success & Implementation"
  pack: "dh-customer-success"
  version: "0.1.0-draft"
  replaces: "DH-02.02 Customer Success & Implementation; DH-02.02.1 Implementation Delivery; DH-02.02.2 Expansion & Renewal; DH-02.02.3 Customer Health & Value Realization; DH-02.02.4 Adoption & Change Enablement"
---

# Customer Success & Implementation: capability map

Framework position: **DH-02.02 Customer Success & Implementation**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu and its four heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the customer success question itself, call a connector, or state any benchmark, framework rule or threshold. Those live in the competency skills, each with its own sourced references. Customer health, net revenue retention, churn and expansion rules are the person's own; no skill in this pack supplies them.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-customer-success`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from the measures and thresholds the person sets; it never sets its own.

**DH-02.02 Customer Success & Implementation**

- **DH-02.02.1 Implementation Delivery**
  - `customer-implementation-planning` (DH-02.02.1.1). What is in scope for this customer, in what order do sites or teams go live, and what bar must be met before go-live?
  - `implementation-quality-monitoring` (DH-02.02.1.2). Against the deployment checks the person set, how did each site go live, and what needs repair?
- **DH-02.02.4 Adoption & Change Enablement**
  - `training-and-change-enablement` (DH-02.02.4.1). Which tasks do customer staff need to learn, how is each session recorded, and what makes the change stay?
  - `adoption-monitoring` (DH-02.02.4.2). Against the adoption measures the person set, did use follow training, and what follow-up is needed?
- **DH-02.02.3 Customer Health & Value Realization**
  - `outcome-tracking-and-customer-health` (DH-02.02.3.1). Which signals the person chooses mean an account is healthy, how does each account read against them, and what value note goes back to the customer?
  - `value-realization-monitoring` (DH-02.02.3.2). Do the health thresholds still hold, does the evidence support the value the customer was told about, and who owns an unsupported note?
- **DH-02.02.2 Expansion & Renewal**
  - `account-growth-and-renewal` (DH-02.02.2.1). When does each renewal fall, what growth offer fits, and what does the renewal risk note record for the person to judge?
  - `expansion-and-renewal-monitoring` (DH-02.02.2.2). Using the renewal-rate definition the person sets, how do cohorts compare, and what did expansion deliver?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Implementation plan, scope, site sequence, go-live criteria, deployment coordination | `customer-implementation-planning` | Planning the deployment |
| "How did the rollout go", site-by-site go-live review, deployment problems | `implementation-quality-monitoring` | Checking the deployment |
| Training plan for customer staff, session records, change management, super-users | `training-and-change-enablement` | Enabling the customer's people |
| "Are they using it after training", adoption funnel, low-use sites | `adoption-monitoring` | Checking adoption against the person's measures |
| Health signals, account health review, outcome tracking, value note or QBR content | `outcome-tracking-and-customer-health` | Tracking agreed outcomes and account health |
| "Is our health score any good", is the claimed value supported, threshold review | `value-realization-monitoring` | Checking health and value evidence |
| Renewal calendar, upsell or expansion offer, renewal risk note | `account-growth-and-renewal` | Running renewal and growth |
| Renewal rate, churn by cohort, net retention, expansion results | `expansion-and-renewal-monitoring` | Checking renewal and expansion over time |

Tie-breakers:

1. Deployment before adoption, adoption before health, health before renewal. If an earlier step has no record yet, start there.
2. Design and execution come before monitoring. If nothing has been set up yet, the monitoring skill has nothing to check; send the person to its partner first.
3. Outcomes a customer agreed to see are tracked here. If payment depends on those outcomes, the contract and its measurement belong to Market Access (`outcomes-contract-monitoring`); name both and the order.
4. Any free item, rebate or incentive offered to patients or providers to win or keep an account stops for the person's compliance or legal owner.
5. If the request is vague ("help with a customer"), ask one question: is the customer deploying, adopting, being measured, or renewing? Then route.

## Jobs to be done routed here

Job ids from the Digital Health JTBD Library, matched by described work in the alignment check of 19 October 2026.

| Job | Go to |
|---|---|
| JTBD-ISM-001 implementation at scale | `customer-implementation-planning`, then `implementation-quality-monitoring` |
| JTBD-DAL-001 adoption inside a customer organization (health system, payer, employer or pharma) | `training-and-change-enablement`, then `adoption-monitoring` |
| JTBD-CS-001 engagement and churn | `outcome-tracking-and-customer-health`; patient engagement KPIs go to `engagement-kpi-dashboards` (`dh-patient-engagement`) |
| JTBD-CS-002 clinical outcomes achieved | `outcome-tracking-and-customer-health`, then `value-realization-monitoring` |

## Out of scope

No skill in this pack does these. Say so in one line and route where a route exists.

- Acquisition cost and acquisition funnels (CAC to LTV, JTBD-GM-001): not covered by this pack.
- Omnichannel journey tracking and orchestration (JTBD-CSL-002, JTBD-PSD-003): not covered; it needs private channel data.
- Patient-level personalization (JTBD-PSD-002): route to `dh-digital-therapeutic-design`.
- Behavior-change intervention design (JTBD-BSL-001): route to `dh-digital-therapeutic-design`.
- Organization-wide culture-change programs (JTBD-DAL-002): not covered; this pack trains customer staff on the product's tasks only.

## Routing examples

- "We signed a 12-hospital system for our sepsis alert. Where do we start?" Route to `customer-implementation-planning`.
- "Nurses at three of the hospitals stopped logging in a month after training." Route to `adoption-monitoring`; if the training itself needs rebuilding, `training-and-change-enablement` next.
- "Build me a customer health score for our employer accounts." Route to `outcome-tracking-and-customer-health`, and say that the signals, weights and thresholds come from the person; the skill computes against them.
- "Our renewal with a large payer is in two quarters and usage is down. What do we prepare?" Route to `account-growth-and-renewal`. Renewal risk is the person's judgement; the skill records the facts.
- "The contract pays us only if readmissions fall 10 percent. How do we track that?" Route to Market Access `outcomes-contract-monitoring` for the payment-linked measure; `outcome-tracking-and-customer-health` for the account view alongside it.

## Related packs

Send the person to another pack when the question is not customer success:

- **Market Access** (`dh-market-access`): where payment depends on outcomes, payer contracts and reimbursement. Skills: `outcomes-based-contracting`, `outcomes-contract-monitoring`, `coding-pricing-and-payer-contracting`, `coding-pricing-and-contract-monitoring`, `coverage-pathway-and-access-strategy`, `coverage-strategy-and-access-rate-monitoring`, `payer-engagement-and-hta-submission`, `hta-submission-and-payer-engagement-monitoring`.
- **Commercial** (`dh-commercial`): winning the account in the first place (segments, launch, offer price, channel partners). Start with `commercial-gtm-capability-map`. Sales-team enablement is there (`launch-planning-and-sales-enablement`); customer-staff training is here.
- **User Experience** (`dh-user-experience`): when low adoption traces to workflow fit or usability. Start with `user-experience-capability-map`; for clinical workflow, `clinical-workflow-ux-design`.
- **Patient Engagement** (`dh-patient-engagement`): patient-facing programs and engagement KPIs, as distinct from the customer organization's health. Start with `patient-engagement-capability-map`.
- Other Digital Health packs, by pack name: `dh-interoperability` (EHR integration and clinical workflow enablement during deployment), `dh-cybersecurity` (business associate and data processing terms), `dh-digital-therapeutic-design` (behavior change and personalization). Use each pack's own map or skill list.

## Downloading the customer success expert

If the person wants a customer success expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a health score, a renewal risk rating, a threshold or a target, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests, including one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
