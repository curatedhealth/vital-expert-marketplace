# Output format: cohort, features and data handoff

Short mode: 450 words maximum, counted without the calls list and the Source and Rows columns. Before handing over, count the words with `python3 scripts/prep_check.py words ANSWER.md` (counts the body without the calls list and leaves out Source and Rows columns); without code execution, count the same way by hand. The note that the connector was unavailable goes in the calls list, not the body. In short mode a table keeps only rows tied to the person's question; the rest go to the full version. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

Build lines 2 to 4 from `scripts/prep_check.py cohort`, `features` and `split` output; do not recount by hand. Budget in words: answer 70, cohort 80, features 110, split 60, handoff 60, record 50.

1. **Answer** (two sentences): start and final counts with the step that removes most; the features to refuse (yours to confirm) and the inputs carrying a 45 CFR 92.210 duty; the split flags; whether the handoff has a version.
2. **Cohort rule:** population, window, setting, exclusions, unit of row, in your words; attrition in one line per step with flags C1 to C3; operational definitions present or "not given" (FDA RWD guidance on EHR and claims data, July 2024, CV80).
3. **Features:** Feature · Window from index · Missing code · Flags; refusal candidates (F3, F5, F7) "for you to confirm"; F6 inputs with the 92.210 duty (45 CFR 92.210, PE-113) "for your legal owner".
4. **Split:** subsets with patients and sites; S1 and S2 as facts beside the FDA draft's proposal of independent test data from different sites (DA-39, DA-41, draft).
5. **Handoff:** version (or "not given": not handed over without one), remaining missingness, provenance and license, who may change the cohort rule (yours, or owner not named).
6. **Calls made**, then one line offering the full version.
7. **Record (the very last line, nothing after it):** "Data preparation draft for the owner. AI-assisted." Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.

## Full mode

### Answer
### Intended use and index time (yours)
### Cohort rule and definitions
| Variable | Conceptual definition (yours) | Operational definition (yours) | Accuracy against a reference standard (yours or published, with passage) | Source and rows |
|---|---|---|---|---|
### Attrition (script output)
| Step | Rule | Remaining | Excluded | Share of start | Flags |
|---|---|---|---|---|---|
### Feature dictionary (script output)
| Feature | Source field | Window from index | Missing code | Available at decision | Flags |
|---|---|---|---|---|---|
### Features to refuse (your decision) and 92.210 inputs (for your legal owner)
### Split check (script output) beside the sourced rules
| Subset | Patients | Sites | Flags | Rule and status (draft, final, market) | Rows |
|---|---|---|---|---|---|
### Handoff record
| Field | Value |
|---|---|
| Dataset version | |
| Cohort rule | |
| Features used and refused | |
| Split and flags | |
| Remaining missingness per feature | |
| Provenance and license (FAIR R1.1, R1.2, a guide) | |
| Transformations and their impact | |
| Standards and versions (OMOP, USCDI: published versus required for certification) | |
| Who may change the cohort rule | |
### EU AI Act Article 10 items you document (if a high-risk system; application date as amended)
### Gaps
### Calls made
### One line offering anything not shown
### Record (the very last line)
Data preparation draft for the owner. AI-assisted. Clears it: [the person named, in their words, or owner not named]. The record is built with `verify.build_record` once that named person clears it; until then, uncleared draft.
