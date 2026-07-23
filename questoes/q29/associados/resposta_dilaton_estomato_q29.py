#!/usr/bin/env python3
"""Resposta linear principal do dilatão a uma fonte unitária de estômato."""

from __future__ import annotations

import argparse
import numpy as np
from scipy.integrate import cumulative_trapezoid

from solve_background_warped_q29 import EPS, R, solve_background


def reverse_integral(values, x):
    return -cumulative_trapezoid(values[::-1], x[::-1], initial=0.0)[::-1]


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--points", type=int, default=20000)
    args = parser.parse_args()
    bg = solve_background()
    x = np.linspace(EPS, np.pi-1e-5, args.points)
    a, _, f, _, _ = bg.sol(x)

    # Medida de Perelman radial, normalizada no domínio.
    mu = np.exp(np.clip(-f, -700, 700))*np.sin(x)**2
    mu /= np.trapezoid(mu, x)
    p = mu/R**2

    # Fonte compatível: delta no estômato menos densidade uniforme mu.
    # No interior, (p c')'=mu; regularidade p c'(pi)=0.
    tail = reverse_integral(mu, x)
    cprime = -tail/p
    c = cumulative_trapezoid(cprime, x, initial=0.0)
    c -= np.trapezoid(mu*c, x)

    # Inserção cinética EM da redução radial; fatores constantes cancelam.
    phi = R**2*np.exp(3*a)
    phi_mean = np.trapezoid(mu*phi, x)
    covariance = np.trapezoid(mu*(phi-phi_mean)*c, x)
    variance_c = np.trapezoid(mu*c*c, x)
    flux_left = p[0]*cprime[0]
    flux_right = p[-1]*cprime[-1]

    print("Q29 — RESPOSTA DO DILATÃO AO ESTÔMATO")
    print(f"pontos                 = {args.points}")
    print(f"normalização mu       = {np.trapezoid(mu,x):.12e}")
    print(f"média c               = {np.trapezoid(mu*c,x):.12e}")
    print(f"fluxo eps / antipolo  = {flux_left:.12e}, {flux_right:.12e}")
    print(f"<Phi_Q>               = {phi_mean:.12e}")
    print(f"Var(c)                = {variance_c:.12e}")
    print(f"Cov(Phi_Q,c)          = {covariance:.12e}")
    print(f"susceptibilidade rel. = {covariance/phi_mean:.12e}")
    assert abs(np.trapezoid(mu,x)-1) < 1e-10
    assert abs(np.trapezoid(mu*c,x)) < 1e-10
    assert abs(flux_left+1) < 2e-4
    assert abs(flux_right) < 1e-10
    assert abs(covariance) > 1e-6
