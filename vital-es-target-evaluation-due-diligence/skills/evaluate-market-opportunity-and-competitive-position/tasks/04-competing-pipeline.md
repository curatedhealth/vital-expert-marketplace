Input:    ClinicalTrials.gov records, company statements, regulator pages (intake item 6)
Atom:     extract-requirements-from-source
Tool:     scripts/market_check.py (pipeline block)
Template: none
Output:   pipeline rows: agent, sponsor, mechanism, phase, expected timing, timing basis, source with ref and date; flags for registry-only entries and old sources
Check:    a registry-only status is read from two registries or flagged (VP-G-050, VP-G-051, VP-G-052); every source dated on or before the reference date; the timing basis stated; missing timing is a gap. Rule: a registry status or date is never the only basis for a competitor's timing
Human:    the named reviewer with market and clinical knowledge reviews the output
