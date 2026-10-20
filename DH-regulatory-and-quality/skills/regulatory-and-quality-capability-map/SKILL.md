---
name: regulatory-and-quality-capability-map
description: >
  The map of the VITAL Regulatory & Quality pack for digital health products (SaMD, AI/ML
  devices, DTx, DiGA-type apps). Use it whenever someone asks "what can the regulatory and
  quality pack do", "which regulatory skill do I need", "which quality skill do I need",
  "where do I start with our FDA or EU MDR pathway", "where do I start with our QMS", "help
  with ISO 13485 or QMSR", or names a topic without naming a skill: classification,
  predicates, PCCP, multi-country registration, dossier, CER, submission outcome, design
  controls, risk file, traceability, document or change control, management review,
  internal audit, CAPA, complaints, inspection readiness. It shows the framework tree and
  routes to one competency skill and task. Use it when a request spans regulatory and
  quality, or touches market access. Not for doing the work: it never
  classifies, picks a pathway, drafts a submission, judges a risk acceptable, grades an
  audit, scores maturity or declares a CAPA effective. Not for drugs, biologics or GMP.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to use the VITAL
  Digital Health Library connector (mcp.vital.expert) for their evidence tasks; the
  quality method skills use it for safety-event and guidance lookups.
metadata:
  name: "regulatory-and-quality-capability-map"
  pack: "dh-regulatory-and-quality"
  framework_code: "DH-03.03; DH-03.02"
  register_code: "CF-12.03.03; CF-12.03.02"
  framework_path: "DH-03 > DH-03.03 Regulatory Strategy & Submissions; DH-03 > DH-03.02 Quality Management & Compliance"
  version: "0.1.0-draft"
  replaces: "Regulatory Strategy & Submissions pack map; Quality Management & Compliance pack map; DH-03.03 Regulatory Strategy & Submissions; DH-03.03.1 AI/ML Regulatory; DH-03.03.2 Global Harmonization; DH-03.03.3 Regulatory Strategy; DH-03.03.4 Submission Excellence; DH-03.02 Quality Management & Compliance; DH-03.02.1 Design Controls & Risk Management; DH-03.02.2 Documentation & Change Control; DH-03.02.3 QMS Strategy & Governance; DH-03.02.4 Audit, CAPA, and Compliance Ops"
---

# Regulatory & Quality: capability map

Framework position: two cores of the VITAL Digital Health capability framework, **DH-03.03 Regulatory Strategy & Submissions** and **DH-03.02 Quality Management & Compliance**. This skill replaces the two earlier pack maps (`regulatory-and-quality-capability-map`), both old core menus and their eight heading menus. It does one job: show the person what the pack covers and send them to the one competency skill, and where useful the one task, that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the regulatory or quality question itself, call a connector, or state any rule, class, pathway, fee, clock or what a standard requires. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-regulatory-and-quality`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that does the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria the person sets; it never sets its own pass rule, and scores, grades and verdicts of effectiveness are the person's decisions.

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

**DH-03.02 Quality Management & Compliance**

- **DH-03.02.3 QMS Strategy & Governance**
  - `qms-design-and-governance` (DH-03.02.3.1). What is in the scope of the quality system, who owns each process, which record each process produces, and how management review reads those records?
  - `qms-maturity-monitoring` (DH-03.02.3.2). Against the maturity criteria the person sets, where does the quality system stand, and which gaps should be repaired first?
- **DH-03.02.1 Design Controls & Risk Management**
  - `design-controls-and-risk-management` (DH-03.02.1.1). How are design inputs written, how are risks identified and controlled, and how is a design review recorded?
  - `design-control-and-risk-monitoring` (DH-03.02.1.2). Do the design controls and the risk file hold together (traceability from input to verification to risk control), and where do they need repair?
- **DH-03.02.2 Documentation & Change Control**
  - `document-and-change-control` (DH-03.02.2.1). How is a document brought under control, how is a change recorded and assessed, and how are obsolete copies withdrawn?
  - `documentation-compliance-monitoring` (DH-03.02.2.2). Against the criteria the person sets, are the controlled documents and change records complete, and what needs repair?
- **DH-03.02.4 Audit, CAPA, and Compliance Ops**
  - `audit-capa-and-complaints` (DH-03.02.4.1). How is an audit finding written, how is a CAPA plan built from it, and how is a complaint recorded and assessed?
  - `capa-effectiveness-monitoring` (DH-03.02.4.2). Against the effectiveness criteria the person sets, did the CAPA work, and what is done when it did not?

## Folded headings

The old menus are gone. A request that names one goes here:

| Old menu | Go to |
|---|---|
| DH-03.03 Regulatory Strategy & Submissions, DH-03.02 Quality Management & Compliance | This map |
| DH-03.03.3 Regulatory Strategy | `regulatory-pathway-and-classification`, then `regulatory-pathway-monitoring` |
| DH-03.03.1 AI/ML Regulatory | `ai-ml-device-pathway-and-change-control`, then `ai-ml-readiness-monitoring` |
| DH-03.03.2 Global Harmonization | `multi-region-regulatory-alignment`, then `cross-region-compliance-monitoring` |
| DH-03.03.4 Submission Excellence | `regulatory-submission-and-dossier`, then `submission-quality-and-outcome-monitoring` |
| DH-03.02.3 QMS Strategy & Governance | `qms-design-and-governance`, then `qms-maturity-monitoring` |
| DH-03.02.1 Design Controls & Risk Management | `design-controls-and-risk-management`, then `design-control-and-risk-monitoring` |
| DH-03.02.2 Documentation & Change Control | `document-and-change-control`, then `documentation-compliance-monitoring` |
| DH-03.02.4 Audit, CAPA, and Compliance Ops | `audit-capa-and-complaints`, then `capa-effectiveness-monitoring` |

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
| Setting up a QMS, QMS scope, process owners, management review cadence | `qms-design-and-governance` | Designing the system |
| "How mature is our QMS", gap assessment, inspection or certification readiness review | `qms-maturity-monitoring` | Assessing the system against the person's criteria |
| Design inputs, user needs, design reviews, risk analysis, risk controls | `design-controls-and-risk-management` | Building design and risk records |
| Traceability matrix gaps, design history file review, "is our risk file complete" | `design-control-and-risk-monitoring` | Checking design and risk records |
| Document numbering, approval and release, change requests, software change records | `document-and-change-control` | Running document and change control |
| Document control audit, change record quality, overdue reviews | `documentation-compliance-monitoring` | Checking documents and changes |
| Internal or supplier audit findings, opening a CAPA, logging a complaint | `audit-capa-and-complaints` | Running audits, CAPA and complaints |
| "Did our CAPA work", repeat findings, effectiveness checks | `capa-effectiveness-monitoring` | Checking CAPA outcomes |

## Task index

When the request already matches one task, name the skill and the task together.

| Skill | Tasks |
|---|---|
| `regulatory-pathway-and-classification` | A1 Intended use and classification; A2 Pathway precedents; B1 Pathway strategy |
| `regulatory-pathway-monitoring` | A1 Authorization and register tracking; A2 Safety signal review; B1 Performance review |
| `ai-ml-device-pathway-and-change-control` | A1 AI/ML pathway map; A2 Change control plan; B1 AI/ML submission plan |
| `ai-ml-readiness-monitoring` | A1 Readiness check; A2 Post-market change and performance tracking; B1 Performance review |
| `multi-region-regulatory-alignment` | A1 Cross-jurisdiction requirement map; A2 Harmonized evidence plan; B1 Regional submission adaptation |
| `cross-region-compliance-monitoring` | A1 Market status by region; A2 Regulatory change tracking; B1 Performance review |
| `regulatory-submission-and-dossier` | A1 Submission content map; A2 Clinical evaluation support; B1 Dossier assembly and agency plan |
| `submission-quality-and-outcome-monitoring` | A1 Dossier completeness check; A2 Agency questions and decision tracking; B1 Performance review |
| `qms-design-and-governance` | A1 QMS scope and process map; A2 Process ownership and governance cadence; B1 Operating model decision |
| `qms-maturity-monitoring` | A1 Maturity check; A2 Governance effectiveness indicators; B1 Review and repair plan |
| `design-controls-and-risk-management` | A1 Design inputs and traceability; A2 Risk management file; B1 Design review and risk acceptability |
| `design-control-and-risk-monitoring` | A1 Traceability and design control check; A2 Risk control effectiveness from post-market data; B1 Review and repair plan |
| `document-and-change-control` | A1 Document control setup; A2 Change impact assessment; B1 Change decision record |
| `documentation-compliance-monitoring` | A1 Document check; A2 Change control quality; B1 Review and repair plan |
| `audit-capa-and-complaints` | A1 Audit finding write-up; A2 Complaint handling and vigilance; B1 CAPA plan |
| `capa-effectiveness-monitoring` | A1 CAPA effectiveness check; A2 Complaint and recurrence trends; B1 Review |

Several monitoring skills share a task name ("Performance review", "Review and repair plan"). If the person names only the task, ask which product area it concerns, then route by the heading.

## Tie-breakers

1. Build before check. If nothing has been chosen, filed or recorded yet, the monitoring skill has nothing to check; send the person to its partner first.
2. A classification question about an AI/ML product goes first to `regulatory-pathway-and-classification`; route to `ai-ml-device-pathway-and-change-control` once the question is about model change, PCCP or AI-specific duties.
3. A question about one market goes to the Regulatory Strategy heading; a question about two or more markets at once goes to Global Harmonization.
4. A software change raises two questions. Whether it needs a new submission goes to `ai-ml-device-pathway-and-change-control` (AI/ML) or `document-and-change-control` task A2 (other software). How it is recorded and controlled goes to `document-and-change-control`. Name both when the person asks one.
5. A complaint that may need reporting to an authority starts in `audit-capa-and-complaints` task A2 for the record and the clocks; whether and when it is reportable is a decision for the person's accountable owner. Effects on the chosen pathway or comparables go to `regulatory-pathway-monitoring`.
6. Software lifecycle questions (IEC 62304 development, verification and validation execution) belong to the Software Engineering pack; quality here covers the system, the records and the controls around them.
7. If the request is vague ("help with regulatory", "help with quality"), ask one question: what is the product and market, and is this about setting something up or checking something that exists? Then route.

## Routing examples

- "We have a sleep app that suggests CBT-I exercises. Is it a medical device in the US and the EU?" Route to `regulatory-pathway-and-classification`, task A1. It lays out the classification arguments for the person's regulatory owner; it does not declare the class.
- "Our ECG algorithm retrains quarterly. How do we avoid a new 510(k) every time?" Route to `ai-ml-device-pathway-and-change-control`, task A2 (planned change control).
- "We are CE marked. What do we need for Switzerland, the UK and Australia?" Route to `multi-region-regulatory-alignment`.
- "Our FDA reviewer sent an additional information request. Help me structure the response." Route to `regulatory-submission-and-dossier`. Any wording for the agency stops for the accountable owner.
- "Two competitors had recalls this quarter. Does that affect our route?" Route to `regulatory-pathway-monitoring`, task A2.
- "Give me a readiness score for our AI submission." Route to `ai-ml-readiness-monitoring`, and say that the readiness criteria and any score come from the person; the skill lays out the evidence against them.
- "We are a 12-person startup with a Class II SaMD. Where do we start with a QMS?" Route to `qms-design-and-governance`.
- "Can you assess how ready we are for our notified body audit?" Route to `qms-maturity-monitoring`, and say that readiness criteria and any grade come from the person.
- "Our traceability matrix has requirements with no linked tests. What do we do?" Route to `design-control-and-risk-monitoring`, task A1.
- "A clinician reported the app showed the wrong insulin dose suggestion." Route to `audit-capa-and-complaints`, task A2, for the complaint record; reportability goes to the accountable owner, and `regulatory-pathway-monitoring` covers the external side.
- "We closed a CAPA on login failures six months ago and the same issue came back." Route to `capa-effectiveness-monitoring`.
- "We changed the risk-scoring threshold in our algorithm. How do we record it?" Route to `document-and-change-control`, and add that whether the change needs a new submission is a question for `ai-ml-device-pathway-and-change-control`.

## Not for

Not for work outside regulatory and quality. Send the person to the sibling pack, by pack and skill:

- Reimbursement, coverage, coding, pricing, HTA and payer work: `dh-access-and-value`, starting with `access-and-value-capability-map`; most used from here are `coverage-pathway-and-access-strategy`, `payer-engagement-and-hta-submission`, `coding-pricing-and-payer-contracting` and `outcomes-based-contracting`, each with its monitoring partner (`coverage-strategy-and-access-rate-monitoring`, `hta-submission-and-payer-engagement-monitoring`, `coding-pricing-and-contract-monitoring`, `outcomes-contract-monitoring`). A regulatory clearance or a certified QMS is not coverage; say so if the person conflates them.
- Study design and clinical evidence generation: `dh-clinical-development`, starting with `clinical-development-capability-map`; most used from here are `study-protocol-and-endpoint-design` and `literature-and-real-world-evidence-review`.
- Device cybersecurity and privacy controls: `dh-cybersecurity`, starting with `DH-04-02-Cybersecurity---Privacy`.
- Model development and responsible AI: `dh-data-science`, starting with `DH-01-04-Data-Science---AI-ML`.
- IEC 62304 development, verification and validation, CI/CD: `dh-software-engineering`; use that pack's own map or skill list.

## Downloading the regulatory or quality expert

If the person wants the regulatory or quality expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never proposes a class, a pathway or a pass rule, and never judges a risk acceptable, a CAPA effective, a QMS mature or an audit passed, even as an example.
- If the person has named no owner for a decision the next skill will need, write "owner not named" and ask; never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests for both halves, one request that spans both, and one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
