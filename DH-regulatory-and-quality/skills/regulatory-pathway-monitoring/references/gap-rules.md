# Gap rules

A gap is information, not an apology. The person needs to know why something is missing, because each reason leads to a different next step.

| Class | When | How to word it | Next step |
|---|---|---|---|
| Found | The library holds the record or event. | State it with source and retrieval date. | None. |
| Field missing | The record exists but a field is empty (every EU decision date; recall number; safety count "not assessable"). | "CE marked as class IIa per EUDAMED (retrieved 14 October 2026); no decision date is stored `[GAP]`." | Check the register page. |
| Log not started | `get_register_deltas` returns "no watch is registered for this scope". | "The library's change log for QVO has not started (no watch set); this says nothing about the market. Compared with your saved snapshot of DATE instead." | Compare snapshots; the person may choose to set a watch. |
| Loaded, nothing found | The source is loaded but holds no row for this product. | "No recall in the library's copy of FDA enforcement records for this product (892 US safety events loaded, 19 October 2026)." | Check the regulator's database before concluding. |
| Not loaded | UK registrations, Swiss devices and actions, EU vigilance. | "The library holds no Swiss field safety actions: not loaded in this release." | Check the regulator. |

## Never

- Never turn an empty change log into "no change", an absent recall into "no safety issues", or absence from the EU copy into "not CE marked".
- Never infer a cause, a class or an outcome for a device from a record. Describe it by what its record states.
- Never attribute a product-code count to one product.
- Never fill a rule from memory: a rule not in a research row is `[GAP]` with the reason.
