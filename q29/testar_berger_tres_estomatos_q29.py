#!/usr/bin/env python3
"""Espectro universal dos squashings comum/relativos no junction C3."""

import numpy as np

H_COMMON = -2.670908561300202
L_C3 = np.array([[2.0, -1.0, -1.0], [-1.0, 2.0, -1.0], [-1.0, -1.0, 2.0]])


def hessian(kappa):
    return H_COMMON*np.eye(3) + kappa*L_C3


if __name__ == "__main__":
    threshold = -H_COMMON/3.0
    print("Q29 — BERGER EM TRÊS ESTÔMATOS")
    print(f"h_common                 = {H_COMMON:.12f}")
    print(f"kappa relativo crítico   = {threshold:.12f}")
    for kappa in (0.0, threshold, 1.0, 10.0):
        print(f"kappa={kappa:.12f} spec={np.linalg.eigvalsh(hessian(kappa))}")
    common = np.ones(3)/np.sqrt(3.0)
    assert np.allclose(L_C3@common, 0.0)
    assert abs(common@hessian(10.0)@common-H_COMMON) < 1e-12
