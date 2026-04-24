# Orchestration Layer

## Lab-only status
`agent-orchestration-lab` is the R&D / validation / evidence lab.
`Leo_Agents_V2` is the active exported authority/runtime pack for real project orchestration.

This lab `orchestration/` directory is a lab R&D / export-source surface.
It is not active Leo authority, and it must not override `/Users/leonidgolub/Developer/Leo_Agents_V2` when that exported pack is present.
This marker does not physically archive, move, or delete any orchestration file.

## Purpose
This directory is the current portable/operator-facing orchestration surface.

## Current contents

### Materialized now
- `router/` — operator-facing routing layer for task classification and default path selection
- `profiles/` — operator-facing execution-profile surface
- `modules/` — functional module layer, activation matrix, and trigger matrix
- `skills/` — narrow operational playbooks attached to specific modules and failure modes
- `overlays/project/` — minimal project-local overlay surfaces
- `adapters/` — thin VS Code-side attachment and verification artifacts
- `tasks/` — bounded task example material for adapter usage

### Current role of this directory
This directory is not the full reusable orchestration core.
It is the current portable attachment layer and working surface for operator-facing orchestration packaging.

It now contains the first materialized v3-style portable execution spine:
- routing
- profiles
- modules
- skills

## Not yet materialized here
- reusable core/runtime migration into `orchestration/`
- skill activation rules beyond the current bounded mapping layer
- host-specific skill invocation patterns
- automatic host/environment enforcement

## Working interpretation
- The operational runtime truth still lives primarily in `docs/` and `scripts/`.
- `orchestration/` is the correct place for portable/operator-facing expansion.
- The current v3-style portable spine is present, usable in bounded form, and still incomplete.
