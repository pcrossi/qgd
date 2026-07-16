#!/usr/bin/env python3
"""Resíduos espectrais do resolvente dilatônico com fonte de estômato."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.sparse.linalg import eigsh

from solve_background_warped_q29 import EPS, R, solve_background
from solve_sturm_liouville_wz_q29 import assemble


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=int, default=5000)
    parser.add_argument("--modes", type=int, default=120)
    args = parser.parse_args()

    bg = solve_background()
    x = np.linspace(EPS, np.pi-1e-5, args.points)
    a, _, f, _, _ = bg.sol(x)
    mu = np.exp(np.clip(-f, -700, 700))*np.sin(x)**2
    mu /= np.trapezoid(mu, x)
    p = mu/R**2
    k, mass = assemble(x, p, mu, 0.0)

    values, vectors = eigsh(k, M=mass, k=args.modes, sigma=-1e-10, which="LM")
    order = np.argsort(values)
    values, vectors = values[order], vectors[:, order]
    values[np.abs(values) < 1e-8] = 0.0

    ones = np.ones(args.points)
    source = np.zeros(args.points)
    source[0] = 1.0
    source -= mass@ones  # delta no bordo menos mu; overlap zero com constante.
    phi = R**2*np.exp(3*a)
    phi_centered = phi-(ones@(mass@phi))/(ones@(mass@ones))

    residues = []
    susceptibility = 0.0
    for idx, lam in enumerate(values):
        mode = vectors[:, idx]
        jn = float(mode@source)
        phin = float(mode@(mass@phi_centered))
        residue = jn*phin
        residues.append(residue)
        if lam > 0:
            susceptibility += residue/lam

    residues = np.array(residues)
    print("Q29 — RESOLVENTE DILATÔNICO DO ESTÔMATO")
    print(f"points/modes             = {args.points}/{args.modes}")
    print(f"lambda_0                 = {values[0]:.12e}")
    print(f"overlap fonte modo zero  = {vectors[:,0]@source:.12e}")
    print("primeiros polos não nulos:")
    for i in range(1, min(8, args.modes)):
        print(f"  n={i:2d} lambda={values[i]:.12e} Res={residues[i]:.12e}")
    print(f"soma Res/lambda          = {susceptibility:.12e}")
    print(f"soma resíduos calculados = {residues[1:].sum():.12e}")
    assert abs(vectors[:,0]@source) < 1e-7
    assert np.any(np.abs(residues[1:]) > 1e-6)
