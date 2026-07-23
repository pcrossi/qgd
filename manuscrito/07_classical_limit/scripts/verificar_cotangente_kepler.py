#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `verificar cotangente kepler` associada ao capítulo `07_classical_limit`.

Verifica o limite local do potencial cotangente.

No espaço cosmológico:

    K_R(r) = (1/R) cot(r/R).

Para r/R pequeno:

    K_R(r) = 1/r - r/(3R^2) + O(r^3/R^4).
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("saida_verificar_cotangente_kepler.md")


def main() -> None:
    r = 1.0
    rows = []
    for R in [5, 10, 20, 50, 100, 200]:
        exact = (1.0 / R) / math.tan(r / R)
        kepler = 1.0 / r
        corrected = kepler - r / (3.0 * R * R)
        err_kepler = abs(exact - kepler)
        err_corrected = abs(exact - corrected)
        rows.append((R, exact, err_kepler, err_corrected, err_kepler * R * R))

    lines = [
        "---",
        'title: "Saída — cotangente para Kepler"',
        "---",
        "",
        "# Saída — cotangente para Kepler",
        "",
        "Classificação: verificação assintótica de consistência.",
        "",
        "Raio local fixo: $r=1$.",
        "",
        "| $R$ | $R^{-1}\\cot(r/R)$ | erro contra $1/r$ | erro com correção $-r/(3R^2)$ | erro$\\cdot R^2$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for R, exact, err_k, err_c, scaled in rows:
        lines.append(f"| {R} | {exact:.12f} | {err_k:.6e} | {err_c:.6e} | {scaled:.8f} |")

    lines += [
        "",
        "Conclusão: o kernel cotangente tende localmente ao potencial de Kepler,",
        "com correção principal de ordem $R^{-2}$.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

