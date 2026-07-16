#!/usr/bin/env python3
"""Teste de consistência das equações exteriores warped da ponte GDQ.

Classificação: teste de consistência e de tolerância. O background inicial é
sintético e não representa a sela cosmológica física.
"""

from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp


TAU = 1.0


def rhs(_s: float, Y: np.ndarray, lam: float) -> np.ndarray:
    x, y, u, v, px, py, pu, pv, _z = Y
    vol = np.exp(4.0 * x + 3.0 * y - u)

    rx = px / (TAU * vol)
    ry = py / (TAU * vol) - 4.0 * np.exp(-y)
    ru = pu / (TAU * vol)

    dx = -rx / 16.0 - ru / 4.0
    dy = -ry / 10.0 - 3.0 * ru / 10.0
    du = -rx / 4.0 - 3.0 * ry / 10.0 - 7.0 * ru / 5.0
    dv = pv / (2.0 * TAU * vol)

    k2 = (
        8.0 * dx**2
        + 4.0 * dy**2
        + 24.0 * dx * dy
        - 8.0 * du * dx
        - 6.0 * du * dy
        + du**2
        + dv**2
    )
    K = k2 + 4.0 * np.exp(-y) * dy + 4.0 * np.exp(-2.0 * y)
    F = TAU * K + u - 4.0 - lam

    dpx = 4.0 * vol * F
    dpy = vol * (
        3.0 * F
        + TAU * (-4.0 * np.exp(-y) * dy - 8.0 * np.exp(-2.0 * y))
    )
    dpu = vol * (1.0 - F)
    dpv = 0.0
    dz = vol
    return np.array([dx, dy, du, dv, dpx, dpy, dpu, dpv, dz])


def constraint(Y: np.ndarray, lam: float) -> float:
    x, y, u, _v, px, py, pu, pv, _z = Y
    vol = np.exp(4.0 * x + 3.0 * y - u)
    rx = px / (TAU * vol)
    ry = py / (TAU * vol) - 4.0 * np.exp(-y)
    ru = pu / (TAU * vol)
    dx = -rx / 16.0 - ru / 4.0
    dy = -ry / 10.0 - 3.0 * ru / 10.0
    du = -rx / 4.0 - 3.0 * ry / 10.0 - 7.0 * ru / 5.0
    dv = pv / (2.0 * TAU * vol)
    k2 = (
        8.0 * dx**2
        + 4.0 * dy**2
        + 24.0 * dx * dy
        - 8.0 * du * dx
        - 6.0 * du * dy
        + du**2
        + dv**2
    )
    return TAU * (4.0 * np.exp(-2.0 * y) - k2) + u - 4.0 - lam


def run(rtol: float, atol: float, max_step: float) -> tuple[float, float]:
    # Dados sintéticos pequenos. lambda é escolhido para satisfazer C_N(0)=0.
    Y0 = np.array([0.0, 0.0, 0.15, 0.0, 0.08, -0.05, 0.03, 0.0, 0.0])
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
    print("Teste exterior warped — background sintético")
    for rtol, atol, step in (
        (1e-7, 1e-9, 2e-3),
        (1e-9, 1e-11, 1e-3),
        (1e-11, 1e-13, 5e-4),
    ):
        res, z = run(rtol, atol, step)
        print(
            f"rtol={rtol:.0e} atol={atol:.0e} step={step:.0e} "
            f"max|C_N|={res:.3e} Z={z:.12e}"
        )
