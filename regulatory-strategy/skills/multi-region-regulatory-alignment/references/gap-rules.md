# Gap rules

A gap is information. The person needs to know why something is missing, because each reason leads to a different next step.

## Authorization facts from the library

| Class | When | How to word it | Next step |
|---|---|---|---|
| Found | `search_devices` returns a record. | Class and pathway as the record states them, identifier, decision date, source, retrieval date. | None. |
| Field missing | The record exists but a field is empty (EU decision date, predicate). | "On the EU market per EUDAMED record ++B720EASPECTSCEGK; the library stores no decision date `[GAP]`." | Check the register entry. |
| Register loaded, product not found | The library holds records for the jurisdiction but none for this product. | "Not in the library's copy of EUDAMED software records (3,142 records, loaded 19 October 2026)." | Check the regulator before concluding. |
| Register loaded, not searchable | The library lists the register but the search tool cannot reach it (Canada). | "The library holds Health Canada MDALL rows but cannot search them by product." | Check MDALL. |
| Register not loaded | The library holds no records for the jurisdiction (GB registration, Switzerland, Australia, Brazil, Japan). | "The library holds no device registrations for this region." | The library cannot answer; check the regulator. |

`get_market_status` "false" is never worded as "not authorized". Restate it with the classes above.

## Rules and routes

| Situation | How to word it |
|---|---|
| No research row sources the rule | "`[GAP]`: not in the sourced references", and name the regulator page to check. Never fill it from memory. |
| The route is a draft, proposal or exploratory | Name the status and the instrument: "UK reliance route: draft statutory instrument (MR-26, MR-27); not available today." |
| Sources disagree | Quote both with their dates and say which is law (for example Health Canada MDSAP: the regulation versus the MDSAP site). |
| Guidance was superseded | Name the current version and date (for example CDS guidance of 29 January 2026). |
| A passage from `retrieve_guidance` has no source URL | Do not cite it. Say the library holds the document without provenance. |

## The person's own facts

| Situation | How to word it |
|---|---|
| Intended purpose not given | Classification stays open: "class depends on intended purpose `[GAP]`". |
| Evidence the person holds is not described | "Not described `[GAP]`"; ask what studies exist, where they ran, and under which GCP basis. |
| Owner not named | "owner not named"; ask. Never suggest a job title. |

## Never

- Never turn a gap into "not authorized", "not accepted" or "not required".
- Never infer a class, pathway or outcome from a product's name, a related record or a competitor.
