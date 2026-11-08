# ON ↔ DD use-case examples

Teaching packs only (evidence class **H**). Never copy figures into a live IC pack.  
Pair with Ontology Navigator `examples/due-diligence-handoff/` (outbound) and DD `templates/handoff-to-navigator-return-packet.md` (inbound).

## Series

| Example | Workflow | Shape | Runnable depth |
|---|---|---|---|
| `UC02-asset-acquisition-aurora-x/` | WF-UC02-A | Top-down | Full step walk + goldens stubs |
| `UC02-company-roll-up/` | WF-UC02-C | Top-down | Route + intake + return |
| `UC02-in-license/` | WF-UC02-L | Top-down | Route + emphasis + return |
| `UC02-partner-option/` | WF-UC02-P | Top-down | Route + emphasis + return |
| `bridge-UC06-portfolio-keep-kill/` | WF-BR-06 | Middle-out | Scoped DD bridge |
| `bridge-UC08-evidence-access/` | WF-BR-08 | Bottom-up | Clinical/reg bridge |

Also see sibling `../fictional-asset-diligence/` (DD-only spine without ON return).

## How to run (operator)

1. Open ON → follow outbound handoff (do not value asset).  
2. Open DD → `/dd-start` → matching example steps.  
3. Fill return packet → back to ON `handoff-verify` / `compare-options` / close.  
4. `bash scripts/run_craft_ci.sh` before sharing prose.

## Honesty

ASC / FC-* / Full Accepted Deferred. Studio Marketplace Done not claimed. Eng smoke ≠ independent Standard Pass.
