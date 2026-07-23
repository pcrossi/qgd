#!/usr/bin/env python3
"""
GDQ — Capítulo 12 / Detector Schur e visibilidade

Objetivo:
    Avaliar R_det=lambda*coth(lambda*L), Gamma_det e exp(-Gamma_det).

Fonte teórica:
    manuscrito/12_tunneling_interference_transport/notes/detector_DtN_Schur_visibilidade.md
    manuscrito/12_tunneling_interference_transport/notes/

Classificação:
    Redução efetiva/aparelho. Não é metrologia de detector material real.

Saída:
    scripts/saida_detector_schur_visibilidade.md
"""

from __future__ import annotations

import math
from pathlib import Path


def coth(x: float) -> float:
    return math.cosh(x) / math.sinh(x)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_detector_schur_visibilidade.md"

    lam = 1.3
    L = 1.0
    r_det = lam * coth(lam * L)
    zetas = [0.0, 0.5, 1.0, 2.0, 4.0]
    rows = []
    for zeta in zetas:
        gamma = 0.5 * r_det * zeta**2
        c = math.exp(-gamma)
        rows.append((zeta, gamma, c))

    table = "\n".join(f"| {z:.3f} | {g:.12f} | {c:.12f} |" for z, g, c in rows)

    text = f"""# Saída — detector Schur e visibilidade

Classificação: redução efetiva/aparelho.

Parâmetros:

- lambda = `{lam}`
- L = `{L}`
- R_det = `{r_det:.12f}`

| zeta_det | Gamma_det | exp(-Gamma_det) |
|---:|---:|---:|
{table}

Interpretação: a coerência do termo cruzado cai monotonamente com o custo
quadrático de distinguir caminhos.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
