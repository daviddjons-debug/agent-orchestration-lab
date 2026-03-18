from pathlib import Path
import json
import sys

EXPECTED_STATUS = "ok"
EXPECTED_MESSAGE = "multi-agent orchestration check passed"
REQUIRED = [
    "00_user_goal.md",
    "01_orchestrator.md",
    "02_planner.md",
    "03_builder.md",
    "output/result.json",
]

def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: python3 scripts/reviewer.py <run_dir>")
        return 2

    base = Path(sys.argv[1])
    missing = [x for x in REQUIRED if not (base / x).exists()]
    artifact = base / "output/result.json"

    data = None
    json_ok = False
    status_ok = False
    message_ok = False

    if artifact.exists():
        try:
            data = json.loads(artifact.read_text(encoding="utf-8"))
            json_ok = isinstance(data, dict)
            status_ok = json_ok and data.get("status") == EXPECTED_STATUS
            message_ok = json_ok and data.get("message") == EXPECTED_MESSAGE
        except Exception:
            json_ok = False

    ok = (not missing) and json_ok and status_ok and message_ok

    verdict = (
        "# Reviewer Verdict\n\n"
        "Source: files on disk only\n\n"
        "Checklist:\n"
        f"- [{'x' if not missing else ' '}] Required prior artifacts exist\n"
        f"- [{'x' if artifact.exists() else ' '}] output/result.json exists\n"
        f"- [{'x' if json_ok else ' '}] output/result.json contains valid JSON\n"
        f"- [{'x' if status_ok else ' '}] status matches exact expected value\n"
        f"- [{'x' if message_ok else ' '}] message matches exact expected value\n\n"
        f"Final verdict: {'PASS' if ok else 'FAIL'}\n"
    )

    (base / "04_reviewer.md").write_text(verdict, encoding="utf-8")
    print(verdict)
    return 0 if ok else 1

if __name__ == "__main__":
    raise SystemExit(main())
