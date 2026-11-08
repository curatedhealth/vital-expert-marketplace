Input:    the signed market register (its country_patients block: low / central / high per country as low / mid / high), the timeline ranges (launch years, probability of success) and the exclusivity register (end dates), per country (intake items 2 to 4)
Atom:     extract-requirements-from-source (the upstream registers are the source; one row per country and field, with the row reference of the register it came from)
Tool:     none
Template: none
Output:   per country: patients low, mid and high with source, year and geography; launch year early, mid and late; exclusivity end date; the probability of success low, mid and high with its source reference; fields a register does not carry are GAP
Check:    every figure points to a register row or is GAP; a country figure never comes from another geography; no estimate of a missing launch year or end date. Rule: upstream gaps stay gaps
Human:    the deal lead (BD head or investment lead) confirms the figures; the skill states no opinion
