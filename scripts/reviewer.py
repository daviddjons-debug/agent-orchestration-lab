from pathlib import Path
import json
import sys

REQUIRED = [
    "00_user_goal.md",
    "01_orchestrator.md",
    "02_planner.md",
    "03_builder.md",
    "run_manifest.json",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/reviewer.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    missing = [x for x in REQUIRED if not (base / x).exists()]

    artifact_rel = "output/result.json"
    expected_status = "ok"
    expected_message = "multi-agent orchestration check passed"
    artifact = base / artifact_rel
    json_ok = False
    status_ok = False
    message_ok = False

    if not missing:
        manifest = json.loads((base / "run_manifest.json").read_text(encoding="utf-8"))
        artifact_rel = manifest["artifact_path"]
        expected_status = manifest["expected_status"]
        expected_message = manifest["expected_message"]
        artifact = base / artifact_rel

        if artifact.exists():
            try:
                data = json.loads(artifact.read_text(encoding="utf-8"))
                json_ok = isinstance(data, dict)
                status_ok = json_ok and data.get("status") == expected_status
                message_ok = json_ok and data.get("message") == expected_message
            except Exception:
                json_ok = False

    ok = (not missing) and artifact.exists() and json_ok and status_ok and message_ok

    verdict = (
        "# Reviewer Verdict\n\n"
        "Source: files on disk and run_manifest.json\n\n"
        "Checklist:\n"
        f"- [{'x' if not missing else ' '}] Required prior artifacts exist\n"
        f"- [{'x' if artifact.exists() else ' '}] {artifact_rel} exists\n"
        f"- [{'x' if json_ok else ' '}] {artifact_rel} contains valid JSON\n"
        f"- [{'x' if status_ok else ' '}] status matches manifest expected value\n"
        f"- [{'x' if message_ok else ' '}] message matches manifest expected value\n\n"
        f"Final verdict: {'PASS' if ok else 'FAIL'}\n"
    )

    (base / "04_reviewer.md").write_text(verdict, encoding="utf-8")
    print(verdict)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
