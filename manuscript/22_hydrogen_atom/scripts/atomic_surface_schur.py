#!/usr/bin/env python3
"""
GDQ — Chapter 22 / Hydrogen

Objective:
    Directly evaluate the collective surface block of the proton at atomic
    and hadronic scales:

        R_sigma(q) = - J_sigma(q)^T K_sigma(q)^(-1) J_sigma(q).

Classification:
    Direct reduced calculation/sectoral no-go. Shows that the collective q^4 block is
    too suppressed at atomic q to close the hyperfine or Lamb shift, but
    is relevant at form factor scales.

Output:
    output_atomic_surface_schur.md
"""

from __future__ import annotations

from math import sqrt
from pathlib import Path

import numpy as np
from scipy import constants as C


OUT = Path(__file__).with_name("output_atomic_surface_schur.md")

alpha = C.alpha
c = C.c
hbar = C.hbar
m_e = C.m_e
m_p = C.m_p
mu_ep = m_e * m_p / (m_e + m_p)

r_p = 0.84077876545  # fm
lambda_E = sqrt(12.0) / r_p
j = np.array([1.712091781054, 1.341454657186, 1.063840998206], dtype=float)


def K_sigma(x: float) -> np.ndarray:
    return np.diag([1.0 + x, (1.0 + x) ** 2, (1.0 + x) ** 2])


def J_sigma(x: float) -> np.ndarray:
    return x * np.array([j[0], j[1], j[2] * sqrt(max(x, 0.0))], dtype=float)


def schur(x: float) -> float:
    K = K_sigma(x)
    J = J_sigma(x)
    return -float(J @ np.linalg.solve(K, J))


def q_bohr_fm_inv() -> float:
    a0_eff = hbar / (mu_ep * c * alpha)
    return (1.0 / a0_eff) / 1e15


def main() -> None:
    q_atom = q_bohr_fm_inv()
    rows = [
        ("hyperfine 1s", q_atom),
        ("Lamb 2s", q_atom / 2.0),
        ("hadronic 1/r_p", 1.0 / r_p),
        ("low scattering", 0.25),
        ("medium scattering", 1.0),
    ]

    lines = [
        "---",
        'title: "Output — surface Schur at atomic scales"',
        "---",
        "",
        "# Output — surface Schur at atomic scales",
        "",
        "Classification: direct reduced calculation/sectoral no-go.",
        "",
        f"- $r_p={r_p:.12f}$ fm",
        f"- $\\Lambda_E=\\sqrt{{12}}/r_p={lambda_E:.12f}$ fm$^{{-1}}$",
        "",
        "$$",
        "\\mathsf R_\\Sigma(q)",
        "=",
        "-J_\\Sigma(q)^T K_\\Sigma(q)^{-1}J_\\Sigma(q),",
        "\\qquad",
        "x=\\frac{q^2}{\\Lambda_E^2}.",
        "$$",
        "",
        "| scale | $q$ [fm$^{-1}$] | $x$ | min eig $K$ | max eig $K$ | $\\mathsf R_\\Sigma$ |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for name, q in rows:
        x = (q / lambda_E) ** 2
        eig = np.linalg.eigvalsh(K_sigma(x))
        lines.append(
            f"| {name} | `{q:.12e}` | `{x:.12e}` | `{eig[0]:.12e}` | `{eig[-1]:.12e}` | `{schur(x):.12e}` |"
        )

    lines += [
        "",
        "Conclusion: at the atomic scale, $x\\ll1$ and the collective Schur is of order",
        "$x^2$. Therefore, this block does not close the hyperfine residue of order",
        "$10^{-5}$ nor the Lamb shift. It belongs to the form factor sector",
        "at hadronic/intermediate scales.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
