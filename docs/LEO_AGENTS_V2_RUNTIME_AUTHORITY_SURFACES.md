# Leo_Agents_V2 Runtime Authority Surfaces

## Purpose
Define the minimum canonical authority surfaces that must exist inside `Leo_Agents_V2` so the runtime pack is internally consistent.

## Problem being solved
The runtime pack cannot rely on lab-only docs that are not exported.

If launch templates or adapters require files that do not exist inside `Leo_Agents_V2`, the pack is structurally broken.

## Required runtime authority surfaces

### Minimum runtime canon
These surfaces must exist inside `Leo_Agents_V2` in some form:

- `README.md`
- `START_HERE.md`
- `docs/README.md`
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`

These do not need to be full lab copies.
They may be condensed runtime versions.

## Why they are required
Current host-facing templates already depend on:
- `docs/README.md`
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`

Therefore the runtime pack must either:
1. carry these files in condensed form, or
2. rewrite all templates to point only at exported orchestration files.

## Preferred direction
Prefer a small runtime canon over template breakage.

That means:
- include condensed runtime versions of the minimum docs surfaces;
- do not carry the full lab historical burden;
- keep the runtime pack self-consistent.

## What remains lab-only
The runtime pack should still exclude:
- session recap archives
- validation case corpus
- codex eval raw evidence
- lab scripts
- selftest harness internals
- run artifacts
- historical proof clutter

## Next task after this file
Decide whether to:
- export condensed runtime docs into `Leo_Agents_V2/docs/`, or
- rewrite all templates to become orchestration-only and docs-free.

Do not proceed to final `START_HERE.md` before this decision is fixed.
