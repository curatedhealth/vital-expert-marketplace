# B1 Engagement plan and value narrative

Framework task: DH-03.01.3.1, Part B, task B1. Replaces the earlier "Payer Negotiation" section, whose negotiation part moved to the coding, pricing and contracting competency (`coding-pricing-and-payer-contracting`, DH-03.01.2.1).

## What this task delivers

Two things, both drafts for the person. First, an engagement plan: which bodies to contact, through which route, in what order, with the dependencies that fix the order and the owner the person names for each step. Second, a value narrative: the few claims the product can make to that body, each tagged with its source, its passage, the requirement it answers, and its Verify status as read by you. It answers "whom do we talk to first, and what can we truthfully say?"

Why it matters: a narrative written before the evidence is checked tends to claim what the study did not show, and a body that finds one overreach reads every other claim with suspicion. A sequence chosen without the clocks (a three-to-four-month wait for a BfArM meeting, a six-month LPPR filing window after PECAN) wastes the only window the route offers.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.3.1 Part B, Engagement plan and value narrative |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/engagement-options.md`; `references/evidence-requirements.md`; the access strategy from the coverage pathway skill if present |
| Tools | `verify.qualify_source`, `verify.check_claim` for any claim A1 did not check; `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/engagement-plan-output.md` |
| Input | The request and its context; target bodies and their order if the person has one; named owners; the claims the person wants |
| Governance | `references/governance.md`; people choose the order, the claims and every word |

## The rule that shapes this task: people decide, claims are earned

The person chooses the bodies, the order and the owners. You lay out the routes, their costs and the order constraints that are facts, and you may propose a sequence labeled "proposed" with the constraint behind each step. A claim enters the narrative only if A1 (or step 4 here) recorded it as "checked". Every sentence meant for a body is a draft that stops for its owner.

## Workflow

### Step 1. Gather the evidence

Use A1 (evidence map, checked claims) and A2 (readiness) from the conversation. If A1 is missing, run it in short mode first: a narrative without checked claims is not possible. If there is no study or claim to run A1 on, show the empty step 5 skeleton for the body (for DiGA: patient group by ICD-10-GM code, effect type DE6 or DE7, study, comparator), one slot per line, each marked "empty: needs a checked claim", and ask for the DOIs and claims that would fill it. Write no claim text into a slot. A plan without A2 is possible and says that readiness was not reviewed.

### Step 2. Lay out the routes per body

From `references/engagement-options.md`, list for each target body the early-contact route, its cost, lead time, format and limits. Add the order constraints that are facts: the BfArM meeting lead time (`DE28`), the single trial listing (`DE23`), the PECAN filing windows (`FR14`), ANS in parallel (`FR15`), NICE requests at scoping (`UK2`), TCET tied to FDA timing (`US5`).

### Step 3. Draft the sequence with the person

Ask for the person's preferred order and owners. If they want a proposal, build one by dependency only (what must exist before what), label it "proposed", and show the constraint behind each step. Where two orders are both possible, show both and the fact that would decide between them. Never order by an assumed likelihood of success.

For each consultation step, list what the person would need to bring, from the source: for BfArM, the application form, 10 to 15 questions at most, a briefing document of about 40 to 50 pages at most, a 15-minute presentation and the participant list (`DE28`). Draft question topics only if asked, labeled "draft for [owner]".

### Step 4. Build the claim table

For each claim the person wants to make to a body:
1. Find its A1 record. If A1 did not check it, call `verify.qualify_source` (study DOI) and `verify.check_claim` with the results sentence quoted verbatim and its locator, then read the passage yourself (`references/tools.md`).
2. Tag it: claim text, body, requirement answered (row id; for DiGA, effect type `DE6` or `DE7`), study and locator, passage, Verify status, your reading (checked or not checked).
3. Drop or rewrite any claim that is not checked. Offer the narrower claim the passage does support, for example the design statement instead of the effect statement.
4. Flag claims that the rules exclude: staff workload or economic indicators for DiGA (`DE8`); organizational claims with no organizational endpoint (`FR25`).

### Step 5. Write the narrative skeleton

Order the checked claims as the body's rules ask for them: for DiGA, patient group by ICD-10-GM code, effect type, study, comparator (`DE3`, `DE9`); for LPPR, SA then ASA with the comparator (`FR3`, `FR4`); for NICE, by ESF standard group (`UK13`). Each sentence carries its source tag. The skeleton is a draft for the owner and says so on its first line.

### Step 6. Point price and contract work elsewhere

If the request touches price, discounts, risk-share or contract terms, say that it belongs to the coding, pricing and contracting skill (`coding-pricing-and-payer-contracting`, DH-03.01.2.1) and stop that part. Note only the facts that tie the two: the CEPS economic file is filed jointly with the LPPR medico-technical file (`FR2`), and the DiGA application states actual prices (`DE3`).

### Step 7. Name owners and decisions

For each step and each claim, name the owner the person gave, or "owner not named". List the decisions the person must take: order, effect type, comparator, which claims to keep, who signs each submission.

## Build the output

Follow `assets/engagement-plan-output.md`. Short mode: the proposed or confirmed sequence in one table, the three to five checked claims with source and status, the excluded claims in one line each, and the decisions needed. Full mode adds the route details, the narrative skeleton and the dependency notes.

## Before you hand it over

- Every claim in the narrative is "checked" with its passage; every excluded claim says why.
- The sequence is the person's or labeled "proposed", with the fact behind each step.
- Every sentence meant for a body is labeled a draft for its owner.
- No price, discount or contract term appears.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No contact with any body; no filing.
- No negotiation, pricing or contract terms.
- No forecast of an opinion, a listing or a price.
- Drugs, biologics and wellness apps are out of scope.
