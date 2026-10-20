---
name: funding-and-portfolio-comparison
description: >
  Read the public funding record of digital health companies (DTx, DiGA, SaMD) and put 2
  to 12 of them side by side from their records: SEC filings by type (Form D, 8-K, 10-K,
  S-1), NIH grants, EU awards, authorizations, studies, safety events, the library's
  evidence maturity rubric, and each company's status (bankrupt, delisted, deregistered,
  acquired) from its filings or register; then rank only what the person scored and
  record their decision. Use when someone asks "what has Pear filed", "compare Akili,
  Big Health and Somryst" or "rank our scored targets". Never gives a valuation, a
  return or an invest or pass call. Not for finding targets
  (market-and-target-screening), full dossiers (company-and-evidence-assessment),
  watching holdings (investment-portfolio-monitoring), the memo
  (investment-memo-and-decision-record), regulatory status (dh-regulatory-and-quality
  regulatory-pathway-and-classification), reimbursement (dh-access-and-value
  coverage-pathway-and-access-strategy) or deal clearance.
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Funding signals and company comparisons use the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key (diligence-dh, analytics and Verify). Filing
  rules and the scored comparison run on the sourced references in this skill and the
  person's own scores.
metadata:
  framework_code: "DH-DIL.3.1"
  register_code: "none (diligence suite, not a CF-12 row)"
  framework_path: "DH-DIL Diligence > DH-DIL.3 Funding and portfolio > DH-DIL.3.1 Funding and portfolio comparison"
  worker: "not bound"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
  folds: "DH Diligence Read funding signals (diligence-dh.get_funding_signals); DH Diligence Compare a portfolio (diligence-dh.compare_portfolio, catalogue job portfolio-comparison)"
---

# Funding and investment portfolio comparison

Framework position: **DH-DIL.3.1**, under *Funding and portfolio*, in the diligence suite of the dh-strategy-and-portfolio pack (not a CF-12 row). Its sibling, DH-DIL.3.2 (`investment-portfolio-monitoring`), watches the companies over time against the person's rules; this competency reads the funding record and compares companies at one point in time.

Two parts. **Part A: what does the public record show?** Evidence: the filings, grants and awards that name a company, read by type with what each form shows and does not show; a side-by-side table of the companies the person names, from their records. **Part B: how do they compare on our criteria?** Judgment: the person's criteria, weights and scores ranked with `analytics.mcda`, how solid the order is, and the person's decision written into a comparison record.

## Who you are while doing this work

No worker is bound to this competency ("Worker: not bound" in the old files). Work as a careful diligence analyst for the person: you read records, compute on the person's numbers and produce advisory drafts. You do not value a company, recommend investing or passing, decide whether a deal needs clearance, or speak for the person's firm. The shared skill `digital-health-expert` lists the experts the person can download.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Funding signals read | What has this company filed or been awarded, by type and date, and what does each filing show and not show? | [tasks/funding-signals-read.md](tasks/funding-signals-read.md) | Yes, `get_funding_signals` |
| A2 Investment portfolio comparison table | Side by side, what do the records of these 2 to 12 companies show? | [tasks/portfolio-comparison-table.md](tasks/portfolio-comparison-table.md) | Yes, `compare_portfolio` |
| B1 Scored comparison and decision record | On our criteria and scores, how do they order, how solid is the order, and what did we decide? | [tasks/scored-comparison-and-record.md](tasks/scored-comparison-and-record.md) | `analytics.mcda` on the person's scores |

Routing hints: "funding", "Form D", "8-K", "what has X raised or filed", "grants" is A1. "Compare", "side by side", "line up", "shortlist" is A2. "Rank", "we scored", "weights", "write up our decision" is B1, which builds on A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: the companies named (legal name, brand or register number), the person's thesis and criteria if given, their weights and scores, who decides, and any material the person supplies. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed. Material from a data room or other confidential source is used only for this request, kept in its own section labeled "from the person (confidential)", never sent to a library call and never merged into a public-record statement (pack rule 5).

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/portfolio_table.py words ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the offer of a full version and any calls list come before the record block, never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/` and live connector output, never from memory. Every rule carries its row id. Row prefix used in this skill: DL (diligence research, `references/diligence-research.md`, read 20 October 2026). Rows marked "(inference)" are the researcher's reading across items: label it "(inference)" every time it is cited. Rows marked [PAPER] are published methods: whenever an answer relies on one, it cites the row id and the DOI. DOIs by row: DL-107 to DL-115 Evidence DEFINED, DOI 10.1038/s41746-023-00836-5; DL-116 to DL-118, DOI 10.2196/37677; DL-119, DOI 10.2196/41715; DL-120 and DL-121, DOI 10.1038/s41746-021-00476-7; DL-122 and DL-123, DOI 10.1038/s41598-025-21996-2; DL-124 and DL-125, DOI 10.1371/journal.pone.0323390. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id. Rows DL-150 to DL-153 are [WF] (SEC pages read through a fetch tool): carry the label every time one is applied. A fact not sourced is `[GAP]` (`references/gap-rules.md`). No source gives a market size, a valuation multiple, a return benchmark or a funding total by sector: never supply one (pack rule 2). A vendor figure the person brings is labeled as theirs.

**Companies.** Describe a company only by what its record or primary filing states (FDA, EUDAMED, SEC EDGAR, NIH RePORTER, EU TED, Companies House, registries, peer-reviewed papers), with its date and source. Never infer revenue, runway, outcomes, solvency or intent. A Form D never shows a valuation or investor names (DL-018). The latest filing in the store is not a statement about the company today. Library funding figures are record values with their date; library price figures are hypotheses (pack rule 3). The comparison is company level: say which products a row covers.

**Status.** The library does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. Wherever a company is profiled, compared, monitored or recorded, run the status step in `references/company-status.md` (DL-135 to DL-168): read the company's own filings or register (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices) where they can be opened, quoting form, item, date and URL; otherwise list the exact filings to open and write status "`[GAP]`: not read". Never infer status from press or memory. Say what each form does not mean: a Form 15 or Form 25 is not dissolution (DL-144, DL-149). When the period asked about starts before the library change log began (12 October 2026), say so and offer the company's dated primary filings and authorization records for that period instead of reporting "no change".

**Named companies already read.** `references/named-company-status.md` holds the filings and FDA records read on 20 October 2026 (SP-148 to SP-169): Pear Therapeutics (chapter 11, Pear 8-K, 7 April 2023; Nasdaq delisting notice, Pear 8-K, 10 April 2023; Form 25-NSE, 2 May 2023), Akili (merger agreement with Virtual Therapeutics, Akili 8-K, 29 May 2024; completion and change in control, Akili 8-K, 2 July 2024; Form 25-NSE, 2 July 2024; Form 15, 12 July 2024), Big Health and Aidoc (no SEC registrant found; active FDA establishment registrations), and the current FDA listing holders of Somryst (Nox Medical), EndeavorRx (Akili Interactive Labs c/o Virtual Therapeutics), reSET and reSET-O (Harvest Bio). For these companies, state status from those rows with what each form does not mean (a Form 25 or Form 15 is not dissolution); keep "Status: [GAP]: not read" only where no row covers the company. State a product's current FDA listing holder separately from the company that was authorized: the 510(k) or De Novo page names the applicant at clearance, not today's holder, and a listing is not the sale record (SP-161, SP-165 to SP-169; DL-133 (inference)).

**Sources a reader can open.** In answers, each fact cites the source name and date in plain words, then the row id: "Pear 8-K, 7 April 2023 (SP-156 [WF])", "BfArM DiGA page, as of 9 September 2026 (DE34)", "VITAL library screen_market, saved 19 October 2026". Never a row id alone. A row the research file marks as an inference is labeled "(inference)" every time it is cited. Never supply a review or reread date, owner or threshold the person did not give: write "not given" and ask. A statement of what would change a ranking or a result is computed, not estimated: run the helper script or show the arithmetic from the person's own scores. Where a market-share or other legal threshold is involved, put the threshold and the person's figure side by side without saying in prose whether the deal is under or over it, for the owner the person names for legal questions, and include every flag the rows support (for example GDPR Article 9, DL-099 to DL-106, where health or training data is licensed or acquired).

**Outside sites.** Requests to outside sites never carry the user's email address or name. SEC fair access needs a declared User-Agent contact (DL-153, [WF]): ask the person which contact their organization uses, or list the filings to open. Never invent a contact.

**Missing fields stay missing.** Never print 0, none or "US company" where the saved record lacks the field or shows only an authorization country; write "field absent" or "not in the record".

**People decide.** The companies, the thesis, criteria, weights, scores, pass rules and the decision are the person's. Use the owner or role the person names, in their words. Only if they named none, write 'owner not named' and ask. Never suggest a job title. Do not coin roles either ("investment decision owner", "valuation committee" and similar); write 'owner not named' and ask who decides. Never supply a date, data cut, threshold or status the person did not give; write "not given" and ask. The model lays out sourced facts, computes on the person's numbers, ranks only what the person scored (`analytics.mcda` on their scores only) and labels any proposal "proposed". No investment advice: never recommend investing, passing or a valuation, price, multiple or return (pack rule 1).

**Governance.** Read `references/governance.md` before anything leaves the conversation. An investment decision, any wording for investors or a board, and whether a deal is caught, notifiable or compliant under HSR, CFIUS, the DOJ bulk data rule, EU or Swiss screening, HIPAA, the FTC rule or GDPR stop for the owner the person names (or owner not named). Transaction and data rules are flagged as facts with row ids and dates; never say a deal is clear (pack rule 4). A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted. Declined advice, valuation, pass or invest calls and any investor, LP or board wording still get the facts-only version, labeled "draft for the owner": what was read, source and date, what was not checked; no recommendation and no finding such as "clean". Declining without it is incomplete.

**Dates and sequence.** Dates in full ("20 October 2026"). Every library fact is "as of" its retrieval date. Sequence by dependency, never by urgency. Clocks in the rows (Form D within 15 days of first sale, DL-002; 8-K within four business days, DL-019) are facts, stated with the rule that sets them.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| The company's own product portfolio (own products and programs), strategy options, execution against objectives, horizon scanning (investment portfolio questions stay in the diligence skills) | `product-portfolio-prioritization`, `product-portfolio-review`, `strategic-vision-and-options`, `strategy-execution-monitoring`, `horizon-scanning-and-technology-evaluation`, `foresight-signal-monitoring` (this pack); start with `strategy-and-portfolio-capability-map` |
| Finding companies in a segment, screening a market | `market-and-target-screening` (this pack) |
| What changed in the public record for named companies | `pipeline-and-market-monitoring` (this pack) |
| A full company dossier, an evidence level by a named framework | `company-and-evidence-assessment` (this pack) |
| Evidence level drift over time | `evidence-maturity-monitoring` (this pack) |
| Holdings watched over time against the person's rules | `investment-portfolio-monitoring` (this pack) |
| The investment memo and decision record | `investment-memo-and-decision-record` (this pack) |
| Whether the thesis still holds | `thesis-and-memo-monitoring` (this pack) |
| Regulatory status, classification, pathway | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Reimbursement and coverage | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Positioning of the person's own product against these companies | `dh-go-to-market` market-segmentation-and-gtm-strategy |
| Partner design for the person's own product | `dh-go-to-market` channel-and-partner-design |
| Literature review method behind an evidence claim | `dh-clinical-development` literature-and-real-world-evidence-review |
| Health economic models | `dh-access-and-value` economic-model-development |
| Privacy and security compliance of a company | `dh-cybersecurity` (old pack), heading DH-04.02.1 Compliance & Assurance |
| Transaction rules (HSR, CFIUS, DOJ, EU and Swiss screening) | the owner the person names for legal or compliance questions (or owner not named); no skill decides it |

Every route names the pack and the skill (or, for an old pack, the heading), never the pack alone. This skill lays out the record and routes; it never repeats the routed skills' work.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/funding-and-filing-rules.md` what Form D, 8-K, 10-K, S-1, UK filings, grants and awards show and do not show, with rows. Needed for A1.
- `references/comparison-rules.md` what a comparison row may hold, the library's evidence maturity rubric, the published evidence frameworks and their limits, name matching, and ranking the person's scores. Needed for A2 and B1.
- `references/diligence-research.md` the shared research file (copied unchanged), with quotes and read dates.
- `references/tools.md` every call used here, with behavior and pitfalls from saved live outputs, and the steps that need a live check.
- `references/company-status.md` the status step (what each status filing or register state says and does not mean), outside-site requests and the change-log window, rows DL-135 to DL-168.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules, MNPI handling, routing and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/portfolio-comparison-dtx.md` a worked A2 run on saved live library data; `examples/live/` the saved outputs and their origins (`SOURCES.md`).
- `scripts/portfolio_table.py` turns saved `compare_portfolio` and `get_funding_signals` output into tables with the notes the person must see, cross-checks funding counts, checks a scored ranking (values, ties, swap points, dominance), lists the status filings to open, and counts an answer's words (`words`).
- `references/named-company-status.md` status of named companies (Pear Therapeutics, Akili, Big Health, Aidoc) and current FDA listing holders of named products, as the filings and FDA records state them on 20 October 2026, each with what it does not mean (SP-148 to SP-169).
- `references/strategy-and-portfolio-research.md` the shared strategy and portfolio research file (SP rows, copied unchanged with its origin line); this skill cites the company status rows SP-148 to SP-169.
