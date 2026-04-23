# Leo_Agents_V2 Project Bridge Model

## Purpose
Define the minimum project-local bridge that allows a target repo to use `Leo_Agents_V2` as external orchestration authority without copying the full brain into the repo.

## Core rule
A target repo should not contain a duplicated full agent pack by default.

It may contain only a thin truthful bridge layer that:
- points to the external authority pack;
- defines repo-local truth;
- defines bounded project constraints.

## Minimum project bridge surfaces
A target repo may contain:

- `PROJECT_AGENT_BRIDGE.md`
- optional truthful project-local files such as:
  - `PROJECT_SCOPE.md`
  - `PROJECT_CONSTRAINTS.md`
  - `PROJECT_FORBIDDEN_ZONES.md`
  - `PROJECT_VALIDATION_TARGETS.md`

These are project truth surfaces, not orchestration brain copies.

## Required behavior of the bridge
The bridge must state:
- external authority pack path or identity (`Leo_Agents_V2`)
- what files in the target repo are considered project truth
- what surfaces are forbidden by default
- whether donor-repo reads are allowed only by explicit declaration

## What the bridge must not become
The bridge must not become:
- a second copy of the orchestration pack
- a project-local swarm prompt set
- a dump of historical notes
- a hidden replacement for the authority pack

## Preferred project model
### Small/simple target repo
Use one compact bridge file:
- `PROJECT_AGENT_BRIDGE.md`

### Larger/long-lived target repo
Use:
- `PROJECT_AGENT_BRIDGE.md`
- plus optional truthful overlay files if needed

## Authority order when bridge is present
1. `Leo_Agents_V2` = orchestration authority
2. project-local truthful bridge/overlay files = repo truth
3. implementation files = bounded execution surface

## Anti-drift rule
Do not let a project bridge grow into a duplicated agent pack.
