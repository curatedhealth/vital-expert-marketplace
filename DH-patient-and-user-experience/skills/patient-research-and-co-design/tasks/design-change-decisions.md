# B1 Design change decisions

Framework task: DH-02.03.1.1, Part B, task B1. Replaces the register task "Design change from co-design" (CF-12.02.03.1.1.3) and the old one-line pass rule and miss owner sections.

## What this task delivers

A decision table for the repeated points from A2: for each, the participants' evidence, any sourced constraint that bears on it, the decision the person's owner records (accept, defer or refuse), the reason, the linked design change and the product version that will show it; a ranking of accepted or candidate changes only if the person scored them; and the points that stop for an owner. It answers "which of the things patients told us do we change, and how will we know it shipped?"

Why it matters: a point that is never decided stays in the transcript (register, CF-12.02.03.1.2.3). An accepted change without a version cannot be traced later (R-12). A change that touches a safety constraint, accepted quietly, moves risk without a decision (R-13).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Patient Experience Designer (`patient-experience-designer`) |
| Skill | DH-02.03.1.1 Part B, Design change decisions |
| Workflow | The steps below |
| Knowledge | `references/insight-log.md`; `references/co-design-method.md`; A2 capture and tally; rows R-10 to R-13, PE-06, PE-22 to PE-27 |
| Tools | `scripts/insight_tracker.py status` (optional); `analytics.rice` or `analytics.mcda` (counted, optional, on the person's scores); `verify.build_record` (counted, when cleared) |
| Prompt | This guide |
| Template | `assets/design-change-decisions-output.md` |
| Input | The request and its context: the insight log, the person's rule for repeated points, decisions already taken, owners, any safety constraints the person's risk file names, scores if they want a ranking |
| Governance | `references/governance.md`; people decide and score, the connector ranks, owners clear |
| Catalogue job | none (checked against list_jobs, 19 October 2026). No catalogue job covers this task; the direct steps below are the method. partner-prioritization runs the same ranking calculators but is scoped to partners and indications; call the calculator directly. |

## The rule that shapes this task: people decide

Accept, defer and refuse are the owner's decisions. The model sets out the evidence per point, names any constraint a row or the person's own risk file states, and records the decision the person gives. It may write a proposed decision with its reason, labeled "proposed", if asked. It never ranks what the person did not score, and never calls a change "recommended".

## Read the request

- **Which points.** Points that meet the person's repeated-point rule (R-10 if adopted). Others may be added by the person.
- **Decisions so far.** From `insights.csv` or the message.
- **Owners.** Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.
- **Safety constraints.** Ask whether any point touches something the risk file or clinical safety owner controls (alarms, thresholds, dosing, out-of-range displays). The model does not decide what is safety-relevant; it asks and flags.
- **Ranking.** Only if the person wants one and gives scores.
- **Mode.** Short for a direct question; full for a decision log.

## Workflow

### Step 1. Lay out each point

Per insight: summary, distinct patient-side participants and sessions (from A2), requests versus observations, one or two quotes. Add sourced context only where a row bears on it, for example: a "which would you rather" point that the team wants to use with FDA is patient preference information only if the regulatory owner says so (PE-23, PE-24). Remind once that counts describe these participants (PE-06).

### Step 2. Record the decision

For each point: accept, defer or refuse as the person or their owner gives it, with the reason (R-11). For accept, the linked change id and the product version (R-12). For defer, what it waits on. For refuse, the reason in plain words. If no decision is given, status stays "open" and the point goes to Step 5.

### Step 3. Check the log

With code execution: `python3 scripts/insight_tracker.py status insights.csv captures.csv --as-of YYYY-MM-DD`. Report: decided without reason or owner, accepted without linked change or version, accepted and marked as touching a safety constraint, open points with their age since first capture and any past the person's own decision date.

### Step 4. Rank only what they scored (optional)

If the person wants an order for accepted or candidate changes, ask for their numbers. RICE: reach, impact (0.25, 0.5, 1, 2 or 3), confidence as a whole-number percent, effort. Call `analytics.rice` with `initiatives` (read `references/tools.md`: confidence is read as a percent). Report the order and the scores as the tool echoed them. For weighted criteria instead, use `analytics.mcda` with 0 to 4 scores and weights summing to 1. Say: "The order reflects your scores; it is not a recommendation."

### Step 5. Open points and stops

List open points with owner (or "owner not named") and the date the person sets for writing the decision; propose no dates. List stops: any accepted change touching a safety constraint (R-13) goes to the person's clinical safety or risk owner; patient-facing copy or wording implying clinical benefit goes to its owner with editorial countersign; any regulatory use goes to the regulatory owner.

## Build the output

Follow `assets/design-change-decisions-output.md`. Answer first: what was decided, what is open, and what stops for an owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every decision, reason, owner, score and date is the person's, and the output says so.
- Every accepted change has a change id and a version, or the gap is stated.
- Safety-touching points are flagged as stops, not decided.
- No co-design point is presented as clinical evidence.
- If it leaves the conversation, ask who clears it and call `verify.build_record` with decisions by insight id (no participant words or codes); otherwise label it an uncleared draft.

## Boundaries

- Decisions on co-design points only. Whether co-design was traced and used over time is the co-design quality monitoring skill.
- Clinical safety, human factors and regulatory conclusions belong to their owners and packs.
- Prices and value messages are Commercial; anything a payer sets is Market Access.
