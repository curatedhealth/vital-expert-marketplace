# Gap rules

A gap is information, not an apology. The person needs to know why something is missing, because each reason leads to a different next step.

## Kinds of gap in this competency

| Class | When | How to word it | Next step for the person |
|---|---|---|---|
| Person's decision not yet made | A role, the value unit, a corridor end, a threshold, an outcome or an audience the person has not given | "Value unit: not chosen yet `[GAP]`." | Ask once; never fill it with a proposal unless asked, then label it "proposed". |
| Library field missing | A record exists but a field is empty (price unit, prescription period, end date, manufacturer versus negotiated amount) | "Registered price 224.99 EUR; unit and prescription period not stated `[GAP]`." | Check the authority's page (for DiGA, the directory entry, DE20). |
| Scheme loaded, product not found | The scheme holds listings (`listing_count` above 0) but none for this product | "Not in the library's copy of DE_DIGA (82 listings, loaded 15 October 2026)." | Check the authority before concluding. |
| Not covered by the library | The scheme or source holds nothing (`listing_count` 0, posture `gap`) | "The library holds no listings for FR_LPPR: REASON." | The library cannot answer; check the authority. |
| Not sourced | A rule the research files do not hold | "The amended UCPD wording is not sourced here `[GAP]`." | Name the authority or text to read; do not fill from memory. |
| Tool failed | HTTP 422 or 503 | "Budget impact tool unavailable (HTTP 422, 19 October 2026); arithmetic shown in the conversation." | Run the arithmetic on the person's numbers, labeled hypothesis. |

## Never

- Never turn a missing listing into "not reimbursed" or "no price".
- Never fill a missing price, unit, threshold or evidence passage from memory.
- Never treat the `get_pricing_corridor` spread as a corridor.
