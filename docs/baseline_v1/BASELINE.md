# Agent Orchestration Lab — Baseline

## What is proven
A minimal 4-step orchestration pipeline is working:

1. `scripts/orchestrator.py` creates a new run folder with initial artifacts.
2. `scripts/planner.py` creates `02_plan.json` as the source-of-truth plan and `02_planner.md` as a human-readable trace.
3. `scripts/builder.py` reads `02_plan.json` and writes all declared output artifacts.
4. `scripts/reviewer.py` validates files on disk and returns PASS/FAIL.

## Current artifact contract
Target artifact:
`output/result.json`

Required JSON shape:
```json
{
  "status": "ok",
  "message": "multi-agent orchestration check passed"
}
```

## What was falsified
A fake handoff was detected earlier:
- `builder.py` originally ignored planner meaning
- it wrote a hardcoded expected value
- this produced a false positive PASS

That defect was fixed by making `builder.py` parse planner-defined fields and build JSON from them.

## Reproducible checks
### Happy path
`python3 scripts/run_pipeline.py`

### Full regression
`python3 scripts/selftest.py`

`selftest.py` verifies:
- PASS on a valid run
- FAIL after semantic corruption of the planner output
- PASS again after planner restore

## Current conclusion
This repository now proves **orchestration mechanics** with:
- separate executable role nodes
- structured planner -> builder handoff via `02_plan.json`
- structured artifact generation
- formal reviewer gate
- reproducible regression test

It does **not** yet prove:
- advanced multi-agent reasoning
- autonomous task decomposition on complex problems
- dynamic planning quality across non-trivial tasks

## Next likely milestone
Extend the artifact contract further with nested directories, richer schemas, or additional artifact types beyond `json` and `text`.
