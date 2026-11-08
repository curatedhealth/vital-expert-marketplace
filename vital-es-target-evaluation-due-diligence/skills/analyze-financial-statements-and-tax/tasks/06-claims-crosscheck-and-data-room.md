Input:    the seller's financial claims; the filings; the data-room index (intake items 2 and 9)
Atom:     compare-against-criteria (state set: consistent / inconsistent / not found in filings)
Tool:     none
Template: none
Output:   claims_crosscheck rows: claim, filing reference, result, question for every inconsistency, source; a list of exhibits referenced in the filings but absent from the data room
Check:    "consistent" cites the passage; "not found in filings" names the sections searched. Rule: a seller statement is a claim, not a source; whether an inconsistency is a misstatement is a human judgement
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) reviews the output
