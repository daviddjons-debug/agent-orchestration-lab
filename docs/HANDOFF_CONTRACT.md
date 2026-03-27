# Handoff Contract

## Purpose
Define one shared contract language for orchestrator, planner, builder, reviewer, tester, and security.

Its job is to prevent scope drift, false-local fixes, uncontrolled reads, silent multi-file widening, and fake completion claims.

If required fields are missing, ambiguous, or contradictory, the next role must stop and escalate.

## Core rule
The system does not start from “finish fast”.
It starts from:
1. where the most likely problem locus is,
2. what immediate dependencies surround it,
3. what can be read,
4. what can be changed,
5. what must remain untouched,
6. what must be verified before completion can be claimed.

No role may silently widen scope.

## Required fields
- task_class
- objective
- expected_end_state
- problem_locus
- locus_confidence
- symptom
- root_cause_hypothesis
- false_locality_risk
- dependency_ring
- allowed_read_set (Builder-enforced read-boundary payload)
- allowed_change_set
- forbidden_zone
- acceptance_criteria
- verification_targets
- evidence_required
- blockers_or_uncertainties
- path_decision
- escalation_trigger

## Conditional fields
- verify_only_surfaces
- excluded_neighbors
- source_of_truth_node
- stale_defect_node
- adjacent_consistency_node
- expansion_trigger
- retriage_required_when_actual_blocker_differs
- patch_strategy
- change_rationale
- reviewer_focus
- tester_focus
- security_focus

## Profile-specific field requirements

### baseline
`baseline` is the runnable compatibility label for the Direct profile.

In the runnable 4-role runtime, baseline still carries some compatibility-form contract fields that are not yet enforced uniformly across every stage.

Baseline must define at minimum:
- task_class
- objective
- expected_end_state
- problem_locus
- locus_confidence
- symptom
- root_cause_hypothesis
- false_locality_risk
- dependency_ring
- allowed_read_set (Builder-enforced read-boundary payload)
- allowed_change_set
- forbidden_zone
- acceptance_criteria
- verification_targets
- evidence_required
- blockers_or_uncertainties
- path_decision
- escalation_trigger

Baseline may omit conditional fields unless the task evidence already requires them.

### lite
Lite must define everything required by baseline, plus any field needed to control bounded adjacent verification or scope protection.

Lite should make explicit when present:
- verify_only_surfaces
- excluded_neighbors
- patch_strategy
- change_rationale
- reviewer_focus
- tester_focus

If adjacent validation is load-bearing, `verify_only_surfaces` is no longer optional in practice.
If executable behavior or bounded regression validation is load-bearing, `tester_focus` is no longer optional in practice.

### heavy
Heavy must define everything required by lite, plus all additional fields needed to prevent ambiguity in multi-node, cluster, blocker-uncertain, or security-relevant work.

Heavy should make explicit whenever applicable:
- source_of_truth_node
- stale_defect_node
- adjacent_consistency_node
- expansion_trigger
- retriage_required_when_actual_blocker_differs
- security_focus
- tester_focus

If the task involves bounded cluster consistency, blocker override risk, or security-sensitive reasoning, the relevant heavy fields must not be omitted.
If executable behavior or bounded regression validation is load-bearing, `tester_focus` must not be omitted.
If a genuine security dimension is present, `security_focus` must not be omitted.

## Field meanings

### task_class
Classifies the task before planning or patching.

Allowed values:
- narrow_bugfix
- local_fix_with_adjacent_risk
- bounded_multi_file_patch
- regression_sensitive_change
- security_sensitive_change
- justified_local_hardening
- unknown

If unclear, use `unknown` and escalate. Do not fake precision.

### objective
Concrete task outcome that must be achieved.

### expected_end_state
Concrete observable state that should hold after completion.

### problem_locus
Best current hypothesis of the primary node where the issue or required intervention actually lives.

This is a single primary locus, not an unbounded list.

### locus_confidence
Confidence in `problem_locus`.

Allowed values:
- high
- medium
- low

Low confidence should block direct patching unless explicitly justified by route policy.

### symptom
Observed failure, mismatch, or risk that triggered the task.

### root_cause_hypothesis
Best current causal hypothesis.

This is a hypothesis, not a proven fact, unless evidence explicitly confirms it.

### false_locality_risk
Whether the issue may only appear local while actually depending on adjacent surfaces.

Allowed values:
- low
- medium
- high

### dependency_ring
Nearest dependency contour around the locus.

The contract should distinguish, conceptually, between:
- primary_target
- adjacent_read_nodes
- adjacent_verify_only_nodes
- excluded_neighbors

In bounded cluster or coordinated-consistency tasks, the domain dependency ring should be described first. Execution/report artifacts must not be mixed into the domain ring unless explicitly justified as execution context.

In the current runnable baseline, this structure may still be carried in compatibility form rather than as a fully enforced structured runtime object.

Do not dump broad repo context into this field.

### allowed_read_set
Current Builder-enforced read-boundary payload carried in the contract.

Important current-runtime note:
- in the runnable 4-role runtime, this field is only mechanically enforced as the Builder read boundary;
- Planner currently has a separate fixed input contract: `01_orchestrator.md` and `run_manifest.json`;
- therefore `allowed_read_set` must not be described as a stage-wide mechanically enforced read control across all runtime stages.

### allowed_change_set
Exact set of artifacts approved for modification.

This must begin at the smallest sufficient repair surface for the current pass, not the maximal imaginable cluster or neighborhood.

No file may be edited unless explicitly inside this set.

### verify_only_surfaces
Artifacts allowed for inspection and validation but not for modification in the current pass.

If declared, these surfaces are load-bearing for completion and may not be ignored merely because the primary target appears fixed.

### forbidden_zone
Explicit no-go zone.

Must include unrelated refactors, cleanup not required by acceptance, style churn, architecture reshaping, speculative hardening, and opportunistic renames unless directly required by task completion.

### acceptance_criteria
Conditions required for task completion.

### verification_targets
Named surfaces where post-change validation must be applied.

### evidence_required
Evidence needed before completion can be claimed.

Examples:
- reproduction log
- diff summary
- test result
- runtime output
- before/after comparison
- reviewer consistency result
- security reasoning note

### blockers_or_uncertainties
Unknowns, assumptions, missing signals, or reasons the task may need escalation.

If none, write `none`.

### path_decision
Routing level chosen for the task.

Allowed values:
- lite
- baseline
- heavy

#### baseline
Use only when locus is clear, change is narrow, false locality risk is low, adjacent blast radius is minimal, and no verify-only or adjacent consistency surface is already load-bearing.

In Activation Matrix terms, `baseline` is the runnable compatibility label for the Direct profile.

#### lite
Use when a local patch is plausible but bounded adjacent reading or verification is still needed.

#### heavy
Use when locus is unclear, dependency ring is non-trivial, multiple coordinated edits may be required, or security/regression risk is materially higher.

### escalation_trigger
Concrete conditions that force stop-and-escalate behavior.

Examples:
- locus confidence drops
- required Builder read exceeds allowed_read_set
- required edit exceeds allowed_change_set
- verify-only surface reveals contract mismatch
- local patch causes adjacent inconsistency
- security impact appears
- small fix turns into refactor pressure

## Conditional field meanings

### excluded_neighbors
Nearby nodes explicitly ruled out for the current pass.

### source_of_truth_node
Optional explicit declaration of the node that defines intended content or intended behavior for a bounded cluster or generated-artifact task.

This must not be automatically conflated with the immediate stale defect node.

### stale_defect_node
Optional explicit declaration of the node that is currently stale, inconsistent, or most directly broken in the present fail mode.

Use this when the source-of-truth and immediate repair locus differ.

### adjacent_consistency_node
Optional explicit declaration of the nearest non-primary node whose consistency must still hold after the repair.

Use this when bounded validation depends on more than one load-bearing cluster node.

### expansion_trigger
Concrete evidence required before widening beyond the initial minimum change set.

Examples:
- summary-only restore does not recover declared cluster consistency
- verify-only surface reveals remaining mismatch
- adjacent node proves stale after primary repair
- source-of-truth itself is shown to be incorrect

### retriage_required_when_actual_blocker_differs
Whether the assumed failure mode must yield to a newly discovered actual blocking defect.

Use this when reviewer or validation evidence may override the original scenario narrative.

### patch_strategy
Shape of the intended intervention, not implementation detail.

Examples:
- single-node surgical patch
- bounded two-file coordinated update
- local fix plus adjacent contract alignment
- no patch until locus confirmed

### change_rationale
Why the proposed change set is sufficient and why broader edits are rejected.

### reviewer_focus
What reviewer must inspect most critically:
- boundary drift
- contract drift
- false-local success
- adjacent consistency
- unjustified widening
- under-validated completion claim

### tester_focus
Direct behavior, regression surfaces, and explicit non-expansion boundary for test-stage validation.

### security_focus
Threat surface, trust-boundary relevance, auth/data-exposure implications, and whether findings block progress or only require escalation.

## Enforcement rules
- If triage is incomplete, Builder must not start.
- If allowed_read_set is undefined, Builder execution must stop.
- In the runnable 4-role runtime, this stop condition is mechanically enforced for Builder, not yet as a universal stage-level read sandbox.
- If allowed_change_set is undefined, execution must stop.
- If verify_only_surfaces are declared, Reviewer must require evidence instead of assuming they were checked.
- If actual blocking evidence contradicts the assumed scenario and re-triage is not made explicit, success must not be assumed.
- If excluded_neighbors are omitted where adjacent risk is material, Reviewer must treat scope control as incomplete.
- If verification_targets are missing, success must not be assumed.
- If evidence_required is missing, completion confidence must not be inflated.
- If path_decision is missing, routing is incomplete.
- If escalation_trigger is missing, narrow execution discipline is incomplete.
- If executable behavior or bounded regression validation is load-bearing and `tester_focus` is absent, completion confidence is incomplete.
- If a genuine security dimension is present and `security_focus` is absent, completion confidence is incomplete.
- Tester is invoked only when explicit behavior or regression validation is needed.
- Security is invoked only when the task has a genuine security dimension.

## Global stop conditions
Any role must stop immediately if:
1. it needs to read beyond declared scope,
2. it needs to edit beyond declared scope,
3. the declared locus no longer looks primary,
4. a verify-only surface indicates hidden breakage,
5. the task is mutating into architecture work,
6. acceptance requires unplanned repo-wide reasoning,
7. uncertainty is being replaced by narrative.

Stopping is not failure.
Silent expansion is failure.

## Anti-fake rules
The following are prohibited:
- claiming completion from plausibility alone
- using “should be fixed” as evidence
- widening scope without updating contract
- editing extra files and calling them “minor”
- bundling cleanup with a surgical fix
- calling refactor “hardening”
- calling guesswork “root cause confirmed”
- calling incomplete validation “good enough”

## Minimal completion statement format
Any final completion claim must be expressible as:

1. Objective achieved: yes / no
2. Problem locus validated: yes / partially / no
3. Patch remained within declared change set: yes / no
4. Adjacent surfaces checked: yes / partially / no
5. Acceptance criteria passed: yes / partially / no
6. Residual risk: none / low / medium / high
7. Escalation still needed: yes / no

If this cannot be filled honestly, the task is not done.

## Default philosophy
This contract exists to force the system to behave like a disciplined debugging and patching operator, not like a narrative generator.

The standard is:
- localize first,
- bound reads,
- bound changes,
- patch minimally,
- verify direct symptom,
- verify nearest adjacency,
- stop before drift.

