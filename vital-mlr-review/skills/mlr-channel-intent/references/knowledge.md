    # Knowledge — MLR channel intent

    Migrated patterns for this skill. Teaching shapes are not evidence.

    ## Product law
    Host-reasoner. Tools are structural. Humans approve.

    ## Skill focus
    This skill should be used when classifying whether material is promotional, scientific exchange, or medical information before MLR chairs run. It gates ruleset choice and never approves.

    ## Failure modes to watch
    - FM-CH1 proactive off-label labeled scientific exchange
- FM-CH2 inventing unsolicited request
- FM-CH3 US-default when channel unclear

## World-class depth notes (8 November 2026)
- Declared channel loses to artefact signals when they conflict.
- Unsolicited MI request records are evidence; absence is [GAP], not "probably fine."
- Mixed channel pieces — promotional and medical-information content in one piece (for example branded claims plus MI letter fragments), or any content that supports more than one channel/intent reading — are `human_gate_required`, with the conflicting elements quoted (TEH-RDY-061). A piece whose intent was simply not declared is not mixed: when its supplied content carries one reading, it gets a provisional decision (`provisional: treat as promotional — pending: …`, `findings_only`; TEH-RDY-062); when the content is incomplete and carries no reading, it is a missing input (TEH-RDY-058).
- Intent (promo / scientific exchange / med info) is what binds a rule pack; the delivery medium (email, print, congress, social) is recorded only (TEH-RDY-057).
- Branding + efficacy + ISI footer strongly suggests promotional posture.

## Operating memory (world-class)
- Status vocabulary is closed: findings_only | revise | human_gate_required | prep_complete.
- Liability line is mandatory on user-facing closes.
- Teaching examples are never live inputs (MLR-H2).
- Offline-first Hybrid B: local CLI before MCP.
- Pilot: no marketplace publish without owner yes.
- Chair isolation: Medical ≠ Legal ≠ Regulatory.
- Markets never silently default to the United States.
- VERIFY overlap ≠ clearance; stamp discipline via stamp_ready_line.py.

### Skill-specific memory — mlr-channel-intent
Own the job in SKILL.md boundaries; refuse out-of-scope themes; stamp every close.
