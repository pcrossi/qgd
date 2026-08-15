#!/usr/bin/env python3
"""
GDQ — Chapter 17 / Dirac–Bismut modes of beta decay

Directly evaluates the declared tangential operator:

    D = (2 sigma.L - m sigma_3)/r

for the electronic channel (m=-1, j=1/2) and for the neutral torsional mode
(m=0, j=0). The script does not use experimental data or fix rate.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


SIGMA = (
    np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex),
    np.array([[0.0, -1j], [1j, 0.0]], dtype=complex),
    np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex),
)


def angular_momentum(two_j: int) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    j = 0.5 * two_j
    magnetic = np.arange(-j, j + 1.0, 1.0)
    lz = np.diag(magnetic).astype(complex)
    lp = np.zeros((magnetic.size, magnetic.size), dtype=complex)
    for col, m_value in enumerate(magnetic[:-1]):
        lp[col + 1, col] = math.sqrt(j * (j + 1.0) - m_value * (m_value + 1.0))
    lm = lp.conj().T
    return 0.5 * (lp + lm), (lp - lm) / (2j), lz


def bismut_block(two_j: int, charge: int, radius: float = 1.0) -> np.ndarray:
    generators = angular_momentum(two_j)
    orbital_dim = two_j + 1
    matrix = np.zeros((2 * orbital_dim, 2 * orbital_dim), dtype=complex)
    for sigma, generator in zip(SIGMA, generators):
        matrix += 2.0 * np.kron(sigma, generator)
    matrix -= charge * np.kron(SIGMA[2], np.eye(orbital_dim))
    return matrix / radius


def kernel_data(two_j: int, charge: int) -> tuple[np.ndarray, np.ndarray, float]:
    matrix = bismut_block(two_j, charge)
    values, vectors = np.linalg.eigh(matrix)
    kernel = vectors[:, np.abs(values) < 1e-12]
    residual = float(np.linalg.norm(matrix @ kernel))
    return values, kernel, residual


def main() -> None:
    charged_values, charged_kernel, charged_residual = kernel_data(1, -1)
    neutral_values, neutral_kernel, neutral_residual = kernel_data(0, 0)

    lines = [
        "# Output — Dirac–Bismut beta modes",
        "",
        "Classification: direct evaluation of the declared tangential operator.",
        "",
        "## Electronic channel",
        "",
        "- `m = -1`, `j = 1/2`",
        f"- eigenvalues: `{np.array2string(charged_values, precision=12)}`",
        f"- kernel dimension: `{charged_kernel.shape[1]}`",
        "- Peter–Weyl spectator multiplicity: `2`",
        f"- kernel residue: `{charged_residual:.3e}`",
        "",
        "## Neutral torsional channel",
        "",
        "- `m = 0`, `j = 0`",
        f"- eigenvalues: `{np.array2string(neutral_values, precision=12)}`",
        f"- kernel dimension: `{neutral_kernel.shape[1]}`",
        f"- kernel residue: `{neutral_residual:.3e}`",
        "",
        "Interpretation: the neutral channel provides the reduced sector of the torsional antineutrino; the APS orientation selects the physical outgoing modes.",
        "",
    ]
    out = Path(__file__).with_name("output_solve_bismut_dirac_modes_beta.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
