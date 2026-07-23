#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar transporte medida ponderada` associada ao capítulo `06_global_local_bridge`.

Verificação didática do transporte de medida ponderada.

Modelo:
- densidade gaussiana normalizada no espaço local x;
- mudança de escala y = a x;
- a densidade transportada deve incluir o jacobiano inverso:

      rho_y(y) = rho_x(y/a) / a.

Sem esse fator, a norma de probabilidade não é preservada.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_transporte_medida_ponderada.md")


def rho_x(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def integrate(func, lo: float, hi: float, n: int = 200000) -> float:
    h = (hi - lo) / n
    total = 0.5 * (func(lo) + func(hi))
    for i in range(1, n):
        total += func(lo + i * h)
    return total * h


def main() -> None:
    a_values = [0.5, 1.0, 2.0, 4.0]
    rows = []
    for a in a_values:
        lo, hi = -10.0 * a, 10.0 * a
        correct = integrate(lambda y: rho_x(y / a) / a, lo, hi)
        wrong = integrate(lambda y: rho_x(y / a), lo, hi)
        rows.append((a, correct, wrong))

    lines = [
        "---",
        'title: "Saída — transporte de medida ponderada"',
        "---",
        "",
        "# Saída — transporte de medida ponderada",
        "",
        "Classificação: verificação de consistência / toy model de medida.",
        "",
        "| escala $a$ | norma com jacobiano | norma sem jacobiano |",
        "|---:|---:|---:|",
    ]
    for a, correct, wrong in rows:
        lines.append(f"| {a:.1f} | {correct:.12f} | {wrong:.12f} |")

    lines += [
        "",
        "Conclusão: o transporte correto da medida exige o fator jacobiano.",
        "No Capítulo 6, isso corresponde ao cuidado de identificar os espaços de",
        "Hilbert ponderados pela raiz do jacobiano da medida, não apenas puxar",
        "funções entre cartas.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

