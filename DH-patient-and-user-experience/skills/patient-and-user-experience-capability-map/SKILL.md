---
name: patient-and-user-experience-capability-map
description: >
  The map of the VITAL Patient & User Experience pack for digital health
  teams. Use it whenever someone asks "what can this pack do", "which patient engagement or
  UX skill do I need", "help with usability for
  our clinical app", or names a topic without naming a skill: patient research, co-design,
  patient advisory board, advocacy partnership, patient program, engagement KPIs, KPI
  reliability, health equity, inclusive design, reach, accessibility, WCAG, Section 508,
  EN 301 549, design system, user research, usability testing, clinician
  workflow, EHR screens, use error, SUS. It shows the framework tree and routes to one
  competency skill by its portable name. Not for doing the work itself: it never picks a
  KPI, threshold or equity priority, declares conformance or accepts usability results.
  Not for device status or human factors submissions (dh-regulatory-and-quality),
  personalization or behavior change (dh-digital-therapeutic-design), customer deployment
  pilots (dh-go-to-market), or omnichannel orchestration.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to are method skills
  that work on the person's own data; some use the VITAL Digital Health Library connector
  (mcp.vital.expert) for published sources and use-error events.
metadata:
  name: "patient-and-user-experience-capability-map"
  pack: "dh-patient-and-user-experience"
  framework_code: "DH-02.03; DH-02.04"
  register_code: "CF-12.02.03; CF-12.02.04"
  framework_path: "DH-02 > DH-02.03 Patient Engagement & Advocacy; DH-02 > DH-02.04 User Experience Excellence"
  version: "0.1.0-draft"
  replaces: "patient-engagement-capability-map; user-experience-capability-map; DH-02.03 Patient Engagement & Advocacy; DH-02.03.1 Patient Insights & Co-Design; DH-02.03.2 Engagement Programs & Advocacy; DH-02.03.3 Measurement & KPIs; DH-02.03.4 Health Equity & Accessibility; DH-02.04 User Experience Excellence; DH-02.04.1 Accessibility & Inclusion; DH-02.04.2 Design Systems; DH-02.04.3 User Research; DH-02.04.4 Healthcare UX Design"
---

# Patient & User Experience: capability map

Framework position: **DH-02.03 Patient Engagement & Advocacy** and **DH-02.04 User Experience Excellence**, two cores of the VITAL Digital Health capability framework, now one pack. This skill replaces the two old core maps (`patient-engagement-capability-map`, `user-experience-capability-map`) and their eight heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the patient engagement or UX question itself, call a connector, or state any guidance, code of practice, equity rule, standard or law, or by when it applies. Those live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-patient-and-user-experience`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from the measures, thresholds and criteria the person sets; it never sets its own. Conformance claims, design-system standards and usability acceptance are the person's decisions.

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

**DH-02.04 User Experience Excellence**

- **DH-02.04.1 Accessibility & Inclusion**
  - `accessibility-standards-implementation` (DH-02.04.1.1). Which accessibility requirements apply to this product and market, how is a barrier fixed, and how is it checked with assistive technology?
  - `accessibility-compliance-monitoring` (DH-02.04.1.2). Against the conformance target the person set, what does a sample of screens show, how long have barriers stayed open, and what goes to the release decision?
- **DH-02.04.2 Design Systems**
  - `design-system-development` (DH-02.04.2.1). What does each component promise (its contract), how is a component change made, and how do product teams adopt it?
  - `design-system-adoption-monitoring` (DH-02.04.2.2). Do components still meet their contract, how many products run behind the current version, and what follow-up is needed?
- **DH-02.04.3 User Research**
  - `patient-and-clinician-user-research` (DH-02.04.3.1). What does the study need to learn, with which patients or clinicians and which task, and what action follows from the session evidence?
  - `user-research-quality-monitoring` (DH-02.04.3.2). Did each research finding lead to an action, did the sample fit the question, and which findings are still unactioned?
- **DH-02.04.4 Healthcare UX Design**
  - `clinical-workflow-ux-design` (DH-02.04.4.1). Does the design fit the clinical task, where does it sit in the workflow, and what on the screen could lead to a use error?
  - `usability-monitoring` (DH-02.04.4.2). Against the usability criteria the person set, how did users do on each task, do the controls hold, and what goes into the release note?

## Folded menus

The old core and heading menus no longer exist as skills. A request that names one routes as follows.

| Old menu | Go to |
|---|---|
| DH-02.03 Patient Engagement & Advocacy, `patient-engagement-capability-map` | This map |
| DH-02.03.1 Patient Insights & Co-Design | `patient-research-and-co-design`; checking it: `co-design-quality-monitoring` |
| DH-02.03.2 Engagement Programs & Advocacy | `engagement-programs-and-advocacy-partnerships`; checking it: `engagement-and-advocacy-impact-monitoring` |
| DH-02.03.3 Measurement & KPIs | `engagement-kpi-dashboards`; checking it: `kpi-reliability-monitoring` |
| DH-02.03.4 Health Equity & Accessibility | `health-equity-and-inclusive-design`; checking it: `health-equity-monitoring`; conformance: `accessibility-standards-implementation` |
| DH-02.04 User Experience Excellence, `user-experience-capability-map` | This map |
| DH-02.04.1 Accessibility & Inclusion | `accessibility-standards-implementation`; checking it: `accessibility-compliance-monitoring` |
| DH-02.04.2 Design Systems | `design-system-development`; checking it: `design-system-adoption-monitoring` |
| DH-02.04.3 User Research | `patient-and-clinician-user-research`; checking it: `user-research-quality-monitoring` |
| DH-02.04.4 Healthcare UX Design | `clinical-workflow-ux-design`; checking it: `usability-monitoring` |

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
| Which accessibility standard applies, fixing a barrier, screen reader or keyboard checks | `accessibility-standards-implementation` | Meeting accessibility requirements |
| Accessibility audit, conformance sample, VPAT or statement evidence, open barriers before release | `accessibility-compliance-monitoring` | Checking conformance against the person's target |
| Interviews, contextual inquiry or task studies with patients or clinicians | `patient-and-clinician-user-research` | Running user research |
| "Did we act on the research", sample fit, unactioned findings | `user-research-quality-monitoring` | Checking research use |
| Clinician workflow fit, EHR-embedded screens, alerts, screen safety, use-error risks | `clinical-workflow-ux-design` | Designing for the clinical context |
| Usability test results, SUS or task success, release readiness from a usability view | `usability-monitoring` | Checking usability against the person's criteria |
| Component library, tokens, design-system governance, component change requests | `design-system-development` | Building the design system |
| Design-system adoption, version drift, component quality | `design-system-adoption-monitoring` | Checking the design system |

Tie-breakers:

1. Patients as partners shaping the product or program, or on an advisory board, go to `patient-research-and-co-design`. Task-based research and usability with patients or clinicians go to `patient-and-clinician-user-research`. If a request mixes both, name both and the order.
2. Who is reached and who is left out (equity) goes to `health-equity-and-inclusive-design`. Accessibility standards and conformance (WCAG, Section 508, EN 301 549) go to `accessibility-standards-implementation` and `accessibility-compliance-monitoring`. If a request mixes both, name both and the order.
3. Workflow fit and usability evidence are here. Whether the product is a device, and what a human factors submission must contain, stay with `dh-regulatory-and-quality`; name both when a usability study will feed a submission.
4. Design and execution come before monitoring. If nothing has been set up, built or studied yet, the monitoring skill has nothing to check; send the person to its partner first.
5. Any payment, gift or free item to patients, carers or advocacy organizations stops for the person's compliance or legal owner.
6. If the request is vague ("help with patients", "help with UX"), ask one question: is this about hearing from patients, running a program, measuring engagement, reaching groups that are left out, access, user research, clinical workflow, or the design system? Then route.

## Jobs to be done routed here

Job ids from the Digital Health JTBD Library, matched by described work in the alignment check of 19 October 2026.

| Job | Go to |
|---|---|
| JTBD-PSD-001 patient support ecosystem | `engagement-programs-and-advocacy-partnerships`, then `engagement-and-advocacy-impact-monitoring` |
| JTBD-PAL-001 patient partnership and voice | `patient-research-and-co-design`, then `co-design-quality-monitoring` |
| JTBD-PXD-002 inclusive experience | `health-equity-and-inclusive-design` for reach; `accessibility-standards-implementation` for conformance |
| JTBD-CS-001 engagement and churn, patient side | `engagement-kpi-dashboards`, then `kpi-reliability-monitoring` |
| JTBD-PXD-001 behavioral framework for patient experience | `dh-digital-therapeutic-design` |

## Routing examples

- "We want five people living with COPD to help redesign our inhaler-coaching app. How do we run that?" Route to `patient-research-and-co-design`.
- "A national kidney patient organization wants to co-host webinars with us. What should the partnership look like?" Route to `engagement-programs-and-advocacy-partnerships`, and flag that any payment to the organization stops for the person's compliance owner.
- "Our engagement dashboard shows 68% retention but the data team gets 54%. Which is right?" Route to `kpi-reliability-monitoring`.
- "Spanish-speaking patients enroll at half the rate of others. What can we do?" Route to `health-equity-and-inclusive-design`; equity priorities are the person's to set.
- "Is our patient app WCAG 2.2 AA compliant?" Route to `accessibility-compliance-monitoring`; the conformance claim stays with the person's owner.
- "We sell a patient portal to US hospitals and in the EU. Which accessibility rules do we have to meet?" Route to `accessibility-standards-implementation`; it lays out the sourced requirements per market.
- "Our nurses keep overriding the fall-risk alert in the EHR. Can we redesign it?" Route to `clinical-workflow-ux-design`.
- "We ran a summative usability test on our insulin dosing app. Is it ready to submit?" Route to `usability-monitoring` for the results against the person's criteria, and to `dh-regulatory-and-quality` `regulatory-submission-and-dossier` for what the submission needs. Usability acceptance is the person's decision.
- "Half our product teams use an old version of the button component." Route to `design-system-adoption-monitoring`.
- "We interviewed 12 oncologists last quarter and nothing changed in the product." Route to `user-research-quality-monitoring`.

## Related packs

Send the person to another pack when the question is not patient engagement or user experience:

- **Regulatory and Quality** (`dh-regulatory-and-quality`): device status, intended use, human factors content of a submission, use-related risk in the risk management file. Start with `regulatory-and-quality-capability-map`. Most used from here: `regulatory-pathway-and-classification` (is it a device), `regulatory-submission-and-dossier` (human factors in the file), `design-controls-and-risk-management` (the risk file).
- **Go-to-Market** (`dh-go-to-market`): the customer organization's adoption, health and renewal; customer training; deployment pilots at a customer site; commercial channel partners and promotional messages. Start with `go-to-market-capability-map`. Most used from here: `customer-implementation-planning` (deployment pilot), `pricing-and-value-message-monitoring` (a patient-facing message that makes a product claim). Patient engagement KPIs are here; account health is there. A formative service pilot to learn whether the service design works stays in `clinical-workflow-ux-design`.
- **Access and Value** (`dh-access-and-value`): where patient input feeds an HTA, and anything a payer prices, codes or pays on. Start with `access-and-value-capability-map`; for HTA patient input, `payer-engagement-and-hta-submission`.
- **Clinical Development** (`dh-clinical-development`): patient-reported outcomes in studies. Start with `clinical-development-capability-map`.
- Other Digital Health packs, by pack name: `dh-interoperability` (EHR integration and clinical workflow enablement), `dh-digital-therapeutic-design` (engagement mechanics, behavioral frameworks, behavior change and personalized journeys inside a therapeutic). Use each pack's own map or skill list.

## Out of scope

No skill in this pack does these. Say so in one line and route where a route exists.

| Request | Route |
|---|---|
| Acquisition cost and acquisition funnels (CAC to LTV, JTBD-GM-001), campaign targeting | Not covered by this pack |
| Omnichannel journey tracking and orchestration (JTBD-CSL-002, JTBD-PSD-003) | Not covered; it needs private channel data |
| Patient-level personalization, personalized journey or adaptive content (JTBD-PSD-002) | `dh-digital-therapeutic-design` (pack name) |
| Behavior-change intervention design, nudges or habit mechanics (JTBD-BSL-001) | `dh-digital-therapeutic-design` (pack name) |
| Organization-wide culture-change programs (JTBD-DAL-002) | Not covered; this pack trains customer staff on the product's tasks only |
| Deployment pilot, go-live or rollout at a customer site | `dh-go-to-market` `customer-implementation-planning` |
| Whether a product is a device, human factors submission content, summative validation conditions | `dh-regulatory-and-quality` `regulatory-pathway-and-classification` or `regulatory-submission-and-dossier` |

In scope here: the patient experience at task and workflow grain, the service blueprint and formative service pilot (`clinical-workflow-ux-design`), and research methods including remote sessions (`patient-and-clinician-user-research`).

## Downloading a patient engagement or UX expert

If the person wants a patient engagement or UX expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a KPI, a threshold, a target group or an equity priority, never declares conformance, sets a design-system standard, or accepts a usability result, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests from both halves of the pack, including cross-pack requests, one request that splits across the two halves, and requests this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
