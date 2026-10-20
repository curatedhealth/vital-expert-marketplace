# Gap rules

A gap is information. The person needs to know why something is missing, because each reason leads to a different next step.

## Rules and requirements

| Situation | How to word it | Next step |
|---|---|---|
| A rule is in a CV or CVB row | State it with the row id and whether it is law, guidance or a recommendation paper. | None. |
| The rule exists in a source the research did not read (ISO 14155, EU MDR investigation rules, EMA computerized systems guideline, FDA adoption of Annex 2, EU national provisions appendix content) | "Not sourced in this skill `[GAP]`: the device GCP standard ISO 14155 was not read." | The owner the person names for that source checks it, or owner not named. |
| The person asks for a threshold the sources do not set (wear time, completeness, accuracy, usability pass rate) | "No source here sets this; it is your acceptance criterion." Offer a "proposed" value only if they ask, with the fact behind it. | The person decides. |
| A rule applies to a different product type (E6(R3) for a device, EU CTR for a device) | "E6(R3) names drugs and biologics, not devices (CV4)." | Point to the device rules gap. |

## The person's documents

| Situation | How to word it |
|---|---|
| An element has no document behind it | "Stated, evidence not seen." Never "met". |
| A field in the capture inventory is blank | "Not recorded `[GAP]`", and name what would fill it (validation summary, data flow diagram, vendor audit-trail setting). |
| Two documents disagree (for example protocol and data management plan on source location) | Quote both and ask which is current. |

## Connector results

| Situation | How to word it |
|---|---|
| `find_trial` finds no registration for a paper | "No registration linked from this paper in the library's sources." Never "unregistered". |
| `search_literature` finds no comparable trial | "None found in pubmed, europepmc, openalex, crossref (searched DATE)." Never "no one has done this". |
| Verify returns "unverifiable" for a regulator page | The register item C1 limit; cite the research row instead. |

## Never

- Never turn a gap into "compliant", "validated", "not required" or "fails".
- Never mark a field `[GAP]` from an abstract when the source is open access: read the full text first.
- Never fill a gap from memory or from a passage without a source URL.
