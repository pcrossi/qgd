#!/usr/bin/env python3
"""Pullback exato da Hessiana de interface ao dubleto de Hopf da Q29."""

import numpy as np


def pauli_generators():
    i = 1j
    t1 = np.array([[0, 1], [1, 0]], complex) / 2
    t2 = np.array([[0, -i], [i, 0]], complex) / 2
    t3 = np.array([[1, 0], [0, -1]], complex) / 2
    hypercharge = np.eye(2, dtype=complex) / 2
    return [t1, t2, t3, hypercharge]


def real_gram(vectors):
    return np.array(
        [[np.vdot(a, b).real for b in vectors] for a in vectors], dtype=float
    )


if __name__ == "__main__":
    u0 = np.array([0, 1], complex)
    vectors = [item @ u0 for item in pauli_generators()]
    gram = real_gram(vectors)
    spectrum = np.linalg.eigvalsh(gram)
    print("Q29 — PULLBACK ROBIN DO DUBLETO DE HOPF")
    print("B =")
    print(gram)
    print("spec(B) =", spectrum)
    print("kernel neutral acoplado ~ (g', g)")
    expected = np.array(
        [[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, -1], [0, 0, -1, 1]],
        float,
    ) / 4
    assert np.allclose(gram, expected)
    assert np.allclose(spectrum, [0, 0.25, 0.25, 0.5])
