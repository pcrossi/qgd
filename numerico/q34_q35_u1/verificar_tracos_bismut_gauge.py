#!/usr/bin/env python3
"""Verifica cancelamentos de traço na conexão produto Bismut--gauge."""

import numpy as np


def traceless_random(rng: np.random.Generator, size: int) -> np.ndarray:
    matrix = rng.normal(size=(size, size))
    return matrix - np.trace(matrix) / size * np.eye(size)


def main() -> int:
    rng = np.random.default_rng(3406)
    tangent_dim = 5
    gauge_dim = 4

    curvature_b = traceless_random(rng, tangent_dim)
    curvature_f = traceless_random(rng, gauge_dim)
    identity_b = np.eye(tangent_dim)
    identity_f = np.eye(gauge_dim)

    total = np.kron(curvature_b, identity_f) + np.kron(identity_b, curvature_f)

    quadratic = np.trace(total @ total)
    separated_quadratic = (
        gauge_dim * np.trace(curvature_b @ curvature_b)
        + tangent_dim * np.trace(curvature_f @ curvature_f)
    )
    assert abs(quadratic - separated_quadratic) < 1e-10

    cubic = np.trace(total @ total @ total)
    separated_cubic = (
        gauge_dim * np.trace(curvature_b @ curvature_b @ curvature_b)
        + tangent_dim * np.trace(curvature_f @ curvature_f @ curvature_f)
    )
    assert abs(cubic - separated_cubic) < 1e-10

    # Um endomorfismo geométrico quadrático permite mistura com F^2.
    e_b = rng.normal(size=(tangent_dim, tangent_dim))
    mixed = np.trace(np.kron(e_b, curvature_f @ curvature_f))
    factorized = np.trace(e_b) * np.trace(curvature_f @ curvature_f)
    assert abs(mixed - factorized) < 1e-10

    print(f"erro quadrático: {abs(quadratic-separated_quadratic):.3e}")
    print(f"erro cúbico: {abs(cubic-separated_cubic):.3e}")
    print(f"erro misto via E_B F^2: {abs(mixed-factorized):.3e}")
    print("Cancelamentos da conexão produto verificados.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
