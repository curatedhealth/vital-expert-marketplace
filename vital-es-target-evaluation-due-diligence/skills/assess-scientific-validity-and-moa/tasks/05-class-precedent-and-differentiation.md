Input:    other agents against the same target or mechanism; class warnings; differentiation claims (intake items 8 and 9)
Atom:     extract-requirements-from-source; compare-against-criteria (addressed / not addressed)
Tool:     scripts/mechanism_check.py (class)
Template: none
Output:   class_precedent rows (agent, outcome, source); differentiation rows (versus, claim, basis, source); flags for adverse precedents with no sourced differentiation
Check:    each class warning states what it rests on for that agent (randomized_safety_trial, pharmacovigilance_or_pooled, mechanistic_extrapolation) and is described as class-wide vigilance, not proof of uniform class toxicity (VP-F-121, VP-F-123); the FDA labeling-change draft (VP-F-130, VP-F-131) is context and does not use the word class; outcome from the list approved, failed_efficacy, failed_safety, class_safety_warning, ongoing, withdrawn; a class warning is always listed. Rule: a differentiation claim without a basis and a source is not counted
Human:    the named scientist reviews class precedent and each differentiation basis
