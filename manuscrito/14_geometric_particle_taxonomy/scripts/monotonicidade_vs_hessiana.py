#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / monotonicidade e estabilidade.

Objetivo:
    Ilustrar por cálculo autocontido a diferença entre:

    1. ter um funcional de Lyapunov monotônico ao longo de um fluxo;
    2. provar estabilidade por Hessiana positiva no setor físico.

    O script usa dois modelos quadráticos:

        E_min(x,y) = 0.5*(x^2 + 2 y^2)
        E_sela(x,y) = 0.5*(x^2 - y^2)

    No primeiro, a Hessiana é positiva e o fluxo gradiente relaxa.
    No segundo, há direção negativa: a origem é ponto crítico, mas é sela.

    Isso espelha o critério GDQ: Perelman--Bismut fornece Lyapunov; a
    estabilidade de partícula exige o operador de Jacobi/Hessiana no espaço
    físico projetado.

Classificação:
    Ilustração simbólico-numérica de critério de estabilidade.
    Não é previsão física.

Saída:
    saida_monotonicidade_vs_hessiana.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


OUT = Path(__file__).resolve().parent


def gradient_flow(hessian: np.ndarray, x0: np.ndarray, dt: float, steps: int) -> tuple[np.ndarray, np.ndarray]:
    """Integra dx/dt = -H x por Euler explícito pequeno."""
    x = x0.astype(float).copy()
    energies = []
    norms = []
    for _ in range(steps):
        energies.append(0.5 * float(x @ hessian @ x))
        norms.append(float(np.linalg.norm(x)))
        x = x - dt * (hessian @ x)
    return np.array(energies), np.array(norms)


def main() -> None:
    h_min = np.diag([1.0, 2.0])
    h_saddle = np.diag([1.0, -1.0])
    x0 = np.array([0.8, 0.2])
    dt = 0.01
    steps = 600

    e_min, n_min = gradient_flow(h_min, x0, dt, steps)
    e_sad, n_sad = gradient_flow(h_saddle, x0, dt, steps)

    eig_min = np.linalg.eigvalsh(h_min)
    eig_sad = np.linalg.eigvalsh(h_saddle)

    monotone_min = bool(np.all(np.diff(e_min) <= 1e-14))

    # No caso sela, a energia também diminui para o fluxo gradiente, mas o
    # estado foge na direção negativa e a norma cresce.
    monotone_sad = bool(np.all(np.diff(e_sad) <= 1e-14))
    norm_growth_sad = float(n_sad[-1] / n_sad[0])

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Saída — monotonicidade versus Hessiana"\n')
    lines.append('---\n\n')
    lines.append("# Saída — monotonicidade versus Hessiana\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração simbólico-numérica de critério de estabilidade. Não é previsão física.\n\n")
    lines.append("## Modelos\n\n")
    lines.append("$$\n")
    lines.append("E_{\\rm min}=\\frac12(x^2+2y^2),\n")
    lines.append("\\qquad\n")
    lines.append("E_{\\rm sela}=\\frac12(x^2-y^2).\n")
    lines.append("$$\n\n")
    lines.append("Fluxo usado:\n\n")
    lines.append("$$\n")
    lines.append("\\dot X=-\\nabla E=-HX.\n")
    lines.append("$$\n\n")
    lines.append("## Hessianas\n\n")
    lines.append("| caso | autovalores da Hessiana | interpretação |\n")
    lines.append("|---|---:|---|\n")
    lines.append(f"| mínimo | {eig_min.tolist()} | estável |\n")
    lines.append(f"| sela | {eig_sad.tolist()} | instável por direção negativa |\n\n")
    lines.append("## Evolução\n\n")
    lines.append("| caso | energia inicial | energia final | energia monotônica? | razão final/inicial da norma |\n")
    lines.append("|---|---:|---:|---|---:|\n")
    lines.append(f"| mínimo | {e_min[0]:.12e} | {e_min[-1]:.12e} | {monotone_min} | {n_min[-1]/n_min[0]:.12e} |\n")
    lines.append(f"| sela | {e_sad[0]:.12e} | {e_sad[-1]:.12e} | {monotone_sad} | {norm_growth_sad:.12e} |\n\n")
    lines.append("## Veredito\n\n")
    lines.append(
        "A energia pode ser monotônica ao longo do fluxo mesmo quando o ponto crítico "
        "é uma sela. Portanto, para a GDQ, monotonicidade de Perelman--Bismut "
        "é condição de Lyapunov, mas estabilidade de sóliton exige Hessiana "
        "física sem autovalores negativos após projetar gauge, simetrias e moduli.\n"
    )

    out = OUT / "saida_monotonicidade_vs_hessiana.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
