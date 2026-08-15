#!/usr/bin/env python3
"""
Objective:
    Self-contained registration of the `logical inventory` verification associated with chapter `26_logical_status`.
    Logical inventory of Chapter 26.

Classification:
    documentary check / inventory.

This script does not calculate a physical prediction. It generates a self-contained
table with the logical classification used in the chapter: axioms, definitions,
conditional results, reductions, and future programs.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_logical_inventory.md"


@dataclass(frozen=True)
class Entry:
    name: str
    category: str
    status: str


ENTRIES = [
    Entry("official action", "axiom", "fixed"),
    Entry("Hermitian/Bismut structure", "geometric axiom", "fixed"),
    Entry("causal boundary gamma", "problem data", "declared"),
    Entry("rho=exp(-(f+fbar)/2)", "definition", "do not reopen locally"),
    Entry("S_R=hbar(f-fbar)/(2i)", "definition", "do not reopen locally"),
    Entry("U=rho/(4pi z_tau)^n", "definition", "do not reopen locally"),
    Entry("Madelung continuity", "derivation", "canonical sector"),
    Entry("Hamilton-Jacobi-Bohm", "derivation", "canonical sector"),
    Entry("weighted metric equation", "derivation", "variational"),
    Entry("global-local bridge", "conditional theorem", "six lemmas and declared gluing"),
    Entry("alpha inheritance", "conditional theorem", "global normalization"),
    Entry("three generations", "conditional theorem", "topological class and three stomata"),
    Entry("effective Yang-Mills", "effective reduction", "operational color domain"),
    Entry("hydrogen", "effective reduction", "structural Dirac-Bismut"),
    Entry("alpha decay", "reduced proof of concept", "Schur/Riesz and alpha channel"),
    Entry("regular black hole", "effective reduction", "future 8D covariant"),
    Entry("integrated cosmological solver", "future program", "joint metrology"),
    Entry("real apparatuses", "future program", "real boundaries and materials"),
]


def main() -> None:
    counts: dict[str, int] = {}
    for entry in ENTRIES:
        counts[entry.category] = counts.get(entry.category, 0) + 1

    lines: list[str] = []
    lines.append("# Output — logical inventory\n\n")
    lines.append("Classification: documentary check / inventory.\n\n")
    lines.append("## Entries\n\n")
    lines.append("| item | category | status |\n")
    lines.append("|---|---|---|\n")
    for entry in ENTRIES:
        lines.append(f"| {entry.name} | {entry.category} | {entry.status} |\n")

    lines.append("\n## Count by category\n\n")
    lines.append("| category | quantity |\n")
    lines.append("|---|---:|\n")
    for category, count in sorted(counts.items()):
        lines.append(f"| {category} | {count} |\n")

    lines.append("\n## Verdict\n\n")
    lines.append(
        "The inventory separates fundamental inputs, definitions, derivations, "
        "conditional theorems, reductions, and future programs. It should not be "
        "read as a physical proof, but as an editorial consistency check.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
