# VS Code Attachment Artifact

## Status
This is a thin adapter-side operational artifact for VS Code.
It does not claim automatic enforcement.
It does not replace the reusable core, project overlay, or bounded task surface.

## Intended use
Use this artifact when attaching the portable orchestration pack to VS Code as the first target environment.

## Attachment order
1. Keep the reusable orchestration core as the primary stable guidance layer.
2. Require the project-local overlay before broad project work begins.
3. Require a bounded current-task surface before implementation.
4. Use VS Code as the execution environment only after those layers are present.

## Required inputs
- reusable core truth from the canonical docs
- project-local overlay under `orchestration/overlays/project/`
- bounded current-task framing for the exact task

## Operational rule
In VS Code, do not treat environment attachment as proof of safe execution.
Safe execution begins only when:
- overlay minimum exists
- current task is explicitly bounded
- forbidden zones are known
- validation expectations are declared

## What this artifact does not claim
- no automatic adapter enforcement
- no UI-specific configuration guarantee
- no extension-specific implementation
- no migrated core/roles under `orchestration/core` or `orchestration/roles`

## Current boundary
This artifact is a first thin operational bridge between:
- the VS Code adapter blueprint
- the materialized project overlay skeleton
- and future bounded task attachment
