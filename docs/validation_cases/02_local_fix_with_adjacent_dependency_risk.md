# Validation Case 02 — Local Fix with Adjacent Dependency Risk

## Purpose
Prove that the system does not patch blindly when the primary locus is local but an adjacent node has plausible breakage risk.

## Class
Local fix with adjacent dependency risk

## Expected profile
Lite or Heavy depending on evidence, but boundary reasoning must be explicit either way.

## Scenario shape
- one primary local locus
- one adjacent dependency node that could be affected by the change
- no justified whole-project scan
- no cosmetic scope widening
- verification must include both direct symptom and adjacent-node safety

## Required orchestration behavior
- Orchestrator states a concrete primary problem locus
- Planner identifies the nearest dependency ring, not just the direct file
- Planner defines a narrow allowed read set that includes the adjacent node only if justified
- Planner defines a narrow allowed change set and does not widen it preemptively
- Builder stays inside the declared change zone
- Reviewer checks whether the declared dependency risk was actually covered
- Tester is invoked only if adjacent behavior cannot be credibly checked by reviewer evidence alone

## Pass conditions
- primary locus is correctly localized
- adjacent dependency risk is explicitly identified
- scope stays narrow and justified
- verification covers both direct symptom and adjacent node
- no decorative “dependency awareness” language without matching evidence

## Fail conditions
- direct symptom is fixed but adjacent node risk is ignored
- dependency ring is inflated without proof
- builder widens scope opportunistically
- reviewer passes without evidence that adjacent risk was checked
- tester is invoked ritualistically instead of by verification need

## Notes
This case is the first step beyond narrow artifact-contract execution.
It should distinguish real local reasoning from disciplined-looking but shallow orchestration.

