#!/usr/bin/env python3
"""
GDQ — Capítulo 4 / Projetor físico linear.

Objetivo:
    Ilustrar a construção de um projetor que remove direções de gauge e
    vínculos lineares, verificando P^2=P, P^T=P, G^T P=0 e C P=0.

Fonte teórica:
    manuscrito/04_action_consistency/04.7 - O que significa consistência em loops.md
    manuscrito/notes/action/Quociente físico, fantasmas e identidades de calibre.md

Classificação:
    Ilustração linear de quociente físico. Não é previsão física.

Equação:
    P = I - A (A^T A)^(-1) A^T,
    onde as colunas de A geram o subespaço a remover.

Domínio e contorno:
    Espaço vetorial real finito de dimensão 5.

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        matrizes pequenas explícitas.

Saída:
    saida_verificar_projetor_fisico_linear.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def main() -> None:
    dim = 5
    # Duas direções de gauge.
    g1 = np.array([1.0, 0.0, 0.0, 0.0, 0.0])
    g2 = np.array([0.0, 1.0, 1.0, 0.0, 0.0])
    # Um vínculo linear representado por covetor C; removemos sua direção normal.
    c1 = np.array([0.0, 0.0, 1.0, 1.0, 0.0])
    a = np.column_stack([g1, g2, c1])
    # Ortonormaliza por QR para evitar dependências numéricas.
    q, _ = np.linalg.qr(a)
    p = np.eye(dim) - q @ q.T
    err_idempotent = np.linalg.norm(p @ p - p)
    err_symmetric = np.linalg.norm(p.T - p)
    err_removed = np.linalg.norm(q.T @ p)
    rank = int(round(np.trace(p)))
    eig = np.linalg.eigvalsh(p)
    ok = err_idempotent < 1e-12 and err_symmetric < 1e-12 and err_removed < 1e-12 and rank == 2

    lines: list[str] = []
    lines.append("# Saída — projetor físico linear\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração linear de quociente físico. Não é previsão física.\n\n")
    lines.append("## Construção\n\n")
    lines.append("Dadas direções removidas reunidas em $A$, usa-se:\n\n")
    lines.append("$$\n")
    lines.append("P=I-A(A^TA)^{-1}A^T\n")
    lines.append("$$\n\n")
    lines.append("após ortonormalização das colunas.\n\n")
    lines.append("## Resultado\n\n")
    lines.append(f"- Dimensão total: `{dim}`.\n")
    lines.append(f"- Dimensão física projetada: `{rank}`.\n")
    lines.append(f"- Erro $P^2-P$: `{err_idempotent:.3e}`.\n")
    lines.append(f"- Erro $P^T-P$: `{err_symmetric:.3e}`.\n")
    lines.append(f"- Erro de remoção das direções: `{err_removed:.3e}`.\n")
    lines.append(f"- Autovalores de $P$: `{eig.tolist()}`.\n\n")
    lines.append("## Veredito\n\n")
    lines.append("A checagem passou.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída ilustra a álgebra do projetor. No problema GDQ real, $P_{\\rm phys}$ depende do domínio, dos vínculos e do contorno.\n")

    out = OUT / "saida_verificar_projetor_fisico_linear.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

