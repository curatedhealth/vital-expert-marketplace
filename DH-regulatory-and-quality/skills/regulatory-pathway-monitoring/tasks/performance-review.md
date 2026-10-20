# B1 Performance review

Framework task: DH-03.03.3.2, Part B, task B1. Replaces the earlier "regulatory pathway pass rule" and "regulatory pathway miss owner" sections.

## What this task delivers

A review draft that says, jurisdiction by jurisdiction, whether the regulatory strategy is working against the rules the person set: on track, at risk or missed; where the pathway stalls; who the person says owns each miss; the possible reasons, labeled as hypotheses; and where the response goes, usually back to the pathway strategy (DH-03.03.3.1). It answers "is our regulatory pathway working, and what do we do about the parts that are not?"

Why it matters: without rules written before the facts come in, every review reopens what "on track" means. Rules set in advance make the review fair, repeatable and quick, and keep the pathway decision with the person who owns it.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.3.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; the pathway strategy and its gates (pathway and classification skill, B1); `references/review-clocks.md`; `references/register-obligations.md`; `references/safety-records.md` |
| Tools | A1's and A2's tools if no run exists; `scripts/review_clock.py` (optional) |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's rules and named owners; A1 and A2 results; the strategy's gates |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the rules in their own words and numbers and names the owner of each. The model checks the facts against those rules, finds the stall point, lays out hypotheses and routes the response. It never sets a threshold, never decides what counts as a miss, never names an owner the person has not named, and never judges people or teams. If asked to propose rules, it may, each labeled "proposed" with the fact behind it (for example "proposed: De Novo decision within FDA's observed average total time of 247 to 278 days, RP US-61"), and it applies none until the person confirms. Published averages are context, never targets.

## Workflow

### Step 1. Gather the evidence

Use A1 (status, clocks, obligations) and A2 (safety records) from the conversation; run either in short mode if missing and needed. Take the strategy's gates from the pathway strategy if the conversation holds it. A review on one part is possible and says what was not reviewed.

### Step 2. Write the rules with the person

For each jurisdiction, ask for two or three rules, each with a number or condition and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Milestone | "Pre-Sub feedback received before we lock the validation protocol" | A1, the person's records |
| Review time | "510(k) decision within 150 FDA days" | A1 clock, with hold days |
| Notified body | "Written agreement signed before the validation study starts" | The person's records; survey context (RP EU-44) |
| Register | "All EU devices registered in EUDAMED UDI/device module" | A1 obligations |
| Safety | "No unexplained recall in our product code since our filing" | A2 |
| Strategy assumption | "Sleepio remains a usable predicate candidate" | A1 snapshot, A2 of the pathway skill |

Write the rules back for confirmation before checking anything. A jurisdiction without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not measurable `[GAP]`, with the fact behind it and its date. A jurisdiction is "on track" if every rule passes, "missed" if any rule misses, "at risk" if every rule passes but a clock or obligation from A1 is close to the condition the rule depends on (for example a De Novo additional-information request with its 180-day limit approaching, RP US-13). With code execution, `scripts/review_clock.py` gives the clock facts. A rule with no date or threshold cannot be missed yet: mark it "not measurable [GAP]: the rule names no date", show the legal date from the references as context (for example Swiss registration by 31 December 2026 for devices placed from 1 July 2026, MedDO Art. 108(2)), and ask the person whether the rule should carry that date. Never treat a MDUFA goal as the date for one file.

### Step 4. Find the stall point

For each missed or at-risk jurisdiction, name the first step of the pathway where a rule missed: classification argument, predicate or comparable, pre-submission, submission accepted, review, decision, registration, post-market. An early stall (the classification argument did not hold) is a different problem from a late one (registration not done).

### Step 5. Lay out hypotheses, not causes

For each stall point, list possible reasons as hypotheses, each with what would confirm it, drawn from sourced mechanics. Examples: a De Novo running long may reflect sponsor hold time rather than FDA time (confirm from the hold days; RP "Changes and conflicts"); a notified body step running long can be set against the survey, where 51% of notified bodies report 13 to 18 months and 31% report 19 to 24 months from written agreement to QMS plus product certificates (RP EU-44), so the question is whether the plan assumed less; a predicate assumption may fail on intended use (confirm from the summary, RP US-06). Never state a cause the facts do not show.

### Step 6. Route the response

| Stall point | Responding work |
|---|---|
| Classification argument, predicate or route no longer holds | Back to the pathway and classification skill (DH-03.03.3.1): A1, A2 or B1 |
| Submission content or quality | Submission Excellence competency (DH-03.03.4) |
| AI change control (PCCP) | AI/ML Regulatory competency (DH-03.03.1) |
| Registration or recognition across regions | Global Harmonization competency (DH-03.03.2) |
| Safety record bearing on the risk file | The person's quality and vigilance owners (Quality pack, DH-03.02) |

Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Build the output

Follow `assets/performance-review-output.md`. Short mode: verdict per jurisdiction, stall point, owner, the one decision needed. 450 words maximum, counted without tables' source column and the calls list. Before handing over, count the words of the answer (excluding the calls list and table source columns). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question, full-mode sections. Never cut a gap, a stop or the record line. Offer the full version in one line.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the fact behind it and its date.
- Causes are hypotheses, labeled; published averages are context.
- Pathway changes, regulator wording and board reporting stop for the owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams and does not choose a new pathway.
- No forecast of a decision date or outcome.
- Drugs, biologics and wellness apps are out of scope.
