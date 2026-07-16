#!/usr/bin/env python3
"""Verificação algébrica do critério de Schur da Hessiana do junction."""

import numpy as np


def is_positive(matrix: np.ndarray, tolerance: float = 1.0e-12) -> bool:
    return bool(np.min(np.linalg.eigvalsh(matrix)) > tolerance)


def main() -> None:
    # Valores simbólicos de teste: verificam a equivalência algébrica, não a GDQ.
    h_rel = np.diag([1.5, 1.5])
    k_perp = np.diag([2.0, 3.0, 4.0])
    coupling = np.array([[0.2, 0.1, 0.0], [0.0, 0.1, 0.2]])

    full = np.block([[h_rel, coupling], [coupling.T, k_perp]])
    schur = h_rel - coupling @ np.linalg.inv(k_perp) @ coupling.T

    print("eig Hessiana completa =", np.linalg.eigvalsh(full))
    print("eig complemento de Schur =", np.linalg.eigvalsh(schur))
    assert is_positive(k_perp)
    assert is_positive(full) == is_positive(schur)

    normalized = (
        np.diag(1.0 / np.sqrt(np.diag(h_rel)))
        @ coupling
        @ np.diag(1.0 / np.sqrt(np.diag(k_perp)))
    )
    norm = np.linalg.svd(normalized, compute_uv=False)[0]
    print("norma normalizada =", norm)
    assert (norm < 1.0) == is_positive(schur)
    print("Critério de Schur verificado; parâmetros físicos ainda devem ser calculados.")


if __name__ == "__main__":
    main()

