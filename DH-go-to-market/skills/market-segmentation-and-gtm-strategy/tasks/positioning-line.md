# B2 Positioning line

Framework task: DH-02.01.2.1, Part B, task B2. Replaces the old "Positioning line" task.

## What this task delivers

One draft positioning line per chosen segment: who it is for, what changes for them, and what the product is not, written inside the intended use the person states and checked against the sourced promotion rules for the segment's market. Each line comes with the words that carry risk flagged, the claims it relies on marked as cleared (from the person's claim list) or `[GAP]`, and the stop for the regulatory or legal owner. It answers "how do we say what this is, for this segment?"

Why it matters: in every market read, what marketing says is part of the product's intended use (PC-US-17, PC-EU-03, PC-UK-01). A line that says more than the intended use changes the product's regulatory position, not just its message.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Marketing Manager (`digital-marketing-manager`) |
| Skill | DH-02.01.2.1 Part B, Positioning line |
| Workflow | The steps below |
| Knowledge | `references/positioning-rules.md`; `references/promotion-and-claims-sources.md` (PC rows); B1's chosen segments |
| Tools | None counted. Claim checks belong to the Commercial claims audit (DH-02.01.3.2) |
| Prompt | This guide |
| Template | `assets/positioning-line-output.md` |
| Input | The request and its context; chosen segments from B1; the intended use and device status as the person states them; the person's cleared claim list, if any; peers on record from A1 |
| Governance | `references/governance.md`; the line is the person's; claims stop for the regulatory or legal owner |
| Catalogue job | none. The line is drafted from the references and B1's chosen segments. |

## Read the request

- **Chosen segments.** Lines are written only for segments in scope (B1). A request for a line for an out-of-scope segment: say so and ask.
- **Intended use and status.** Required. Without it, write no line; mark `[GAP]` and say why (Rule 1 in `positioning-rules.md`).
- **Claim list.** The person's cleared claims, if any. A claim not on it is `[GAP]` in the line, never written as fact.
- **Market.** Each line is checked against its segment's market rules.

## Workflow

### Step 1. Fix the frame per segment

From B1 and the person: the user (who it is for), the job, the intended use in the person's words, and the market. Write them back.

### Step 2. Draft the line in three parts

- **For:** the user and setting, inside the intended population.
- **What changes:** the change the intended use supports, using only cleared claims; otherwise describe what the product does, not what it achieves.
- **What it is not:** one boundary that sets it apart (for example "not a replacement for your clinician", "not for diagnosis"). The register's method: reject a line that could describe a peer without change; compare against the peers on record from A1, by their public descriptions only.

Offer two or three drafts, all labeled "proposed".

### Step 3. Check each draft against the rules

For each draft, in its market:

1. **Intended use** (Rule 1): does any word extend the use, population or result? Mark the word.
2. **Wellness or device** (Rule 2): for a wellness product, any disease, threshold or "clinical grade" wording takes it out of wellness (PC-US-63). For a device, disease wording must match the cleared use.
3. **Approval words** (Rule 3): "FDA approved", "certified", "DiGA-listed", "NHS approved" only if true and within its terms (CP-US-74, PC-EU-11, PC-UK-08).
4. **Effect and certainty** (Rule 4): no guaranteed success or no-side-effect impression (PC-DE-04); in Germany, public device advertising may not suggest health improves with use (PC-DE-10).
5. **Device-indicating words** in Great Britain (PC-UK-04 list in `positioning-rules.md`): flag each hit for the owner; a hit is a flag, not a verdict.
6. **Comparisons** (Rule 5): any "better than" goes to the claims audit.

Record each finding with its row. Never rewrite a finding into "compliant"; the model does not clear.

### Step 4. Safer wording, for the owner

For each flagged word, offer a safer alternative inside the intended use, labeled "draft for the owner".

### Step 5. Stops

Any line that makes a clinical, comparative or economic claim, any use of approval or listing words, and any line for public use stops for the person's regulatory or legal owner, after the Commercial claims audit (DH-02.01.3.2). Name the owner the person gives; if none, "owner not named" and ask.

## Build the output

Follow `assets/positioning-line-output.md`. Short mode: one recommended draft per segment with its flags and the stop; other drafts in one line each. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every line is labeled "proposed" or "draft for the owner".
- Every flag cites its row; [INDUSTRY] and [WF] rows say so.
- No claim that is not on the person's cleared list.
- No peer described beyond its record.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- The model drafts and flags; it does not clear a line or a claim.
- No price, coverage status or listing presented as a benefit or as evidence of effect.
- Value messages and payer-facing economics: Commercial pricing (DH-02.01.3.1) and Market Access.
- Drugs, biologics and wellness apps are out of scope. Rule 2 is used only to show where wording would take a product across the wellness line, so the owner sees it.
