#!/usr/bin/env python3
"""Teste mínimo do momento anisotrópico inicial dos colares.

Extensão exploratória do ansatz 11D, preservado em arquivo separado. Um único
momento relativo ``p_c`` entra com orientações opostas nos dois colares. O
valor inicial de ``u`` deixa de usar a fórmula válida apenas para p_c=0 e é
obtido impondo diretamente a restrição interna.

Com 12 variáveis e 11 condições, este teste detecta se a obstrução desaparece,
mas não seleciona sozinho o módulo adicional.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
from scipy.optimize import brentq, least_squares

from ponte_global_local_integrador import Parameters, constraint as inner_constraint, rhs as inner_rhs
from ponte_global_local_solver_portas_bd import (
    LOG_R_COS, TransportOptions, causal_field, causal_initial,
    energy_ratio_from_porta_a,
)
from ponte_global_local_exterior_causal_equacoes import constraint as causal_constraint

E_INITIAL = -0.3333554761281252
OPTIONS = TransportOptions(rtol=2e-9, atol=2e-11, collar_steps=90, causal_steps=130)


def constrained_initial(theta, side, pc_value):
    j = 0 if side == "L" else 4
    a, c = np.exp(theta[j]), np.exp(theta[j+1])
    tau = np.exp(theta[8])
    pc = pc_value
    params = Parameters(tau=tau, h0=-2*c*c, pv=0.0, hopf_m=1, kappa_psi=1.0)

    def equation(u):
        state = np.array([a, c, u, 0.0, theta[j+2], pc, 0.0])
        return float(inner_constraint(state, params))

    # Seleciona continuamente a raiz mais próxima do ramo p_c=0.
    u_reference = 4-8*tau/a**2+4*tau*c**2/a**4-tau/c**2
    grid = u_reference + np.linspace(-12.0, 12.0, 241)
    values = np.array([equation(u) for u in grid])
    brackets = []
    for k in range(grid.size-1):
        if values[k] == 0 or values[k]*values[k+1] < 0:
            brackets.append((grid[k], grid[k+1]))
    if not brackets:
        raise ValueError("nenhuma raiz regular da restrição interna")
    bracket = min(brackets, key=lambda pair: abs(0.5*(pair[0]+pair[1])-u_reference))
    u = brentq(equation, *bracket, xtol=2e-13, rtol=2e-13)
    return np.array([a, c, u, 0.0, theta[j+2], pc, 0.0]), params


def residual_extended(phi, h=0.18):
    theta = np.asarray(phi[:11])
    pc_left, pc_right = float(phi[11]), float(phi[12])
    left0, p_left = constrained_initial(theta, "L", pc_left)
    right0, p_right = constrained_initial(theta, "R", pc_right)

    def collar(state, params, side):
        j = 0 if side == "L" else 4
        length = np.exp(theta[j+3])
        solution = solve_ivp(
            lambda s, y: length*inner_rhs(s, y, params), (0, 1), state,
            method="DOP853", rtol=OPTIONS.rtol, atol=OPTIONS.atol,
            max_step=1/OPTIONS.collar_steps,
        )
        if not solution.success:
            raise RuntimeError(solution.message)
        return solution.y[:, -1]

    left = collar(left0, p_left, "L")
    right = collar(right0, p_right, "R")
    exterior0, _ = causal_initial(left, np.zeros((7, 11)), theta)
    solution = solve_ivp(
        lambda s, y: np.real(causal_field(s, y, theta)), (0, 1), exterior0,
        method="DOP853", rtol=OPTIONS.rtol, atol=OPTIONS.atol,
        max_step=1/OPTIONS.causal_steps,
    )
    if not solution.success:
        raise RuntimeError(solution.message)
    q = solution.y[:, -1]
    a, c, u, _v, pia, pic, piu = right
    target = (1-h)*E_INITIAL+h
    energy = energy_ratio_from_porta_a(1.0, target)
    ce, _, _ = energy(q, theta)
    return np.array([
        q[0], q[1], q[2]-np.log(a), q[3]-np.log(c), q[4]-u,
        q[9]+a*pia, q[10]+c*pic, q[11]+piu,
        causal_constraint(exterior0[:13], np.exp(theta[8])),
        (2*q[2]+q[3])/3-LOG_R_COS, ce,
    ])


def main():
    theta = np.array([
        -1.11969325, -1.32818522, -2.16530735e-4, -1.36303888,
        -0.375378791, 1.23798835, -7.11696853e-5, -2.87139190,
        -3.33082694, -1.35391353e-3, -4.06174061e-3,
    ])
    seed = np.r_[theta, 0.0, 0.0]
    lower = np.r_[[-3,-3,-10,-4,-3,-3,-10,-4,-5,-5,-5], -0.5, -0.5]
    upper = np.r_[[3,3,10,0,3,3,10,0,3,5,5], 0.5, 0.5]

    def safe(value):
        try:
            return residual_extended(value)
        except (RuntimeError, ValueError, FloatingPointError, OverflowError):
            return np.full(11, 1e3)

    def central_jacobian(value):
        jacobian = np.empty((11, 13))
        for k in range(13):
            # O mapa e extremamente sensível aos momentos anisotrópicos na
            # garganta; passos relativos usuais atravessam a fronteira de
            # existência. Usa-se passo absoluto menor somente nesses campos.
            step = 1e-9 if k >= 11 else 5e-7*max(1.0, abs(value[k]))
            plus, minus = value.copy(), value.copy()
            plus[k] += step
            minus[k] -= step
            jacobian[:, k] = (safe(plus)-safe(minus))/(2*step)
        return jacobian

    result = least_squares(
        safe, seed, jac=central_jacobian, bounds=(lower, upper),
        x_scale=1.0, max_nfev=80, xtol=1e-11, ftol=1e-11, gtol=1e-11,
    )
    residual = safe(result.x)
    print("Exploratory independent p_c extension at h=0.18")
    print("nfev =", result.nfev, "status =", result.status)
    print("phi =", repr(result.x))
    print("p_c_left/right =", result.x[-2:])
    print("residual =", repr(residual))
    print("norm_inf =", np.linalg.norm(residual, ord=np.inf))
    print("active_mask =", result.active_mask)


if __name__ == "__main__":
    main()
