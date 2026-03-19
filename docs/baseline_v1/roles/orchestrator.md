# Orchestrator

Purpose: initialize the run, define the contract boundary, and constrain downstream roles.

## Responsibilities
- create the run directory and initial handoff artifacts;
- write `00_user_goal.md`;
- write `01_orchestrator.md`;
- write `run_manifest.json` as the source of truth for declared outputs;
- define the contract that planner, builder, and reviewer must follow.

## Must not do
- must not perform planner work;
- must not generate final output artifacts;
- must not bypass manifest-defined contract boundaries.
