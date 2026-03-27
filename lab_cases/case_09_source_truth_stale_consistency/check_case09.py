import json
from pathlib import Path
import sys

base = Path("lab_cases/case_09_source_truth_stale_consistency/src")

source = json.loads((base / "source.json").read_text(encoding="utf-8"))
stale = json.loads((base / "stale_view.json").read_text(encoding="utf-8"))
adjacent = (base / "adjacent_index.txt").read_text(encoding="utf-8").rstrip("\n")

source_message = source.get("message")
stale_message = stale.get("message")

assert isinstance(source_message, str) and source_message.strip(), "source.json message must be non-empty"
assert isinstance(stale_message, str) and stale_message.strip(), "stale_view.json message must be non-empty"

assert stale_message == source_message, "stale_view.json must match source.json"
assert adjacent == source_message, "adjacent_index.txt must match source.json"

sys.exit(0)
