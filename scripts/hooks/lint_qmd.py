"""PostToolUse hook (Edit|Write): run the style tripwire on an edited course .qmd file.
Flags are shown to Claude (exit 2). The edit itself has already happened."""
import json
import subprocess
import sys
from pathlib import Path

data = json.load(sys.stdin)
path = Path(data.get("tool_input", {}).get("file_path", ""))
if path.suffix != ".qmd" or not ({"book", "slides", "assessment"} & set(path.parts)) or not path.exists():
    sys.exit(0)
script = Path(__file__).resolve().parents[1] / "style_check.py"
r = subprocess.run([sys.executable, str(script), str(path)], capture_output=True, text=True)
if r.returncode != 0:
    print("Style check (CLAUDE.md, Writing style) flags in the file you just edited:\n" + r.stdout, file=sys.stderr)
    sys.exit(2)
sys.exit(0)
