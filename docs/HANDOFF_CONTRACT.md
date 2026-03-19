# Handoff Contract

## Purpose
Define one shared contract language for orchestrator, planner, builder, reviewer, tester, and security.

## Required fields
- objective
- problem_locus
- dependency_ring
- allowed_read_set
- allowed_change_set
- forbidden_zone
- acceptance_criteria
- verification_targets
- blockers_or_uncertainties

## Surgical extension fields
- verify_only_surfaces
- excluded_neighbors
- review_strictness

## Field meanings
### objective
Concrete task outcome that must be achieved.

### problem_locus
Current best hypothesis of where the real issue or change surface is located.

### dependency_ring
Nearest files, modules, artifacts, or surfaces that may be directly affected or required for verification.

### allowed_read_set
What execution-stage roles are allowed to inspect after planning produces the executable contract. In the current runnable baseline, this should be interpreted primarily as the Builder read boundary, not as the Planner input scope.

### allowed_change_set
What downstream roles are allowed to modify.

### verify_only_surfaces
Surfaces that must be inspected or validated for correctness but must not be modified.

### excluded_neighbors
Nearby nodes or surfaces intentionally excluded from the current execution scope, with the expectation that planning or review makes that exclusion explicit and defensible.

### forbidden_zone
What is explicitly out of scope and must not be touched.

### review_strictness
How aggressively reviewer should treat evidence gaps, adjacent-risk concerns, and sufficiency-of-scope questions in the current run.

### acceptance_criteria
Conditions required for task completion.

### verification_targets
What must be checked after implementation.

### blockers_or_uncertainties
Unknowns, assumptions, or missing evidence that may affect correctness.

## Enforcement rules
- If triage is incomplete, Builder must not start.
- If allowed_read_set is undefined, Builder must not widen its read scope on its own.
- If allowed_change_set is undefined, Builder must not widen scope on its own.
- If verify_only_surfaces are declared, Reviewer must not assume they were checked unless evidence is present.
- If excluded_neighbors are omitted where adjacent-risk is material, Reviewer must treat scope control as incomplete.
- If verification_targets are missing, Reviewer must not assume success.
- If review_strictness is declared, Reviewer must apply it explicitly; runs with adjacent-risk or false-local-success risk should declare it.
- Tester is invoked only when explicit behavior or regression validation is needed.
- Security is invoked only when the task has a real security dimension.

## Minimal example
```json
{
  "objective": "Produce declared artifacts for the current run contract",
  "problem_locus": "run folder contract files and declared outputs",
  "dependency_ring": ["01_orchestrator.md", "run_manifest.json", "02_plan.json", "output/"],
  "allowed_read_set": ["02_plan.json"],
  "allowed_change_set": ["02_plan.json", "output/", "03_builder.md"],
  "verify_only_surfaces": ["output/summary.txt"],
  "excluded_neighbors": [],
  "forbidden_zone": ["scripts/", "docs/baseline_v1/"],
  "review_strictness": "standard",
  "acceptance_criteria": ["all declared artifacts exist", "all declared artifacts satisfy contract"],
  "verification_targets": ["manifest-plan alignment", "artifact content checks"],
  "blockers_or_uncertainties": ["none"]
}
```

## Current status
This contract is defined at the documentation layer first.
Current runtime proves propagation of `allowed_read_set` and baseline Builder-compatible read-boundary enforcement, but does not yet provide full mechanical runtime read sandboxing.
Planner input scope remains role-defined and separate from `allowed_read_set` semantics.
Runtime enforcement can be expanded later if justified.
