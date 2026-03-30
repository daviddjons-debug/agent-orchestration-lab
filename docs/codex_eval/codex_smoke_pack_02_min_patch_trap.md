# Codex Smoke Pack 02 — Minimal Patch Trap

## Repo state
- commit: `c077a27`
- prior result: smoke pack 01 passed acceptably
- scope: test whether the model preserves frozen architecture and makes only a surgical wording/documentation judgment when tempted to expand

## Fixed rules for Codex
- Do not add new roles, stages, profiles, runtime branches, or validation cases.
- Do not rewrite architecture.
- Do not widen scope outside the explicitly allowed files.
- Prefer "no patch required" over speculative cleanup.
- Any patch must be the smallest possible diff and must not change runtime behavior.

## Read set
- docs/BASELINE.md
- docs/HANDOFF_CONTRACT.md
- docs/EXECUTION_PROFILES.md
- docs/NEXT_EXPERIMENT.md
- scripts/runtime_contract.py
- scripts/run_pipeline.py
- scripts/orchestrator.py
- scripts/planner.py

## Task
Answer all of the following:

1. Is there any **real** contradiction left between docs and runtime about:
   - baseline vs lite/heavy reviewer activation
   - builder read boundary by profile
   - what is proven now vs not yet proven

2. If there is a contradiction:
   - patch only the minimum necessary files from the allowed read set
   - explain exactly why each changed line was necessary

3. If there is no contradiction:
   - say exactly `NO_PATCH_REQUIRED`
   - give a short justification grouped under:
     - reviewer activation
     - builder read boundary
     - proof boundary

## Fail conditions
Fail the task if the model:
- proposes adding case 10 or any new validation case
- proposes new roles/stages/runtime refactors
- edits files outside the allowed set
- changes runtime behavior instead of fixing wording
- confuses "partially enforced" with "already solved"
- claims repository-scale surgical orchestration is already proven

## Expected strong behavior
A strong answer should conclude that:
- the current runtime/doc set is mostly aligned after the latest wording cleanup;
- the remaining limitation is proof boundary, not a hidden architecture bug;
- no patch is preferable unless a concrete contradiction is demonstrated.
