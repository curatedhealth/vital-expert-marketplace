# Tool calls

## extract_claims

Arguments: the submitted text.

Returns: claims with offsets, kind, entities, and cited markers. It does not return a status.

Pitfall: do not send a cleaned copy. Offsets are into the text the person submitted.

Schema source: Verify connector, 19 October 2026.
