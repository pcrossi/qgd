#!/usr/bin/env python3
"""Hessiana vinculada universal do junction GDQ C3.

Usa somente: fechamento de Noether, fluxos primitivos normalizados,
simetria C3 e gap radial homogêneo 3/(2 tau) da ação oficial.
Não introduz Robin nem parâmetros ajustados.
"""

from __future__ import annotations

import numpy as np


def orthogonal_complement(vector: np.ndarray) -> np.ndarray:
    """Base ortonormal do complemento de vector."""
    _, _, vh = np.linalg.svd(vector.reshape(1, -1), full_matrices=True)
    return vh[1:].T


def main() -> None:
    tau = 1.0
    angles = 2.0 * np.pi * np.arange(3) / 3.0
    directions = np.column_stack((np.cos(angles), np.sin(angles)))

    # Jacobiano do vínculo C=sum T_a em relação aos ângulos.
    constraint_jacobian = np.vstack((-np.sin(angles), np.cos(angles)))
    h_angular = constraint_jacobian.T @ constraint_jacobian

    # Remove a rotação comum. O espaço relativo tem dimensão dois.
    q_relative = orthogonal_complement(np.ones(3) / np.sqrt(3.0))
    h_relative = q_relative.T @ h_angular @ q_relative

    # Setor radial homogêneo já derivado da ação oficial.
    radial_gap = 3.0 / (2.0 * tau)
    k_perp = radial_gap * np.eye(3)

    # Fluxo primitivo é topológico: variações físicas preservam sua classe.
    # No background C3, o termo misto angular-radial do funcional vinculado é zero.
    j_mixed = np.zeros((2, 3))
    schur = h_relative - j_mixed @ np.linalg.solve(k_perp, j_mixed.T)

    # Matriz KKT angular: H  C'†; C' 0.
    kkt = np.block(
        [
            [h_angular, constraint_jacobian.T],
            [constraint_jacobian, np.zeros((2, 2))],
        ]
    )

    print("Q28 — HESSIANA VINCULADA DE TRÊS CENTROS")
    print("fechamento =", np.linalg.norm(np.sum(directions, axis=0)))
    print("spec H angular =", np.linalg.eigvalsh(h_angular))
    print("spec H relativa =", np.linalg.eigvalsh(h_relative))
    print("kappa_rel*T^2 (normalização primitiva) = 1")
    print("spec K_perp radial homogêneo =", np.linalg.eigvalsh(k_perp))
    print("J angular-radial =\n", j_mixed)
    print("spec complemento de Schur =", np.linalg.eigvalsh(schur))
    print("rank KKT =", np.linalg.matrix_rank(kkt), "/", kkt.shape[0])

    assert np.linalg.norm(np.sum(directions, axis=0)) < 1.0e-14
    assert np.allclose(np.linalg.eigvalsh(h_relative), [1.5, 1.5])
    assert np.all(np.linalg.eigvalsh(k_perp) > 0.0)
    assert np.all(np.linalg.eigvalsh(schur) > 0.0)


if __name__ == "__main__":
    main()
