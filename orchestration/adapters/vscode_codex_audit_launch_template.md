# VS Code + Codex Audit Launch Template

Use this template only for bounded audit / consistency-review / no-change-verification tasks.

---

Read and follow only the minimum orchestration spine required for this task.

Required reading order:
1. `docs/README.md`
2. `docs/HANDOFF_CONTRACT.md`
3. `docs/ACTIVATION_MATRIX.md`
4. `orchestration/README.md`
5. `orchestration/router/README.md`
6. `orchestration/router/TASK_CLASS_DEFAULTS.md`
7. `orchestration/profiles/README.md`
8. `orchestration/modules/README.md`
9. `orchestration/modules/ACTIVATION_MATRIX.md`
10. `orchestration/modules/TRIGGER_MATRIX.md`

Load no skill files unless their modules are actually activated.

Task packet:
- Objective: <fill>
- Requested outcome: bounded audit / consistency review / no-change verification
- Best current problem locus: <fill>
- Task surface type: <docs | code | unknown>

Classification rule for this template:
- If implementation is not authorized at the start, do **not** classify the task as:
  - `narrow_bugfix`
  - `local_fix_with_adjacent_risk`
  - `bounded_multi_file_patch`
  - `regression_sensitive_change`
  - `security_sensitive_change`
  - `justified_local_hardening`
- Prefer:
  - `bounded_consistency_audit` when the main goal is bounded truth/alignment review
  - `no_change_verification` when the main goal is to confirm that no patch is needed unless verification fails

Implementation is not authorized in this step unless the audit itself proves a specific bounded inconsistency that justifies reclassification.

Before any implementation, output only:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

Rules:
- `execution` must remain blocked at audit start.
- Do not scan the repo broadly by default.
- Do not widen scope because a cleaner design is imaginable.
- Do not silently reframe an audit as a fix task.
