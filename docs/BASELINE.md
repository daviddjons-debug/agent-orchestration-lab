# Agent Orchestration Lab — Baseline

## What is currently runnable
A runnable orchestration pipeline exists with these executable roles:

- Orchestrator
- Planner
- Builder
- Reviewer

The runtime can create a run folder, derive a plan artifact, execute declared writes through the builder, and evaluate the result through a reviewer gate.

Tester and Security still exist only as non-runnable role concepts, not as enforced runtime stages.

## What is currently proven
The repository no longer proves only a minimal 4-step artifact pipeline.

It now proves a bounded orchestration runtime with:

1. structured orchestrator -> planner -> builder -> reviewer execution;
2. planner-defined contract propagation into runtime artifacts;
3. builder enforcement against undeclared writes;
4. reviewer-side detection of contract drift and malformed outputs;
5. reproducible validation through self-test and explicit validation cases.

## What is proven at artifact level
The current baseline proves the following at artifact level:

- separate executable role nodes;
- structured planner -> builder handoff via `02_plan.json`;
- structured artifact generation from declared contract data;
- formal reviewer gate with PASS/FAIL behavior;
- manifest/runtime influence over output contract shape;
- builder write-boundary enforcement;
- regression coverage for semantic corruption and schema failure;
- bounded adjacent-artifact consistency checks in validation scenarios.

## What is not yet proven at code or task level
The repository does **not** yet prove:

- real surgical triage on live engineering tasks;
- real dependency-aware planning over code graphs;
- structured runtime use of `dependency_ring` as a true ring object with:
  - `primary_target`
  - `adjacent_read_nodes`
  - `adjacent_verify_only_nodes`
  - `excluded_neighbors`;
- full stage-wide runtime read sandboxing beyond the current Builder-enforced `allowed_read_set` contract;
- minimal patch-zone discipline on real source files;
- runnable Tester stage with execution-backed validation;
- runnable Security stage with real policy enforcement;
- realistic multi-file code repair with bounded blast radius.

## What was falsified
A fake handoff was detected earlier:

- `builder.py` originally ignored planner meaning;
- it wrote a hardcoded expected value;
- this produced a false positive PASS.

That defect was corrected by making the builder consume planner-defined contract data instead of emitting a fixed expected result.

## Reproducible checks
### Happy path
`python3 scripts/run_pipeline.py`

### Full regression
`python3 scripts/selftest.py`

`selftest.py` currently verifies:

- PASS on a valid run;
- PASS after manifest override with different output paths and values;
- FAIL after semantic corruption of planner output;
- PASS again after planner restore;
- PASS under relaxed review policy for malformed output content;
- explicit builder failure on invalid planner schema.

## Current conclusion
This repository now represents a runnable **artifact-level orchestration baseline** with partial surgical discipline.

That is stronger than a toy pipeline, but still weaker than a true surgical runtime for live code tasks.

The honest boundary is:

- artifact-level orchestration discipline: proven for bounded runtime artifacts and validation cases;
- persistent bounded live code-level validation: now present through Case 07 on a minimal substrate under `lab_cases/`, but not yet as a first-class automated runtime scenario;
- code-level surgical execution discipline at repository scale: not yet proven.

## Immediate transition principle
Do not replace the runnable baseline.

Preserve the working runtime and continue hardening it by closing falsifiable gaps one at a time.

Do not inflate the system with additional roles or framework complexity before the current baseline proves stricter control over read scope, dependency reasoning, and bounded intervention.

## Next falsifiable milestone
The next load-bearing milestone is not a vague role rewrite.

It is to prove one missing hard control in runtime behavior, preferably one of:

- stricter stage-wide read-boundary enforcement beyond the current Builder-only `allowed_read_set` runtime contract;
- a new validation case that moves from artifact-only consistency into bounded code-level dependency behavior.

Only after that should additional runnable stages or profile layers be treated as meaningful progress.
