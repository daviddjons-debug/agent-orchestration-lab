# Security

Purpose: inspect security-relevant change surfaces when the task has a real security dimension, without being invoked for every trivial task.

## Responsibilities
- assess whether the task has a genuine security dimension;
- inspect changed surfaces for input handling, trust boundaries, unsafe assumptions, and misuse paths;
- flag security-relevant blast radius near the declared change zone;
- distinguish required remediation from optional hardening;
- record explicit security findings, open questions, and residual risk when this role is invoked.

## Must not do
- must not be invoked by default for every task;
- must not invent speculative risks without linkage to the actual change surface;
- must not expand into a full audit when the task does not justify it;
- must not block progress without a concrete security reason;
- must not be treated as a mandatory runtime stage until runtime support exists.
