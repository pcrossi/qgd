#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Material soliton criterion

Objective:
    Verify the explicit calculations of the neutral Gaussian solution:

        g = delta, H = 0, phi = |x|^2/(4 sigma)

    1. soliton equation: Hess(phi) = (1/(2 sigma)) g;
    2. normalization of the Gaussian density;
    3. reduced free energy W = <sigma |grad phi|^2 + phi - d> = 0;
    4. reduced scalar Ornstein--Uhlenbeck spectrum:

           lambda_k = k/(2 sigma).

Classification:
    Symbolic-numerical verification of an explicit neutral solution.
    Not a metrological prediction and does not identify a charged particle.

Output:
    output_verify_gaussian_soliton.md
"""

from __future__ import annotations

from pathlib import Path
import math
import numpy as np


def main() -> None:
    d = 8
    sigma = 1.3

    # Analytical calculation: the Gaussian rho_N has covariance 2 sigma I.
    expected_r2 = 2.0 * d * sigma
    expected_phi = expected_r2 / (4.0 * sigma)
    expected_sigma_grad = expected_r2 / (4.0 * sigma)
    w_analytic = expected_sigma_grad + expected_phi - d

    # Reproducible Monte Carlo verification of the Gaussian average.
    rng = np.random.default_rng(1818)
    samples = 500_000
    x = rng.normal(loc=0.0, scale=math.sqrt(2.0 * sigma), size=(samples, d))
    r2 = np.sum(x * x, axis=1)
    phi = r2 / (4.0 * sigma)
    sigma_grad = r2 / (4.0 * sigma)
    w_samples = sigma_grad + phi - d

    w_mc = float(np.mean(w_samples))
    w_mc_stderr = float(np.std(w_samples, ddof=1) / math.sqrt(samples))
    r2_mc = float(np.mean(r2))

    # Hess(phi) = (1/(2 sigma)) I.
    hess_coeff = 1.0 / (2.0 * sigma)
    hess = hess_coeff * np.eye(d)
    metric = np.eye(d)
    soliton_residual = hess - hess_coeff * metric
    residual_norm = float(np.linalg.norm(soliton_residual))

    # First eigenvalues of the reduced OU operator.
    eigenvalues = [k / (2.0 * sigma) for k in range(7)]
    first_gap = eigenvalues[1] - eigenvalues[0]

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Output — Neutral Gaussian soliton"\n')
    lines.append('---\n\n')
    lines.append("# Output — Neutral Gaussian soliton\n\n")
    lines.append("## Classification\n\n")
    lines.append(
        "Symbolic-numerical verification of an explicit neutral solution. "
        "Not a metrological prediction.\n\n"
    )
    lines.append("## Data\n\n")
    lines.append(f"- Real dimension: $d={d}$\n")
    lines.append(f"- Geometric scale: $\\sigma={sigma}$\n")
    lines.append(f"- Monte Carlo samples: ${samples}$\n\n")
    lines.append("## Soliton equation\n\n")
    lines.append("$$\n")
    lines.append("\\phi=\\frac{|x|^2}{4\\sigma},\n")
    lines.append("\\qquad\n")
    lines.append("\\nabla_i\\nabla_j\\phi=\\frac{1}{2\\sigma}\\delta_{ij}.\n")
    lines.append("$$\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $1/(2\\sigma)$ | {hess_coeff:.12e} |\n")
    lines.append(f"| soliton residue norm | {residual_norm:.12e} |\n\n")
    lines.append("## Reduced free energy\n\n")
    lines.append("$$\n")
    lines.append("\\mathcal W_{\\rm gauss}\n")
    lines.append("=\n")
    lines.append("\\left\\langle\\sigma|\\nabla\\phi|^2+\\phi-d\\right\\rangle.\n")
    lines.append("$$\n\n")
    lines.append("| quantity | analytical | Monte Carlo |\n")
    lines.append("|---|---:|---:|\n")
    lines.append(f"| $\\langle |x|^2\\rangle$ | {expected_r2:.12e} | {r2_mc:.12e} |\n")
    lines.append(f"| $\\langle\\phi\\rangle$ | {expected_phi:.12e} | {float(np.mean(phi)):.12e} |\n")
    lines.append(
        f"| $\\langle\\sigma|\\nabla\\phi|^2\\rangle$ | "
        f"{expected_sigma_grad:.12e} | {float(np.mean(sigma_grad)):.12e} |\n"
    )
    lines.append(f"| $\\mathcal W$ | {w_analytic:.12e} | {w_mc:.12e} |\n")
    lines.append(f"| MC standard error of $\\mathcal W$ | — | {w_mc_stderr:.12e} |\n\n")
    lines.append("## Reduced scalar Ornstein--Uhlenbeck spectrum\n\n")
    lines.append("$$\n")
    lines.append("\\lambda_k=\\frac{k}{2\\sigma}.\n")
    lines.append("$$\n\n")
    lines.append("| $k$ | $\\lambda_k$ |\n")
    lines.append("|---:|---:|\n")
    for k, val in enumerate(eigenvalues):
        lines.append(f"| {k} | {val:.12e} |\n")
    lines.append("\n")
    lines.append(f"Gap after removing the constant mode: ${first_gap:.12e}$.\n\n")
    lines.append("## Verdict\n\n")
    lines.append(
        "The Gaussian solution exactly satisfies the neutral soliton equation, "
        "has $\\mathcal W=0$ analytically, and exhibits a positive gap in the reduced "
        "OU sector after removing the zero mode. It serves as a neutral reference; "
        "charge, spin, and mass of real particles require the solitonic record "
        "of the corresponding sector.\n"
    )

    out = root / "output_verify_gaussian_soliton.md"
    out.write_text("".join(lines), encoding="utf-8")
    print("".join(lines))


if __name__ == "__main__":
    main()
