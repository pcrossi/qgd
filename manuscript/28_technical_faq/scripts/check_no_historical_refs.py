#!/usr/bin/env python3
"""
Objective:
    Self-contained recording of the `check no historical refs` verification associated with chapter `28_technical_faq`.

Classification:
    Documentary, symbolic, or numerical verification preserved in the manuscript.

Verifies if Chapter 28 is self-contained and does not depend on historical files.

The final manuscript must be self-contained. Therefore, this checker looks for typical terms
of external historical files, such as numerical codes isolated by letter and number. The script
ignores the scripts folder itself, since this comment explains the audited rule.
"""

from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PATTERNS = [
    re.compile(r"\bquest(ão|oes|ões|ao)\b", re.IGNORECASE),
    re.compile(r"\bq[0-9]{1,3}\b", re.IGNORECASE),
    re.compile(r"\bQ[0-9]{1,3}\b"),
]


def scan() -> list[tuple[str, int, str]]:
    hits: list[tuple[str, int, str]] = []
    for path in sorted(ROOT.glob("**/*.md")):
        if "/scripts/" in str(path):
            continue
        for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if any(pattern.search(line) for pattern in PATTERNS):
                hits.append((str(path.relative_to(ROOT)), lineno, line.strip()))
    return hits


def main() -> None:
    hits = scan()
    out = Path(__file__).with_name("output_check_no_historical_refs.md")
    lines = [
        "---",
        'title: "Output — self-containment verification"',
        "---",
        "",
        "# Output — self-containment verification",
        "",
    ]
    if not hits:
        lines.append("No references to external historical files were found in the chapter's Markdown files.")
    else:
        lines.append("| File | Line | Snippet |")
        lines.append("|---|---:|---|")
        for rel, lineno, text in hits:
            lines.append(f"| `{rel}` | {lineno} | {text} |")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Occurrences: {len(hits)}")
    print(f"File generated: {out.name}")
    if hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
