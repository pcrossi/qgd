#!/usr/bin/env python3
"""Continuacao da Porta B com K_gamma=1 fixado pela Porta A.

O valor unitario vem de ``q29/projetor_causal_cauchy_normalizado.md`` e nao e
variavel de ajuste. A homotopia move primeiro o raio e depois a energia para
evitar atravessar simultaneamente duas regioes rigidas.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import least_squares

from ponte_global_local_solver_portas_bd import (
    LOG_R_COS, TransportOptions, energy_ratio_from_porta_a,
    historical_seed, residual_jacobian, residual_only,
)

LOWER = np.array([-3, -3, -10, -4, -3, -3, -10, -4, -5, -5, -5.0])
UPPER = np.array([3, 3, 10, 0, 3, 3, 10, 0, 3, 5, 5.0])
COARSE = TransportOptions(rtol=3e-7, atol=3e-9, collar_steps=25, causal_steps=35)


def solve_stage(theta, log_radius, energy_target, max_nfev=28):
    energy = energy_ratio_from_porta_a(1.0, target=energy_target)

    def fun(value):
        try:
            return residual_only(value, energy, COARSE, log_radius)
        except (RuntimeError, ValueError, FloatingPointError, OverflowError):
            # Barreira numerica: nao transforma uma trajetoria degenerada em
            # candidata e permite ao trust-region reduzir o passo.
            return np.full(11, 1.0e3)

    def jac(value):
        return residual_jacobian(value, energy, COARSE, log_radius)[1]

    result = least_squares(
        fun, theta, jac=jac, bounds=(LOWER, UPPER), x_scale="jac",
        max_nfev=max_nfev, xtol=2e-8, ftol=2e-8, gtol=2e-8,
    )
    residual = fun(result.x)
    jacobian = jac(result.x)
    singular = np.linalg.svd(jacobian, compute_uv=False)
    return result.x, result, residual, singular


def report(label, result, residual, singular):
    print(
        label,
        "nfev=", result.nfev,
        "status=", result.status,
        "inf=", np.linalg.norm(residual, ord=np.inf),
        "cost=", result.cost,
        "sigma_min=", singular[-1],
        flush=True,
    )


def main():
    theta = historical_seed()
    initial = residual_only(theta, energy_ratio_from_porta_a(1.0), COARSE)
    radius_initial = LOG_R_COS + initial[9]
    energy_initial = 1.0 + initial[10]
    print("K_gamma=1 (Porta A); no fitting", flush=True)
    print("initial radius/energy =", radius_initial, energy_initial, flush=True)

    # Ancora a semente na folha que passa pelo proprio valor inicial.
    theta, result, residual, singular = solve_stage(
        theta, radius_initial, energy_initial, max_nfev=35,
    )
    report("anchor", result, residual, singular)

    # Raio primeiro: a energia permanece na folha inicial.
    for fraction in np.linspace(0.1, 1.0, 10):
        radius = (1.0-fraction)*radius_initial + fraction*LOG_R_COS
        theta, result, residual, singular = solve_stage(
            theta, radius, energy_initial, max_nfev=24,
        )
        report(f"radius {fraction:.2f}", result, residual, singular)
        if np.linalg.norm(residual, ord=np.inf) > 2e-3:
            print("STOP: radius continuation lost the regular branch", flush=True)
            print("theta =", repr(theta), flush=True)
            print("residual =", repr(residual), flush=True)
            return 2

    # Energia depois: cruza zero sem mover simultaneamente o raio.
    for fraction in np.linspace(0.05, 1.0, 20):
        target = (1.0-fraction)*energy_initial + fraction
        theta, result, residual, singular = solve_stage(
            theta, LOG_R_COS, target, max_nfev=30,
        )
        report(f"energy {fraction:.2f}", result, residual, singular)
        if np.linalg.norm(residual, ord=np.inf) > 2e-3:
            print("STOP: energy continuation lost the regular branch", flush=True)
            print("theta =", repr(theta), flush=True)
            print("residual =", repr(residual), flush=True)
            return 3

    print("coarse_candidate =", repr(theta), flush=True)
    print("coarse_residual =", repr(residual), flush=True)
    print("coarse_singular_values =", repr(singular), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
