---
command: /dd-clinical-risk-check
args: [asset, indication, buyer_mode (bd|investor), unit (asset|company), markets (US|EU|both)]
---
Run intake for assess-scientific-validity-and-moa and build the mechanism register (the scientific go/no-go stays with a named scientist); when it is signed, or the buyer waives it, run intake for review-clinical-data-quality. When the evidence register exists and is signed off by a
named reviewer, run estimate-development-risk-and-timeline. Otherwise stop at the register. Any market
other than US or EU is a [GAP].
