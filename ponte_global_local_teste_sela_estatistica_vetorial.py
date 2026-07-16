#!/usr/bin/env python3
"""Teste vetorial de fechamento estatistico da sela bulk--interface.

Classificacao: teste numerico de consistencia. A amplitude e expressa na
coordenada euclidiana do mapa de tiro e, portanto, nao e ainda uma variancia
fisica. O teste e mais forte que a projecao escalar: verifica se uma unica
covariancia ao longo do modo mole pode cancelar o vetor completo de residuos
ate segunda ordem.
"""
from __future__ import annotations

import numpy as np

from ponte_global_local_pseudo_arclength import target
from ponte_global_local_solver_portas_bd import (
    LOG_R_COS,
    TransportOptions,
    energy_ratio_from_porta_a,
    residual_jacobian,
    residual_only,
)


THETA = np.array([
    -1.11969325, -1.32818522, -2.16530735e-4, -1.36303888,
    -0.375378791, 1.23798835, -7.11696853e-5, -2.87139190,
    -3.33082694, -1.35391353e-3, -4.06174061e-3,
])
H = 0.18
OPTIONS = TransportOptions(
    rtol=2.0e-10, atol=2.0e-12, collar_steps=180, causal_steps=240,
)


def field(theta: np.ndarray) -> np.ndarray:
    energy = energy_ratio_from_porta_a(1.0, target(H))
    return residual_only(theta, energy, OPTIONS, LOG_R_COS)


def main() -> None:
    f0 = field(THETA)
    energy = energy_ratio_from_porta_a(1.0, target(H))
    _, jac = residual_jacobian(
        THETA, energy=energy, options=OPTIONS, log_r_cos=LOG_R_COS,
    )
    u, singular, vh = np.linalg.svd(jac, full_matrices=False)
    psi = u[:, -1]
    phi = vh[-1]
    if psi @ f0 < 0.0:
        psi = -psi

    print("Teste vetorial de sela estatistica; K_gamma=1; h=0.18")
    print("norm_F_2 =", np.linalg.norm(f0))
    print("norm_F_inf =", np.linalg.norm(f0, ord=np.inf))
    print("sigma_min_J =", singular[-1])
    print("left_projection_fraction =", abs(psi @ f0)/np.linalg.norm(f0))

    for dq in (5.0e-4, 1.0e-3, 2.0e-3, 5.0e-3):
        fp = field(THETA + dq*phi)
        fm = field(THETA - dq*phi)
        curvature = 0.5*(fp - 2.0*f0 + fm)/(dq*dq)

        # Minimiza ||F + variance * curvature||_2 sem impor o alvo.
        variance_ls = -float(curvature @ f0)/float(curvature @ curvature)
        mean_residual = f0 + variance_ls*curvature
        projected_variance = -float(psi @ f0)/float(psi @ curvature)
        projected_residual = f0 + projected_variance*curvature

        print(f"dq={dq:.1e}")
        print("  variance_vector_ls =", variance_ls)
        print("  residual_2_after_ls =", np.linalg.norm(mean_residual))
        print("  residual_inf_after_ls =", np.linalg.norm(mean_residual, ord=np.inf))
        print("  reduction_factor_2 =", np.linalg.norm(mean_residual)/np.linalg.norm(f0))
        print("  variance_projected =", projected_variance)
        print("  projected_component_after =", psi @ projected_residual)
        print("  full_residual_2_projected =", np.linalg.norm(projected_residual))


if __name__ == "__main__":
    main()
