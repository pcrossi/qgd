#!/usr/bin/env python3
"""Extremos do ansatz de Berger S3 com fluxo torsional primitivo."""

from __future__ import annotations

import numpy as np
from scipy.optimize import root


def gradient(values: np.ndarray, tau: float = 1.0, flux: int = 1) -> np.ndarray:
    radius, squash = values
    pi = np.pi
    return np.array(
        [
            -4.0 * tau * (4.0 - squash**2) / radius**3
            + 3.0 * tau * flux**2 / (pi**2 * radius**7 * squash**2)
            + 3.0 / radius,
            -4.0 * tau * squash / radius**2
            + tau * flux**2 / (pi**2 * radius**6 * squash**3)
            + 1.0 / squash,
        ]
    )


def main() -> None:
    solutions: list[np.ndarray] = []
    for initial in [(2.0, 1.0), (0.4, 1.0), (2.0, 2.0), (3.0, 0.5)]:
        result = root(gradient, initial)
        if result.success and np.all(result.x > 0):
            if not any(np.linalg.norm(result.x - old) < 1e-8 for old in solutions):
                solutions.append(result.x)

    print("Q29 — BERGER S3 COM FLUXO PRIMITIVO")
    for radius, squash in solutions:
        print(f"R={radius:.12f} q={squash:.12f} |grad|={np.linalg.norm(gradient([radius,squash])):.3e}")
        assert np.isclose(squash, 1.0, atol=1e-8)

    assert len(solutions) == 2


if __name__ == "__main__":
    main()
