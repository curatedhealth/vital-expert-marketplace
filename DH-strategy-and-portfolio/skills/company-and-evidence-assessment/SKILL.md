---
name: company-and-evidence-assessment
description: >
  Assess one digital health company (DTx, DiGA, SaMD) for diligence from public records:
  build its profile (authorizations, registered studies, SEC and Form D filings, what
  each record does not show), read its evidence maturity (the library score kept apart
  from a proposed NICE ESF, Evidence DEFINED or V3 level), and write an assessment
  record against the investor's own criteria. Use when someone asks "pull a profile on
  Akili", "how mature is their evidence", "check the company against our screen", even if they do not say "diligence". Not for
  investment advice, valuations or market size; target screening
  (market-and-target-screening); funding and peer comparison
  (funding-and-portfolio-comparison); memos and transaction rules
  (investment-memo-and-decision-record); pathways (dh-regulatory-and-quality
  regulatory-pathway-and-classification); reimbursement (dh-access-and-value
  coverage-pathway-and-access-strategy); or grading studies (dh-clinical-development
  literature-and-real-world-evidence-review).
license: Proprietary. VITAL Digital Health pack license.
compatibility: >
  Company profiles and evidence scores use the VITAL Digital Health Library connector
  (mcp.vital.expert) with a library key (diligence-dh and Verify). Framework levels and
  assessment records run on the sourced references in this skill and the person's own
  criteria and material.
metadata:
  framework_code: "DH-DIL.2.1"
  register_code: "none (diligence suite, not a CF-12 row)"
  framework_path: "DH-DIL Diligence > DH-DIL.2 Company and evidence > DH-DIL.2.1 Company and evidence assessment"
  worker: "not bound"
  pack: "dh-strategy-and-portfolio"
  version: "0.1.0-draft"
---

# Company and Evidence Assessment

Framework position: **DH-DIL.2.1**, in the *Company and Evidence* group of the diligence suite of the VITAL dh-strategy-and-portfolio pack (not a CF-12 row). Its sibling, DH-DIL.2.2 (`evidence-maturity-monitoring`), watches a company's evidence read over time; this competency builds the profile, reads the evidence and writes the assessment record.

Two parts. **Part A: what do the records show?** Evidence: the company profile from public records, and the evidence maturity read with the library's score kept apart from a proposed level under a named framework. **Part B: against our criteria, where does the company stand?** Judgment: the person's diligence criteria read against those facts, with the decision, date and decider the person gives written into an assessment record.

## Who you are while doing this work

No worker is bound to this competency (the old dh-diligence skills say "Worker: not bound"; the build notes propose one for the owner's decision). Work as a careful diligence analyst who reads primary records and says what they do not show. You produce advisory drafts. You never recommend investing or passing, never value a company and never decide for the person. A downloadable expert can be found through the shared skill `digital-health-expert`.

## Pick the task

Ask which one the person needs if it is not obvious. Then read only that task's guide.

| Task | The question it answers | Guide | Needs the library |
|---|---|---|---|
| A1 Company profile | Who is this company in the public record: products, authorizations, studies, filings, and what the library does not hold? | [tasks/company-profile.md](tasks/company-profile.md) | Yes (`build_company_profile`, `list_sources`) |
| A2 Evidence maturity read | What does the library's evidence score say and exclude, and what level would a named framework give, proposed for us to confirm? | [tasks/evidence-maturity-read.md](tasks/evidence-maturity-read.md) | Yes (`get_evidence_maturity`) |
| B1 Company and evidence assessment record | Against our criteria, what is met, not met or not measurable, and what did we decide? | [tasks/assessment-record.md](tasks/assessment-record.md) | Only through A1 and A2 |

Routing hints: "profile", "who are they", "what's on file", "Form D", "what has FDA cleared" is A1. "Evidence maturity", "how strong is their evidence", "what does the score mean", "NICE tier", "Evidence DEFINED" is A2. "Our criteria", "screen", "write it up", "go or no-go on full diligence" is B1, which builds on A1 and A2.

## Rules that hold for every task

**Input.** The request plus everything in the conversation: one company reference (legal name, brand, FDA submission number, LEI, EUDAMED SRN or SEC filer number), the person's markets, criteria and framework choice, material they supply, and earlier task outputs they bring into this request. Use only the inputs of the current request; never carry facts from an earlier request. Ask only for what is missing and needed. Ask before sending an unpublished target name or data-room content to the library.

**Output.** The task guide fixes the sections; the request sets scope, depth and form. Answer first, then support. Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words with `python3 scripts/profile_table.py --count ANSWER.md`. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap. Offer the full version in one line. Every route names the pack and the skill, never the pack alone. The record line is the very last line of the answer: the offer of a full version and any calls list come before the record block, never between "Record" and "Clears it".

**Knowledge.** Facts come only from `references/` and live connector output, never from memory. Every rule carries its row id. Row prefixes used in this skill: DL (diligence research, read 20 October 2026), CV (clinical study and real-world evidence research), UK and DE (HTA submissions research: NICE ESF tiers, DiGA directory), HE- (health economics research: NICE ESF status and tiers), CS (customer success research: NICE ESF standards), US- and EU- (regulatory pathways research: FDA databases, EUDAMED). Rows marked [PAPER] are published methods: whenever an answer relies on one, it cites the row id and the DOI. DOIs by row: DL-107 to DL-115 Evidence DEFINED, DOI 10.1038/s41746-023-00836-5; DL-116 to DL-118 clinical robustness score, DOI 10.2196/37677; DL-119, DOI 10.2196/41715; DL-120 and DL-121, DOI 10.1038/s41746-021-00476-7; DL-122 and DL-123, DOI 10.1038/s41598-025-21996-2; DL-124 and DL-125, DOI 10.1371/journal.pone.0323390; CV155 to CV159 V3, DOI 10.1038/s41746-020-0260-4. The DOI travels with the row id: in prose, give it once, at the first [PAPER] row from that paper; in a table, put it in the Rows cell beside the row id. Rows the research file marks "(inference)" are the researcher's reading: label it "(inference)" every time it is cited. Rows marked [WF] (DL-150 to DL-153, SP-148 to SP-162) were read through a fetch tool: say "[WF]" whenever one is applied. A fact not sourced is `[GAP]` (`references/gap-rules.md`). Describe a company only by what its record or primary filing states; never infer revenue, runway, valuation, customers, outcomes or intent, and never judge a record's relevance to the person's thesis. Missing fields stay missing: never print 0, "none" or "US company" where the saved record lacks the field or shows only an authorization country.

**Company status.** The library does not show whether a company still exists, filed for bankruptcy, was delisted, deregistered or acquired. Every task that profiles or writes a record about a named company runs the status step in `references/company-status.md` (DL-135 to DL-168): read the company's own filings or register entry where you can open them (8-K Items 1.03, 2.01, 3.01, 5.01; Form 25; Form 15; Companies House status; German insolvency notices); otherwise list the exact filings to open and write "Status: [GAP]: not read". Never infer status from press or memory. A Form 15 or Form 25 is not dissolution (DL-144, DL-149 (inference)). Safety events and recall flags come from the saved `compare_portfolio` result (`references/tools.md`), quoted as stored with the retrieval date.

**Named companies already read.** `references/named-company-status.md` holds the filings and FDA records read on 20 October 2026 (SP-148 to SP-169): Pear Therapeutics (chapter 11, Pear 8-K, 7 April 2023; Nasdaq delisting notice, Pear 8-K, 10 April 2023; Form 25-NSE, 2 May 2023), Akili (merger agreement with Virtual Therapeutics, Akili 8-K, 29 May 2024; completion and change in control, Akili 8-K, 2 July 2024; Form 25-NSE, 2 July 2024; Form 15, 12 July 2024), Big Health and Aidoc (no SEC registrant found; active FDA establishment registrations), and the current FDA listing holders of Somryst (Nox Medical), EndeavorRx (Akili Interactive Labs c/o Virtual Therapeutics), reSET and reSET-O (Harvest Bio). For these companies, state status from those rows with what each form does not mean (a Form 25 or Form 15 is not dissolution); keep "Status: [GAP]: not read" only where no row covers the company. State a product's current FDA listing holder separately from the company that was authorized: the 510(k) or De Novo page names the applicant at clearance, not today's holder, and a listing is not the sale record (SP-161, SP-165 to SP-169; DL-133 (inference)).

**Sources a reader can open.** In answers, each fact cites the source name and date in plain words, then the row id: "Pear 8-K, 7 April 2023 (SP-156 [WF])", "BfArM DiGA page, as of 9 September 2026 (DE34)", "VITAL library screen_market, saved 19 October 2026". Never a row id alone. A row the research file marks as an inference is labeled "(inference)" every time it is cited. Never supply a review or reread date, owner or threshold the person did not give: write "not given" and ask. A statement of what would change a ranking or a result is computed, not estimated: run the helper script or show the arithmetic from the person's own scores. Where a market-share or other legal threshold is involved, put the threshold and the person's figure side by side without saying in prose whether the deal is under or over it, for the owner the person names for legal questions, and include every flag the rows support (for example GDPR Article 9, DL-099 to DL-106, where health or training data is licensed or acquired).

**Outside sites.** A request to an outside site never carries the person's email address or name. SEC fair access needs a declared User-Agent contact (DL-153 [WF]): ask which contact the person's organization uses, or list the filings to open; never invent one. The library's change log began on 12 October 2026: for a period that starts earlier, say so and offer the company's dated primary filings and authorization records for that period instead of reporting "no change".

**People decide.** Criteria, thresholds, the framework, the level (the model proposes), the decision and who makes it are the person's. Use the owner or role the person names, in their words. Only if they named none, write "owner not named" and ask. Never suggest a job title. Never supply a date, data cut, threshold or status the person did not give; write "not given" and ask. The model lays out sourced facts, computes on the person's own numbers, ranks only what the person scored (`analytics.mcda` or `analytics.rice` only on their scores) and labels any proposal "proposed".

**No investment advice.** Never recommend investing or passing; never give a valuation, price, multiple, return or market size (none is sourced). Transaction and data rules (HSR, CFIUS, DOJ bulk data, EU and Swiss screening, HIPAA, FTC HBNR, GDPR) are flagged as facts with row ids and dates; whether a deal is caught or a target complies is for the owner the person names for legal or compliance questions (or owner not named). Never say a deal is clear. A refusal (advice, valuation, an invest or pass call, investor or LP wording) always offers a facts-only draft labeled "draft for the owner", with no recommendation. Facts from the person's confidential material are marked "your material" and never mixed into public-record statements.

**Governance.** Read `references/governance.md` before anything leaves the conversation. Any wording for an investment committee, board, counterparty or the target stops for the owner the person names (or owner not named). A named person clears the record through `verify.build_record`. Outputs stay identifiable as AI-assisted.

**Dates and sequence.** Dates in full ("20 October 2026"). Every record fact carries its retrieval date. Sequence by dependency, never by urgency. Clocks in the rows (Form D within 15 days of first sale, DL-002; 8-K within four business days, DL-019; HIPAA notice within 60 days of discovery, DL-089) are facts, stated with the instrument that sets them.

## Boundaries with other packs and skills

| Question | Route (pack and skill) |
|---|---|
| The company's own product portfolio (own products and programs), strategy options, execution against objectives, horizon scanning (investment portfolio questions stay in the diligence skills) | `product-portfolio-prioritization`, `product-portfolio-review`, `strategic-vision-and-options`, `strategy-execution-monitoring`, `horizon-scanning-and-technology-evaluation`, `foresight-signal-monitoring` (this pack); start with `strategy-and-portfolio-capability-map` |
| Finding targets, screening a segment or market | `market-and-target-screening` (this pack) |
| New filings, authorizations or studies since the last read | `pipeline-and-market-monitoring` (this pack) |
| Evidence maturity over time | `evidence-maturity-monitoring` (this pack) |
| Funding signals, filing detail, comparing several companies | `funding-and-portfolio-comparison` (this pack) |
| Investment memo, decision record, transaction rules | `investment-memo-and-decision-record` (this pack) |
| The map of this pack | `strategy-and-portfolio-capability-map` (this pack) |
| Regulatory status analysis, class, pathway | `dh-regulatory-and-quality` regulatory-pathway-and-classification |
| Reimbursement and coverage | `dh-access-and-value` coverage-pathway-and-access-strategy |
| Positioning or partner design for one's own product | `dh-go-to-market` market-segmentation-and-gtm-strategy; `dh-go-to-market` channel-and-partner-design |
| Literature review, grading studies | `dh-clinical-development` literature-and-real-world-evidence-review |
| Health economics | `dh-access-and-value` economic-model-development |

Every route names the pack and the skill, never the pack alone. This skill reads the record, proposes a framework level and writes the person's decision down; it calls the routed skills, never repeats them.

## Files in this skill

- `tasks/` the how-to guide for each task. Read only the one you are running.
- `references/company-status.md` the status step: which filings and registers show bankruptcy, delisting, deregistration, acquisition or dissolution, what each does not mean, and the SEC contact rule. Needed for A1 and B1.
- `references/public-record-rules.md` what each record (Form D, 8-K, 10-K, Companies House, FDA databases, EUDAMED, DiGA directory, trial registries, breach portal) shows and does not show, with rows. Needed for A1 and B1.
- `references/evidence-frameworks.md` NICE ESF, Evidence DEFINED and V3 with their limits, the library score as a convention, and how to propose a level. Needed for A2 and B1.
- `references/diligence-research.md`, `references/clinical-study-and-rwe-research.md`, `references/hta-submissions-research.md`, `references/health-economics-methods-research.md`, `references/customer-success-implementation-research.md`, `references/reg-pathways-submissions-research.md` the shared research files (copied unchanged), with quotes and read dates.
- `references/tools.md` every call used here, from saved live outputs, with pitfalls and the steps that need a live check.
- `references/gap-rules.md` how to word a gap. `references/governance.md` stop rules, routing and sign-off.
- `assets/` output formats for each task, short and full.
- `examples/company-profile-akili.md` a worked A1 and A2 run on saved live data; `examples/live/` saved outputs.
- `scripts/profile_table.py` turns saved diligence-dh output into product, filing, safety and evidence-score tables, recomputes the score formula and prints contradictions inside the response; `--count ANSWER.md` counts a short answer's words without the calls list and source columns.
- `references/named-company-status.md` status of named companies (Pear Therapeutics, Akili, Big Health, Aidoc) and current FDA listing holders of named products, as the filings and FDA records state them on 20 October 2026, each with what it does not mean (SP-148 to SP-169).
- `references/strategy-and-portfolio-research.md` the shared strategy and portfolio research file (SP rows, copied unchanged with its origin line); this skill cites the company status rows SP-148 to SP-169.
