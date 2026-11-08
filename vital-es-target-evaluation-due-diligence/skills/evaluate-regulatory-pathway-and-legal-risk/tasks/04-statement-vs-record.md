Input:    seller's public statements (intake item 5); regulator correspondence (item 4)
Atom:     classify-text-labels (label per statement: matches the record / not in the record / contradicts the record / record not supplied)
Tool:     none
Template: none
Output:   risk rows of category statement_vs_record, each with public_statement_ref and regulatory_record_ref (or GAP)
Check:    the complete response letters are read at openFDA (VP-D-053); a statement is compared with the letter, not with a press release (VP-D-050, VP-D-080 to VP-D-082); each row has both references; "record not supplied" is a gap naming what it hides (failure mode RL-01). Rule: do not infer the content of a letter that was not supplied
Human:    the named regulatory reviewer (counsel for legal rows) reviews the output
