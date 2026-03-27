# Session Recap — 2026-03-23 — runtime_pipeline_cleanup_green

## Session goal
Stabilize the runnable pipeline after the pipeline-side cleanup of `00_user_goal.md`, restore green reviewer behavior for lite/heavy profiles, preserve compressed baseline behavior, and prove the runtime is still falsifiable rather than cosmetically “passing”.

## What was actually fixed

### 1) Reviewer required-files contract was wrong after pipeline cleanup
The pipeline now deletes `00_user_goal.md` from the generated run directory before planner/builder/reviewer execution.

But `scripts/reviewer.py` still treated `00_user_goal.md` as a required prior artifact.

That created a false failure mode:
- lite/heavy runs could fail reviewer even when contract, artifacts, and content were all correct;
- failure was caused by stale runtime expectations, not by a real orchestration defect.

### 2) Pipeline entry behavior was cleaned up
`scripts/run_pipeline.py` was aligned with the runnable runtime shape:
- argument validation now expects exactly `2` or `3` argv items;
- `base_dir` is handled as `Path(sys.argv[1])`;
- orchestrator is invoked with `str(base_dir)`;
- run discovery uses `base_dir.glob("orchestrated-*")`;
- missing run directory now reports:
  - `ERROR: orchestrator did not create run directory`
- `00_user_goal.md` is explicitly removed from the run dir before planner/builder/reviewer stages;
- planner, builder, reviewer are invoked with `str(run_dir)`;
- baseline still skips reviewer when no declared trigger is present;
- final output prints the run directory path.

### 3) Reviewer contract was aligned with runtime cleanup
In `scripts/reviewer.py`, `00_user_goal.md` was removed from `REQUIRED`.

This was the decisive contract repair.
Anything else without this change would have been theater.

## Exact meaningful diff
Two files changed:

### `scripts/reviewer.py`
- removed stale required artifact:
  - `00_user_goal.md`

### `scripts/run_pipeline.py`
- removed command echo noise from `run()`;
- normalized argument count handling;
- normalized `Path` usage;
- deleted `00_user_goal.md` during pipeline execution;
- normalized subprocess argument passing with `str(...)`;
- preserved baseline compressed path behavior;
- ensured final run dir is printed.

## Validation that was performed

Validation was not superficial. Multiple runtime cases were exercised.

### A. Baseline profile
Command:
`python3 scripts/run_pipeline.py docs/runs`

Observed behavior:
- orchestrator generated a bounded baseline contract;
- planner produced `02_plan.json`;
- builder created declared artifacts;
- reviewer was correctly skipped:
  - `REVIEWER_SKIPPED=baseline compressed path (no declared review trigger)`

This confirms baseline still behaves as compressed path, not silently upgraded into always-review mode.

### B. Lite profile
A lite run was executed and produced:
- builder actual read sources:
  - `02_plan.json, run_manifest.json`
- reviewer full PASS
- all manifest-plan alignment checks passed
- declared artifact existence and content checks passed
- no undeclared output drift

This proves the reviewer now activates correctly for lite and no longer fails because of deleted `00_user_goal.md`.

### C. Heavy profile
A heavy run was executed and produced:
- builder actual read sources:
  - `02_plan.json, run_manifest.json`
- reviewer full PASS
- full contract alignment and artifact checks passed

This proves the widest runnable runtime path remains green after cleanup.

### D. Falsifiability checks still work
The session also re-exercised failure modes, not just green paths.

Observed reviewer/builder failures included:
- manifest-plan mismatch → FAIL
- artifact content mismatch → FAIL
- undeclared output drift (`output/rogue.txt`) → FAIL
- verify-only adjacent surface unsatisfied → FAIL
- builder read contract mismatch for baseline/heavy → FAIL
- invalid artifact contract shape → FAIL
- clustered artifact inconsistency (`src/spec.json` / generated files) → FAIL

Then restored scenarios returned to PASS.

This matters because a system that only demonstrates green paths is still fake.

## Selftest outcome
A full selftest sequence was run and completed green.

Key visible result:
- `SELFTEST RESULT: PASS`

Also confirmed:
- baseline pipeline skips reviewer on compressed path;
- lite pipeline runs reviewer and passes.

That is the exact activation distinction we needed preserved.

## Final repository state
At the end:
- `git status --short` returned clean
- no uncommitted changes remained

## Commit and tag
Final commit:
- `ab4b7c9` — `Runtime: align reviewer required files with pipeline cleanup`

Final tag:
- `runtime_pipeline_cleanup_green`

Verified final pointer:
- `ab4b7c9 (HEAD -> main, tag: runtime_pipeline_cleanup_green, origin/main, origin/HEAD)`

## What this session proved
This session proved a specific and important thing:

The runnable runtime is not just “green by narration”.
It can:
- preserve profile-dependent activation behavior;
- fail on real contract drift;
- fail on adjacent verification failures;
- fail on undeclared output drift;
- recover to green once the contract is actually repaired.

That is evidence of a bounded and falsifiable runtime, not a decorative multi-agent story.

## Current project state after this session
Current state:
- pipeline cleanup is aligned with reviewer expectations;
- baseline compressed path remains intact;
- lite and heavy review lanes are green;
- selftest is green;
- working tree is clean;
- commit and tag are recorded.

## Recommended next step
Do not jump to broad new architecture yet.

The correct next move is:
1. update the docs layer so runtime behavior and documented behavior stop drifting apart;
2. verify activation/profile semantics in the docs package (`ACTIVATION_MATRIX.md`, `EXECUTION_PROFILES.md`, `HANDOFF_CONTRACT.md`, `VALIDATION_MATRIX.md`, `NEXT_EXPERIMENT.md`);
3. then define the next experiment from the now-stable runtime baseline.

## Revision
### Refuted
- The lite/heavy reviewer failure was not a deep orchestration defect.
- The failure was not in builder artifact creation.
- The failure was not in manifest-plan propagation.
- The failure was a stale reviewer required-files assumption after pipeline cleanup.

### Still unclear
- Whether docs now fully match the repaired runtime behavior.
- Whether any remaining legacy references to `00_user_goal.md` still exist outside runtime-critical code.
- Whether the next experiment should target activation semantics, stricter dependency-ring mechanics, or handoff-contract hardening.

### Sources needed next
- `ACTIVATION_MATRIX.md`
- `EXECUTION_PROFILES.md`
- `HANDOFF_CONTRACT.md`
- `VALIDATION_MATRIX.md`
- `NEXT_EXPERIMENT.md`
- grep across repo for remaining references to `00_user_goal.md`
