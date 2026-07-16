#!/usr/bin/env python3
"""Gram cinético dos Killing T3/Y sobre S3 e projeção eletromagnética Q29."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.integrate import trapezoid

from solve_background_bismut_l1_q29 import solve_beta


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--samples", type=int, default=2_000_000)
    parser.add_argument("--kbase", type=float, default=41.594825709)
    args = parser.parse_args()
    rng = np.random.default_rng(2901)
    x = rng.normal(size=(args.samples, 4))
    x /= np.linalg.norm(x, axis=1)[:, None]
    z1 = x[:, 0]+1j*x[:, 1]
    z2 = x[:, 2]+1j*x[:, 3]
    u = np.column_stack((z1, z2))
    t3u = 0.5j*np.column_stack((z1, -z2))
    yu = 0.5j*u
    gram = np.array(
        [
            [np.mean(np.sum(np.abs(t3u)**2, axis=1)),
             np.mean(np.real(np.sum(np.conj(t3u)*yu, axis=1)))],
            [np.mean(np.real(np.sum(np.conj(yu)*t3u, axis=1))),
             np.mean(np.sum(np.abs(yu)**2, axis=1))],
        ]
    )
    q = np.array([1.0, 1.0])
    qnorm = float(q@gram@q)
    single = args.kbase*gram[0, 0]
    alpha_inv_single = 4*np.pi*single
    print("Q29 — MATRIZ CINÉTICA NEUTRA DE HOPF")
    print("Gram(T3,Y) =")
    print(gram)
    print(f"||Q=T3+Y||² médio = {qnorm:.12e}")
    print(f"K_base             = {args.kbase:.12e}")
    print(f"K por gerador      = {single:.12e}")
    print(f"alpha^-1 (comum)   = {alpha_inv_single:.12e}")
    # Medida on-shell no ramo torsional zonal l=1.
    beta = 0.0108937431
    sol = None
    for value in np.linspace(0.0, beta, 21):
        sol = solve_beta(float(value), sol)
        if not sol.success:
            raise RuntimeError(sol.message)
    chi = np.linspace(0.011591040463, np.pi-1e-5, 30000)
    a, _, f, _, _ = sol.sol(chi)
    weight = np.exp(np.clip(-f+3*a, -700.0, 700.0))*np.sin(chi)**2
    # Para Y=Re(z2)=cos(chi), a média sobre o S2 transversal dá
    # <|z1|²-|z2|²>_{S2|chi}=1/3-(4/3)cos²(chi), não cos(chi).
    moment_map = (1.0-4.0*np.cos(chi)**2)/3.0
    delta_b = trapezoid(weight*moment_map, chi)/trapezoid(weight, chi)
    gram_b = 0.25*np.array([[1.0, delta_b], [delta_b, 1.0]])
    print(f"delta_B on-shell   = {delta_b:.12e}")
    print("Gram Berger-Bismut =")
    print(gram_b)
    assert np.max(np.abs(gram-0.25*np.eye(2))) < 2e-3


if __name__ == "__main__":
    main()
