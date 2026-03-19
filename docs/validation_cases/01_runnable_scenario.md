# Validation Case 01 — Runnable Scenario

## Scenario name
Manifest-declared narrow output contract

## Why this scenario fits Case 01
- the locus is obvious: run contract files plus declared output artifacts;
- the intended change surface is narrow;
- no multi-file code patching is required;
- the reviewer can falsify corrupted contract state.

## Concrete runnable mapping
- Orchestrator defines the run folder and manifest contract.
- Planner converts that contract into `02_plan.json`.
- Builder creates only the declared output artifacts.
- Reviewer checks manifest-plan alignment and artifact correctness.

## Observable problem locus
`run_manifest.json`, `02_plan.json`, and declared files under `output/`

## Minimal dependency ring
- `01_orchestrator.md`
- `run_manifest.json`
- `02_plan.json`
- `output/`
- `03_builder.md`
- `04_reviewer.md`

## What counts as pass evidence
- planner output matches declared manifest contract;
- builder writes only declared artifacts;
- reviewer returns PASS on valid state;
- reviewer returns FAIL after contract corruption.

## What counts as fail evidence
- undeclared artifact creation;
- contract mismatch between manifest and plan;
- reviewer PASS despite corrupted contract;
- scenario language claims scope control that runtime does not actually enforce.

## Current limitation
This scenario validates narrow contract execution, not full surgical reasoning.
That limitation must stay explicit.
