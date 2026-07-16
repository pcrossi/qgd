#!/usr/bin/env python3
"""Espectro da Hessiana angular do equilíbrio torsional em H=ker(eta_H)."""

import numpy as np


def hessian_regular_polygon(number: int) -> np.ndarray:
    angles = 2.0 * np.pi * np.arange(number) / number
    vectors = np.column_stack((np.cos(angles), np.sin(angles)))
    return vectors @ vectors.T


def main() -> None:
    for number in range(2, 9):
        hessian = hessian_regular_polygon(number)
        eigenvalues = np.linalg.eigvalsh(hessian)
        nullity = int(np.count_nonzero(np.abs(eigenvalues) < 1.0e-10))
        internal_zero_modes = max(0, nullity - 1)  # remove rotação comum
        print(
            f"N={number}: eig={np.round(eigenvalues, 10)}, "
            f"nulidade={nullity}, zeros internos={internal_zero_modes}"
        )

        assert np.all(eigenvalues >= -1.0e-10)
        expected_nullity = 1 if number == 2 else number - 2
        assert nullity == expected_nullity

    eig3 = np.linalg.eigvalsh(hessian_regular_polygon(3))
    assert np.allclose(eig3, [0.0, 1.5, 1.5], atol=1.0e-10)
    print("N=3 é o único junction não colinear sem modos zero internos.")


if __name__ == "__main__":
    main()
