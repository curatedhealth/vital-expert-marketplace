# B1 Execution review and miss owners

Framework task: DH-01.05.4.2 with DH-01.05.1.2 and DH-01.08.2.2, Part B, task B1. Carries the old one-line tasks "DH-01.05.4.2.2 strategy execution pass rule", "DH-01.05.4.2.3 strategy execution miss owner", "DH-01.05.1.2.2 strategic vision pass rule", "DH-01.05.1.2.3 strategic vision miss owner", "DH-01.08.2.2.2 prototype experiment pass rule" and "DH-01.08.2.2.3 prototype experiment miss owner" as steps 1 and 4.

## What this task delivers

For each benefit, milestone and option test: the person's pass rule, the result against it from A2, and for every failed element the owner the person names and the date it will be rechecked, or "stopped" if the person stops the unit. Then the decisions the review surfaces (reset a target, change a rule, continue, change or stop an option), each with its facts, all left to the person. It answers "by our own rules, what failed, who owns each miss, and what do we have to decide?"

Why it matters: the old tasks were clear that a failed element must not be closed "because the existing assessment skill already described it", and that a unit is not scored before its rule exists. A review that assigns owners the team never named, or calls a strategy "on track" from a partial read, says more than the data does.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `behavior-change-designer` (old DH-01.05.4.2.2 and .3, DH-01.05.1.2.2 and .3); `ai-ml-governance-director` (old DH-01.08.2.2.2 and .3). Work as a strategy delivery analyst who checks against the person's rules |
| Skill | DH-01.05.4.2 Part B, Execution review and miss owners |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/execution-frameworks.md`; `references/governance.md` |
| Tools | None beyond A2. `scripts/execution_check.py`; `verify.build_record` when the record leaves |
| Prompt | This guide |
| Template | `assets/execution-review-and-miss-owners-output.md` |
| Input | The request and its context: A2 output or the person's files and read date, the pass rules, owners, recheck dates and follow-up rules the person sets |
| Governance | `references/governance.md`; the person judges and decides |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the rules, names the owners, sets the recheck dates and decides what a failure leads to. The model reads the data against the rules and writes down the result. It never decides that the strategy is on track or off track, never decides kill or continue, never names an owner the person has not named, and never closes a failed element on its own. Where a rule's words allow two readings on the data, it shows both and writes "your call".

## Workflow

### Step 1. Confirm the pass rules (old "pass rule" tasks)

Write each rule back verbatim, numbered: for benefits the share of planned change that counts as met; for milestones the elements that count (owner, evidence of completion, on time) and the element that blocks if it fails; for tests the decision rule and the date it was written. A unit without a rule: "pass rule not given `[GAP]`"; report its values but mark nothing met or failed.

### Step 2. Read each unit against its rule

From A2 or by running the script on the person's files: benefits met, not met or not measurable (E flags); milestone elements failed (M flags); tests readable or not (X flags). Check the signal measures what the rule says: a benefit measured on a different population or date than its baseline is "not comparable"; say so.

### Step 3. Partner facts behind a unit

Where a failed or at-risk unit depends on a named partner, carry the A2 record facts and the company status line. A press claim stays the person's claim; it does not fail a milestone by itself. Where a row covers the company, quote what its filings state (`execution-frameworks.md` section 5) instead of leaving it unread. What a partner's change means for the agreement goes to the owner the person names for legal matters, or owner not named.

### Step 4. Owners and recheck dates for each failed element (old "miss owner" tasks)

For each failed element: the owner the person named (or "owner not named"; ask), the recheck date they set (or "not given"; ask), or "stopped" if they stopped the unit. A recheck date earlier than the read date is stated as a fact, never as urgency. A failed element stays open until the person closes it with evidence.

### Step 5. What the person must decide

List the decisions the review surfaces, each with the facts behind it: whether to reset a target or rule (and the date the new rule is written, so later reads use it), whether a test without a prior rule is rerun with one, whether an option continues, changes or stops, whether a benefit without a baseline gets one. Propose nothing unless asked; label any proposal "proposed". Kill or continue is the person's. Where the person calls a test failed (or succeeded), state the logged result and its direction against the comparator verbatim from the experiment log (for example "enrollment 31% vs 24%"), alongside the flag that no rule was written before the start: a fact from the person's data, not a verdict.

## Build the output

Follow `assets/execution-review-and-miss-owners-output.md`. Answer first: counts of units whose rule is met, failed and not measurable, the failed elements by name, how many have an owner and recheck date, and the flag that most limits the review. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/execution_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Rules, owners, recheck dates and follow-ups are the person's, and the record says so.
- No overall verdict; no kill or continue; no failed element closed by the model.
- Units without a rule are not marked met or failed.
- The review is labeled "execution review draft for the owner".
- The company status line is present for any named partner.
- `python3 scripts/execution_check.py words ANSWER.md` prints "within the short-mode cap".
- Every fact names its source and date in plain words with the row id after it; "(inference)" rows carry the label each time.
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Reopening the strategy or choosing a different option: `strategic-vision-and-options` (this pack).
- Any wording for a board, investors, partners or staff: stops for the owner the person names.
- Partner agreement conclusions: the owner the person names for legal matters, or owner not named.
