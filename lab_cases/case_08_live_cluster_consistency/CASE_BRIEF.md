# Case 08 Brief

## Purpose
Provide a persistent live substrate for bounded coordinated-cluster validation.

## Intended cluster
- `src/spec.json` — primary locus
- `src/generated_summary.txt` — dependent human-readable surface
- `src/generated_manifest.json` — dependent structured surface

## Intended validation value
This case should test whether the orchestration system can:
- localize one explicit primary node;
- justify a bounded local cluster;
- update all required dependent surfaces coherently;
- fail when one dependent surface becomes stale.

## Status
Persistent live substrate is now exercised by automated `scripts/selftest.py` coverage.
Runnable bounded case contract is now established through automated selftest coverage.
