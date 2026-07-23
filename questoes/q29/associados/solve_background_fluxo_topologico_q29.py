#!/usr/bin/env python3
"""Continuação do background GDQ com fluxo dilatônico no estômato."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.integrate import trapezoid, solve_bvp

from solve_background_warped_q29 import (
    EPS,
    R,
    equations,
    solve_background,
)


def boundary_flux(k: float):
    def bc(ya: np.ndarray, yb: np.ndarray) -> np.ndarray:
        # Fluxo do operador radial principal p f', p=e^{-f}sin²(chi)/R².
        flux_f = np.exp(np.clip(-ya[2], -700.0, 700.0))*np.sin(EPS)**2/R**2*ya[3]
        return np.array(
            [
                flux_f+k,
                yb[1],
                yb[3],
                ya[4],
                yb[4]-1.0,
            ]
        )
    return bc


def continue_background(k_target: float, steps: int, tol: float):
    sol = solve_background(tol=tol)
    if not sol.success:
        raise RuntimeError(sol.message)
    history = []
    for k in np.linspace(0.0, k_target, steps+1)[1:]:
        sol = solve_bvp(
            equations,
            boundary_flux(float(k)),
            sol.x,
            sol.y,
            tol=tol,
            max_nodes=100000,
            verbose=0,
        )
        xq = np.linspace(EPS, np.pi-1e-5, 20000)
        a, _, f, _, _ = sol.sol(xq)
        mu_raw = np.exp(np.clip(-f, -700.0, 700.0))*np.sin(xq)**2
        mu = mu_raw/trapezoid(mu_raw, xq)
        phi = R**2*np.exp(np.clip(3*a, -700.0, 700.0))
        mean_phi = trapezoid(mu*phi, xq)
        flux = np.exp(np.clip(-f[0], -700.0, 700.0))*np.sin(EPS)**2/R**2*sol.sol(EPS)[3]
        history.append((k, sol.success, sol.x.size, np.max(sol.rms_residuals), flux, mean_phi, a[0], f[0]))
        if not sol.success:
            break
    return sol, history


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--k", type=float, default=1.0)
    parser.add_argument("--steps", type=int, default=40)
    parser.add_argument("--tol", type=float, default=2e-5)
    args = parser.parse_args()
    base = solve_background(tol=args.tol)
    xb = np.linspace(EPS, np.pi-1e-5, 20000)
    ab, _, fb, _, _ = base.sol(xb)
    mub = np.exp(np.clip(-fb, -700.0, 700.0))*np.sin(xb)**2
    mub /= trapezoid(mub, xb)
    phi_base = trapezoid(mub*R**2*np.exp(np.clip(3*ab, -700.0, 700.0)), xb)

    _, hist = continue_background(args.k, args.steps, args.tol)
    print("Q29 — BACKGROUND COM FLUXO TOPOLÓGICO")
    print(f"K_Q relativo em k=0 = {phi_base:.12e}")
    print(" k          ok nodes    residual       fluxo          <Phi_Q>       razão")
    for row in hist:
        k, ok, nodes, res, flux, phi, _, _ = row
        print(f"{k: .6f} {str(ok):>5s} {nodes:5d} {res: .3e} {flux: .6e} {phi: .8e} {phi/phi_base: .8e}")
    if not hist or not hist[-1][1]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
