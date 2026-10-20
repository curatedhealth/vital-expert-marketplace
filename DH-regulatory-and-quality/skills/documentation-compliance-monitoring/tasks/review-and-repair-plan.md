# B1 Review and repair plan

Framework task: DH-03.02.2.2, Part B, task B1. Replaces the earlier "Document score" and "Document repair" sections and their owner rule.

## What this task delivers

A repair plan for the findings from A1 and A2: each finding scored by the person's people on criteria they choose, ranked by those scores only, with the owner and due date the person names and the repair that answers it (remove an obsolete copy, correct a citation, write a late assessment dated today, review the risk file, consider whether a CAPA is warranted). It answers "what do we fix first, who fixes it, and how?"

Why it matters: FDA expects CAPA depth to match the size of the problem and the risk (QS18), and MDSAP treats a repeat nonconformity as a sign that a corrective action was not adequately taken (QS47). A plan that fixes the record but not the process that produced it brings the same finding back.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (`quality-assurance-manager-software`) |
| Skill | DH-03.02.2.2 Part B, Review and repair plan |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/required-records.md`; `references/change-control-checks.md`; `references/QUALITY_SYSTEMS.md` (QS18, QS44 to QS47) |
| Tools | `verify.build_record` at clearance only |
| Prompt | This guide |
| Template | `assets/review-and-repair-plan-output.md` |
| Input | The findings; the scores the person's people give; named owners and dates |
| Governance | `references/governance.md`; people score and name owners |

## Read the request

- **Which findings.** From A1, A2 or both, from the conversation. If neither exists, run the one needed in short mode first.
- **Who scores.** The person, or a group they name. The model does not score.
- **Purpose.** Internal clean-up, inspection readiness, or a response to an observation. A response to an FDA 483 or a notified body finding stops for the owner (governance).

## The rule that shapes this task: people score

People score each finding; the model ranks only what they scored. The model may lay out scoring criteria with their source, for example MDSAP's grading inputs: QMS impact direct 3 or indirect 1, plus 1 each for a repeat, for a missing procedure combined with failure to implement, and for release of nonconforming devices (QS45), with clauses 4.1 to 6.3 indirect except 4.2.3 (medical device file, direct), and 6.4 to 8.5 direct except 8.2.4 (internal audits, indirect) (QS46). The person decides whether to use them. The model never assigns a grade, a severity or a priority itself. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Workflow

### Step 1. Lay out the findings with their facts

One line per finding: what it is, the evidence (dates, fields, list date), the rule row, and the facts that bear on scoring (does the change touch a hazard; was the device released; has the same finding appeared before, by the person's records). No adjectives that pre-judge severity.

### Step 2. Agree the criteria and collect scores

Ask how the person wants to score. Offer the MDSAP inputs (QS45) or a simple scale the person defines. Record each score with who gave it. Unscored findings stay unranked and are listed as such.

### Step 3. Rank what was scored

Order by the person's scores. Where two findings tie, say so; do not break the tie. If the person used weights, say which weight change would swap adjacent findings, if any.

### Step 4. Propose repairs, labeled

For each finding, lay out the repair that answers it, marked "proposed":

| Finding | Proposed repair | Basis |
|---|---|---|
| Obsolete copy in use; two versions marked current | Withdraw the obsolete copy; record the withdrawal | Pack method (A1 lifecycle) |
| Submission or file cites a superseded version | Identify the current version; the owner decides whether the filed document needs correction | Pack method; filing stops for the owner |
| No assessment, or assessment without rationale | Write the assessment now, dated today, stating it is late; walk the sibling skill's question sheet | QS34, QX14, QX22 |
| Implemented before approval | Record the facts in a new dated entry; the owner decides whether a CAPA is warranted, proportionate to the risk | QS34, QS18 |
| Hazard-touching change without risk review | Review the risk file for the change | QS22 |
| No aggregate assessment | Assess the changes to the item together | QX12, QX13 |
| Required record missing | Create it under the controlled lifecycle; for complaint or MDR records, check the required content | QS11, VG21, QX3 |

Never propose editing a past entry, backdating, or reconstructing an approval.

### Step 5. Owners and dates

Take each owner and due date from the person. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

### Step 6. Stop for the owner and clear

Present the plan as a draft. Responses to regulators, CAPA decisions and any "compliant" statement stop for the owner. If the plan leaves the conversation, ask who clears it and call `verify.build_record` with that person's name.

## Build the output

Follow `assets/review-and-repair-plan-output.md`. Short mode: the top findings by the person's scores, each with owner, repair and date; the unscored findings count; the one decision needed. 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every score is attributed to a named person; no score is the model's.
- Every owner and date is the person's, or "owner not named".
- Every repair is labeled "proposed" and none alters a past record.
- CAPA decisions and regulator responses are marked as stops for the owner.
- The record is labeled AI-assisted draft; cleared by a named person or uncleared.

## Boundaries

- Plans repairs; does not run the CAPA system or judge CAPA effectiveness (DH-03.02.4).
- Does not grade findings as an auditor would.
- Does not assign blame to people or teams.
