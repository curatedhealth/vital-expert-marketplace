# B1 Robustness review

Framework task: DH-01.02.1.2, Part B, task B1. Replaces the earlier "protocol robustness pass rule" and "protocol robustness miss owner" sections.

## What this task delivers

A review draft that says, rule by rule, whether the protocol and its public record meet the robustness rules the person set: pass, miss, or not measurable; for each miss, the owner the person names and the piece of work that responds. It answers "will our design hold up, by our own standard, and who fixes what?"

Why it matters: without written rules, every protocol review reopens what "robust" means, and the most senior reader's preference wins. Rules written before the check make the review repeatable at every amendment.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.1.2 Part B, Robustness review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/robustness-signals.md`; `references/registration-and-reporting-clocks.md`; `references/completeness-rules.md` |
| Tools | A2's tools if no registration check exists; `scripts/registry_check.py` |
| Prompt | This guide |
| Template | `assets/robustness-review-output.md` |
| Input | The request and its context; the person's pass rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |
| Catalogue job | none |

## The rule that shapes this task: people judge

The person writes the pass rules, in their own words, and names the owner of each. The model checks the evidence against those rules, finds where the design misses, and routes the work. It never sets a rule, never decides that a signal is a miss on its own, and never names an owner the person has not named. If asked to propose rules, it may, each marked "proposed" with the row behind it, and applies none until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 (completeness) and A2 (registration and amendments) from the conversation. If either is missing and needed for a rule, run it first in short mode. A review on one of them alone is possible and says what was not reviewed.

### Step 2. Write the pass rules with the person

Ask for the rules and an owner for each. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Completeness | "Every SPIRIT item addressed or stated not relevant before ethics submission" | A1 counts (CV117) |
| Estimand | "Primary estimand and its sensitivity analysis in the protocol" | A1 step 3 (CV40) |
| Digital measure | "V&V in the target population shown for every DHT endpoint before first enrollment" | A1 triggered duties (CV46, CV48) |
| Registration | "Registered before first consent" | A2 (CV132) |
| Consistency | "Registry, protocol and paper state the same primary outcome and time point" | A2 compare (SP-16) |
| Change control | "No change to the primary outcome after first enrollment without a documented reason" | A2 amendment log (CV114) |

Write the rules back for confirmation before checking anything. A rule without an owner is checked, and the miss is listed as "owner not named".

### Step 3. Check each rule

Mark pass, miss, or not measurable `[GAP]`, with the fact behind it and its source (A1 locator, registry field and read date, paper locator). Where a rule depends on a clock, state the clock and its applicability (A2).

### Step 4. Name the miss and its owner

For each miss, state the first point where it bites (for example an undefined estimand blocks the missing data plan and the sample size). Name the owner the person gave. If none, write "owner not named" and ask.

### Step 5. Route the response

Map each miss to the work that responds, without choosing for the person:

| Miss | Responding work |
|---|---|
| Missing or partly addressed protocol items | Protocol drafting (design skill DH-01.02.1.1, A2) |
| Endpoint not fully defined, DHT not fit for purpose | Endpoint and COA selection (design skill, A1) |
| Estimand, missing data, SAP decisions | Estimand and SAP decisions (design skill, B1) and the owner the person names for statistics, or owner not named |
| Registry and protocol differ; clocks | The owner who maintains the registration; the owner the person names for regulatory status, or owner not named, on applicability |
| Monitoring, remote visit operations | `dh-clinical-validation` trial-operations-monitoring (DH-01.02.3) |
| Payer or HTA evidence fit | `dh-market-access` payer-engagement-and-hta-submission |

### Step 6. Re-run on amendment

Say which rules to re-check when the next protocol version arrives (all rules touching changed items). The review is repeatable because the rules are written; keep them with the protocol version.

## Build the output

Follow `assets/robustness-review-output.md`. Short mode for a direct question: rules passed and missed, each miss with owner and responding work, and the one decision the person needs to make. Full mode adds the evidence per rule. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule and owner is the person's, and the output says so; proposals are labeled.
- Every verdict cites the fact and source behind it.
- No general verdict ("robust", "compliant"); only per-rule pass or miss.
- Protocol amendments, registry updates and external wording stop for the owner.
- Each [PAPER] paper cited has its DOI once in prose, and beside its row id in every table.
- The record line ends the answer: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people, sites or sponsors.
- No forecast of regulatory, ethics or journal outcomes.
- Risk-of-bias judgments of results belong to a review (ES-70).
