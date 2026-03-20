# Execution Profiles

## Purpose
Define when the system should stay lightweight and when it should use the heavier surgical flow.

## Lite profile

### Use when
- the task is narrow and localized;
- the problem locus is already obvious;
- the dependency ring is small;
- the change surface is low-risk;
- no explicit security dimension is present;
- no meaningful regression surface is expected beyond the nearest node.

### Expected flow
- Orchestrator
- Planner
- Builder
- Reviewer

### Rules
- keep read scope narrow;
- keep change scope narrow;
- do not invoke Tester by default;
- do not invoke Security by default;
- do not widen the task unless evidence forces it.

## Heavy profile

### Use when
- the problem locus is unclear;
- the dependency ring is wider than one immediate node;
- multiple files or surfaces are likely involved;
- regression risk is non-trivial;
- the task has a real security dimension;
- local hardening may be justified;
- failure cost is high enough that shallow verification is not credible.

### Expected flow
- Orchestrator
- Planner
- Builder
- Reviewer
- Tester when verification depth is required
- Security when risk dimension is real

### Rules
- triage must be explicit before implementation;
- dependency ring must be stated;
- allowed read and change sets must be explicit;
- verification targets must be explicit;
- Tester and Security are invoked by evidence, not by ritual.

## Selection rule
Orchestrator must choose Lite by default only when the task is clearly narrow and low-risk.
If that cannot be justified, the task must be treated as Heavy.

## Current status
Profiles are currently defined primarily at the policy and documentation layer.

They guide routing and expected discipline, but they do not yet constitute a fully enforced runtime stage graph.

Runtime/profile enforcement can be expanded later if justified.
