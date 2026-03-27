# Next Experiment — From Artifact Pipeline to Surgical Runtime

## Current state
The lab already proves a structured 4-role runnable pipeline:
- orchestrator creates the run and initial contract files;
- planner writes `02_plan.json` as the source of truth;
- builder creates declared artifacts from the structured plan;
- reviewer validates contract alignment and artifact contents;
- selftest covers valid, broken, restored, relaxed, and invalid-schema cases.

## Problem with the current state
The current lab proves bounded execution mechanics and contract discipline, but it still risks optimizing for validation expansion instead of operating compression.

It already proves in bounded form:
- structured problem locus and dependency-ring propagation through the run contract;
- planner-to-reviewer contract alignment checks;
- builder-side write-boundary enforcement through `allowed_change_set`;
- Direct-path Builder read-boundary validation through `allowed_read_set` under current Direct compatibility behavior;
- reviewer-side falsification of content drift, undeclared output drift, bounded adjacent consistency failures, and verify-only false-local success.

It does not yet prove or enforce:
- profile compression as a real operating rule for cheap tasks;
- a crisp always-on vs trigger-based activation boundary;
- triage-first behavior as real runtime decision logic outside bounded artifact scenarios;
- genuine dependency discovery beyond predeclared scenario structure;
- blast-radius control on live code tasks;
- justified local hardening based on discovered evidence;
- runnable Tester and Security stages as evidence-triggered lanes rather than default ceremony.

## Next goal
Preserve the runnable 4-role harness, keep the current bounded proof honest, and compress the operating model so the system defaults to the cheapest credible path and escalates only on bounded evidence.

## Immediate upgrade path
### Phase 1 — Freeze the proven bounded core
Treat the existing falsification lanes and bounded live substrates as proof artifacts, not as an endlessly expanding validation matrix.

Preserve:
- baseline/Direct compatibility behavior;
- Builder-enforced read boundary semantics;
- reviewer falsification of drift, inconsistency, and verify-only failures;
- bounded persistent substrates already established through Case 07 and Case 08.

### Phase 2 — Compress activation logic into an operating rule
Before expanding the stage graph, define the minimal execution model that should survive into real use.

The activation/dispatch contract is now defined at the policy layer in:
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`
- `docs/HANDOFF_CONTRACT.md`

The current priority is:
- remove remaining documentation contradictions against the activation model;
- distinguish policy-level Direct from current Direct compatibility behavior consistently;
- keep the bounded validation corpus as proof, not as a substitute for operating compression;
- only expand runtime after tester/security activation rules are operationally coherent.

The next step is therefore alignment and compression discipline first, not fresh validation expansion by default.

### Phase 3 — Introduce missing roles only after compression is coherent
Add:
- tester -> behavior verification and regression-focused validation when executable behavior exists;
- security -> risk-gated inspection only when a real trust boundary is involved.

Only after that should runtime expansion be reconsidered explicitly.

### Phase 4 — Re-evaluate runtime
Only after the activation model is coherent:
- decide whether `scripts/` should remain a 4-stage runner;
- or whether the runtime should expand to support tester/security explicitly.

## Success criterion
The next stage must satisfy all of the following:
- the runtime `baseline` path remains operational;
- simple tasks stay on the minimum credible path;
- escalation happens only on bounded evidence;
- the repository clearly distinguishes proven mechanics from declared target state;
- the transition toward a surgical system is explicit, staged, falsifiable, and cost-aware.

## Failure condition
This next step fails if:
- new roles are added only cosmetically;
- runtime is expanded before the activation model is coherent;
- simple tasks still pay Heavy-style ceremony by default;
- the repository starts claiming a 6-role system without real execution support;
- “surgical” language is added without actual boundary discipline.
