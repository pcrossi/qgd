#!/usr/bin/env python3
"""Q39 — previsão da terceira ressonância pela condição Koide-GDQ.

Classificação:
    avaliação direta de uma identidade geométrica reduzida.
    Não usa a terceira massa como alvo.
"""

from __future__ import annotations

import math
from pathlib import Path


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV


def muon_ratio(alpha: float = ALPHA) -> float:
    return 1.5 / alpha + 6.0 / 5.0 + 2.0 * alpha


def koide_q(*ratios: float) -> float:
    amps = [math.sqrt(r) for r in ratios]
    return sum(ratios) / (sum(amps) ** 2)


def third_resonance(r1: float, r2: float) -> tuple[float, float]:
    x = math.sqrt(r1)
    y = math.sqrt(r2)
    root = math.sqrt(3.0 * x * x + 12.0 * x * y + 3.0 * y * y)
    z_minus = 2.0 * (x + y) - root
    z_plus = 2.0 * (x + y) + root
    return z_minus * z_minus, z_plus * z_plus


def main() -> None:
    base = Path(__file__).resolve().parent
    r_e = 1.0
    r_mu = muon_ratio()
    r_shadow, r_tau = third_resonance(r_e, r_mu)
    q_val = koide_q(r_e, r_mu, r_tau)

    lines = [
        "# Q39 — previsão da terceira ressonância pela condição Koide-GDQ",
        "",
        "## Classificação",
        "",
        "Avaliação direta da identidade geométrica reduzida. O valor de tau",
        "não entra como alvo.",
        "",
        "## Entradas",
        "",
        f"- `alpha_inv = {ALPHA_INV:.12f}`",
        f"- `R_e = {r_e:.15f}`",
        f"- `R_mu = 3/(2 alpha)+6/5+2 alpha = {r_mu:.15f}`",
        "",
        "## Fórmula",
        "",
        "Dados `x=sqrt(R1)` e `y=sqrt(R2)`:",
        "",
        "$$",
        "R_{3,\\pm}",
        "=",
        "\\left[",
        "2(x+y)\\pm\\sqrt{3x^2+12xy+3y^2}",
        "\\right]^2.",
        "$$",
        "",
        "## Saída",
        "",
        f"- ramo leve/sombra `R_3_minus = {r_shadow:.15f}`",
        f"- ramo pesado/físico `R_3_plus = {r_tau:.15f}`",
        f"- `Q(R_e,R_mu,R_3_plus) = {q_val:.15f}`",
        "",
        "## Leitura GDQ",
        "",
        "O ramo pesado é o tau no setor leptônico carregado. O ramo leve é uma",
        "solução matemática da mesma condição angular e não deve ser promovido a",
        "partícula sem estabilidade e interpretação pela Hessiana física.",
    ]

    (base / "saida_predizer_terceira_koide_gdq_q39.md").write_text(
        "\n".join(lines) + "\n", encoding="utf-8"
    )


if __name__ == "__main__":
    main()
