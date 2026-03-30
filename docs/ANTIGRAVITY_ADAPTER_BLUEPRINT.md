# Antigravity Adapter Blueprint

## Purpose
Define the canonical environment adapter for attaching the portable orchestration pack to Antigravity-style agent execution.

This document defines attachment strategy only.
It does not claim that Antigravity automatically enforces the pack in every context.

---

## Why Antigravity matters
- it represents a more execution-heavy environment than plain doc-level orchestration
- it is a realistic target for bounded task execution under the same portable core
- it tests whether the reusable orchestration brain can remain stable outside VS Code-only assumptions

---

## Adapter goal
Attach the portable orchestration pack to Antigravity in a way that:
- preserves the same reusable core used in other environments
- keeps project-local overlay separate from adapter-specific guidance
- forces bounded-task framing before broad execution begins
- prevents Antigravity-specific execution behavior from being mistaken for portable core truth

---

## Attachment layers in Antigravity

### 1. Global reusable layer
The same reusable portable core should remain authoritative here too.

Carries:
- contract semantics
- activation and escalation logic
- role behavior layer
- bounded orchestration rules

### 2. Project-local overlay
Antigravity execution must still consult project-local overlay minimum before broad work begins:
- PROJECT_SCOPE
- PROJECT_CONSTRAINTS
- PROJECT_FORBIDDEN_ZONES
- PROJECT_VALIDATION_TARGETS

### 3. Bounded execution task surface
Antigravity should receive a bounded current-task surface that references:
- the reusable core
- the local overlay
- the exact current task locus and scope

This surface must not be replaced by vague high-agency prompting.

---

## Intended Antigravity operating model

### Mode A — bounded executor under reusable core
Antigravity acts as an execution-heavy environment constrained by the same orchestration brain.

Use when:
- a current task is already localized enough for bounded execution
- the project overlay is present and truthful

### Mode B — bounded evaluator/executor loop
Antigravity may also act as an external evaluator or patch executor under strict read/change boundaries.

Use when:
- the task is a falsifiable current-repo target
- minimal patch / no-patch discipline is required

### Preferred model
The preferred default is:
- reusable portable core
- plus project-local overlay
- plus one bounded current-task surface

This keeps Antigravity inside the same orchestration discipline rather than letting it invent its own architecture path.

---

## Adapter rules

### Required
- keep portable core separate from Antigravity-specific execution wording
- require truthful project-local overlay before broad task execution
- require bounded-task framing before implementation
- preserve profile-aware routing instead of defaulting to maximal agency
- prefer minimal patch / no-patch discipline when the task is current-repo bounded work

### Forbidden
- treating Antigravity-specific execution style as portable core truth
- letting execution-heavy defaults bypass the reusable contract
- allowing project-local overlays to fork core semantics
- using broad repository exploration as a substitute for bounded task localization
- assuming adapter attachment is automatically enforced without checking actual environment behavior

---

## Current boundary
What this adapter blueprint defines now:
- the canonical Antigravity attachment model
- how reusable core, project overlay, and bounded task surface should relate

What it does not yet define:
- exact Antigravity UI/runtime configuration steps
- automatic enforcement guarantees
- a finalized on-disk `orchestration/adapters/antigravity.md` implementation

---

## Next required step
After this document, the next step should be the first minimal operational portable-pack checkpoint:
- define the smallest safe adapter-side attachment artifact for Antigravity,
- keep it thin relative to reusable core, project overlay, and bounded task surface,
- and avoid claiming automatic environment enforcement before a real bounded implementation exists.
