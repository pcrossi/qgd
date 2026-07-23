#!/usr/bin/env python3
"""Transporte espectral GDQ de K_W/K_Y a partir dos operadores gamma/W/Z."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.optimize import brentq
from scipy.sparse.linalg import eigsh

from solve_background_warped_q29 import EPS, R, solve_background
from solve_sturm_liouville_wz_q29 import assemble, couplings_match

KAPPA_OVER_C = 3.949505425268e-5
I2 = 2.0
IY = 10.0 / 3.0
SIN2_MATCH = 3.0 / 8.0


def spectrum(k, m, count):
    values = eigsh(k, M=m, k=count, sigma=-1.0e-9, which="LM", return_eigenvectors=False)
    values.sort()
    values[np.abs(values) < 1e-9] = 0.0
    return values


def heat(values, tau):
    return float(np.exp(-tau * values).sum())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=int, default=3500)
    parser.add_argument("--modes", type=int, default=100)
    args = parser.parse_args()

    bg = solve_background()
    x = np.linspace(EPS, np.pi - 1e-5, args.points)
    a, _, f, _, _ = bg.sol(x)
    common = np.exp(np.clip(-f + 3*a, -700, 700))*np.sin(x)**2
    p, w = common/R**2, common
    g, gp = couplings_match()
    masses = {
        "gamma": 0.0,
        "W": KAPPA_OVER_C*g*g/4.0,
        "Z": KAPPA_OVER_C*(g*g+gp*gp)/4.0,
    }
    spectra = {}
    for name, boundary_mass in masses.items():
        k, m = assemble(x, p, w, boundary_mass)
        spectra[name] = spectrum(k, m, args.modes)

    s2, c2 = SIN2_MATCH, 1.0-SIN2_MATCH

    def quantities(tau):
        hg = heat(spectra["gamma"], tau)
        hw = heat(spectra["W"], tau)
        hz = heat(spectra["Z"], tau)
        h_w3 = s2*hg + c2*hz
        h_y = c2*hg + s2*hz
        h_w_avg = (2*hw+h_w3)/3.0
        kw, ky = I2*h_w_avg, IY*h_y
        return kw, ky, kw/(kw+ky), hg, hw, hz

    taus = np.geomspace(1e-5, 1e9, 600)
    sin_values = np.array([quantities(t)[2] for t in taus])
    target = 2.0/9.0
    brackets = []
    for left, right, fl, fr in zip(taus[:-1], taus[1:], sin_values[:-1]-target, sin_values[1:]-target):
        if fl*fr < 0:
            brackets.append((left, right))
    crossing = brentq(lambda t: quantities(t)[2]-target, *brackets[0]) if brackets else np.nan

    print("Q29 — TRANSPORTE ESPECTRAL DO ÂNGULO DE WEINBERG")
    print(f"points/modes = {args.points}/{args.modes}")
    print(f"sin²(tau->0 truncado) = {quantities(1e-5)[2]:.12f}")
    for tau in (0.01, 1.0, 10.0, 1e4, 1e5, 1e6, 1e7, 1e8):
        kw, ky, sin2, hg, hw, hz = quantities(tau)
        print(f"tau={tau:7.3f} KW={kw:.8e} KY={ky:.8e} sin²={sin2:.12f}")
    print(f"cruzamento sin²=2/9: tau = {crossing:.12f}")
    if np.isfinite(crossing):
        print("quantidades no cruzamento =", quantities(crossing)[:3])
    assert abs(quantities(1e-5)[2]-SIN2_MATCH) < 2e-5
    assert brackets


if __name__ == "__main__":
    main()
