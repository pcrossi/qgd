#!/usr/bin/env python3
"""Triagem local da catastrofe de dobra no ramo causal da ponte.

Calcula r=<psi,F>, b=1/2<psi,D2F[phi,phi]> e sigma_req^2=-r/b
no melhor candidato preservado antes da perda do ramo. A coordenada do modo
e normalizada na metrica euclidiana dos parametros do tiro; por isso o sinal
e diagnostico, mas o modulo nao e ainda uma variancia fisica da GDQ.
"""
from __future__ import annotations

import numpy as np

from ponte_global_local_pseudo_arclength import E_INITIAL, target
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
    _rv, jac = residual_jacobian(
        THETA, energy=energy, options=OPTIONS, log_r_cos=LOG_R_COS,
    )
    u, singular, vh = np.linalg.svd(jac, full_matrices=False)
    psi = u[:, -1]
    phi = vh[-1]
    # Orientacao fixa apenas para facilitar reproducao; -r/b nao depende da
    # troca simultanea psi -> -psi.
    if psi @ f0 < 0:
        psi = -psi
    r = float(psi @ f0)
    print("Teste reduzido de catastrofe; K_gamma=1; h=0.18")
    print("norm_residual_inf =", np.linalg.norm(f0, ord=np.inf))
    print("sigma_min_J =", singular[-1])
    print("r_projected =", r)
    estimates = []
    for dq in (2e-4, 5e-4, 1e-3, 2e-3, 5e-3, 1e-2):
        fp = field(THETA+dq*phi)
        fm = field(THETA-dq*phi)
        second = (fp-2.0*f0+fm)/(dq*dq)
        b = 0.5*float(psi @ second)
        variance = -r/b if b != 0.0 else np.nan
        estimates.append((dq, b, variance))
        print(f"dq={dq:.1e} b={b:+.9e} sigma_req2={variance:+.9e}")
    stable = np.array([x[1] for x in estimates[2:5]])
    spread = np.std(stable)/max(abs(np.mean(stable)), 1e-300)
    bmid = float(np.median(stable))
    variance = -r/bmid
    print("relative_b_spread_mid =", spread)
    print("b_representative =", bmid)
    print("sigma_req2_representative =", variance)
    print("sign_test =", "POSSIBLE" if variance > 0 else "IMPOSSIBLE")
    print("WARNING: coordinate variance; physical normalization still required")


if __name__ == "__main__":
    main()
