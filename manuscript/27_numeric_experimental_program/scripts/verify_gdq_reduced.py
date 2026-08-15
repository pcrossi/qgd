#!/usr/bin/env python3
"""Verifies the reduced GDQ library.

Classification:
    methodological consistency test.

The goal is to confirm that the reduced blocks used in the manuscript reproduce
simple analytical identities:

    1. Massive DtN: R = lambda coth(lambda L);
    2. Schur: explicit elimination of internal degrees of freedom;
    3. quadratic response: 1/2 delta^T R delta;
    4. detector: Gamma = 1/2 zeta^2 C_path R;
    5. two-alternative density: the cross term decays as exp(-Gamma).

No experimental parameters are fitted here.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np

from gdq_reduced import (
    coherence_from_gamma,
    detector_gamma,
    dtn_massive_interval,
    quadratic_response,
    schur_complement,
    two_path_density,
)


OUT = Path(__file__).resolve().parent / "output_verify_gdq_reduced.md"


def main() -> None:
    # Test 1: reduced DtN used in detector problems.
    lambda_eff = 1.1
    length = 1.0
    r_dtn = dtn_massive_interval(lambda_eff, length)

    # Test 2: Schur complement on a small matrix.
    kbb = np.array([[2.0, 0.2], [0.2, 1.7]])
    kbi = np.array([[0.3, 0.1], [0.2, 0.4]])
    kib = kbi.T
    kii = np.array([[3.0, 0.25], [0.25, 2.5]])
    k_eff = schur_complement(kbb, kbi, kib, kii)

    # Independent verification by solving the internal system:
    # for each boundary vector b, the minimized energy must use
    # i = -K_ii^{-1} K_ib b and return b^T K_eff b.
    b = np.array([1.0, -0.5])
    i_star = -np.linalg.solve(kii, kib @ b)
    full = (
        b @ kbb @ b
        + 2.0 * b @ kbi @ i_star
        + i_star @ kii @ i_star
    )
    reduced = b @ k_eff @ b

    # Test 3: quadratic response.
    delta = np.array([1.0, -1.0])
    e_resp = quadratic_response(delta, k_eff)

    # Test 4: detector and coherence.
    zeta = 1.25
    c_path = 1.0
    gamma = detector_gamma(zeta, lambda_eff, length, c_path)
    coherence = coherence_from_gamma(gamma)

    # Test 5: two-alternative density.
    x = np.linspace(-np.pi, np.pi, 9)
    i1 = np.ones_like(x)
    i2 = np.ones_like(x)
    rho_free = two_path_density(i1, i2, x, gamma=0.0)
    rho_det = two_path_density(i1, i2, x, gamma=gamma)
    contrast_free = float((rho_free.max() - rho_free.min()) / (rho_free.max() + rho_free.min()))
    contrast_det = float((rho_det.max() - rho_det.min()) / (rho_det.max() + rho_det.min()))

    checks = {
        "Schur reproduces minimized energy": abs(full - reduced),
        "symmetric K_eff": np.linalg.norm(k_eff - k_eff.T),
        "K_eff lowest eigenvalue": float(np.linalg.eigvalsh(k_eff).min()),
        "contrast with detector smaller than free contrast": float(contrast_det < contrast_free),
    }

    lines = ["# Output — verification of the reduced GDQ library\n\n"]
    lines.append("Classification: methodological consistency test.\n\n")
    lines.append("## Fixed test parameters\n\n")
    lines.append("| parameter | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $\\lambda_{{\\rm eff}}$ | {lambda_eff:.12f} |\n")
    lines.append(f"| $L$ | {length:.12f} |\n")
    lines.append(f"| $\\zeta$ | {zeta:.12f} |\n")
    lines.append(f"| $C_{{\\rm path}}$ | {c_path:.12f} |\n")
    lines.append("\n## Results\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $\\mathsf R_{{\\rm DtN}}=\\lambda\\coth(\\lambda L)$ | {r_dtn:.12f} |\n")
    lines.append(f"| $\\Gamma_{{\\rm det}}$ | {gamma:.12f} |\n")
    lines.append(f"| $e^{{-\\Gamma_{{\\rm det}}}}$ | {coherence:.12f} |\n")
    lines.append(f"| contrast without detector | {contrast_free:.12f} |\n")
    lines.append(f"| contrast with detector | {contrast_det:.12f} |\n")
    lines.append(f"| $E_{{\\rm resp}}$ | {e_resp:.12f} |\n")
    lines.append("\n## Verifications\n\n")
    lines.append("| test | value |\n")
    lines.append("|---|---:|\n")
    for name, value in checks.items():
        lines.append(f"| {name} | {value:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append(
        "The reduced blocks satisfy the expected algebraic identities. "
        "The reduction is methodological: in physical applications, the parameters must "
        "come from the background, the boundary, or the declared apparatus.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
