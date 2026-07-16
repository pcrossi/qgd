#!/usr/bin/env python3
"""Verifica a matriz de Gram e a decomposição de Hodge em T^4 retangular."""

from __future__ import annotations

import numpy as np


PAIRS = ((0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3))


def permutation_sign(indices: tuple[int, ...]) -> int:
    inversions = sum(
        indices[i] > indices[j]
        for i in range(len(indices))
        for j in range(i + 1, len(indices))
    )
    return -1 if inversions % 2 else 1


def gram_top(radii: np.ndarray) -> np.ndarray:
    product = float(np.prod(radii))
    diagonal = [product / (radii[a] ** 2 * radii[b] ** 2) for a, b in PAIRS]
    return np.diag(diagonal)


def hodge_top(radii: np.ndarray) -> np.ndarray:
    """Matrix with columns equal to star(omega_pair) in the topological basis."""
    gram = gram_top(radii)
    star = np.zeros((6, 6))
    all_indices = set(range(4))
    for source_index, (a, b) in enumerate(PAIRS):
        c, d = sorted(all_indices - {a, b})
        target_index = PAIRS.index((c, d))
        sign = permutation_sign((a, b, c, d))
        coefficient = sign * gram[source_index, source_index]
        star[target_index, source_index] = coefficient
    return star


def canonical_transform(gram: np.ndarray) -> np.ndarray:
    """omega_hat = omega_top @ transform (columns in topological coordinates)."""
    return np.diag(1.0 / np.sqrt(np.diag(gram)))


def chiral_basis() -> tuple[np.ndarray, np.ndarray]:
    plus = np.zeros((6, 3))
    minus = np.zeros((6, 3))
    inv_sqrt2 = 1.0 / np.sqrt(2.0)

    # (12 ± 34), (13 ∓ 24), (14 ± 23) in zero-based pair ordering.
    plus[0, 0] = plus[5, 0] = inv_sqrt2
    plus[1, 1] = inv_sqrt2
    plus[4, 1] = -inv_sqrt2
    plus[2, 2] = plus[3, 2] = inv_sqrt2

    minus[0, 0] = inv_sqrt2
    minus[5, 0] = -inv_sqrt2
    minus[1, 1] = minus[4, 1] = inv_sqrt2
    minus[2, 2] = inv_sqrt2
    minus[3, 2] = -inv_sqrt2
    return plus, minus


def main() -> None:
    radii = np.array([1.0, 1.2, 0.8, 1.5])
    gram = gram_top(radii)
    star_top = hodge_top(radii)
    transform = canonical_transform(gram)

    # Hodge matrix in canonical coordinates: T^{-1} star_top T.
    star_can = np.linalg.solve(transform, star_top @ transform)
    plus, minus = chiral_basis()

    gram_can = transform.T @ gram @ transform
    plus_gram = plus.T @ gram_can @ plus
    minus_gram = minus.T @ gram_can @ minus
    cross_gram = plus.T @ gram_can @ minus

    star2_error = np.linalg.norm(star_top @ star_top - np.eye(6), ord=np.inf)
    plus_error = np.linalg.norm(star_can @ plus - plus, ord=np.inf)
    minus_error = np.linalg.norm(star_can @ minus + minus, ord=np.inf)
    gram_error = np.linalg.norm(gram_can - np.eye(6), ord=np.inf)
    reciprocal_error = max(
        abs(gram[0, 0] * gram[5, 5] - 1.0),
        abs(gram[1, 1] * gram[4, 4] - 1.0),
        abs(gram[2, 2] * gram[3, 3] - 1.0),
    )

    rng = np.random.default_rng(20260711)
    n = rng.normal(size=3)
    n /= np.linalg.norm(n)
    hopf_plus = plus @ n
    hopf_norm = float(hopf_plus.T @ gram_can @ hopf_plus)

    print("=" * 82)
    print("GDQ — TESTE DA MATRIZ DE GRAM TORSIONAL EM T^4")
    print("=" * 82)
    print(f"Raios: {radii}")
    print("\nDiagonal de G_top na ordem (12,13,14,23,24,34):")
    print(np.array2string(np.diag(gram), precision=10))
    print("\nMatriz de Hodge na base canônica:")
    print(np.array2string(star_can, precision=5, suppress_small=True))
    print("\nVerificações:")
    print(f"pares recíprocos                 : {reciprocal_error:.3e}")
    print(f"||star^2-I||_inf                 : {star2_error:.3e}")
    print(f"||G_can-I||_inf                  : {gram_error:.3e}")
    print(f"erro de autodualidade (+)        : {plus_error:.3e}")
    print(f"erro de anti-autodualidade (-)   : {minus_error:.3e}")
    print(f"||G_plus-I||_inf                 : {np.linalg.norm(plus_gram-np.eye(3), ord=np.inf):.3e}")
    print(f"||G_minus-I||_inf                : {np.linalg.norm(minus_gram-np.eye(3), ord=np.inf):.3e}")
    print(f"||G_cross||_inf                  : {np.linalg.norm(cross_gram, ord=np.inf):.3e}")
    print(f"norma de n^i Sigma_i^+           : {hopf_norm:.12f}")
    print("\nStatus: teste algébrico; não fixa raios nem quiralidade física.")


if __name__ == "__main__":
    main()
