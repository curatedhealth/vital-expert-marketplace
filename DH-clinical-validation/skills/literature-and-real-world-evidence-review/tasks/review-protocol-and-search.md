# A1 Review protocol and search

Framework task: DH-01.02.4.1, Part A, task A1. Replaces the old *Search literature*, *List literature sources* and the search half of *RWE Data Pipeline Management*.

## What this task delivers

A review protocol draft and a search plan that the person's target body will accept: the question as PICOs, eligibility criteria, the sources each rule requires with what the library can and cannot reach, a draft strategy per database with its PRESS check, the reporting items (PRISMA 2020 items 6, 7 and 24; PRISMA-S), the registration step, and, for an EU JCA, the cut-off date and AI-use plan. It answers "what exactly are we asking, where do we search, with what, and what must we report?"

Why it matters: the search decides what the review can ever find. EU law sets a floor of MEDLINE plus CENTRAL and a cut-off at most 3 months before submission (ES-151, ES-152); Cochrane makes several search steps mandatory (ES-43, ES-46, ES-48, ES-50, ES-51). A protocol fixed in advance is what keeps the review from bending to its results (ES-38).

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Clinical Informatics Lead (`clinical-informatics-lead`) |
| Skill | DH-01.02.4.1 Part A, Review protocol and search |
| Workflow | The steps below |
| Knowledge | `references/review-rules-by-body.md` sections 1 to 3, 5 and 6; `references/rwe-and-digital-endpoints.md` sections 1 and 5 when RWD or digital endpoints are in scope; ES-01 [PAPER] doi 10.1136/bmj.n71 to ES-68, ES-110 [PAPER] doi 10.1016/j.jclinepi.2020.10.007 to ES-118 [PAPER] doi 10.1136/bmjebm-2024-112899, ES-145 to ES-170, ES-194, ES-228 to ES-234 |
| Tool | `literature.list_sources` (free); `literature.search_literature` to test terms; `literature.get_record` for known key papers (seed set); `literature.find_related` for citation searching |
| Prompt | This guide |
| Template | `assets/protocol-and-search-output.md` |
| Input | The decision the review serves and the target body; the product, population and comparators; the person's scope or PICOs; known key studies; the planned publication or submission date; any existing protocol |
| Governance | `references/governance.md`; the question, criteria and protocol are the person's |
| Catalogue job | none |

## Read the request

- **Target body and purpose.** EU JCA, NICE (PMG36 or PMG48), IQWiG, a Cochrane-style publication, a CER, or an internal decision. If not named, ask: the rules differ on databases, registries, cut-off and screening. If the person wants speed, a rapid review is a choice with its own rules (ES-110 [PAPER] doi 10.1016/j.jclinepi.2020.10.007 to ES-118 [PAPER] doi 10.1136/bmjebm-2024-112899) and is not appropriate solely for ease or cost (ES-117 [PAPER] doi 10.1136/bmjebm-2023-112722).
- **PICOs.** For a JCA they come from the assessment scope; ask for them, do not invent comparators (ES-167). For other purposes draft them from what the person gave and label them "proposed".
- **Study types.** Randomized trials only, or also non-randomized and real-world studies? If RWD or digital endpoints are in scope, read `references/rwe-and-digital-endpoints.md`.
- **Dates.** Planned submission or publication date, so the search window can be planned against the cut-off (ES-52, ES-152). Timing is the person's; state the rule, not a schedule.
- **Scoping instead?** If the person wants to map what exists rather than answer an effect question, offer a scoping review (PRISMA-ScR, ES-33, ES-34).

## Workflow

### Step 1. Write the question as PICOs

One row per PICO: population, intervention, comparator, outcomes (critical and important), time points. Mark each element "from the person" or "proposed". For a JCA, one PICO is one population, one intervention, one comparator and at least one outcome (ES-167), and the search covers every PICO in scope (ES-159). Note the synthesis PICOs that must be fixed now (ES-37).

### Step 2. Draft the protocol skeleton

Sections: question and PICOs; eligibility criteria (study designs, dates, languages with justification, ES-43, ES-50); sources; search methods; selection process with reviewer numbers by the target body's rule (`review-rules-by-body.md` section 4); extraction; risk-of-bias tools by design and body (`appraisal-and-certainty.md` section 1); synthesis plan including when not to pool and pre-specified subgroups (ES-83, ES-87); certainty method (GRADE, ES-89 to ES-96); amendments log (ES-41); team and conflicts (ES-42); AI and automation use (section 5 of the rules file).

### Step 3. List the sources the rules require

Build the source table from `review-rules-by-body.md` section 2 for the named body. Then call `literature.list_sources()` (free) and mark each required source "library can query", "library cannot query: run in the source" or "not a library source". On 19 October 2026 CENTRAL, Embase and PROSPERO were gaps (`tools.md`). State plainly that the library cannot meet the database floor on its own.

### Step 4. Draft and test the strategy

1. Draft the MEDLINE (PubMed) strategy: one block per PICO concept plus a study-design block, controlled vocabulary and free text (ES-49). Mark limits and justify each (ES-29, ES-50); for diagnostic questions no design filter (ES-130).
2. Test the free-text terms: `literature.search_literature(query="<plain-language PICO terms>", limit=20)`. Example measured: `query="digital cognitive behavioral therapy for insomnia app randomized controlled trial", limit=8` returned 29 merged records with off-topic hits. Use the off-topic and missed records to refine terms.
3. Seed check: for each known key study the person names, `literature.get_record(doi=...)`, and check the draft strategy would retrieve it (IQWiG tests against an independent set of relevant citations, ES-138).
4. Plan citation searching: `literature.find_related(record=<key study>, direction="cited_by", limit=20)` and reference lists (ES-48, ES-27).

### Step 5. PRESS check, before any search is run

Lay out the six PRESS 2015 elements (ES-63, abstract only) against the draft strategy, with what you see for each, and name the person's peer reviewer as owner (or "owner not named"). Cochrane strongly recommends peer review before running (ES-67); IQWiG always does it (ES-138); NICE's guideline manual has a second information specialist use a PRESS-based checklist (ES-231); timing is after the MEDLINE draft and before translation to other databases (ES-65). A missing element without explanation means the search may not be complete (ES-228). Plan to report how the strategy was developed and peer reviewed, with the reviewer named if they agree (ES-229, ES-230). The questions under each element were not reachable on 20 October 2026: write "PRESS checklist text not reachable `[GAP]`" and do not supply questions from memory.

### Step 6. Reporting and registration plan

- PRISMA 2020 item 6 (every source with last-searched date), item 7 (full strategies), item 24 (register name and number, or a statement that it was not registered, and amendments) (ES-06, ES-07, ES-15).
- PRISMA-S items 1 to 16 as a checklist with an owner per item (ES-25 [PAPER] doi 10.1186/s13643-020-01542-z to ES-31).
- Registration: PROSPERO recommended by Cochrane (ES-39); rapid reviews publish the protocol (ES-115). PROSPERO's own fields were not read `[GAP]`.
- JCA: Appendix D.2 strategies, RIS export, cut-off date at most 3 months before submission (ES-152, ES-156, ES-162).

### Step 7. AI-use plan

List each step where AI or automation will help (search term testing, deduplication, screening, extraction, risk of bias, analysis, drafting) with the human responsible. For a JCA, this table goes in the dossier (ES-169, ES-170). For IQWiG, AI screening needs shown suitability (ES-140).

## Build the output

Follow `assets/protocol-and-search-output.md`. Answer first: the rule set that applies, the sources the library cannot reach, and the one decision the person must make next (usually: confirm the PICOs, or name the search peer reviewer). Then the PICO table, source table, draft strategy and reporting checklist.

## Before you hand it over

- Every required source shows whether the library can reach it.
- Every limit has a justification or a `[GAP]`.
- Proposed PICO elements are labeled "proposed"; JCA PICOs are only the scope's.
- The cut-off rule for the named body is stated with its row, without turning it into a deadline.
- The AI-use table names a human per step or says "owner not named".
- Record line present in every answer, refusals included: "Clears it: [the person named, in their words, or owner not named]. The record is built with verify.build_record once that named person clears it; until then, uncleared draft."

## Boundaries

- Not the search itself: the person's searcher runs the strategies in each database and logs the dates.
- Choosing comparators or outcomes for a JCA is the assessment scope's, not the model's.
- Designing a new study or a new RWD collection belongs to clinical study design (DH-01.02.1).
- Checking whether an existing review is current belongs to `evidence-quality-and-signal-monitoring`.
