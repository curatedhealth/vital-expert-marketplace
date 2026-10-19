# B1 Contract structuring

Framework task: DH-03.01.1.1, Part B, task B1. Replaces the earlier "Outcomes Contract Structuring" section.

## What this task delivers

A term sheet structure for an outcomes-based contract, with the design test run first: which uncertainty the contract addresses, whether the data exists, and whether the value of the information exceeds the cost of running it. Then the sections every term sheet needs (measures, baselines, attainment rule, payment link, data flow and verification, lost-to-follow-up handling, dispute and audit, confidentiality, exit), each filled with the person's terms or left open. It answers "what does our contract have to say, and is it worth doing?"

Why it matters: ISPOR and the OECD both record that negotiation, monitoring and evaluation costs can sink an arrangement, and that recouping money or delisting is hard once it is running. The terms that decide this (who counts as a failure, who verifies the data, how to leave) are the ones most often left implicit.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.1.1 Part B, Contract structuring |
| Workflow | The steps below |
| Knowledge | `references/contract-terms.md` (design test, term sections, anchors); `references/risk-share-models.md`; `references/outcome-measures.md` |
| Tools | `scripts/payment_scenarios.py` for the payment-link section; A1 and A2 tools if they have not run |
| Prompt | This guide |
| Template | `assets/contract-structuring-output.md` |
| Input | The request and its context; A1 measures and A2 option if run; the person's terms, owners and walk-away points |
| Governance | `references/governance.md`; every term stops for the owner |

## Read the request

- **Counterparty and route.** GKV-Spitzenverband price agreement, a single sickness fund under § 140a, an ACCESS participant, or a commercial payer. The route decides which terms are fixed by rule and which are open.
- **What is already decided.** Measures (A1), design (A2), any agreed price or share. Ask for the person's terms, owners and walk-away points; never supply them.
- **Audience.** Internal working draft or a document for counsel or the owner. Nothing in this task is wording for the payer.
- **Mode.** Short for a direct question; full for a document.

## The rule that shapes this task: people set terms

The person sets every value: share at risk, threshold, windows, cap, price, term length, walk-away point. The model structures, checks consistency, and shows consequences. If asked to propose a value, it marks it "proposed", names the anchor it borrows from (for example the ACCESS 50 percent threshold), and says that borrowing a public model's number is a choice, not a norm. Every term, proposed or given, stops for the accountable owner.

## Workflow

### Step 1. Gather what is decided

Use A1 (measures) and A2 (design) from the conversation. If either is missing and the person wants a full structure, run it in short mode first. Write back what is already decided and what is open.

### Step 2. Run the design test

Ask and record the answer to each, with the facts that bear on it (`references/contract-terms.md`):

1. **Name the uncertainty.** Which uncertainty does this contract share or resolve? If none is named, stop and say so.
2. **Confirm the data source exists.** For each measure, which source holds it for this population, by when, and who can reach it. A measure whose data will not exist in time fails here (for example AbEM PROMs before Stage II in 2027).
3. **Value of information exceeds administration cost.** Ask what the threshold rests on: what share of patients met the same improvement definition in the listing study or real-world data. If the threshold is near that rate, say the risk carried is high. Ask the person for their view of the money at stake and the cost of collecting, verifying and reconciling. Use A2's arithmetic for the money at stake. The person judges; the model lays out both sides.

If a test fails, say so first and lay out a financial-only alternative for the owner.

### Step 3. Fill the term sections

Go through the ten sections of `references/contract-terms.md` in order. For each: the person's term if given; otherwise "open" with the question that settles it and the sourced anchor that shows how a public model handled it. Do not fill a value the person has not given unless asked, and then mark it "proposed".

### Step 4. Check consistency

Look for terms that undo each other and name them:

- An all-or-nothing patient rule with dropouts in the denominator, but no baseline window or data-completeness duty: missing data becomes lost payment.
- A payment date before the data exists (German outcome component from 1 January 2026, AbEM data from 15 April 2027).
- Self-reported values used for a measure where the anchor model forbids them (ACCESS allows self-report only for weight and PROMs). Diaries and symptom scores are patient-reported and allowed under that anchor; raise verification instead (who checks values, validity window).
- A share at risk below a legal floor (German 20 percent).
- A fund deal that may stack on the national outcome component. The national share is at least 20 percent (§ 134 SGB V; DE-19), so never state a maximum combined exposure. Ask whether the fund share applies to the same price base, and leave the combined figure to the person.
- No exit or review clause, given OECD's finding that recouping and delisting are hard.

### Step 5. Show the payment link

Run `scripts/payment_scenarios.py` on the person's payment terms at three to five attainment rates they choose, or compute by hand. Show the result beside the payment-link section.

### Step 6. List what the owner must decide

A numbered list of every open term and every proposed value, each with the owner the person named or "owner not named".

## Build the output

Follow `assets/contract-structuring-output.md`. Short mode answers first: does the design test pass, which terms are set, which are open, and the inconsistencies found. Full mode adds the full term table and payment scenarios.

## Before you hand it over

- The design test result is stated first.
- Every term is the person's or marked "proposed" with its anchor.
- Every anchor cites its row.
- The whole term sheet is labeled "draft for the owner": contract terms, risk-share terms, pricing and any wording for a payer stop for the accountable owner.
- Attainment under the contract is never described as clinical evidence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No legal drafting of clauses; this is a structure for the owner and their counsel.
- No statement that a payer will accept any term.
- Drugs, biologics and wellness apps are out of scope.
