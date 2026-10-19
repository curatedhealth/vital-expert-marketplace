---
name: patient-engagement-capability-map
description: >
  The map of the VITAL Patient Engagement & Advocacy pack for digital health and life
  sciences teams. Use it whenever someone asks "what can the patient engagement pack do",
  "which patient engagement skill do I need", "where do I start with patient co-design",
  or names a patient engagement topic (patient
  research, co-design, patient advisory board, lived experience, advocacy partnership,
  patient program, engagement KPIs, dashboard, KPI reliability, health equity, underserved
  groups, inclusive design, reach) without naming a skill. It shows the framework tree and
  routes the person to one competency skill by its portable name, and sorts requests that
  fall between patient engagement, user experience and customer success.
  Not for doing the patient engagement work itself: it never picks a KPI, a threshold or
  an equity priority. Not for accessibility standards or conformance
  (user-experience-capability-map), personalization or behavior change
  (dh-digital-therapeutic-design), or omnichannel orchestration.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to are method skills
  that work on the person's own data; some use the VITAL Digital Health Library connector
  (mcp.vital.expert) for published sources.
metadata:
  framework_code: "DH-02.03"
  register_code: "CF-12.02.03"
  framework_path: "DH-02 > DH-02.03 Patient Engagement & Advocacy"
  pack: "dh-patient-engagement"
  version: "0.1.0-draft"
  replaces: "DH-02.03 Patient Engagement & Advocacy; DH-02.03.1 Patient Insights & Co-Design; DH-02.03.2 Engagement Programs & Advocacy; DH-02.03.3 Measurement & KPIs; DH-02.03.4 Health Equity & Accessibility"
---

# Patient Engagement & Advocacy: capability map

Framework position: **DH-02.03 Patient Engagement & Advocacy**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu and its four heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the patient engagement question itself, call a connector, or state any guidance, code of practice or equity rule. Those live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-patient-engagement`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from the measures and thresholds the person sets; it never sets its own.

**DH-02.03 Patient Engagement & Advocacy**

- **DH-02.03.1 Patient Insights & Co-Design**
  - `patient-research-and-co-design` (DH-02.03.1.1). What question will patients or carers help answer, how is each co-design session captured, and which design change follows from it?
  - `co-design-quality-monitoring` (DH-02.03.1.2). Can each design change be traced to what participants said, did the participants fit the question, and which points remain unresolved?
- **DH-02.03.2 Engagement Programs & Advocacy**
  - `engagement-programs-and-advocacy-partnerships` (DH-02.03.2.1). What is a patient program for, what does it do, and where are the boundaries in a partnership with an advocacy organization?
  - `engagement-and-advocacy-impact-monitoring` (DH-02.03.2.2). Against the engagement results the person defined, what did each activity achieve, and what changes in the program?
- **DH-02.03.3 Measurement & KPIs**
  - `engagement-kpi-dashboards` (DH-02.03.3.1). How is each engagement KPI the person chose defined, which dashboard slice shows it, and how is it tracked automatically?
  - `kpi-reliability-monitoring` (DH-02.03.3.2). Does each KPI recompute to the same value from the source data, has a formula drifted, and what repair is needed?
- **DH-02.03.4 Health Equity & Accessibility**
  - `health-equity-and-inclusive-design` (DH-02.03.4.1). Which groups does the product reach or leave out, which inclusive change could close a gap, and which partner could help reach a group?
  - `health-equity-monitoring` (DH-02.03.4.2). Against the equity evidence the person defined, did a change reach the group it was meant for, and what follow-up is needed?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Patient advisory board, co-design workshop, lived-experience input, patient preference questions | `patient-research-and-co-design` | Running research and co-design with patients |
| "Did we act on what patients told us", participant fit, open co-design points | `co-design-quality-monitoring` | Checking co-design was used |
| Patient support or engagement program, advocacy group partnership, partner boundaries | `engagement-programs-and-advocacy-partnerships` | Building programs and partnerships |
| "Is our patient program working", advocacy partnership impact | `engagement-and-advocacy-impact-monitoring` | Checking programs against the person's results |
| Defining engagement KPIs, building a dashboard, automated tracking | `engagement-kpi-dashboards` | Building measurement |
| "Can we trust these numbers", KPI recomputation, formula drift | `kpi-reliability-monitoring` | Checking measurement |
| Who is left out, underserved groups, language, digital literacy, inclusive design changes | `health-equity-and-inclusive-design` | Equity assessment and inclusive change |
| "Did the change reach the group", reach by group over time | `health-equity-monitoring` | Checking equity outcomes |

Tie-breakers:

1. Co-design here treats patients as partners shaping the product or program. A usability study or task-based research with patients or clinicians goes to the User Experience pack (`patient-and-clinician-user-research`). If a request mixes both, name both and the order.
2. Equity here is about who is reached and who is left out. Accessibility standards and conformance (WCAG, Section 508, EN 301 549) go to the User Experience pack (`accessibility-standards-implementation`, `accessibility-compliance-monitoring`).
3. Design and execution come before monitoring. If nothing has been set up yet, the monitoring skill has nothing to check; send the person to its partner first.
4. Any payment, gift or free item to patients, carers or advocacy organizations stops for the person's compliance or legal owner.
5. If the request is vague ("help with patients"), ask one question: is this about hearing from patients, running a program, measuring engagement, or reaching groups that are left out? Then route.

## Jobs to be done routed here

Job ids from the Digital Health JTBD Library, matched by described work in the alignment check of 19 October 2026.

| Job | Go to |
|---|---|
| JTBD-PSD-001 patient support ecosystem | `engagement-programs-and-advocacy-partnerships`, then `engagement-and-advocacy-impact-monitoring` |
| JTBD-PAL-001 patient partnership and voice | `patient-research-and-co-design`, then `co-design-quality-monitoring` |
| JTBD-PXD-002 inclusive experience | `health-equity-and-inclusive-design` for reach; conformance to the User Experience pack |
| JTBD-CS-001 engagement and churn, patient side | `engagement-kpi-dashboards`, then `kpi-reliability-monitoring` |
| JTBD-PXD-001 behavioral framework for patient experience | `dh-digital-therapeutic-design` |

## Out of scope

No skill in this pack does these. Say so in one line and route where a route exists.

- Acquisition cost and acquisition funnels (CAC to LTV, JTBD-GM-001): not covered by this pack.
- Omnichannel journey tracking and orchestration (JTBD-CSL-002, JTBD-PSD-003): not covered; it needs private channel data.
- Patient-level personalization (JTBD-PSD-002): route to `dh-digital-therapeutic-design`.
- Behavior-change intervention design (JTBD-BSL-001): route to `dh-digital-therapeutic-design`.
- Organization-wide culture-change programs (JTBD-DAL-002): not covered; this pack trains customer staff on the product's tasks only.

## Routing examples

- "We want five people living with COPD to help redesign our inhaler-coaching app. How do we run that?" Route to `patient-research-and-co-design`.
- "A national kidney patient organization wants to co-host webinars with us. What should the partnership look like?" Route to `engagement-programs-and-advocacy-partnerships`, and flag that any payment to the organization stops for the person's compliance owner.
- "Our engagement dashboard shows 68% retention but the data team gets 54%. Which is right?" Route to `kpi-reliability-monitoring`.
- "Spanish-speaking patients enroll at half the rate of others. What can we do?" Route to `health-equity-and-inclusive-design`; equity priorities are the person's to set.
- "Is our patient app WCAG 2.2 AA compliant?" Route to the User Experience pack, `accessibility-compliance-monitoring`; this pack covers reach and equity, not conformance.

## Related packs

Send the person to another pack when the question is not patient engagement:

- **User Experience** (`dh-user-experience`): accessibility standards and conformance, design systems, task-based user research and usability. Start with `user-experience-capability-map`. Most used from here: `accessibility-standards-implementation`, `accessibility-compliance-monitoring`, `patient-and-clinician-user-research`.
- **Customer Success** (`dh-customer-success`): the customer organization's adoption, health and renewal. Start with `customer-success-capability-map`. Patient engagement KPIs are here; account health is there.
- **Commercial** (`dh-commercial`): commercial channel partners and promotional messages. Start with `commercial-gtm-capability-map`. A patient-facing message that makes a product claim goes there for the claims check (`pricing-and-value-message-monitoring`).
- **Regulatory** (`dh-regulatory-strategy`) and **Market Access** (`dh-market-access`): where patient input feeds a submission or an HTA. Start with `regulatory-strategy-capability-map`, or `payer-engagement-and-hta-submission` for HTA patient input.
- Other Digital Health packs, by pack name: `dh-clinical-validation` (patient-reported outcomes in studies), `dh-digital-therapeutic-design` (engagement mechanics, behavior change and personalization inside a therapeutic). Use each pack's own map or skill list.

## Downloading the patient engagement expert

If the person wants a patient engagement expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a KPI, a threshold, a target group or an equity priority, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests, including one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
