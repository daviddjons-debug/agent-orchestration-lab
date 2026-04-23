# VS Code + Codex Launch Template

Use this as the bounded launch packet for a new task in VS Code with Codex.

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
- Task surface type: <code | docs | browser_ui | security | packaging | unknown>

Before implementation, output only:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

Rules:
- Do not begin implementation before bounded routing is stated.
- Do not scan the repo broadly by default.
- Do not widen scope because a cleaner design is imaginable.
- Do not activate browser verification without a real UI/browser surface.
- Do not activate security without a real trust-boundary/security dimension.
- Do not activate second opinion without contradiction or retriage pressure.
- Do not activate release packaging without explicit delivery/handoff output requirements.

If implementation is justified after routing, stay inside the minimum sufficient change contour.

Completion output must state:
- objective achieved: yes / partial / no
- patch stayed bounded: yes / no
- adjacent or verify-only surfaces checked when required: yes / partial / no
- behavior evidence produced when required: yes / partial / no / not required
- retriage or escalation still needed: yes / no
