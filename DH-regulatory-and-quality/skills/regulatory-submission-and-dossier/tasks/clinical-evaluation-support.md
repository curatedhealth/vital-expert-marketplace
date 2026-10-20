# A2 Clinical evaluation support

Framework task: DH-03.03.4.1, Part A, task A2. Replaces "Clinical Evaluation Report Assembly".

## What this task delivers

A clinical evaluation skeleton for a software device that follows MDR Article 61 and Annex XIV Part A, organized by the three MDCG 2020-1 components, with the person's evidence placed in it, candidate literature found through the library, each record's design and draft level labeled with its basis, the gaps a notified body will see (mapped to the MDCG 2020-13 CEAR sections), and any claimed finding checked only against a results passage read in the same direction. It answers "what does our clinical evaluation need, what do we have, and where are the holes?"

Why it matters: the notified body documents its assessment of the CER section by section (S-66), and checks claimed equivalence specifically (S-69). Gaps found before submission cost a revision; gaps found by the notified body cost a review cycle.

## The formula for this task

| Slot | For this task |
|---|---|
| Worker | SaMD Regulatory Affairs Director |
| Skill | DH-03.03.4.1 Part A, Clinical evaluation support |
| Workflow | The steps below |
| Knowledge | `references/clinical-evaluation-method.md`; `references/submission-sources-supplement.md` (S-55 to S-76); `references/REG_PATHWAYS_SUBMISSIONS.md` (RP EU-17 to RP EU-20, RP EU-32 to RP EU-34) |
| Tools | `literature.search_literature`, `literature.get_record`, `literature.classify_study`, `literature.grade_evidence`; `verify.qualify_source` then `verify.check_claim` (only with a results passage); `verify.build_record` on release |
| Prompt | This guide |
| Template | `assets/clinical-evaluation-output.md` |
| Input | Intended purpose, target groups, indications and contra-indications, clinical claims, class (as decided), the person's existing evidence (studies, V&V reports, literature), any equivalence claim |
| Governance | `references/governance.md`; the sufficiency judgment and every clinical conclusion are the person's |

## Read the request

- **Intended purpose and claims.** The plan is built around them (RP EU-20). If they are missing, ask; do not infer them from the product name.
- **Class and route.** From the person. For class III and implantables, clinical investigations are the default unless an Article 61 exception applies (S-78; the regulatory owner decides whether an exception applies).
- **Existing evidence.** Ask for the list; the person's own reports are the backbone. Library search only finds candidate publications.
- **US only?** For a US-only submission, there is no sourced FDA clinical-evaluation structure in this skill (`clinical-evaluation-method.md`); clinical data go in Performance Testing (S-13, S-19). Offer the MDCG 2020-1 structure as an organizing frame, labeled as EU guidance.

## Workflow

### Step 1. Lay out the plan skeleton

From Annex XIV Part A Section 1 (RP EU-20, S-58): GSPRs needing clinical data; intended purpose; target groups, indications, contra-indications; intended clinical benefits with outcome parameters; methods for clinical safety; benefit-risk parameters; clinical development plan including PMCF. Fill each line only with what the person gave; mark the rest `[GAP]`.

### Step 2. Place the evidence in the three components

Use the table in `clinical-evaluation-method.md`. For each component (valid clinical association, technical performance, clinical performance) list the person's evidence, its type and the source row that says that type can count (S-60 to S-62). Then the amount and quality questions (S-63) as headings for the person's justification. Note that clinical performance validation is considered at each new release (S-64).

### Step 3. Find candidate literature

Call `literature.search_literature` with the indication and the intervention in plain terms (for example `query="digital cognitive behavioral therapy for insomnia randomized controlled trial app", limit=10`). For promising records, call `literature.get_record` by DOI or PMID. Then `literature.classify_study` and `literature.grade_evidence(question_type="treatment")` on the records the person wants to consider.

- Report each record as found: design label with `publication_type_raw`, draft level, whether it is a preprint or a conference abstract, and that the excerpt may stop before results.
- On 19 October 2026 a conference abstract titled "pooled analysis" came back as a meta-analysis at CEBM level 1 (`tools.md`). Correct the label in your table ("conference abstract; library label meta-analysis decided by title text").
- State that this search is not the systematic literature review Annex XIV asks for (S-58); the review protocol is the person's.

### Step 4. Check findings only against results passages

If the person (or a draft CER) states a finding from a paper, check it this way:

1. Get the results passage: from the person, or from the paper's open-access text they point to. The library excerpt is not enough if it ends before the results. When the claim is a single accuracy figure, ask for the companion metrics MDCG 2020-1 lists (specificity, PPV, NPV, confidence intervals; S-81) from the same report. Do not judge whether they are sufficient.
2. `verify.qualify_source(doi=...)`.
3. `verify.check_claim(claim={"text": ...}, passage={"text": <exact results sentence>, "locator": <section, table or page>}, source=<qualified source>)`.
4. Accept "supported" only if you have read that passage and it states the finding in the same direction. If the passage states only the aim or design, report "not checked: no results passage", whatever the tool returned (register N3).

### Step 5. Equivalence, if claimed

Lay out the three characteristic groups and the threshold (S-75, S-76) as a table for the person to fill, with "data access shown?" as its own line. Do not judge equivalence.

### Step 6. See it from the notified body's side

Map each part of the skeleton to the CEAR section that will assess it (S-66, S-67): C for device, classification, CEP, equivalence and state of the art; D for the literature review; E for investigations; F for PMS and PMCF; G for IFU and SSCP. List the gaps per CEAR section.

### Step 7. What it means for the person

State the consequence of the gaps in sourced terms only (for example: "Without a PMCF plan or a justification, Annex II 6.1(d) is not met (S-54)").

## Build the output

Follow `assets/clinical-evaluation-output.md`. Answer first: the components that are covered, the ones that are not, and the one decision the person must make next. Then the skeleton, the evidence table and the CEAR gap view.

## Before you hand it over

- No clinical conclusion, sufficiency judgment or equivalence decision is written as the model's.
- Every record shows its design basis; every "supported" rests on a results passage you read.
- Draft or superseded guidance is flagged with its date.
- Clinical wording for the CER stops for the regulatory owner; label it "draft for the regulatory owner".
- If it leaves the conversation, ask who clears it and call `verify.build_record`; otherwise label it an uncleared draft.

## Boundaries

- Not a systematic review and not a CER: a structure, an inventory and a gap list.
- Usability or engagement figures are not clinical evidence.
- Study design for new investigations belongs to clinical validation (DH-01.02).
