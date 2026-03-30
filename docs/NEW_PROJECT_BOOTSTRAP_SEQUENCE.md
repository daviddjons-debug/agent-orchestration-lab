# New Project Bootstrap Sequence

## Purpose
Define the canonical bootstrap sequence for attaching the portable orchestration pack to a new project safely.

This document defines the minimum startup order only.
It does not claim automatic environment enforcement.

---

## Why bootstrap order matters
A portable pack is not safely attached just because reusable docs exist.
The project must be bootstrapped in the right order so that:
- reusable core is present conceptually,
- project-local truth exists before execution,
- bounded task framing exists before implementation begins,
- the environment adapter is attached on top of real project context rather than empty assumptions.

---

## Canonical bootstrap sequence

### Step 1 — choose the target environment
Select the concrete execution environment first.

Examples:
- VS Code
- Antigravity
- another supported bounded executor shell

This determines which adapter guidance applies.

### Step 2 — establish the reusable core
Attach or reference the reusable portable orchestration core.

This means the environment must have access to the stable core layers:
- contract
- activation logic
- profile model
- role behavior layer

At this step, do not inject project-specific facts into the core.

### Step 3 — create the minimum project-local overlay
Before broad work begins, create at least:
- PROJECT_SCOPE
- PROJECT_CONSTRAINTS
- PROJECT_FORBIDDEN_ZONES
- PROJECT_VALIDATION_TARGETS

If these do not exist, the project is still under-specified.

### Step 4 — classify the initial task mode
Decide which kind of project/task state exists now:
- greenfield bootstrap
- bounded extension
- narrow fix
- adjacent-risk fix
- heavy uncertainty

This prevents fake surgical behavior on a project that is still too undefined.

### Step 5 — create the bounded current-task surface
Use the bounded task prompt template to define:
- current objective
- current locus
- current allowed scope
- adjacent / verify-only surfaces
- validation target
- retriage condition

No implementation should begin before this bounded task surface exists.

### Step 6 — apply the environment adapter
Now apply the adapter logic for the selected environment.

The adapter sits on top of:
- reusable core
- project-local overlay
- bounded task surface

It must not replace any of those layers.

### Step 7 — begin bounded execution
Only now may actual implementation/evaluation work begin.

Execution must remain:
- profile-aware
- bounded by declared scope
- validation-aware
- retriage-capable when evidence breaks initial assumptions

---

## Minimum safe-attachment rule
A project should be considered safely attached to the portable pack only when all of the following are true:
- reusable core is available
- project-local overlay minimum exists
- current task has been bounded explicitly
- an adapter model has been selected

If any of these are missing, the correct state is:
- setup / triage only
- not broad execution

---

## Greenfield special case
For an empty repo or new project:
- the first bounded task is usually a bootstrap milestone, not a fake narrow fix
- forbidden zones should still be declared, even if broad architecture is not complete yet
- validation target should be milestone-based rather than defect-fix-based

This preserves discipline without pretending locality already exists.

---

## Design rules

### Required
- bootstrap order must move from reusable core to local truth to bounded task to execution
- project-local truth must exist before broad implementation
- adapters must remain thin attachment layers
- execution must begin only after bounded task framing exists

### Forbidden
- starting implementation directly from reusable core alone
- treating missing project overlay as acceptable
- treating environment attachment as proof that the project is safely bounded
- skipping bounded task framing because the environment appears powerful

---

## Next required step
After this document, the next step should be the first minimal operational portable-pack checkpoint:
- define the smallest safe on-disk project overlay skeleton,
- keep it separate from the reusable core,
- and avoid claiming automated adapter enforcement before a real bounded implementation exists.
