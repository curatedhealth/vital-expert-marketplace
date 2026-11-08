Input:    supplied dispute documents; public registers read through the connectors (Orange Book or Purple Book listing, PTAB, EPO register, Unified Patent Court)
Atom:     extract-requirements-from-source (rows: forum, parties, patent, status, date read, source)
Tool:     none
Template: none
Output:   list of live disputes and challenges with status as of the date read
Check:    each row has a source and the date it was read; an unread register is listed as a GAP with the consequence. Rule: status is as of the date read; no prediction of outcome
Human:    the named patent counsel (or named IP reviewer) reviews the output
