#!/usr/bin/env python3
"""Continuacao pseudo-arclength da Porta B perto da dobra energetica.

Mantem K_gamma=1 fixo pelo projetor causal normalizado. A variavel ``h`` e
somente o parametro de homotopia entre a energia da folha inicial e a energia
fisica; nao e parametro da teoria.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import least_squares

from ponte_global_local_solver_portas_bd import (
    LOG_R_COS, TransportOptions, energy_ratio_from_porta_a,
    residual_jacobian, residual_only,
)

E_INITIAL = -0.3333554761281252
OPTIONS = TransportOptions(rtol=1e-7, atol=1e-9, collar_steps=35, causal_steps=50)
LOWER_THETA = np.array([-3, -3, -10, -4, -3, -3, -10, -4, -5, -5, -5.0])
UPPER_THETA = np.array([3, 3, 10, 0, 3, 3, 10, 0, 3, 5, 5.0])


def target(h):
    return (1.0-h)*E_INITIAL + h


def field(theta, h):
    return residual_only(theta, energy_ratio_from_porta_a(1.0, target(h)), OPTIONS, LOG_R_COS)


def derivative(theta, h):
    jac = residual_jacobian(
        theta, energy_ratio_from_porta_a(1.0, target(h)), OPTIONS, LOG_R_COS,
    )[1]
    dh = np.zeros(11)
    dh[-1] = -(1.0-E_INITIAL)
    return np.column_stack((jac, dh))


def tangent(theta, h, previous=None):
    _u, _s, vh = np.linalg.svd(derivative(theta, h), full_matrices=True)
    vector = vh[-1]
    if previous is None:
        if vector[-1] < 0:
            vector = -vector
    elif vector @ previous < 0:
        vector = -vector
    return vector/np.linalg.norm(vector)


def correct(z_previous, tangent_previous, step, max_nfev=22):
    predicted = z_previous + step*tangent_previous

    def fun(z):
        try:
            physical = field(z[:11], z[11])
        except (RuntimeError, ValueError, FloatingPointError, OverflowError):
            physical = np.full(11, 1e3)
        return np.r_[physical, tangent_previous @ (z-predicted)]

    def jac(z):
        return np.vstack((derivative(z[:11], z[11]), tangent_previous))

    result = least_squares(
        fun, predicted, jac=jac,
        bounds=(np.r_[LOWER_THETA, -2.0], np.r_[UPPER_THETA, 2.0]),
        x_scale=1.0, max_nfev=max_nfev,
        xtol=2e-9, ftol=2e-9, gtol=2e-9,
    )
    return result, fun(result.x)


def main():
    # Melhor candidato salvo no ramo imediatamente antes da dobra.
    theta = np.array([
        -1.11969325, -1.32818522, -2.16530735e-4, -1.36303888,
        -0.375378791, 1.23798835, -7.11696853e-5, -2.87139190,
        -3.33082694, -1.35391353e-3, -4.06174061e-3,
    ])
    h = 0.18
    z = np.r_[theta, h]
    direction = tangent(theta, h)
    step = 0.20
    print("pseudo-arclength; K_gamma=1; no fitting", flush=True)
    for index in range(1, 41):
        result, residual = correct(z, direction, step)
        norm = np.linalg.norm(residual[:11], ord=np.inf)
        new_z = result.x
        new_direction = tangent(new_z[:11], new_z[11], direction)
        print(
            index, "h=", new_z[11], "ds=", step, "nfev=", result.nfev,
            "inf=", norm, "dh/ds=", new_direction[-1], flush=True,
        )
        if norm > 2e-3:
            step *= 0.5
            if step < 0.002:
                print("STOP: corrector failed", flush=True)
                print("z =", repr(new_z), flush=True)
                print("residual =", repr(residual), flush=True)
                return 2
            continue
        z, direction = new_z, new_direction
        if result.nfev < 12:
            step = min(0.30, 1.2*step)
        elif result.nfev > 20:
            step = max(0.01, 0.85*step)
        if z[11] >= 1.0:
            print("CROSSED h=1", flush=True)
            print("z =", repr(z), flush=True)
            print("residual =", repr(residual), flush=True)
            return 0
    print("STOP: arclength budget reached", flush=True)
    print("z =", repr(z), flush=True)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
