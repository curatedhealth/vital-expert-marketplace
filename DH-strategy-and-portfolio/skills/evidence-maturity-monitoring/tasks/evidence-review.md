# B1 Evidence review

Framework task: DH-DIL.2.2, Part B, task B1. New in this suite (see A1).

## What this task delivers

A review draft that says, measure by measure, whether the movement read triggers the person's rules: triggered, not triggered, or not measurable; for each trigger, the record behind it, the owner the person names, what the person decided to do (or "decision not given"), any new framework level labeled "proposed" until the person confirms it, and the reread date the person sets. It answers "against our measures, what moved, who follows up, and is our level still the one we confirmed?"

Why it matters: a movement read lists differences; a review ties them to the person's thesis and writes down who acts. Keeping the level change separate and unconfirmed until the person says so keeps the baseline honest.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (old skill "Worker: not bound"); see `references/governance.md` |
| Skill | DH-DIL.2.2 Part B, Evidence review |
| Workflow | The steps below |
| Knowledge | A1 measures and A2 read; `references/monitoring-signals.md`; `references/company-status.md`; `references/evidence-frameworks.md` section 3; rows DL-107 to DL-113 (DOI 10.1038/s41746-023-00836-5), UK12, HE-084, CV155 to CV159 (DOI 10.1038/s41746-020-0260-4) |
| Tools | A2's tools if no movement read exists in this request; `scripts/maturity_diff.py` |
| Prompt | This guide |
| Template | `assets/review-output.md` |
| Input | The request and its context: the person's measures and owners, the A2 read, the confirmed baseline level, decisions as stated, reread dates |
| Governance | `references/governance.md`; people set rules, owners, levels and dates; no investment advice |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the measures, names the owners, confirms any level and sets the reread date. The model checks the A2 read against those measures and routes the work. It never sets a measure, decides an action, confirms a level, states a value effect, names an owner the person has not named, or rates a company or a team. If asked to propose a measure or a new level, it may, labeled "proposed" with the row behind it, and applies none until the person confirms.

## Workflow

### Step 1. Gather the read

Use the A2 read the person brings into this request. If there is none, run A2 first in short mode on the runs in this request. Say what was not compared (for example inputs missing from a compare_portfolio snapshot). Carry each company's status line from A2 (read from a filing or register, or "Status: [GAP]: not read" with the filings to open, `references/company-status.md`) and every resolution flag carried forward; a measure that turns on status is not measurable until the filing or register is read.

### Step 2. Confirm the measures and owners

Write the person's measures back, numbered, with the owner of each. A measure without an owner is checked; its trigger is listed as "owner not named".

### Step 3. Check each measure

Mark triggered, not triggered or not measurable `[GAP]`, with the change class and the record behind it (reference and retrieval date). A METHOD, COVERAGE or RESOLUTION change never triggers an evidence measure unless the person's measure says so.

### Step 4. The framework level

If an INPUT change bears on the confirmed level (for example a second high-quality RCT for Evidence DEFINED level 4, DL-112; a changed intended purpose for the NICE tier, UK12), write "proposed level X under FRAMEWORK, for you to confirm", with the framework's limits. If the change needs studies graded, route to `dh-clinical-development` literature-and-real-world-evidence-review and keep the confirmed level. Never change the baseline yourself.

### Step 5. For each trigger: record, owner, decision, reread date

Name the record, the owner given, the action the person decided (or "decision not given"; never propose a buy, hold or sell), and the reread date the person set (or "not given"; ask).

### Step 6. Route the follow-up

| Trigger | Responding work |
|---|---|
| New study or results to grade | `dh-clinical-development` literature-and-real-world-evidence-review |
| New or changed authorization | `dh-regulatory-and-quality` regulatory-pathway-monitoring |
| Reimbursement listing change | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Thesis or decision record to update | `thesis-and-memo-monitoring`; `investment-memo-and-decision-record` (this pack) |
| Fresh profile or assessment record | `company-and-evidence-assessment` (this pack) |

## Build the output

Follow `assets/review-output.md`. Short mode for a direct question: measures triggered and not, each trigger with record, owner, decision as stated and reread date, and the level as confirmed or newly proposed. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every measure, owner, decision, level and date is the person's, and the output says so; proposals are labeled.
- Every trigger cites the class and the record behind it.
- Status comes from a filing or register, or is "[GAP]: not read"; never from press or memory.
- A refusal (buy, hold, sell, value, LP or committee wording) offers a facts-only draft labeled "draft for the owner", with no recommendation.
- Word count: run `python3 scripts/maturity_diff.py --count ANSWER.md` on the short answer; at or under 450 words, counted without the calls list and source columns.
- No overall rating, no ranking, no value statement, no buy, hold or sell.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model checks and routes; it does not judge companies, teams or people.
- No forecast of when evidence will mature.
