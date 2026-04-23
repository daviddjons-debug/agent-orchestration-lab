# Documentation Map

## Operational core
These are the live operational documents for current runtime behavior and bounded orchestration discipline.

1. `docs/HANDOFF_CONTRACT.md` — canonical handoff / field semantics
2. `docs/ACTIVATION_MATRIX.md` — canonical profile activation and escalation logic
3. `docs/EXECUTION_PROFILES.md` — compact profile summary / compatibility layer derived from the activation matrix
4. `docs/BASELINE.md` — current bounded runtime proof boundary
5. `docs/VALIDATION_MATRIX.md` — validation-case coverage and status
6. `docs/agent_pack_v2_rule_extraction.md` — extracted architecture rules from observed bounded validation behavior
7. `docs/NEXT_EXPERIMENT.md` — current next-step target, if still active

## Portable / design layer
These documents describe the portable-pack direction and attachment model.
They are important, but they are not the first stop when validating current runtime truth.

1. `docs/PORTABLE_PACK_BLUEPRINT.md` — portable pack design blueprint
2. `docs/PORTABLE_PACK_LAYOUT.md` — canonical portable pack layout
3. `docs/PROJECT_OVERLAY_MINIMUM.md` — minimum required project-local overlay
4. `docs/VSCODE_ADAPTER_BLUEPRINT.md` — VS Code attachment model
5. `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md` — Antigravity attachment model
6. `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md` — shared bounded current-task attachment template
7. `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md` — canonical bootstrap order for new projects
8. `docs/PORTABLE_MODE_CANON.md` — operator-facing portable-mode canon
9. `docs/PORTABLE_MODE_CHECKLIST.md` — compact operator checklist for portable-mode attachment

## Supporting directories
- `docs/roles/` — role-level behavior docs aligned to the canonical contract
- `docs/validation_cases/` — per-case runtime binding / evidence docs
- `orchestration/` — current portable/operator-facing orchestration surface
- `orchestration/router/` — task classification and default path selection layer
- `orchestration/profiles/` — operator-facing execution-profile surface
- `orchestration/modules/` — functional module layer, activation matrix, and trigger matrix
- `orchestration/skills/` — narrow module-attached operational playbooks
- `orchestration/overlays/project/` — project-local overlay surface for scope, constraints, forbidden zones, and validation targets
- `orchestration/adapters/` — thin adapter-side operational artifacts

## Evidence / archive layers
- `docs/session_recaps/` — session-level historical recap layer
- `docs/baseline_v1/` — preserved older baseline role pack / reference layer
- `docs/codex_eval/` — raw external evaluation artifacts; not a canonical policy/contract layer
- `docs/runs/` — generated run artifacts; archival evidence only, not editable source-of-truth docs

## Reading order

### For current runtime truth
1. `docs/README.md`
2. `docs/HANDOFF_CONTRACT.md`
3. `docs/ACTIVATION_MATRIX.md`
4. `docs/EXECUTION_PROFILES.md`
5. `docs/BASELINE.md`
6. `docs/VALIDATION_MATRIX.md`
7. `docs/agent_pack_v2_rule_extraction.md`

### For portable attachment/design
8. `docs/PORTABLE_PACK_BLUEPRINT.md`
9. `docs/PORTABLE_PACK_LAYOUT.md`
10. `docs/PROJECT_OVERLAY_MINIMUM.md`
11. `docs/VSCODE_ADAPTER_BLUEPRINT.md`
12. `docs/ANTIGRAVITY_ADAPTER_BLUEPRINT.md`
13. `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
14. `docs/NEW_PROJECT_BOOTSTRAP_SEQUENCE.md`
15. `docs/PORTABLE_MODE_CANON.md`
16. `docs/PORTABLE_MODE_CHECKLIST.md`
17. `orchestration/README.md`
18. `orchestration/router/README.md`
19. `orchestration/router/TASK_CLASS_DEFAULTS.md`
20. `orchestration/profiles/README.md`
21. `orchestration/modules/README.md`
22. `orchestration/modules/ACTIVATION_MATRIX.md`
23. `orchestration/modules/TRIGGER_MATRIX.md`
24. `orchestration/skills/README.md`
25. `orchestration/skills/MODULE_TO_SKILL_MAPPING.md`
26. `orchestration/overlays/project/PROJECT_SCOPE.md`
27. `orchestration/overlays/project/PROJECT_CONSTRAINTS.md`
28. `orchestration/overlays/project/PROJECT_FORBIDDEN_ZONES.md`
29. `orchestration/overlays/project/PROJECT_VALIDATION_TARGETS.md`
30. `orchestration/adapters/vscode_codex_bounded_invocation.md`
31. `orchestration/adapters/vscode_codex_launch_template.md`
32. `orchestration/adapters/vscode_codex_audit_launch_template.md`
33. `orchestration/adapters/vscode.md`
34. `orchestration/adapters/vscode_usage.md`
35. `orchestration/adapters/vscode_verification.md`
36. `orchestration/adapters/vscode_live_verification_checklist.md`
37. `orchestration/tasks/vscode_bounded_task_example.md`

### Read only when needed
- `docs/roles/`
- `docs/validation_cases/`
- `docs/session_recaps/`
- `docs/codex_eval/` only when reviewing raw external evaluator evidence
