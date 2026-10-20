# A1 Channel measure sheet

Framework task: DH-02.01.4.2, Part A, task A1. Replaces the register task "Channel measure" (CF-12.02.01.4.2.1).

## What this task delivers

A measure sheet per partner type, written with the person: the counts, how each is defined and counted, the period, the person's threshold, which count forces a hold, and the duties the rules set that the review must check (breach notices, sub-processor changes, patient engagement caps, disclosure). It answers "what does a healthy partner look like for us, and what must we watch?"

Why it matters: without rules written before the numbers arrive, every review reopens what "good" means and the partner's own slide becomes the record. The register method counts from the handoff record and does not score a partner on leads it did not hand off.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Partnerships Director (`digital-partnerships-director`) |
| Skill | DH-02.01.4.2 Part A, Channel measure sheet |
| Workflow | The steps below |
| Knowledge | `references/monitoring-signals.md`; the channel design (role cards, handoff events, terms) if the conversation holds it |
| Tools | `diligence-dh.get_funding_signals` or `diligence-dh.get_deltas` for a partner that is a public filer or a regulated company (optional) |
| Prompt | This guide |
| Template | `assets/measure-sheet-output.md` |
| Input | The request and its context: partner types, the handoff event as defined, what data the person holds, the terms in force (BAA, processor, compensation) |
| Governance | `references/governance.md`; the person sets every measure, threshold and hold rule |
| Catalogue job | none. Measures are the person's; the optional filings view is a single diligence call. |

## Read the request

- **Partner types.** Reseller, implementation partner, referral partner, marketplace, co-sell. Measures differ by type.
- **Handoff event.** Take it from the channel design. Without it, "handed off" cannot be counted; ask.
- **Data held.** Which records exist (CRM, order forms, implementation log). A measure without a record is not measurable `[GAP]`.
- **Terms in force.** Data terms and compensation decide which duties go on the sheet.
- **Mode.** Short for "what should we track"; full for the sheet itself.

## Workflow

### Step 1. Offer the starting counts

From `references/monitoring-signals.md` Part 1: qualified buyers handed off, implementations started, claim breaches. Present them as a starting list, labeled so, with the definition to agree and the record each is counted from. The person keeps, renames, drops or adds.

### Step 2. Write the person's rules

For each partner type and measure: the period, the threshold in the person's numbers, and whether a miss forces a hold. Write them back for confirmation. If the person asks for thresholds, say no benchmark is sourced `[GAP]`; any number offered is labeled "proposed" with its basis (for example the partner's own committed plan, if the person has one) and is not applied until confirmed.

### Step 3. Add the duties the rules set

From `references/monitoring-signals.md` Part 2, add only the duties that apply to the terms in force, each with its row: business associate breach notice no later than 60 calendar days after discovery (CP-US-49); EU sub-processor authorization (CP-EU-02); outcomes-based partner payments need regular monitoring of performance and quality of care (CP-US-14); patient engagement tools capped at $623 per patient for calendar year 2026 (CP-US-27); Germany prescription-routing ban (CP-DE-06). Each becomes a check on the sheet ("evidence that ... is in place"), not a score.

### Step 4. Public signals (optional)

For a partner that is a regulated digital health company or an SEC filer, name the public signals the library can show and their limits (`references/tools.md`): `diligence-dh.get_deltas {companies: [...], since: "YYYY-MM-DD"}` returns new authorizations, studies, safety events, filings and awards in the log; `get_funding_signals` lists filings by type. Say that "no change recorded" is a statement about the library's log. Do not put a confidential partner name into a call without the person's say.

### Step 5. Name the data owner per measure

Who holds each record, as the person names them. "owner not named" otherwise.

## Build the output

Follow `assets/measure-sheet-output.md`. Answer first: the measures per partner type and which one forces a hold. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every measure, threshold, period and hold rule is the person's, and the output says so; any proposal is labeled.
- Every duty has a row; none is presented as a performance target.
- No benchmark is offered as a target.
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Defining measures only; scoring is A2, actions are B1.
- Payer outcomes contracts are Market Access; customer outcomes are Customer Success.
- Drugs, biologics and wellness apps are out of scope.
