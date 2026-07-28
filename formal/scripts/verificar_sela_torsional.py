#!/usr/bin/env python3
"""
Verificação independente da sela torsional conformal reduzida da GDQ.

Classificação:
    - avaliação direta de uma quantidade analiticamente derivada;
    - teste de consistência e de convergência do localizador de raiz;
    - não é ajuste nem previsão metrológica.

O script usa apenas a biblioteca padrão do Python. A equação resolvida é:

    q exp(-28 u) (672 u - 80) + 128 = 0,

no intervalo físico:

    0 < u < 5/42,

existente somente quando q > 8/5.
"""

from __future__ import annotations

import math


U_MAX = 5.0 / 42.0
Q_CRITICAL = 8.0 / 5.0


def slope(q: float, u: float) -> float:
    """Derivada dA_red/du."""
    return q * math.exp(-28.0 * u) * (672.0 * u - 80.0) + 128.0


def slope_derivative(q: float, u: float) -> float:
    """Segunda derivada d²A_red/du²."""
    return q * math.exp(-28.0 * u) * (2912.0 - 18816.0 * u)


def bisect_root(q: float, tolerance: float = 1.0e-14) -> float:
    """Localiza a única raiz física por bisseção, sem bibliotecas externas."""
    if not q > Q_CRITICAL:
        raise ValueError("a raiz torsional não nula exige q > 8/5")

    left = 0.0
    right = U_MAX
    f_left = slope(q, left)
    f_right = slope(q, right)

    if not (f_left < 0.0 < f_right):
        raise RuntimeError("o intervalo analítico não contém mudança de sinal")

    while right - left > tolerance:
        middle = 0.5 * (left + right)
        f_middle = slope(q, middle)
        if f_middle < 0.0:
            left = middle
        else:
            right = middle

    return 0.5 * (left + right)


def main() -> None:
    print("GDQ — sela torsional conformal normalizada")
    print(f"q crítico = {Q_CRITICAL:.12f}")
    print()
    print(
        "q       u_*                 a_* sqrt(tau)       "
        "|equação|           d²A/du²          K_aa/tau"
    )

    for q in (2.0, 3.0, 5.0, 10.0):
        u = bisect_root(q)
        dimensionless_a = math.sqrt(u)
        residual = abs(slope(q, u))
        curvature = slope_derivative(q, u)
        hessian_a_over_tau = 4.0 * u * curvature
        print(
            f"{q:4.1f}  {u: .14e}  {dimensionless_a: .14e}  "
            f"{residual: .3e}  {curvature: .12e}  "
            f"{hessian_a_over_tau: .12e}"
        )

    # Refinamento explícito para o caso de controle q=2.
    q = 2.0
    print("\nConvergência por tolerância para q=2")
    print("tolerância        u_*                 |equação|")
    for tolerance in (1.0e-6, 1.0e-8, 1.0e-10, 1.0e-12, 1.0e-14):
        u = bisect_root(q, tolerance)
        print(f"{tolerance: .1e}  {u: .14e}  {abs(slope(q, u)): .3e}")


if __name__ == "__main__":
    main()
