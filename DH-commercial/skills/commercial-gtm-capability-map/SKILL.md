---
name: commercial-gtm-capability-map
description: >
  The map of the VITAL Commercial & GTM Strategy pack for digital health products (SaMD,
  DTx, DiGA-type apps, remote monitoring, clinical software). Use it whenever someone asks
  "what can the commercial pack do", "which commercial skill or job do I need", "where do
  I start with our launch", or names a commercial topic (launch, sales enablement,
  segmentation, positioning, competitor landscape, value proposition, price positioning,
  claims, channel, partner) without naming a skill. It routes the person to one
  competency skill and its catalogue job, and sorts requests that fall between
  commercial, market access, regulatory and customer success. Not for doing the
  commercial work itself (it never picks a segment, sets a price, clears a claim or
  chooses a partner), payer prices or codes (dh-market-access), acquisition cost and
  lifetime value, referral mechanics, omnichannel tracking, culture-change programs, or
  patient personalization and behavior change (dh-digital-therapeutic-design).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to use the VITAL
  Digital Health Library connector (mcp.vital.expert), mainly the Commercial suite, for
  their evidence tasks.
metadata:
  framework_code: "DH-02.01"
  register_code: "CF-12.02.01"
  framework_path: "DH-02 > DH-02.01 Commercial & GTM Strategy"
  pack: "dh-commercial"
  version: "0.1.0-draft"
  replaces: "DH-02.01 Commercial & GTM Strategy; DH-02.01.1 Commercial Execution; DH-02.01.2 GTM Strategy; DH-02.01.3 Pricing & Value Communication; DH-02.01.4 Channel & Partnership Strategy"
---

# Commercial & GTM Strategy: capability map

Framework position: **DH-02.01 Commercial & GTM Strategy**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu and its four heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the commercial question itself, call a connector, or state any price, market figure, competitor fact or promotion rule. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-commercial`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from measures and thresholds the person sets; it never sets its own target.

**DH-02.01 Commercial & GTM Strategy**

- **DH-02.01.2 GTM Strategy**
  - `market-segmentation-and-gtm-strategy` (DH-02.01.2.1). Which segments could the product serve, which go-to-market motion fits each, how is it positioned, and what do commercial peers on record show?
  - `gtm-positioning-monitoring` (DH-02.01.2.2). Against the positioning the person chose, do the live materials still say it, and where do they drift?
- **DH-02.01.1 Commercial Execution**
  - `launch-planning-and-sales-enablement` (DH-02.01.1.1). How is the launch sequenced, how ready is it, which claims go into launch materials, and who on the sales side is enabled to use them?
  - `launch-performance-monitoring` (DH-02.01.1.2). Against the launch measures the person set, how is the launch going, what has changed in the commercial record, and who owns a miss?
- **DH-02.01.3 Pricing & Value Communication**
  - `pricing-and-value-proposition` (DH-02.01.3.1). What is the unit of value, where could the offer price sit against what is on record, how does money flow between buyer, payer and user, and what is the value message?
  - `pricing-and-value-message-monitoring` (DH-02.01.3.2). Against the price outcomes the person set, what was realized, and do the value and promotional claims hold up against the sourced rules? It flags claims and drafts safer wording; it never clears a claim.
- **DH-02.01.4 Channel & Partnership Strategy**
  - `channel-and-partner-design` (DH-02.01.4.1). Which channels and partners fit, what role does each play, which terms need confirming, and how do the options the person scored rank?
  - `channel-and-partnership-monitoring` (DH-02.01.4.2). Against the channel measures the person set, how is each partner performing, and what action follows?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Target segments, ideal customer, GTM motion, positioning line, competitor or peer landscape | `market-segmentation-and-gtm-strategy` | Choosing where and how to compete |
| "Is our messaging still on position", positioning drift across website, decks, sales materials | `gtm-positioning-monitoring` | Checking positioning against what was chosen |
| Launch plan, launch sequence, launch readiness, commercial brief, sales leave-behind, sales enablement | `launch-planning-and-sales-enablement` | Building and running the launch |
| Launch KPIs, "how is the launch going", changes in the commercial record since launch | `launch-performance-monitoring` | Tracking the launch over time |
| Value proposition, unit of value, offer or list price positioning, money flow, value message | `pricing-and-value-proposition` | Designing the offer and its message |
| Realized vs planned price, discounting, "can we say this in our ad", claims audit | `pricing-and-value-message-monitoring` | Checking price outcomes and claims |
| Channel design, resellers, distribution, health-system or pharma partners, ranking partner options | `channel-and-partner-design` | Designing channels and partner roles |
| Partner scorecards, channel performance, what to do about an underperforming partner | `channel-and-partnership-monitoring` | Checking channels and partners |

Tie-breakers:

1. Strategy before execution: if no segment or positioning is chosen yet, start with `market-segmentation-and-gtm-strategy` before `launch-planning-and-sales-enablement`.
2. Design and execution come before monitoring. If nothing has been set or launched, the monitoring skill has nothing to check; send the person to its partner first.
3. A price the company offers or positions is here. A price, code or payment a payer sets, negotiates or reimburses is Market Access (see Related packs). If a request mixes both, name both and the order.
4. Any claim question ends with the person's regulatory or legal owner. The pack drafts and flags; it never clears.
5. If the request is vague ("help with commercial"), ask one question: is this about where to compete, how to launch, what to charge and say, or who to sell through? Then route.

## Catalogue jobs: which skill and job a request goes to

The VITAL Digital Health Library lists one-call jobs for the Commercial suite (`list_jobs`, 19 October 2026: 13 jobs, all available). A job is the buyer's one-call option; `start_job` returns its steps and inputs and runs nothing, so the competency skill's task steps remain the method. This map names the job; it does not start it.

| Request | Catalogue job | Skill and task |
|---|---|---|
| Rivals' regulatory, evidence and access position | `competitor-landscape` | `market-segmentation-and-gtm-strategy` A1; `gtm-positioning-monitoring` A2 for movement |
| Peer list for a segment | `screen-commercial-peers` | `market-segmentation-and-gtm-strategy` A1; `channel-and-partner-design` A1 |
| What changed for a product | `product-watch` | `launch-performance-monitoring` A1 (dated reruns of `get_deltas`; the skills never set a watch) |
| Who uses, buys and pays | `money-flow` | `pricing-and-value-proposition` A1 |
| Claims against the authorization on file | `claim-labels` | `launch-planning-and-sales-enablement` A2; `pricing-and-value-message-monitoring` A2 |
| Public price stored for a product | `pricing-corridor` | `pricing-and-value-proposition` A2 |
| Authorization and listing dates for a launch | `launch-sequence` | `launch-planning-and-sales-enablement` A1 |
| Commercial launch checklist | `launch-readiness` | `launch-planning-and-sales-enablement` A1 |
| One memo a founder can hand on | `commercial-brief` | `launch-planning-and-sales-enablement` A1 |
| Rank partners, indications or segments the person scored | `partner-prioritization` | `channel-and-partner-design` B1; `market-segmentation-and-gtm-strategy` B1 |
| One page for a sales call | `sales-leave-behind` | `launch-planning-and-sales-enablement` B1 |
| Compare candidate partners the person scored | `partnership-screen` | `channel-and-partner-design` B1 |
| Price a health-system conversation from the seller's numbers | `health-system-value-brief` | `pricing-and-value-proposition` A2 and B1; for an existing customer, `account-growth-and-renewal` A2 (`dh-customer-success`) |

## Out of scope for this pack

Say so in one line and route where a home exists. Do not do the work from this map.

- Customer acquisition cost and lifetime value models: not covered by this pack.
- Referral program mechanics: not covered. A referral incentive is a fraud-and-abuse stop handled in `channel-and-partner-design`; the program design itself is out of scope.
- Omnichannel journey tracking and orchestration: not covered (it runs on the person's private data and systems).
- Patient-level personalization and behavior-change design: route to `dh-digital-therapeutic-design` (personalization engine; engagement mechanics).
- Culture-change programs inside an organization: not covered. Adoption of a deployed product by a customer's staff is `dh-customer-success` (`training-and-change-enablement`).

## Routing examples

- "We have a DiGA-listed insomnia app and want to enter the US employer market. Where do we start?" Route to `market-segmentation-and-gtm-strategy`. It lays out segments and motions for the person to choose; it does not pick one.
- "Our launch is planned in three countries. Can you check launch readiness and build the sales leave-behind?" Route to `launch-planning-and-sales-enablement`.
- "Marketing wants to say our app 'reduces HbA1c by 1 point'. Can we?" Route to `pricing-and-value-message-monitoring`. It flags the claim against the sourced rules and drafts safer wording; clearance stops for the person's regulatory or legal owner.
- "We want to offer free devices to clinics that sign up patients." Route to `channel-and-partner-design`, and say that any free item or payment tied to referrals or volume stops for the person's compliance or legal owner; the skill lays out the facts, never that an arrangement is protected.
- "Our reseller in Germany is missing targets. What now?" Route to `channel-and-partnership-monitoring`.

## Related packs

Send the person to another pack when the question is not commercial:

- **Market Access** (`dh-market-access`): anything a payer sets, codes, negotiates or reimburses. Skills: `coverage-pathway-and-access-strategy`, `coverage-strategy-and-access-rate-monitoring`, `payer-engagement-and-hta-submission`, `hta-submission-and-payer-engagement-monitoring`, `coding-pricing-and-payer-contracting`, `coding-pricing-and-contract-monitoring`, `outcomes-based-contracting`, `outcomes-contract-monitoring`. Most used from here: `coding-pricing-and-payer-contracting` for payer price and codes, `outcomes-based-contracting` where payment depends on outcomes.
- **Regulatory** (`dh-regulatory-strategy`): intended use, classification and what the label permits. Start with `regulatory-strategy-capability-map`; for intended use, `regulatory-pathway-and-classification`. A claim that changes intended use is a regulatory question first.
- **Customer Success** (`dh-customer-success`): what happens after the contract is signed (implementation, customer training, health, renewal). Start with `customer-success-capability-map`. Sales-team enablement is here; customer-staff training is there (`training-and-change-enablement`).
- **Patient Engagement** (`dh-patient-engagement`): patient advocacy partnerships and patient programs. Start with `patient-engagement-capability-map`; for advocacy partners, `engagement-programs-and-advocacy-partnerships`. Commercial channel partners stay here.
- **User Experience** (`dh-user-experience`): accessibility, design systems, user research and usability. Start with `user-experience-capability-map`.
- Other Digital Health packs, by pack name: `dh-health-economics` (economic models, value dossiers), `dh-clinical-validation` (the clinical evidence behind a claim). Use each pack's own map or skill list.

## Downloading the commercial expert

If the person wants a commercial expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a segment, a price, a target, a partner or a claim verdict, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- Catalogue job ids follow `list_jobs` as retrieved 19 October 2026.
- `evals/evals.json` routing tests, including one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
