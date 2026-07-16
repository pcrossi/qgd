#!/usr/bin/env python3
"""Teste de consistência do exterior Berger completo da ponte GDQ.

Classificação: teste de consistência/tolerância em dados sintéticos.
Não constitui background físico nem previsão.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


TAU = 1.0


def velocities(Y: np.ndarray) -> tuple[float, ...]:
    x, y, z, u, _v, px, py, pz, pu, pv, _Z = Y
    vol = np.exp(4.0 * x + 2.0 * y + z - u)
    E = np.exp(z - 2.0 * y)
    rx = px / (TAU * vol)
    ry = py / (TAU * vol) - 4.0 * E
    rz = pz / (TAU * vol)
    ru = pu / (TAU * vol)
    dx = -rx / 16.0 - ru / 4.0
    dy = -ry / 8.0 - ru / 4.0
    dz = -rz / 2.0 - ru / 2.0
    du = -rx / 4.0 - ry / 4.0 - rz / 2.0 - 1.5 * ru
    dv = pv / (2.0 * TAU * vol)
    return dx, dy, dz, du, dv


def constraint(Y: np.ndarray, lam: float) -> float:
    _x, y, z, u, _v, *_ = Y
    dx, dy, dz, du, dv = velocities(Y)
    k2 = (
        8.0 * dx**2
        + 16.0 * dx * dy
        + 8.0 * dx * dz
        + 4.0 * dy * dz
        - 8.0 * du * dx
        - 4.0 * du * dy
        - 2.0 * du * dz
        + du**2
        + dv**2
    )
    potential = 8.0 * np.exp(-2.0 * y) - 4.0 * np.exp(2.0 * z - 4.0 * y)
    return TAU * (potential - k2) + u - 4.0 - lam


def rhs(_s: float, Y: np.ndarray, lam: float) -> np.ndarray:
    x, y, z, u, _v, _px, _py, _pz, _pu, _pv, _Z = Y
    dx, dy, dz, du, dv = velocities(Y)
    vol = np.exp(4.0 * x + 2.0 * y + z - u)
    E = np.exp(z - 2.0 * y)
    k2 = (
        8.0 * dx**2
        + 16.0 * dx * dy
        + 8.0 * dx * dz
        + 4.0 * dy * dz
        - 8.0 * du * dx
        - 4.0 * du * dy
        - 2.0 * du * dz
        + du**2
        + dv**2
    )
    K = k2 + 4.0 * E * dy + 8.0 * np.exp(-2.0 * y) - 4.0 * E**2
    F = TAU * K + u - 4.0 - lam
    dpx = 4.0 * vol * F
    dpy = vol * (
        2.0 * F
        + TAU * (-8.0 * E * dy - 16.0 * np.exp(-2.0 * y) + 16.0 * E**2)
    )
    dpz = vol * (F + TAU * (4.0 * E * dy - 8.0 * E**2))
    dpu = vol * (1.0 - F)
    dpv = 0.0
    dZ = vol
    return np.array([dx, dy, dz, du, dv, dpx, dpy, dpz, dpu, dpv, dZ])


def run(rtol: float, atol: float, max_step: float) -> tuple[float, float]:
    Y0 = np.array(
        [0.0, 0.03, -0.02, 0.12, 0.0, 0.08, -0.04, 0.025, 0.03, 0.0, 0.0]
    )
    lam = constraint(Y0, 0.0)
    sol = solve_ivp(
        lambda s, Y: rhs(s, Y, lam),
        (0.0, 0.02),
        Y0,
        method="DOP853",
        rtol=rtol,
        atol=atol,
        max_step=max_step,
    )
    residual = max(abs(constraint(Y, lam)) for Y in sol.y.T)
    return residual, sol.y[-1, -1]


if __name__ == "__main__":
    print("Teste exterior Berger completo — dados sintéticos")
    for rtol, atol, step in (
        (1e-7, 1e-9, 2e-3),
        (1e-9, 1e-11, 1e-3),
        (1e-11, 1e-13, 5e-4),
    ):
        res, Z = run(rtol, atol, step)
        print(
            f"rtol={rtol:.0e} atol={atol:.0e} step={step:.0e} "
            f"max|C_N|={res:.3e} Z={Z:.12e}"
        )
