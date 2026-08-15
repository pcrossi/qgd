#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `generate example manifest` associated with the chapter `27_numeric_experimental_program`.
Generates a minimal manifest for GDQ scripts.

Classification:
    documentary tool.

This script does not calculate a physical observable. It produces an output model
that every new numerical/symbolic script must fill out to declare domain,
boundary, operator, projector, parameters, and experimental data usage.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_generate_example_manifest.md"

FIELDS = [
    ("Equation/functional", "Which part of S_GDQ or which reduction is being evaluated."),
    ("Background Phi_*", "Solution, reduced ansatz, or declared fixture."),
    ("Domain", "Interval, manifold, mesh, or spectral space."),
    ("Boundary", "Dirichlet, Neumann, Robin, DtN/Schur, or external data."),
    ("Constraints", "Charge, flux, normalization, gauge, phase, boundaries."),
    ("Operator/Hessian", "K_phys, Jacobi, DtN, Schur, or reduced operator."),
    ("Physical projector", "How gauge/coordinate modes are removed."),
    ("Source/apparatus", "J_app or independent external parameter."),
    ("Observable", "Quantity compared or diagnosed."),
    ("Universal parameters", "Constants coming from the theory."),
    ("Apparatus parameters", "Independent data from the experiment/material."),
    ("Numerical parameters", "Mesh, tolerance, solver, seed."),
    ("Data usage", "Whether the experimental target entered prior to comparison."),
    ("Classification", "Evaluation, convergence, consistency, fit, comparison, or prediction."),
]


def main() -> None:
    lines = ["# Output — minimal GDQ script manifest\n\n"]
    lines.append("Classification: documentary tool.\n\n")
    lines.append("| Field | Expected Content |\n")
    lines.append("|---|---|\n")
    for field, description in FIELDS:
        lines.append(f"| {field} | {description} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append("A script that cannot fill these fields is still exploratory.\n")
    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
