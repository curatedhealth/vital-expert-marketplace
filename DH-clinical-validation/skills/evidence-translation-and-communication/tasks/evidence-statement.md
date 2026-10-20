# A1 Evidence statement

Framework task: DH-01.02.2.1, Part A, task A1. Replaces the old "Regulatory Evidence Dossier Authoring" section: it delivers the evidence summary a dossier, a payer file or a publication draws on. Assembling a device submission stays with dh-regulatory-strategy; an HTA dossier with dh-market-access.

## What this task delivers

One statement per outcome the person cares about: the outcome as measured, population, comparator, time point, the effect as the paper reports it, the passage it rests on (read in the same direction), the study count and design as checked against the paper, the retraction check, and the certainty as rated by a named person or body, or `[GAP]`. Plus a reference list built by the library.

Why it matters: most evidence communication errors start here, upstream of any audience. A comparator that drifts from "waiting list" to "usual care", a within-arm change reported as a difference between arms, or a design label taken from a database make every later message wrong, and no reviewer downstream sees the paper.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | Digital Health Access & Reimbursement Lead (`digital-health-access-reimbursement-lead`) |
| Skill | DH-01.02.2.1 Part A, Evidence statement |
| Workflow | The steps below |
| Knowledge | `references/certainty-wording.md`; `references/evidence-synthesis-research.md` (ES rows); `references/clinical-study-and-rwe-research.md` (CV rows on reporting) |
| Tools | `literature.list_sources` (free); `literature.get_record` or `literature.search_literature`; `literature.check_retraction` or `verify.check_currency`; `verify.qualify_source` and `verify.check_claim` per outcome passage; `literature.build_evidence_table`; `literature.build_citation`; `verify.build_record`; `scripts/statement_check.py` (optional) |
| Prompt | This guide |
| Template | `build_evidence_table` rows for the data, completed by hand from the passages; `assets/evidence-statement-output.md` for the answer |
| Input | The request and its context: the studies (DOI, PMID, registry id or document), the results passages or full text, the outcomes that matter, the person's certainty ratings and who made them, the intended use if the statement will be used externally |
| Governance | `references/governance.md` |
| Catalogue job | `evidence-table` (available): the buyer's one-call option. The steps below remain the method, because the job's grade and table steps return a design-based starting level and empty effect fields (`references/tools.md`). `examples/live/jobs_and_experts.json` |

## Read the request

- **Which studies?** Use the studies the person names. If the person asks for "all the evidence", say that a systematic search is the work of dh-clinical-validation (literature-and-real-world-evidence-review), offer to run there, and meanwhile work on what is in hand, saying the list is not a search.
- **Which outcomes?** The person's critical and important outcomes, up to seven per comparison if they want a Summary of Findings layout (ES-97). If none are named, ask once; otherwise use the primary outcome stated in the paper and say so.
- **Ratings?** Ask whether certainty has been rated and by whom. Never rate it yourself.
- **Short or full?** "What did the trial show" is short. "Evidence summary for the dossier", "evidence table", "Summary of Findings" is full.

## Workflow

### Step 1. Know what the library can reach

Call `literature.list_sources` (free). Keep the loaded and gap lists; Cochrane, Embase and PROSPERO are gaps. Any search-based statement says so.

### Step 2. Resolve each study

Call `literature.get_record` with the DOI or PMID for each study the person named (or `search_literature` with the title if only a name is given; confirm identity from authors, year and venue). Check the design and the registry id against the paper or abstract the person supplies, never from `design` or `trial_ids` alone (register N8). A protocol is not a result.

### Step 3. Check currency

Call `literature.check_retraction` (or `verify.check_currency`) per DOI. Report the status and the source checked (Crossref only in the live run). Retraction notices and errata matter for every included study (ES-119). A retracted study leaves the statement.

### Step 4. Read and check the passage for each outcome

For each outcome, take the results passage from the paper (the person's PDF, the full text, or the abstract when only the abstract is available, said as such). When a source is open access, read the full text before marking a field `[GAP]` from an abstract. Write the candidate statement in the paper's direction, with its population, comparator and time point. Call `verify.qualify_source` with the DOI and the person's question, then `verify.check_claim` with the statement, the verbatim passage (`text`, `locator`) and the full returned source object (register C18). Keep numbers and instrument names in the claim only if the passage states them: in the live run a faithful claim naming "PHQ-9" came back `partial` because the passage did not contain it. Accept only after reading the passage yourself: same direction, population, comparator, time point (register N3: a wrong comparator and an overstatement both came back `partial`). No passage: `[GAP]`.

### Step 5. Record the effect exactly as reported

Copy the effect measure the paper gives (mean difference, standardized effect, risk ratio, p-value) with its time point. Do not convert a standardized effect into points, a within-arm change into a between-arm difference, or a p-value into "proven". A single trial is "one randomized trial of N participants" (`references/certainty-wording.md`, rule 6).

### Step 6. Certainty, as rated

For each outcome, write the rating the person, a review or an HTA body gave, with the rater and date, and the reason for any rating below high (ES-99). If none, write "certainty not rated `[GAP]`" and list what a rater would look at (ES-91, ES-92), without filling the domains. If the person asks for a draft rating, decline the rating and offer the domain checklist. A `grade_evidence` output is reported, if at all, as "library starting level from design label, not a rating". For an EU JCA, quote the report's own certainty words (ES-149, ES-166). Where a rating is given, word the statement with the Table 15.6.b verb for that rating: direct for high, "likely" or "probably" for moderate, "may" for low, "the evidence is very uncertain" for very low (ES-203 to ES-206; `references/certainty-wording.md`, rule 5). The level's meaning comes from GRADE handbook Table 5.1 (ES-195 to ES-198). The rating stays the person's.

### Step 7. Table and references

Call `literature.build_evidence_table` with the records, the passages keyed by `record_id`, the PICO and `standard: "grade"`. Fill `outcome` and `effect` by hand from Step 4 where the tool returns `[GAP]`, and say so. Do not print the tool's `evidence_level`. Call `literature.build_citation` per record for the reference line. With code execution, run `scripts/statement_check.py` on the draft statements and the passages: it lists numbers that appear in no passage and certainty words above the person's rating, and certainty verbs stronger than the Table 15.6.b wording for the highest rating supplied (ES-203 to ES-206), for you to judge.

## Build the output

Follow `assets/evidence-statement-output.md`. Answer first: one sentence per outcome. Then the table, the gaps and the record line.

## Before you hand it over

- Every statement has a passage read in the same direction, or is `[GAP]`.
- Design and registry id checked against the paper, not the label.
- Certainty is the person's or a named body's, with date, or `[GAP]`; no library level printed as a rating.
- No "proves", "safe and effective", "cost-effective".
- Count the words in short mode (450 maximum, without the calls list and source column).
- If the output leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- No systematic search or risk-of-bias assessment here: dh-clinical-validation (literature-and-real-world-evidence-review).
- No economic conclusion: dh-health-economics.
- No device status or submission assembly: dh-regulatory-strategy (regulatory-pathway-and-classification). No HTA dossier wording, payer routes or prices: dh-market-access (payer-engagement-and-hta-submission). No marketing claims: dh-commercial (pricing-and-value-proposition).
- Drugs and biologics are out of scope: say so in two or three lines and stop without calling the library.
