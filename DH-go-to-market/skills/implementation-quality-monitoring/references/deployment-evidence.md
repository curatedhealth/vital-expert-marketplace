# Deployment evidence: what shows a bar item is met

Interpretive reference for tasks A1 and B1. Rows: `CS` in `customer-success-research.md`; `CP-UK` in `channels-partners-research.md`. The candidate bar items G1 to G10 are in `go-live-bar-elements.md`.

## 1. The register's rules for this competency

From the old register tasks (CF-12.02.02.1.2.1 to 1.2.3), kept as rules the person may adopt:

| Old task | Rule | How this skill applies it |
|---|---|---|
| Deployment check | Use the go-live bar for that site; set a pass only when each bar item has evidence; name the evidence (task log, data present, site confirmation). Do not pass a site on the project plan's status field. | Evidence seen per item, with an evidence id; a plan status field is never evidence. |
| Site score | Check each bar item and keep the evidence id. Mark missing evidence as failed, not as unknown-pass. Note items that slipped past the agreed go-live date. Do not rescore the bar after the site is live to make it pass. | "Missing evidence counts as not met" is the register starter rule: offered for the person to adopt, labeled as such. A score needs the person's scale. |
| Deployment repair | Name the open bar item and the owner; state whether the site stays in a limited launch; name the date the item will be rechecked. Do not close the deployment while a day-one workflow item is open. | Owner, limited launch and recheck date are the person's; the model never picks them. Closing the deployment with a day-one item open is a stop. |

## 2. Evidence classes

| Class | Meaning | Counts as evidence seen? |
|---|---|---|
| Seen | The record was shown in the conversation (task log extract, data check, signed agreement page, training record by role, site approver's confirmation) | Yes |
| Described | The person says it exists but it was not shown | No: "described, not seen" |
| Status field | A project plan or tracker marks the item done | No (register rule) |
| None | Nothing | No: "no evidence" |

Evidence ids are the person's (for example a ticket number or document reference). Records about people are by role; never named staff performance (worker stop rule).

## 3. Evidence types per candidate bar item

| Item | Evidence that shows it | Row |
|---|---|---|
| G1 Named roles completed one real task in the day-one workflow | Task log by role, date | Register method |
| G2 Data present and flowing as mapped | Data check against the data dictionary and flow map | CS64 |
| G3 Written data agreement signed before data flowed | Signed BAA (US) or Article 28 contract (EU), with signature date earlier than the first data flow | US: CS96. EU: CS110. UK and other markets: `[GAP]`; cite only the row for the site's market. |
| G4 Roles and access match job need | Role list against the access set | US: CS103, CS104 (HIPAA). Other markets: `[GAP]`. |
| G5 Users trained, matching validated training | Training record by role and the company's training approach | CS65, CS80 |
| G6 Silent mode done, where chosen | Silent-mode summary | CS60 |
| G7 Usage profile and reporting agreed | The agreed profile and reporting schedule | CS61, CS62 |
| G8 Load testing at expected scale | Load test summary | CS66 |
| G9 NHS deploying organization's clinical risk assessment and the developer's DCB0129 evidence | The deployer's assessment; the manufacturer's findings | CP-UK-09, CP-UK-10, CP-UK-06 (NHS England guidance pages); CS71 [WF] |
| G10 Pilot-site statement, if the site wants one | The statement on acceptability, performance, integration, no unintended harm, use as expected | CS59 |

## 4. Slippage

Slippage is counted from the baseline date the site agreed, to the done date or to the as-of date for an open item. A re-baselined date is shown beside it, never instead of it (register rule: do not rescore after go-live). Go-live slippage is go-live actual minus go-live planned.

## 5. Field safety events (external signal)

A recall or alert for the product during or after a deployment is a fact the person may weigh for a limited launch. It is not evidence about the deployment's quality, and no events is not evidence of no events (`tools.md`).
