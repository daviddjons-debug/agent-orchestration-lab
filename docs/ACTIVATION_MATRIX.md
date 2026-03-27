# Agent Pack v2 / Surgical Edition — Activation Matrix

## Purpose
Translate extracted surgical rules into runtime activation logic so the system uses the minimum necessary execution graph for each task class.

## Design objective
The system must not scale by agent count.
It must scale by activated function, risk trigger, and justified validation depth.

## Core principle
Default to the cheapest path that can still prevent the relevant failure class.

---

## Execution profiles

### Direct
Use when:
- locus is already clear
- false locality risk is low
- change surface is single-node
- no verify-only or adjacent consistency surface is load-bearing
- no security-sensitive boundary is involved
- no prior failed attempt suggests hidden complexity

Active by profile:
- triage/localize
- planner via the current runnable compatibility path
- bounded execution
- one targeted validation

Inactive by profile:
- tester
- security pass
- retriage loop
- reviewer as separate full lane unless a declared review trigger is present

### Lite
Use when:
- locus is mostly clear but bounded discipline still matters
- false locality risk is low-to-medium
- verify-only surface may matter
- undeclared drift risk is non-zero
- patch is small but should still be reviewed

Active by profile:
- orchestrator/triage
- bounded mini-plan
- builder
- light reviewer

Trigger-based functions within profile:
- tester
- retriage

Inactive by profile:
- security pass unless explicitly triggered
- heavy review stack

### Heavy
Use when:
- locus confidence is not high
- false locality risk is medium or high
- bounded cluster consistency is involved
- generated artifacts must stay aligned
- actual blocker may differ from assumed blocker
- security-sensitive surface is involved
- previous bounded attempt failed
- blast radius is material

Active by profile:
- orchestrator
- planner
- builder
- reviewer
- tester when executable behavior exists
- security when boundary-relevant
- retriage/escalation loop when evidence demands it

---

## Profile selection rule

- Start in Direct at the policy layer.
- Escalate to Lite only when bounded evidence shows that Direct policy / runnable `baseline` compatibility path would under-control locality, adjacent validation, or drift risk.
- Escalate to Heavy only when bounded evidence shows that Direct policy / runnable `baseline` compatibility path or Lite would under-control locality, consistency, security, or blocker uncertainty.
- Do not escalate by task size narrative alone.
- Do not activate extra roles merely because they exist in the pack.

---
## Function matrix

| Function | Primary responsibility | Risk reduced | Direct | Lite | Heavy | Must activate when | Must stay off when |
|---|---|---|---|---|---|---|---|
| Triage / Orchestrator | Localize problem and choose execution profile | false locality, scope drift | yes | yes | yes | task begins | never skipped |
| Planner | Convert triage into explicit bounded contract | premature widening, sloppy patch surface | compatibility-on, policy-compressed | trigger-based mini-plan | on | locus uncertainty, cluster task, verify-only surface, multi-node dependency | fully collapsed future Direct runtime |
| Builder | Apply bounded patch or no-op | uncontrolled edits | yes | yes | yes | any execution path | never skipped |
| Reviewer | Check contract alignment, bounded completion, undeclared drift | false success, drift, unjustified widening | trigger-based | on | on | any non-trivial patch, verify-only load, cluster consistency | trivial direct no-op with explicit bounded proof |
| Tester | Validate executable symptom or regression surface | behavior regression | off | trigger-based | trigger-based | executable behavior changed or symptom-level test exists | data/text-only task with no runnable behavior |
| Security | Inspect trust-boundary implications | auth/data exposure, privilege risk | off | trigger-based | trigger-based | auth, file handling, secrets, network, permissions, dangerous boundary | isolated low-risk local task |
| Retriage loop | Override assumed failure mode when evidence disagrees | narrative lock-in, wrong-locus repair | off | trigger-based | trigger-based | actual blocker differs from assumed blocker | clean case with aligned evidence |
| No-op discipline | Accept validated no-change outcome | needless patching | yes | yes | yes | bounded validation shows no defect | claimed defect remains unconfirmed |

---

## Role mapping to current pack

This matrix does not replace the current role pack.
It constrains when each role should activate and how much behavior it should express under each profile.

| Current role | Load-bearing function | Direct | Lite | Heavy |
|---|---|---|---|---|
| Orchestrator | triage, locus selection, profile choice | compressed | on | on |
| Planner | bounded contract shaping | compatibility-on, policy-compressed | trigger-based mini-plan | on |
| Builder | bounded patch or no-op execution | on | on | on |
| Reviewer | bounded audit, drift detection, completion check | trigger-based light check | on | on |
| Tester | executable symptom / regression validation | off | trigger-based | trigger-based |
| Security | trust-boundary audit | off | trigger-based | trigger-based |

### Interpretation
- Direct does not mean no discipline; it means the minimum graph.
- In the current runnable compatibility path, Planner still executes in Direct even though policy-level Direct treats it as compressed rather than truly optional.
- Lite keeps the same pack but compresses non-essential roles.
- Heavy activates the full bounded surgical graph only on evidence.
- A role being present in the pack does not mean it should always appear as a separate expensive lane.
- No-op discipline and retriage are cross-cutting behaviors, not standalone default roles.

---

## Trigger candidates

### Planner triggers
- locus_confidence is not high
- false_locality_risk is medium or high
- verify_only_surfaces is non-empty
- adjacent consistency must be preserved
- allowed_change_set would otherwise widen speculatively
- contract boundary pressure exists; see `docs/UNIFIED_HANDOFF_CONTRACT_CANON_V4.md`
- task is bounded cluster or generated-artifact consistency work

### Reviewer triggers
- patch was applied
- verify_only_surfaces is non-empty
- adjacent consistency link exists
- undeclared drift risk is non-zero
- contract completion semantics follow `docs/UNIFIED_HANDOFF_CONTRACT_CANON_V4.md`
- task is not trivial direct no-op

### Tester triggers
- behavior is executable
- symptom can be checked directly
- patch changes runtime behavior
- regression surface is meaningful

### Security triggers
- auth or permission logic
- file upload / file write / parsing boundary
- secrets or credentials
- network-facing behavior
- trust-boundary crossing

### Retriage triggers
- reviewer-blocking evidence contradicts assumed defect path
- actual blocker is outside initial stale node
- primary fix does not clear bounded failure
- verify-only or adjacent surface exposes a different blocker

---

## Rules to preserve from extracted cases
- localize before patching
- start from the smallest sufficient change surface
- widen only on evidence
- verify-only and adjacent consistency surfaces are load-bearing when declared
- no-op is valid when bounded evidence clears the defect claim
- source-of-truth must not be conflated with stale defect node
- actual blocker must override assumed scenario when evidence disagrees

---

## Open decisions
- when Planner can be removed from Direct at runtime rather than only compressed at the policy layer
- which functions collapse together in Lite
- when Direct may skip separate Reviewer safely
- whether Tester remains a separate role or a Heavy-only lane
- whether Security is role-based or policy-based
