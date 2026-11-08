# DD hooks — routing + optional Claude Code lifecycle

Craft deepen 8 November 2026 (world-class plugin wave). Pattern mirrors READY (`vital-mlr-review/hooks`) and Anthropic plugin components docs.

## Two hook layers (do not collapse)

| File | Host | Job |
|---|---|---|
| `hooks.json` | Cowork / Agent Skills | **Skill-routing** — phrase → skill; refuse phrases → hard stop |
| `claude-code-hooks.json` | Claude Code (optional) | **Lifecycle** — Stop runs `preflight_refuse_scan.py` |

Guardrails that must hold every time belong in hooks / scripts, not only in facilitation prose (Anthropic: hooks = deterministic; skills = judgment).

## Routing table (`hooks.json`)

| Hook id | Route |
|---|---|
| `H-dd-intake` / `H-dd-report` / `H-dd-return-on` | capability-map (intake, IR, return packet to ON) |
| `H-dd-science` … `H-dd-viability` | Skills F / A / B / C / D / E / G / R / H |
| `H-dd-refuse` | Refuse — deal approve, FTO opinion, ASC/FC enable, Marketplace Done, self-Pass |

## Standing refuses (also enforced by `scripts/preflight_refuse_scan.py`)

- AI recommends sign / GO–NO-GO as the decision
- FTO / clearance / legal opinion from the plugin alone
- Enabling ASC 205-40 or FC-* defaults without owner + primary
- Claiming Studio Marketplace Done or Standard Pass without independent grade
- Inventing COI clearances

## Not claimed

Hooks do **not** make the plugin ON-complete, Full Done, or Marketplace Done.
