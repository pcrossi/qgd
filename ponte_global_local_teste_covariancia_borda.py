#!/usr/bin/env python3
"""Viabilidade de covariância positiva nos dois deslocamentos de interface.

As coordenadas 3 e 7 são log-comprimentos dos colares esquerdo e direito.
O teste calcula o jato quadrático do mapa de colagem e minimiza o resíduo
médio sobre matrizes C=L L^T. A covariância obtida, se houver, é engenharia
inversa e não uma derivação física.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import least_squares

from ponte_global_local_teste_sela_estatistica_vetorial import THETA, field


IDX = (3, 7)
STEP = 5.0e-4


def main() -> None:
    f0 = field(THETA)
    hessian = np.zeros((f0.size, 2, 2))
    for a, ia in enumerate(IDX):
        da = np.zeros_like(THETA)
        da[ia] = STEP
        hessian[:, a, a] = (
            field(THETA + da) - 2*f0 + field(THETA - da)
        )/STEP**2
    d0 = np.zeros_like(THETA)
    d1 = np.zeros_like(THETA)
    d0[IDX[0]], d1[IDX[1]] = STEP, STEP
    mixed = (
        field(THETA+d0+d1) - field(THETA+d0-d1)
        - field(THETA-d0+d1) + field(THETA-d0-d1)
    )/(4*STEP**2)
    hessian[:, 0, 1] = hessian[:, 1, 0] = mixed

    def covariance(p):
        # Cholesky com diagonal exponencial: toda matriz produzida é PSD.
        L = np.array([[np.exp(p[0]), 0.0], [p[1], np.exp(p[2])]])
        return L @ L.T

    def mean_residual(p):
        C = covariance(p)
        return f0 + 0.5*np.einsum("kij,ij->k", hessian, C)

    fit = least_squares(mean_residual, np.array([-20.0, 0.0, -20.0]),
                        xtol=1e-13, ftol=1e-13, gtol=1e-13,
                        max_nfev=4000)
    C = covariance(fit.x)
    corrected = mean_residual(fit.x)
    print("success =", fit.success)
    print("covariance =")
    print(C)
    print("covariance_eigenvalues =", np.linalg.eigvalsh(C))
    print("residual_2_before =", np.linalg.norm(f0))
    print("residual_2_after =", np.linalg.norm(corrected))
    print("residual_inf_after =", np.linalg.norm(corrected, ord=np.inf))
    print("reduction_factor =", np.linalg.norm(corrected)/np.linalg.norm(f0))
    print("NOTE: feasibility/inverse test only; covariance not derived")


if __name__ == "__main__":
    main()
