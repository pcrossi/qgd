#!/usr/bin/env python3
"""
GDQ — Capítulo 01 / Verificação reduzida

Objetivo:
    Comparar numericamente a estrutura de módulo dos kernels livres de Wiener
    e Feynman em uma dimensão, mostrando por que a integral de Wiener define
    uma medida positiva enquanto a integral de Feynman é oscilatória.

Fonte teórica:
    manuscrito/01_initial_problem/

Classificação:
    Teste pedagógico de consistência. Não é previsão física.

Equação:
    K_W(x,t)=(4*pi*D*t)^(-1/2)*exp(-x^2/(4Dt)).
    K_F(x,t)=(m/(2*pi*i*hbar*t))^(1/2)*exp(i*m*x^2/(2*hbar*t)).

Domínio e contorno:
    Linha real truncada numericamente em [-L,L], sem contorno físico; o corte
    é apenas numérico.

Parâmetros:
    Universais reduzidos:
        hbar=m=D=t=1.
    Numéricos:
        L=8, N=20001.
    Dados experimentais:
        Nenhum.

Saída:
    manuscrito/01_initial_problem/scripts/saida_comparar_kernel_wiener_feynman.md
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "manuscrito/01_initial_problem/scripts/saida_comparar_kernel_wiener_feynman.md"


def main() -> None:
    hbar = m = D = t = 1.0
    L = 8.0
    N = 20_001
    x = np.linspace(-L, L, N)

    K_w = (4.0 * np.pi * D * t) ** -0.5 * np.exp(-(x**2) / (4.0 * D * t))
    K_f = (m / (2.0 * np.pi * hbar * t)) ** 0.5 * np.exp(1j * m * x**2 / (2.0 * hbar * t))

    mass_w = np.trapezoid(K_w, x)
    abs_mass_f = np.trapezoid(np.abs(K_f), x)
    osc_int_f = np.trapezoid(K_f, x)

    lines = [
        "---",
        'title: "Saída — comparação Wiener/Feynman"',
        "---",
        "",
        "# Saída — comparação Wiener/Feynman",
        "",
        "| Quantidade | Valor | Interpretação |",
        "|---|---:|---|",
        f"| Integral de Wiener truncada | {mass_w:.12f} | aproxima a massa unitária positiva |",
        f"| Integral do módulo de Feynman | {abs_mass_f:.12f} | cresce com o tamanho do corte; não é medida de probabilidade |",
        f"| Integral oscilatória de Feynman, parte real | {osc_int_f.real:.12f} | cancelamento por fase |",
        f"| Integral oscilatória de Feynman, parte imaginária | {osc_int_f.imag:.12f} | cancelamento por fase |",
        "",
        "Conclusão: a diferença inicial não é de constante numérica. O kernel de "
        "Wiener é positivo e normalizável como medida; o kernel de Feynman possui "
        "fase oscilatória e exige interpretação por amplitude, fase estacionária "
        "ou continuação de Wick.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"Saída: {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
