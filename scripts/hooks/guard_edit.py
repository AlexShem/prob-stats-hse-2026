"""PreToolUse hook (Edit|Write): sources/ is read-only input (CLAUDE.md, "Working with sources").
Only sources/README.md and *.summary.md may be written. Exit 2 = block."""
import json
import sys
from pathlib import Path

data = json.load(sys.stdin)
path = Path(data.get("tool_input", {}).get("file_path", ""))
parts = path.parts
if "sources" in parts:
    if path.name == "README.md" or path.name.endswith(".summary.md"):
        sys.exit(0)
    print("Blocked by repo hook: sources/ is read-only. Adapt material into book/ or slides/ instead.", file=sys.stderr)
    sys.exit(2)
sys.exit(0)
