# Agent Orchestration Lab

## Purpose
This repository is a controlled sandbox for building and checking a bounded orchestration system that is observable, falsifiable, and reproducible rather than narrative-driven.

## Core operating rule
Do not start from maximum agent count or maximum ceremony.
Start from the smallest justified execution path that can still localize the problem, bound scope, apply a minimal change, and verify completion honestly.

## Current repository state
The repository now contains three distinct layers:

1. **Operational core**
   - handoff contract
   - activation / execution profile logic
   - bounded runtime scripts
   - validation matrix
   - role behavior docs aligned to the bounded contract

2. **Portable / design layer**
   - portable pack blueprint and layout
   - project overlay minimum
   - bounded task prompt template
   - adapter blueprints for environments such as VS Code and Antigravity

3. **Evidence / archive layer**
   - validation cases
   - generated run artifacts
   - session recaps
   - external evaluator artifacts

## Current runnable runtime
The runnable harness is still the bounded 4-role runtime centered on:
- orchestrator
- planner
- builder
- reviewer

This runtime is supported by:
- `scripts/orchestrator.py`
- `scripts/planner.py`
- `scripts/builder.py`
- `scripts/reviewer.py`
- `scripts/run_pipeline.py`
- `scripts/runtime_contract.py`
- `scripts/selftest.py`

## What is currently proven
The repository currently proves a bounded orchestration core with:
- explicit contract-driven handoff;
- profile-aware activation logic at the policy/documentation layer;
- Builder boundary enforcement;
- reviewer failure on contract drift and undeclared drift;
- validation cases for bounded locality, adjacent verification, and consistency logic;
- a materialized but still bounded portable / VS Code attachment seam.

## What is not yet proven
The repository does not yet prove:
- universal repo-scale surgical orchestration on arbitrary codebases;
- full live interactive enforcement inside host environments;
- complete Heavy-path maturity;
- broad autonomous decomposition without bounded evidence.

## Where to start
- Read `docs/README.md` first for the current documentation map.
- Treat `docs/HANDOFF_CONTRACT.md`, `docs/ACTIVATION_MATRIX.md`, `docs/EXECUTION_PROFILES.md`, `docs/BASELINE.md`, and `docs/VALIDATION_MATRIX.md` as the operational spine.
- Treat portable/adapters as secondary until current runtime truth is clear.
