---
name: handoff-from-navigator
description: Accept Navigator handoff packets into Curator steward skills; keep vont_ path clean.
---

# Handoff from Navigator

Navigator Outcome skills must not run Curator stewards inline. They call **handoff-to-curator** and stop.

Here: open the steward packet, then `classify-incoming` → `file-and-process` → `steward-decide` as needed with `vcur_`.
