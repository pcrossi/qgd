#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `testar incerteza gaussianas` associada ao capítulo `08_hilbert_quantization_uncertainty`.

Verifica a desigualdade de Heisenberg para gaussianas mínimas.

Usamos unidades hbar=1. Para uma gaussiana normalizada com desvio sigma:

    Delta x = sigma
    Delta p = hbar/(2 sigma)

Logo:

    Delta x Delta p = hbar/2.
"""

from pathlib import Path


OUT = Path(__file__).with_name("saida_testar_incerteza_gaussianas.md")


def main() -> None:
    hbar = 1.0
    sigmas = [0.25, 0.5, 1.0, 2.0, 4.0]
    lines = [
        "---",
        'title: "Saída — incerteza em gaussianas"',
        "---",
        "",
        "# Saída — incerteza em gaussianas",
        "",
        "Classificação: avaliação direta de fórmula analítica.",
        "",
        "| $\\sigma$ | $\\Delta x$ | $\\Delta p$ | produto |",
        "|---:|---:|---:|---:|",
    ]
    for sigma in sigmas:
        dx = sigma
        dp = hbar / (2.0 * sigma)
        lines.append(f"| {sigma:.2f} | {dx:.8f} | {dp:.8f} | {dx * dp:.8f} |")
    lines += [
        "",
        "Conclusão: gaussianas mínimas saturam",
        "$\\Delta x\\,\\Delta p=\\hbar/2$.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"escreveu {OUT}")


if __name__ == "__main__":
    main()

