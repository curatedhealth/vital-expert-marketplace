# B1 Review and repair plan

Framework task: DH-03.02.3.2, Part B, task B1. Replaces the earlier "QMS repair" section and the one-line pass rule and owner rule.

## What this task delivers

A review draft that says, process by process, whether the QMS and its governance meet the rules the person set, where they do not, which repairs could respond, how the person scores those repairs, and who owns each one and which governance forum will see it. It answers "what do we fix first in our QMS, and who owns it?"

Why it matters: without rules written before the numbers, every review reopens what "good" means. A repair with no owner and no forum that will see it tends not to happen; the register's own rule is "do not raise the maturity claim while the process fails".

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Quality & Software Lifecycle Director (`quality-systems-director-software`) |
| Skill | DH-03.02.3.2 Part B, Review and repair plan |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/maturity-criteria.md`; `references/indicators.md`; `references/quality-systems-research.md` |
| Tools | `analytics.mcda` (counted, for repair options the person scored); A2's tools if no indicator run exists |
| Prompt | This guide |
| Template | `assets/review-and-repair-output.md` |
| Input | The request and its context; the person's rules, scores, weights and named owners; A1 findings and A2 indicators |
| Governance | `references/governance.md`; people set rules, score repairs and name owners |

## The rule that shapes this task: people decide, the owner rule holds

The person writes the rules, scores the repair options and names the owner of each repair and the forum that will see it. The model checks results against the rules, lays out repair options with their sourced basis, ranks only what was scored, and labels any suggestion "proposed". If no owner is named: "owner not named", and ask. Never suggest a job title. CAPA effectiveness, audit grades and risk acceptability are the person's decisions; the model lays out criteria and evidence.

## Workflow

### Step 1. Gather the evidence

Use A1 (findings per process) and A2 (indicators) from the conversation. If either is missing and needed, run it first in short mode. A review on one of them only says what was not reviewed.

### Step 2. Write the rules with the person

For each process or indicator in scope, ask for one or two rules, each with a number or a condition and an owner. Offer this shape, filled with the person's words:

| Rule type | Example shape (their words and numbers) | Checked against |
|---|---|---|
| Evidence | "A management review record for every half year" | A1 evidence |
| Closure | "No open CAPA past its due date" | A2 CAPA ageing |
| Repeat | "No repeat audit finding within three years" (MDSAP's window, QS47) | A2 findings |
| Effectiveness | "Every closed CAPA has a recorded effectiveness check" (EU4) | A2 CAPA |
| Timeliness | "Every EU serious incident reported within the Article 87 clock" (VG4 to VG6) | A2 events |

Write the rules back for confirmation. A process without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule met, missed, or not measurable `[GAP]`, with the number or the evidence behind it. A process is "meets your rules" if every rule is met, "misses" if any rule misses. Never average processes into one score (register starter rule).

### Step 4. Hypotheses, not causes

For each miss, list possible reasons as hypotheses to test, each with what would confirm it. Draw them from mechanisms the rows state, for example: open CAPA past due on change control may reflect changes implemented before a risk assessment (QS34 is the requirement it would breach; confirm from the change records); repeat findings may mean the correction did not hold (QS47; confirm from the CAPA effectiveness record). Never state a cause the data does not show.

### Step 5. Repair options

For each miss, list repair options with their basis, for example: write or revise a procedure; run the missing review and record it; verify effectiveness of closed CAPA and record it (EU4); reassess CAPA depth against risk (QS18); add the missing review input. Label suggestions "proposed".

If the person wants to rank repairs, ask for criteria (higher is better, for example "risk addressed", "effort avoided"), weights and 0 to 4 scores, then call `analytics.mcda`. Report values and contributions. Never score for them.

### Step 6. Owner and the forum that will see it

For each repair, record the owner the person names and the governance forum and date they choose to see it. If either is missing: "owner not named" or "forum and date not set"; ask. No dates proposed by the model, no urgency.

### Step 7. Stops

State what stops for the accountable owner: any maturity or effectiveness claim while a process misses; any notification (for example a late vigilance report, or a substantial QMS change to the notified body, EU24); closing a CAPA of record; any wording for the board or a regulator. When asked for such wording, draft only what the facts support and label it "draft for the owner".

## Build the output

Follow `assets/review-and-repair-output.md`. Answer first: which processes miss the person's rules, the repair with the owner, and the one decision needed. Short mode: 450 words maximum, counted without tables' source column; cut in this order: context paragraphs, secondary rules, full-mode sections; offer the full version in one line. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, score, owner and date is the person's, and the output says so.
- Every verdict cites the number or evidence behind it.
- Causes are hypotheses, labeled.
- No maturity or effectiveness claim; no averaging.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams, close CAPA, or grade audits.
- No forecast of inspection or audit outcomes.
- Drugs, biologics and wellness apps are out of scope.
