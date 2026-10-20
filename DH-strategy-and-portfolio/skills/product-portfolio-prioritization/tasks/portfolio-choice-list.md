# A1 Product portfolio choice list

Framework task: DH-01.03.3.1, Part A, task A1. Replaces the old "Portfolio choice" task (CF-12.01.03.3.1.1) and keeps its three steps: name the forum and the period, list the items asking for a continue, stop or delay, and name a request that is not ready for the forum, and why.

## What this task delivers

A choice list for one forum and one period: each product or program asking to continue, stop or delay, with its stage gate record, the facts the person and the public record give (stage, evidence, regulatory status, readiness level proposed, licensing position), the gaps, and the requests left off with one reason each. Items that are in-licensed, partnered or acquired carry a licensing flag block and a company status line. It answers "what is on the table, and is each request ready?"

Why it matters: a forum that ranks items without their records ranks opinions. A request with no stage gate record cannot be compared with one that has one, and a gap hidden in a slide becomes a surprise after the money is committed.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Chief Digital Health Officer (`chief-digital-health-officer`) |
| Skill | DH-01.03.3.1 Part A, Product portfolio choice list (CF-12.01.03.3.1.1) |
| Workflow | The steps below |
| Knowledge | `references/prioritization-methods.md` sections 5 to 7; `references/licensing-and-deal-flags.md`; `references/gap-rules.md` |
| Tools | `regulatory-dh.search_devices` or the identity block of `commercial-dh.generate_report` for a named product's public record only |
| Prompt | This guide |
| Template | `assets/choice-list-output.md` |
| Input | The request and its context: forum, period, items with their stage gate records, stage, evidence and status as the person states them, the person's licensing facts, named owners |
| Governance | `references/governance.md`; the person decides which items come to the forum |
| Catalogue job | none. No catalogue job covers product portfolio choices (`references/tools.md`). |

## The rule that shapes this task: records before rankings

An item comes to the forum with its stage gate record or it is listed as not ready (old method: "Do not bring a request that has no stage gate record"). Facts come from the person's records and the public record, each with its source; nothing is filled from memory. The model lists and checks; it does not decide which items come to the forum.

## Workflow

### Step 1. Forum, period and scope

Write back the forum and the period as the person gives them. If either is missing, write "not given" and ask. Confirm the list is the **product portfolio** (the company's own products and programs). If the request mixes in companies held as investments, separate them and route those to `investment-portfolio-monitoring` (this pack); if "portfolio" is ambiguous, ask which one before listing anything.

### Step 2. The items and their asks

For each item: name, the ask (continue, stop, delay, or the person's words), the stage as the person states it, and the stage gate record (reference and date) the person points to. An item without a stage gate record goes to the "not ready" list with that reason and a route to `dh-clinical-development` clinical-product-lifecycle-and-stage-gates. Other not-ready reasons the person states are written in their words.

### Step 3. Facts beside each item

For each ready item, set out the facts that the person's criteria will need, each with its source:
- **Evidence and readouts** as the person states them, with dates. Evidence quality is not judged here; a reading routes to `dh-clinical-development` literature-and-real-world-evidence-review.
- **Regulatory status** as the person states it. For a named product with a public authorization, the library record with reference, decision date and retrieval date (`regulatory-dh.search_devices {query, jurisdiction}` or the submission number; `references/tools.md`). Use FDA words: cleared, granted, approved. State who lists the product with FDA today as a separate fact from the company that was authorized (`licensing-and-deal-flags.md` section 4; for example Somryst: 510(k) K191716 cleared to Pear Therapeutics, Inc. on 23 March 2020, SP-165; listed today by Nox Medical, listing created 18 December 2024, SP-167). Pathway questions route to `dh-regulatory-and-quality` regulatory-pathway-and-classification.
- **Readiness level, proposed**: where it helps, the EU TRL wording verbatim with its row (SP-029 to SP-031) and the fact behind the level; say NASA 7 to 9 assume space and flight (SP-035). Marked "proposed" until the person confirms.
- **Benchmarks, context only**: if the person asks how programs like theirs usually fare, give the figure with its counting method and DOI (SP-082 to SP-087, `prioritization-methods.md` section 5), say the rows are drug-program figures and that no row gives a software or medtech rate `[GAP]`. Never write it as the item's probability.
- **Delay routes** where the ask is delay pending evidence: the sourced routes as facts (SP-110 to SP-129, `prioritization-methods.md` section 7).
- **Capacity ask** in the person's unit and period, or "not given".

### Step 4. Licensing, partnering and acquisition items

For an item that is in-licensed, out-licensed, partnered or acquired, add the flag block from `licensing-and-deal-flags.md` section 2, each fact cited by source name and date with its row: Regulation (EU) 2026/877 of 16 April 2026, in force 1 May 2026 (SP-135); the 20% combined (competitors) and 30% per-party (non-competitors) conditions on any relevant market (SP-136); the transition to 30 April 2027 only for agreements in force on 30 April 2026, so a new license is not covered (SP-137); the DOJ/FTC safety zone of 12 January 2017 (SP-144 to SP-146); SEC exhibit and 8-K rules if a party is listed (SP-130 to SP-133, DL-019 to DL-021); and GDPR Article 9 if the deal moves health data, for example data to train a model (DL-101, DL-105, DL-106). Put each threshold beside the person's figure, or "not given", without leaning, for the owner the person names for legal. List the deal facts not given (relevant market, shares, whether the parties compete, agreement date, health data moved). Conclusions go to the owner the person names for legal, or owner not named.

Where a candidate in-license and an item already on the list address the same indication (for example Somryst and an own insomnia DTx), list the overlap and ask whether the parties compete. The competitor test selects the 20% combined or 30% per-party condition (SP-136). The answer is for the owner the person names for legal.

### Step 5. Company status of a named counterparty

For each licensor, licensee, partner or target named, add the status line (`licensing-and-deal-flags.md` section 3, DL-135 to DL-168). For Pear Therapeutics, Akili, Big Health and Aidoc, quote the dated filings and FDA records read on 20 October 2026 (SP-148 to SP-169; SEC rows [WF]), with what each form does not mean. For Somryst that means: Pear 8-K, 7 April 2023: chapter 11 filed in Delaware, case 23-10429, section 363 sale process with no buyer named (SP-156, SP-159); Pear 8-K, 10 April 2023: Nasdaq delisting notice (SP-160); Form 25-NSE, 2 May 2023, the last filing (SP-155); no SEC filing names a buyer (SP-161); Nox Medical lists the device today (SP-167). So the counterparty is unconfirmed: ask who the person is negotiating with, and say the company in the library record may no longer hold the product. For any other company, quote the filing or register item read with its date, or write "Company status [GAP]: not read" and list the filings to open, most recent first (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House `company_status`; German insolvency notices). Never infer status from press, memory or when filings stopped. Requests to outside sites never carry the person's email address or name; for EDGAR, ask which User-Agent contact the person's organization uses (DL-153).

### Step 6. The not-ready list and the open questions

List each request left off with one reason. Then list what the forum will need before B1: the person's criteria and weights, missing facts per item, capacity.

## Build the output

Follow `assets/choice-list-output.md`. Answer first: the forum and period, how many items are ready and how many are not, and the gap that blocks most. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Count with `python3 scripts/portfolio_rank.py words ANSWER.md`.

## Before you hand it over

- Every item is a product or program of the person's company; no investment holding is on the list.
- Every fact has its source and date; every missing fact is `[GAP]` or "not given".
- Every item without a stage gate record is on the not-ready list with the route.
- Readiness levels are verbatim EU wording, "proposed"; benchmarks carry method and DOI and are not probabilities.
- Licensing items carry the flag block, the thresholds beside the person's figures, any overlap that bears on the competitor test, and a status line; the authorized company and the current listing holder are stated separately; no license called exempt.
- Each fact names its source and date in plain words, then the row id; inference rows say "(inference)".
- `python3 scripts/portfolio_rank.py words ANSWER.md` prints "within the short-mode cap" for a short answer.
- The record line is the last line of the answer body (any calls list follows it): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- The list does not rank, score or decide; that is B1 and B2, on the person's numbers.
- Stage gate records are written in `dh-clinical-development` clinical-product-lifecycle-and-stage-gates, not here.
- A company profile in depth: `company-and-evidence-assessment` (this pack). Deal facts for a memo: `investment-memo-and-decision-record` (this pack).
- No market size, valuation, price or return for any item.
