# Medical chair — industry standards by market (v0.3)

Authoritative names the medical skill must respect. Full checklists and URLs live in
`mlr_get_ruleset` packs (`mcps/mlr_review/rulesets/`). Date-read on packs: 24 October 2026.
Stubs (FR, JP, CA, AU, BR) list authority hints only — mark `[GAP]`, never substitute another market’s pack.

| Market | Medical-facing instruments (primary) | What medical reviews against |
|---|---|---|
| **global** | Cross-cutting hygiene (no invented figures; benefit–risk balance) | Supplied label/authorized-use text + cited study materials |
| **US** | FDA medical-product communications consistent with FDA-required labeling (guidance); 21 CFR Part 202 fair-balance expectations for Rx advertising | US Prescribing Information / FDA-required labeling |
| **EU** | Directive 2001/83/EC Title VIII (advertising of authorized medicines / essential information); EFPIA Code clinical/claim norms | Supplied SmPC for markets in scope |
| **UK** | ABPI Code (claims consistent with SmPC); MHRA Blue Guide (clinical promotional expectations) | UK SmPC |
| **DE** | HWG + AMG advertising-related limits; FSA Code clinical advertising norms | German Fachinformation / SmPC |
| **CH** | Swissmedic advertising guidance; TPA/HMG advertising frame; Pharma Code | Swiss product information supplied by user |
| **FR / JP / CA / AU / BR** | Stub authority hints only in registry | Do not invent national medical rules; `[GAP]` + company SOP |

## Practice rules (medical)

1. **Label first.** No PI/SmPC/FI for a market → medical finding is `[GAP]`, not a recalled label.
2. **Per-market authorized use.** US PI is not a substitute for EU SmPC or DE Fachinformation.
3. **Fair balance is clinical.** Benefit claims without material risks from the supplied label are medical findings; burying risks in layout may also be regulatory — flag medical severity and point Regulatory at format.
4. **Superiority needs basis.** Comparative clinical claims without adequate supplied evidence → medical finding; legal owns disparagement/comparative-ad risk separately.
5. **Company medical SOP wins** when it is stricter; name it when supplied.

## Tool companions

- `mlr_align_claims` — structural claim vs authorized-use labels (heuristic, not clearance).
- `mlr-verify-handoff` — when a clinical citation must be admitted against a passage (`vvfy_`).
