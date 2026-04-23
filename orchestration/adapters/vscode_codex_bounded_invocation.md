# VS Code + Codex Bounded Invocation

## Purpose
This file defines the minimal operator-facing invocation pattern for running bounded tasks through VS Code with Codex against the current orchestration layer.

It is not a generic prompt dump.
It is the practical entry surface for launching a task without collapsing back into unbounded chat behavior.

## Operator workflow

### Step 1 — establish the task surface
Before asking Codex to act, define:
- task objective
- visible symptom or requested outcome
- best current problem locus
- whether the task is code, docs, browser/UI, security, packaging, or unknown

### Step 2 — load only the required orchestration surfaces
For a normal bounded coding/debugging task, the minimum reading spine is:
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

Load skill files only if their attached modules are actually activated.

### Step 3 — require bounded routing first
Before implementation, Codex should state:
- `task_class`
- `locus_confidence`
- `false_locality_risk`
- `blast_radius_risk`
- `profile_decision`
- `allowed_modules`
- `blocked_modules`
- `escalation_triggers`

If this routing step is missing, implementation should not start.

### Step 4 — activate only justified modules
Do not let Codex activate:
- browser verification without a real browser/UI surface
- security without a real trust-boundary/security dimension
- second opinion without contradiction/retriage pressure
- release packaging without explicit delivery/handoff output requirements

### Step 5 — require bounded completion output
At minimum, Codex should report:
- whether the objective was achieved
- whether the patch stayed inside the declared change contour
- whether adjacent / verify-only surfaces were checked when required
- whether behavior evidence was produced when required
- whether retriage or escalation is still needed

## Anti-drift rules
Do not let Codex:
- start with broad repo scanning by default
- widen the task because a cleaner architecture is imaginable
- claim success from plausibility alone
- treat skills as always-on prompts
- invoke extra modules merely because they exist

## Current role
This is the first practical Codex-hosted invocation surface for the materialized v3-style portable spine.
