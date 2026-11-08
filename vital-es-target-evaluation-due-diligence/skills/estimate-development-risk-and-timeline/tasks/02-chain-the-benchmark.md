Input:    start_phase, benchmark_key
Atom:     none
Tool:     python3 scripts/pos_chain.py input.json --pretty (with an empty adjustments list)
Template: none
Output:   benchmark technical, regulatory and overall success from the start phase
Check:    exit 0; the benchmark figure and page are named in the output. Rule: this is the benchmark, not the estimate; show it before any adjustment
Human:    none (script output only)
