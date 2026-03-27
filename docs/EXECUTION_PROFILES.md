# Execution Profiles

## Purpose
Summarize the execution profiles used by Surgical Edition.

`docs/ACTIVATION_MATRIX.md` is the canonical source of truth for activation logic, trigger logic, and role/profile behavior.
This file is a compact profile summary only.

## Profiles

### Direct (`baseline` in runnable 4-role runtime)
Direct is the policy-layer starting profile.
`baseline` is the runnable compatibility label for the Direct profile.

Use when:
- the task is narrow and localized;
- the problem locus is already obvious;
- false-locality risk is low;
- the change surface is low-risk;
- no verify-only or adjacent consistency surface is already load-bearing;
- no explicit security dimension is present.

Expected flow:
- Orchestrator in compressed form
- Planner via the current runnable compatibility path
- Builder
- targeted validation
- Reviewer only when trigger evidence requires a separate check

Rules:
- keep read scope narrow;
- keep change scope narrow;
- treat Planner as policy-compressed in Direct, even though the current runnable compatibility path still executes it;
- do not invoke Tester by default;
- do not invoke Security by default;
- do not widen the task unless evidence forces it.

### Lite
Use when:
- a local fix is still plausible;
- bounded adjacent reading or verification is needed;
- the task remains narrow enough for disciplined execution;
- drift or adjacent-risk control still matters.

Expected flow:
- Orchestrator
- Planner in bounded/mini-plan form
- Builder
- Reviewer
- Tester only when trigger evidence requires behavior validation

Rules:
- keep the execution graph bounded;
- make adjacent verification explicit when load-bearing;
- do not invoke Security unless the task has a real security dimension;
- do not widen the task unless evidence forces it.

### Heavy
Use when:
- the problem locus is unclear or disputed;
- the dependency ring is non-trivial;
- multiple surfaces or coordinated consistency may be involved;
- blocker uncertainty is material;
- regression risk is non-trivial;
- the task has a real security dimension;
- failure cost is high enough that shallow verification is not credible.

Expected flow:
- Orchestrator
- Planner
- Builder
- Reviewer
- Tester when verification depth is required
- Security when risk dimension is real
- retriage/escalation loop when evidence requires it

Rules:
- triage must be explicit before implementation;
- dependency ring must be stated;
- allowed read and change sets must be explicit;
- verification targets must be explicit;
- Tester and Security are invoked by evidence, not by ritual;
- widening beyond the minimum justified contour must be evidence-driven.

## Selection rule
- Start in Direct at the policy layer.
- Escalate to Lite only when bounded evidence shows that Direct policy / runnable `baseline` compatibility path would under-control locality, adjacent validation, or drift risk.
- Escalate to Heavy only when bounded evidence shows that Direct policy / runnable `baseline` compatibility path or Lite would under-control locality, consistency, security, or blocker uncertainty.
- Do not escalate by task-size narrative alone.

## Current status
Profiles are currently defined primarily at the policy and documentation layer.

They guide routing and expected discipline, but they do not yet constitute a fully enforced runtime stage graph.
In the current runnable compatibility path, Direct still executes Planner, while Reviewer remains trigger-based for Direct and always-on for Lite/Heavy.

Runtime/profile enforcement can be expanded later if justified.
