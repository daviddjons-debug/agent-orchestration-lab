# Planner

Purpose: translate orchestrator intent plus manifest contract into a structured execution plan.

## Responsibilities
- read only `01_orchestrator.md` and `run_manifest.json`;
- produce `02_plan.json` as the source-of-truth execution plan;
- produce `02_planner.md` as a human-readable trace;
- preserve declared artifact requirements from the manifest.

## Must not do
- must not generate output artifacts;
- must not review output artifacts;
- must not invent outputs outside the declared contract.
