#!/usr/bin/env python3
"""
Objective:
    Self-contained recording of the `check overclaim terms` verification associated with chapter `28_technical_faq`.

Classification:
    Documentary, symbolic, or numerical verification preserved in the manuscript.

Searches for terms of possible overclaim in Chapter 28.

This checker is deliberately simple. It does not replace human review, but it helps detect phrases
that could violate the scientific protocol of the manuscript, such as declaring universal resolution
when the text must preserve conditional status.
"""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
WATCH = [
    "resolves everything",
    "definitive proof",
    "without hypothesis",
    "universally proven",
    "fundamental Yang--Mills action",
    "fundamental BRST",
    "physical ghost",
    "fundamental renormalization",
    "universal 8D Perelman",
]


def scan() -> list[tuple[str, int, str, str]]:
    hits: list[tuple[str, int, str, str]] = []
    for path in sorted(ROOT.glob("**/*.md")):
        if "/scripts/" in str(path):
            continue
        lines = path.read_text(encoding="utf-8").splitlines()
        for lineno, line in enumerate(lines, 1):
            low = line.lower()
            for term in WATCH:
                if term.lower() in low:
                    hits.append((str(path.relative_to(ROOT)), lineno, term, line.strip()))
    return hits


def main() -> None:
    hits = scan()
    out = Path(__file__).with_name("output_check_overclaim_terms.md")
    lines = [
        "---",
        'title: "Output — overclaims verification"',
        "---",
        "",
        "# Output — overclaims verification",
        "",
    ]
    if not hits:
        lines.append("No monitored expression of overclaim was found.")
    else:
        lines.append("| File | Line | Term | Snippet |")
        lines.append("|---|---:|---|---|")
        for rel, lineno, term, text in hits:
            lines.append(f"| `{rel}` | {lineno} | {term} | {text} |")
    lines.append("")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(f"Occurrences: {len(hits)}")
    print(f"File generated: {out.name}")
    if hits:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
