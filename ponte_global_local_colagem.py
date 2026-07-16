#!/usr/bin/env python3
"""Adaptador e teste de colagem colar--exterior Berger da ponte GDQ.

Classificação: teste de consistência de interface. Os dados padrão são os do
fixture histórico do integrador interno; não representam a sela física.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp

from ponte_global_local_integrador import integrate as integrate_inner
from ponte_global_local_exterior_berger_teste import (
    constraint as exterior_constraint,
    rhs as exterior_rhs,
    velocities as exterior_velocities,
)


def inner_to_exterior(
    inner_state: np.ndarray,
    px: float,
    tau: float,
    z_accumulated: float = 0.0,
) -> np.ndarray:
    """Converte traços e momentos canônicos na interface esquerda.

    Convenção: a coordenada exterior cresce para fora do colar interno.
    """
    a, c, u, v, pi_a, pi_c, pi_u = inner_state
    if a <= 0.0 or c <= 0.0:
        raise ValueError("Traço métrico não positivo")
    # p_y delta(log a) = Pi_a delta a = Pi_a a delta(log a).
    py = a * pi_a
    pz = c * pi_c
    pv = 0.0
    return np.array(
        [0.0, np.log(a), np.log(c), u, v, px, py, pz, pi_u, pv, z_accumulated],
        dtype=float,
    )


def interface_mismatch(inner_state: np.ndarray, exterior_state: np.ndarray) -> np.ndarray:
    """Resíduo dos quatro traços/momentos na interface esquerda."""
    a, c, u, v, pi_a, pi_c, pi_u = inner_state
    x, y, z, ue, ve, _px, py, pz, pu, pv, _Z = exterior_state
    del x
    return np.array(
        [
            np.exp(y) - a,
            np.exp(z) - c,
            ue - u,
            ve - v,
            py / np.exp(y) - pi_a,
            pz / np.exp(z) - pi_c,
            pu - pi_u,
            pv,
        ]
    )


def run_fixture(inner_length: float = 0.05, exterior_length: float = 0.05):
    inner, constraints, parameters = integrate_inner(
        r0=1.0,
        tau=1.0,
        pv=0.0,
        pa0=4.0,
        length=inner_length,
        hopf_m=1,
        kappa_psi=1.0,
    )
    inner_end = inner.y[:7, -1]
    exterior_initial = inner_to_exterior(inner_end, px=0.0, tau=parameters.tau)
    # A reação lambda_N é inferida somente para satisfazer a restrição inicial
    # do fixture; não é um valor físico derivado.
    lam = exterior_constraint(exterior_initial, 0.0)
    ext = solve_ivp(
        lambda s, Y: exterior_rhs(s, Y, lam),
        (0.0, exterior_length),
        exterior_initial,
        method="DOP853",
        rtol=1e-10,
        atol=1e-12,
        max_step=exterior_length / 200.0,
    )
    c_ext = np.array([exterior_constraint(Y, lam) for Y in ext.y.T])
    join = interface_mismatch(inner_end, exterior_initial)
    far = ext.y[:, -1]
    far_velocities = np.array(exterior_velocities(far))
    # Um fechamento refletido simples exigiria velocidades nulas no meio.
    reflected_residual = far_velocities
    return {
        "inner_constraint": float(np.max(np.abs(constraints))),
        "join_residual": join,
        "exterior_constraint": float(np.max(np.abs(c_ext))),
        "reflected_residual": reflected_residual,
        "lambda_fixture": float(lam),
        "inner_end": inner_end,
        "exterior_end": far,
    }


if __name__ == "__main__":
    result = run_fixture()
    print("Teste de adaptador colar--exterior Berger")
    print(f"max|C_inner| = {result['inner_constraint']:.3e}")
    print(f"max|J_interface| = {np.max(np.abs(result['join_residual'])):.3e}")
    print(f"max|C_exterior| = {result['exterior_constraint']:.3e}")
    print(f"lambda_fixture = {result['lambda_fixture']:.12e}")
    print("resíduo refletido (xdot,ydot,zdot,udot,vdot) =")
    print(result["reflected_residual"])
    print(f"norma = {np.linalg.norm(result['reflected_residual']):.6e}")
