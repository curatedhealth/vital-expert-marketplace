Input:    filed license agreements and amendments; the license notes in the annual report (intake item 6)
Atom:     extract-requirements-from-source; classify-text-labels (milestone, royalty, sublicense_income, change_of_control, assignment, diligence, termination, other)
Tool:     none
Template: none
Output:   licensor obligation rows: licensor, agreement, type, trigger, amount or rate, passes_to_buyer (yes, no, needs consent, gap), source
Check:    a redacted milestone or royalty term (Item 601(b)(10)(iv), VP-E-012) is recorded as GAP with terms_redacted = true and a request for the unredacted agreement; it is never read as zero; each row quotes or points to the clause; change-of-control and assignment clauses are always looked for and recorded (as a row or as a GAP naming the clause not found); redacted terms are GAPs. Rule: whether an obligation binds the buyer is a legal question: record the clause and ask counsel; do not decide
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) decides; the skill states no opinion
