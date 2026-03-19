# Agent Orchestration Lab

## Purpose
This repository is a controlled sandbox to verify whether multi-agent orchestration is real, observable, falsifiable, and reproducible rather than simulated.

## Operating rule
Do not jump to a large system first.
Start with the smallest end-to-end orchestration that can be tested, broken, reviewed, and restored.

## Current runnable baseline
The lab currently proves a minimal 4-role contract-driven pipeline with:
- explicit role separation;
- visible handoff artifacts;
- planner-to-builder execution through structured `02_plan.json`;
- multi-file artifact generation from manifest-declared outputs;
- reviewer validation against both plan contract and output artifacts;
- reproducible negative tests and recovery.

The runnable baseline roles are:
- orchestrator
- planner
- builder
- reviewer

## What this lab does not yet prove
This repository does not yet prove:
- advanced autonomous reasoning;
- strong decomposition on complex real-world tasks;
- surgical debugging behavior;
- dependency-aware patch planning;
- blast-radius control across realistic code changes;
- tester and security participation as real execution roles.

It currently proves orchestration mechanics and contract enforcement.

## Current transition
The next stage is not to inflate the system with more roles immediately.
The next stage is to transform the existing 4 runnable roles from a simple artifact-contract pipeline into a surgical contract baseline while preserving the current runnable harness.

That means:
- keep the runnable 4-role pipeline intact;
- rewrite role behavior around triage, boundaries, dependency awareness, and minimal change discipline;
- only add tester and security after the surgical contract model is coherent.
