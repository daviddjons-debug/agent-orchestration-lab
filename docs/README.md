# Documentation Map

## Canonical top-level documents
1. `docs/HANDOFF_CONTRACT.md` — canonical handoff / field semantics
2. `docs/ACTIVATION_MATRIX.md` — profile activation and escalation logic
3. `docs/EXECUTION_PROFILES.md` — profile summary / compatibility layer
4. `docs/BASELINE.md` — current bounded runtime proof boundary
5. `docs/VALIDATION_MATRIX.md` — validation-case coverage and status
6. `docs/UNIFIED_HANDOFF_CONTRACT_CANON_V4.md` — unified canon snapshot
7. `docs/agent_pack_v2_rule_extraction.md` — extracted architecture rules from observed bounded validation behavior
8. `docs/PORTABLE_PACK_BLUEPRINT.md` — portable pack design blueprint
9. `docs/PORTABLE_PACK_LAYOUT.md` — canonical portable pack layout
10. `docs/PROJECT_OVERLAY_MINIMUM.md` — minimum required project-local overlay
11. `docs/VSCODE_ADAPTER_BLUEPRINT.md` — VS Code attachment model
12. `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md` — Antigravity attachment model
13. `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md` — shared bounded current-task attachment template
14. `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md` — canonical bootstrap order for new projects
15. `docs/PORTABLE_MODE_CANON.md` — single operator-facing portable-mode canon
16. `docs/PORTABLE_MODE_CHECKLIST.md` — compact operator checklist for portable-mode attachment
17. `docs/NEXT_EXPERIMENT.md` — current next-step target, if still active

## Supporting directories
- `docs/roles/` — role-level behavior docs aligned to the canonical contract
- `docs/validation_cases/` — per-case runtime binding / evidence docs
- `docs/session_recaps/` — session-level historical recap layer
- `docs/baseline_v1/` — preserved older baseline role pack / reference layer
- `orchestration/` — first minimal operational portable-pack skeleton; not a full migrated core or implemented adapter layer
- `orchestration/adapters/` — thin adapter-side operational artifacts when materialized

## Evidence layers
- `docs/codex_eval/` — raw external evaluation artifacts; not a canonical policy/contract layer
- `docs/runs/` — generated run artifacts; archival evidence only, not editable source-of-truth docs

## Reading order
For current architecture/runtime understanding, start with:
1. `docs/README.md`
2. `docs/HANDOFF_CONTRACT.md`
3. `docs/ACTIVATION_MATRIX.md`
4. `docs/BASELINE.md`
5. `docs/VALIDATION_MATRIX.md`
6. `docs/agent_pack_v2_rule_extraction.md`

For portable-pack attachment/design understanding, then read:
7. `docs/PORTABLE_PACK_BLUEPRINT.md`
8. `docs/PORTABLE_PACK_LAYOUT.md`
9. `docs/PROJECT_OVERLAY_MINIMUM.md`
10. `docs/VSCODE_ADAPTER_BLUEPRINT.md`
11. `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md`
12. `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
13. `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md`
14. `docs/PORTABLE_MODE_CANON.md`
15. `docs/PORTABLE_MODE_CHECKLIST.md`
16. `orchestration/README.md`
17. `orchestration/adapters/vscode.md`
18. `orchestration/adapters/vscode_usage.md`
19. `orchestration/adapters/vscode_verification.md`
20. `orchestration/tasks/vscode_bounded_task_example.md`

Then read supporting material as needed:
- `docs/roles/`
- `docs/validation_cases/`
- `docs/session_recaps/`
- `docs/codex_eval/` only when reviewing raw external evaluator evidence
