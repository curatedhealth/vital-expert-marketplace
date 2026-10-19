# Library tools used by this competency

Connector: VITAL Digital Health Library, `https://mcp.vital.expert/api/mcp/library`. Names below are the library's; your assistant may prefix them (for example `regulatory-dh_get_authorization`). Counted calls draw on the library key's monthly allowance; free calls do not. Behavior below was observed in live calls on 19 October 2026; trimmed outputs are in `examples/live/`.

This competency is mostly a method pack. The regulatory rules come from `references/`, not from the library: the library's guidance store returned nothing on the QMSR, FDA's software-change guidance or MDCG 2020-3 (see `retrieve_guidance`).

## regulatory-dh.list_jurisdictions (free)

- No arguments. Returns per jurisdiction: authorization count, safety-event count, last load, sources.
- Observed: US 1,226 authorizations and 892 safety events (openFDA, loaded 19 October 2026); EU 3,142 EUDAMED software devices with the decision date empty on all 3,142; UK safety alerts only (10), no registrations; CH nothing loaded.
- Use it first in A2 to say what the library can and cannot show for the person's markets.

## regulatory-dh.search_devices (counted)

- Required: `query` (product or manufacturer, 3+ characters). Optional: `jurisdiction`, `limit`, `software_only`.
- Pitfall: a full product name can miss. "Dexcom G7" returned nothing in US; "Dexcom" returned two rows (Dexcom Smart Basal, K252818; a 2014 De Novo). Search by manufacturer, then read the rows.
- Absence is a gap in the store, not evidence that a device is unauthorized.

## regulatory-dh.get_authorization (counted)

- Required: `reference` (K, DEN or P number; Basic UDI-DI; or SRN plus trade name).
- Returns pathway, class, status, decision and submission dates, product code, regulation number, predicate references, source URL and retrieval date.
- Use it in A2 to fix the comparison baseline: the most recently cleared device (QX18, QX33). Example: K252818, Dexcom Smart Basal, 510(k), class 2, decided 18 November 2025, product code QRX, predicate K222888; K222888 is the BlueStar CGM insulin dose calculator (Welldoc), decided 11 August 2023.
- Gap: no field says whether a PCCP was authorized with the clearance. Ask the person and cite their authorization letter. Logged in the build notes.
- Describe a device only by what its record states. Do not infer what changed between a device and its predicate.

## regulatory-dh.search_safety_events (counted)

- Needs at least one of `manufacturer`, `product`, `product_code`; `jurisdiction` alone returns "give manufacturer, product or product_code".
- Returns FDA recalls whose product text mentions software, algorithm, application, firmware or app, with event date, class, manufacturer, summary; plus MAUDE report counts by year.
- Pitfalls seen:
  - Rows carry no product code, so a `product_code` filter cannot be confirmed from the row. `product_code: "QRX"` returned Dexcom CGM app and Omnipod 5 recalls.
  - The software filter matches title text: a Dexcom sensor-theft recall matched because its title says "Software Version: N/A".
  - `product_code: "LLZ"` returned nothing, while `product: "software"` returned PACS software recalls.
  - `maude_counts` can list product codes unrelated to the returned recalls; MAUDE counts are reports, not confirmed events.
  - `source_url` is the openFDA API endpoint, not the recall record. Cite the recall by firm, product, version and event date, and tell the person to confirm it in FDA's recall database.
- Use it in A2 for context on how comparable software changes failed in the field. Never as evidence about the person's change.

## regulatory-dh.retrieve_guidance (counted)

- Observed: no passage for the 2017 software-change guidance, the QMSR, or MDCG 2020-3. "predetermined change control plan" returned four Health Canada passages, each with `source_url` "[GAP]" and no retrieval date.
- Do not cite a passage without a source URL. Use `references/` instead.

## regulatory-dh.get_deltas (counted)

- Requires `since`. Without a registered watch it returns "the change log has not started". This competency does not register watches, so it does not use this tool.

## verify.build_record (counted)

- Needs a named human in `cleared_by.name`. Observed: `cleared_by: {name: "Claude"}` is refused ("build_record refuses a record without a human cleared_by.name").
- Use it only when the change decision record leaves the conversation and the person names who clears it.

## agent-pack.list_experts and download_agent

- `list_experts {query: "quality"}` returns the bound worker `quality-assurance-manager-software` (QA Manager, Software (V&V)) and also `quality-systems-director-software` (Quality & Software Lifecycle Director). Offer the download only if the person asks for the agent.

## Not used here

- `verify.check_claim` on regulatory rules: the rules come from primary rows already quote-checked; Verify can return "supported" on word overlap (register item N3).
- `watch_register`: described only, never called.
