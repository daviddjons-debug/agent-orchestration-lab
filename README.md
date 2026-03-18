# Agent Orchestration Lab

## Purpose
This repository is a controlled sandbox to verify whether multi-agent orchestration is real, observable, falsifiable, and reproducible rather than simulated.

## Operating rule
Do not jump to a large system first.
Start with the smallest end-to-end orchestration that can be tested, broken, reviewed, and restored.

## Current baseline
The lab now proves a contract-driven orchestration harness with:
- explicit role separation;
- visible handoff artifacts;
- planner-to-builder execution through structured `02_plan.json`;
- multi-file artifact generation from manifest-declared outputs;
- reviewer validation against both plan contract and output artifacts;
- reproducible negative tests and recovery.

## What this lab does not prove
This repository does not yet prove:
- advanced autonomous reasoning;
- high-quality decomposition on complex real-world tasks;
- general agent intelligence.

It proves orchestration mechanics and contract enforcement.
