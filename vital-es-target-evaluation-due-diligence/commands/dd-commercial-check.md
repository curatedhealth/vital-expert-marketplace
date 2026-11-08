---
command: /dd-commercial-check
args: [asset, indication, buyer_mode (bd|investor), unit (asset|company), markets (US|EU|both)]
---
Run intake for evaluate-market-opportunity-and-competitive-position and build the market register (population with
source, year and geography; competitors with dated sources; differentiation tied to the clinical evidence register and
the mechanism register). When the market register is signed, run intake for determine-commercial-viability: the analog
range and the option set GO, CONDITIONAL GO and NO-GO. Price, coverage and access come from the Market Access pack and
are a [GAP] until it is Released. The commercial decision is human only. Any market other than US or EU is a [GAP].
