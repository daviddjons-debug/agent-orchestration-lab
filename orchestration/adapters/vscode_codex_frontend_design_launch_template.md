# VS Code + Codex Frontend Design Launch Template

Use this template only for bounded frontend design tasks where visual quality, interface polish, redesign, or design critique is materially part of the task.

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
- Task surface type: frontend_design
- design_mode: <audit | polish | redesign>
- design_variance: <low | medium | high>
- motion_intensity: <low | medium | high>
- visual_density: <low | medium | high>

Classification guidance:
- Use `audit` when the job is critique-first with no implementation yet.
- Use `polish` when the design direction is already known and the task is to improve execution quality.
- Use `redesign` only when a stronger visual restructuring is explicitly requested.
- Do not convert a bounded design task into broad product redesign by default.

Before implementation, output only:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

Frontend design rules:
- Do not claim visual success from code plausibility alone.
- Keep motion bounded and justified.
- Prefer transform/opacity over layout-thrashing animation.
- Respect reduced-motion and touch/hover reality.
- Do not let “premium design” become generic frontend slop.
