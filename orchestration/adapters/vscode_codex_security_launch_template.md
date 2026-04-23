# VS Code + Codex Security Launch Template

Use this template only for bounded security-sensitive tasks where trust boundaries, permissions, exposure, parsing, secrets, or auth-related logic may matter.

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
11. `orchestration/adapters/external_target_repo_invocation.md`

Load no skill files unless their modules are actually activated.

Task packet:
- Objective: <fill>
- Symptom / requested outcome: <fill>
- Best current problem locus: <fill>
- Task surface type: security

Classification guidance:
- Prefer a security-sensitive class only when there is a real trust-boundary or exposure dimension.
- Do not inflate ordinary code cleanup into a security task.
- Do not use “security” as a ritual excuse for broad scanning.

Before implementation, output only:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

Security rules:
- Activate `security` only when there is a real auth / permission / exposure / secret / parsing / trust-boundary dimension.
- Do not activate `security` for ordinary local fixes with no boundary significance.
- Do not widen from a bounded risk to repo-wide audit without explicit authorization.
- Do not claim “secure now” from plausibility alone.

If implementation is later authorized, completion output must also state:
- what exact security-relevant surface was checked
- whether the bounded change alters trust/exposure behavior
- whether residual risk remains
