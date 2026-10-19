---
name: user-experience-capability-map
description: >
  The map of the VITAL User Experience Excellence pack for digital health products. Use it whenever someone asks "what can the UX pack do",
  "which UX skill do I need", "help with usability for our clinical app", or names a UX topic (accessibility, WCAG, Section 508, EN 301 549,
  screen reader, design system, component library, user research, usability testing,
  clinician workflow, EHR screen design, use error, SUS) without naming a skill. It shows the framework tree and routes the person to one competency skill by its
  portable name, and sorts requests between UX, patient engagement and regulatory.
  Not for doing the UX work itself: it never declares conformance, sets a design-system
  standard or accepts usability results. Not for deciding whether a product is a device or
  what a human factors submission needs (dh-regulatory-strategy), behavioral frameworks
  for engagement or behavior change (dh-digital-therapeutic-design), or deployment
  pilots at a customer site (dh-customer-success).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to are method skills
  that work on the person's own data; some use the VITAL Digital Health Library connector
  (mcp.vital.expert) for published sources and use-error events.
metadata:
  framework_code: "DH-02.04"
  register_code: "CF-12.02.04"
  framework_path: "DH-02 > DH-02.04 User Experience Excellence"
  pack: "dh-user-experience"
  version: "0.1.0-draft"
  replaces: "DH-02.04 User Experience Excellence; DH-02.04.1 Accessibility & Inclusion; DH-02.04.2 Design Systems; DH-02.04.3 User Research; DH-02.04.4 Healthcare UX Design"
---

# User Experience Excellence: capability map

Framework position: **DH-02.04 User Experience Excellence**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu and its four heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the UX question itself, call a connector, or state what a standard, law or guidance requires, or by when. Those live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-user-experience`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria the person sets; conformance claims, standards and usability acceptance are the person's decisions.

**DH-02.04 User Experience Excellence**

- **DH-02.04.1 Accessibility & Inclusion**
  - `accessibility-standards-implementation` (DH-02.04.1.1). Which accessibility requirements apply to this product and market, how is a barrier fixed, and how is it checked with assistive technology?
  - `accessibility-compliance-monitoring` (DH-02.04.1.2). Against the conformance target the person set, what does a sample of screens show, how long have barriers stayed open, and what goes to the release decision?
- **DH-02.04.3 User Research**
  - `patient-and-clinician-user-research` (DH-02.04.3.1). What does the study need to learn, with which patients or clinicians and which task, and what action follows from the session evidence?
  - `user-research-quality-monitoring` (DH-02.04.3.2). Did each research finding lead to an action, did the sample fit the question, and which findings are still unactioned?
- **DH-02.04.4 Healthcare UX Design**
  - `clinical-workflow-ux-design` (DH-02.04.4.1). Does the design fit the clinical task, where does it sit in the workflow, and what on the screen could lead to a use error?
  - `usability-monitoring` (DH-02.04.4.2). Against the usability criteria the person set, how did users do on each task, do the controls hold, and what goes into the release note?
- **DH-02.04.2 Design Systems**
  - `design-system-development` (DH-02.04.2.1). What does each component promise (its contract), how is a component change made, and how do product teams adopt it?
  - `design-system-adoption-monitoring` (DH-02.04.2.2). Do components still meet their contract, how many products run behind the current version, and what follow-up is needed?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Which accessibility standard applies, fixing a barrier, screen reader or keyboard checks | `accessibility-standards-implementation` | Meeting accessibility requirements |
| Accessibility audit, conformance sample, VPAT or statement evidence, open barriers before release | `accessibility-compliance-monitoring` | Checking conformance against the person's target |
| Interviews, contextual inquiry or task studies with patients or clinicians | `patient-and-clinician-user-research` | Running user research |
| "Did we act on the research", sample fit, unactioned findings | `user-research-quality-monitoring` | Checking research use |
| Clinician workflow fit, EHR-embedded screens, alerts, screen safety, use-error risks | `clinical-workflow-ux-design` | Designing for the clinical context |
| Usability test results, SUS or task success, release readiness from a usability view | `usability-monitoring` | Checking usability against the person's criteria |
| Component library, tokens, design-system governance, component change requests | `design-system-development` | Building the design system |
| Design-system adoption, version drift, component quality | `design-system-adoption-monitoring` | Checking the design system |

Tie-breakers:

1. Accessibility conformance is here. Who is reached and who is left out (equity) is the Patient Engagement pack (`health-equity-and-inclusive-design`). If a request mixes both, name both and the order.
2. Task-based research and usability with patients or clinicians is here. Patients as co-design partners or on an advisory board go to the Patient Engagement pack (`patient-research-and-co-design`).
3. Workflow fit and usability evidence are here. Whether the product is a device, and what a human factors submission must contain, stay with the Regulatory pack; name both when a usability study will feed a submission.
4. Design and execution come before monitoring. If nothing has been built or studied yet, the monitoring skill has nothing to check; send the person to its partner first.
5. If the request is vague ("help with UX"), ask one question: is this about access, research, clinical workflow, or the design system? Then route.

## Routing examples

- "We sell a patient portal to US hospitals and in the EU. Which accessibility rules do we have to meet?" Route to `accessibility-standards-implementation`; it lays out the sourced requirements per market, and the conformance claim stays with the person's owner.
- "Our nurses keep overriding the fall-risk alert in the EHR. Can we redesign it?" Route to `clinical-workflow-ux-design`.
- "We ran a summative usability test on our insulin dosing app. Is it ready to submit?" Route to `usability-monitoring` for the results against the person's criteria, and to the Regulatory pack (`regulatory-submission-and-dossier`) for what the submission needs. Usability acceptance is the person's decision.
- "Half our product teams use an old version of the button component." Route to `design-system-adoption-monitoring`.
- "We interviewed 12 oncologists last quarter and nothing changed in the product." Route to `user-research-quality-monitoring`.

## Related packs

Send the person to another pack when the question is not user experience:

- **Regulatory** (`dh-regulatory-strategy`): device status, intended use, human factors content of a submission. Start with `regulatory-strategy-capability-map`. Most used from here: `regulatory-pathway-and-classification` (is it a device), `regulatory-submission-and-dossier` (human factors in the file).
- **Patient Engagement** (`dh-patient-engagement`): equity and reach, patient co-design, patient programs. Start with `patient-engagement-capability-map`. Most used from here: `health-equity-and-inclusive-design`, `patient-research-and-co-design`.
- **Customer Success** (`dh-customer-success`): customer training and adoption after deployment. Start with `customer-success-capability-map`.
- **Quality** (`dh-quality`): use-related risk in the risk management file and design controls. Start with `quality-management-capability-map`; for the risk file, `design-controls-and-risk-management`.
- Other Digital Health packs, by pack name: `dh-interoperability` (EHR integration and clinical workflow enablement), `dh-digital-therapeutic-design` (engagement mechanics, behavioral frameworks for engagement or behavior change, and personalized journeys inside a therapeutic). Use each pack's own map or skill list.
- **Customer Success** for a deployment pilot at a customer site: `customer-implementation-planning`. A formative service pilot to learn whether the service design works stays in `clinical-workflow-ux-design`.

## Out of scope

The pack does not do these jobs. Name the route and stop.

| Request | Route |
|---|---|
| Behavioral framework for engagement, behavior-change intervention design, nudges or habit mechanics | `dh-digital-therapeutic-design` (pack name) |
| Personalized patient journey or adaptive content | `dh-digital-therapeutic-design` (pack name) |
| Deployment pilot, go-live or rollout at a customer site | `customer-implementation-planning` (dh-customer-success) |
| Omnichannel journey orchestration, acquisition funnels or campaign targeting | Not covered by this pack; no Digital Health skill named for it |
| Whether a product is a device, human factors submission content, summative validation conditions | `dh-regulatory-strategy` |
| Patients as co-design partners, equity and reach | `dh-patient-engagement` |

In scope here: the patient experience at task and workflow grain, the service blueprint and formative service pilot (`clinical-workflow-ux-design`), and research methods including remote sessions (`patient-and-clinician-user-research`).

## Downloading the UX expert

If the person wants a UX expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never declares conformance, sets a design-system standard, or accepts a usability result, even as an example.
- Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests, including one cross-pack request and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
