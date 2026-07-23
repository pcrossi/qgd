#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar positividade hilbert` associada ao capítulo `08_hilbert_quantization_uncertainty`.

Toy model de positividade e quociente por norma nula.

Uma forma positiva semidefinida G define norma, mas vetores no kernel têm
norma zero. O espaço físico é o quociente pelo kernel.
"""

from pathlib import Path
import numpy as np


OUT = Path(__file__).with_name("saida_verificar_positividade_hilbert.md")


def main() -> None:
    G = np.diag([2.0, 1.0, 0.0])
    vals = np.linalg.eigvalsh(G)
    rank = np.linalg.matrix_rank(G, tol=1e-12)
    examples = [
        np.array([1.0, 0.0, 0.0]),
        np.array([0.0, 1.0, 0.0]),
        np.array([0.0, 0.0, 1.0]),
        np.array([1.0, 1.0, 3.0]),
    ]
    lines = [
        "---",
        'title: "Saída — positividade e quociente"',
        "---",
        "",
        "# Saída — positividade e quociente",
        "",
        "Classificação: toy model algébrico.",
        "",
        f"Autovalores da forma: `{vals}`.",
        "",
        f"Posto físico após quociente pelo kernel: `{rank}`.",
        "",
        "| vetor | norma quadrática |",
        "|---|---:|",
    ]
    for v in examples:
        norm = float(v @ G @ v)
        lines.append(f"| `{v.tolist()}` | {norm:.8f} |")
    lines += [
        "",
        "Conclusão: vetores de norma nula devem ser quocientados antes do",
        "completamento Hilbertiano, como em $\\mathcal D_+/(\\mathcal N+\\mathcal G)$.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

