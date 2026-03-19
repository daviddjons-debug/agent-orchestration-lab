# Validation Matrix

## Purpose
Define the minimum task set required to distinguish a real surgical orchestration system from a role-decorated toy pipeline.

## Test classes

### 1. Narrow single-node fix
- Goal: verify that the system can stay local when the problem locus is obvious.
- Expected profile: Lite
- What must be checked: no unnecessary read expansion, no unnecessary change expansion, explicit local verification.

### 2. Local fix with adjacent dependency risk
- Goal: verify that the system maps the nearest dependency ring instead of patching blindly.
- Expected profile: Lite or Heavy depending on evidence
- What must be checked: adjacent node awareness, no fake certainty, bounded verification of the nearby surface.

### 3. Multi-file coordinated change
- Goal: verify that the system can widen scope only when justified.
- Expected profile: Heavy
- Runnable lab interpretation: a bounded pseudo-code dependency scenario, not yet a real repository-scale code patch task.
- What must be checked:
  - explicit primary locus plus explicitly justified secondary nodes;
  - explicit dependency ring and explicit allowed_change_set;
  - no uncontrolled spread beyond the declared local cluster;
  - evidence that widening was necessary rather than decorative;
  - reviewer can falsify the case if the primary symptom is addressed but coordinated dependent surfaces remain stale or inconsistent.

### 4. False-local change with omitted adjacent verification
- Goal: verify that the system does not accept an apparently local fix when adjacent correctness depends on verify-only or explicitly excluded nearby surfaces.
- Expected profile: Heavy
- Runnable lab interpretation: a bounded false-locality scenario where the primary artifact can pass while adjacent correctness remains unverified or stale.
- What must be checked:
  - orchestrator states false-locality risk explicitly;
  - planner distinguishes primary target, adjacent nodes, excluded neighbors, and verify-only surfaces;
  - builder does not widen the change surface just because adjacent risk exists;
  - reviewer fails or withholds a trustworthy pass when adjacent verification is omitted;
  - the case can distinguish true local success from false-local success.

### 5. Security-relevant task
- Goal: verify that Security is invoked only when justified, stays constrained to the declared security-relevant surface, and produces concrete findings instead of ritual security theater.
- Expected profile: Heavy
- Runnable lab interpretation: a bounded scenario where a task has a specific declared security trigger and the system must distinguish confirmed findings, unproven concerns, and optional hardening.
- What must be checked:
  - security invocation is explicitly justified rather than automatic;
  - security trigger is concrete and linked to the actual task surface;
  - findings stay within the declared change surface and immediate trust-boundary neighbors;
  - optional hardening is not presented as a blocker;
  - speculative concerns are not reported as confirmed findings;
  - the case can distinguish `invoke` from `skip` on evidence, not ritual.

### 6. Task with justified local hardening
- Goal: verify that the system can distinguish required local hardening from opportunistic refactoring and can justify why the hardening is necessary for the declared task rather than decorative scope growth.
- Expected profile: Heavy
- Runnable lab interpretation: a bounded scenario where a task can be completed without a broader rewrite, but one local protective change may still be justified if evidence ties it directly to the same failure surface.
- What must be checked:
  - the system distinguishes direct fix, justified local hardening, and optional refactoring;
  - any hardening remains inside the declared local surface and does not widen into unrelated cleanup;
  - tester or reviewer records evidence for why the hardening is required rather than cosmetic;
  - the case can reject opportunistic refactoring disguised as safety or cleanup;
  - the case can pass when the hardening is tightly linked, bounded, and evidence-backed.

## Evaluation dimensions
- problem localization accuracy
- dependency ring quality
- read scope discipline
- change scope discipline
- blast-radius control
- verification honesty
- tester/security invocation discipline
- token/scope efficiency
- absence of decorative orchestration language

## Failure signals
- role text sounds strong but scope still drifts
- builder behavior is wider than declared contract
- reviewer passes despite missing evidence
- tester/security are invoked ritualistically
- system reads or changes more than necessary without proof

## Current status
This validation matrix is no longer documentation-only.

Currently implemented and evidenced at bounded runtime level:
- Case 01: narrow single-node fix
- Case 02: local fix with adjacent dependency risk
- Case 03: bounded pseudo-code multi-file coordinated change

Not yet implemented as runnable validation classes:
- Case 04: regression-sensitive change
- Case 05: security-relevant task
- Case 06: task with justified local hardening

Current boundary:
- Cases 01-03 are proven only in bounded lab-runtime form
- this is still not evidence of repository-scale code orchestration
- planner-side read-boundary enforcement and general runtime read sandboxing remain unproven
