#!/usr/bin/env python3
"""
GDQ — Capítulo 16 / hierarquia leptônica não substitui g-2.

Testa a hipótese reduzida ruim:

    residuo_l ∝ 1/R_l

normalizada pelo resíduo do elétron. O objetivo é registrar, de forma limpa,
que a hierarquia leptônica fornece o background, mas não a fonte transversal
magnética completa.
"""

from __future__ import annotations

import math
from pathlib import Path


def koide_branches(r1: float, r2: float) -> tuple[float, float]:
    x = math.sqrt(r1)
    y = math.sqrt(r2)
    rad = math.sqrt(3.0 * r1 + 12.0 * math.sqrt(r1 * r2) + 3.0 * r2)
    return (2.0 * (x + y) - rad) ** 2, (2.0 * (x + y) + rad) ** 2


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_teste_hierarquia_nao_substitui_gmenos2.md"

    alpha_inv = 137.035999177
    alpha = 1.0 / alpha_inv
    a1 = alpha / (2.0 * math.pi)
    r_mu = 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha
    _, r_tau = koide_branches(1.0, r_mu)

    a_e_obs = 2.002319304361180 / 2.0 - 1.0
    a_mu_obs = 116592059e-11
    resid_e = a_e_obs - a1
    resid_mu = a_mu_obs - a1
    pred_mu = resid_e / r_mu
    pred_tau = resid_e / r_tau

    text = f"""# Saída — hierarquia não substitui g-2

Classificação: diagnóstico de não substituição.

| quantidade | valor |
|---|---:|
| R_mu hierarquia leptônica | {r_mu:.12f} |
| R_tau hierarquia leptônica | {r_tau:.12f} |
| a1 | {a1:.15e} |
| residuo elétron | {resid_e:.15e} |
| residuo múon observado | {resid_mu:.15e} |
| residuo múon por 1/R_mu | {pred_mu:.15e} |
| razão predito/observado | {pred_mu/resid_mu:.15e} |
| residuo tau por 1/R_tau | {pred_tau:.15e} |

Interpretação: a escala de massa/hierarquia não determina sozinha a anomalia.
O cálculo físico precisa de $H_{{C,\\ell}}^+m_{{\\perp,\\ell}}$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
