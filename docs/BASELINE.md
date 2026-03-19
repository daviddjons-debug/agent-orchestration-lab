# Agent Orchestration Lab — Baseline

## What is currently proven
A minimal 4-step orchestration pipeline is working:

1. `scripts/orchestrator.py` creates a new run folder with initial artifacts.
2. `scripts/planner.py` creates `02_plan.json` as the source-of-truth plan and `02_planner.md` as a human-readable trace.
3. `scripts/builder.py` reads `02_plan.json` and writes all declared output artifacts.
4. `scripts/reviewer.py` validates files on disk and returns PASS/FAIL.

## What the current baseline actually is
This is a runnable **4-role contract pipeline**, not yet a full surgical agent system.

Current runnable roles:
- Orchestrator
- Planner
- Builder
- Reviewer

Missing as real runnable roles:
- Tester
- Security

## Current artifact contract
Target artifacts:
- `output/result.json`
- `output/summary.txt`

Required JSON shape:
```json
{
  "status": "ok",
  "message": "multi-agent orchestration check passed"
}
```

Required text content:
```text
multi-agent orchestration check passed
```

## What was falsified
A fake handoff was detected earlier:
- `builder.py` originally ignored planner meaning;
- it wrote a hardcoded expected value;
- this produced a false positive PASS.

That defect was fixed by making `builder.py` parse planner-defined fields and build artifacts from planner-provided contract data.

## Reproducible checks
### Happy path
`python3 scripts/run_pipeline.py`

### Full regression
`python3 scripts/selftest.py`

`selftest.py` verifies:
- PASS on a valid run;
- PASS after manifest override with different output paths and values;
- FAIL after semantic corruption of planner output;
- PASS again after planner restore;
- PASS under relaxed review policy for malformed output content;
- explicit builder failure on invalid planner schema.

## Current conclusion
This repository proves:
- separate executable role nodes;
- structured planner -> builder handoff via `02_plan.json`;
- structured artifact generation from declared contract;
- formal reviewer gate;
- reproducible regression checks.

It does **not** yet prove:
- surgical triage behavior;
- dependency-aware planning;
- minimal patch-zone discipline;
- scope-drift control in realistic task execution;
- tester/security role integration.

## Immediate transition principle
Do not replace the runnable baseline first.
Preserve it.
Then redesign the role contracts so the same 4-role system stops being merely an artifact pipeline and becomes a surgical orchestration baseline.

## Next likely milestone
Rewrite the 4 existing roles into a surgical contract baseline before adding any new runnable roles.
