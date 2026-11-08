Input:    rows with design facts, trial reports
Atom:     compare-against-criteria (criteria = the five RoB 2 domains (Table 1 of Sterne 2019); levels low / some concerns / high)
Tool:     none
Template: none
Output:   per randomized trial result, five domain judgements with a quoted basis, the result assessed, the effect of interest (assignment or adherence) and the overall judgement
Check:    scripts/validate_register.py agrees with the overall; the basis is a quote with a locator. Rule: non-randomized studies name their tool in rob_tool; with no report, rob is GAP. Human reviews every judgement
Human:    the clinical development reviewer judges every domain and the overall; the script only checks consistency
