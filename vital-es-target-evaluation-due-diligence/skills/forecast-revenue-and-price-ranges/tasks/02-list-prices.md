Input:    the countries in scope, the asset or its comparators, and the public price pages in references/source-register.md (intake item 5)
Atom:     extract-requirements-from-source (the dated public price record is the source; one row per country: price per patient-year low, mid and high, reference, date, public yes or no)
Tool:     connectors (read-only); price pages read by a person where scripted access is refused
Template: none
Output:   per country: list price per patient-year as a range with a dated source reference; a team assumption is marked public false; a country without a source is GAP
Check:    every price has a reference and a date on or before the reference date; the currency is the country's own; no net or discounted price is entered as list. Rule: the pages differ by country in what they contain and how often they update (references/markets/)
Human:    the deal lead confirms every price and its source
