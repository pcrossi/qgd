#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Physical Hessian C3 and reduced gap

Objective:
    Explicitly calculate the constrained angular Hessian of the C3 junction, the
    projector that removes global rotation, the homogeneous radial block, the
    Schur complement, and the reduced physical gap.

Classification:
    Direct evaluation of reduced operators derived in the text. No use of
    experimental data or fitting.

Output:
    scripts/output_physical_hessian_c3_gap.md
"""

from pathlib import Path
import numpy as np


def main() -> None:
    tau = 1.0
    kappa_rel = 1.0
    tension = 1.0
    theta = np.array([0.0, 2.0 * np.pi / 3.0, 4.0 * np.pi / 3.0])

    d_constraint = tension * np.vstack((-np.sin(theta), np.cos(theta)))
    h_theta = kappa_rel * d_constraint.T @ d_constraint

    ones = np.ones((3, 1))
    p_phys = np.eye(3) - (ones @ ones.T) / 3.0
    h_projected = p_phys.T @ h_theta @ p_phys

    eig_all = np.linalg.eigvalsh(h_theta)
    eig_projected = np.linalg.eigvalsh(h_projected)
    eig_physical = eig_projected[eig_projected > 1e-10]

    k_radial = (3.0 / (2.0 * tau)) * np.eye(3)
    j_theta_r = np.zeros((3, 3))
    h_schur = h_theta - j_theta_r @ np.linalg.inv(k_radial) @ j_theta_r.T
    eig_schur = np.linalg.eigvalsh(p_phys.T @ h_schur @ p_phys)
    eig_schur_physical = eig_schur[eig_schur > 1e-10]

    non_homogeneous_gap = 1.0 / (2.0 * tau)
    reduced_gap = min(float(np.min(eig_schur_physical)), non_homogeneous_gap)

    lines = [
        "# Output — Physical Hessian C3 and reduced gap",
        "",
        "## Normalized parameters",
        "",
        f"- tau: `{tau}`",
        f"- kappa_rel: `{kappa_rel}`",
        f"- T: `{tension}`",
        "",
        "## Angular spectrum",
        "",
        f"- Eigenvalues of H_theta: `{eig_all.tolist()}`",
        f"- Physical eigenvalues after projection: `{eig_physical.tolist()}`",
        "",
        "## Schur",
        "",
        "- J_theta_r is zero due to the conservation of the primitive flux class.",
        f"- Physical eigenvalues of the Schur complement: `{eig_schur_physical.tolist()}`",
        "",
        "## Gap",
        "",
        f"- Gaussian inhomogeneous gap: `{non_homogeneous_gap}`",
        f"- Final reduced gap: `{reduced_gap}`",
        "",
        "Conclusion: after removing global rotation, the C3 junction has two positive relative modes and a positive reduced gap.",
    ]

    out = Path(__file__).with_name("output_physical_hessian_c3_gap.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
