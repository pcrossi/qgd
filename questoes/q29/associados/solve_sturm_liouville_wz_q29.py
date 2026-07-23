#!/usr/bin/env python3
"""Elementos finitos para os canais radiais gamma/W/Z da Q29."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import eigsh

from solve_background_warped_q29 import EPS, R, solve_background

KAPPA_OVER_C = 3.949505425268e-5
ALPHA_INV = 137.03599907


def couplings_match():
    e = np.sqrt(4.0 * np.pi / ALPHA_INV)
    return np.sqrt(8.0 / 3.0) * e, np.sqrt(8.0 / 5.0) * e


def assemble(x, p, w, boundary_mass):
    rows, cols, kvals, mvals = [], [], [], []
    for i in range(x.size - 1):
        h = x[i + 1] - x[i]
        pm = 0.5 * (p[i] + p[i + 1])
        wm = 0.5 * (w[i] + w[i + 1])
        ke = pm / h * np.array([[1.0, -1.0], [-1.0, 1.0]])
        me = wm * h / 6.0 * np.array([[2.0, 1.0], [1.0, 2.0]])
        for a in range(2):
            for b in range(2):
                rows.append(i + a)
                cols.append(i + b)
                kvals.append(ke[a, b])
                mvals.append(me[a, b])
    k = coo_matrix((kvals, (rows, cols)), shape=(x.size, x.size)).tocsr()
    m = coo_matrix((mvals, (rows, cols)), shape=(x.size, x.size)).tocsr()
    k[0, 0] += boundary_mass
    return k, m


def channel_spectrum(x, p, w, boundary_mass, count=4):
    k, m = assemble(x, p, w, boundary_mass)
    values, vectors = eigsh(k, M=m, k=count, sigma=-1.0e-9, which="LM")
    order = np.argsort(values)
    values, vectors = values[order], vectors[:, order]
    # Perfil fundamental com amplitude unitária no estômato.
    profile = vectors[:, 0] / vectors[0, 0]
    kinetic_norm = float(np.trapezoid(w * profile**2, x))
    return values, profile, kinetic_norm


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=int, default=5000)
    args = parser.parse_args()
    background = solve_background()
    if not background.success:
        raise RuntimeError(background.message)

    # Malha uniforme moderada; o background já resolve a camada de bordo.
    x = np.linspace(EPS, np.pi - 1.0e-5, args.points)
    a, _, f, _, _ = background.sol(x)
    common = np.exp(np.clip(-f + 3.0 * a, -700.0, 700.0)) * np.sin(x) ** 2
    w = common
    p = common / R**2
    p_eps = p[0]

    g, gp = couplings_match()
    boundary = {
        "gamma": 0.0,
        "W": KAPPA_OVER_C * g**2 / 4.0,
        "Z": KAPPA_OVER_C * (g**2 + gp**2) / 4.0,
    }

    results = {}
    print("Q29 — STURM–LIOUVILLE RADIAL GAMMA/W/Z")
    print(f"points         = {args.points}")
    print(f"p(epsilon)/C = {p_eps:.12e}")
    for name, mass in boundary.items():
        vals, profile, norm = channel_spectrum(x, p, w, mass)
        results[name] = (vals, norm)
        print(f"{name:5s} M_boundary/C={mass:.12e} eta={mass/p_eps:.12e}")
        print("      lambdas =", " ".join(f"{item:.10e}" for item in vals))
        print(f"      norm(Psi(eps)=1) = {norm:.12e}")

    assert abs(results["gamma"][0][0]) < 1e-7
    assert results["W"][0][0] > 0
    assert results["Z"][0][0] > results["W"][0][0]


if __name__ == "__main__":
    main()
