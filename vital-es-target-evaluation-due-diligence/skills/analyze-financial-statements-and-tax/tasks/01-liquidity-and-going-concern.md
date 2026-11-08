Input:    latest annual and interim reports; the liquidity and capital resources discussion; the notes on going concern, subsequent events and debt (intake items 2 and 3)
Atom:     extract-requirements-from-source (the filing as the source; extract the stated cash, the stated sufficiency period, any going-concern language, any "material deficiency" statement)
Tool:     none
Template: none
Output:   going_concern block (filed_language_present true or false; the quote; source with filing, period and note), cash and debt figures with sources
Check:    the quote is verbatim from the filing; the period covered by the company's own sufficiency statement is stated; rule ids FIN-HORIZON-12M and FIN-AUDITOR-1Y named where a flag applies. Rule: never write "no going-concern issue"; if no language is found, write false with the filing and the section searched
Human:    the named accountant (tax specialist for tax flags, counsel for license obligations) reviews the output
