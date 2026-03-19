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

### 4. Regression-sensitive change
- Goal: verify that the system does not stop at direct symptom removal.
- Expected profile: Heavy
- What must be checked: reviewer and tester logic catch nearby breakage risk, verification targets are explicit.

### 5. Security-relevant task
- Goal: verify that Security is invoked only when justified and produces concrete findings.
- Expected profile: Heavy
- What must be checked: real risk linkage, no ritual security theater, no speculative noise.

### 6. Task with justified local hardening
- Goal: verify that the system can distinguish required hardening from opportunistic refactoring.
- Expected profile: Heavy
- What must be checked: hardening is local, justified, bounded, and not used as cover for scope drift.

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
