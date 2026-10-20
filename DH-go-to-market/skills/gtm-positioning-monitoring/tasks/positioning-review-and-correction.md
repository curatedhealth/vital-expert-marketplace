# B1 Positioning review and correction

Framework task: DH-02.01.2.2, Part B, task B1. Replaces the old "Positioning correction" task and folds in the pass rule and owner steps.

## What this task delivers

A review draft that says, artifact by artifact, whether the in-market copy meets the person's pass rule; for each miss, whether the line or the claim list is what must change; and one correction per miss: the artifact, the owner the person names, and the date the person sets for the corrected artifact to replace the current one. Movement from A2 that touches the positioning is weighed as a reason to revisit the line itself. It answers "are we on message, and what do we fix?"

Why it matters: without a rule written before the sample, every review reopens what "on message" means. A correction with no owner, or one made in a slide customers never see, does not change what the market hears.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.01.2.2 Part B, Positioning review and correction |
| Workflow | The steps below |
| Knowledge | A1 and A2 outputs; `references/positioning-rules.md`; `references/monitoring-signals.md` |
| Tools | A2's tools if no movement read exists; `scripts/positioning_check.py` (optional) |
| Prompt | This guide |
| Template | `assets/review-and-correction-output.md` |
| Input | The request and its context; the person's pass rules, named owners and dates; A1 sample and A2 movement |
| Governance | `references/governance.md`; people set rules, owners and dates; claims stop for the regulatory or legal owner |
| Catalogue job | none. Review and correction are the person's decisions on A1 and A2. |

## The rule that shapes this task: people judge

The person writes the pass rules and decides whether an altered line passes, whether the line or the claim list is wrong, who owns each correction and by when. The model checks results against the rules, lays out options with their basis, and labels proposals "proposed". It never sets a date, names an owner, or calls an artifact compliant.

## Workflow

### Step 1. Gather the evidence

Use A1 (sample and flags) and A2 (movement) from the conversation. If A1 is missing, run it first; a review without a sample of in-market copies is not possible. Without A2, say that movement was not reviewed.

### Step 2. Confirm the pass rules

Start from the check set's rules. Offer the register's shape if the person has none: "the line is present and no contradicted claim is present". Ask whether an altered line passes. Write the rules back for confirmation. An artifact without a rule gets a factual summary and no verdict.

### Step 3. Check each artifact

Mark each in-market artifact meets or misses its rule, or not measurable `[GAP]`, with the evidence: the line status and the quoted sentence. Never average artifacts into one score.

### Step 4. Line or claim list?

For each miss, lay out which is wrong, as options for the person:
- **The artifact drifted** (the line and claim list still hold): the artifact changes.
- **The line no longer holds** (A2 shows a peer now matches the "what it is not" boundary, a route the line names changed, or a wording rule moved): the line is revisited in the segmentation skill (B2).
- **The claim list is wrong or incomplete** (a claim in market is not on the list): the claim goes to the claims audit (DH-02.01.3.2); the artifact does not carry it until cleared.
Label each reading "hypothesis for review", with what would confirm it.

### Step 5. One correction per miss

Record: artifact, what changes (line, claim or wording; proposed unless the person gave it), the owner the person names, the date the person sets for the corrected copy to replace the current one in market. Missing owner: "owner not named"; missing date: "date not set"; ask. The register's method: do not correct the line in a slide that customers will not see; corrections apply to in-market copies.

### Step 6. Stops

Flagged claims and approval or listing wording go to the claims audit and the regulatory or legal owner. Withdrawing or replacing an artifact in market, and any external statement about a correction, stop for the artifact's owner. When asked for corrected copy, draft only wording inside the stated intended use, labeled "draft for the owner".

## Build the output

Follow `assets/review-and-correction-output.md`. Short mode: verdict per artifact with evidence, the corrections with owner and date, the stop, and the record line. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every rule, owner and date is the person's, and the output says so.
- Every verdict cites the line status and the quoted sentence.
- Readings of "line or claim list" are hypotheses, labeled.
- No artifact called compliant; no claim cleared.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model checks and structures; it does not judge the people who wrote the copy.
- No forecast of the effect of a correction on sales or share.
- Drugs, biologics and wellness apps are out of scope.
