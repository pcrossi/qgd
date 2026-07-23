#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `modo hopf eletrofraco` associada ao capítulo `19_electroweak_geometric_breaking`.

GDQ — Capítulo 19 / modo de Hopf eletrofraco.

Verifica a construção reduzida:

    u=(z1,z2)^T em S^3 subset C^2,
    u ~ (1,2)_{1/2},
    Q=T3+Y preserva u0=(0,1)^T.

Classificação: teste simbólico reduzido; não usa dado experimental.
"""

from __future__ import annotations

from pathlib import Path
import numpy as np


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_modo_hopf_eletrofraco.md"

    t3 = 0.5 * np.array([[1.0, 0.0], [0.0, -1.0]])
    y = 0.5 * np.eye(2)
    q = t3 + y
    u0 = np.array([0.0, 1.0])

    t3_u0 = t3 @ u0
    y_u0 = y @ u0
    q_u0 = q @ u0
    laplace_eigenvalue_r1 = 3.0

    text = f"""# Saída — modo de Hopf eletrofraco

Classificação: teste simbólico reduzido.

| quantidade | valor |
|---|---:|
| T3 sobre u0 | {t3_u0[1]:.12f} |
| Y sobre u0 | {y_u0[1]:.12f} |
| Q=T3+Y sobre u0 | {q_u0[1]:.12e} |
| autovalor -Delta_S3 para R=1 | {laplace_eigenvalue_r1:.12f} |

Interpretação: o dupleto de Hopf realiza $(1,2)_{{1/2}}$ e a escolha
u0=(0,1)^T preserva exatamente $Q=T_3+Y$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
