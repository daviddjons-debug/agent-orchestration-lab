# Next Experiment — From Artifact Pipeline to Surgical Baseline

## Current state
The lab already proves a structured 4-role runnable pipeline:
- orchestrator creates the run and initial contract files;
- planner writes `02_plan.json` as the source of truth;
- builder creates declared artifacts from the structured plan;
- reviewer validates contract alignment and artifact contents;
- selftest covers valid, broken, restored, relaxed, and invalid-schema cases.

## Problem with the current state
The current lab proves execution mechanics, but it is still too close to a toy artifact pipeline.

It does not yet enforce:
- triage-first behavior;
- problem locus definition;
- dependency-ring awareness;
- allowed read / allowed change boundaries;
- blast-radius control;
- justified local hardening;
- explicit separation between simple execution and real verification logic.

## Next goal
Preserve the runnable 4-role harness, but redefine the role contracts so the system behaves like a surgical orchestration baseline rather than a generic artifact emitter.

## Immediate upgrade path
### Phase 1 — Rewrite the existing 4 roles
Transform:
- orchestrator -> triage, routing, boundary control
- planner -> locus refinement, dependency ring, execution plan, allowed zones
- builder -> narrow execution within declared change zone
- reviewer -> contract audit, scope-drift detection, falsifiable verdict

### Phase 2 — Introduce missing roles only after Phase 1 is coherent
Add:
- tester -> behavior verification and regression-focused validation
- security -> risk-gated inspection for security-relevant tasks

### Phase 3 — Re-evaluate runtime
Only after the role contracts are coherent:
- decide whether `scripts/` should remain a 4-stage runner;
- or whether the runtime should expand to support tester/security explicitly.

## Success criterion
The next stage must satisfy all of the following:
- the runnable baseline remains operational;
- the role definitions stop pretending that artifact generation alone is enough;
- the repository clearly distinguishes proven mechanics from target behavior;
- the transition toward a surgical system is explicit, staged, and falsifiable.

## Failure condition
This next step fails if:
- new roles are added only cosmetically;
- runtime is expanded before the contract model is coherent;
- the repository starts claiming a 6-role system without real execution support;
- “surgical” language is added without actual boundary discipline.
