# B1 Performance review

Framework task: DH-03.03.2.2, Part B, task B1. Replaces the earlier "cross-region compliance pass rule" and "cross-region compliance miss owner" sections.

## What this task delivers

A review draft that says, region by region, whether the multi-region alignment is holding against the rules the person set: on track, at risk, or missed; where it stalls; who the person says owns each miss; and which planning work should respond. It answers "is our multi-region alignment holding, and what do we do about the regions that are drifting?"

Why it matters: without written rules, every review reopens what "aligned" means. Rules set before the facts arrive make the review fair and repeatable.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.2.2 Part B, Performance review |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; the multi-region plan (DH-03.03.2.1) if one exists; `references/obligations.md`; `references/change-sources.md` |
| Tools | A1's tools if no status run exists; `scripts/obligations_table.py` |
| Prompt | This guide |
| Template | `assets/performance-review-output.md` |
| Input | The request and its context; the person's rules and named owners; A1 and A2 results |
| Governance | `references/governance.md`; people set rules and name owners |

## The rule that shapes this task: people judge

The person writes the rules, in their own words and numbers, and names the owner of each. The model checks facts against those rules, finds where the alignment stalls, and lays out options. It never sets a threshold, never decides what counts as a miss, and never names an owner the person has not named. If asked to propose rules, it may, each marked "proposed" with the fact behind it, and it does not apply them until the person confirms.

## Workflow

### Step 1. Gather the evidence

Use A1 (status and obligations) and A2 (changes) from the conversation. If either is missing and needed, run it first in short mode.

### Step 2. Write the rules with the person

For each region, ask for two or three rules, each with a measure and an owner. Offer this shape, filled with the person's words:

| Rule type | Example in the person's words | Measured by |
|---|---|---|
| Authorization held | "Valid authorization in every launch market" | A1 status (records and gap classes) |
| Obligation met | "Every annual registration and license statement confirmed filed before its date" | A1 obligations table plus the owner's confirmation |
| Same product everywhere | "Same intended purpose and software version in every region" | The person's records; A1 records as stated |
| Change absorbed | "Every in-force change in A2 assessed within the quarter" | A2 list plus the owner's log |

Where the plan (DH-03.03.2.1 B1) set gates, start from those. Write the rules back for confirmation before checking anything. A region without rules gets a factual summary and no verdict.

### Step 3. Check each rule

Mark each rule pass, miss, or not measurable `[GAP]`, with the fact behind it. A date that has passed is "not measurable" until the owner confirms the filing; the model does not mark it missed on the date alone. A region is "on track" if every rule passes, "missed" if any rule misses, "at risk" if every rule passes but an obligation the rule depends on falls inside a window the person set, or an in-force change from A2 is not yet assessed.

### Step 4. Find the stall point

For each missed region, name the first point where a rule missed: authorization not obtained or not maintained; an obligation not confirmed; product divergence between regions; a change not absorbed. That is where the response goes.

### Step 5. Lay out hypotheses, not causes

For each stall point, list possible reasons as hypotheses to test, each with what would confirm it. Draw them from sourced mechanics: for example, a Canadian license at risk because the QMS certificate copy was not sent within 30 days of issue (JX-35) or the annual statement not filed before 1 November (JX-33); a GB route at risk because the product was placed under MDD acceptance that ends 30 June 2028 or at certificate expiry (UK-02); a Swiss registration not confirmed before 31 December 2026 for devices placed from 1 July 2026 (JX-43). Label each "hypothesis". Never state a cause the facts do not show.

### Step 6. Route the response

Map each stall point to the work that responds, without choosing for the person:

| Stall point | Responding work |
|---|---|
| Classification or route changed in a region | Requirement map (DH-03.03.2.1 A1) |
| Evidence no longer meets a region's conditions | Harmonized evidence plan (DH-03.03.2.1 A2) |
| Sequence or reliance basis changed (a route lost, a draft adopted) | Regional submission adaptation (DH-03.03.2.1 B1) |
| Obligation not confirmed | The named owner, with the obligations table |
| Product divergence between regions | Change control in the quality system: document-and-change-control in this pack |

Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title.

## Build the output

Follow `assets/performance-review-output.md`. Short mode for a direct question: verdict per region, the stall point, the owner, and the one decision needed. Full mode adds the rule table, evidence and hypotheses.

## Before you hand it over

- Every rule and owner is the person's, and the output says so.
- Every verdict cites the fact behind it.
- Causes are hypotheses, labeled.
- No filing is declared missed on a date alone.
- Filings, wording for a regulator and plan changes stop for the regulatory owner.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge people or teams.
- No forecast of when a region will be back on track.
- Drugs, biologics and wellness apps are out of scope.
