from pathlib import Path
import json
import sys

REQUIRED = [
    "00_user_goal.md",
    "01_orchestrator.md",
    "02_plan.json",
    "02_planner.md",
    "03_builder.md",
    "run_manifest.json",
]

CONTRACT_FIELDS = [
    "objective",
    "problem_locus",
    "dependency_ring",
    "allowed_read_set",
    "allowed_change_set",
    "verify_only_surfaces",
    "excluded_neighbors",
    "forbidden_zone",
    "review_strictness",
    "verification_targets",
    "blockers_or_uncertainties",
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
    verify_only_checks = []
    security_checks = []
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

        require_valid_json = policy.get("require_valid_json", True)
        require_exact_text = policy.get("require_exact_text", True)

        if isinstance(manifest, dict) and isinstance(plan, dict):
            for field in CONTRACT_FIELDS:
                same = manifest.get(field) == plan.get(field)
                contract_checks.append((field, same))

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
            and all(same for _, same in verify_only_checks)
            and all(same for _, same in security_checks)
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
    for path, same in verify_only_checks:
        lines.append(f"- [{'x' if same else ' '}] verify-only surface satisfied: {path}")
    for label, same in security_checks:
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
