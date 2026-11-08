Input:    outputs of tasks 01 to 06, buyer mode, unit
Atom:     compose-draft (templates/pathway-and-risk.md)
Tool:     python3 scripts/validate_pathway.py pathway.json
Template: templates/pathway-and-risk.md
Output:   pathway map and legal-and-regulatory risk register, answer first: the routes worth keeping open per market, the three risks that most affect the decision, what each puts at risk, options to close each gap with effort and risk
Check:    validate_pathway.py exit 0; route_choice and legal_opinion HUMAN ONLY; BD view (representations, conditions, milestones tied to designation or confirmatory-trial events) or investor view (what the route does to the timeline and the next inflection); options only. Rule: the team chooses the route; counsel gives the opinion
Human:    the named regulatory reviewer (counsel for legal rows) decides; the skill states no opinion
