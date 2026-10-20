# A1 Opportunity and option landscape

Framework task: DH-01.05.1.1, Part A, task A1. Carries the old tasks "DH-01.05.1.1.1 Opportunity Identification" and the fact-gathering half of "DH-01.05.1.1.3 Build-Partner-Buy Assessment" (the choice itself is B1).

## What this task delivers

The opportunity in the person's words, named in shared vocabularies (WHO digital intervention axes, Oslo innovation type) with a proposed EU TRL; the policy context the strategy has to name for the markets in the request; and a longlist of options (build, partner, license in or out, acquire, and business as usual) with, for each named candidate, its public-record facts, its company status line and the licensing rules the person's legal owner must check. Every fact carries its row or its source and retrieval date; every gap is named. It answers "what exactly is the opportunity, and what options do we really have?"

Why it matters: a strategy that starts from a vendor slide, a press release or a benchmark treated as a target commits money on facts nobody checked. Clearance is not approval (DL-128), a Form D shows no valuation (DL-016; DL-018, an inference), and the old EU technology transfer exemption expired on 30 April 2026 (SP-134).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | `behavior-change-designer` (old DH-01.05.1.1.1); `chief-compliance-officer-digital-health` (old DH-01.05.1.1.3). Work as a strategy analyst who assembles and checks |
| Skill | DH-01.05.1.1 Part A, Opportunity and option landscape |
| Workflow | The steps below |
| Knowledge | `references/option-frameworks.md` sections 1 to 6 and 8; rows SP-028 to SP-073, SP-088 to SP-098, SP-130 to SP-169, DL-016, DL-018 to DL-021, DL-101, DL-106, DL-126 to DL-128, DL-135 to DL-168 |
| Tools | Only for named candidates: `diligence-dh.build_company_profile`; optional `diligence-dh.compare_portfolio` (2 to 12 named candidates); optional `diligence-dh.get_funding_signals` (SEC filers); `scripts/options_check.py facts` |
| Prompt | This guide |
| Template | `assets/opportunity-and-option-landscape-output.md` |
| Input | The request and its context: the opportunity and product in the person's words, the markets, named candidates, options the person already has, sibling-skill outputs the person brings (horizon-scanning-and-technology-evaluation, market-and-target-screening, company-and-evidence-assessment) |
| Governance | `references/governance.md`; candidates described only by their record; licensing conclusions stop for the person's legal owner |
| Catalogue job | none (`list_jobs` lists no strategy job; `list_jobs_2026-10-19.json`) |

## Read the request

- **The opportunity.** Write it back in the person's words, with the population, setting and market they named. If the market is not given, write "not given" and ask before citing market rows.
- **Options already named.** Keep them verbatim. Add business as usual as the baseline option (SP-093, UK public-sector guidance) and mark any option the model adds as "proposed".
- **Named candidates.** A company, a product, an FDA or SEC number. A product name resolves to its company in the library; say which products the facts cover.
- **"Portfolio".** If the person says "our portfolio", ask whether they mean the product portfolio (own products and programs) or an investment portfolio (companies held). Investment questions route to `investment-memo-and-decision-record` (this pack).
- **Press or vendor claims.** Keep them as "from you (press claim, not checked)"; they are not signals. Then answer the record question the claim raises. If the company is one the research pass read (`option-frameworks.md` section 5), quote what its filings state, with names and dates, and correct the claim's date if the filings date it differently (for example "you read it was last year; the filings date completion to 2 July 2024"). If not, name the filing that would show it (8-K Item 2.01, DL-138, or Item 5.01, DL-141) as "Company status [GAP]: not read". In the Answer paragraph, name the option the status blocks (for an acquired licensor: the in-license option cannot be scored on counterparty-dependent criteria until you confirm the legal name of the entity that holds the authorizations and would grant the license) and what would unblock it.

## Workflow

### Step 1. Write the opportunity back

One sentence in the person's words, with population, setting, market and the problem it addresses. Missing parts: "not given".

### Step 2. Name it in shared terms (proposed)

Using `option-frameworks.md` section 1: the WHO classification axes that apply (SP-054 to SP-057), the Oslo type (product or business process innovation, and which of the six business functions, SP-038, SP-039, SP-042). Label both "proposed". If the person works to ISO 56002, say it is guidance only and under revision, read from the ISO abstract [WF] (SP-044 to SP-047).

### Step 3. Context the strategy must name

For the markets in the request only (section 2): WHO guideline and global strategy rows (SP-048 to SP-066), EHDS dates for an EU strategy (SP-068 to SP-073). State each as context, never as compliance.

### Step 4. Proposed readiness level

If the person describes the technology's state, propose a TRL with the EU wording verbatim and its row (SP-029 to SP-031), the evidence the person gave behind it, and the note that NASA 7 to 9 assume space and flight (SP-035). Without a description of the state: "TRL not proposed: state of the technology not given". For an emerging technology scan, route to `horizon-scanning-and-technology-evaluation` (this pack).

### Step 5. The longlist

List the options: the person's, business as usual, and any the model adds labeled "proposed" (build, partner, license in, license out, acquire). For each: what it would need to be true (in the person's words if given), and the facts that bear on it. Green Book longlist and shortlist terms may be used as a checklist, labeled "UK public-sector guidance" (SP-094, SP-095). The model never names a preferred way forward.

### Step 6. Named candidates (library)

For each named candidate company, call `diligence-dh.build_company_profile {company: "<exact legal name, brand, FDA or SEC number>"}`. With code execution, save the output and run `python3 scripts/options_check.py facts --profile PROFILE.json [--funding FUNDING.json]`. Report authorizations with the pathway in words and, separately, the product's current FDA listing holder where a row gives it (SP-165 to SP-169; never the listing holder as licensor or buyer), ("De Novo granted", "510(k) cleared"; never "approved" unless a PMA, DL-128), registered studies by link tier, Form D rows with their caveats, and the library's evidence maturity with its rubric and limits (a convention, never the evidence verdict). For 2 to 12 named candidates the person wants side by side, `diligence-dh.compare_portfolio {companies: [...]}`. For an SEC filer, `diligence-dh.get_funding_signals {company: "<legal name as resolved>"}` gives the 8-K rows for the status step. A candidate that does not resolve: "Lookup missed for NAME (exact matching)".

### Step 7. Company status (every named candidate)

Follow `option-frameworks.md` section 5 and the SKILL.md rule. For a company the research pass read (Akili, Pear, Big Health, Aidoc), quote the status from section 5 with each filing's name and date and the row after it, marked [WF] for SEC rows, and what each form does not mean (Form 25 concerns the listing only, DL-144; Form 15 is not dissolution, DL-149, inference). The `facts` output prints these lines for those companies. For any other company, where the assistant can open the filing or register, quote the item and date; otherwise write "Company status [GAP]: not read" and list the filings to open. Never take status from press or memory, even when the person states it. Then state, per option, what the status blocks and what would unblock it (section 5, "What the status blocks").

### Step 8. Licensing and disclosure facts to flag

If an option is a license or a collaboration: the EU rules (Regulation (EU) 2026/877 in force 1 May 2026, the 20% and 30% market share conditions, the transition to 30 April 2027 for agreements in force on 30 April 2026, hardcore R&D restriction, SPCs, data licensing; SP-134 to SP-142) and the US DOJ/FTC guidelines (SP-143 to SP-147), for the markets in the request; and, for listed counterparties, where a deal would be disclosed (8-K Item 1.01, DL-019 to DL-021; Regulation S-K 601(b)(10), SP-130 to SP-133). State each as a fact for the owner the person names for legal or competition matters, or owner not named. Market shares are the person's figures: print each threshold beside the person's figure (or "your figure: not given") without saying which side it falls on in legal terms. If the license includes health data (for training, validation or real-world evidence), add the data flags from section 6 (SP-142; DL-101, inference in part; DL-106; SP-071, SP-072 for the EU).

### Step 9. Gaps

By reason (`references/gap-rules.md`): not in the sources (for example a success rate for digital health programs, a market size), not given by the person, lookup missed, status not read.

## Build the output

Follow `assets/opportunity-and-option-landscape-output.md`. Answer first: the opportunity in one sentence, how many options are on the longlist, what the record shows on named candidates (including status and which option it blocks), and the largest gap. Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/options_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop, the company status line or the record line. Refusals follow the same 450-word cap.

## Before you hand it over

- The opportunity and options are in the person's words; added options, classifications and the TRL are labeled "proposed".
- No option is named as preferred; no probability, market size, valuation, price or return appears.
- Every fact names its source and date in plain words with the row id after it; never a row id alone; "approved" only for a PMA.
- Every "(inference)" row carries its label each time; every [WF] row says [WF].
- The company status line is present for each named company: quoted from a filing or register read (section 5 for companies the research pass read), or "[GAP]: not read" with the filings to open; the option it blocks is named.
- Licensing facts carry their rows and dates and stop for the owner the person names; never "exempt".
- Green Book terms are labeled UK public-sector guidance.
- `python3 scripts/options_check.py words ANSWER.md` prints "within the short-mode cap".
- The record line is the very last line; the calls list and the offer of the full version come before the record block: Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Boundaries

- Scanning for emerging technologies: `horizon-scanning-and-technology-evaluation` (this pack).
- Screening a market for targets: `market-and-target-screening` (this pack).
- Evidence maturity by a named framework: `company-and-evidence-assessment` (this pack).
- Partner design for one's own product: `dh-go-to-market` channel-and-partner-design.
- Device status of an option: `dh-regulatory-and-quality` regulatory-pathway-and-classification.
