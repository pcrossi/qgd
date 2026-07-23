#!/usr/bin/env python3
"""Background radial GDQ com fluxo de Bismut primitivo e modo zonal l=1."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.integrate import trapezoid, solve_bvp

from solve_background_warped_q29 import EPS, N_COMPLEX, R, TAU, initial_guess


def equations_beta(beta: float):
    b0 = 1.0/(np.pi*R**3)

    def ode(x: np.ndarray, y: np.ndarray) -> np.ndarray:
        a, ap, f, fp, norm = y
        cot = np.cos(x)/np.sin(x)
        b = b0+beta*np.cos(x)
        torsion = -0.5*b**2
        q = TAU/R**2*(6.0+fp**2-5.0*ap**2)+TAU*torsion+f+5.0*a-N_COMPLEX
        app = -R**2/(2.0*TAU)-(2.0*cot-fp)*ap
        fpp = R**2/(2.0*TAU)*(1.0-q)-2.0*cot*fp+fp**2
        normp = np.exp(np.clip(-f, -700.0, 700.0))*np.sin(x)**2
        return np.vstack((ap, app, fp, fpp, normp))
    return ode


def boundary(ya: np.ndarray, yb: np.ndarray) -> np.ndarray:
    return np.array([ya[3], yb[1], yb[3], ya[4], yb[4]-1.0])


def solve_beta(beta: float, previous=None, tol: float = 2e-5):
    if previous is None:
        left = np.geomspace(EPS, 0.2, 350)
        right = np.linspace(0.2, np.pi-1e-5, 650)
        x = np.unique(np.concatenate((left, right)))
        y = initial_guess(x)
    else:
        x, y = previous.x, previous.y
    return solve_bvp(
        equations_beta(beta), boundary, x, y, tol=tol,
        max_nodes=100000, verbose=0,
    )


def norm_hopf(sol) -> float:
    x = np.linspace(EPS, np.pi-1e-5, 30000)
    a, _, f, _, _ = sol.sol(x)
    mu = np.exp(np.clip(-f, -700.0, 700.0))*np.sin(x)**2
    mu /= trapezoid(mu, x)
    return float(trapezoid(mu*R**2*np.exp(np.clip(3*a, -700.0, 700.0)), x))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--beta", type=float, default=0.0108937431)
    parser.add_argument("--steps", type=int, default=20)
    parser.add_argument("--tol", type=float, default=2e-5)
    args = parser.parse_args()

    sol = None
    rows = []
    for beta in np.linspace(0.0, args.beta, args.steps+1):
        sol = solve_beta(float(beta), sol, args.tol)
        phi = norm_hopf(sol)
        rows.append((beta, sol.success, sol.x.size, np.max(sol.rms_residuals), phi))
        if not sol.success:
            break

    phi0 = rows[0][-1]
    print("Q29 — BACKGROUND BISMUT l=1")
    print(f"b0={1/(np.pi*R**3):.12e} beta_target={args.beta:.12e}")
    print(" beta          ok nodes residual       <Phi_Q>       razão")
    for beta, ok, nodes, res, phi in rows:
        print(f"{beta: .8e} {str(ok):>5s} {nodes:5d} {res: .3e} {phi: .10e} {phi/phi0: .10e}")
    if not rows[-1][1]:
        raise SystemExit(2)


if __name__ == "__main__":
    main()
