# Agent Pack v2 / Surgical Edition — Rule Extraction

## Purpose
This document converts observed Codex behavior from bounded validation runs into architecture rules, contract implications, reviewer checks, and runtime/selftest implications.

---

## Case 07 — Live bounded code repair

### Observed good behavior
- Correctly identified `lab_cases/case_07_live_bounded_code/src/parser.py` as the primary locus.
- Distinguished primary parser behavior from adjacent / verify-only surfaces.
- Confirmed the defect before patching when a break was introduced.
- Applied a minimal local repair in `parser.py` only.
- Used `python3 scripts/selftest.py` as the minimum relevant validation within the dedicated Case 07 lane.
- Preserved adjacent behavior and verify-only evidence without unnecessary widening.
- Returned no-op when no defect was present.
- In later runs, narrowed the read set substantially and avoided speculative edits.

### Observed bad behavior
- Early runs read more files than strictly necessary.
- Early runs used slightly inflated false-locality language.
- Staged discipline began as narrative guidance and was later converted into explicit architecture rules.

### Architecture rules to keep
- Primary locus must be identified before repair.
- Verify-only surfaces must be treated as load-bearing when present.
- Defect confirmation must precede patching when a defect is claimed.
- No-op is valid when bounded validation shows no defect.
- Minimal relevant validation is preferred over broad sweeps.
- Widening beyond the initial local patch is allowed only on concrete evidence.

### Architecture rules to forbid
- Treating local primary success as sufficient when verify-only evidence is still unsatisfied.
- Broad repo reading when a bounded read set is sufficient.
- Refactors or helper extraction on a single-node bounded repair without evidence.
- Full validation sweep by default on a bounded case.

### Contract field impact
- `problem_locus` must identify the primary repair node.
- `dependency_ring` must include adjacent / verify-only surfaces when they are validation-bearing.
- `false_locality_risk` must be explicitly assessed.
- `allowed_read_set` should remain minimal-first as a Builder-enforced read-boundary payload, not as a claimed stage-wide sandbox.
- `allowed_change_set` should begin at the smallest sufficient repair surface.
- `verify_only_surfaces` must be explicit when present.
- Add or strengthen `expansion_trigger` semantics: widening requires concrete evidence.

### Reviewer check impact
- Reject primary-only success if verify-only surfaces remain unsatisfied.
- Require evidence that the patch stayed within `allowed_change_set`.
- Prefer targeted validation evidence over broad unspecific test runs.
- Accept no-op only when bounded validation proves no defect.
- Flag unjustified widening of read or change scope.

### Runtime / selftest impact
- Keep Case 07 as a persistent live bounded code proof lane.
- Preserve explicit checks for:
  - primary behavior
  - adjacent dependency behavior
  - verify-only completion evidence
- Preserve at least one no-op discipline path.
- Preserve at least one patch-required path.

---

## Case 03 — Coordinated cluster consistency

### Observed good behavior
- After correction, distinguished:
  - `src/spec.json` as source-of-truth
  - `src/generated_summary.txt` as the stale defect node
  - `src/generated_manifest.json` as the adjacent consistency node
- In the clean stale-summary scenario, repaired only `src/generated_summary.txt`.
- Avoided unnecessary whole-cluster rewrite.
- Used reviewer validation to confirm:
  - declared artifact validity
  - spec-summary consistency
  - spec-manifest consistency
  - absence of undeclared drift
- When the actual blocking failure differed from the expected stale-summary scenario, re-triaged to the real blocker instead of blindly repairing the assumed node.

### Observed bad behavior
- Initial runs incorrectly treated `src/spec.json` as the immediate repair locus for stale-summary failure.
- Initial runs widened `allowed_change_set` to the full trio too early.
- Initial dependency-ring framing mixed execution artifacts with domain cluster nodes.
- A polluted run caused a re-triage into plan/manifest mismatch and undeclared drift instead of the intended stale-summary scenario.

### Architecture rules to keep
- In bounded cluster tasks, distinguish:
  - source-of-truth node
  - stale defect node
  - adjacent consistency node
- Multi-file cluster does not imply multi-file patch.
- Initial repair must begin with the minimum sufficient stale node.
- Widening beyond that node requires explicit evidence.
- Reviewer-only validation is acceptable when it covers all consistency links and drift checks for the bounded case.
- If actual blocking evidence contradicts the assumed scenario, mandatory re-triage is required.

### Architecture rules to forbid
- Treating source-of-truth automatically as the immediate repair locus.
- Whole-cluster rewrite as the default response to cluster inconsistency.
- Mixing execution/report artifacts into the domain dependency ring without justification.
- Continuing with the assumed scenario when reviewer evidence shows a different blocking failure mode.

### Contract field impact
- Add or clarify explicit node roles for bounded cluster tasks:
  - `source_of_truth_node`
  - `stale_defect_node`
  - `adjacent_consistency_node`
- `allowed_change_set` should start with the minimum initial change set, not the maximal cluster set.
- `expansion_trigger` must specify what evidence justifies widening beyond the initial node.
- `dependency_ring` should describe the domain consistency ring first; execution artifacts belong in a separate context field if needed.
- Add a re-triage rule when actual blocking evidence overrides the assumed failure mode.

### Reviewer check impact
- Reject repair proposals that widen to the whole cluster without evidence.
- Validate both:
  - direct artifact contract satisfaction
  - inter-node consistency links
- Flag mismatch between assumed defect and actual reviewer-blocking defect unless re-triage is explicitly recorded.
- Accept summary-only repair when it restores cluster consistency and no broader drift exists.
- Reject undeclared drift even if cluster content appears repaired.

### Runtime / selftest impact
- Preserve the clean stale-summary Case 03 path:
  - PASS in clean cluster state
  - FAIL on stale `src/generated_summary.txt`
  - PASS after minimal summary restore
- Preserve reviewer evidence for both consistency links:
  - `src/spec.json <-> src/generated_summary.txt`
  - `src/spec.json <-> src/generated_manifest.json`
- Add or preserve a separate polluted-run / re-triage path:
  - assumed stale-summary scenario
  - actual blocking fail mode differs
  - executor must switch to evidence-driven re-triage


## Case 08 — Live bounded cluster consistency

### Observed good behavior
- Preserved one explicit primary node: `lab_cases/case_08_live_cluster_consistency/src/spec.json`.
- Preserved two explicit dependent surfaces:
  - `lab_cases/case_08_live_cluster_consistency/src/generated_summary.txt`
  - `lab_cases/case_08_live_cluster_consistency/src/generated_manifest.json`
- Validated PASS when all three declared cluster surfaces carried the same canonical message.
- Returned FAIL when only `generated_summary.txt` became stale while `spec.json` and `generated_manifest.json` remained unchanged.
- Returned PASS again after restoring the stale dependent surface.
- Kept the cluster bounded and predeclared rather than widening into unrelated repository regions.

### Observed bad behavior
- The cluster is still predeclared rather than runtime-derived.
- The case still depends on dedicated selftest scaffolding rather than generic manifest-driven execution.
- The runnable lab still does not prove automatic cluster discovery, planner-side read-boundary compatibility beyond Builder, or any stage-wide mechanically enforced read control.

### Architecture rules to keep
- Cluster consistency must be judged against one explicit canonical source-of-truth node.
- Dependent surfaces must be justified explicitly, not inferred decoratively after the fact.
- PASS requires agreement across all declared cluster surfaces, not just pairwise partial success.
- A stale dependent node must cause hard FAIL even if the primary node remains valid.
- Restoring one stale dependent surface is sufficient when that alone re-establishes full declared cluster consistency.
- Persistent live substrate validation is stronger than pseudo-code cluster validation, but it does not change the invariant.

### Architecture rules to forbid
- Treating a valid primary node as sufficient while one dependent surface is stale.
- Treating multi-surface validation as evidence of generic repository-scale dependency reasoning.
- Widening beyond the declared cluster when the bounded cluster already explains the failure.
- Rewriting the whole cluster by default when only one dependent surface is stale.

### Contract field impact
- Cluster tasks should preserve explicit source/dependent role separation:
  - `source_of_truth_node`
  - `stale_defect_node`
  - `adjacent_consistency_node`
- `dependency_ring` should reflect the declared live cluster directly.
- `allowed_change_set` should allow minimum sufficient dependent repair, not automatic whole-cluster rewrite.
- `verification_targets` should explicitly encode all required cluster links.
- `evidence_required` should require both direct artifact validity and cluster-consistency proof.

### Reviewer check impact
- Reject PASS when any declared dependent surface diverges from the canonical node.
- Validate:
  - primary node contract satisfaction
  - source-to-summary consistency
  - source-to-manifest consistency
- Reject claims of completion if cluster restoration is incomplete.
- Reject undeclared widening outside the bounded live cluster.

### Runtime / selftest impact
- Keep Case 08 as the persistent live bounded cluster-consistency proof lane.
- Preserve explicit PASS/FAIL/PASS sequencing:
  - PASS in clean cluster state
  - FAIL on stale dependent summary
  - PASS after minimal restore
- Preserve explicit proof that the stale-summary failure occurs while the other two cluster nodes remain unchanged.
- Keep Case 08 separate from generic manifest-driven runtime claims.

---

## Candidate cross-case hard requirements
- Localize before patching.
- Distinguish actual defect node from broader source or cluster context.
- Start with the smallest sufficient change surface.
- Widen only on evidence.
- Prefer minimum relevant validation.
- Accept no-op when evidence shows no defect.
- Treat verify-only and adjacent consistency surfaces as load-bearing where applicable.
- Treat persistent live substrates as stronger evidence than pseudo-code artifact simulations, without overstating them as generic repository-scale orchestration.
- Require explicit re-triage when actual blocking evidence overrides the assumed scenario.

## Candidate cross-case reviewer hard failures
- Unjustified widening of read or change set.
- Primary-only success while verify-only / adjacent consistency surfaces remain broken.
- Declaring cluster success while any declared dependent live surface diverges from the canonical node.
- Whole-cluster or multi-file repair without evidence.
- Skipping defect confirmation on a claimed defect path.
- Declaring success while undeclared drift remains.
- Ignoring actual reviewer-blocking evidence in favor of assumed scenario narrative.

---

## Mapping scaffold for contract rewrite

### Format
- Observed behavior
- Derived rule
- Contract field(s)
- Reviewer enforcement
- Runtime/selftest enforcement

### Case 07 mapping seeds
- Verify-only surface remained load-bearing even after local primary success
  - Derived rule: local success is insufficient when verify-only evidence is required
  - Contract field(s): `verify_only_surfaces`, `verification_targets`, `evidence_required`
  - Reviewer enforcement: fail if verify-only surface is unsatisfied
  - Runtime/selftest enforcement: retain Case 07 verify-only fail/pass path

- No-op was the correct outcome when bounded validation showed no defect
  - Derived rule: no-op is valid and should be explicitly accepted
  - Contract field(s): `problem_locus`, `allowed_change_set`, `verification_targets`
  - Reviewer enforcement: accept no-op only with positive bounded evidence
  - Runtime/selftest enforcement: retain Case 07 no-op validation path

### Case 08 mapping seeds
- One canonical live node stayed correct while one dependent live surface became stale
  - Derived rule: cluster completion requires all declared dependent live surfaces to remain aligned with the canonical node
  - Contract field(s): `source_of_truth_node`, `stale_defect_node`, `adjacent_consistency_node`, `verification_targets`
  - Reviewer enforcement: fail if any declared live dependent surface diverges from the canonical message
  - Runtime/selftest enforcement: retain Case 08 stale-summary fail path

- Minimal dependent restore returned the live cluster to PASS
  - Derived rule: bounded cluster restoration should begin with the minimum sufficient stale dependent repair
  - Contract field(s): `allowed_change_set`, `expansion_trigger`, `evidence_required`
  - Reviewer enforcement: reject whole-cluster rewrite when single-node restoration is sufficient
  - Runtime/selftest enforcement: retain Case 08 minimal-restore pass path


### Case 03 mapping seeds
- Source-of-truth node differed from the stale defect node
  - Derived rule: cluster tasks must distinguish source, stale, and adjacent consistency nodes
  - Contract field(s): `source_of_truth_node`, `stale_defect_node`, `adjacent_consistency_node`
  - Reviewer enforcement: reject repair locus conflation when evidence shows stale dependent failure
  - Runtime/selftest enforcement: retain clean stale-summary fail/pass path

- Summary-only repair restored cluster consistency without whole-cluster rewrite
  - Derived rule: multi-file cluster does not imply multi-file patch
  - Contract field(s): `allowed_change_set`, `expansion_trigger`
  - Reviewer enforcement: reject unjustified whole-cluster widening
  - Runtime/selftest enforcement: retain stale-summary minimal-restore path

- Actual reviewer-blocking failure overrode the assumed scenario in the polluted run
  - Derived rule: assumed failure mode must yield to evidence-driven re-triage
  - Contract field(s): `blockers_or_uncertainties`, `escalation_trigger`, `verification_targets`
  - Reviewer enforcement: flag mismatch between assumed scenario and actual blocking defect unless re-triage is explicit
  - Runtime/selftest enforcement: preserve polluted-run / re-triage branch

