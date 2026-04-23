# Leo_Agents_V2 Workspace Composition Model

## Purpose
Define how VS Code workspaces should be composed when using `Leo_Agents_V2` as the orchestration authority.

## Core rule
Do not open the whole `Developer` directory as the default Codex workspace.

Use a bounded multi-root workspace instead.

## Standard workspace modes

### Mode 1 — authority + target
Use for normal project work.

Roots:
1. `Leo_Agents_V2`
2. target repo

Meaning:
- `Leo_Agents_V2` = orchestration authority
- target repo = bounded execution surface

### Mode 2 — authority + target + donor
Use only when explicitly borrowing from another project.

Roots:
1. `Leo_Agents_V2`
2. target repo
3. donor repo

Meaning:
- `Leo_Agents_V2` = orchestration authority
- target repo = write surface
- donor repo = read-only surface by explicit declaration only

## What not to do
Do not use:
- whole `Developer` as the main workspace root
- multiple unrelated target repos at once without declared roles
- donor repos as silent default context
- project-local legacy packs as orchestration authority

## Required task declaration in cross-project mode
When donor repo is present, the task must explicitly state:
- target repo
- donor repo
- allowed target read scope
- allowed target change scope
- allowed donor read scope
- donor is read-only unless explicitly changed by a separate bounded task

## Authority order in workspace mode
1. `Leo_Agents_V2`
2. truthful project-local bridge/overlay files
3. target implementation files
4. donor repo only when explicitly declared and read-only by default

## Anti-drift rule
Workspace convenience must not become authority confusion.
