# Change control quality checks: what each check rests on

Interpretive reference for task A2 and `scripts/change_log_check.py`. Rows: QS and CH in `QUALITY_SYSTEMS.md`; QX in `supplementary-rows.md`. Read on 19 October 2026.

## The checks

| Code | Check | What the source says | Row |
|---|---|---|---|
| NO_ASSESSMENT | A change has no impact assessment reference | FDA's Change Control inspection area exists "to ensure changes are adequately evaluated for risk and impact on products and processes prior to implementation" | QS34 |
| NO_RATIONALE | An assessment concludes with no rationale | FDA: decide to submit or "document the basis for concluding that submission of a new 510(k) is not required"; MDCG 2020-3: the manufacturer justifies and documents the outcome | QX14, QX22 |
| IMPL_BEFORE_APPROVAL | Implemented (or released) before the approval date, or implemented with no approval date recorded | Changes are evaluated "prior to implementation" | QS34 |
| IMPL_BEFORE_ASSESSMENT | Implemented before the assessment date | Same | QS34 |
| NO_APPROVER | Approval date without an approver name, or the reverse | The register task "Change record" asks for the approver and the date (pack method, class O) | O |
| NO_RISK_REVIEW | Risk file review not recorded for a change marked as touching a hazard | Risk documentation is reviewed when new information emerges; investigators use it throughout | QS22, QS31 |
| DECISION_WITHOUT_BASIS | A "no submission" or "not significant" decision with an empty rationale | As NO_RATIONALE | QX14, QX22 |
| NOT_ASSESSED_IN_AGGREGATE | Several changes to the same item since the last clearance with no aggregate assessment reference | Each change is assessed separately and in aggregate; cumulative changes can cross the threshold | QX12, QX13 |
| MISSING_DATE | A date the check needs is blank or unreadable | Not measurable; reported as `[GAP]` | none |

## What the checks do not do

- They do not judge whether an assessment's conclusion was right. That is the owner's call, reviewed in B1 with the sibling skill's question sheet.
- They do not set a pass rate. The person sets any threshold; the script reports counts and rates only.
- They do not grade. MDSAP grades nonconformities 1 to 5 from QMS impact, repeat, missing procedure with failure to implement, and release of nonconforming devices (QS44, QS45); a grade is the auditor's decision. B1 lays these criteria out for people who choose to score with them.

## Why these checks first

Design change procedures drew 48 FDA 483 citations in FY 2025 (QS54, measured; QS regulation numbering). That is context for where inspectors have looked, not a target.
