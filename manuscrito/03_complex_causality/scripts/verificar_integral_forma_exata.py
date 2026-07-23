#!/usr/bin/env python3
"""
GDQ — Capítulo 3 / Formas exatas, períodos e contornos.

Objetivo:
    Ilustrar numericamente a diferença entre:
    1. uma forma exata regular dF, cuja integral em ciclo fechado é zero;
    2. a forma dtheta no círculo parametrizado, que representa período
       não trivial quando theta é coordenada angular multivalorada.

Fonte teórica:
    manuscrito/03_complex_causality/03.3 - O contorno causal e as formas exatas.md
    manuscrito/notes/causality/Formas exatas, períodos e resíduos no contorno causal.md

Classificação:
    Ilustração de contorno. Não é previsão física.

Equações:
    integral_gamma dF = 0 para F globalmente monovalorada.
    integral_0^{2pi} dtheta = 2pi para coordenada angular.

Domínio e contorno:
    Ciclo unitário S^1 parametrizado por theta em [0, 2pi].

Parâmetros:
    Universais:
        nenhum
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        número de pontos de quadratura.

Saída:
    saida_verificar_integral_forma_exata.md

Observação:
    Nenhum alvo experimental é usado.
"""

from __future__ import annotations

from pathlib import Path
import math
import numpy as np


OUT = Path(__file__).resolve().parent


def trapz_periodic(values: np.ndarray, theta: np.ndarray) -> float:
    return float(np.trapezoid(values, theta))


def main() -> None:
    n_values = [200, 1000, 5000, 20000]
    rows = []
    for n in n_values:
        theta = np.linspace(0.0, 2.0 * math.pi, n + 1)
        # F(theta)=cos(theta) is globally single-valued on S^1.
        dF_dtheta = -np.sin(theta)
        exact_integral = trapz_periodic(dF_dtheta, theta)
        # dtheta integrates to 2pi over one winding.
        period_integral = trapz_periodic(np.ones_like(theta), theta)
        rows.append((n, exact_integral, period_integral))

    ok_exact = abs(rows[-1][1]) < 1e-12
    ok_period = abs(rows[-1][2] - 2.0 * math.pi) < 1e-12

    lines: list[str] = []
    lines.append("# Saída — integral de forma exata e período\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Ilustração de contorno. Não é previsão física.\n\n")
    lines.append("## Construção\n\n")
    lines.append("Para $F(\\theta)=\\cos\\theta$:\n\n")
    lines.append("$$\n")
    lines.append("\\oint_{S^1}dF=F(2\\pi)-F(0)=0.\n")
    lines.append("$$\n\n")
    lines.append("Para a coordenada angular multivalorada:\n\n")
    lines.append("$$\n")
    lines.append("\\int_0^{2\\pi}d\\theta=2\\pi.\n")
    lines.append("$$\n\n")
    lines.append("## Resultados numéricos\n\n")
    lines.append("| N | $\\oint d(\\cos\\theta)$ | $\\int d\\theta$ | erro período |\n")
    lines.append("|---:|---:|---:|---:|\n")
    for n, exact_integral, period_integral in rows:
        lines.append(
            f"| {n} | {exact_integral:.16e} | {period_integral:.16e} | "
            f"{abs(period_integral - 2.0 * math.pi):.3e} |\n"
        )
    lines.append("\n## Veredito\n\n")
    if ok_exact and ok_period:
        lines.append("A checagem passou: forma exata regular cancela; período angular sobrevive.\n")
    else:
        lines.append("A checagem falhou.\n")
    lines.append("\nEsta saída ilustra a diferença entre exatidão global e período topológico. ")
    lines.append("Ela não fixa unidade de carga nem normalização física.\n")

    out = OUT / "saida_verificar_integral_forma_exata.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

