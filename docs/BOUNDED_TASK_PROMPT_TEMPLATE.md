# Bounded Task Prompt Template

## Purpose
Define the canonical bounded task prompt surface shared across environment adapters.

This template is not the reusable core itself.
It is the current-task attachment layer that binds:
- the portable core,
- the project-local overlay,
- and the exact current task.

---

## Why this layer is required
Reusable core + project overlay are not enough by themselves.
A concrete task still needs a bounded current-task instruction surface so that the executor does not invent:
- a wider locus,
- broader reads,
- broader writes,
- fake completion criteria,
- or a different task than the one actually requested.

---

## Canonical template fields

### 1. Task objective
- what must be achieved now
- the expected bounded end state

### 2. Task classification
- greenfield bootstrap
- bounded extension
- narrow fix
- adjacent-risk fix
- heavy uncertainty

### 3. Problem/task locus
- primary target node or surface
- why this is the current best locus
- current locality confidence

### 4. Allowed working scope
- allowed read set or bounded read contour
- allowed change set
- explicit forbidden zones

### 5. Adjacent / verify-only surfaces
- known adjacent nodes
- verify-only surfaces if applicable
- surfaces that must remain unchanged

### 6. Validation target
- what evidence is required before claiming completion
- minimum acceptable validation
- conditions for NO_PATCH_REQUIRED when applicable

### 7. Escalation / retriage rule
- when the executor must stop narrow execution
- when the executor must declare retriage instead of widening silently

---

## Canonical bounded task prompt skeleton

Use the portable orchestration core plus the project-local overlay for this project.

Current task objective:
- <fill>

Task class:
- <fill>

Primary current locus:
- <fill>

Locus confidence:
- <high / medium / low>

Allowed read scope:
- <fill>

Allowed change scope:
- <fill>

Forbidden zones:
- <fill>

Adjacent / verify-only surfaces:
- <fill>

Required validation evidence:
- <fill>

Stop and retriage when:
- <fill>

Special rule:
- prefer the smallest sufficient patch;
- prefer NO_PATCH_REQUIRED when no real mismatch/defect is proven;
- do not widen scope without explicit evidence.

---

## Design rules

### Required
- current-task prompt must stay thinner than the reusable core
- task prompt must reference project-local overlay rather than replacing it
- task prompt must define bounded scope before implementation begins
- task prompt must state validation target before completion claims

### Forbidden
- using a vague task prompt as a substitute for overlay truth
- silently widening beyond the declared task contour
- restating the entire reusable core in every task prompt
- claiming completion without the declared evidence

---

## Adapter usage

### VS Code
Use this as the bounded current-task attachment layer on top of:
- reusable user-level orchestration brain
- project-local overlay

### Antigravity
Use this as the bounded execution/evaluation surface on top of:
- reusable portable core
- project-local overlay

---

## Current boundary
This template defines the canonical task-level attachment surface.
It does not yet define an automated loader or UI-specific integration path.

---

## Next required step
After this document, the next canonical layer should define the new-project bootstrap sequence:
- what to create first,
- what to fill in first,
- and when the portable pack may be considered safely attached.
