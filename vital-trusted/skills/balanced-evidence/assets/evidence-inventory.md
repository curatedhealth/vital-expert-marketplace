# Output format: evidence inventory

Filled from the supplied material only, before drafting or repairing. Every field not in
the material is `[GAP: not supplied]`, never inferred. For anything leaving the company,
the inventory is shown in the balance note; for internal work, it stays as working.

Plain words throughout, so it can be shown to the person (TR-H13).

```
Evidence in your material, and where it is in the draft

Material: <one line per item supplied, with its kind, e.g. "ZELORA-2 publication (PDF)">

Studies of this product for this use
  <study>   primary result: <as reported, at its planned time point>   in draft: <yes | buried | no | out of stated scope>
  <study>   ...
  Other studies: <none in the material | asked: "are there others?">

Endpoints (per study)
  Primary:    <endpoint, time point, result>                  in draft: <yes | buried | no>
  Secondary:  <endpoint, result> ...                          in draft: <yes | no | out of stated scope>

Time points reported
  <planned time point> ... <others>                           in draft: <which>

Subgroups and analysis sets
  <subgroup, planned or unplanned, result>                    in draft: <yes, labeled | yes, unlabeled | no>
  Analysis set used in the draft: <everyone randomized | completers | responders | other>

Side effects and discontinuations
  Serious adverse events: <each group>                        in draft: <yes | footnote only | no>
  Most common side effects: <as the source lists, each group> in draft: <...>
  Stopped because of side effects: <each group>               in draft: <...>
  Stopped for any reason: <each group>                        in draft: <...>
  Warnings the label or study puts first: <as listed>         in draft: <...>

Limitations the source states
  <one line each>                                             in draft: <yes | no>

Scope of the draft as stated: <the stated scope | not stated>
```
