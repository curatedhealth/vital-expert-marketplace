# A2 Claims audit

Framework task: DH-02.01.3.2, Part A, task A2. Replaces the old "Audit claims" tool skill.

## What this task delivers

A claim-by-claim table for the material the person supplies (an ad, app store text, a website page, a payer deck, a sales leave-behind): each claim, its audience and market, the intended use it is judged against, the sourced rules it may cross (with row ids), whether the evidence passage behind it supports it in the same direction, a flag level, and a safer draft for the owner. The task flags; it never clears.

Why it matters: in digital health, promotional wording decides regulatory status (PC-US-17, PC-EU-03, PC-UK-01) and is enforced (PC-US-76, PC-US-77 [WF]; PC-DE-14; PC-UK-14 [INDUSTRY]). An audit that names the row and drafts a fix saves the owner's review time; one that says "looks fine" moves the risk to them unseen.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-02.01.3.2 Part A, Claims audit |
| Workflow | The steps below |
| Knowledge | `references/claim-rules.md`; `references/audience-rules.md`; `references/promotion-and-claims-research.md` |
| Tools | `verify.extract_claims`; `commercial-dh.audit_claims` (authorization on file only); `verify.qualify_source` and `verify.check_claim` per evidence passage; `verify.build_record`; `scripts/claim_screen.py` (optional) |
| Prompt | This guide |
| Template | `audit_claims` response for the record data; `assets/claims-audit-output.md` for the answer |
| Input | The request and its context; the material; the audience and market where it runs; the product's intended use per market from its label or authorization; the passages or documents behind any number or efficacy claim |
| Governance | `references/governance.md`; every flag and draft stops for the regulatory or legal owner |
| Catalogue job | `claim-labels` (`commercial-dh.audit_claims`, authorization on file only). The direct calls in the steps remain the method; the job is the buyer's one-call option (`start_job` returns the steps and inputs and runs nothing; `examples/live/start_job_runs.json`). |

## Read the request

- **Material.** Take the text the person gives. Do not scrape a website; claims arrive as text.
- **Audience and market.** Consumer, clinician, payor, professional circles (Germany) and market change which rows apply. If not stated, ask once; otherwise audit for the strictest audience the material could reach and say so.
- **Intended use.** Ask for the label or authorization wording. Without it, mark `[GAP]` and label every flag provisional.
- **Competitor material.** If the person asks to audit a competitor's claims, describe only what the material says and which rows a claim could engage; never conclude that a competitor broke a law.
- **Short or full?** "Is this ad OK" is short; "audit our launch materials" is full.

## Workflow

### Step 1. Split the material into claims

Call `verify.extract_claims` with the text. It splits by sentence; split compound sentences yourself ("Doctor-recommended and CE-certified" is two claims). Keep the offsets. With code execution, `scripts/claim_screen.py` lists candidate flags with row ids as a first pass; it finds wording, not meaning, and a person judges every hit.

### Step 2. Find the authorization on file

Call `commercial-dh.audit_claims` once with the exact identifier (K, DEN or P number, or Basic UDI-DI if the person gives one, otherwise the product name) and the claims (up to 20). Read the inner `get_authorization` and `search_devices` blocks: which record exists, route, class, regulation, source URL. Do not use the tool's labels or its evidence maturity score as findings (`references/tools.md`). If the name finds no authorization but the inner search finds a record, report the record and the mismatch.

### Step 3. Map each claim to rules

For each claim, find its type in `references/claim-rules.md` and list the rows it may cross for the audience and market (`references/audience-rules.md`). Label [INDUSTRY] and [WF] rows. Judge against the intended use the person stated: inside, outside, or not determinable `[GAP]`.

### Step 4. Check the evidence behind numbers and efficacy claims

For each claim with a number, an efficacy statement or a comparison, ask for the passage if the person has not given it. Call `verify.qualify_source` (DOI, PMID or URL), then `verify.check_claim` with the claim, the verbatim passage and the source. Read the passage yourself: same direction, same population, same comparator, same time point. A "supported" from the tool on a passage that only states a study's aim is not support (register N3). No passage: `[GAP]`, unsupported as worded.

### Step 5. Set a flag level and draft safer wording

| Level | When |
|---|---|
| Stop | The claim matches an "always unfair" or prohibited form (PC-EU-10, PC-EU-11, PC-UK-07, PC-UK-08, PC-DE-04, PC-DE-13, PC-DE-15) or goes beyond the stated intended use |
| Review | A row could apply depending on facts the owner holds (evidence quality, audience, context), or the passage does not support the claim as worded |
| Note | Disclosure or presentation points (citation details under PC-DE-05, prominence under PC-US-32) |

For each Stop and Review, draft safer wording that keeps only what the intended use and the passages support (`references/claim-rules.md`, last column), labeled "draft for the owner". Never write "compliant", "approved" or "OK to publish"; "no flag" means only that no sourced rule here was matched.

### Step 6. List what the owner decides

Each flag, each safer draft, each [INDUSTRY] or [WF] row relied on, each `[GAP]`. Name the owner the person gave, or "owner not named".

## Build the output

Follow `assets/claims-audit-output.md`. Answer first: how many claims, how many Stop, Review, Note, and the one that matters most.

## Before you hand it over

- Every flag cites at least one row, and every row is labeled by kind.
- Every evidence check names the passage; none rests on the tool's status alone.
- No sentence says the material is compliant or cleared.
- Count the words in short mode.
- If the audit leaves the conversation, ask who clears it and call `verify.build_record`, with the record text stating that it records the audit, not a clearance of the claims; otherwise label it an uncleared draft.

## Boundaries

- The skill never clears a claim; promotional review stops for the regulatory or legal owner.
- No conclusion that the product is or is not a device; that stays with dh-regulatory-strategy.
- No legal opinion on enforcement exposure.
- Drugs and biologics are out of scope.
