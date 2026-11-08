# Handoff → Ontology Navigator (return packet)

CF-01.02.06 → CF-01.06.01 · UC02 closed loop.  
DD finishes grades; **ON** owns compare-options / board integrity / close. Navigator never values the asset.

**Engagement:** {name} · **Mode:** asset | company · **As of:** {date}  
**Prepared by:** {agent/person} · **Reviewed by:** {name or UNSIGNED} · Status: UNSIGNED

## 1. What ON asked for (from frame)

| Field | Value |
|---|---|
| Decision of intent (one sentence) | |
| Options on the table (include do-nothing / pass / build) | |
| Deal lead / IC owner | |
| ON session / record id (if any) | |

## 2. DD deliverables attached (pointers only)

| Workstream | Register path / tip | Proposed R-STATUS | Deal-lead confirmed? |
|---|---|---|---|
| F MoA | | | Y/N/PENDING |
| A Clinical | | | |
| B Dev risk / timeline | | | |
| C IP / exclusivity | | | |
| D Regulatory / legal | | | |
| E Finance / tax flags | | | |
| G Market / competitive | | | |
| R Revenue / price ranges | | | |
| H Commercial viability options | | | |
| IR Integrated report | | | |

## 3. Graded claims / unverified list (for ON `handoff-verify`)

| # | Claim (plain) | Support (rule/VP/[CHECK]) | Grade posture | Next |
|---|---|---|---|---|
| 1 | | | supported / partial / unverifiable / refused | |

Paste companion gap list from `templates/gap-list.md` if long.

## 4. Conflicts DD will not reconcile (for ON compare)

| ID | Left | Right | Why ON must see both |
|---|---|---|---|
| R-CONF-* | | | |

## 5. Decision options DD assembled (none recommended)

| Option | Conditions / blockers | `recommended` |
|---|---|---|
| Sign | | `recommended=false` / **false** |
| Sign with conditions | | **false** |
| Do not sign | | **false** |

Deal lead may have recorded a human decision separately — copy here only if signed.

## 6. What ON should do next

1. `handoff-verify` (or explicit not-tool-checked) on graded claims  
2. `compare-options` using people-entered scores — DD ranges are **V inputs**, not scores  
3. Integrity path → `compile-board-pack` / `close-the-decision`  
4. Do **not** invent rNPV / deal value inside ON or DD (valuation sibling if needed)

## 7. Standing refuses carried into ON

- No FTO / tax / QoE opinion from either plugin alone  
- ASC / FC-* / Full / Marketplace Done not claimed by this packet  
- Teaching figures from `examples/` never copied into live IC packs  

## Check-line

```bash
python3 tools/stamp_check_line.py --skill handoff-to-navigator --mode assemble --extra "return-packet"
```
