#!/usr/bin/env python3
"""Kernel, conexão de Berry e c2 para holonomias comutativas em T5."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def kernel_block() -> tuple[np.ndarray, np.ndarray]:
    matrix = np.array(
        [
            [0, 0, 0, 0],
            [0, -2, 2, 0],
            [0, 2, 0, 0],
            [0, 0, 0, 2],
        ],
        dtype=float,
    )
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    kernel = eigenvectors[:, np.abs(eigenvalues) < 1.0e-12]
    return matrix, kernel


def berry_data() -> tuple[list[np.ndarray], list[list[np.ndarray]], float]:
    # Exemplo genérico de cinco geradores Hermitianos comutativos no dubleto.
    charges = ((1, -1), (2, 0), (0, 1), (-1, 2), (3, -2))
    generators = [np.diag(pair).astype(complex) for pair in charges]
    connection = [1j * generator for generator in generators]
    curvature: list[list[np.ndarray]] = []
    max_norm = 0.0
    for left in generators:
        row: list[np.ndarray] = []
        for right in generators:
            component = -(left @ right - right @ left)
            row.append(component)
            max_norm = max(max_norm, float(np.linalg.norm(component)))
        curvature.append(row)
    return connection, curvature, max_norm


def render() -> str:
    matrix, kernel = kernel_block()
    _, _, curvature_norm = berry_data()
    residual = np.linalg.norm(matrix @ kernel)
    orthogonality = np.linalg.norm(kernel.conj().T @ kernel - np.eye(kernel.shape[1]))

    # O kernel 4x4 tem dimensão um; a multiplicidade espectadora gera o
    # dubleto completo de dimensão dois.
    spectator = np.eye(2)
    full_modes = [np.kron(kernel[:, 0], spectator[:, index]) for index in range(2)]
    gram = np.array([[np.vdot(x, y) for y in full_modes] for x in full_modes])
    gram_error = np.linalg.norm(gram - np.eye(2))

    lines = [
        "# Q28 — Berry do kernel sobre $T^5$",
        "",
        "## Kernel",
        "",
        f"- dimensão do kernel do bloco $4\\times4$: ${kernel.shape[1]}$;",
        "- multiplicidade espectadora: $2$;",
        "- dimensão do kernel completo: $2$;",
        f"- resíduo do kernel: ${residual:.3e}$;",
        f"- erro de ortogonalidade interno: ${orthogonality:.3e}$;",
        f"- erro de Gram dos dois modos completos: ${gram_error:.3e}$.",
        "",
        "## Curvatura",
        "",
        f"Norma máxima de $[Q_i,Q_j]$: ${curvature_norm:.3e}$.",
        "",
        "$$",
        "\\mathcal F=0,",
        "\\qquad",
        "c_2(E_G)=0,",
        "\\qquad",
        "N_{ab}=0.",
        "$$",
        "",
        "O resultado vale para qualquer conjunto de geradores constantes e",
        "comutativos, não apenas para os autovalores usados no teste.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    report = render()
    output = Path(__file__).with_name("resultado_berry_kernel_t5.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
