#!/usr/bin/env python3
"""Short metrological table of the technical FAQ.

Classification:
    documentary consolidation / phenomenological comparison.

This script does not adjust parameters. It only regenerates, in a self-contained manner,
the short table of values that the FAQ uses to explain the difference between
numerical comparison and a full variational proof.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_faq_metrological_comparisons.md"


@dataclass(frozen=True)
class Comparison:
    observable: str
    gdq: float
    reference: float
    unit: str
    status: str

    @property
    def absolute_error(self) -> float:
        return self.gdq - self.reference

    @property
    def relative_error(self) -> float:
        return self.absolute_error / self.reference


COMPARISONS = [
    Comparison("alpha^-1", 137.036082448164, 137.035999, "dimensionless", "structural inheritance"),
    Comparison("m_mu/m_e", 206.768593470629, 206.768283, "dimensionless", "conditional reduction"),
    Comparison("m_tau/m_e", 3477.446405098382, 3477.15, "dimensionless", "conditional reduction"),
    Comparison("v_EW", 246.111195996, 246.21965, "GeV", "structural scale"),
    Comparison("r_p", 0.840778765432, 0.84087, "fm", "structural radius"),
    Comparison(
        "nu_hfs_H",
        1_420_405_718.790905,
        1_420_405_751.768,
        "Hz",
        "leading metrology",
    ),
    Comparison(
        "rho_Lambda",
        6.136532599384e-27,
        5.842445930612e-27,
        "kg/m^3",
        "cosmological boundary",
    ),
]


def main() -> None:
    lines = ["# Output — metrological comparisons of the FAQ\n\n"]
    lines.append("Classification: documentary consolidation / phenomenological comparison.\n\n")
    lines.append("| observable | GDQ | reference | unit | absolute error | relative error | status |\n")
    lines.append("|---|---:|---:|---|---:|---:|---|\n")
    for item in COMPARISONS:
        lines.append(
            "| "
            f"{item.observable} | "
            f"{item.gdq:.15g} | "
            f"{item.reference:.15g} | "
            f"{item.unit} | "
            f"{item.absolute_error:.12g} | "
            f"{item.relative_error:.12g} | "
            f"{item.status} |\n"
        )
    lines.append("\n## Reading rule\n\n")
    lines.append(
        "The table documents preserved compatibilities. The status of each line "
        "remains determined by the corresponding deductive chain, not just "
        "by numerical proximity.\n"
    )
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
