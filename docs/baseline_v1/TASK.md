# Current Experiment

Goal: prove that a 4-role workflow can execute through explicit contracts, produce multiple output artifacts, and return a falsifiable verdict.

## Success criteria
- every role leaves a separate artifact;
- planner handoff is structured and reviewable;
- builder reads only the structured plan contract;
- reviewer validates both contract consistency and declared outputs;
- reviewer returns PASS on the valid case and FAIL on broken cases;
- a human can inspect a run folder in under 2 minutes.

## Current workflow
1. orchestrator creates run scaffolding, handoff, and `run_manifest.json`;
2. planner reads only orchestrator handoff plus manifest and writes `02_plan.json` and `02_planner.md`;
3. builder reads only `02_plan.json` and creates all declared output artifacts plus `03_builder.md`;
4. reviewer evaluates files on disk against `run_manifest.json` and `02_plan.json`, then writes `04_reviewer.md`.

## Current proof target
The current baseline is a multi-file artifact contract:
- one JSON artifact;
- one text artifact;
- explicit reviewer validation for both.

## Next hardening direction
Extend the contract model with one or more of:
- nested output directories;
- richer JSON schemas;
- additional artifact types;
- stricter planner schema validation;
- more realistic task decomposition under the same contract rules.
