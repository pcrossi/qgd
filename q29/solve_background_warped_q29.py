#!/usr/bin/env python3
"""Resolve o background cohomogeneidade-um reduzido da ação oficial (Q29)."""

from __future__ import annotations

import numpy as np
from scipy.integrate import cumulative_trapezoid, solve_bvp, trapezoid

R = 1.998411184770
TAU = 1.0
EPS = 0.011591040463
N_COMPLEX = 4.0


def equations(x: np.ndarray, y: np.ndarray) -> np.ndarray:
    a, ap, f, fp, norm = y
    cot = np.cos(x) / np.sin(x)
    q = TAU / R**2 * (6.0 + fp**2 - 5.0 * ap**2) + f + 5.0 * a - N_COMPLEX
    app = -R**2 / (2.0 * TAU) - (2.0 * cot - fp) * ap
    fpp = R**2 / (2.0 * TAU) * (1.0 - q) - 2.0 * cot * fp + fp**2
    normp = np.exp(np.clip(-f, -700.0, 700.0)) * np.sin(x) ** 2
    return np.vstack((ap, app, fp, fpp, normp))


def boundary(ya: np.ndarray, yb: np.ndarray) -> np.ndarray:
    return np.array(
        [
            ya[3],       # F'(epsilon)=0: condição natural dilatônica
            yb[1],       # A'(pi)=0: regularidade
            yb[3],       # F'(pi)=0: regularidade
            ya[4],       # integral começa em zero
            yb[4] - 1.0, # medida radial normalizada
        ]
    )


def initial_guess(x: np.ndarray) -> np.ndarray:
    c = R**2 / (2.0 * TAU)
    ap = c * ((np.pi - x) / 2.0 + np.sin(2.0 * x) / 4.0) / np.sin(x) ** 2
    # Escolha A(pi)=0 apenas na semente; a equação completa fixa a constante.
    reversed_integral = cumulative_trapezoid(ap[::-1], x[::-1], initial=0.0)
    a = reversed_integral[::-1]
    f0 = np.log(trapezoid(np.sin(x) ** 2, x))
    f = np.full_like(x, f0)
    fp = np.zeros_like(x)
    density = np.exp(-f) * np.sin(x) ** 2
    norm = cumulative_trapezoid(density, x, initial=0.0)
    norm /= norm[-1]
    return np.vstack((a, ap, f, fp, norm))


def solve_background(tol: float = 2.0e-5):
    left = np.geomspace(EPS, 0.2, 350)
    right = np.linspace(0.2, np.pi - 1.0e-5, 650)
    x = np.unique(np.concatenate((left, right)))
    return solve_bvp(
        equations,
        boundary,
        x,
        initial_guess(x),
        tol=tol,
        max_nodes=50000,
        verbose=0,
    )


def main() -> None:
    result = solve_background()
    values = result.sol(np.array([EPS, np.pi / 2.0, np.pi - 1.0e-5]))
    a_eps, _, f_eps, _, _ = values[:, 0]
    p_over_c_eps = np.exp(np.clip(-f_eps + 3.0 * a_eps, -700.0, 700.0)) * np.sin(EPS) ** 2 / R**2
    flux = np.exp(-f_eps) * np.sin(EPS) ** 2 * values[1, 0]

    print("Q29 — BACKGROUND WARPED ACOPLADO")
    print("success             =", result.success)
    print("status/message      =", result.status, result.message)
    print("nodes               =", result.x.size)
    print(f"max rms residual    = {np.max(result.rms_residuals):.6e}")
    print(f"A(eps), F(eps)      = {a_eps:.12e}, {f_eps:.12e}")
    print(f"A'(eps), F'(eps)    = {values[1,0]:.12e}, {values[3,0]:.12e}")
    print(f"normalization       = {values[4,-1]:.12e}")
    print(f"p(eps)/C_GDQ        = {p_over_c_eps:.12e}")
    print(f"fluxo ponderado A   = {flux:.12e}")
    if not result.success:
        raise SystemExit(2)
    expected_flux = R**2 / (2.0 * TAU)
    assert abs(values[4, -1] - 1.0) < 1e-8
    assert abs(flux - expected_flux) / expected_flux < 5e-5


if __name__ == "__main__":
    main()
