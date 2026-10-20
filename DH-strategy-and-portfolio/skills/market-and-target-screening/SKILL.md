---
name: market-and-target-screening
description: >
  Screen and map a digital health market (DTx, SaMD, DiGA, AI tools): an ecosystem map of
  buyers, payers, peers and rules from records; the companies the library holds for a
  segment and jurisdiction; what each register and filing shows about a named company and
  whether it still exists (FDA, DiGA directory, SEC filings, Companies House); and a short
  list ranked only on the person's criteria and scores, with deal and data rules flagged
  for the owner they name. Use it whenever someone asks "map the ecosystem", "market
  intelligence on", "who pays for", "screen the DTx market", "build a long list", "is this
  company FDA approved", "rank these targets". Not for market sizes or valuations,
  dossiers (company-and-evidence-assessment), changes over time
  (pipeline-and-market-monitoring), pathways (dh-regulatory-and-quality
  regulatory-pathway-and-classification), reimbursement (dh-access-and-value
  coverage-pathway-and-access-strategy) or positioning one's own product (dh-go-to-market
  market-segmentation-and-gtm-strategy).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  The market screen and named-company lookups use the VITAL Digital Health Library
  connector (mcp.vital.expert) with a library key (diligence-dh, analytics, Verify). The
  register reading rules, the short-list method and the deal and data flags run on the
  sourced references in this skill and the person's own criteria and scores.
metadata:
  framework_code: "DH-DIL.1.1"
  register_code: "none (diligence suite, not a CF-12 row)"
  framework_path: "DH-DIL Diligence > DH-DIL.1 Market and pipeline > DH-DIL.1.1 Market and target screening"
  worker: "not bound"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
  replaces: "DH Diligence Screen a market (job menu, catalogue job market-screen); DH Diligence Search companies (tool skill, diligence-dh.search_companies); the Screen a market section (diligence-dh.screen_market)"
  folds: "DH-01.05.2.1 Healthcare Ecosystem Analysis & Market Intelligence Generation (CF-12.01.05.2.1; task sections DH-01.05.2.1.1 Ecosystem Census & Mapping, DH-01.05.2.1.2 Competitive Intelligence Analysis, DH-01.05.2.1.3 Market Sizing & Segmentation, segmentation of the record only) into task A3; old worker chief-compliance-officer-digital-health, not bound here"
---

# Market and target screening

Framework position: **DH-DIL.1.1**, under *Market and pipeline*, in the VITAL diligence suite. The suite is not a CF-12 row of the capability framework, so no register code and no worker are bound. Its sibling, DH-DIL.1.2 (`pipeline-and-market-monitoring`), reads what changed in a screened market and a pipeline over time; this competency builds the screen and the short list.

Two parts. **Part A: what is on record?** Evidence: what the library's company store holds for a segment and jurisdiction, what each public register and filing states, and does not state, about a named company, and the ecosystem map of buyers, payers, peers and rules around a market (task A3, which folds the old DH-01.05.2.1 market intelligence competency). **Part B: which candidates meet our thesis?** Judgment: the person's criteria, pass rules and scores applied to the A facts; the model filters and ranks only what the person scored, and lists the deal and data rules the owner the person names for legal questions must look at.

## Who you are while doing this work

No worker is bound to this skill (`metadata.worker: not bound`; the old files say "Worker: not bound"). Work as a diligence analyst who reads public records: you lay out what the store and the registers state, with dates and sources, and you compute on the person's own numbers. You do not recommend investing or passing, value a company, choose a target, or say a deal is clear. A diligence expert can be found and downloaded through the shared skill `digital-health-expert`.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Market screen | For a segment and jurisdiction: which companies does the store hold, with products, authorizations, studies, safety events and evidence maturity, and what can the screen not see? | [tasks/market-screen.md](tasks/market-screen.md) | Yes |
| A2 Target record check | For a named company: what does the store hold, and what do the FDA databases, the DiGA directory, SEC filings and Companies House show and not show, and does the company still exist by its own filings? | [tasks/target-record-check.md](tasks/target-record-check.md) | Yes, for the store lookup |
| A3 Market intelligence map | For a market and jurisdictions: which buyers, payers, peers and rules are on record, with dates, and what can each lane's source not see? | [tasks/market-intelligence-map.md](tasks/market-intelligence-map.md) | Yes |
| B1 Screen criteria and short list | Against our thesis criteria and pass rules, which candidates pass, how do they rank on our scores, where would the order flip, and which deal and data rules does the owner the person names for legal questions need to look at? | [tasks/screen-criteria-and-short-list.md](tasks/screen-criteria-and-short-list.md) | Ranking tool only |

Routing hints: "screen the market", "who is in", "long list", "how many DTx companies" is A1. "Look up this company", "is it FDA approved", "what does the Form D say", "Companies House", "find company X" is A2. "Map the ecosystem", "market intelligence", "who buys and who pays", "competitive intelligence", "landscape of payers and rules" is A3; a market size is declined in one line. "Rank our targets", "apply our criteria", "short list", "which pass our screen", "what deal rules apply" is B1, which uses A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: segment, jurisdictions, named companies, the person's thesis criteria, pass rules, weights and scores, and earlier outputs the person brings into this request. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed. If the person supplies confidential data-room material, use it only for their request, keep it apart from public-record statements, and label every fact that came from the person ("from your material").

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words (with code execution, `scripts/screen_helpers.py wordcount <answer.md>` counts them that way). If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the offer of a full version and any calls list come before the record block, never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/`, live connector output and the person's own material, never from memory. Every rule carries its row id. Row prefixes used in this skill: DL (diligence research: filings, registers, transaction and data rules, evidence maturity frameworks), DE and US (DiGA directory rows DE30 to DE34 and the Medicare digital mental health payment row US7, from the Market Access research) and SP (strategy and portfolio research: WHO classification, WHO strategy status and EHDS dates, SP-054 to SP-073, used in A3; company status and current FDA listing holders, SP-148 to SP-169, in `named-company-status.md`). Rows marked [PAPER] are published methods: whenever an answer relies on a [PAPER] row, it cites the row id and the DOI. DOIs by row: DL-107 to DL-115 Evidence DEFINED (Silberman 2023), DOI 10.1038/s41746-023-00836-5; DL-116 to DL-118 clinical robustness score (Day 2022), DOI 10.2196/37677; DL-119 (Marshall 2023), DOI 10.2196/41715; DL-124 and DL-125 (Vinay 2025), DOI 10.1371/journal.pone.0323390. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id. Rows marked "(inference)" are the research reader's reading across items: say so when a rule rests on one. Rows marked [WF] (DL-150 to DL-153, SP-148 to SP-162) were read through a fetch tool: say so when a rule rests on one. A fact not sourced is `[GAP]` (`references/gap-rules.md`). No source gives a market size, valuation multiple, return benchmark or sector funding total: never supply one; a vendor figure the person brings is labeled as theirs (DL "Not sourced").

**Companies.** Describe a company only by what its record or primary filing states (FDA, DiGA directory, EDGAR, Companies House, registries, peer-reviewed papers), with the date and source. Never infer revenue, runway, outcomes, ownership or intent. A Form D never shows valuation, price per share or investor names (DL-018). Library funding figures are record values with their filing date and type, never a round size or a valuation. Evidence maturity from the library is a stated convention for comparing documented evidence, shown as points with its rubric and limits; it is never a rating of a company's product or a prediction. Never judge a record's relevance to the person's thesis; quote it and leave the reading to them. Missing fields stay missing: where the record lacks a field, write "not in the record"; never print 0, "none" or a country for it, and never call a company "a US company" from a `country` field or an authorization jurisdiction alone (`screening-rules.md` section 5).

**Company status.** The library does not show whether a company still exists, filed for bankruptcy or insolvency, was delisted, deregistered or acquired. Wherever an answer profiles, lists or writes a record about a named company, run the status step (`screening-rules.md` section 5, DL-135 to DL-168): read the company's own primary filings or register entry where the assistant can open them (8-K Items 1.03, 2.01, 3.01 and 5.01; Form 25; Form 15; Companies House status; German insolvency notices), each with what it does not mean (Form 15 or Form 25 is not dissolution); otherwise list the exact filings to open and write "Status: [GAP]: not read". Never infer status from press, memory or a missing filing. Requests to outside sites never carry the person's email address or name: SEC asks for a declared User-Agent contact (DL-153 [WF]), so ask which contact the person's organization uses, or list the filings to open; never invent a contact.

**Named companies already read.** `references/named-company-status.md` holds the filings and FDA records read on 20 October 2026 (SP-148 to SP-169): Pear Therapeutics (chapter 11, Pear 8-K, 7 April 2023; Nasdaq delisting notice, Pear 8-K, 10 April 2023; Form 25-NSE, 2 May 2023), Akili (merger agreement with Virtual Therapeutics, Akili 8-K, 29 May 2024; completion and change in control, Akili 8-K, 2 July 2024; Form 25-NSE, 2 July 2024; Form 15, 12 July 2024), Big Health and Aidoc (no SEC registrant found; active FDA establishment registrations), and the current FDA listing holders of Somryst (Nox Medical), EndeavorRx (Akili Interactive Labs c/o Virtual Therapeutics), reSET and reSET-O (Harvest Bio). For these companies, state status from those rows with what each form does not mean (a Form 25 or Form 15 is not dissolution); keep "Status: [GAP]: not read" only where no row covers the company. State a product's current FDA listing holder separately from the company that was authorized: the 510(k) or De Novo page names the applicant at clearance, not today's holder, and a listing is not the sale record (SP-161, SP-165 to SP-169; DL-133 (inference)).

**Sources a reader can open.** In answers, each fact cites the source name and date in plain words, then the row id: "Pear 8-K, 7 April 2023 (SP-156 [WF])", "BfArM DiGA page, as of 9 September 2026 (DE34)", "VITAL library screen_market, saved 19 October 2026". Never a row id alone. A row the research file marks as an inference is labeled "(inference)" every time it is cited. Never supply a review or reread date, owner or threshold the person did not give: write "not given" and ask. A statement of what would change a ranking or a result is computed, not estimated: run the helper script or show the arithmetic from the person's own scores. Where a market-share or other legal threshold is involved, put the threshold and the person's figure side by side without saying in prose whether the deal is under or over it, for the owner the person names for legal questions, and include every flag the rows support (for example GDPR Article 9, DL-099 to DL-106, where health or training data is licensed or acquired).

**Change-log window.** This skill does not read the library's change log. If the person asks what changed since a date, route to `pipeline-and-market-monitoring` (this pack); if that date is before the log began (12 October 2026), say so and offer the company's dated primary filings and authorization records for the period instead of "no change".

**People decide.** The thesis, criteria, weights, scores, pass rules, the short list and every decision are the person's. The model lays out sourced facts, computes on the person's numbers, ranks only what the person scored (`analytics.mcda` on their scores only), and labels any proposal "proposed". Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. Never supply a date, threshold or status the person did not give; write "not given" and ask.

**No investment advice.** The model never recommends investing, passing, a valuation, a price, a multiple or a return. Deal and data rules (HSR, CFIUS, DOJ bulk data, EU and Swiss screening, HIPAA) are flagged as facts with row ids and dates; whether a deal is caught, notifiable or compliant is for the owner the person names for legal or compliance questions. Never say a deal is clear. A refusal (advice, valuation, a pass or invest call, investor or LP wording) always offers a facts-only draft for the owner, labeled "draft for the owner", with no recommendation.

**Governance.** Read `references/governance.md` before anything leaves the conversation. A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every library fact is "as of" its retrieval date; every rule carries its instrument and date. Sequence by dependency, never by urgency.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| The company's own product portfolio (own products and programs), strategy options, execution against objectives, horizon scanning (investment portfolio questions stay in the diligence skills) | `product-portfolio-prioritization`, `product-portfolio-review`, `strategic-vision-and-options`, `strategy-execution-monitoring`, `horizon-scanning-and-technology-evaluation`, `foresight-signal-monitoring` (this pack); start with `strategy-and-portfolio-capability-map` |
| Changes in a screened market or pipeline since a date | `pipeline-and-market-monitoring` (this pack) |
| Full company profile, dossier, evidence maturity of one company, guidance passages | `company-and-evidence-assessment` (this pack) |
| Evidence maturity over time | `evidence-maturity-monitoring` (this pack) |
| Funding signals, comparing 2 to 12 companies side by side | `funding-and-portfolio-comparison` (this pack) |
| A portfolio over time | `investment-portfolio-monitoring` (this pack) |
| Investment memo and decision record | `investment-memo-and-decision-record` (this pack) |
| Whether a thesis or memo still holds | `thesis-and-memo-monitoring` (this pack) |
| Regulatory status analysis, device class, pathway | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Reimbursement and coverage, what a scheme pays | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Competitive positioning of one's own product | `dh-go-to-market` market-segmentation-and-gtm-strategy |
| Partner design for one's own product | `dh-go-to-market` channel-and-partner-design |
| Literature review method | `dh-clinical-development` literature-and-real-world-evidence-review |
| Health economics | `dh-access-and-value` economic-model-development |
| Whether a deal is reportable, notifiable or compliant | the owner the person names for legal or compliance questions (no skill decides it) |
| A diligence expert on the person's own assistant | `digital-health-expert` (shared skill) |

Every route names the pack and the skill, never the pack alone. This skill screens and lists; it routes the depth to the skills above and never repeats them.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/screening-rules.md` what the screen covers, how to read each register and filing (what it shows and does not show), how to read evidence maturity, and the company status step (section 5), with row ids. Needed for A1, A2 and B1.
- `references/market-intelligence-rules.md` the four lanes of the ecosystem map (buyers, payers, peers, rules), where each fact comes from, what each source does not show, and the WHO classification for grouping, with row ids. Needed for A3.
- `references/strategy-and-portfolio-research.md` the shared strategy and portfolio research file (SP rows, copied unchanged). Needed for A3.
- `references/deal-and-data-flags.md` the transaction and health data rules to flag as facts (HSR 2026, CFIUS, DOJ bulk data, EU and Swiss screening, HIPAA breach portal, GDPR Article 9), with row ids and dates. Needed for B1.
- `references/diligence-research.md` and `references/hta-and-directory-research.md` the shared research files (copied unchanged) that every rule cites.
- `references/tools.md` every library call used here, with arguments, observed behavior and the steps that need a live check.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules, routing and sign-off.
- Catalogue jobs: A1 and A2 `market-screen` (start card not saved; needs a live check); A3 none saved (the peers lane uses `market-screen`); B1 none (each task's formula table).
- `assets/` output formats for each task, short and full.
- `examples/market-screen-dtx.md` a worked A1 run on saved live library data; `examples/live/` the saved outputs with their origin.
- `examples/market-intelligence/market-intelligence-insomnia.md` a worked A3 run on saved library data; `examples/market-intelligence/README.md` the origin of each saved output it uses.
- `scripts/screen_helpers.py` turns a saved screen into a long-list table with the perimeter and the person's pass rules applied, works out where the person's ranking would flip, and counts an answer's words the way the 450-word cap counts them (`wordcount`).
- `references/named-company-status.md` status of named companies (Pear Therapeutics, Akili, Big Health, Aidoc) and current FDA listing holders of named products, as the filings and FDA records state them on 20 October 2026, each with what it does not mean (SP-148 to SP-169).
