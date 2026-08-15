#!/usr/bin/env python3
"""
GDQ — Chapter 13 / Hessian, physical projector and Schur complement

Objective:
    Verify, in a self-contained matrix, the sequence used for real
    apparatuses:

        K_GDQ -> P_phys^T K_GDQ P_phys -> R_app

    where:

        R_app = K_YY - K_YI K_II^{-1} K_IY.

    The script does not calculate a real physical solenoid. It tests the
    variational algebra that will be used when the apparatus background is
    provided.

Theoretical source:
    manuscript/13_holonomies_ab_sagnac/notes/hessian_projectors_interface_response.md

Classification:
    Symbolic-numerical consistency test. It is not an experimental prediction.

Output:
    scripts/output_verify_schur_projector.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def orthogonal_projector_from_constraints(constraints: np.ndarray) -> np.ndarray:
    """Return P = I - C^T (C C^T)^{-1} C for full-row-rank constraints C."""

    n = constraints.shape[1]
    gram = constraints @ constraints.T
    return np.eye(n) - constraints.T @ np.linalg.inv(gram) @ constraints


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_verify_schur_projector.md"

    # Toy Hessian symmetric positive on the physical subspace.
    # Coordinates are ordered as two boundary variables and three interior
    # variables before constraint projection.
    K_gdq = np.array(
        [
            [5.0, 0.8, 0.4, 0.0, 0.1],
            [0.8, 4.0, 0.2, 0.3, 0.0],
            [0.4, 0.2, 3.0, 0.5, 0.1],
            [0.0, 0.3, 0.5, 2.5, 0.4],
            [0.1, 0.0, 0.1, 0.4, 2.0],
        ],
        dtype=float,
    )

    # Two linear constraints representing one gauge direction and one flux/charge
    # restriction in this finite-dimensional model.
    C = np.array(
        [
            [1.0, -1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 1.0, -1.0],
        ],
        dtype=float,
    )

    P = orthogonal_projector_from_constraints(C)
    K_phys = P.T @ K_gdq @ P

    # Restrict to an explicit basis of the projected physical image by QR.
    # This avoids inverting a singular matrix in the full ambient coordinates.
    u, s, _ = np.linalg.svd(P)
    rank = int(np.sum(s > 1e-10))
    B = u[:, :rank]
    K_red = B.T @ K_gdq @ B

    # Choose one physical coordinate as boundary and the rest as interior in the
    # reduced physical basis. This is the finite-dimensional analogue of the
    # Y/I splitting after projection.
    K_YY = K_red[:1, :1]
    K_YI = K_red[:1, 1:]
    K_IY = K_red[1:, :1]
    K_II = K_red[1:, 1:]
    R = K_YY - K_YI @ np.linalg.inv(K_II) @ K_IY

    eig_KII = np.linalg.eigvalsh(K_II)
    eig_Kred = np.linalg.eigvalsh(K_red)
    idem_error = np.linalg.norm(P @ P - P)
    constraint_error = np.linalg.norm(C @ P)

    text = f"""# Output — Schur/projector verification

Classification: symbolic-numerical consistency test.

This script verifies the construction:

$$
K_{{\\rm phys}}
=
P_{{\\rm phys}}^T K_{{\\rm GDQ}}P_{{\\rm phys}},
\\qquad
\\mathsf R
=
K_{{YY}}-K_{{YI}}K_{{II}}^{{-1}}K_{{IY}}.
$$

## Projector diagnostics

| quantity | value |
|---|---:|
| physical rank | {rank} |
| idempotency error `||P^2-P||` | {idem_error:.12e} |
| constraint error `||CP||` | {constraint_error:.12e} |

## Reduced physical spectrum

| eigenvalue | value |
|---:|---:|
"""

    for i, val in enumerate(eig_Kred, 1):
        text += f"| {i} | {val:.12e} |\n"

    text += f"""
## Internal gap

| eigenvalue of K_II | value |
|---:|---:|
"""

    for i, val in enumerate(eig_KII, 1):
        text += f"| {i} | {val:.12e} |\n"

    text += f"""
## Schur response

| quantity | value |
|---|---:|
| R_app toy | {float(R[0, 0]):.12e} |

Interpretation: the physical projection and Schur reduction algebra is consistent.
To obtain a real solenoid, this toy matrix must be replaced by the Hessian
of the official action evaluated on the physical background of the apparatus.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
