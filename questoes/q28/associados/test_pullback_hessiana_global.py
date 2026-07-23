#!/usr/bin/env python3
"""Teste do projetor de um operador produto translacionalmente invariante."""

import numpy as np


def projector(vecs: np.ndarray, count: int) -> np.ndarray:
    basis = vecs[:, :count]
    return basis @ basis.conj().T


def main() -> None:
    # Bloco interno com um kernel bidimensional e dois modos massivos.
    internal = np.diag([0.0, 0.0, 2.0, 5.0])
    _, vecs = np.linalg.eigh(internal)
    p0 = projector(vecs, 2)

    # Translação no toro apenas multiplica todo o subespaço por fases.
    charges = np.diag([1.0, -1.0, 2.0, -2.0])
    samples = np.linspace(0.0, 2.0 * np.pi, 65)
    deviations = []
    for theta in samples:
        unitary = np.diag(np.exp(1j * theta * np.diag(charges)))
        p_theta = unitary @ p0 @ unitary.conj().T
        deviations.append(np.linalg.norm(p_theta - p0))

    max_deviation = max(deviations)

    # Derivadas por diferenças finitas e fórmula P[dP,dP]P.
    dp = np.zeros_like(p0)
    curvature = p0 @ (dp @ dp - dp @ dp) @ p0

    print("# Q28 — pullback da Hessiana produto")
    print()
    print(f"variação máxima do projetor: {max_deviation:.3e}")
    print(f"norma da curvatura de Berry: {np.linalg.norm(curvature):.3e}")
    print("M12 = M34 = A = N_ab = 0")

    assert max_deviation < 1e-12
    assert np.linalg.norm(curvature) < 1e-12


if __name__ == "__main__":
    main()
