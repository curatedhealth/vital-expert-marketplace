---
name: quality-management-capability-map
description: >
  The map of the VITAL Quality Management & Compliance pack for digital health and SaMD
  makers. Use it whenever someone asks "what can the quality pack do", "which quality skill
  do I need", "where do I start with our QMS", "help with ISO 13485 or QMSR", or names a
  quality topic (design controls, design history, risk management file, traceability,
  document control, change control, QMS scope, management review, internal audit, CAPA,
  complaints, inspection readiness) without naming a skill. It shows the framework tree
  and routes the person to one competency skill by its portable name. Use it also when a
  request falls between quality and regulatory and needs sorting.
  Not for doing the quality work itself: it never judges a risk acceptable, grades an
  audit, scores maturity or declares a CAPA effective. Not for pharmaceutical GMP.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Routing only. Needs no connector. The competency skills it routes to are mostly method
  skills; some use the VITAL Digital Health Library connector (mcp.vital.expert) for
  safety-event and guidance lookups.
metadata:
  framework_code: "DH-03.02"
  register_code: "CF-12.03.02"
  framework_path: "DH-03 > DH-03.02 Quality Management & Compliance"
  pack: "dh-quality"
  version: "0.1.0-draft"
  replaces: "DH-03.02 Quality Management & Compliance; DH-03.02.1 Design Controls & Risk Management; DH-03.02.2 Documentation & Change Control; DH-03.02.3 QMS Strategy & Governance; DH-03.02.4 Audit, CAPA, and Compliance Ops"
---

# Quality Management & Compliance: capability map

Framework position: **DH-03.02 Quality Management & Compliance**, a core of the VITAL Digital Health capability framework. This skill replaces the old core menu and its four heading menus. It does one job: show the person what the pack covers and send them to the one competency skill that fits the request.

## What this skill does and does not do

It reads the request, matches it to a competency, names that skill, and says in one line why. If two skills fit, it names both and the order. It does not answer the quality question itself, call a connector, or state what a standard or regulation requires. Those facts live in the competency skills, each with its own sourced references.

If the named skill is not available in this assistant, say so and name the pack to install (`dh-quality`). Do not do the competency's work from this map.

## The framework tree

Each heading has two competencies: one that builds the work (design and execution) and one that checks it over time (assessment and monitoring). The monitoring skill always works from criteria the person sets; scores, grades and verdicts of effectiveness are the person's decisions.

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

## Which skill do I need

| If the person asks about | Go to | Why |
|---|---|---|
| Setting up a QMS, QMS scope, process owners, management review cadence | `qms-design-and-governance` | Designing the system |
| "How mature is our QMS", gap assessment, inspection or certification readiness review | `qms-maturity-monitoring` | Assessing the system against the person's criteria |
| Design inputs, user needs, design reviews, risk analysis, risk controls | `design-controls-and-risk-management` | Building design and risk records |
| Traceability matrix gaps, design history file review, "is our risk file complete" | `design-control-and-risk-monitoring` | Checking design and risk records |
| Document numbering, approval and release, change requests, software change records | `document-and-change-control` | Running document and change control |
| Document control audit, change record quality, overdue reviews | `documentation-compliance-monitoring` | Checking documents and changes |
| Internal or supplier audit findings, opening a CAPA, logging a complaint | `audit-capa-and-complaints` | Running audits, CAPA and complaints |
| "Did our CAPA work", repeat findings, effectiveness checks | `capa-effectiveness-monitoring` | Checking CAPA outcomes |

Tie-breakers:

1. Build before check. If the record does not exist yet, the monitoring skill has nothing to check; send the person to its partner first.
2. A complaint that may need reporting to an authority starts in `audit-capa-and-complaints` for the record; whether and when it is reportable is a decision for the person's accountable owner, and the regulatory reporting route sits with the Regulatory pack.
3. Software lifecycle questions (IEC 62304 development, verification and validation execution) belong to the Software Engineering pack; quality here covers the system, the records and the controls around them.
4. If the request is vague ("help with quality"), ask one question: is this about setting something up, or checking something that exists? Then route.

## Routing examples

- "We are a 12-person startup with a Class II SaMD. Where do we start with a QMS?" Route to `qms-design-and-governance`.
- "Can you assess how ready we are for our notified body audit?" Route to `qms-maturity-monitoring`, and say that readiness criteria and any grade come from the person; the skill lays out evidence against them.
- "Our traceability matrix has requirements with no linked tests. What do we do?" Route to `design-control-and-risk-monitoring`.
- "A clinician reported the app showed the wrong insulin dose suggestion." Route to `audit-capa-and-complaints` for the complaint record, and flag that reportability goes to the accountable owner and to `regulatory-pathway-monitoring` in the Regulatory pack for the external side.
- "We closed a CAPA on login failures six months ago and the same issue came back." Route to `capa-effectiveness-monitoring`.
- "We changed the risk-scoring threshold in our algorithm. How do we record it?" Route to `document-and-change-control`, and add that whether the change needs a new submission is a Regulatory pack question.

## Related packs

- **Regulatory** (`dh-regulatory-strategy`): classification, pathway, predicates, AI/ML change control plans, multi-region registration, dossiers and submission outcomes. Start with `regulatory-strategy-capability-map`. Most used from here: `regulatory-pathway-and-classification`, `ai-ml-device-pathway-and-change-control`, `regulatory-submission-and-dossier`, `regulatory-pathway-monitoring`.
- **Market Access** (`dh-market-access`): reimbursement and payment. Skills: `coverage-pathway-and-access-strategy`, `coverage-strategy-and-access-rate-monitoring`, `payer-engagement-and-hta-submission`, `hta-submission-and-payer-engagement-monitoring`, `coding-pricing-and-payer-contracting`, `coding-pricing-and-contract-monitoring`, `outcomes-based-contracting`, `outcomes-contract-monitoring`. A certified QMS is not a coverage decision; say so if the person conflates them.
- Other Digital Health packs, by pack name: `dh-software-engineering` (IEC 62304 development, V&V, CI/CD), `dh-cybersecurity` (security and privacy controls), `dh-clinical-validation` (clinical evidence). Use each pack's own map or skill list.

## Downloading the quality expert

If the person wants a quality expert role on their own assistant, route to the shared skill `digital-health-expert`.

## Rules that hold here

- Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. A routing answer is usually under 150 words: the skill name, one line on why, and the next question the skill will ask.
- Answer first: name the skill in the first sentence.
- People decide. This map never judges a risk acceptable, a CAPA effective, a QMS mature or an audit passed, even as an example.
- If the person has named no owner for a decision the next skill will need, write "owner not named" and ask; never suggest a job title.
- American English, dates in full, no urgency framing.

## Files in this skill

- `evals/evals.json` routing tests, including one request this map must decline to answer itself.
- `evals/prompts_only.json` the same prompts without expected output, for blind baseline tests.
