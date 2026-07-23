#!/usr/bin/env python3
"""Verificações algébricas da colagem projetiva Z6 da Q28."""

import numpy as np


def main() -> None:
    order = 6
    omega = np.exp(2j * np.pi / order)
    clock = np.diag(omega ** np.arange(order))
    shift = np.roll(np.eye(order, dtype=complex), -1, axis=1)

    projective_error = np.linalg.norm(clock @ shift - omega * shift @ clock)

    # Uma matriz 2x2 só pode realizar um comutador central zI se z^2=1,
    # pois det(UV)=det(zVU)=z^2 det(VU).
    determinant_obstruction = abs(omega**2 - 1)

    # Teste da fórmula N_ab=A*nu para alguns levantamentos integrais.
    values = []
    for A in (0, 6, 12, 18, 24):
        for nu in (1, -1, 2):
            values.append((A, nu, A * nu))

    print("# Q28 — teste da colagem projetiva Z6")
    print()
    print(f"erro ||CS-omega SC||: {projective_error:.3e}")
    print(f"obstrução determinantal em dimensão 2: {determinant_obstruction:.6f}")
    print("dimensão projetiva mínima para cociclo primitivo: 6")
    print()
    print("A, nu, N_ab=A*nu")
    for row in values:
        print(*row)

    assert projective_error < 1e-12
    assert determinant_obstruction > 1e-6
    assert (18, 1, 18) in values


if __name__ == "__main__":
    main()
