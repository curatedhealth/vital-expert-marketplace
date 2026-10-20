# A2 Forum score and benefits read

Framework task: DH-01.03.3.2, Part A, task A2. Replaces the old "Forum score" task (CF-12.01.03.3.2.2) and keeps its method: read each decision against the rule, mark match or drift, note a continue that exceeded the named capacity, and do not rescore the rule to match what was decided. Adds the read of continue items against the person's benefits plan and the dated changes since the forum.

## What this task delivers

For one forum sitting: each decision's recomputed value and rank under the rule confirmed before the forum, what the rule implied, the recorded decision, and "match" or "drift"; recorded ranks that differ from the recomputed ranks; the continue items' capacity against the named capacity; for continue items, the share of planned change achieved against the person's own benefits plan, with missing register fields flagged; and dated rule or record changes since the forum that touch an item. It answers "did we follow our rule, and are the items we continued delivering what we planned?"

Why it matters: a forum that drifts from its rule without saying why loses the rule's protection. A continue item read only on activity, not on the benefits planned for it, can run for years without a check.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.03.3.2 Part A, Forum score and benefits read (CF-12.01.03.3.2.2) |
| Workflow | The steps below |
| Knowledge | A1 output; `references/review-signals.md` sections 2, 3, 4 and 6; `references/licensing-and-deal-flags.md` |
| Tools | `scripts/forum_check.py drift`, `benefits`, `words`; `analytics.mcda` (recompute a recorded rank, without code execution); `diligence-dh.get_deltas` and `regulatory-dh.search_devices` (only for a named counterparty or product) |
| Prompt | This guide |
| Template | `assets/forum-score-output.md` |
| Input | The request and its context; the A1 check; the rule confirmed before the forum with its date; the scores in the record; the named capacity; the person's benefits plan; the read date |
| Governance | `references/governance.md`; match and drift are readings, not verdicts |
| Catalogue job | none |

## The rule that shapes this task: the rule as written, before the forum

The decision is read against the rule confirmed before the forum, with the scores the forum used. The model never adjusts a weight, a score or the rule to make a decision match, never reconstructs missing scores, and never calls a drift wrong. Benefits are read only against the person's own plan.

## Workflow

### Step 1. Gather the evidence

Use A1 from the conversation; if missing, run it first, since only recorded decisions can be scored. Ask for the rule confirmed before the forum (weights, decision rule, capacity, date) and the scores in the record. If the rule is dated after the forum, say it cannot be used to score this sitting (old method: do not rescore the rule to match what was decided) and ask for the earlier rule.

### Step 2. Recompute and read each decision

With code execution, add score columns `s_<criterion>` and `capacity_use` to the log, write the rule as JSON (`weights`, `rule_date`, `decision_rule` with `type` "capacity_in_rank_order", "top_n" or "min_value"), and run `python3 scripts/forum_check.py drift LOG.csv RULE.json`. Without it, call `analytics.mcda` with exactly the recorded scores and weights, or compute value = 25 x sum of weight x score by hand. For each decision: recomputed value and rank, recorded rank, what the rule implied, the recorded decision, "match" or "drift" (continue beyond the rule; held back against the rule), and whether the recorded rank differs. Where the rule's words allow two readings, show both and write "your call". Where the rule is silent on stop against delay, say so.

In the illustrative sitting, Program C was continued although the rule placed it past 14 FTE (continue items used 15 FTE), and its record carried no rank: "drift: continue beyond the rule" (`examples/live/forum_check_runs_output.md`).

### Step 3. Capacity

Sum recorded continue items in rank order against the capacity the person named (amount, unit, period). Name the first continue item past it. Missing capacity: "capacity not given"; no check.

### Step 4. Benefits against the person's plan

For each continue item with a benefits plan, run `python3 scripts/forum_check.py benefits PLAN.csv --as-of READ_DATE` (add `--rule SHARE` only with the person's own threshold). Report baseline, target, actual with its date, the share of planned change achieved, and flags for missing register fields (owner, baseline, target, measure: the contents a benefits register lists, SP-104) and review dates not given or already past. Label the UK terms "UK public-sector guidance, applied by analogy" (SP-099 to SP-105). Without a threshold, give the numbers and no verdict. An item with no benefits plan: "no benefits plan supplied `[GAP]`".

### Step 5. Changes since the forum

From `review-signals.md` section 6, list the dated rule changes since the forum that touch a reviewed item, each with its instrument and date (for example, a licensed item signed before 1 May 2026: Regulation (EU) 2026/877 of 16 April 2026, in force 1 May 2026 (SP-135); the 20% combined (competitors) or 30% per-party (non-competitors) market share condition on any relevant market, set beside the person's figure or "not given", without leaning (SP-136); the transition to 30 April 2027 for agreements in force on 30 April 2026 (SP-137); GDPR Article 9 where health data moves (DL-101, DL-105, DL-106); all for the owner the person names for legal). For a named licensor, licensee or partner: its company status line (`licensing-and-deal-flags.md` section 3). For a company covered by the dated rows (Pear Therapeutics, Akili, Big Health, Aidoc), quote each filing by name and date with its row and what the form does not mean; otherwise "Company status [GAP]: not read" with the filings to open, listed from the most recent backward, not only from the forum date, because an earlier bankruptcy, acquisition or delisting governs status in the period, and `diligence-dh.get_deltas {companies: [NAME], since: FORUM_DATE}` only if the person wants the library's log. If the forum date is before 12 October 2026, say the log began then and cannot show earlier changes; offer the company's dated filings and authorization records instead of "no change". `get_deltas` for a portfolio counterparty has no saved output beyond the test companies: **needs a live check**. A change is a signal for B1, never a verdict.

## Build the output

Follow `assets/forum-score-output.md`. Answer first: matches and drifts by count, the capacity check, benefits items not measurable or below the person's rule, and the change since the forum that touches most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/forum_check.py words ANSWER.md`.

## Before you hand it over

- Every decision is read against the rule confirmed before the forum, with the recorded scores; nothing rescored.
- Match and drift are labeled readings against the rule, not verdicts.
- Benefits read against the person's plan only; no threshold supplied by the model.
- UK guidance labeled as such; [PAPER] rows carry their DOI; [WF] rows say so.
- Company status line for any named counterparty, from the dated filings where a row covers it; no status inferred; no "no change" for a period before the log began; filings listed from the most recent backward.
- Each fact names its source and date in plain words, then the row id; inference rows say "(inference)".
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Strategy-level objectives and their benefits: `strategy-execution-monitoring` (this pack).
- Stage health of an item: `dh-clinical-development` lifecycle-quality-monitoring.
- No forecast of an item's revenue, value or success; no benchmark as a target.
