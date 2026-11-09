# Label document by market (lookup, TEH-RDY-038)

Use this lookup to name a market's authorized labeling document on a market-scoped line (label basis, authorized-use bind, `[GAP]` for missing label text). Take the row for each market the person supplied, and only those rows. Never copy this table's market list into an answer, never name another market's document, and never write an "X or Y" list of document names on one line.

Source of the names: the "What medical reviews against" column of `../skills/mlr-medical-chair/references/standards-by-market.md` (no other name is added here).

| Market | Label document name to use |
|---|---|
| DE | Fachinformation |
| CH | Swiss product information |
| UK | SmPC |
| EU | SmPC |
| US | Prescribing Information |
| Any other market, or `global` | authorized labeling for `<market>` |

Line shape: `<market>: <document name> supplied` or `<market>: [GAP] <document name> not supplied`. Example shape only — the market and name come from the person's supplied list and this lookup.
