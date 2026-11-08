Input:    seller's patent list, register extracts, supplied documents (intake items 3 and 4)
Atom:     extract-requirements-from-source (one row per patent: number, family, jurisdiction, dates, claims text with passage); classify-text-labels (claim type per patent: composition, method_of_use, formulation, process, other)
Tool:     none
Template: none
Output:   patent family table: family id, patents, jurisdictions, claim types, filing, issue and expiry dates, source per row
Check:    every row has a source or [CHECK]; a missing date is a GAP naming the period it blocks; claim type comes from the claim text, not from the seller's label. Rule: do not infer expiry from filing date; take the expiry from the register or the seller and mark which
Human:    the named patent counsel (or named IP reviewer) reviews the output
