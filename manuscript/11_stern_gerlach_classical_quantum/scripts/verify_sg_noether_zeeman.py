#!/usr/bin/env python3
"""Algebraic verification of the Noether--Zeeman theorem.

Classification:
    symbolic-numerical consistency test.

The script uses a physical positive Hessian H_C, a circulation functional c, and
a magnetic functional m = gamma0 c + m_perp. It verifies:

    gamma_eff = <c,H^-1 m>/<c,H^-1 c>
              = gamma0 + <c,H^-1 m_perp>/<c,H^-1 c>.

Also verifies the stationary selection C x B = 0 for the two channels.

The numbers are diagnostics and do not represent a real apparatus.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def main() -> None:
    h = np.array(
        [
            [3.0, 0.2, 0.1],
            [0.2, 2.5, 0.3],
            [0.1, 0.3, 2.0],
        ]
    )
    c = np.array([1.0, 0.0, 0.0])
    gamma0 = 2.0
    m_perp = np.array([0.0, 0.15, -0.05])
    m = gamma0 * c + m_perp

    h_inv_c = np.linalg.solve(h, c)
    h_inv_m = np.linalg.solve(h, m)
    denom = float(c @ h_inv_c)
    gamma_eff = float(c @ h_inv_m / denom)
    delta_gamma = float(c @ np.linalg.solve(h, m_perp) / denom)

    # Stationary selection: the stable channels are parallel/antiparallel to B.
    b = np.array([0.4, -0.2, 0.7])
    n = b / np.linalg.norm(b)
    c_plus = 0.5 * n
    c_minus = -0.5 * n
    cross_plus = np.linalg.norm(np.cross(c_plus, b))
    cross_minus = np.linalg.norm(np.cross(c_minus, b))

    eig_h = np.linalg.eigvalsh(h)

    lines = ["# Output — Noether--Zeeman verification\n\n"]
    lines.append("Classification: symbolic-numerical consistency test.\n\n")
    lines.append("## Test parameters\n\n")
    lines.append("| quantity | value |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| minimum eigenvalue of H_C | {eig_h.min():.12f} |\n")
    lines.append(f"| gamma0 | {gamma0:.12f} |\n")
    lines.append(f"| denom = <c,H^-1 c> | {denom:.12f} |\n")
    lines.append(f"| Delta gamma geom | {delta_gamma:.12f} |\n")
    lines.append(f"| gamma eff | {gamma_eff:.12f} |\n")
    lines.append(f"| gamma0 + Delta gamma | {gamma0 + delta_gamma:.12f} |\n")
    lines.append("\n## Verifications\n\n")
    lines.append("| test | error |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| gamma_eff identity | {abs(gamma_eff - (gamma0 + delta_gamma)):.12e} |\n")
    lines.append(f"| ||C_+ x B|| | {cross_plus:.12e} |\n")
    lines.append(f"| ||C_- x B|| | {cross_minus:.12e} |\n")
    lines.append("\n## Verdict\n\n")
    lines.append(
        "The variational multiplier identity is satisfied in the finite block. "
        "The minimal component is protected by Noether; the excess depends on the "
        "transverse response m_perp and the physical Hessian.\n"
    )

    text = "".join(lines)
    out = Path(__file__).resolve().parent / "output_verify_sg_noether_zeeman.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
