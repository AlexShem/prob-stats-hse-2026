"""Flag wording that makes course text read as machine-written.

Usage: make lint                      (all .qmd files)
       uv run python scripts/style_check.py book/lectures/L03-*.qmd

This is a tripwire, not a judge: a hit means "look at this sentence again".
Word list and patterns follow the writing rules in CLAUDE.md.
"""
import re
import sys
from pathlib import Path

BANNED_WORDS = [
    "delve", "leverage", "underscore", "harness", "foster", "utilize", "facilitate",
    "streamline", "bolster", "illuminate", "showcase", "embark", "elevate", "empower",
    "unleash", "unlock", "optimize", "garner", "resonate", "revolutionize", "elucidate",
    "transcend", "intertwine", "grapple", "exemplify", "underpin",
    "tapestry", "landscape", "realm", "paradigm", "synergy", "testament", "beacon",
    "journey", "interplay", "intricacies", "myriad", "plethora", "endeavor",
    "pivotal", "crucial", "seamless", "robust", "vibrant", "intricate", "meticulous",
    "nuanced", "cutting-edge", "transformative", "game-changing", "groundbreaking",
    "unparalleled", "invaluable", "multifaceted", "profound", "ever-evolving", "fast-paced",
]
# "robust" is a term of art in statistics (robust estimator, robust SE): allowed in that sense.
TERM_OF_ART = {"robust": re.compile(r"robust (standard|estimat|regression|to )", re.I)}

BANNED_PHRASES = [
    r"it'?s (important|worth) (to note|noting)", r"it is worth noting", r"plays? an? (pivotal|crucial|key|vital) role",
    r"in today'?s", r"\bin conclusion\b", r"\bin summary\b", r"\bto sum up\b", r"at its core",
    r"that being said", r"key takeaways?", r"let'?s (dive|delve|explore|unpack|break down)",
    r"dive into", r"deep dive", r"when it comes to", r"not only\b.*\bbut also",
    r"here'?s the (kicker|thing|catch)", r"the best part\?", r"\b(furthermore|moreover)\b",
    r"^\s*additionally,", r"shed(s)? light", r"valuable insights?", r"deeper understanding",
    r"in this (lecture|chapter|section|seminar),? we (will|'ll)", r"as we (have|'ve) seen",
    r"serves as", r"stands as", r"\bboasts\b", r"I hope this helps", r"rich (history|tapestry)",
    r"it'?s not (just )?\w+[^.]{0,40}(—|--|, it'?s) ",
]
BOLD_BULLET = re.compile(r"^\s*[-*+]\s+\*\*[^*]+:\*\*")
EMOJI = re.compile("[\U0001F300-\U0001FAFF✅✨➡⭐]")
EM_DASH = re.compile(r"—|(?<![-<!])--(?![->])")

def strip_code(text: str) -> str:
    """Blank out fenced code, YAML front matter and HTML comments, keeping line numbers."""
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"^---\n.*?\n---\n", blank, text, count=1, flags=re.S)
    text = re.sub(r"^```.*?^```", blank, text, flags=re.S | re.M)
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    return text

def check(path: Path) -> int:
    text = strip_code(path.read_text(encoding="utf-8"))
    hits = 0
    for n, line in enumerate(text.splitlines(), 1):
        low = line.lower()
        for w in BANNED_WORDS:
            if re.search(rf"\b{re.escape(w)}", low):
                if w in TERM_OF_ART and TERM_OF_ART[w].search(line):
                    continue
                print(f"{path}:{n}: word '{w}'"); hits += 1
        for p in BANNED_PHRASES:
            if re.search(p, line, re.I):
                print(f"{path}:{n}: phrase /{p}/"); hits += 1
        if BOLD_BULLET.search(line):
            print(f"{path}:{n}: bold-first bullet"); hits += 1
        if EMOJI.search(line):
            print(f"{path}:{n}: emoji"); hits += 1
    dashes = len(EM_DASH.findall(text))
    words = max(len(text.split()), 1)
    if dashes > max(2, words // 400):
        print(f"{path}: {dashes} em dashes in ~{words} words (aim for about one per page)"); hits += 1
    return hits

if __name__ == "__main__":
    args = sys.argv[1:]
    files = [Path(a) for a in args] if args else [
        p for d in ("book", "slides", "assessment") for p in Path(d).rglob("*.qmd")]
    total = sum(check(f) for f in files)
    print(f"{total} flag(s) in {len(files)} file(s)")
    sys.exit(1 if total else 0)
