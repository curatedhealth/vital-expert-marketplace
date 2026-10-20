# B1 Performance review

Framework task: DH-03.01.3.2, Part B, task B1. Replaces the earlier "HTA submission pass rule" and "HTA submission miss owner" sections, which are now steps 2 and 6.

## What this task delivers

A review draft that says, body by body, whether the person's HTA submissions and payer engagement are working against the rules the person set: on track, at risk, or missed; where the path stalls; who the person says owns each miss; which hypotheses could explain it; and which piece of preparation work should respond. It answers "is our HTA and payer engagement working, and what do we do where it is not?"

Why it matters: without written rules, every review reopens what "good" means. Rules set before the outcomes arrive make the review fair and repeatable, and a named stall point sends the fix to the right work instead of to the loudest explanation.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.3.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; the engagement plan from the preparation skill if present; `references/decision-sources.md`; `references/submission-checklists.md` |
| Tools | A2's tools if no decision run exists; `scripts/decision_tracker.py` (optional) |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's pass rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the pass rules, in their own words and numbers, and names the owner of each. You check results against those rules, find the stall point and lay out options. You never set a threshold, never decide what counts as a miss, and never name an owner the person did not name. If asked to propose rules, you may, each marked "proposed" with the fact behind it, and you do not apply them until the person confirms. A national rate is never a rule.

## Workflow

### Step 1. Gather the evidence

Use A1 (completeness and findings) and A2 (decisions, clocks, comparables) from the conversation. If A2 is missing, run it in short mode. A review without A1 is possible and says the file itself was not checked.

### Step 2. Write the pass rules with the person

For each body, ask for two or three rules, each with a number or date and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Completeness | "No incompleteness letter from BfArM" | A2 letters; A1 checklist |
| Engagement | "BfArM consultation held before we file" | The person's records |
| Decision | "Permanent listing at the first application" | A2 decision |
| Claim scope | "All claimed positive care effects confirmed, none struck" | A2 directory status (`DE-24`) |
| Evidence obligation | "NICE evidence-generation report sent each year" | The person's records; `EN-2` |

Where the engagement plan set steps or dates, start from those. Write the rules back for confirmation before checking anything. A body without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not measurable `[GAP]`, with the fact behind it. A body is "on track" if every rule passes, "missed" if any rule misses, and "at risk" if every rule passes but a running clock from A2 (an objection window, a PECAN filing window, an early-use evidence period) is close to a date a rule depends on. State the clock with its row.

### Step 4. Find the stall point

For each missed body, name the first stage where a rule missed, in this order: engagement (consultation, scoping), completeness, substance (evidence, claims), decision, post-decision obligations. A miss at completeness is a different problem from a miss on substance.

### Step 5. Lay out hypotheses, not causes

For each stall point, list possible reasons as hypotheses, each labeled "hypothesis" with what would confirm it. Draw them from the sourced failure patterns, never from memory:
- Completeness: administrative items (in 2025, 51 percent of CNEDiMTS requests were suspended for administrative reasons only, `FR24`); device description, clinical or vigilance data (`FR7`); the gematik or BSI conditions for DiGA (`DE29`; `references/requirements/germany-diga.md` "Data security: TR-03161 and completeness").
- Substance: an organizational claim without an organizational endpoint (`FR25`); a study outside Germany without transferability (`DE12`); no comparative data for ASA (`FR4`); a trial study that did not confirm all claimed effects (`DE-24`).
- Decision timing: actual BfArM review days are not published `[GAP]`, so a long wait cannot be compared with a norm.
- Post-decision: not engaging in NICE evidence generation is a listed withdrawal ground (`EN-2`).
Never state a cause the evidence does not show.

### Step 6. Route the response and name the owner

Map each stall point to the work that responds, without choosing for the person:

| Stall point | Responding work |
|---|---|
| Evidence does not meet a rule, or claims not checked | Evidence requirement map (preparation skill DH-03.01.3.1, A1) |
| Incomplete file, missed fee or clock | Submission readiness (DH-03.01.3.1, A2) |
| Wrong body, wrong order, consultation not used, claims overreached | Engagement plan and value narrative (DH-03.01.3.1, B1) |
| Route itself in question | Coverage pathway and access strategy skill |
| Price or contract terms | Coding, pricing and contracting (`coding-pricing-and-payer-contracting`, DH-03.01.2.1) and its review skill (`coding-pricing-and-contract-monitoring`, DH-03.01.2.2) |
| New study needed | Clinical validation pack, outside this pack |

Name the owner the person gave. If none, write "owner not named" and ask.

## Build the output

Follow `assets/performance-review-output.md`. Short mode: verdict per body with the fact behind it, the stall point, the owner, and the one decision needed. With no rules supplied: a one-line answer, one factual table (body, position, clock with row, stage), at most two hypotheses, the routing in one line per body, and the request for rules and owners, within 450 words. Full mode adds the rule table, the evidence, the hypotheses and the routing.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the fact behind it.
- Hypotheses are labeled; no cause is asserted.
- No national rate is used as a rule or a target.
- Objections, re-submissions and any wording for a body stop for the owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- You check and structure; you do not judge people or teams.
- No forecast of a decision or of recovery.
- Drugs, biologics and wellness apps are out of scope.
