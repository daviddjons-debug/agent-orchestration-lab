# VS Code + Codex Browser/UI Launch Template

Use this template only for bounded browser/UI tasks where visible client-side behavior is part of completion.

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
- Symptom / requested outcome: <fill>
- Best current problem locus: <fill>
- Task surface type: browser_ui

Classification guidance:
- Prefer a fix class only if implementation is actually authorized.
- If browser-visible behavior must be checked before any repair claim, keep the path bounded and require browser verification explicitly.
- Do not treat “UI task” as permission for broad visual cleanup.

Before implementation, output only:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

Browser/UI rules:
- Activate `browser_verification` only when a real visible UI/browser surface is part of acceptance.
- Do not activate `browser_verification` for non-UI tasks.
- Do not widen from a visible symptom to broad page redesign.
- Do not claim success from static reasoning alone when the requested outcome is browser-visible.

If implementation is justified after routing, completion output must also state:
- whether visible browser behavior was actually checked
- what exact UI surface was checked
- whether the browser-visible symptom is resolved
