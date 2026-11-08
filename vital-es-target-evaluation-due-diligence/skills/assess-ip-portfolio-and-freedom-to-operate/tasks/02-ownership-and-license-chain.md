Input:    assignments, chain of title, in-licenses, option agreements (intake item 6)
Atom:     extract-requirements-from-source (rows: owner of record, link in the chain with date and document, licensor, field, territory, obligations with trigger)
Tool:     none
Template: none
Output:   ownership and license chain per family, and a list of obligations that pass to a buyer (royalty, milestone, change of control, assignment, sublicense, field limits)
Check:    every link from inventor to owner of record has a supporting document and the assignment language is read (present assignment versus promise to assign: Stanford v. Roche, VP-C-120 to VP-C-122; IP map, VP-C-130); each link has a document and date; each obligation has type, detail, trigger, source (validate_register.py E_OBLIGATION); a break in the chain is a GAP. Rule: say what the document says; whether a clause is triggered by this deal is a question for counsel, not a finding
Human:    the named patent counsel (or named IP reviewer) decides; the skill states no opinion
