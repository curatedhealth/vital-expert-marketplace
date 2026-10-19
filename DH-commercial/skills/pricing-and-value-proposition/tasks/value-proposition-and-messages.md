# B1 Value proposition and messages

Framework task: DH-02.01.3.1, Part B, task B1. Replaces the old "Value message" section.

## What this task delivers

A value message map, drafted for the owner: for each audience the person names (payer, economic buyer, clinician, patient), the message, the outcomes it uses with the source behind each, the rules that bind that audience in that market with row ids, the wording the rules require (disclosures, statements of material differences, "not cleared" statements), and the wording the rules exclude. Every message is a draft for the person's regulatory or legal owner.

Why it matters: in digital health the marketing copy decides the regulatory status of the product (PC-US-17, PC-EU-03, PC-UK-01), and a payor message is a regulated communication of its own (PC-US-04). A strong message that steps outside the intended use costs more than it earns.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-02.01.3.1 Part B, Value proposition and messages |
| Workflow | The steps below |
| Knowledge | `references/audience-rules.md`; `references/promotion-and-claims-research.md`; A1 (roles, unit) and A2 (price evidence) if run |
| Tools | `verify.qualify_source` and `verify.check_claim` for each published passage an outcome rests on; `verify.extract_claims` and `commercial-dh.audit_claims` for a case study; `verify.build_record` |
| Prompt | This guide |
| Template | `assets/value-message-output.md` |
| Input | The request and its context; the product's cleared or certified intended use, per market, in the person's words or from their labeling; the outcomes the person can point to, with the passage or document; the audiences |
| Governance | `references/governance.md`; every message stops for the regulatory or legal owner |
| Catalogue job | `health-system-value-brief` for the value case of a health-system message (numbers the person types or adopts); `claim-labels` for the authorization record. The Verify steps below remain the method for every outcome. `examples/live/job_health_system_value_brief_somnio.json` |

## Read the request

- **Intended use per market.** The anchor for every message. If the person cannot state it, mark `[GAP]`, say every message is provisional, and point to the person's regulatory owner or the dh-regulatory-strategy pack.
- **Cleared yet?** For a US product not yet cleared, a payor message runs under 502(gg) only (PC-US-08 to PC-US-10); clinician and consumer promotion of the uncleared use is not drafted.
- **Audiences.** Use the audiences the person names. A US "payer deck" that will also sit on a public website is two audiences (PC-US-35).
- **Health-system buyer?** If the audience is a health system, ask whether the person wants a value case on their own numbers (catalogue job `health-system-value-brief`; see Step 5) and whether a customer case study will be used (Step 2b).
- **Claim list.** The outcomes the message may use come from the person's claim list or evidence. The model does not add outcomes.
- **Short or full?** "A line for our payer slide" is short; "value proposition document" or "message house" is full.

## Workflow

### Step 1. State the value proposition in one sentence per audience

Use A1's roles: what the user gets, what the buyer gets, what the payer gets, in the person's words. Use only outcomes the person can point to. Mark an outcome with no passage as `[GAP]` rather than a number.

### Step 2. Check every outcome against its passage

For each outcome from a published source, call `verify.qualify_source` with the DOI, PMID or URL, then `verify.check_claim` with the outcome as the claim, the verbatim passage (`text`, `locator`) and the returned source. Accept "supported" only after you have read the passage and it states the outcome in the same direction, for the same population and comparator (register N3: the tool decides on overlap, and a negated claim came back "partial", not "contradicted"). If the passage only states a study's aim or design, the outcome is `[GAP]`. Do not send register facts (listings, prices) to Verify.

If the person's result does not say whether a figure is a difference between arms or a change within one arm, ask, and word it as the person gave it ("a 7-point drop in ISI at 8 weeks, compared with sleep hygiene education") until the passage settles it. Never write "greater than" or "more than" from the person's summary alone.

### Step 2b. A case study is a claim

A customer case study used in a sale is the company's own claim (PC-UK-03; in German public advertising, third-party statements used in a misleading way are banned, PC-DE-11). Treat every result in it like any other outcome:

1. Split it into single claims with `verify.extract_claims` on the case-study text.
2. Call `commercial-dh.audit_claims` with `reference` (exact regulatory identifier) and those claims. Report the authorization record it returns; report a label only as the connector's label, never as a finding (no intended purpose is stored, so on-label claims come back `exceeds_record`; `references/tools.md`).
3. For each result, ask for the document it rests on (the customer's report or a publication). Qualify it with `verify.qualify_source`, then `verify.check_claim` with the verbatim passage, accepted only when read in the same direction (register N3). A result with no document is `[GAP]` and stays out of the message.
4. Apply the audience rules in Step 3 to each claim: a single site's result is not a product effect, and its population, comparator, period and denominator travel with it.
5. Customer-identifying details (name, logo, people, site): the rows hold no rule on the customer's written permission to be named, so write "customer permission to be named: [GAP], for your legal owner". Where the case study uses a patient's health information that a covered entity discloses for marketing, individual authorization applies (PC-US-87); for a DiGA, its personal data may not be used for advertising (PC-DE-16).

### Step 3. Apply the audience rules

Open `references/audience-rules.md`. For each audience and market, list the rows that bind the message and what each requires:

- US payor, cleared indication: HCEI conditions (PC-US-04), study design, limitations and sensitivity analyses presented (PC-US-40), a conspicuous statement of material differences from labeling where applicable (PC-US-04), not for prescribers or a public website (PC-US-35). Name the 2018 final and the June 2026 revised draft status (PC-US-47).
- US payor, before clearance: the required statements, permitted content and factual results only (PC-US-08 to PC-US-10, PC-US-44, PC-US-45).
- US clinician: consistent with labeling. PC-US-22 applies only to 510(k) and 510(k)-exempt devices; PC-US-23 and PC-US-24 apply to De Novo and PMA devices; PC-US-25 to PC-US-31 apply to both. Cite only the rows for the product's route.
- US consumer: FTC substantiation [WF] (PC-US-72, PC-US-73); for a wellness product the 2026 wellness limits (PC-US-63).
- EU, Germany, UK: MDR Article 7 (PC-EU-01, PC-EU-02); HWG, and the stricter public rules outside Fachkreise (PC-DE-03 to PC-DE-13); DiGA ad-free (PC-DE-15); DMCCA and CAP Code [INDUSTRY] (PC-UK-05 to PC-UK-13).

### Step 4. Draft each message inside the rules

Write the message for each audience. Next to it, write the disclosures the rows require. Where a message the person wants would cross a rule (a cure claim, a comparison outside the cleared population, a health-improvement promise to German consumers, an uncleared use to US clinicians), do not draft it; write the row it crosses and a safer wording that the facts support, labeled "draft for the owner". Describe a competitor only by what its record or public source states.

### Step 5. Price in the message

If the message states a price or a budget impact, it is a price position and, for a US payor, HCEI (PC-US-06, PC-US-36). Use A2's numbers with their kinds and labels. For a health-system value case, run A2 Step 5 (the `health-system-value-brief` route) on numbers the person types or adopts; a rejected calculator or the unexposed scenario and sensitivity tools are `[GAP]`, never filled. Never state a price as secured or a coverage outcome as achieved.

### Step 6. Route for review

List what the owner must decide: each message, each disclosure, each [INDUSTRY] code applied, each [WF] row relied on, each `[GAP]`. PC-US-33 recommends review by qualified medical or scientific, legal and regulatory personnel before release; name the owner the person gave, or "owner not named".

## Build the output

Follow `assets/value-message-output.md`. Answer first: the one-sentence proposition per audience. Then the message map.

## Before you hand it over

- Every outcome has a passage read in the same direction, or is `[GAP]`; case-study results included, with customer permission to be named marked `[GAP]` unless a sourced row covers it.
- Every message has its binding rows and required disclosures; [INDUSTRY] and [WF] rows are labeled.
- No message claims clinical effect from a listing, a price or uptake.
- Count the words in short mode.
- Label the whole output "draft for the owner"; if it leaves the conversation, call `verify.build_record` with the named clearer, or label it an uncleared draft.

## Boundaries

- The skill never clears a message or says it complies with any law or code.
- No message for an uncleared use to clinicians or consumers.
- Wording for a payer negotiation, an HTA dossier or a reimbursement submission belongs to dh-market-access (payer-engagement-and-hta-submission) and stops for its owner.
- Drugs, biologics and wellness apps outside the 2026 wellness policy are out of scope.
