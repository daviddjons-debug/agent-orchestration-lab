# VS Code Adapter Blueprint

## Purpose
Define the first canonical environment adapter for attaching the portable orchestration pack to VS Code.

This document defines attachment strategy only.
It does not claim that VS Code automatically enforces the pack in every context.

---

## Why VS Code comes first
- it is the primary working environment for this project
- the user-level custom agent model already exists conceptually in VS Code history
- VS Code is the most realistic first target for a portable pack attachment model

---

## Adapter goal
Attach the portable orchestration pack to VS Code in a way that:
- preserves the reusable core
- keeps project-local overlay separate
- avoids copying architecture truth into ad hoc prompts repeatedly
- makes the pack the default working discipline for new projects

---

## Attachment layers in VS Code

### 1. Global reusable layer
The reusable portable core should exist independently of any one project.
In VS Code terms, this corresponds conceptually to user-level reusable orchestration guidance.

Carries:
- core contract and profile logic
- role behavior layer
- stable orchestration rules

### 2. Project-local overlay
Each project must supply its own overlay minimum before safe attachment:
- PROJECT_SCOPE
- PROJECT_CONSTRAINTS
- PROJECT_FORBIDDEN_ZONES
- PROJECT_VALIDATION_TARGETS

### 3. Session/task prompt surface
A concrete task still needs a bounded current-task instruction surface.
This surface must reference:
- the reusable core
- the project-local overlay
- the current bounded task

It must not replace the reusable core with ad hoc one-off prompting.

---

## Intended VS Code operating model

### Mode A — user-level reusable brain
The orchestration pack is primarily attached as a reusable user-level working discipline.

Use when:
- the same orchestration logic should carry across multiple repos
- the project only needs local overlay additions

### Mode B — project-attached overlay
The repo carries project-local overlay docs that the reusable brain must consult before acting.

Use when:
- the project has strong local constraints
- forbidden zones or validation targets differ materially from defaults

### Preferred combined model
The strongest default model is:
- reusable user-level orchestration brain
- plus project-local overlay inside the repo

This avoids rewriting the core per project while still grounding decisions locally.

---

## Adapter rules

### Required
- keep reusable core separate from project-local overlay
- require project overlay minimum before broad project work begins
- force bounded-task framing before implementation
- preserve profile-aware routing instead of always-heavy execution

### Forbidden
- copying the full core into every repo as uncontrolled duplicates
- letting project-local prompts silently override reusable contract semantics
- treating VS Code-specific attachment wording as portable core truth
- assuming VS Code always applies the pack automatically without checking actual configuration

---

## Current boundary
What this adapter blueprint defines now:
- the canonical VS Code attachment model
- the distinction between reusable brain and project-local overlay
- a first thin on-disk adapter-side artifact at `orchestration/adapters/vscode.md`
- a thin bounded usage proof card at `orchestration/adapters/vscode_usage.md`
- a bounded verification note at `orchestration/adapters/vscode_verification.md`

What it does not yet define:
- exact UI/configuration steps for a specific VS Code extension or agent shell
- automatic enforcement guarantees
- extension-specific implementation proof
- UI-level attachment verification in a live VS Code environment

---

## Next required step
After this document, the next step should be the first minimal operational portable-pack checkpoint:
- define the smallest safe adapter-side attachment artifact for VS Code,
- keep it thin relative to reusable core, project overlay, and bounded task surface,
- and avoid claiming automatic environment enforcement before a real bounded implementation exists.
