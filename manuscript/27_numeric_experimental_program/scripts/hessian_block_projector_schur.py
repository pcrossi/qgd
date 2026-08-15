#!/usr/bin/env python3
"""Common GDQ block: Hessian, constraints, physical projector, and Schur.

Classification:
    methodological tool / algebraic verification.

This script does not solve a specific physical problem. It demonstrates, with
small matrices and fixed numbers, the algebraic pattern that must appear in
final solvers:

    official action -> Hessian K -> constraints DC -> projector P_phys
    -> physical Hessian -> Schur complement / DtN.

The example uses a symmetric positive Hessian in four modes:

    x0, x1 : boundary/apparatus modes;
    x2, x3 : internal eliminated modes.

A linear constraint removes a gauge/normalization combination. The test checks:

    1. P_phys is idempotent;
    2. DC P_phys = 0;
    3. K_phys is symmetric;
    4. the Schur complement is positive.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "output_hessian_block_projector_schur.md"


def projector_from_constraints(dc: np.ndarray, metric: np.ndarray) -> np.ndarray:
    """Builds P = I - G^-1 DC^T (DC G^-1 DC^T)^-1 DC."""

    g_inv = np.linalg.inv(metric)
    gram = dc @ g_inv @ dc.T
    return np.eye(metric.shape[0]) - g_inv @ dc.T @ np.linalg.inv(gram) @ dc


def format_matrix(matrix: np.ndarray) -> str:
    """Formats matrix without `[[`, avoiding false wikilinks in Quartz/Obsidian."""

    rows = []
    for row in matrix:
        rows.append(" ".join(f"{value: .6f}" for value in row))
    return "\n".join(rows)


def main() -> None:
    # Example reduced Hessian. In a physical problem, this matrix must come
    # from the second variation of the official action evaluated on the stationary background.
    k = np.array(
        [
            [4.0, 0.3, 0.6, 0.1],
            [0.3, 3.0, 0.2, 0.4],
            [0.6, 0.2, 5.0, 0.7],
            [0.1, 0.4, 0.7, 4.5],
        ]
    )

    # Quadratic metric of the fluctuation space. Here we use the identity to
    # isolate the algebra; in real solvers it can be the mass/measurement matrix.
    g = np.eye(4)

    # A linear constraint: removes the direction x0 - x1 + 0.5 x2 = 0.
    dc = np.array([[1.0, -1.0, 0.5, 0.0]])

    p = projector_from_constraints(dc, g)
    k_phys = p.T @ k @ p

    # We choose the first two physical modes as observed and the last two
    # as internal. The Schur complement eliminates the internal response.
    k_bb = k_phys[:2, :2]
    k_bi = k_phys[:2, 2:]
    k_ib = k_phys[2:, :2]
    k_ii = k_phys[2:, 2:]
    k_eff = k_bb - k_bi @ np.linalg.pinv(k_ii) @ k_ib

    eig_k_phys = np.linalg.eigvalsh(k_phys)
    eig_k_eff = np.linalg.eigvalsh(k_eff)

    checks = {
        "idempotence norm(P^2-P)": np.linalg.norm(p @ p - p),
        "constraint norm(DC P)": np.linalg.norm(dc @ p),
        "symmetry norm(Kphys-Kphys^T)": np.linalg.norm(k_phys - k_phys.T),
        "lowest eigenvalue K_eff": float(eig_k_eff.min()),
    }

    lines = ["# Output — Hessian block, projector, and Schur\n\n"]
    lines.append("Classification: methodological tool / algebraic verification.\n\n")
    lines.append("## Matrices used\n\n")
    lines.append("Hessian example $K$:\n\n")
    lines.append("```text\n")
    lines.append(format_matrix(k))
    lines.append("\n```\n\n")
    lines.append("Linearized constraint $DC$:\n\n")
    lines.append("```text\n")
    lines.append(format_matrix(dc))
    lines.append("\n```\n\n")
    lines.append("## Verifications\n\n")
    lines.append("| test | value |\n")
    lines.append("|---|---:|\n")
    for name, value in checks.items():
        lines.append(f"| {name} | {value:.12e} |\n")
    lines.append("\n## Spectrum\n\n")
    lines.append("| operator | eigenvalues |\n")
    lines.append("|---|---|\n")
    lines.append(f"| $K_{{\\rm phys}}$ | `{np.array2string(eig_k_phys, precision=9)}` |\n")
    lines.append(f"| $K_{{\\rm eff}}$ | `{np.array2string(eig_k_eff, precision=9)}` |\n")
    lines.append("\n## Verdict\n\n")
    lines.append(
        "The algebraic block removes the constraint, preserves the symmetry of the Hessian "
        "and produces a non-negative effective Schur operator in this example "
        "up to roundoff error. "
        "In physical applications, only $K$, $DC$, domain, and boundaries change.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
