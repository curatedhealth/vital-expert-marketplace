# B1 Review and repair

Framework task: DH-01.03.3.2, Part B, task B1. Replaces the old "Governance repair" task (CF-12.01.03.3.2.3) and keeps its method: name whether the rule or the decision is corrected, name the owner, name the next forum that must show the correction, and do not leave both the rule and a contradicting decision in force.

## What this task delivers

A review draft that lists, for each failed record (A1), each drift (A2), each capacity overrun and each benefit below the person's rule: the options (correct the decision, correct the rule, or record the forum's reason as a dated override for that decision, with the rule unchanged), the person's choice, the owner they name, the forum that must show the correction, and the date they set. It answers "what do we correct, who owns it, and where will it show?"

Why it matters: a rule that says one thing while a standing decision says another protects nobody. A correction with no owner and no forum is a note, not a repair.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.03.3.2 Part B, Review and repair (CF-12.01.03.3.2.3) |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/review-signals.md` sections 4 and 7; `references/governance.md` |
| Tools | A2's tools if no forum score exists; `scripts/forum_check.py words`; `verify.build_record` once the named person clears it |
| Prompt | This guide |
| Template | `assets/review-and-repair-output.md` |
| Input | The request and its context; A1 and A2 outputs; the person's choices, owners, forums and dates; reasons the forum gave for any drift |
| Governance | `references/governance.md`; the person chooses each correction |
| Catalogue job | none |

## The rule that shapes this task: people choose the correction

For each finding the model lays out what each correction would mean; the person chooses, names the owner, the forum and the date. The model never chooses, never names an owner, forum or date the person has not given, and never judges the people in the forum.

## Workflow

### Step 1. Gather the findings

Use A1 and A2 from the conversation. If A1 is missing, run it; if A2 is missing, say decisions were not read against the rule and limit B1 to record fails.

### Step 2. Ask for the forum's reasons

For each drift, ask whether the forum recorded a reason. If it did, write it verbatim beside the drift. If not, write "reason not recorded".

### Step 3. Lay out the options per finding

For each finding, label each option "proposed" and state what it would mean:
- **Correct the decision**: the item returns to the next forum against the unchanged rule (for example a continue beyond capacity is reconsidered). Reversing a continue or stop stops for the forum's decider as the person names them.
- **Correct the rule**: the rule is rewritten (weights, decision rule or capacity), dated, and the whole sitting is re-read against it in the next forum; one item's decision does not get its own rule.
- **Record the reason**: the forum's reason for departing from the rule is recorded, dated and attributed to the decider the person names, as an override for that decision. The rule's weights, scores and capacity are not changed (old method: do not rescore the rule to match what was decided, `review-signals.md` section 2). The override record states the reason, who approved it, and the capacity it uses against the named capacity.
- **Complete the record** (A1 fails): add the missing rule, rank, decider or record; a decision only in a slide is written into the forum's record.
- **Benefits below the person's rule or not measurable**: complete the plan fields (owner, baseline, target, measure, review date), or bring the item to the next forum with its benefits read.
Never leave the rule and a contradicting decision both in force without one of these (old method).

### Step 4. Record the person's choices

For each finding: the option the person chose, the owner they name ("owner not named" if none; ask), the forum that must show the correction ("forum not named"; ask), and the date they set ("date not set"; ask). The decider is not the default owner. Write any condition in the person's words.

### Step 5. Stops

Reversing a decision, changing committed capacity, and any external statement stop for the owner the person names. A licensing finding (for example an item relying on the transition to 30 April 2027 under Regulation (EU) 2026/877, SP-137) goes to the owner the person names for legal, or owner not named; never "this license is exempt". A request to name who was at fault is declined; offer the decision-level findings as a draft for the owner.

### Step 6. Clear the record

If the review leaves the conversation, ask who clears it and call `verify.build_record` with that person in `cleared_by.name` (`examples/live/verify_build_record_refusal.json`).

## Build the output

Follow `assets/review-and-repair-output.md`. Answer first: findings by count, the corrections the person chose, owners and forums named or missing, and the finding with no owner. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md`.

## Before you hand it over

- Every correction, owner, forum and date is the person's, and the output says so; options are labeled "proposed".
- No finding leaves the rule and a contradicting decision both in force without a chosen correction or an open item.
- No person judged; no external wording drafted without the stop.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Writing the corrected rule and re-ranking: `product-portfolio-prioritization` (this pack), task B1; recording the new decision: task B2.
- No forecast of the effect of a correction on value, revenue or success.
