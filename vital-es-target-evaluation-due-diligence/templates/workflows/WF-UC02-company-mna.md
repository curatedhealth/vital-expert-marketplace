# WF-UC02-C — Company M&A roll-up

Same spine as WF-UC02-A, with **per-pipeline-asset** DD runs then company roll-up.

| Extra vs asset mode | Detail |
|---|---|
| Intake | Mode = company; list assets in scope |
| E finance | Filed 10-K/10-Q liquidity + license exhibits (person-read) |
| IR | Roll-up table across assets (IR § company mode) — never merge dates across assets |
| Return packet | One packet + per-asset annex pointers |

Do not invent consolidated PoS or EU-wide price.
