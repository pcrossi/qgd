#!/usr/bin/env python3
"""Verifica o loop geométrico da fase em R4 x T4 para Q34."""

from __future__ import annotations

import math

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import exp1


def pi_scalar_geom(q2: float, charge: float, mass: float, s0: float, points: int = 512) -> float:
    if q2 < 0 or mass <= 0 or s0 <= 0:
        raise ValueError("requer q2>=0, mass>0 e s0>0")
    z, w = leggauss(points)
    x = 0.5 * (z + 1.0)
    w = 0.5 * w
    u = x * (1.0 - x)
    weight = (1.0 - 2.0 * x) ** 2
    eta = s0 * mass**2
    integrand = weight * (exp1(eta) - exp1(s0 * (mass**2 + u * q2)))
    return float(charge**2 / (16.0 * math.pi**2) * np.dot(w, integrand))


def pi_infinity(charge: float, mass: float, s0: float) -> float:
    return charge**2 / (48.0 * math.pi**2) * float(exp1(s0 * mass**2))


def tensor(q: np.ndarray, pi_value: float) -> np.ndarray:
    q2 = float(q @ q)
    return (np.outer(q, q) - q2 * np.eye(q.size)) * pi_value


def main() -> int:
    # Unidades internas: R=1, kappa=1, n=1.
    charge = 1.0
    mass = 1.0
    s0 = 0.2749005225136263

    assert abs(pi_scalar_geom(0.0, charge, mass, s0)) < 1e-15

    q = np.array([0.31, -0.43, 0.59, 0.71])
    pi_value = pi_scalar_geom(float(q @ q), charge, mass, s0)
    ward = q @ tensor(q, pi_value)
    ward_error = float(np.linalg.norm(ward))
    assert ward_error < 1e-15

    asymptote = pi_infinity(charge, mass, s0)
    values = [pi_scalar_geom(x, charge, mass, s0) for x in np.logspace(-6, 10, 80)]
    assert np.all(np.diff(values) >= -1e-13)
    assert max(values) <= asymptote + 1e-14

    # Refinamento de quadratura.
    coarse = pi_scalar_geom(1e3, charge, mass, s0, 128)
    fine = pi_scalar_geom(1e3, charge, mass, s0, 256)
    refinement = abs(coarse - fine)
    assert refinement < 1e-12

    print(f"Pi(0)={pi_scalar_geom(0.0, charge, mass, s0):.3e}")
    print(f"erro absoluto de Ward={ward_error:.3e}")
    print(f"Pi(infinito)={asymptote:.12e}")
    print(f"erro de refinamento={refinement:.3e}")
    print("Todos os testes do loop geométrico passaram.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
