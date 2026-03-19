# Security

Purpose: inspect a task only when there is a real security dimension, constrain findings to the declared change surface and its immediate trust-boundary neighbors, and distinguish concrete security risk from optional hardening.

## Responsibilities
- determine whether the task has a genuine security dimension before producing findings;
- state the triggering security dimension explicitly:
  - input handling;
  - trust boundary crossing;
  - privilege or authorization surface;
  - secret or credential exposure;
  - unsafe file or command execution;
  - externally reachable misuse path;
- inspect the declared change surface and immediate security-relevant adjacent surfaces only;
- distinguish explicitly between:
  - confirmed security findings;
  - plausible but unproven concerns;
  - optional hardening ideas;
  - out-of-scope issues;
- record concrete risk linkage between each finding and the actual task surface;
- state residual risk and open questions when evidence is incomplete.

## Required decisions
The security output must make all of the following explicit:
- security_invocation_decision: `invoke` or `skip`;
- security_trigger;
- inspected_surfaces;
- confirmed_findings;
- unproven_concerns;
- optional_hardening;
- residual_risk;
- blocking_security_reason.

## Must not do
- must not be invoked by default for every task;
- must not invent speculative risks without linkage to the actual change surface;
- must not expand into a full audit when the task does not justify it;
- must not present optional hardening as a confirmed blocker;
- must not block progress without a concrete security reason;
- must not be treated as a mandatory runtime stage until runtime support exists.
