# B1 Foresight review: pass rule, miss owners and feedback

Framework task: Part B, task B1. Carries the old one-line tasks as steps: DH-01.08.4.2.2 horizon signal pass rule and DH-01.08.4.2.3 horizon signal miss owner; DH-01.05.3.2.2 technology foresight pass rule and DH-01.05.3.2.3 technology foresight miss owner; DH-01.08.1.2.2 technology selection pass rule and DH-01.08.1.2.3 technology selection miss owner.

## What this task delivers

The A1 and A2 results set against the person's pass rules (for signals, calls and selections), whether each rule is met on the log as confirmed, each miss with the owner the person names to follow it up and the reread date they set, what their follow-up rule says happens next, and what feeds back into the next scan or decision. Decisions to revisit a technology, a partner or a scenario are listed as the person's. It answers "by our own rules, is our foresight good enough, who follows up each miss, and what do we change?"

Why it matters: without a pass rule written down, every review becomes a debate about whether 60 percent is good. With the person's rule applied to a confirmed log, the review is a fact, and the follow-ups have names.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`), as bound to DH-01.08.4.2; the folded pass-rule and miss-owner tasks keep their old bindings (`chief-compliance-officer-digital-health` for DH-01.05.3.2, `behavior-change-designer` for DH-01.08.1.2) |
| Skill | DH-01.08.4.2, DH-01.05.3.2 and DH-01.08.1.2 Part B, Foresight review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/monitoring-signals.md` sections 1 and 6 (SP-090, SP-091, SP-104, SP-105; SP-075, SP-081 [PAPER] DOI 10.1016/j.jval.2015.12.016 [WF]); `references/governance.md` |
| Tools | None beyond A1 and A2. `scripts/foresight_check.py --pass-rule` |
| Prompt | This guide |
| Template | `assets/foresight-review-output.md` |
| Input | The request and its context: the confirmed log (outcomes the person accepted), the pass rules, owners, reread dates and follow-up rules the person sets, the read date |
| Governance | `references/governance.md`; the person judges; no person is scored |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the pass rules and the follow-up rules, confirms the outcomes, and names who follows up each miss. The model applies the rules to the confirmed log and writes down the result. It never sets a threshold, never compares the log with a benchmark (none exists in the sources), never blames or rates a person or team, and never decides to drop a technology, a partner or a scenario.

## Workflow

### Step 1. Confirm the rules and the log

Write back, numbered and verbatim: the pass rule for signals (for example "no leads logged as signals, and at least 90 percent of sampled rereads unchanged"), for calls and for selections, in the person's words and, if given, the machine form (`hit_share >= 0.6`). Missing: "pass rule not given: nothing marked passed or failed". Use only outcomes the person confirmed; proposed outcomes from A2 stay proposed and are listed apart.

### Step 2. Apply the pass rules

Run `python3 scripts/foresight_check.py --log LOG.csv --as-of DATE --pass-rule "<the person's rule>"`, adding `--owners "call=<name>;selection=<name>"` when the person names owners by kind and `--if-confirmed "<id>=<outcome>;..."` for proposed outcomes. Report "met" or "not met" per rule with the counts behind it and the denominator. Proposed outcomes stay out of the count; what the result would be if the person confirmed them is the script's `--if-confirmed` line, quoted, never estimated. Where a rule's words allow two readings on the data, show both and write "your call".

### Step 3. Misses and their owners (old "miss owner" tasks)

List each miss and each failed check with the owner the person names, in their words, and the reread date they set. Missing owner: "owner not named", ask; never suggest a job title. List every row flagged O1 (owner not named in the log), misses or not, and ask who owns it. Where the person names owners by kind (for example calls and selections) and the log's owner column names someone else for a row (O4), show both names in that row and ask which applies; never choose. Missing reread date: "not given", ask. A follow-up rule relative to the review ("within 30 days of the review") stays in the person's words; compute a calendar date only when the person gives the review date. A reread date earlier than the read date is stated as a fact ("reread date 1 October 2026 is earlier than the read date 20 October 2026"), never as urgency. A miss owner follows up the miss; the review never says whose fault it was.

### Step 4. What the person's follow-up rule says

For each miss, write what their follow-up rule says happens (for example "reread the record", "reopen the technology choice in `horizon-scanning-and-technology-evaluation` B1", "ask the vendor for the EUDAMED record"). No rule: "follow-up not given; your call". Never add a decision.

### Step 5. Feedback into the next scan (ROAMEF feedback)

List, labeled "proposed", what the misses suggest for the next scan: a check to add (for example "log the confirming record before a press item enters the map"), a source to add or drop, a resolution rule to write before the next call. Where the person uses ROAMEF or benefits terms, say they are UK public-sector guidance (SP-090, SP-091, SP-104, SP-105). If options are rescored, the re-ranking runs in `horizon-scanning-and-technology-evaluation` B1 (this pack), and MCDA consistency can be tested by eliciting the scores again (SP-081, [PAPER] Marsh 2016, DOI 10.1016/j.jval.2015.12.016, [WF]).

### Step 6. What the person decides

List each decision surfaced (accept the proposed outcomes, revisit a selection, keep or drop a source, change a pass rule), with the facts behind it.

## Build the output

Follow `assets/foresight-review-output.md`. Answer first: per pass rule, met or not met with its counts, the misses with their owners, and the decision that is theirs. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/foresight_check.py --words ANSWER.md` (counts the whole answer except the calls list, and leaves out the Source, Rows, Retrieved and Evidence columns); without code execution, count the same way by hand. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Pass rules, outcomes, owners, reread dates and follow-ups are the person's, and the record says so.
- No benchmark, no threshold from the model, no rating of a person or team.
- Proposed outcomes and proposed feedback are labeled and kept apart.
- The review is labeled "foresight review draft for the owner".
- No calendar date computed from a relative rule unless the review date was given; every O1 row listed; every O4 conflict shown with both names.
- The record line is the very last line of the answer; the calls list and the one-line offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Re-ranking options or redoing scenarios: `horizon-scanning-and-technology-evaluation` B1 (this pack).
- Strategy execution against objectives and benefits: `strategy-execution-monitoring` (this pack).
- Any wording for a board, investors or partners: stops for the owner the person names.
