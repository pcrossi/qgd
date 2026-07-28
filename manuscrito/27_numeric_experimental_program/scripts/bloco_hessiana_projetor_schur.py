#!/usr/bin/env python3
"""Bloco comum GDQ: Hessiana, vínculos, projetor físico e Schur.

Classificação:
    ferramenta metodológica / verificação algébrica.

Este script não resolve um problema físico específico. Ele demonstra, com
matrizes pequenas e números fixos, o padrão algébrico que deve aparecer nos
solvers finais:

    ação oficial -> Hessiana K -> vínculos DC -> projetor P_phys
    -> Hessiana física -> complemento de Schur/DtN.

O exemplo usa uma Hessiana simétrica positiva em quatro modos:

    x0, x1 : modos de bordo/aparelho;
    x2, x3 : modos internos eliminados.

Um vínculo linear remove uma combinação de gauge/normalização. O teste confere:

    1. P_phys é idempotente;
    2. DC P_phys = 0;
    3. K_phys é simétrica;
    4. uma base ortonormal do núcleo de DC remove a direção proibida;
    5. o complemento de Schur no espaço físico é positivo.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "saida_bloco_hessiana_projetor_schur.md"


def projector_from_constraints(dc: np.ndarray, metric: np.ndarray) -> np.ndarray:
    """Constrói P = I - G^-1 DC^T (DC G^-1 DC^T)^-1 DC."""

    g_inv = np.linalg.inv(metric)
    gram = dc @ g_inv @ dc.T
    return np.eye(metric.shape[0]) - g_inv @ dc.T @ np.linalg.inv(gram) @ dc


def format_matrix(matrix: np.ndarray) -> str:
    """Formata matriz sem `[[`, evitando falso wikilink no Quartz/Obsidian."""

    rows = []
    for row in matrix:
        rows.append(" ".join(f"{value: .6f}" for value in row))
    return "\n".join(rows)


def nullspace_basis(dc: np.ndarray) -> np.ndarray:
    """Retorna colunas ortonormais que geram `ker(DC)`.

    O SVD separa o espaço físico da direção removida pelo vínculo. Assim, o
    complemento de Schur é calculado em coordenadas físicas independentes, sem
    pseudoinversa e sem reintroduzir o modo nulo projetado.
    """

    _, singular_values, vh = np.linalg.svd(dc, full_matrices=True)
    tolerance = max(dc.shape) * np.finfo(float).eps * singular_values.max()
    rank = int(np.sum(singular_values > tolerance))
    return vh[rank:].T


def main() -> None:
    # Hessiana reduzida de exemplo. Em um problema físico, esta matriz deve vir
    # da segunda variação da ação oficial avaliada no background estacionário.
    k = np.array(
        [
            [4.0, 0.3, 0.6, 0.1],
            [0.3, 3.0, 0.2, 0.4],
            [0.6, 0.2, 5.0, 0.7],
            [0.1, 0.4, 0.7, 4.5],
        ]
    )

    # Métrica quadrática do espaço de flutuações. Aqui usamos a identidade para
    # isolar a álgebra; em solvers reais ela pode ser a matriz de massa/medida.
    g = np.eye(4)

    # Um vínculo linear: remove a direção x0 - x1 + 0.5 x2 = 0.
    dc = np.array([[1.0, -1.0, 0.5, 0.0]])

    p = projector_from_constraints(dc, g)
    k_phys = p.T @ k @ p

    # Q parametriza somente ker(DC). A Hessiana reduzida Q^T K Q não possui o
    # modo nulo de vínculo. Separamos então um canal observado e dois internos.
    q = nullspace_basis(dc)
    k_reduced = q.T @ k @ q
    k_bb = k_reduced[:1, :1]
    k_bi = k_reduced[:1, 1:]
    k_ib = k_reduced[1:, :1]
    k_ii = k_reduced[1:, 1:]
    k_eff = k_bb - k_bi @ np.linalg.solve(k_ii, k_ib)

    eig_k_phys = np.linalg.eigvalsh(k_phys)
    eig_k_reduced = np.linalg.eigvalsh(k_reduced)
    eig_k_eff = np.linalg.eigvalsh(k_eff)

    checks = {
        "idempotencia norm(P^2-P)": np.linalg.norm(p @ p - p),
        "vinculo norm(DC P)": np.linalg.norm(dc @ p),
        "base fisica norm(DC Q)": np.linalg.norm(dc @ q),
        "ortonormalidade norm(Q^T Q-I)": np.linalg.norm(q.T @ q - np.eye(q.shape[1])),
        "simetria norm(Kphys-Kphys^T)": np.linalg.norm(k_phys - k_phys.T),
        "menor autovalor K reduzida": float(eig_k_reduced.min()),
        "menor autovalor K_II": float(np.linalg.eigvalsh(k_ii).min()),
        "menor autovalor K_eff": float(eig_k_eff.min()),
    }

    lines = ["# Saída — bloco Hessiana, projetor e Schur\n\n"]
    lines.append("Classificação: ferramenta metodológica / verificação algébrica.\n\n")
    lines.append("## Matrizes usadas\n\n")
    lines.append("Hessiana de exemplo $K$:\n\n")
    lines.append("```text\n")
    lines.append(format_matrix(k))
    lines.append("\n```\n\n")
    lines.append("Vínculo linearizado $DC$:\n\n")
    lines.append("```text\n")
    lines.append(format_matrix(dc))
    lines.append("\n```\n\n")
    lines.append("## Verificações\n\n")
    lines.append("| teste | valor |\n")
    lines.append("|---|---:|\n")
    for name, value in checks.items():
        lines.append(f"| {name} | {value:.12e} |\n")
    lines.append("\n## Espectro\n\n")
    lines.append("| operador | autovalores |\n")
    lines.append("|---|---|\n")
    lines.append(f"| $K_{{\\rm phys}}$ | `{np.array2string(eig_k_phys, precision=9)}` |\n")
    lines.append(f"| $Q^T KQ$ | `{np.array2string(eig_k_reduced, precision=9)}` |\n")
    lines.append(f"| $K_{{\\rm eff}}$ | `{np.array2string(eig_k_eff, precision=9)}` |\n")
    lines.append("\n## Veredito\n\n")
    lines.append(
        "O bloco algébrico remove o vínculo, constrói coordenadas ortonormais "
        "no setor físico, preserva a simetria da Hessiana e produz um bloco "
        "interno invertível e um operador efetivo de Schur positivo. "
        "Em aplicações físicas, apenas $K$, $DC$, domínio e contornos mudam.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
