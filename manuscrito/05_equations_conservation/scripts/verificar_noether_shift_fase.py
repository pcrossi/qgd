#!/usr/bin/env python3
"""
GDQ — Capítulo 5 / Simetria global da fase.

Objetivo:
    Ilustrar que uma densidade lagrangiana que depende apenas de derivadas de
    S_R é invariante sob S_R -> S_R + constante, e que a quantidade sensível
    é o gradiente.

Fonte teórica:
    manuscrito/05_equations_conservation/05.6 - Noether, vínculos e condições de bordo.md

Classificação:
    Ilustração de simetria contínua. Não é previsão física.

Equação:
    L = 1/2 |grad S_R|^2

Domínio e contorno:
    Malha periódica 1D.

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        deslocamentos constantes da fase.

Saída:
    saida_verificar_noether_shift_fase.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def energy(s: np.ndarray, dx: float) -> float:
    grad = (np.roll(s, -1) - np.roll(s, 1)) / (2.0 * dx)
    return float(np.trapezoid(0.5 * grad * grad, dx=dx))


def main() -> None:
    n = 2000
    x = np.linspace(0.0, 2.0 * np.pi, n, endpoint=False)
    dx = x[1] - x[0]
    s = np.sin(x) + 0.25 * np.sin(3.0 * x)
    e0 = energy(s, dx)
    rows = []
    for shift in [0.0, 0.1, 1.0, -3.5, 10.0]:
        e = energy(s + shift, dx)
        rows.append((shift, e, abs(e - e0)))
    ok = all(err < 1e-12 for _, _, err in rows)

    lines: list[str] = []
    lines.append("# Saída — simetria global da fase\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração de simetria contínua. Não é previsão física.\n\n")
    lines.append("## Densidade usada\n\n")
    lines.append("$$\n")
    lines.append("L=\\frac12|\\nabla S_R|^2.\n")
    lines.append("$$\n\n")
    lines.append("Como $L$ depende apenas de $\\nabla S_R$, deslocamentos globais de $S_R$ não alteram a ação.\n\n")
    lines.append("## Resultados\n\n")
    lines.append("| deslocamento | energia | variação |\n")
    lines.append("|---:|---:|---:|\n")
    for shift, e, err in rows:
        lines.append(f"| {shift:.6g} | {e:.12e} | {err:.3e} |\n")
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída ilustra a simetria global. A corrente GDQ completa inclui $\\mathcal U$, $g$ e fatores da ação oficial.\n")

    out = OUT / "saida_verificar_noether_shift_fase.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

