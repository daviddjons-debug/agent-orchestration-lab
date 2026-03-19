# Validation Case 02 — Runnable Scenario

## Scenario name
Primary artifact contract with adjacent summary-consistency risk

## Why this scenario fits Case 02
- the primary locus is local: one declared output artifact contract
- an adjacent node exists: a second declared artifact that must stay semantically aligned with the primary artifact
- the task is still narrow and runnable in the current 4-stage pipeline
- reviewer can falsify the case if direct artifact correctness is checked but cross-artifact consistency is ignored

## Concrete runnable mapping
- Orchestrator declares a narrow run contract with two related output artifacts
- Planner carries forward the primary locus and explicit adjacent dependency node
- Builder creates both artifacts inside the declared write boundary
- Reviewer checks both:
  - direct artifact contract correctness
  - adjacent artifact consistency with the primary artifact message

## Primary locus
`output/result.json`

## Adjacent dependency node
`output/summary.txt`

## Why the adjacent node is in scope
The summary artifact is not an unrelated extra file.
It is a neighboring output surface that must remain consistent with the primary JSON artifact message.
If the JSON contract changes but the summary artifact remains stale or semantically inconsistent, the local task is not actually safe.

## Minimal dependency ring
- `01_orchestrator.md`
- `run_manifest.json`
- `02_plan.json`
- `output/result.json`
- `output/summary.txt`
- `03_builder.md`
- `04_reviewer.md`

## Cross-artifact consistency rule
The semantic message represented in `output/summary.txt` must match the message declared in `output/result.json`.
This rule is what makes the summary file an adjacent dependency node rather than a decorative second artifact.

## What counts as direct symptom evidence
- `output/result.json` exists
- `output/result.json` satisfies declared required fields

## What counts as adjacent-node safety evidence
- `output/summary.txt` exists
- `output/summary.txt` satisfies its declared contract
- `output/summary.txt` remains semantically consistent with the JSON message in `output/result.json`

## What counts as fail evidence
- primary artifact is correct but adjacent summary artifact is missing
- primary artifact is correct but adjacent summary artifact is stale or semantically inconsistent
- reviewer passes despite missing cross-artifact consistency evidence
- scenario language claims dependency awareness without making the adjacent consistency rule explicit

## Current limitation
This scenario is still a controlled contract case, not a real source-code dependency case.
Its purpose is to test whether the runtime can distinguish direct correctness from nearby consistency risk in a bounded setting.

