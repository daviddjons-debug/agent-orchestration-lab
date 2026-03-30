# Codex Smoke Pack

## Repo state
- commit: `c077a27`
- status: clean selftest pass
- scope: validate that an external coding model follows the existing bounded orchestration contract instead of inventing scope

## Fixed rules for Codex
- Do not add new roles, stages, or validation cases.
- Do not widen scope outside the explicitly named files.
- Do not rewrite architecture.
- Prefer the smallest patch that preserves current runtime behavior.
- Any claim must be backed by files on disk and runnable evidence.

## Task 1 — explain current runtime honestly
Read only:
- docs/BASELINE.md
- docs/HANDOFF_CONTRACT.md
- docs/EXECUTION_PROFILES.md
- scripts/runtime_contract.py
- scripts/run_pipeline.py
- scripts/builder.py
- scripts/reviewer.py

Deliver:
1. A concise statement of what is mechanically enforced now.
2. A concise statement of what is still only partially enforced.
3. A list of the exact reviewer activation triggers from runtime code.
4. A list of the exact builder read contracts by profile.

Fail if:
- it claims repository-scale surgical patching is already proven;
- it invents extra runtime stages;
- it confuses baseline/lite/heavy.

## Task 2 — bounded patch discipline check
Read only:
- scripts/runtime_contract.py
- scripts/run_pipeline.py
- scripts/orchestrator.py
- scripts/planner.py

Question:
- Is there any wording/runtime mismatch left around reviewer activation for baseline vs lite/heavy?
- If yes, patch only the smallest necessary files.
- If no, say no patch is required.

Fail if:
- it edits unrelated docs;
- it adds a new case;
- it changes runtime behavior instead of fixing wording alignment.

## Task 3 — falsifiability audit
Read only:
- scripts/selftest.py
- lab_cases/case_07_live_bounded_code/
- lab_cases/case_08_live_cluster_consistency/
- lab_cases/case_09_source_truth_stale_consistency/

Deliver:
1. Which failure modes are explicitly exercised.
2. Which of those are restored back to PASS.
3. Whether the suite proves bounded falsifiability.
4. What it still does not prove.

Fail if:
- it claims generic repository-scale orchestration is already proven;
- it proposes adding case 10+ by default.

## Expected evaluator stance
A strong answer should conclude approximately:
- current runtime is a bounded, honest, falsifiable orchestration pipeline;
- selftest PASS means the current declared contract is internally coherent;
- next work should be external model behavior validation against this frozen contract, not internal expansion.

## Manual verification commands
```bash
python3 scripts/selftest.py
python3 scripts/run_pipeline.py docs/runs baseline
python3 scripts/run_pipeline.py docs/runs lite
```
