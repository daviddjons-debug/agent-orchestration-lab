# Leo_Agents_V2 Runtime Activation Matrix

## Purpose
This is the compact runtime activation matrix for `Leo_Agents_V2`.

It defines:
- which execution profile to prefer;
- when to escalate;
- how modules should activate without role theater or default full-stack behavior.

## Core profile rule
Start from the cheapest justified path.
Escalate only when bounded evidence shows the cheaper path would under-control the task.

## Profiles

### direct
Use when:
- the task is narrow and localized;
- the likely locus is already clear;
- false-locality risk is low;
- the change contour is small;
- no real browser/security/adjacent-consistency burden is already load-bearing.

Default shape:
- minimal routing
- minimal planning
- bounded implementation only if authorized

### lite
Use when:
- the task remains bounded but needs stricter discipline;
- adjacent verification matters;
- a local fix may still be valid, but false-local success risk is non-trivial;
- browser/UI verification or bounded external invocation requires more control.

Default shape:
- routing
- planning
- bounded implementation only if authorized
- bounded module activation by evidence

### heavy
Use when:
- the task has a real security or trust-boundary dimension;
- blocker uncertainty is material;
- regression or exposure risk is non-trivial;
- a cheaper path would under-control the failure class.

Default shape:
- explicit routing
- explicit bounded planning
- no ritual full-stack activation; modules still require evidence

## Module activation principles
- `triage` and `planning` are the normal starting core
- `execution` activates only when implementation is authorized
- `review` activates when consistency/completion checking is materially needed
- `testing` activates when runnable behavior evidence is load-bearing
- `browser_verification` activates when visible browser/UI behavior is part of acceptance
- `security` activates when a real trust/exposure boundary is involved
- `external_second_opinion` activates only when contradiction/retriage pressure is justified
- `release_packaging` activates only when delivery/handoff output is part of the task

## Escalation triggers
Escalate when:
- locus confidence drops
- allowed read scope is insufficient
- allowed change scope is insufficient
- verify-only surfaces block a local completion claim
- browser-visible behavior cannot be validated under the cheaper path
- security/trust-boundary behavior cannot be evaluated under the cheaper path
- actual blocker evidence contradicts the assumed path

## Anti-drift rule
Do not escalate by task-size narrative alone.
Do not activate extra modules merely because they exist.
