Input:    the Market Access pack state and any records (intake item 6); references/market-access-interface.md
Atom:     extract-requirements-from-source
Tool:     scripts/option_set.py (access_inputs block)
Template: none
Output:   the access_interface block: pack name, release state, state GAP or met, and the consequence when it is a GAP
Check:    "met" only if the pack is Released and carries records; otherwise GAP with the consequence "not adjusted for price, coverage or access; the range may be overstated". Rule: price, coverage and access assumptions are never rebuilt here
Human:    the named reviewer with commercial experience reviews the output
