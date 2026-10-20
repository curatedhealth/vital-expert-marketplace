# A2 Transaction and data flags

Framework task: DH-DIL.4.1, Part A, task A2. New in this version; the old suite had no task for the rules a memo must flag.

## What this task delivers

For the deal facts the person gives, the transaction and health-data rules the memo must flag: US premerger notification (HSR), CFIUS sensitive personal data, the DOJ bulk sensitive data rule, EU and Swiss investment screening, HIPAA breach and business associate rules, the FTC Health Breach Notification Rule, GDPR special-category data and, when the deal includes a technology license, the licensing rules (EU TTBER 2026/877 and its transition, the DOJ/FTC IP licensing guidelines, SEC material-contract disclosure). Each flag states the rule, the figure, the instrument and its date, the row, and how the person's fact sits beside it (above, at or below, not given). It answers "what must our legal or compliance owner look at, and on which figures?"

Why it matters: thresholds move every year (DL-049), the HSR form changed and was vacated in 2026 (DL-051), and the DOJ thresholds sit far below the CFIUS test and count de-identified data (DL-066, DL-067; research file, changes and conflicts item 6). A memo that carries remembered figures, or says a deal is "clear", states something no source supports.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Not bound (diligence suite); work as a diligence analyst who assembles and checks |
| Skill | DH-DIL.4.1 Part A, Transaction and data flags |
| Workflow | The steps below |
| Knowledge | `references/transaction-and-data-rules.md`; `references/licensing-deal-rules.md` (licensing deals); rows DL-019 to DL-021, DL-044 to DL-106, DL-134, SP-130 to SP-147, CP-US-44 to CP-US-49, CP-US-54 to CP-US-56, CP-EU-01 to CP-EU-09 |
| Tools | None from the library (`diligence-dh.retrieve_guidance` returned no passage for a legal query; `tools.md`). `scripts/memo_facts.py flags` on the person's deal facts |
| Prompt | This guide |
| Template | `assets/transaction-flags-output.md` |
| Input | The request and its context: the person's deal facts (`transaction-and-data-rules.md` section 8; for a license, `licensing-deal-rules.md` section 4) |
| Governance | `references/governance.md`; conclusions are for the owner the person names for legal or compliance, or owner not named |
| Catalogue job | none |

## Read the request

- **Deal facts.** Take only what the person states: value and currency, closing date, structure, each investor's country, government ownership and voting percentage, board or observer rights, data counts by kind (health, genetic, 'omic), access by any foreign party, EU member states, Swiss presence and turnover, HIPAA role. Anything missing is "not given"; ask for it. Never assume a nationality, a count or a date.
- **License terms.** If the deal includes a technology license (in-licensing, out-licensing, co-development with licensed rights, a data license), take only what the person states: territory, rights licensed, exclusivity, whether their legal owner treats the parties as competitors, the relevant markets and shares as their legal owner defines them, whether the agreement was in force on 30 April 2026, any research and development restriction, any technology pool, any SEC registrant party (`licensing-deal-rules.md` section 4). Never define a market, supply a share or decide whether the parties compete.
- **Currency.** HSR figures are in USD (DL-045); Swiss turnover in CHF (DL-084). Do not convert unless the person gives the rate.
- **Who reads it.** The owner the person names for legal or compliance, or owner not named.

## Workflow

### Step 1. Write the deal facts back

List the person's facts, numbered, verbatim, and the "not given" ones. With code execution, write them as JSON in the shape of `evals/files/deal_facts_illustrative.json`.

### Step 2. US premerger notification

From `transaction-and-data-rules.md` section 1: the 2026 size-of-transaction figure USD 133.9 million, effective 17 February 2026 (DL-044, DL-045); the size-of-person figures when the value is between USD 133.9 million and USD 535.5 million (DL-046, DL-047); the fee where the row states the tier (DL-048), else `[GAP]`; the form status after the vacatur of 12 February 2026 (DL-051 to DL-054); the typical 30-day waiting period (DL-055). A closing before 17 February 2026 used 2025 figures, which are `[GAP]`. How the value is calculated under the HSR rules is not sourced: say so.

### Step 3. CFIUS and the DOJ bulk data rule

Section 2 and 3: the one-million scale test and its other limbs (DL-056), genetic results at any count (DL-058), aggregation across categories (DL-059), TID US business (DL-061), a board or observer seat in a non-controlling investment (DL-062), mandatory declaration percentages (DL-063, DL-064). Then the DOJ thresholds (DL-066), de-identified data counted (DL-067), countries of concern and covered persons (DL-069, DL-071). Set the person's counts and percentages beside each figure. State plainly when the two regimes diverge for these facts.

### Step 4. EU and Swiss screening

Section 4 and 5: which EU regime applies on the person's closing date (2019/452 until 17 January 2028, then 2026/1386, DL-075), that health is a risk factor rather than in the 2026/1386 mandatory list (DL-076, DL-078), that member states may go further (DL-077), and that national laws are `[GAP]`. Swiss: IPG adopted, not in force, planned for 2027, state-controlled acquirers only, CHF 100 million turnover for health companies (DL-081 to DL-084).

### Step 5. Health data and breach records

Section 6: what the memo asks the target for (four-factor breach risk assessments, DL-087; burden-of-proof documentation, DL-094; DPIA, DL-106; Article 9(2) ground per purpose, DL-101), and what the person checks (HHS portal main list and archive, DL-095, DL-096). Business associate terms (CP-US-44 to CP-US-49) or the FTC rule (CP-US-54 to CP-US-56), by the HIPAA role the person gives; if not given, ask.

### Step 5b. Licensing deal facts (only if the deal includes a license)

From `licensing-deal-rules.md`, flagged for the owner the person names for legal or competition questions, or owner not named:

- **EU.** Regulation 316/2014 expired on 30 April 2026 (SP-134); Regulation (EU) 2026/877 applies from 1 May 2026 to 30 April 2038 (SP-135). Set the person's shares beside the conditions as the person gives them: competitors, combined share at most 20% on any relevant market; non-competitors, each party at most 30% (SP-136). For an agreement in force on 30 April 2026, state the transition to 30 April 2027 for agreements that met the old rules but not the new ones (SP-137). Add SPCs as technology rights (SP-138), the hardcore research and development restriction between competitors (SP-139), technology pools outside the regulation (SP-140; echo technology pool true or false from the person's facts beside it), the 2026 Guidelines (SP-141) and, for a data license, that the TTBER can apply only where the data qualifies as an existing technology right such as production know-how (SP-142).
- **US.** The 2017 guidelines' principles (SP-143, SP-147); the safety zone at no more than 20% collectively of each relevant market significantly affected, for a restraint not facially anticompetitive (SP-144); the four-entity test for research and development markets (SP-145); outside the safety zone is not presumed unlawful (SP-146).
- **Disclosure.** If a party is an SEC registrant: material contracts and licenses the business depends on are filed as exhibits, with permitted redaction (SP-130 to SP-133); a material definitive agreement goes on Form 8-K Item 1.01 (DL-019 to DL-021). This says where a counterparty's terms may appear and what a redacted exhibit does not show.
- **Data.** If the rights licensed include data (for example training data for an algorithm), add the GDPR rows beside the person's fact: data concerning health (DL-099), the Article 9(1) prohibition unless a 9(2) ground applies (DL-101 (inference)), member-state add-ons (DL-105), and a DPIA for large-scale processing of special categories (DL-106). Whether the data is health data, and which ground applies, is for the owner.

Each line: the person's fact, the rule's figure or wording, the instrument and date, the row, and the person's figure beside the condition ("your 18% beside the 20% condition; not assessed: competitor status, markets and shares are for your legal owner", "not given; ask"). The answer paragraph never says the figure is under or over a share threshold. Never write "exempt", "block-exempted", "safe harbor", "inside the safety zone" or "compliant", and never supply a market definition or a share. With code execution, give the license facts under `license` in the deal JSON (shape of `evals/files/license_deal_illustrative.json`); step 6 prints them.

### Step 6. Run the comparison

With code execution, run `python3 scripts/memo_facts.py flags --deal DEAL.json`. Check each line against the rows; the script prints figures and rows only.

### Step 7. What the owner must decide

List the conclusions the owner the person names must reach (reportable, covered, declaration, prohibited, notifiable), each with the facts and rows behind it. Never answer them.

## Build the output

Follow `assets/transaction-flags-output.md`. Answer first: which regimes the person's facts touch a figure in, and which facts are missing. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/memo_facts.py words ANSWER.md` (counts the body above the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- Every figure has its row, instrument and date; yearly figures name the year.
- Pending and moved rules (HSR form, EU 2026/1386, Swiss IPG, the TTBER change of 1 May 2026 and its transition) are labeled as such.
- For a license: no "exempt", "safe" or "inside the safety zone"; no market definition or share supplied; whether the parties compete is the owner's.
- Rows marked "(inference)" are labeled as the researcher's reading.
- No sentence says or implies that the deal is clear, not reportable or compliant.
- Missing deal facts are "not given", with the question to ask.
- `python3 scripts/memo_facts.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line of the answer (the offer of a full version and any calls list come before it, never between "Record" and "Clears it"): Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- AI Act and AI-enabled device questions: `dh-regulatory-and-quality` ai-ml-device-pathway-and-change-control.
- Business associate agreements for one's own partner contracts: `dh-go-to-market` channel-and-partner-design.
- National FDI laws, state privacy laws, CFIUS fees and timelines: not sourced; the owner the person names, or owner not named.
- License terms, partner selection and partner economics for one's own product: `dh-go-to-market` channel-and-partner-design. Competition rules beyond the TTBER and the DOJ/FTC guidelines, and market definition: not sourced; the owner the person names for legal or competition questions.
