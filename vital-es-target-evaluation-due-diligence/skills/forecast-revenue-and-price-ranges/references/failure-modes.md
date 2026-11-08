# Failure modes for the revenue and price register

The detection questions are written for this skill (ENGINEERING RULE in grounding-register.md; no published detection checklist exists). The documented column says what the cited analysis is about, so that a reader can judge the fit.

| Id | How it enters the register | Detection question | Documented for | Passage ids | Status |
|---|---|---|---|---|---|
| FR-01 | A single optimistic forecast presented as the expectation | Is every revenue figure a low, mid and high range, and is the context that published forecasts have run high stated? | sales forecasts in reimbursement dossiers (Austria) and consensus forecasts of drugs | VP-H-001, VP-H-002, VP-H-010 | VERIFIED (re-opened) |
| FR-02 | Uptake path not comparable to the asset | Does every analog behind the share path have a written basis for comparability and a dated source, and is the share path the driver with the largest swing? | analog-based launch forecasting is common practice; no failure analysis located | none | [CHECK] |
| FR-03 | List price used as net, or net presented as a fact | Are list and net separate fields, and does net carry a setter's name and the word assumption? | confidentiality of discounts and rebates in Europe; US net prices differ by payer | VP-R-021, VP-R-023, VP-R-024 | VERIFIED (re-opened) |
| FR-04 | Loss of exclusivity ignored or erosion invented | Is the exclusivity end date placed, and is erosion applied only from supplied, sourced parameters, with a GAP otherwise? | price erosion after generic and biosimilar entry (US retail generics; European biosimilars); volume erosion not covered | VP-R-001, VP-R-002, VP-R-010 | VERIFIED (re-opened) |
| FR-05 | Launch timing taken as a single date | Do launch years come from the timeline ranges (early, mid, late), and is launch year in the sensitivity table? | launch timing is an input of the timeline skill; no failure analysis located for revenue | none | [CHECK] |
| FR-06 | A price or net ratio carried from one country to another | Does each country carry its own patients, list price source, net assumption and currency? | prices and discounts differ by country | VP-R-020, VP-R-021 | VERIFIED (re-opened) |

No mode is added without a published analysis behind it. FR-02 and FR-05 stay [CHECK]: they are detection questions for this skill; no failure analysis for them was opened in this build.
