#!/usr/bin/env python3
"""
GDQ — Capítulo 13 / Hessiana, projetor físico e complemento de Schur

Objetivo:
    Verificar, em uma matriz autocontida, a sequência usada para aparelhos
    reais:

        K_GDQ -> P_phys^T K_GDQ P_phys -> R_app

    onde:

        R_app = K_YY - K_YI K_II^{-1} K_IY.

    O script não calcula um solenoide físico real. Ele testa a álgebra
    variacional que será usada quando o background de aparelho for fornecido.

Fonte teórica:
    manuscrito/13_holonomies_ab_sagnac/notes/hessiana_projetores_resposta_interface.md

Classificação:
    Teste de consistência simbólico-numérico. Não é previsão experimental.

Saída:
    scripts/saida_verificar_schur_projetor.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def orthogonal_projector_from_constraints(constraints: np.ndarray) -> np.ndarray:
    """Return P = I - C^T (C C^T)^{-1} C for full-row-rank constraints C."""

    n = constraints.shape[1]
    gram = constraints @ constraints.T
    return np.eye(n) - constraints.T @ np.linalg.inv(gram) @ constraints


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_schur_projetor.md"

    # Toy Hessian symmetric positive on the physical subspace.
    # Coordinates are ordered as two boundary variables and three interior
    # variables before constraint projection.
    K_gdq = np.array(
        [
            [5.0, 0.8, 0.4, 0.0, 0.1],
            [0.8, 4.0, 0.2, 0.3, 0.0],
            [0.4, 0.2, 3.0, 0.5, 0.1],
            [0.0, 0.3, 0.5, 2.5, 0.4],
            [0.1, 0.0, 0.1, 0.4, 2.0],
        ],
        dtype=float,
    )

    # Two linear constraints representing one gauge direction and one flux/carga
    # restriction in this finite-dimensional model.
    C = np.array(
        [
            [1.0, -1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, 1.0, 1.0, -1.0],
        ],
        dtype=float,
    )

    P = orthogonal_projector_from_constraints(C)
    K_phys = P.T @ K_gdq @ P

    # Restrict to an explicit basis of the projected physical image by QR.
    # This avoids inverting a singular matrix in the full ambient coordinates.
    u, s, _ = np.linalg.svd(P)
    rank = int(np.sum(s > 1e-10))
    B = u[:, :rank]
    K_red = B.T @ K_gdq @ B

    # Choose one physical coordinate as boundary and the rest as interior in the
    # reduced physical basis. This is the finite-dimensional analogue of the
    # Y/I splitting after projection.
    K_YY = K_red[:1, :1]
    K_YI = K_red[:1, 1:]
    K_IY = K_red[1:, :1]
    K_II = K_red[1:, 1:]
    R = K_YY - K_YI @ np.linalg.inv(K_II) @ K_IY

    eig_KII = np.linalg.eigvalsh(K_II)
    eig_Kred = np.linalg.eigvalsh(K_red)
    idem_error = np.linalg.norm(P @ P - P)
    constraint_error = np.linalg.norm(C @ P)

    text = f"""# Saída — verificação Schur/projetor

Classificação: teste de consistência simbólico-numérico.

Este script verifica a construção:

$$
K_{{\\rm phys}}
=
P_{{\\rm phys}}^T K_{{\\rm GDQ}}P_{{\\rm phys}},
\\qquad
\\mathsf R
=
K_{{YY}}-K_{{YI}}K_{{II}}^{{-1}}K_{{IY}}.
$$

## Diagnóstico do projetor

| quantidade | valor |
|---|---:|
| posto físico | {rank} |
| erro de idempotência `||P^2-P||` | {idem_error:.12e} |
| erro de vínculo `||CP||` | {constraint_error:.12e} |

## Espectro físico reduzido

| autovalor | valor |
|---:|---:|
"""

    for i, val in enumerate(eig_Kred, 1):
        text += f"| {i} | {val:.12e} |\n"

    text += f"""
## Gap interno

| autovalor de K_II | valor |
|---:|---:|
"""

    for i, val in enumerate(eig_KII, 1):
        text += f"| {i} | {val:.12e} |\n"

    text += f"""
## Resposta de Schur

| quantidade | valor |
|---|---:|
| R_app toy | {float(R[0, 0]):.12e} |

Interpretação: a álgebra de projeção física e redução de Schur é consistente.
Para obter um solenoide real, deve-se substituir esta matriz toy pela Hessiana
da ação oficial avaliada no background físico do aparelho.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
