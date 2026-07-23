#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `polarizacao hiperons confinamento` associada ao capítulo `18_confinement_signal_problem`.

GDQ — Capítulo 18 / polarização de híperons.

Avalia a forma fenomenológica preservada:

    P = base * chi_over_delta2

com escolha reduzida que reproduz a estimativa preliminar P≈0.85%.
Classificação: fenomenologia preservada; não prova de confinamento.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_polarizacao_hiperons_confinamento.md"

    base = 0.005
    chi_over_delta2 = 1.7
    p = base * chi_over_delta2

    text = f"""# Saída — polarização de híperons

Classificação: fenomenologia preservada.

| quantidade | valor |
|---|---:|
| base térmico-vortical | {base:.12f} |
| chi_Fano/delta^2 | {chi_over_delta2:.12f} |
| P_Lambda | {p:.12f} |
| P_Lambda percentual | {100.0*p:.6f}% |

Interpretação: o valor preserva a estimativa reduzida de acoplamento
torção/vorticidade. Não é usado como prova do confinamento.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
