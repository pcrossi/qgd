#!/usr/bin/env python3
"""Assinatura exata do bloco cinetico Berger da acao reduzida oficial."""
from __future__ import annotations

import numpy as np


def main() -> None:
    # Ordem (x,y,z,u,v), com K_2 = qdot.T @ M @ qdot.
    M = np.array([
        [8.0, 8.0, 4.0, -4.0, 0.0],
        [8.0, 0.0, 2.0, -2.0, 0.0],
        [4.0, 2.0, 0.0, -1.0, 0.0],
        [-4.0, -2.0, -1.0, 1.0, 0.0],
        [0.0, 0.0, 0.0, 0.0, 1.0],
    ])
    eigenvalues = np.linalg.eigvalsh(M)
    tolerance = 1.0e-12
    signature = (
        int(np.sum(eigenvalues > tolerance)),
        int(np.sum(eigenvalues < -tolerance)),
        int(np.sum(abs(eigenvalues) <= tolerance)),
    )
    print("eigenvalues =", eigenvalues)
    print("signature (positive, negative, zero) =", signature)
    print("raw_gaussian_covariance_admissible =", signature[1] == 0)


if __name__ == "__main__":
    main()
