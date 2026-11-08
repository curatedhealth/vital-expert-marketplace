Input:    the buyer's analog list or sourced candidates (intake item 4)
Atom:     extract-requirements-from-source (peak annual sales, year, currency and geography from the dated source)
Tool:     connectors (literature; company filings read by a person)
Template: none
Output:   analog rows: name, origin (supplied_by_person or sourced), similarity_basis, peak_annual_sales, currency, peak_year, geography, eligible population if known, source with ref and date, included or excluded with the reason
Check:    each analog carries a stated basis (properties, order of entry, unmet need, launch environment: practitioner criteria VP-H-030 to VP-H-032); forecast error is context only (VP-H-001 to VP-H-005); every row has a stated basis and a dated source on or before the reference date; one currency and one geography across included rows; excluded rows have reasons. Rule: never a figure from memory; an analog without a dated source is not used
Human:    the named reviewer with commercial experience reviews the output
