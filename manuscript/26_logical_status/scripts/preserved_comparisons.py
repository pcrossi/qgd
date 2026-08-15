#!/usr/bin/env python3
"""
Objective:
    Self-contained registration of the `preserved comparisons` verification associated with chapter `26_logical_status`.
    Numerical comparisons preserved in the manuscript.

Classification:
    documentary consolidation.

The script does not recalculate physical models. It gathers numbers already incorporated
into previous chapters to verify that the logical chapter maintains explicit status and
comparisons.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_preserved_comparisons.md"


@dataclass(frozen=True)
class Comparison:
    observable: str
    gdq: str
    reference: str
    error: str
    status: str


COMPARISONS = [
    Comparison("mean alpha^-1", "137.036082448164", "137.035999", "6.08e-7 relative", "structural inheritance"),
    Comparison("m_mu/m_e", "206.768593470629", "206.768283", "1.50e-6 relative", "conditional reduction"),
    Comparison("m_tau/m_e", "3477.446405098382", "3477.15", "8.52e-5 relative", "conditional reduction"),
    Comparison("v_GDQ", "246.111195996 GeV", "246.21965 GeV", "-0.044048%", "structural scale"),
    Comparison("r_p^surf", "0.840778765432 fm", "0.84087 fm", "-0.010850%", "structural radius"),
    Comparison("hydrogen hyperfine", "1.420405718790905e9 Hz", "1.420405751768e9 Hz", "-32.977095 Hz", "leading metrology"),
    Comparison("alpha RMS", "0.067894 decades", "diagnostic dataset", "—", "proof of concept"),
    Comparison("rho_Lambda", "6.136532599384e-27 kg/m^3", "5.842445930612e-27 kg/m^3", "+5.033622%", "cosmological boundary"),
]


def main() -> None:
    lines: list[str] = []
    lines.append("# Output — preserved comparisons\n\n")
    lines.append("Classification: documentary consolidation.\n\n")
    lines.append("| observable | GDQ/reduced | reference | error | status |\n")
    lines.append("|---|---:|---:|---:|---|\n")
    for c in COMPARISONS:
        lines.append(f"| {c.observable} | {c.gdq} | {c.reference} | {c.error} | {c.status} |\n")

    lines.append("\n## Reading rule\n\n")
    lines.append(
        "These comparisons reinforce specific routes. They do not transform "
        "conditional reductions into complete variational proofs.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
