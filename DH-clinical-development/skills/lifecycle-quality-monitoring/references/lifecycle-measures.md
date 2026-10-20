# Lifecycle measures and post-market inputs

Interpretive reference for A1 (defining measures), A2 (reading stage status) and B1 (repair). Row prefixes: PL, TM, QS, CH. Rows marked [PAPER] carry their DOI; [WF] rows were read through a summarizing fetch tool.

## The rule that shapes this reference

No source read for this skill sets a measure, a target or a threshold for stage health, cycle time or gate quality. The sources say what a stage move must rest on (a decision against criteria set in advance, a record that shows it) and which events reopen a stage. The person writes the measures; the skill says which source each measure leans on, and counts what the log shows. A count is never a score.

## 1. What a healthy stage move rests on

| Basis for a measure | What the source says | Rows |
|---|---|---|
| Criteria set before the gate | Feasibility tests predefined progression criteria; refinement boundaries are agreed at the start of each phase | TM14, TM13 (DOI 10.1136/bmj.n2061) |
| No automatic progression | Repeating a phase is preferable to automatic progression if uncertainties remain unresolved | TM3 (DOI 10.1136/bmj.n2061) |
| Revisit before moving | The six core elements are revisited "especially before moving between phases" | TM4 (DOI 10.1136/bmj.n2061) |
| Decision at a review | Design reviews at major decision points | PL5 |
| A record behind the move | The design and development file contains or references all records needed to show design compliance, including the plan and procedures | PL9, QS24 |
| What the review checked | Inputs met for intended use and user needs; verification data against requirements | PL4 |
| Who took part | Functions concerned with the stage; independence a risk-proportionate choice | PL1, PL2, QS23, PL66, PL67 |

Moves that do not count as evidence of a healthy move (from the old task rules and these rows): a status color or slide with no work product behind it; a stage advanced because a date arrived; a work product marked in progress and then passed with no decision recorded. These are proposals the person may adopt as measures, labeled "proposed".

## 2. Countable facts in a gate log (what `scripts/gate_log_check.py` computes)

| Fact | How it is computed | It is not |
|---|---|---|
| Owed items per stage, accepted, missing, in progress, waived | Counted from the person's log statuses | A quality score |
| Days open | First opened date to the last decision date if the stage has no missing or in-progress item, else to the read date | A target or a delay judgment |
| F1 accepted with no evidence reference | Status "accepted", evidence_ref empty | Proof the item does not exist |
| F2 accepted with no named decider or decision date | | |
| F3 missing, owner not named | | |
| F4 next stage started while an item is missing or in progress | next_stage_started_on filled on that row | A judgment that the start was wrong |
| F5 missing or in progress with no reread date | | |

## 3. Post-market inputs that reopen a stage

| Input | What the source says | Rows |
|---|---|---|
| Change to the definition statement | Recategorize against the new statement | PL59 |
| Any software change | A software change is a design change; risk-based assessment comes first; whether a new 510(k) is needed follows FDA's questions | CH9, CH11, CH12 to CH16 |
| EU significant change (legacy devices) | A significant change needs a change to design or intended purpose and significance; software assessed with chart C | CH4, CH5 |
| DiGA change | Significant changes alter published data or materially affect safety, function, quality, data protection and security or the care-effect evidence; minor changes bundled, up to four times a year; BfArM provides a checklist | PL95, PL96 |
| Multiple function product | A change to an other function is assessed for impact on the reviewed function | PL29 |
| Clinical evaluation update | Complaints, PMCF or PMPF, real-world performance data, user feedback and new research feed the continuous update | PL68, PL76 |
| Module-level change | Clinical performance may be confirmed for changed modules only where modules are independent | PL75 |
| Risk file | Reviewed and updated when unforeseen risks or new information emerge | QS22 |
| Change control in inspection | Changes are evaluated for risk and impact before implementation | QS34 |
| Register events | FDA recalls and MAUDE counts from `regulatory-dh.search_safety_events`; MAUDE counts are reports, not confirmed events | `references/tools.md` |

Whether an input requires a submission, a notification or a new classification goes to `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control. Complaint handling and CAPA records are `dh-regulatory-and-quality` audit-capa-and-complaints. This skill names the input as the record states it, writes the stage the person says it reopens (or "your call"), and routes; it never judges the record's relevance to the person's product.

## 4. Not sourced

- Benchmarks for stage duration, gate pass rates or cycle time in digital health: none read `[GAP]`. Never compare the person's days open with an "industry norm".
- Any scoring scale for stage quality: none read `[GAP]`; the old "stage score" becomes counts plus the person's rule.
