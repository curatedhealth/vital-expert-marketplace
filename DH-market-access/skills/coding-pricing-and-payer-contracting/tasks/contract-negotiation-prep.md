# B1 Contract negotiation preparation

Framework task: DH-03.01.2.1, Part B, task B1 (old name: Contract Negotiation).

## What this task delivers

A preparation brief for one negotiation: who the counterparty is and how the process runs, the clocks that bound it, the inputs the counterparty will require, the terms that are mandatory and those that are open, and the person's own objectives and walk-away, written in their words. It answers "what are we walking into, and what must we decide before we sit down?"

Why it matters: in a DiGA negotiation the statute already fixes part of the deal (at least 20 percent outcome-linked from 2026, volume discounts from 2027) and the clock (arbitration after nine months). Teams that prepare only a price arrive without the submissions the GKV-Spitzenverband requires and without a position on the open terms.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-03.01.2.1 Part B, Contract negotiation preparation |
| Workflow | The steps below |
| Knowledge | `references/contract-terms.md`; `references/price-rules.md`; `references/outcomes-contracting-sources.md` (cite only); A1 and A2 outputs |
| Tool | None required; A1 and A2 tools if their outputs are missing |
| Prompt | This guide |
| Template | `assets/contract-negotiation-prep-output.md` |
| Input | The request and its context; the person's objectives, constraints, walk-away and named negotiator; A1 and A2 results |
| Governance | `references/governance.md`; pricing position and terms stop for the owner |

## The rule that shapes this task: people decide

The person sets objectives, priorities, opening position, concessions and walk-away. The model lays out the process, the fixed and open terms, and what the counterparty will ask for. Where the person asks for a proposal, it may offer options marked "proposed", each tied to a fact, and does not write a number for price, discount or walk-away.

## Workflow

### Step 1. Name the counterparty and the process

From `references/contract-terms.md`: Germany, GKV-Spitzenverband, agreed amount applies from month 13, arbitration if no agreement nine months after listing, award within three months (DE1, DE5, DE9). France, CEPS after CNEDiMTS, within the 180-day clock (FR1, FR4); clauses not sourced. US, no Medicare fee negotiation (fee schedule, MAC pricing for G0552); ACCESS participation terms; commercial payers `[GAP]`. England, framework buyers and MTFM (EN2, EN4). If the product's listing date is known, count the clocks from it and state the dates.

### Step 2. List the inputs the counterparty will require

Germany: evidence and trial results, self-pay prices and prices in other European countries, in-use outcome measurement results (DE4). France: HAS evaluation file and interoperability certificate (FR4, FR6). ACCESS: baseline measures via API within 60 days of alignment, end-of-period measures (outcomes file, "ACCESS: verification data"). For each, mark whether the person has it, does not, or `[GAP]`.

### Step 3. Mandatory terms

Write the terms the law fixes: 20 percent minimum outcome-linked share (DE2), volume discount tiers from 1 January 2027 (DE3), and, as context only, the year-one group maximum and threshold for the product's own group (DE7, DE11, DE14, DE15); never quote a group's maximum when the indication is not given. ACCESS: 50 percent withhold of the Medicare portion (80 percent of the allowed amount; BH initial $72 of $180), 50 percent outcome attainment threshold, 90 percent substitute spend threshold (US32, US33). State the conflict: the 2024 framework says outcome components "can" be agreed while the statute requires them, with no implementing agreement found (contract-terms.md).

### Step 4. Open terms

List what the parties define: outcome measures and attainment method, share above the minimum, discount levels and tiers beyond the statutory floors, data delivery, termination. For each, note what the evidence in hand supports (from A2 and the person's data) and leave the position blank for the person.

### Step 5. The person's objectives and walk-away

Ask for, and write back in their words: two or three objectives ranked by them; constraints; the walk-away condition; who negotiates and who signs. If they decline to give a walk-away, write "not set". Never fill it. Say what walking away means here: in Germany no agreement does not end reimbursement; the arbitration board sets the amount within three months and the award stands during a lawsuit (DE5). The walk-away is therefore weighed against a possible award, not against no deal. Do not estimate the award.

### Step 6. Risks the facts show

From sourced rules only: for example the arbitration award stands during a lawsuit (DE5); data for outcome components may not exist before AbEM data from 15 April 2027 (outcomes file, "Payer and industry position"); a 2027 PFS proposal that would change the economics of a US route (US25 to US27, proposed). State each as conditional.

### Step 7. Stop

The brief ends with the decisions the owner must take. No price, no concession, no wording for the counterparty is drafted unless the owner asks, and then it is a draft for the owner.

## Build the output

Follow `assets/contract-negotiation-prep-output.md`. Short mode: counterparty and clock, the three inputs most at risk, fixed vs open terms, and the decisions the person owes. Full mode adds the full input checklist and the risk table.

## Before you hand it over

- Objectives, walk-away and owner are the person's, and the brief says so.
- Every mandatory term carries its row; every clock its anchor date.
- No price or concession is proposed by the model.
- Outcome-contract attainment is not presented as clinical evidence.
- If it leaves the conversation, ask who clears it and call `verify.build_record`.

## Boundaries

- The model prepares; it does not negotiate, send, or commit.
- Outcome-based contract design in depth belongs to the value-based care skill (DH-03.01.1.1).
- Drugs, biologics and wellness apps are out of scope.
