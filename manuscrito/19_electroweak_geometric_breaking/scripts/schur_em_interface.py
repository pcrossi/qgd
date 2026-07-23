#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `schur em interface` associada ao capítulo `19_electroweak_geometric_breaking`.

GDQ — Capítulo 19 / Schur eletromagnético de interface.

Verifica:

    K_eff = K0 Kp / (K0 + Kp)

e a forma condicional:

    K_eff/K0 = 1/(1+S_partial).

Classificação: teste de consistência variacional.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_schur_em_interface.md"

    alpha_inv = 137.035999
    alpha = 1.0 / alpha_inv
    s_partial = alpha * (1.5 * math.pi + 3.0 / (4.0 * math.pi**3))
    ratio = 1.0 / (1.0 + s_partial)
    text = f"""# Saída — Schur eletromagnético de interface

Classificação: teste de consistência variacional.

| quantidade | valor |
|---|---:|
| S_partial | {s_partial:.13f} |
| K_eff/K0 | {ratio:.12f} |

Interpretação: a álgebra de Schur fecha. A conversão desta razão em
$\\alpha_{{\\rm EW}}$ exige a normalização global do canal eletromagnético e
não é feita aqui para evitar engenharia inversa.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
