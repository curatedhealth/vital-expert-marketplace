---
name: regulatory-strategy-capability-map
description: >
  The map of the VITAL Regulatory Strategy & Submissions pack for digital health products
  (SaMD, AI/ML devices, DTx, DiGA-type apps). Use it whenever someone asks "what can the
  regulatory pack do", "which regulatory skill do I need", "where do I start with our FDA or
  EU MDR pathway", "help me with regulatory strategy for our app", or names a regulatory
  topic (classification, predicates, PCCP, change control, multi-country registration,
  dossier, CER, submission outcome) without naming a skill. It shows the framework tree
  and routes the person to one competency skill by its portable name. Use it also when a
  request falls between regulatory, quality and market access and needs sorting.
  Not for doing the regulatory work itself: it never classifies a product, picks a
  pathway, reads a register or drafts a submission. Not for drugs or biologics.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to use the VITAL
  Digital Health Library connector (mcp.vital.expert) for their evidence tasks.
metadata:
  framework_code: "DH-03.03"
  register_code: "CF-12.03.03"
  framework_path: "DH-03 > DH-03.03 Regulatory Strategy & Submissions"
  pack: "dh-regulatory-strategy"
  version: "0.1.0-draft"
  replaces: "DH-03.03 Regulatory Strategy & Submissions; DH-03.03.1 AI/ML Regulatory; DH-03.03.2 Global Harmonization; DH-03.03.3 Regulatory Strategy; DH-03.03.4 Submission Excellence"
---

# Regulatory Strategy & Submissions: capability map

Framework position: **DH-03.03 Regulatory Strategy & Submissions**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu and its four heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the regulatory question itself, call a connector, or state any rule, class, pathway, fee or clock. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-regulatory-strategy`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria the person sets; it never sets its own pass rule.

**DH-03.03 Regulatory Strategy & Submissions**

- **DH-03.03.3 Regulatory Strategy**
  - `regulatory-pathway-and-classification` (DH-03.03.3.1). What is the intended use, how might this product be classified in each market, which routes are open, and what do comparable devices, predicates and authorizations on record show?
  - `regulatory-pathway-monitoring` (DH-03.03.3.2). Is the chosen pathway still on track, and what has changed in the registers, the comparables or the safety record since it was chosen?
- **DH-03.03.1 AI/ML Regulatory**
  - `ai-ml-device-pathway-and-change-control` (DH-03.03.1.1). Which route fits an AI/ML device, how should planned model changes be handled (a predetermined change control plan), and what goes into the AI/ML parts of the submission?
  - `ai-ml-readiness-monitoring` (DH-03.03.1.2). Against the readiness criteria the person sets, how ready is the AI/ML device file, and what is missing?
- **DH-03.03.2 Global Harmonization**
  - `multi-region-regulatory-alignment` (DH-03.03.2.1). What does each target market require, where can one evidence plan or one file serve several markets (reliance, recognition, MDSAP), and how must a submission be adapted per region?
  - `cross-region-compliance-monitoring` (DH-03.03.2.2). Across the markets where the product is registered, which registrations, renewals or requirements have moved, and where is the product now out of step?
- **DH-03.03.4 Submission Excellence**
  - `regulatory-submission-and-dossier` (DH-03.03.4.1). How should the dossier and clinical evaluation be assembled for the chosen pathway, what does current guidance ask for, and how should agency interactions be prepared?
  - `submission-quality-and-outcome-monitoring` (DH-03.03.4.2). Against criteria the person sets, how good is the submission, and what happened to it (questions, holds, decision)?

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| "Is our app a medical device", intended use, device class, risk class | `regulatory-pathway-and-classification` | Classification and intended use start here for all software, AI included |
| 510(k), De Novo, PMA, CE route, UKCA, predicates, "who else got cleared" | `regulatory-pathway-and-classification` | Pathway choice and comparables |
| A register change, a recall or adverse event on a comparable, "has anything changed since we chose the route" | `regulatory-pathway-monitoring` | Watching the chosen route |
| Locked vs adaptive model, retraining, PCCP, AI Act duties for a device | `ai-ml-device-pathway-and-change-control` | AI/ML-specific route and change control |
| "Are we ready to file our AI device", AI/ML readiness review | `ai-ml-readiness-monitoring` | Readiness against the person's criteria |
| Launching in several countries, reliance, MDSAP, one file for many markets | `multi-region-regulatory-alignment` | Cross-market requirement mapping |
| Keeping registrations current across markets, renewals, divergence after launch | `cross-region-compliance-monitoring` | Multi-market tracking over time |
| Dossier structure, clinical evaluation report, pre-submission meeting, agency questions | `regulatory-submission-and-dossier` | Building the file |
| How a submission went, deficiency letters, approval outcome review | `submission-quality-and-outcome-monitoring` | Reviewing the file and its result |

Tie-breakers:

1. A classification question about an AI/ML product goes first to `regulatory-pathway-and-classification`; route to `ai-ml-device-pathway-and-change-control` once the question is about model change, PCCP or AI-specific duties.
2. A question about one market goes to the Regulatory Strategy heading; a question about two or more markets at once goes to Global Harmonization.
3. Design and execution come before monitoring. If nothing has been chosen or filed yet, the monitoring skill has nothing to check; send the person to its partner first.
4. If the request is vague ("help with regulatory"), ask one question: what is the product, which market, and is a route already chosen? Then route.

## Routing examples

- "We have a sleep app that suggests CBT-I exercises. Is it a medical device in the US and the EU?" Route to `regulatory-pathway-and-classification`. It lays out the classification arguments for the person's regulatory owner; it does not declare the class.
- "Our ECG algorithm retrains quarterly. How do we avoid a new 510(k) every time?" Route to `ai-ml-device-pathway-and-change-control` (planned change control).
- "We are CE marked. What do we need for Switzerland, the UK and Australia?" Route to `multi-region-regulatory-alignment`.
- "Our FDA reviewer sent an additional information request. Help me structure the response." Route to `regulatory-submission-and-dossier`. Any wording for the agency stops for the accountable owner.
- "Two competitors had recalls this quarter. Does that affect our route?" Route to `regulatory-pathway-monitoring`.
- "Give me a readiness score for our AI submission." Route to `ai-ml-readiness-monitoring`, and say that the readiness criteria and any score come from the person; the skill lays out the evidence against them.

## Related packs

Send the person to another pack when the question is not regulatory:

- **Quality** (`dh-quality`): design controls, risk management files, document and change control, QMS design, audits, CAPA and complaints. Start with `quality-management-capability-map`. A software change raises two questions: whether it needs a new submission (here) and how it is recorded and controlled (quality, `document-and-change-control`).
- **Market Access** (`dh-market-access`): reimbursement and payment after (or alongside) authorization. Skills: `coverage-pathway-and-access-strategy`, `coverage-strategy-and-access-rate-monitoring`, `payer-engagement-and-hta-submission`, `hta-submission-and-payer-engagement-monitoring`, `coding-pricing-and-payer-contracting`, `coding-pricing-and-contract-monitoring`, `outcomes-based-contracting`, `outcomes-contract-monitoring`. A regulatory clearance is not coverage; say so if the person conflates them.
- Other Digital Health packs, by pack name: `dh-clinical-validation` (study design and clinical evidence), `dh-cybersecurity` (device cybersecurity and privacy), `dh-software-engineering` (IEC 62304 development, V&V), `dh-data-science` (model development, responsible AI). Use each pack's own map or skill list.

## Downloading the regulatory expert

If the person wants the regulatory expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a class, a pathway or a pass rule, even as an example.
- If the person has named no owner for a decision the next skill will need, write "owner not named" and ask; never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests, including one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
