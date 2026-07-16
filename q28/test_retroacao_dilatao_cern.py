#!/usr/bin/env python3
"""Modelo discreto do teorema do envelope para a medida normalizada."""

import numpy as np


def effective_free_energy(A: float, potential: np.ndarray, q: np.ndarray, sign: int) -> float:
    values = potential + sign * A * q
    minimum = values.min()
    return float(minimum - np.log(np.exp(-(values - minimum)).sum()))


def density(A: float, potential: np.ndarray, q: np.ndarray, sign: int) -> np.ndarray:
    values = potential + sign * A * q
    weights = np.exp(-(values - values.min()))
    return weights / weights.sum()


def main() -> None:
    grid = np.linspace(0.0, 2.0 * np.pi, 257, endpoint=False)
    potential = 0.3 * np.cos(grid) + 0.1 * np.cos(2.0 * grid)
    q = 0.2 + (1.0 + 0.4 * np.sin(grid)) ** 2
    step = 1.0e-5

    print("# Q28 — retroação entrópica da medida")
    print()
    for sign in (-1, 1):
        for A in (6.0, 12.0, 18.0, 24.0):
            numerical = (
                effective_free_energy(A + step, potential, q, sign)
                - effective_free_energy(A - step, potential, q, sign)
            ) / (2.0 * step)
            rho = density(A, potential, q, sign)
            envelope = sign * float(np.dot(rho, q))
            print(
                f"sinal={sign:+d} A={A:4.0f} "
                f"derivada={numerical:+.9f} envelope={envelope:+.9f}"
            )
            assert np.isclose(numerical, envelope, rtol=2e-7, atol=2e-7)
            assert numerical * sign > 0

    print()
    print("A redistribuição da medida altera a magnitude, não o sinal.")


if __name__ == "__main__":
    main()
