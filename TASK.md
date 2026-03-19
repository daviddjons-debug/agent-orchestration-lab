# Current Experiment

Goal: preserve the working 4-role pipeline while redefining its contract around surgical orchestration discipline instead of simple artifact emission.

## Success criteria
- the runnable baseline remains intact;
- the 4 current roles are reframed around a surgical contract model;
- orchestrator defines objective, locus hypothesis, and boundaries;
- planner defines dependency ring, allowed reads, allowed changes, and verification targets;
- builder is constrained to narrow execution inside the declared change zone;
- reviewer audits boundary adherence and contract completion, not just file existence;
- the repository clearly separates:
  - what is already runnable and proven;
  - what is being redesigned at the role-contract level;
  - what is deferred for later expansion.

## Current runnable workflow
1. orchestrator creates run scaffolding, handoff, and `run_manifest.json`;
2. planner reads only orchestrator handoff plus manifest and writes `02_plan.json` and `02_planner.md`;
3. builder reads only `02_plan.json` and creates all declared output artifacts plus `03_builder.md`;
4. reviewer evaluates files on disk against `run_manifest.json` and `02_plan.json`, then writes `04_reviewer.md`.

## Current redesign target
The current redesign target is a 4-role surgical baseline:
- orchestrator = triage, routing, boundary control;
- planner = locus refinement, dependency ring, execution boundary definition;
- builder = minimal execution inside allowed change zone;
- reviewer = contract audit, scope control, falsifiable verdict.

## Explicit non-goals for this step
This step does not yet:
- rewrite runtime scripts;
- add tester as a runnable stage;
- add security as a runnable stage;
- claim real multi-agent reasoning on complex tasks.

## Next hardening direction
After the 4-role surgical baseline is coherent:
- add `tester` as a verification-specific role;
- add `security` as a risk-gated role;
- then evaluate whether runtime expansion beyond 4 runnable stages is justified.
