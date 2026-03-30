# Portable Pack Blueprint

## Purpose
Define the target portable orchestration pack shape that can sit above different LLM / agent environments without changing the bounded orchestration core itself.

This document is a design-layer blueprint.
It does not claim that the adapter/runtime layer is already implemented.

---

## Goal
Build a portable orchestration pack that:
- preserves the bounded Surgical Edition core;
- can be attached to different environments as an instruction / policy layer;
- separates canonical contract logic from environment-specific adapter logic;
- supports future project bootstrapping without rewriting the core for each new repo.

---

## Non-goals
This blueprint does not define:
- a new runtime framework;
- a new role pack architecture;
- automatic enforcement guarantees across all external tools;
- repository-scale orchestration proof.

It is only the packaging and attachment blueprint.

---

## Canonical portable pack layers

### 1. Core policy layer
Files that define portable orchestration semantics independent of environment:
- `docs/HANDOFF_CONTRACT.md`
- `docs/ACTIVATION_MATRIX.md`
- `docs/EXECUTION_PROFILES.md`
- `docs/BASELINE.md`
- `docs/VALIDATION_MATRIX.md`
- `docs/agent_pack_v2_rule_extraction.md`

### 2. Role behavior layer
Role-specific behavior docs aligned to the contract:
- `docs/roles/orchestrator.md`
- `docs/roles/planner.md`
- `docs/roles/builder.md`
- `docs/roles/reviewer.md`
- `docs/roles/tester.md`
- `docs/roles/security.md`

### 3. Evidence / validation layer
Proof surfaces that must remain separate from policy truth:
- `docs/validation_cases/`
- `docs/session_recaps/`
- `docs/codex_eval/`
- `docs/runs/`

### 4. Environment adapter layer
Not yet implemented in canon.
This future layer should define how the same portable pack is attached to:
- VS Code
- Antigravity
- Codex-like external executor environments
- other supported LLM/agent shells

### 5. Project-local overlay layer
Not yet implemented in canon.
This future layer should contain project-specific additions such as:
- local project objective
- domain constraints
- forbidden zones
- architecture notes
- project-specific validation targets

The project-local overlay must not rewrite the core policy layer.

---

## Target packaging model

### Global reusable pack
A reusable top-level orchestration pack that remains stable across projects.

### Project-local overlay
A minimal project-specific layer added on top of the global pack.

### Adapter-specific attachment
A thin environment-specific attachment method that tells a concrete tool how to consume:
- the global reusable pack
- the project-local overlay

---

## Design rules

### Keep
- one bounded orchestration core
- one canonical contract
- one activation logic
- one role pack aligned to the contract
- project-local additions separated from portable core
- raw evidence layers separated from policy truth

### Forbid
- duplicating the core contract per environment
- mixing raw evaluation evidence into canonical policy
- treating environment-specific glue as architecture truth
- letting project-local overlays silently mutate the portable core
- claiming adapter enforcement before it is proven in the target environment

---

## Current boundary
What exists now:
- bounded orchestration core
- canonical docs for contract / profiles / validation
- raw external evaluation evidence layer
- documentation map

What does not yet exist:
- canonical environment adapter docs
- canonical project-local overlay format
- implemented portable pack directory layout
- proven multi-environment attachment workflow

---

## Next required step
After this blueprint, the next document should define:
- the canonical directory layout for the portable pack;
- which files are global reusable core;
- which files are environment adapters;
- which files are project-local overlays.
