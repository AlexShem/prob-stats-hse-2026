"""PreToolUse hook (Bash): git guardrails from CLAUDE.md, "Git workflow".

Blocks: renaming main, pushing (Aleksandr pushes himself), committing on main
(except solution releases, schedule refreshes and finishing a merge).
Exit 2 = block; the message goes to Claude.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

data = json.load(sys.stdin)
cmd = data.get("tool_input", {}).get("command", "")
cwd = data.get("cwd") or "."


def block(msg):
    print(f"Blocked by repo hook: {msg}", file=sys.stderr)
    sys.exit(2)


def branch():
    r = subprocess.run(["git", "branch", "--show-current"], cwd=cwd, capture_output=True, text=True)
    return r.stdout.strip()


for part in re.split(r"&&|\|\||;|\n", cmd):
    p = part.strip()
    if re.match(r"git\s+(-C\s+\S+\s+)?branch\s+.*(-m|-M|--move)\b", p) and ("main" in p.split() or branch() == "main"):
        block("never rename `main`. Create a branch with `git switch -c <name>` instead.")
    if re.match(r"git\s+(-C\s+\S+\s+)?push\b", p):
        block("agents don't push. Aleksandr pushes himself. Tell him the branch is ready.")
    if re.match(r"git\s+(-C\s+\S+\s+)?commit\b", p) and branch() == "main":
        git_dir = subprocess.run(["git", "rev-parse", "--git-dir"], cwd=cwd, capture_output=True, text=True).stdout.strip()
        merging = (Path(cwd) / git_dir / "MERGE_HEAD").exists()
        allowed = re.search(r"Release S\d\d|[Ss]chedule", p)
        if not (merging or allowed):
            block("no commits straight to `main`. Create `unit/…`, `fix/…` or `infra/…` with `git switch -c` "
                  "and commit there. (Exceptions: 'Release SNN solutions', schedule refresh.)")
sys.exit(0)
