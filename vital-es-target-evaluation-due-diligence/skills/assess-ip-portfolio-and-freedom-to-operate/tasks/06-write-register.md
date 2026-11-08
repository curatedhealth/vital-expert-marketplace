Input:    outputs of tasks 01 to 05, buyer mode, unit
Atom:     compose-draft (templates/exclusivity-register.md)
Tool:     python3 scripts/validate_register.py register.json
Template: templates/exclusivity-register.md
Output:   exclusivity register, answer first: the effective dates per market, the biggest open question for counsel, what each puts at risk, options to close each gap with effort and risk
Check:    validate_register.py exit 0; reviewer UNSIGNED until named; BD view (deal terms: milestones tied to extension grants, license consents, price protection) or investor view (runway to the first loss of exclusivity); options only. Rule: the decision belongs to the team; the opinion belongs to counsel
Human:    the named patent counsel (or named IP reviewer) decides; the skill states no opinion
