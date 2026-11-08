# C4 connector contract notes (research absorb)

Copied from research export for implementers. Reinspect live tools before writes.

# C4 connector notes — descriptive, not tested adapters

Earlier conversation inspected the exposed tool definitions. Reinspect before implementation; no live write is needed for this research package.

sequence_check: required brief_id, steps (generic object array). Description says it orders depends_on, checks capacity and stores order; cycles/empty list are gaps. Nested full schema unspecified. It is a write, not a purely offline checker.

delegation_place: required brief_id, items (generic object array). Description rejects missing/AI owners and role-only ownership; regulated agent/agent_with_review exceptions need reason and a person's name. Do not assume these choices are DC09/AEM codes or map them silently. No one-to-one crosswalk verified.

trial_note: required brief_id,payload (object). Description lists option_name,outcome,hypothesis,value/cost_to_test low/mid/high/unit/basis; measure name/unit/baseline/baseline_source/target/direction reduce|increase/owner; stop_rule,time_limit,exit_condition,oversight_owner. Appends under 5_execution; declares_success stays false. Description is not a fully enumerated nested schema; verify actual contract before calls. Do not send new proposed fields as if declared.

methods_capability_gap: required capabilities; optional scores,outcome_links,outcome_scores,brief_id. Current/required whole numbers1–10, human supplied. With brief_id only released outcome scores weight gaps; without brief indicative supplied scores. Links are supplied/stored, not inferred. No universal maturity claim or new thresholds.

chain_trace: optional jt_id,vd_id,depth1–8; stored path only; missing capability is a gap.

opportunity_recommend: stage execution groups CF level4 competencies and PH level4 process steps. Retrieved draft is not a human decision or authorization.

A generic read scope does not make writes read-only. Resolve targets and obtain explicit approval for actual writes. No MCP mutation, brief creation, owner assignment or synthetic live test is authorized by this report.
