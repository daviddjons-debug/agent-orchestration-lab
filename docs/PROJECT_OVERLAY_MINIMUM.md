# Project Overlay Minimum

## Purpose
Define the minimum required project-local overlay that must exist before the portable orchestration pack can be attached safely to a new project.

This document defines the minimum project-local inputs only.
It does not define environment adapters or claim automatic enforcement.

---

## Why this layer exists
A portable orchestration pack must not infer core project truth from nothing.
Without a minimal project-local overlay, the pack risks:
- fake locality assumptions
- uncontrolled scope drift
- unsafe reads across irrelevant surfaces
- pretending that a greenfield repo and a mature repo should be handled identically
- mixing reusable core rules with project-specific facts

---

## Minimum required project-local files

### 1. `PROJECT_SCOPE.md`
Must define:
- project objective
- current task mode: greenfield / bounded extension / narrow fix / adjacent-risk fix / heavy uncertainty
- expected end state
- explicitly out-of-scope surfaces

### 2. `PROJECT_CONSTRAINTS.md`
Must define:
- technical constraints
- product/domain constraints
- environment/tool constraints
- cost/scope discipline requirements if stricter than core defaults

### 3. `PROJECT_FORBIDDEN_ZONES.md`
Must define:
- files/directories/surfaces that must not be touched without explicit escalation
- protected architecture areas
- non-target systems or repos that are out of bounds

### 4. `PROJECT_VALIDATION_TARGETS.md`
Must define:
- the minimum load-bearing validation surfaces for the current project
- adjacent or verify-only surfaces when known
- acceptance evidence expected before claiming completion

---

## Minimum attachment rule
The portable pack should not be attached to a new project unless these four project-local files exist in at least a minimal truthful form.

If they are missing, the correct behavior is not to improvise hidden project truth.
The correct behavior is to treat the project as under-specified and remain in a bounded setup/triage mode.

---

## Greenfield exception
For a truly empty or greenfield project, the overlay may begin in a reduced form, but it must still define:
- what is being built
- what is explicitly not being built yet
- what counts as the first bounded milestone
- what areas are forbidden until architecture is clarified

This prevents fake surgical behavior on an empty repo while preserving scope discipline.

---

## Design rules

### Required
- project-local overlay must stay separate from reusable core
- project-local facts must be explicit rather than inferred silently
- forbidden zones must be written down before broad implementation begins
- validation targets must be declared before completion claims

### Forbidden
- storing reusable core rules inside project overlay files
- letting project overlays redefine profile logic or contract semantics
- treating missing local context as permission to scan or mutate broadly
- claiming project readiness for the portable pack without minimum overlay truth

---

## Current boundary
What this document defines now:
- minimum project-local overlay contents
- minimum attachment preconditions

What it does not yet define:
- the exact future on-disk `orchestration/overlays/project/` implementation
- how a specific adapter loads these files in VS Code, Antigravity, or other environments

---

## Next required step
After this document, the next step should be the first minimal operational portable-pack checkpoint:
- define the smallest safe on-disk project overlay skeleton,
- keep it separate from reusable core truth,
- and avoid treating blueprint-level adapter guidance as implemented attachment behavior.
