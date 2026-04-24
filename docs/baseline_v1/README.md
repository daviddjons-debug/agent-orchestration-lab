# Agent Orchestration Lab

## Archive/evidence status
`agent-orchestration-lab` is the R&D / validation / evidence lab.
`Leo_Agents_V2` is the active exported authority/runtime pack for real project orchestration.

This `baseline_v1` directory is historical baseline evidence for early lab orchestration mechanics.
It is not current Leo authority and should not be used as the active runtime contract.
This marker does not physically archive, move, or delete any baseline artifact.

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
