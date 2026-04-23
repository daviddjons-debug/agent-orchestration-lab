# Leo_Agents_V2 Extraction Plan

## Purpose
Define how to extract a clean runtime pack (`Leo_Agents_V2`) from the lab without dragging R&D noise, stale canon, or validation-only artifacts into the battle-ready package.

## Goal
The runtime pack should become:
- the single portable orchestration brain for real projects;
- separate from the lab;
- clean, minimal, and versionable;
- usable across target repos without copying the full lab into each project.

## What the lab remains
`agent-orchestration-lab` remains:
- the R&D surface;
- the validation surface;
- the falsification surface;
- the place for experiments, recaps, and evidence.

The lab is **not** the battle-ready pack itself.

## What Leo_Agents_V2 should become
`Leo_Agents_V2` should become:
- the battle-ready portable runtime pack;
- the default orchestration authority for real projects;
- minimal enough to avoid noise and duplication;
- stable enough to use across multiple target repos.

## Include in Leo_Agents_V2
Only material that is load-bearing for runtime use:

### Control-plane core
- orchestration routing layer
- task class defaults
- profiles layer
- modules layer
- module activation matrix
- module trigger matrix

### Runtime skills
- module-to-skill mapping
- review false-locality skill
- testing behavior evidence skill
- external second-opinion contradiction skill
- browser visible-behavior skill
- security boundary exposure skill

### Host-facing invocation surfaces
- generic bounded invocation
- generic launch template
- audit launch template
- browser/UI launch template
- security launch template
- external target repo invocation

### Minimal entry surfaces
- runtime-pack README
- START_HERE / first-read entry
- compact reading map

## Do not include in Leo_Agents_V2
### Lab-only / R&D-only material
- old session recap archives
- validation-case corpus
- raw codex eval artifacts
- long-form experiment history
- obsolete canon snapshots
- duplicate transitional files
- anything kept only to prove history rather than drive runtime use

### Not default runtime surfaces
- broad lab scripts
- selftest harness internals
- generated run artifacts
- frozen checkpoint clutter

## Likely structure of Leo_Agents_V2
- `README.md`
- `START_HERE.md`
- `orchestration/`
  - `README.md`
  - `router/`
  - `profiles/`
  - `modules/`
  - `skills/`
  - `adapters/`

## Project-side model after extraction
Target repos should contain:
- project code/content only
- optional truthful project-local overlay files
- no duplicated full agent brain by default

## Authority model after extraction
1. `Leo_Agents_V2` = orchestration authority
2. truthful target-repo local files = project truth
3. target implementation files = bounded execution surface

Do not let legacy local packs override `Leo_Agents_V2`.

## Next extraction tasks
1. define the exact file list to export from the lab
2. define the exact file list to exclude
3. define the minimal `START_HERE.md`
4. define the runtime-pack `README.md`
5. define the project bridge model for target repos
6. define recommended VS Code workspace composition for:
   - authority pack + target repo
   - authority pack + target repo + donor repo
