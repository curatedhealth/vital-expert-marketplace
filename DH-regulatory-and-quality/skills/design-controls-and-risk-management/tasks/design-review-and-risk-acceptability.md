# B1 Design review and risk acceptability

Framework task: DH-03.02.1.1, Part B, task B1. Replaces the earlier "Design review record" task (CF-12.03.02.1.1.3).

## What this task delivers

A design review pack: the evidence for each design input and risk control in scope, the open items, each residual risk laid out against the person's own acceptability criteria, and a record page with empty decision cells for the reviewers. It answers "are we ready for the design review", "prepare the review pack", and "is this residual risk acceptable". The last question is answered by laying out the evidence and stopping for the owner: the model never says a risk is acceptable.

Why it matters: the review is where people commit. A pack that separates evidence from open items, and leaves the decisions visibly to named people, produces a record that survives inspection. A pack in which the tool has already "accepted" the risks produces a record nobody actually decided.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Product Development Lead (`product-development-lead`) |
| Skill | DH-03.02.1.1 Part B, Design review and risk acceptability |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/risk-management-requirements.md` (acceptability rows EU12, EU13, EU16, EU18, ST4); `references/design-control-requirements.md` (QS23, QS24) |
| Tools | None beyond A1 and A2. `scripts/trace_check.py` if the trace has changed since A1 |
| Prompt | This guide |
| Template | `assets/design-review-output.md` |
| Input | The request and its context: review scope (stage, release, change), A1 and A2 results, the person's acceptability policy, the named reviewers and the named owner |
| Governance | `references/governance.md`; people decide acceptability, the review outcome and whether a release waits |

## The rule that shapes this task: people decide

Acceptability is judged against the person's own policy, because ISO 14971 does not set acceptable levels (ST4) and the MDR frames acceptability as risk weighed against benefit at the state of the art (EU12, EU18). The model lays out evidence, computes where a residual risk falls against criteria the person supplied, and lists what is still open. The reviewers record accept, accept with actions, or change required. The owner decides whether a release waits. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

Where a residual estimate equals the limit in the person's criterion, write "at the limit" in "Where it falls" for every such row, consistently. Write "inside" only when the estimate is strictly below the limit.

## Workflow

### Step 1. Fix the scope and the people

Ask, if not given: what is under review (a design stage, a release, a change), who the reviewers are, and who owns the decision. Who must attend is set by the person's own procedure under ISO 13485 Clause 7.3.5; the QMSR dropped the old explicit independent-reviewer rule (QS23). Do not tell the person who to invite.

### Step 2. Gather the evidence

Use A1 (trace findings) and A2 (hazard table) from the conversation. If either is missing, run it first in short mode, or say the review covers only one side. If the trace changed, rerun `scripts/trace_check.py`.

### Step 3. Lay out each item

For each design input and each risk control in scope: the evidence (verification or validation id and result, from the person's files), the open items (G and R findings from A1), and the source of each fact. An item with a failed or missing result is an open item, never "nearly done".

### Step 4. Lay out each residual risk

For each hazard: residual severity and probability as the person gave them, the person's criterion, where the risk falls against it (computed only from their criterion), the control types used and whether design controls were exhausted before information for safety (EU16), and the benefit the person states. Leave the decision cell empty. If the person has no written criterion, say the risk cannot be laid out against one and that writing it is the first open item.

### Step 5. Lay out the overall residual risk

The MDR asks for the overall residual risk to be acceptable against the evaluated benefits (EU18). Put the person's benefit statement and the residual risks side by side. Do not write the conclusion.

### Step 6. Stop for the owner

Write the record page: date, scope, reviewers as named, items reviewed, and for each item an empty outcome cell (accept / accept with actions / change required) and an action owner cell. State the open items that would block a release under the person's own rule, if they gave one; otherwise list the open items and say the owner decides whether the release waits. Name where the record will be filed in the design and development file (QS24); if the person has not said, write `[GAP]` and ask. A review held only in a chat is not a record (earlier task wording).

If the person asks the model to declare a risk acceptable or the release ready, decline that part in one line and give the draft for the owner instead: the evidence, the open items, and the wording the facts support ("residual risk for HZ-03 falls inside the criterion in policy section X; RC-03 verification is open"), labeled "draft for the owner".

## Build the output

Follow `assets/design-review-output.md`. Short mode: what is ready, what is open, and the decisions the reviewers must take. Full mode: the item-by-item evidence, the residual-risk layout, and the record page.

Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line.

## Before you hand it over

- Every evidence cell cites the person's record id; every rule cites a row id.
- Decision and owner cells are empty or hold what the person said.
- No sentence states that a risk is acceptable, a hazard closed, or a release ready.
- The record is a draft for the owner. If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft. AI-assisted draft.

## Boundaries

- The model does not accept risks, approve designs or release software.
- No acceptability criteria of the model's own; no benefit claim the person did not make.
- Device class and pathway statements route to the regulatory owner.
