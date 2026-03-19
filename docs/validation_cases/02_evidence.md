# Validation Case 02 — Evidence

## Evidence status
PASS for a bounded adjacent-dependency-risk scenario in current runtime.

## What was executed
- `python3 scripts/selftest.py`
- override run used a primary artifact and an adjacent artifact under:
  - `output/custom/result.json`
  - `output/custom/summary.txt`
- reviewer validated declared artifact contracts
- reviewer validated cross-artifact message consistency
- reviewer returned FAIL when adjacent summary consistency was broken
- planner/builder restore steps returned the run to PASS

## Positive evidence
- `output/custom/result.json` existed and satisfied declared JSON contract
- `output/custom/summary.txt` existed and satisfied declared text contract
- reviewer checked:
  - `output/custom/result.json <-> output/custom/summary.txt message consistency`
- reviewer returned PASS when both direct artifact validity and adjacent consistency held

## Negative evidence
- reviewer returned FAIL when contract drift was introduced
- reviewer returned FAIL when undeclared output drift was introduced
- builder returned FAIL when declared artifact path was outside `allowed_change_set`
- reviewer returned FAIL when adjacent summary content became stale or inconsistent relative to the JSON message

## What this PASS proves
- current runtime can distinguish direct artifact correctness from nearby adjacent-surface consistency
- adjacent-node verification is no longer only decorative documentation language
- reviewer can falsify a local scenario where the primary surface is correct but the neighboring dependent surface is not
- current runtime now supports a bounded bridge from Case 01 to Case 02

## What this PASS does not prove
- real source-code dependency analysis
- genuine discovery of adjacent dependency risk without predeclared scenario structure
- enforced `allowed_read_set` in runtime
- tester as a runnable stage for adjacent-risk cases
- full behavioral dependency validation on non-artifact engineering tasks

## Final judgment
Validation Case 02 is passed only as a bounded artifact-level adjacent-dependency scenario.

It is not yet passed as a real code-dependency surgical-runtime scenario.

