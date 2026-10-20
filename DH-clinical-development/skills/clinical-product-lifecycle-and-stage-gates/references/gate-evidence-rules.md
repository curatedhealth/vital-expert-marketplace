# Gate evidence rules: what each gate type names, and how to check material against it

Interpretive reference for A2 (gate evidence plan) and B1 (stage gate record). Row prefixes: PL, TM, QS, CH. The gate criteria and the pass rule are always the person's (governance). This file says which source names which element, so a gate can be planned and read against named sources rather than a slide status.

## 1. Who attends a gate

| Fact | Rows |
|---|---|
| ISO 13485 Clause 7.3.5 (as FDA restates it) requires each design and development review to include representatives of the functions concerned with the stage under review plus other specialist personnel; the manufacturer chooses which individuals. | PL1 |
| FDA names manufacturing, quality assurance, purchasing, sales and servicing as functions that may give input at design review for a large manufacturer; small manufacturers may tailor the review. | PL6 |
| Independent review is valued but no longer a fixed QMSR attendee rule. | PL2, QS23 |
| IMDRF N41: independent review of clinical evidence (by someone not significantly involved in development and with nothing to gain) matters more for SaMD that treats or diagnoses in serious or critical situations; lower-risk review can be internal and is analogous to QMS design review. | PL66, PL67 |
| Treat independence as a risk-proportionate choice the person justifies, not a QMSR rule (research file "Changes and conflicts"). | PL1, PL2, PL66, PL67 |

The skill writes the attendees the person named, in their words. If none were named, it writes "attendees not named" and asks. It never fills a job title.

## 2. Gate types and the elements a source names

| Gate type (person's name may differ) | Elements a source names | Rows |
|---|---|---|
| Concept or intended use | Definition statement in three parts; general wellness two-factor test and disqualifiers as context; multiple function separation decided early in architecture | PL58, PL47, PL50, PL26 |
| Program theory and feasibility entry | Program theory written; key uncertainties named; refinement boundaries agreed; evaluability assessment considered | TM6, TM7, TM4, TM13, TM15 (DOI 10.1136/bmj.n2061) |
| Feasibility exit | Results against the predefined progression criteria (evaluation design and the intervention itself) | TM14, TM3 (DOI 10.1136/bmj.n2061) |
| Design review (any major decision point) | Design inputs met for intended use and user needs; verification data against functional and operational requirements, compatibility, safety, reliability and maintenance, labeling and regulatory requirements | PL4, PL5, PL3 |
| Software verification complete | Verification defined as each phase's outputs meeting that phase's inputs; testing summary by level; version history; unresolved anomalies with their impact | PL21, PL19, PL20 |
| Design validation and clinical evaluation | Validation that specifications conform to user needs and intended uses; clinical or performance evaluation; valid clinical association, analytical validation and clinical validation; for a product with no measurable patient outcome claimed, predictable reliable use and usability | PL22, PL7, PL63 to PL65, PL73 |
| First human use of a prototype | Prototypes in clinical studies ship under the IDE provisions of part 812; proportionality of proof before stage 1; learning-curve studies | PL8, PL113, PL119 (DOI 10.1097/SLA.0000000000004907) |
| Design transfer or release | Final design output in the design and development file starts the medical device file; IEC 62304 does not cover final release | PL10, PL105 |
| Pre-submission meeting (US) | A Pre-Sub asks specific questions and is not a pre-review; one Q-Sub per device at a time; the submitter drafts minutes within 15 days | PL39 to PL41 |
| DiGA application (Germany) | §§ 3 to 6 DiGAV met at application; certificates no older than 12 months; claimed care effect consistent with the intended purpose and published statements; sensitivity and specificity study where a diagnostic instrument is included; no trial listing for class IIb | PL80, PL91, PL92, PL93, PL79 |
| NHS England procurement | DTAC sections C1 to C4 and D1, current form per product version [WF] | PL97 to PL99 |
| Post-market change | A software change is a design change; risk-based assessment comes first; whether it needs a new 510(k) or is a significant change is answered by `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control | CH9, CH11, CH4, PL95 |

Every gate also asks the six MRC/NIHR core element questions where the product is a complex intervention (TM5). That is a proposal the person may adopt, not a source requirement for device gates.

## 3. Reading the person's material against a gate (used in B1)

For each criterion the person set:

1. Find the work product the criterion names in the person's material (document id, version, date).
2. Mark it: **present** (the item exists and its reference is given), **missing**, or **not measurable** `[GAP]` (the criterion cannot be checked from what was shared).
3. Never mark a criterion present from a status word alone ("done", "green", "in progress"). A status with no work product behind it does not count (old task rule: do not score a stage from a roadmap color).
4. Record the decision the person states (pass, hold, recycle, stop), the date and the person who decided, as given. The model never writes the decision.
5. Do not advance a stage because a calendar date arrived (old task rule). TM3 says repeating a phase is preferable to automatic progression while uncertainties remain.

## 4. What this skill never checks

- The content quality of a design control record, risk file or design and development file: `dh-regulatory-and-quality` design-controls-and-risk-management.
- Whether a change needs a submission or PCCP scope: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. Human-factors validation in a submission: `dh-regulatory-and-quality` regulatory-submission-and-dossier.
- Study protocol content and endpoints: `dh-clinical-development` study-protocol-and-endpoint-design.
