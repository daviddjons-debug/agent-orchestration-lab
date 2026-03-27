from pathlib import Path
import json
import sys

REQUIRED = [
    "01_orchestrator.md",
    "02_plan.json",
    "02_planner.md",
    "03_builder.md",
    "run_manifest.json",
]

CONTRACT_FIELDS = [
    "task_class",
    "objective",
    "expected_end_state",
    "symptom",
    "root_cause_hypothesis",
    "problem_locus",
    "locus_confidence",
    "false_locality_risk",
    "profile_selection_basis",
    "path_decision",
    "dependency_ring",
    "dependency_ring_structured",
    "allowed_change_set",
    "verify_only_surfaces",
    "source_of_truth_node",
    "stale_defect_node",
    "adjacent_consistency_node",
    "expansion_trigger",
    "retriage_required_when_actual_blocker_differs",
    "excluded_neighbors",
    "forbidden_zone",
    "acceptance_criteria",
    "verification_targets",
    "evidence_required",
    "blockers_or_uncertainties",
    "escalation_trigger",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/reviewer.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    missing = [x for x in REQUIRED if not (base / x).exists()]

    plan_ok = False
    contract_checks = []
    artifact_checks = []
    artifact_results = []
    consistency_checks = []
    structured_ring_checks = []
    verify_only_checks = []
    adjacent_read_evidence_checks = []
    cluster_role_checks = []
    retriage_checks = []
    security_checks = []
    hardening_checks = []
    undeclared_files = []
    ok = False

    if not missing:
        try:
            manifest = json.loads((base / "run_manifest.json").read_text(encoding="utf-8"))
            plan = json.loads((base / "02_plan.json").read_text(encoding="utf-8"))
        except Exception:
            manifest = None
            plan = None

        manifest_artifacts = manifest.get("artifacts") if isinstance(manifest, dict) else None
        plan_artifacts = plan.get("artifacts") if isinstance(plan, dict) else None
        policy = manifest.get("review_policy", {}) if isinstance(manifest, dict) else {}
        verify_only_surfaces = plan.get("verify_only_surfaces", []) if isinstance(plan, dict) else []
        structured_ring = plan.get("dependency_ring_structured", {}) if isinstance(plan, dict) else {}
        builder_report_text = (base / "03_builder.md").read_text(encoding="utf-8") if (base / "03_builder.md").exists() else ""
        source_of_truth_node = plan.get("source_of_truth_node") if isinstance(plan, dict) else None
        stale_defect_node = plan.get("stale_defect_node") if isinstance(plan, dict) else None
        adjacent_consistency_node = plan.get("adjacent_consistency_node") if isinstance(plan, dict) else None
        retriage_required = plan.get("retriage_required_when_actual_blocker_differs") if isinstance(plan, dict) else None

        require_valid_json = policy.get("require_valid_json", True)
        require_exact_text = policy.get("require_exact_text", True)

        if isinstance(manifest, dict) and isinstance(plan, dict):
            for field in CONTRACT_FIELDS:
                same = manifest.get(field) == plan.get(field)
                contract_checks.append((field, same))

            dependency_ring = plan.get("dependency_ring", [])
            primary_target = structured_ring.get("primary_target")
            adjacent_read_nodes = structured_ring.get("adjacent_read_nodes")
            adjacent_verify_only_nodes = structured_ring.get("adjacent_verify_only_nodes")
            structured_excluded_neighbors = structured_ring.get("excluded_neighbors")

            structured_ring_checks.append((
                "dependency_ring_structured is an object",
                isinstance(structured_ring, dict),
            ))
            structured_ring_checks.append((
                "dependency_ring_structured.primary_target is non-empty",
                isinstance(primary_target, str) and bool(primary_target.strip()),
            ))
            structured_ring_checks.append((
                "dependency_ring_structured.adjacent_read_nodes is a list",
                isinstance(adjacent_read_nodes, list),
            ))
            structured_ring_checks.append((
                "dependency_ring_structured.adjacent_verify_only_nodes is a list",
                isinstance(adjacent_verify_only_nodes, list),
            ))
            structured_ring_checks.append((
                "dependency_ring_structured.excluded_neighbors is a list",
                isinstance(structured_excluded_neighbors, list),
            ))

            if isinstance(primary_target, str) and isinstance(dependency_ring, list):
                structured_ring_checks.append((
                    "dependency_ring_structured.primary_target is present in dependency_ring",
                    primary_target in dependency_ring,
                ))

            if isinstance(adjacent_read_nodes, list) and isinstance(dependency_ring, list):
                structured_ring_checks.append((
                    "dependency_ring_structured.adjacent_read_nodes stay inside dependency_ring",
                    all(isinstance(node, str) and node in dependency_ring for node in adjacent_read_nodes),
                ))

            if isinstance(adjacent_verify_only_nodes, list) and isinstance(dependency_ring, list):
                structured_ring_checks.append((
                    "dependency_ring_structured.adjacent_verify_only_nodes stay inside dependency_ring",
                    all(isinstance(node, str) and node in dependency_ring for node in adjacent_verify_only_nodes),
                ))

            if isinstance(adjacent_verify_only_nodes, list):
                structured_ring_checks.append((
                    "verify_only_surfaces matches dependency_ring_structured.adjacent_verify_only_nodes",
                    verify_only_surfaces == adjacent_verify_only_nodes,
                ))

            if isinstance(adjacent_read_nodes, list):
                actual_read_line = next(
                    (line for line in builder_report_text.splitlines() if line.startswith("Actual read sources: ")),
                    None,
                )
                if actual_read_line is None:
                    adjacent_read_evidence_checks.append(("builder reported actual read sources", False))
                else:
                    reported = actual_read_line.split(": ", 1)[1].strip()
                    reported_sources = [] if reported == "(none)" else [x.strip() for x in reported.split(",") if x.strip()]
                    adjacent_read_evidence_checks.append(("builder reported actual read sources", True))
                    adjacent_read_evidence_checks.append((
                        "builder actual read sources stay inside dependency_ring_structured.adjacent_read_nodes",
                        all(source in adjacent_read_nodes for source in reported_sources),
                    ))

            if isinstance(structured_excluded_neighbors, list):
                structured_ring_checks.append((
                    "excluded_neighbors matches dependency_ring_structured.excluded_neighbors",
                    plan.get("excluded_neighbors", []) == structured_excluded_neighbors,
                ))

        artifacts_match = (
            isinstance(manifest_artifacts, list)
            and isinstance(plan_artifacts, list)
            and plan_artifacts == manifest_artifacts
        )

        plan_ok = artifacts_match and bool(contract_checks) and all(same for _, same in contract_checks)

        declared_artifact_paths = []
        if isinstance(manifest_artifacts, list):
            for spec in manifest_artifacts:
                path = spec.get("path", "<missing>")
                declared_artifact_paths.append(path)

                atype = spec.get("type")
                artifact = base / path
                exists_ok = artifact.exists()
                content_ok = False

                if exists_ok:
                    if atype == "json":
                        try:
                            data = json.loads(artifact.read_text(encoding="utf-8"))
                            required_fields = spec.get("required_fields")
                            if isinstance(required_fields, dict):
                                content_ok = isinstance(data, dict) and all(data.get(k) == v for k, v in required_fields.items())
                            elif not require_valid_json:
                                content_ok = True
                        except Exception:
                            content_ok = not require_valid_json
                    elif atype == "text":
                        exact_content = spec.get("exact_content")
                        if isinstance(exact_content, str):
                            actual = artifact.read_text(encoding="utf-8")
                            content_ok = (actual == exact_content) if require_exact_text else True

                artifact_checks.append((path, exists_ok, content_ok))
                artifact_results.append(exists_ok and content_ok)

            allowed_files = set(REQUIRED + ["04_reviewer.md"] + declared_artifact_paths + verify_only_surfaces)
            for p in sorted(base.rglob("*")):
                if p.is_file():
                    rel = p.relative_to(base).as_posix()
                    if rel not in allowed_files:
                        undeclared_files.append(rel)

            declared_paths_set = set(declared_artifact_paths)

            for verify_path in verify_only_surfaces:
                verify_file = base / verify_path
                verify_ok = False
                if verify_file.exists():
                    try:
                        verify_text = verify_file.read_text(encoding="utf-8").strip()
                        verify_ok = verify_text == "adjacent verified"
                    except Exception:
                        verify_ok = False
                verify_only_checks.append((verify_path, verify_ok))

            cluster_roles_declared = any(
                value is not None for value in [source_of_truth_node, stale_defect_node, adjacent_consistency_node]
            )
            if cluster_roles_declared:
                cluster_role_checks.append((
                    "cluster role completeness",
                    all(isinstance(value, str) and value.strip() for value in [
                        source_of_truth_node, stale_defect_node, adjacent_consistency_node
                    ]),
                ))
                if (
                    isinstance(source_of_truth_node, str) and source_of_truth_node.strip()
                    and isinstance(stale_defect_node, str) and stale_defect_node.strip()
                ):
                    cluster_role_checks.append((
                        "source_of_truth_node distinct from stale_defect_node",
                        source_of_truth_node != stale_defect_node,
                    ))

            if retriage_required is not None:
                retriage_checks.append((
                    "explicit retriage policy declared when required",
                    isinstance(retriage_required, bool),
                ))

            security_input_posix = "output/security_input.json"
            security_review_posix = "output/security_review.json"
            if (
                security_input_posix in declared_paths_set
                and security_review_posix in declared_paths_set
            ):
                security_input = base / security_input_posix
                security_review = base / security_review_posix

                trigger_link_ok = False
                blocking_reason_ok = False

                try:
                    if security_input.exists() and security_review.exists():
                        input_data = json.loads(security_input.read_text(encoding="utf-8"))
                        review_data = json.loads(security_review.read_text(encoding="utf-8"))

                        input_trigger = input_data.get("security_trigger")
                        review_trigger = review_data.get("security_trigger")
                        invocation = review_data.get("security_invocation_decision")
                        optional_hardening = review_data.get("optional_hardening", [])
                        blocking_reason = review_data.get("blocking_security_reason")

                        trigger_link_ok = (
                            invocation == "invoke"
                            and isinstance(input_trigger, str) and input_trigger.strip()
                            and review_trigger == input_trigger
                        )

                        blocking_reason_ok = (
                            isinstance(blocking_reason, str) and blocking_reason.strip()
                            and (
                                not isinstance(optional_hardening, list)
                                or blocking_reason not in optional_hardening
                            )
                        )
                except Exception:
                    trigger_link_ok = False
                    blocking_reason_ok = False

                security_checks.append(("security trigger linked to declared surface", trigger_link_ok))
                security_checks.append(("blocking security reason is not optional hardening", blocking_reason_ok))

            hardening_posix = "output/hardening_note.json"
            if hardening_posix in declared_paths_set:
                hardening_file = base / hardening_posix

                hardening_scope_ok = False
                hardening_reason_ok = False
                refactoring_ok = False

                try:
                    if hardening_file.exists():
                        hardening_data = json.loads(hardening_file.read_text(encoding="utf-8"))
                        hardening_scope_ok = hardening_data.get("hardening_scope") == "local"
                        hardening_reason_ok = hardening_data.get("hardening_reason") == "prevents same nearby failure mode"
                        refactoring_ok = hardening_data.get("refactoring_detected") is False
                except Exception:
                    hardening_scope_ok = False
                    hardening_reason_ok = False
                    refactoring_ok = False

                hardening_checks.append(("hardening scope is local", hardening_scope_ok))
                hardening_checks.append(("hardening reason is evidence-linked", hardening_reason_ok))
                hardening_checks.append(("refactoring is not disguised as hardening", refactoring_ok))

            summary_candidates = sorted(
                path for path in declared_artifact_paths
                if path == "summary.txt" or path.endswith("/summary.txt")
            )

            for summary_path in summary_candidates:
                summary_posix = Path(summary_path).as_posix()
                parent = Path(summary_posix).parent
                result_posix = (parent / "result.json").as_posix()
                if result_posix == ".":
                    result_posix = "result.json"
                if result_posix not in declared_paths_set:
                    continue

                result_json = base / result_posix
                summary_txt = base / summary_posix
                same_message = False

                if result_json.exists() and summary_txt.exists():
                    try:
                        result_data = json.loads(result_json.read_text(encoding="utf-8"))
                        json_message = result_data.get("message")
                        summary_message = summary_txt.read_text(encoding="utf-8").rstrip("\n")
                        same_message = isinstance(json_message, str) and summary_message == json_message
                    except Exception:
                        same_message = False

                consistency_checks.append((f"{result_posix} <-> {summary_posix} message consistency", same_message))

            spec_posix = "src/spec.json"
            summary_posix = "src/generated_summary.txt"
            manifest_posix = "src/generated_manifest.json"
            if (
                spec_posix in declared_paths_set
                and summary_posix in declared_paths_set
                and manifest_posix in declared_paths_set
            ):
                spec_json = base / spec_posix
                summary_txt = base / summary_posix
                manifest_json = base / manifest_posix

                spec_summary_same = False
                spec_manifest_same = False

                try:
                    if spec_json.exists() and summary_txt.exists():
                        spec_data = json.loads(spec_json.read_text(encoding="utf-8"))
                        spec_message = spec_data.get("message")
                        summary_message = summary_txt.read_text(encoding="utf-8").rstrip("\n")
                        spec_summary_same = isinstance(spec_message, str) and summary_message == spec_message
                except Exception:
                    spec_summary_same = False

                try:
                    if spec_json.exists() and manifest_json.exists():
                        spec_data = json.loads(spec_json.read_text(encoding="utf-8"))
                        manifest_data = json.loads(manifest_json.read_text(encoding="utf-8"))
                        spec_message = spec_data.get("message")
                        manifest_message = manifest_data.get("message")
                        spec_manifest_same = isinstance(spec_message, str) and manifest_message == spec_message
                except Exception:
                    spec_manifest_same = False

                consistency_checks.append((f"{spec_posix} <-> {summary_posix} message consistency", spec_summary_same))
                consistency_checks.append((f"{spec_posix} <-> {manifest_posix} message consistency", spec_manifest_same))

        ok = (
            (not missing)
            and plan_ok
            and bool(artifact_results)
            and all(artifact_results)
            and all(same for _, same in consistency_checks)
            and all(same for _, same in structured_ring_checks)
            and all(same for _, same in verify_only_checks)
            and all(same for _, same in adjacent_read_evidence_checks)
            and all(same for _, same in cluster_role_checks)
            and all(same for _, same in retriage_checks)
            and all(same for _, same in security_checks)
            and all(same for _, same in hardening_checks)
            and not undeclared_files
        )

    lines = [
        "# Reviewer Verdict",
        "",
        "Source: files on disk, run_manifest.json, 02_plan.json, and review_policy",
        "",
        "Checklist:",
        f"- [{'x' if not missing else ' '}] Required prior artifacts exist",
        f"- [{'x' if plan_ok else ' '}] 02_plan.json matches full run_manifest.json contract",
    ]
    for field, same in contract_checks:
        lines.append(f"- [{'x' if same else ' '}] {field} matches between manifest and plan")
    for path, exists_ok, content_ok in artifact_checks:
        lines.append(f"- [{'x' if exists_ok else ' '}] {path} exists")
        lines.append(f"- [{'x' if content_ok else ' '}] {path} satisfies declared contract")
    for label, same in consistency_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    for label, same in structured_ring_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    for path, same in verify_only_checks:
        lines.append(f"- [{'x' if same else ' '}] verify-only surface satisfied: {path}")
    for label, same in adjacent_read_evidence_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    for label, same in cluster_role_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    for label, same in retriage_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    for label, same in security_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    for label, same in hardening_checks:
        lines.append(f"- [{'x' if same else ' '}] {label}")
    lines.append(f"- [{'x' if not undeclared_files else ' '}] No undeclared output drift detected")
    if undeclared_files:
        lines.append("Undeclared files:")
        for path in undeclared_files:
            lines.append(f"- {path}")
    lines.extend([
        "",
        f"Final verdict: {'PASS' if ok else 'FAIL'}",
        "",
    ])
    verdict = "\n".join(lines)

    (base / "04_reviewer.md").write_text(verdict, encoding="utf-8")
    print(verdict)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
