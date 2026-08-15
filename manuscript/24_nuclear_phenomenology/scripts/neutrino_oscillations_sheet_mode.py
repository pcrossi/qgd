#!/usr/bin/env python3
"""
Sheet--mode neutral oscillations in GDQ.

Goal
----
Preserve, in a self-contained manner, the reduced verification of the
neutrino oscillations sector in Chapter 24.

Scientific classification
-------------------------
Reduced GDQ candidate. The script does not use squared mass differences as
input. It uses:

1. the beta neutral channel as the physical origin of the scale;
2. S_nu = alpha^7 Q_beta^2;
3. chi_nu = (12/25) exp(-alpha/4);
4. lambda = (0, chi_nu^2/2, 6*pi/5);
5. reduced geometric angles to construct the sheet--mode matrix.

The goal is to verify consistency, order of magnitude, hermiticity,
unitarity, and operational oscillation probabilities. The final
metrological prediction would require calculating G^nu and K^nu directly from the
complete official neutral Hessian on the neutral background.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "output_neutrino_oscillations_sheet_mode.md"

# Constants used in the chapter.
ALPHA = 1.0 / 137.035999177
Q_BETA_EV = 0.782333559310e6

# Reference values for final comparison. They do not enter the GDQ calculation.
REF = {
    "theta12_deg": 33.68,
    "theta23_deg": 48.50,
    "theta13_deg": 8.52,
    "delta_cp_deg": 177.0,
    "dm21": 7.49e-5,
    "dm31": 2.534e-3,
}

FLAVORS = ("e", "mu", "tau")


def pmns(theta12: float, theta23: float, theta13: float, delta: float) -> np.ndarray:
    """Standard unitary matrix used only as an operational parameterization.

    In the GDQ reading, this matrix represents the sheet--mode projection
    U_GDQ. The trigonometric form is an operational language to print
    the laboratory oscillation probabilities.
    """

    c12, s12 = math.cos(theta12), math.sin(theta12)
    c23, s23 = math.cos(theta23), math.sin(theta23)
    c13, s13 = math.cos(theta13), math.sin(theta13)
    e_minus = complex(math.cos(-delta), math.sin(-delta))
    e_plus = complex(math.cos(delta), math.sin(delta))
    return np.array(
        [
            [c12 * c13, s12 * c13, s13 * e_minus],
            [
                -s12 * c23 - c12 * s23 * s13 * e_plus,
                c12 * c23 - s12 * s23 * s13 * e_plus,
                s23 * c13,
            ],
            [
                s12 * s23 - c12 * c23 * s13 * e_plus,
                -c12 * s23 - s12 * c23 * s13 * e_plus,
                c23 * c13,
            ],
        ],
        dtype=complex,
    )


def rel_err(value: float, reference: float) -> float:
    return (value - reference) / reference


def oscillation_probability(U: np.ndarray, masses2: np.ndarray, alpha_i: int, beta_i: int, l_over_e: float) -> float:
    """Operational probability P(alpha -> beta).

    Uses the standard laboratory form with phase 1.267 Delta m^2 L/E, where
    Delta m^2 is in eV^2 and L/E in km/GeV. GDQ enters by providing U and m_i^2.
    """

    prob = 1.0 if alpha_i == beta_i else 0.0
    for i in range(3):
        for j in range(i + 1, 3):
            x = np.conj(U[alpha_i, i]) * U[beta_i, i] * U[alpha_i, j] * np.conj(U[beta_i, j])
            phase = 1.267 * (masses2[j] - masses2[i]) * l_over_e
            prob -= 4.0 * x.real * math.sin(phase) ** 2
            prob += 2.0 * x.imag * math.sin(2.0 * phase)
    return float(prob.real)


def main() -> None:
    chi_nu = (12.0 / 25.0) * math.exp(-ALPHA / 4.0)
    s_nu = ALPHA**7 * Q_BETA_EV**2
    lambdas = np.array([0.0, 0.5 * chi_nu**2, 6.0 * math.pi / 5.0], dtype=float)
    masses2 = s_nu * lambdas
    masses = np.sqrt(masses2)
    dm21 = masses2[1] - masses2[0]
    dm31 = masses2[2] - masses2[0]

    theta12 = math.atan(1.0 / math.sqrt(2.0))
    theta23 = math.pi / 4.0
    theta13 = math.asin(chi_nu / math.pi)

    # Historical value kept as a comparative marker, still pending
    # derivation via neutral oriented holonomy.
    delta_cp = 3.84

    U = pmns(theta12, theta23, theta13, delta_cp)
    G = np.eye(3)
    K = U @ np.diag(lambdas) @ U.conj().T
    unitarity_err = np.linalg.norm(U.conj().T @ U - np.eye(3))
    hermiticity_err = np.linalg.norm(K - K.conj().T)
    generalized_residual = np.linalg.norm(K @ U - G @ U @ np.diag(lambdas))

    lambda2_required = REF["dm21"] / s_nu
    lambda3_required = REF["dm31"] / s_nu
    chi_required = math.sqrt(2.0 * lambda2_required)

    l_over_e_values = [100.0, 295.0 / 0.6, 810.0 / 2.0, 1300.0 / 2.5, 1000.0]

    lines: list[str] = []
    lines.append("# Output — sheet--mode neutral oscillations\n\n")
    lines.append("Classification: reduced GDQ candidate and operational verification.\n\n")

    lines.append("## Inputs frozen before comparison\n\n")
    lines.append(f"- alpha: `{ALPHA:.15e}`\n")
    lines.append(f"- Q_beta: `{Q_BETA_EV:.12e} eV`\n")
    lines.append(f"- S_nu = alpha^7 Q_beta^2: `{s_nu:.12e} eV^2`\n")
    lines.append(f"- chi_nu = (12/25) exp(-alpha/4): `{chi_nu:.12e}`\n")
    lines.append("- lambda = `(0, chi_nu^2/2, 6*pi/5)`\n")
    lines.append("- delta_CP used in the test: historical marker `3.84 rad`, not final prediction.\n\n")

    lines.append("## Eigenvalues and masses\n\n")
    lines.append("| mode | lambda | m_i^2 (eV^2) | m_i (eV) |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for i, (lam, m2, m) in enumerate(zip(lambdas, masses2, masses), start=1):
        lines.append(f"| {i} | {lam:.12e} | {m2:.12e} | {m:.12e} |\n")
    lines.append(f"| sum | — | — | {masses.sum():.12e} |\n")

    lines.append("\n## Squared differences\n\n")
    lines.append("| quantity | Reduced GDQ | reference | relative error |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(f"| dm21 | {dm21:.12e} | {REF['dm21']:.12e} | {rel_err(dm21, REF['dm21']):+.6e} |\n")
    lines.append(f"| dm31 | {dm31:.12e} | {REF['dm31']:.12e} | {rel_err(dm31, REF['dm31']):+.6e} |\n")

    lines.append("\n## Sheet--mode angles\n\n")
    theta_rows = [
        ("theta12", math.degrees(theta12), REF["theta12_deg"]),
        ("theta23", math.degrees(theta23), REF["theta23_deg"]),
        ("theta13", math.degrees(theta13), REF["theta13_deg"]),
        ("delta_CP marker", math.degrees(delta_cp), REF["delta_cp_deg"]),
    ]
    lines.append("| parameter | Reduced GDQ | reference | difference |\n")
    lines.append("|---|---:|---:|---:|\n")
    for name, value, reference in theta_rows:
        lines.append(f"| {name} | {value:.9f} deg | {reference:.9f} deg | {value-reference:+.9f} deg |\n")

    lines.append("\n## Squared moduli of the sheet--mode matrix\n\n")
    mod2 = np.abs(U) ** 2
    lines.append("| sheet | i=1 | i=2 | i=3 | sum |\n")
    lines.append("|---|---:|---:|---:|---:|\n")
    for flavor, row in zip(FLAVORS, mod2):
        lines.append(f"| {flavor} | {row[0]:.12f} | {row[1]:.12f} | {row[2]:.12f} | {row.sum():.12f} |\n")

    lines.append("\n## Reconstruction of reduced K^nu\n\n")
    lines.append(f"- unitary error of U: `{unitarity_err:.3e}`\n")
    lines.append(f"- hermiticity error of K: `{hermiticity_err:.3e}`\n")
    lines.append(f"- generalized problem residue with G=I: `{generalized_residual:.3e}`\n\n")
    lines.append("Real part of K:\n\n")
    for row in K.real:
        lines.append("- " + "  ".join(f"{x:.12e}" for x in row) + "\n")
    lines.append("\nImaginary part of K:\n\n")
    for row in K.imag:
        lines.append("- " + "  ".join(f"{x:.12e}" for x in row) + "\n")

    lines.append("\n## Sensitivity of the coefficients\n\n")
    lines.append("| coefficient | reference required | Reduced GDQ | relative error |\n")
    lines.append("|---|---:|---:|---:|\n")
    lines.append(
        f"| lambda2 | {lambda2_required:.12e} | {lambdas[1]:.12e} | {rel_err(lambdas[1], lambda2_required):+.6e} |\n"
    )
    lines.append(
        f"| lambda3 | {lambda3_required:.12e} | {lambdas[2]:.12e} | {rel_err(lambdas[2], lambda3_required):+.6e} |\n"
    )
    lines.append(f"| chi_nu | {chi_required:.12e} | {chi_nu:.12e} | {rel_err(chi_nu, chi_required):+.6e} |\n")
    lines.append(
        f"| lambda3/(2*pi) | {lambda3_required/(2*math.pi):.12e} | {3.0/5.0:.12e} | {rel_err(3.0/5.0, lambda3_required/(2*math.pi)):+.6e} |\n"
    )

    lines.append("\n## Operational probabilities P(alpha -> beta)\n\n")
    lines.append("| L/E (km/GeV) | P(e->e) | P(mu->e) | P(mu->mu) | P(mu->tau) |\n")
    lines.append("|---:|---:|---:|---:|---:|\n")
    for l_over_e in l_over_e_values:
        pee = oscillation_probability(U, masses2, 0, 0, l_over_e)
        pme = oscillation_probability(U, masses2, 1, 0, l_over_e)
        pmm = oscillation_probability(U, masses2, 1, 1, l_over_e)
        pmt = oscillation_probability(U, masses2, 1, 2, l_over_e)
        lines.append(f"| {l_over_e:.6f} | {pee:.12f} | {pme:.12f} | {pmm:.12f} | {pmt:.12f} |\n")

    lines.append("\n## Verdict\n\n")
    lines.append(
        "The reduced reconstruction is internally consistent: U is unitary, K is "
        "Hermitian and the spectral problem closes with machine numerical residue. "
        "The squared differences remain close to the reference values, with "
        "the largest error in the solar mode. The result is not yet final metrology, since "
        "G^nu, K^nu, Z_nu, delta_CP and the medium potential must come from the official "
        "neutral Hessian and classical matter sources.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
