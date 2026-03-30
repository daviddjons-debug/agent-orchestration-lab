# VS Code Usage Proof Card

## Purpose
Show the minimum bounded way the VS Code attachment artifact should be used with:
- the reusable orchestration core
- the project-local overlay
- the bounded current-task surface

This is a usage proof card, not an automation claim.

## Required preconditions
Before broad execution in VS Code:
1. reusable core truth is available through the canonical docs
2. project overlay exists under `orchestration/overlays/project/`
3. current task is explicitly bounded

If any of these are missing, the correct mode is:
- setup / triage only
- not broad execution

## Minimum bounded usage sequence
1. Read the reusable core guidance.
2. Read the project overlay minimum.
3. Create or attach a bounded current-task prompt.
4. Only then begin task execution in VS Code.

## Minimum bounded task fields
The task surface must declare:
- objective
- task class
- current locus
- allowed read scope
- allowed change scope
- forbidden zones
- validation evidence
- retriage condition

## Proof boundary
This card proves only that:
- a thin VS Code attachment path now exists on disk
- the adapter artifact is connected to overlay and bounded task usage
- safe execution is still conditional on explicit task bounding

This card does not prove:
- automatic VS Code enforcement
- extension-specific implementation
- UI-level configuration behavior
- full environment integration

## Current repo linkage
- adapter blueprint: `docs/VSCODE_ADAPTER_BLUEPRINT.md`
- adapter artifact: `orchestration/adapters/vscode.md`
- project overlay: `orchestration/overlays/project/`
- bounded task template: `docs/BOUNDED_TASK_PROMPT_TEMPLATE.md`
