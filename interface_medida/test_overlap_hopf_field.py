#!/usr/bin/env python3
"""Teste algébrico da sobreposição Hopf--campo em base anisotrópica de T^4."""

from __future__ import annotations

import numpy as np

from test_gram_t4 import canonical_transform, chiral_basis, gram_top


def random_rotation(rng: np.random.Generator) -> np.ndarray:
    matrix = rng.normal(size=(3, 3))
    q, _ = np.linalg.qr(matrix)
    if np.linalg.det(q) < 0:
        q[:, 0] *= -1
    return q


def main() -> None:
    rng = np.random.default_rng(20260712)
    radii = np.array([1.0, 1.2, 0.8, 1.5])
    gram = gram_top(radii)
    transform = canonical_transform(gram)
    plus, _ = chiral_basis()

    max_dot_error = 0.0
    max_rotation_error = 0.0
    max_norm_error = 0.0

    for _ in range(10_000):
        n = rng.normal(size=3)
        n /= np.linalg.norm(n)
        b = rng.normal(size=3)
        rotation = random_rotation(rng)

        # Coefficients in the topological basis omega_ab.
        omega_n_top = transform @ plus @ n
        omega_b_top = transform @ plus @ b
        overlap = float(omega_n_top.T @ gram @ omega_b_top)
        max_dot_error = max(max_dot_error, abs(overlap - float(n @ b)))

        norm = float(omega_n_top.T @ gram @ omega_n_top)
        max_norm_error = max(max_norm_error, abs(norm - 1.0))

        rotated_overlap = float((rotation @ n) @ (rotation @ b))
        max_rotation_error = max(
            max_rotation_error, abs(rotated_overlap - float(n @ b))
        )

    # Isotropic centered profile: odd moment vanishes exactly in symmetric
    # Gauss-Hermite quadrature, and the quadratic correction is sigma^2.
    nodes, weights = np.polynomial.hermite.hermgauss(24)
    weights /= np.sqrt(np.pi)
    sigma = 0.17
    z = np.sqrt(2.0) * sigma * nodes
    mean_z = float(np.sum(weights * z))
    mean_z2 = float(np.sum(weights * z**2))

    print("=" * 84)
    print("GDQ — TESTE DA SOBREPOSIÇÃO HOPF--CAMPO")
    print("=" * 84)
    print(f"erro máximo <Omega(n),Omega(B)> - n.B : {max_dot_error:.3e}")
    print(f"erro máximo de norma do modo de Hopf   : {max_norm_error:.3e}")
    print(f"erro máximo sob rotações simultâneas   : {max_rotation_error:.3e}")
    print("\nMomentos de perfil gaussiano centrado:")
    print(f"<z>                                    : {mean_z:.3e}")
    print(f"<z^2> numérico                         : {mean_z2:.12f}")
    print(f"sigma^2 analítico                      : {sigma**2:.12f}")
    print(f"erro em <z^2>                          : {abs(mean_z2-sigma**2):.3e}")
    print("\nStatus: teste algébrico; I_H e ell_B não foram fixados.")


if __name__ == "__main__":
    main()
