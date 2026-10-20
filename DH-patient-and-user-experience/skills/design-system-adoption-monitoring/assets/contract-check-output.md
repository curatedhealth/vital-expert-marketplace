# Output format: contract check

Short mode: 450 words maximum, counted without the calls list and tables' source column. Before handing over, count the words. If over 450, cut in this order until under: context paragraphs, repeated row ids in prose, secondary rules, rows not tied to the person's question. Never cut a gap, a stop or the record line. Refusals follow the same 450-word cap.

## Short mode (default for a direct question)

1. **Answer:** breach or no breach found on what was checked; the one or two breaches that matter most (clinical and device first); what could not be checked.
2. **Frame:** component, contract version (or "type criteria only"), surface, version on the surface, surface type.
3. **Checks (compact):** Item (state, criterion, never-invent, allowed surface) · Row · Observed · Evidence: seen / described / none · Result: met on evidence / breach / not checked.
4. **Breaches:** facts only, each with contract item, row and evidence.
5. **Open questions (at most three):** the evidence that would close the most "not checked" items first.
6. **Record:** "Check of one surface against one contract, limited to what was supplied. Not a conformance assessment. Clears: the person you name. Record built with verify.build_record once they clear it; until then, uncleared draft. AI-assisted."
7. One line offering the full version.

## Full mode

### Answer

### Frame
| Item | Value |
|---|---|
| Component | |
| Contract version | |
| Surface | |
| Component version on surface | |
| Surface type (clinical, patient-facing, marketing, device UI) | |

### Allowed surface
| Contract says | Surface | Result |
|---|---|---|

### States
| State | In contract | On surface | Result |
|---|---|---|---|

### Criteria
| Criterion (number, name) | Row | Observed | Evidence (what, date, tool) | Result |
|---|---|---|---|---|

### Never-invent content
| Content shown | Source as you describe it | Contract says | Result |
|---|---|---|---|

### Breaches and concerns
| # | Breach (fact) | Contract item and row | Evidence | Concern type (if you classify) |
|---|---|---|---|---|

### Not checked
Items without a measurement or a view of the surface.

### Record
No statement that the surface or product is accessible or conformant. AI-assisted. Clears: NAME (the person you name). The record is built with `verify.build_record` once NAME clears it; until then it reads "uncleared draft".
