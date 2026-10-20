# B1 Review

Framework task: DH-03.02.4.2, Part B, task B1. Replaces the earlier "CAPA score" and "Ineffective CAPA" sections, which become steps here.

## What this task delivers

A review draft across open and recently closed CAPAs and the complaint operation: each CAPA's state (open, checked and criteria met, checked and criteria not met, evidence missing), the scores the people in the review gave, the owner the person names for each miss, and what goes back to DH-03.02.4.1 as new action. It answers "is our CAPA and complaint system working, and what do we do about what is not?"

Why it matters: FDA calls robust management review fundamental to the culture of quality it expects (QS16), and can now inspect management review records (QS15). A review that scores without evidence, or closes failed CAPAs by reopening them, will not hold.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | QA Manager, Software (V&V) |
| Skill | DH-03.02.4.2 Part B, Review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/effectiveness-and-trends.md`; rows QS15, QS16, QS19, QS47, R3 |
| Tools | A1 and A2 (and their helper) if not yet run |
| Prompt | This guide |
| Template | `assets/review-output.md` |
| Input | The request and its context: the CAPA list, A1 and A2 results, the people's scores, named owners, the person's review rules |
| Governance | `references/governance.md`; people score and name owners |

## The rule that shapes this task: people score

The people in the review score. The model lays out the evidence per CAPA and per complaint measure, records the scores people give, and ranks only those scores. It never assigns a score, a rating or an owner. If asked to propose a scoring scheme, it may, labeled "proposed", and does not apply it until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 per CAPA and A2 for the complaint log. If missing and needed, run them in short mode. A review without A2 says complaint handling was not reviewed.

### Step 2. List each CAPA's state

Keep the finding or complaint id. States: open; checked, criteria met; checked, criteria not met; evidence missing; no check performed. Do not score a closed-on-time CAPA as effective without the check (register rule). Note any complaint whose reportability decision is missing or late (from A2).

### Step 3. Write the review rules with the person

Ask for the scoring scale and what each point means, in their words, and the owner of each area. Offer this shape:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| CAPA effectiveness | "Every closed CAPA checked within its window" | A1 statuses |
| Recurrence | "No candidate recurrence on a version released after the fix" | A2 recurrence |
| Timeliness | "No reporting clock passed without a decision" | A2 timeliness |
| Ageing | "No complaint open beyond our limit" | A2 ageing |

Write them back for confirmation before checking anything. Without rules, give a factual summary and no verdict.

### Step 4. Record the scores

The people score each CAPA or area on their scale. Record each score with who gave it and the evidence row it rests on. Rank by their scores only. Where two scorers differ, show both.

### Step 5. Owner for each miss

For each criterion not met, check not performed, late decision, or ageing miss, record the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. State whether the cause looks the same or new only from what A1 and A2 show; otherwise "cause to be established".

### Step 6. Route back to DH-03.02.4.1

For each failed effectiveness check or candidate recurrence the person confirms: a new action in the sibling skill's B1, not a reopening of the old CAPA (register rule). A CAPA whose window passed with no check performed is routed the same way as a failed check: a new action in the sibling skill's B1. A late check may be run as evidence for that new action; it does not turn the closed CAPA into a pass. The finding stays open while the new action runs. For an undecided complaint past its clock, route to the sibling skill's A2 now. For an MDSAP-audited firm, note R3: new occurrences after accepted actions can bring a nonconformity for an ineffective corrective action system.

### Step 7. Management review link

If the review feeds management review, list the inputs it supplies (complaints, CAPA status), citing QS19, without stating ISO clause text.

## Build the output

Follow `assets/review-output.md`. Short mode: the state counts, the misses with owners, the new actions to open, the one decision needed. Full mode adds rules, scores with scorers, evidence and routing.

## Before you hand it over

- Every rule, score and owner is the people's, and the output says so.
- Every state cites its A1 or A2 evidence.
- Failed checks route to new actions; nothing is reopened or closed in the model's voice.
- Board or management review wording stops for the owner. If it leaves the conversation, call `verify.build_record` with the named clearer; otherwise label it an uncleared draft.

## Boundaries

- Reviews records and actions, never people's performance.
- No forecast of when a CAPA will become effective.
- 483 figures are context, never a score.
