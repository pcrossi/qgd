#!/usr/bin/env python3
"""
GDQ — Capítulo 4 / Variação da medida constitutiva.

Objetivo:
    Verificar numericamente, em perturbações pequenas, a identidade
    delta U / U = -delta(f + fbar)/2 para métrica fixa e z_tau fixo.

Fonte teórica:
    manuscrito/04_action_consistency/04.3 - Campos, medida e dados estruturais.md
    manuscrito/notes/action/Primeira variação da ação GDQ - estrutura completa.md

Classificação:
    Teste simbólico de identidade constitutiva. Não é previsão física.

Equação:
    U = exp(-(f+fbar)/2)/(4*pi*z_tau)^n

Domínio e contorno:
    Checagem pontual; sem operador diferencial.

Parâmetros:
    Universais:
        n = 4
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        perturbações pequenas eps.

Saída:
    saida_verificar_variacao_medida.md
"""

from __future__ import annotations

from pathlib import Path
import math


OUT = Path(__file__).resolve().parent


def measure(real_f_sum: float, z_tau: float = 1.0, n: int = 4) -> float:
    return math.exp(-real_f_sum / 2.0) / ((4.0 * math.pi * z_tau) ** n)


def main() -> None:
    f_sum = 0.7
    u0 = measure(f_sum)
    rows = []
    for eps in [1e-2, 1e-4, 1e-6, 1e-8]:
        u1 = measure(f_sum + eps)
        finite_ratio = (u1 - u0) / u0
        linear_prediction = -eps / 2.0
        error = abs(finite_ratio - linear_prediction)
        rows.append((eps, finite_ratio, linear_prediction, error))
    ok = rows[-1][-1] < 1e-12

    lines: list[str] = []
    lines.append("# Saída — variação da medida constitutiva\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico de identidade constitutiva. Não é previsão física.\n\n")
    lines.append("## Identidade linearizada\n\n")
    lines.append("Para métrica fixa e $z_\\tau$ fixo:\n\n")
    lines.append("$$\n")
    lines.append("\\frac{\\delta\\mathcal U}{\\mathcal U}\n")
    lines.append("=-\\frac12\\delta(f+\\bar f).\n")
    lines.append("$$\n\n")
    lines.append("## Teste por diferenças finitas\n\n")
    lines.append("| $\\epsilon$ | variação relativa exata | predição linear | erro |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for eps, finite_ratio, linear_prediction, error in rows:
        lines.append(
            f"| {eps:.0e} | {finite_ratio:.16e} | "
            f"{linear_prediction:.16e} | {error:.3e} |\n"
        )
    lines.append("\n## Veredito\n\n")
    lines.append("A checagem passou no limite linear.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída verifica apenas a variação constitutiva da medida, não as equações de movimento.\n")

    out = OUT / "saida_verificar_variacao_medida.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

