# A1 Handoff measure

Framework task: DH-01.01.3.2, Part A, task A1. Replaces the earlier "Handoff measure" section (DH-01.01.3.2.1).

## What this task delivers

The person's written measure, set before any scoring: what counts as a received handoff, which integration points are scored, the period, what "late" means, which categories are counted apart, and which handoffs the person marks as carrying a critical-to-quality factor. The measure is dated, so a later change is a new measure, not a quiet move of the target.

Why it matters: a handoff score with an unwritten rule gets argued about instead of acted on. "Sent" and "received" give very different numbers, and the difference is exactly the work that falls between teams.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.01.3.2 Part A, Handoff measure |
| Workflow | The steps below |
| Knowledge | `references/measurement-rules.md` sections 1 and 2; `references/handoff-rules.md`; rows TM57, TM118, CS27, CS28, CS9, PL94, CV29, CS61, PL25 |
| Tools | Optional: `verify.qualify_source` then `verify.check_claim` if the measure cites a methods passage |
| Prompt | This guide |
| Template | `assets/handoff-measure-output.md` |
| Input | The request and its context: the integration map or log, the period the person wants, any rule already in use |
| Governance | `references/governance.md`; the measure is the person's |
| Catalogue job | none |

## Read the request

- **Which handoffs.** From the sibling skill's integration map, the person's log, or a list. Each needs a work product, a sender, a named receiver and a blocked decision; without them a handoff cannot be scored (old framework: "use the integration point").
- **Rule in use.** Does the team already count something? Write it down verbatim before proposing anything.
- **Period.** Start and end dates in full.
- **Categories.** The person's (for example clinical evidence, copy, implementation).

## Workflow

### Step 1. Offer the default received rule, labeled

Offer the old framework's rule as the default: "a pass is the work product received by the named receiver, not a message sent". Say it is the framework's working rule, not a sourced standard. Two labeled patterns support it: a regulator counts receipt of a complete set (BfArM confirms receipt of a complete application within 21 days, PL94; an analogy), and for multiple function products the documented impact assessment in the design file is the record (PL25). The person confirms, edits or replaces the rule in their own words.

### Step 2. Say what evidence of receipt counts

Ask how receipt is shown: a dated entry naming the receiver in the log, a document in the receiver's system, a signed review record. The person decides. The script's default is `received_on` plus a `received_by` that matches `receiver_named`.

### Step 3. Period and denominator

Set the period. Offer the counting pattern from RE-AIM, labeled: count against everything that was due, not only what someone reported (valid denominator, CS27, CS28; an analogy from a different field). Ask whether handoffs due before the period and still open are carried in (the script carries them in).

### Step 4. Late, categories and critical items

Ask what "late" means (after the due date, or after a grace the person sets). Record the person's categories. Ask which handoffs carry a critical-to-quality factor, citing the definition (CV29); the marks are the person's, and the score reports them apart. Lateness is one dimension of execution quality (CS9), never a verdict on a team.

### Step 5. Targets, only if the person has them

If the person sets a target, write it down now, dated (pre-specified targets, TM118; a priori milestones prevent moving the target, TM57). If they have none, write "no target set". Never propose a number as a norm; no source gives one.

### Step 6. Write it back and date it

Write the measure back in the person's words with today's date, and ask for confirmation. Nothing is scored until it is confirmed. A rule changed after scoring is recorded as a new version with its date.

## Build the output

Follow `assets/handoff-measure-output.md`. Answer first: the received rule in the person's words, the period, the categories and critical marks, any target, and what is still to confirm. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The rule, the period, "late", categories, CTQ marks and any target are the person's, dated; patterns are labeled as patterns and analogies.
- No numeric norm was supplied by the model.
- A sent message is not counted as received under the default rule.
- Each [PAPER] paper cited has its DOI once in prose, and beside its own row id in every table cell (rows from several papers each keep their own DOI).
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Building the integration map the measure rests on: cross-functional product integration (DH-01.01.3.1), A1.
- Quality system metrics and CAPA: `dh-regulatory-and-quality` audit-capa-and-complaints.
