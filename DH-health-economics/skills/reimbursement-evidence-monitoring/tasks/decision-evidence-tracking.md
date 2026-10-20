# A1 Decision evidence tracking

Framework task: DH-01.07.1.2, Part A, task A1.

## What this task delivers

A dated log of decisions on the person's product and on comparable products, read for the evidence: the recommendation category in the body's words, what the body said about the economic case, the uncertainties and limitations it named, the evidence it asked for, and any evidence window that follows, each quoted verbatim with its section, URL and read date. It answers "what did NICE (or HAS, BfArM) say about the evidence and the economics, for us and for products like ours?"

Why it matters: a decision's text is the most precise statement a company gets of what its evidence lacked. A committee that calls cost savings "uncertain" because data could not be extrapolated beyond one year, or that asks for eleven named outcomes during early use, has written the next evidence plan. Comparable decisions show which evidence a body has accepted for similar products. Neither is a forecast.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead |
| Skill | DH-01.07.1.2 Part A, Decision evidence tracking |
| Workflow | The steps below |
| Knowledge | `references/decision-evidence-sources.md`; `references/access-monitoring-sources.md` (EN, DE-, FR- rows); `references/health-economics-methods-research.md` |
| Tools | `market-access-dh.list_schemes` (free); `market-access-dh.find_scheme_precedents`; `market-access-dh.get_status_history`; the decision page at each row's `source_url` (read, not a library call); `scripts/decision_evidence_log.py` (optional); `verify.build_record` on clearance |
| Prompt | This guide |
| Template | `assets/decision-evidence-output.md` |
| Input | The request and its context: the person's decisions (body, reference, letters or guidance), the product's indication and route, comparables they care about |
| Governance | `references/governance.md` |
| Catalogue job | `scheme-precedents` covers step 2 (call `find_scheme_precedents` only; never `watch_scheme`). No job reads decision text (`references/tools.md`) |

## Read the request

- **Own decisions.** For each: body, reference (for example HTG675), date, and the document if the person has it. A decision still in development is not in the library.
- **Comparables.** Named guidance or products, or "similar" by indication. For DiGA, ask for the ICD-10-GM code.
- **Focus.** Economic evidence, clinical evidence, or both. Default to both, with the economic statements first.
- **Mode.** "What did NICE say about Sleepio's economics?" is short mode. A review pack across several decisions is full mode.

## Workflow

### Step 1. Know what the library can see

Call `market-access-dh.list_schemes` (free). Note the row counts for the schemes in the request. UK_NICE_NHAP and FR_LPPR held no rows on 19 October 2026; say so once if relevant.

### Step 2. Find the decisions

Call `find_scheme_precedents` on the scheme (UK_NICE_EVA for early use, UK_NICE_HTG for routine use, DE_DIGA by ICD code, FR_PECAN or FR_LATM), with `indication` where it narrows. Keep reference, title, stored status, publication date, source URL and retrieval date. Then apply what the library does not:
- Merge renumbered NICE guidance (HTE8 is HTG675; HTE9 is HTG676) and count each once.
- An early-use title stored as permanent (HTG778) is flagged: read the guidance.
- "Last updated" sits only in the stored passage; if the person needs to know whether a decision changed, call `get_status_history` and say when it holds only a day-zero snapshot (`references/tools.md`).

### Step 3. Read each decision for the evidence

The library holds the page header, not the reasoning. For each decision in scope, read the guidance page at `source_url`: the overview ("Last reviewed", migration note), recommendations, the technology chapter (prices), evidence (model results per price and scenario), committee discussion, evidence generation or further evidence sections, and update information; or ask the person for the document. Saved examples: `examples/live/nice_pages/htg624_*_2026-10-20.txt` and `htg562_*_2026-10-20.txt`. Using the checklist in `references/decision-evidence-sources.md`, quote verbatim with section numbers:
1. The recommendation category (`HE-071`).
2. What it says about the economic evidence, with any price, uptake or horizon it rested on, and the section 3 model result for each price and scenario the answer needs. Tie each doubt to the price, model or scenario it was raised against; a doubt raised on an earlier price is not a doubt about the accepted case. For HTG624: uptake ("any cost savings depended on the uptake rate") and the 3-year extrapolation ("did not agree that there was enough evidence to extrapolate the data to 3 years") were raised on the population-based price and the £66.11 tiered price (4.14); at £45 per user the EAC base case was "cost saving by £4.52 per person" at 1 year and "the results do not depend on the uptake of the technology" (3.9); the committee concluded "likely to be at least cost neutral and very likely cost saving", with limits from "dependence on the Sampson et al. (2021) study and the lack of remission outcomes" (4.15).
3. Every uncertainty and limitation the evidence and committee discussion chapters name, section by section, including clinical-evidence limits that feed the model. List every doubt section, never a sample (for HTG624: comparator definition 3.4, head-to-head evidence 4.5, drop-out bias 4.6, model variables and data linkage 4.13, uptake and extrapolation on the earlier prices 4.14, single-study dependence and no remission outcomes at £45 4.15, equivalence 4.16). Each line names the price, model or scenario it applies to, or "all prices" where the doubt is about the evidence itself. In short mode, keep one line per section; if that pushes the answer over 450 words, shorten each line to section number, price and five to ten words.
4. The evidence asked for, as listed.
5. The stated period or review point for early use. The guidance's own period governs over the PMG48 default of 3 years (`HE-072`, `EN-1`; for example review within 4 years in HTG675, `EN-6`).
A decision you did not read is `[GAP]`, never summarized from its title. With code execution, write the quotes into a notes file and run `scripts/decision_evidence_log.py --rows <saved JSON> --notes <notes JSON> --as-of DATE` for the merged log and the window counts.

### Step 4. Other bodies

- **DiGA.** Struck positive care effects in the directory show which claimed effects a trial did not confirm (`DE-24`); the library does not hold them (register N7), so read the directory entry. Aggregate trial outcomes and the payer's stated removal reason are context (`DE-1` to `DE-3`).
- **HAS.** Opinions are published; the library holds none (register N7). Named cases in the references: `FR-5` (a favorable LPPR opinion for a digital therapeutic with a required real-world follow-up study), `FR-6`.
- **EU JCA.** Reports state relative effects and certainty, with no economic content (`ES-149`, `HE-094`).
- **ICER-PHTI, IQWiG.** No individual report was read: `[GAP]`.

### Step 5. Say what it means

In facts: across the decisions read, which kinds of evidence the bodies accepted, which economic assumptions they doubted (for example extrapolation beyond the observed horizon, clinical equivalence assumed without direct evidence), and which outcomes they asked to be generated. Say which of these touch the person's own evidence, and route the response: building or fixing the case to `reimbursement-evidence-support` (A2, B1); status, clocks and resubmission to dh-market-access. Never say how a body would decide on the person's product.

## Build the output

Follow `assets/decision-evidence-output.md`. Answer first: per decision, one line on what it said about the evidence. Then the log table, the verbatim statements, and the evidence windows. Short mode keeps the table and, per decision, the economic conclusion with its price and model result, and one line per doubt section tied to its price or scenario.

## Before you hand it over

- Every decision statement is verbatim, with section, URL and read date; a decision not read is `[GAP]`.
- Every doubt section the guidance names is listed, each with the price, model or scenario it applied to.
- Renumbered guidance counted once; stored status at odds with the title flagged.
- Windows labeled with their source (the guidance's own period or the PMG48 default) and counted from a stated date.
- No forecast; comparables are context.
- Short mode counted: 450 words or fewer.
- Record line present.

## Boundaries

- No listing status, objection or review clocks, prices or resubmission: dh-market-access (`hta-submission-and-payer-engagement-monitoring`).
- No appeal or comment drafting beyond a labeled draft for the owner.
- Drugs, biologics and wellness apps are out of scope.
