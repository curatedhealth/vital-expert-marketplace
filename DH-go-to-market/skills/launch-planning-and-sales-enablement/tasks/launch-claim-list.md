# A2 Launch claim list

Framework task: DH-02.01.1.1, Part A, task A2. Replaces the earlier "Launch claim list" section.

## What this task delivers

The claims this launch proposes to use, one row each: the claim text, the market and audience, the evidence it rests on, the authorization it must stay within, the flags from the sourced promotion rules, and safer wording drafted for the owner where a flag applies. Claims without a source stay off the list. The list is a draft for the person's regulatory or legal owner, who approves it; nothing here clears a claim.

Why it matters: in digital health the marketing copy is part of what the product legally is. Labeling claims, advertising and statements show intended use in the US (PC-US-17); in the EU intended purpose includes promotional materials (PC-EU-03); in Great Britain the app store description and landing page count (PC-UK-01). One sentence in a leave-behind can turn a wellness app into an unauthorized device or a cleared device into an off-label promotion.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Adoption Lead (`digital-adoption-lead`) |
| Skill | DH-02.01.1.1 Part A, Launch claim list |
| Workflow | The steps below |
| Knowledge | `references/claim-rules.md`; the person's labeling or intended-use text; A1 output for markets and authorizations |
| Tools | `commercial-dh.audit_claims` (optional, with the person's say); `verify.qualify_source` then `verify.check_claim` for published evidence; `literature.search_literature` to find a source the person names but cannot cite; `scripts/claim_screen.py` (optional) |
| Prompt | This guide |
| Template | `assets/launch-claim-list-output.md` |
| Input | The request and its context: product, markets, audiences (HCP, payer, patient or consumer), the draft claims, the labeling or intended-use text, the sources the person holds |
| Governance | `references/governance.md`; the regulatory or legal owner approves |
| Catalogue job | `claim-labels` (audit_claims) for the connector's labels; `evidence-table` (literature.*) for published evidence. The direct calls in the steps remain the method. `examples/live/list_jobs_commercial.json` |

## Read the request

- **Claims.** Take the person's draft claims verbatim. If they ask "what can we say", start from the authorized indication text they supply; do not write new claims beyond it.
- **Authorization and labeling.** Ask for the indication or intended-use text as authorized (510(k) indications, De Novo, CE declaration, DiGA directory entry). Without it, claims cannot be checked against labeling: say so and mark `[GAP]`.
- **Market and audience per claim.** Rules differ for payers, HCPs and consumers, and in Germany for public versus professional audiences.
- **Sources.** The study, label or contract behind each claim. A claim carried over from a previous product does not count as sourced (old task rule).
- **Owner.** Who approves claims, in the person's words, or "owner not named".

## Workflow

### Step 1. One row per claim

Split compound sentences into single claims. Record market, audience and the source the person gives. A claim with no source goes to the "not on the list" section with `[GAP]`.

### Step 2. Screen the words (optional script)

First check that the product named in the material is the person's product. If the text names another product (for example a competitor's brand), flag that before any claim and ask; such material cannot be used as written.

With code execution, save the claims as a text or CSV file and run `scripts/claim_screen.py --claims FILE`. It lists risk-word hits with the row behind each (`references/claim-rules.md` section 4). A hit is a prompt to read the claim; no hit does not clear it.

### Step 3. Check each claim against the authorization

Compare the claim with the labeling text the person supplied. Apply the flags in `references/claim-rules.md` section 3 (on record, check against labeling, beyond the authorization, no authorization shown, blacklist risk, needs evidence, audience mismatch, coverage or price statement, discourages treatment), each with its rows. For US claims to HCPs, apply the consistent-with-labeling tests (PC-US-22 to PC-US-25); for payers, the HCEI elements (PC-US-04 to PC-US-07); for consumers, the FTC substantiation rows and, for wellness products, PC-US-63.

### Step 4. Connector labels, if the person agrees

`commercial-dh.audit_claims` sends the claim text to the library. Ask first. Pass `reference` (FDA number for US products) and up to 20 claims. Record each label as "connector label" beside your flag. Today the library stores no intended purpose text, so labels do not separate on-label from off-label claims (`references/tools.md`); never let a label replace step 3.

### Step 5. Check the evidence

For each claim resting on a publication: `verify.qualify_source` with the DOI, then `verify.check_claim` with the claim, a passage the person or the record supplies (`{text, locator}`) and the source. Accept support only when the passage reads in the same direction as the claim; otherwise flag "needs evidence". Do not send register pages or regulator guidance to Verify; cite them to their URL. In Germany, a cited study must say whether it concerns the advertised product, with author, date and source (PC-DE-05).

### Step 6. Draft safer wording for the owner

For each flagged claim, write a safer version that stays within the authorization and the evidence, labeled "draft for the owner". Do not invent a new claim. Where no safe version exists inside the authorization, say so.

### Step 7. Stops

List what goes to the regulatory or legal owner: every flag except "on record", every coverage or price statement (and payer matters to Market Access), every payer communication. Name the owner the person gave, or "owner not named".

## Build the output

Follow `assets/launch-claim-list-output.md`. Answer first: how many claims are on the proposed list, how many are flagged, and the one flag that matters most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every claim has a source or sits off the list with `[GAP]`.
- Every flag has its rows; [INDUSTRY] and [WF] rows are labeled.
- The list is called "proposed claim list, for approval by OWNER". Nothing is described as cleared, approved or compliant.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Checking claims already in the market and value messages is Commercial 3.2; price positioning is Commercial 3.1.
- Payer communications, prices and coverage claims: Market Access and the accountable owner.
- Device status or a new indication: the regulatory owner and the Regulatory pack.
- Drugs and biologics are out of scope.
