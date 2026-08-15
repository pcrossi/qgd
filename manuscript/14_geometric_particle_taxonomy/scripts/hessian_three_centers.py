#!/usr/bin/env python3
"""
GDQ — Chapter 14 / Constrained Hessian of the C3 junction

Objective:
    Calculate the constrained angular Hessian of the three centers, remove the
    global rotation, include the homogeneous radial block, and verify the Schur
    complement.

Constrained construction:
    H_theta = kappa_rel (D C)^T (D C)
    H_eff = H_rel - J (K_perp)^(-1) J^T

Classification:
    Direct verification of reduced construction of the geometric taxonomy.

Output:
    scripts/output_hessian_three_centers.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def orthogonal_complement_to_constant(n: int) -> np.ndarray:
    """Return an orthonormal basis of the subspace sum(delta theta)=0."""

    vector = np.ones(n) / np.sqrt(float(n))
    _, _, vh = np.linalg.svd(vector.reshape(1, -1), full_matrices=True)
    return vh[1:].T


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_hessian_three_centers.md"

    tau = 1.0
    angles = 2.0 * np.pi * np.arange(3) / 3.0
    directions = np.column_stack((np.cos(angles), np.sin(angles)))

    # D C maps angular variations to variation of the closure vector.
    d_constraint = np.vstack((-np.sin(angles), np.cos(angles)))
    h_angular = d_constraint.T @ d_constraint

    # Remove the common rotation, which is a zero mode by symmetry.
    q_relative = orthogonal_complement_to_constant(3)
    h_relative = q_relative.T @ h_angular @ q_relative

    # Homogeneous radial block from the official-action sector used in the geometric taxonomy sector.
    k_perp = (3.0 / (2.0 * tau)) * np.eye(3)

    # Primitive flux class is conserved in physical variations, so J=0 here.
    j_mixed = np.zeros((2, 3))
    h_eff = h_relative - j_mixed @ np.linalg.solve(k_perp, j_mixed.T)

    closure_norm = float(np.linalg.norm(np.sum(directions, axis=0)))
    eig_angular = np.linalg.eigvalsh(h_angular)
    eig_relative = np.linalg.eigvalsh(h_relative)
    eig_radial = np.linalg.eigvalsh(k_perp)
    eig_eff = np.linalg.eigvalsh(h_eff)

    assert closure_norm < 1.0e-14
    assert np.allclose(eig_relative, [1.5, 1.5])
    assert np.all(eig_radial > 0)
    assert np.all(eig_eff > 0)

    text = f"""# Output — Constrained Hessian of the three centers

Classification: direct verification of reduced construction.

## Closure

| quantity | value |
|---|---:|
| norm of the sum of tensions | {closure_norm:.12e} |

## Spectra

| block | eigenvalues |
|---|---|
| raw angular H | {', '.join(f'{x:.12e}' for x in eig_angular)} |
| relative H | {', '.join(f'{x:.12e}' for x in eig_relative)} |
| homogeneous radial K | {', '.join(f'{x:.12e}' for x in eig_radial)} |
| effective Schur H | {', '.join(f'{x:.12e}' for x in eig_eff)} |

## Interpretation

The zero of the raw angular block is global rotation. After projecting out this
mode, the two relative modes have eigenvalue $3/2$ in the primitive
normalization. Since $J_{{\\theta r}}=0$ by conservation of the flux class, the
Schur complement maintains the positive relative gap.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
