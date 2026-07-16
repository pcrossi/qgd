#!/usr/bin/env python3
"""Verifica det(g_KK)=det(h)det(G) para blocos positivos aleatórios."""

import numpy as np


def positive_matrix(rng: np.random.Generator, n: int) -> np.ndarray:
    a = rng.normal(size=(n, n))
    return a.T @ a + np.eye(n)


def main() -> None:
    rng = np.random.default_rng(30030)
    max_relative_error = 0.0

    for _ in range(100):
        h = positive_matrix(rng, 4)
        internal = positive_matrix(rng, 4)
        connection = rng.normal(size=(4, 4))

        # ds^2=h_{mu nu}dx^mu dx^nu
        #     +G_{ij}(dy^i+K^i_mu dx^mu)(dy^j+K^j_nu dx^nu).
        metric = np.block(
            [
                [h + connection.T @ internal @ connection,
                 connection.T @ internal],
                [internal @ connection, internal],
            ]
        )

        lhs = np.linalg.det(metric)
        rhs = np.linalg.det(h) * np.linalg.det(internal)
        relative_error = abs(lhs - rhs) / abs(rhs)
        max_relative_error = max(max_relative_error, relative_error)

    print(f"max_relative_error={max_relative_error:.3e}")
    if max_relative_error > 1e-10:
        raise SystemExit("Falha na identidade do determinante KK.")


if __name__ == "__main__":
    main()
