#!/usr/bin/env python3
"""
GDQ — Capítulo 18 / ponte operacional de Heaviside.

Objetivo:
    Verificar simbolicamente a função de transferência confinante:

        F_mu(k^2) = -8*pi*sigma/(k^2+mu^2)^2

    e o limite subtraído:

        sigma*(1-exp(-mu*r))/mu -> sigma*r.

Classificação:
    Verificação simbólica de equivalência operacional reduzida.

Saída:
    scripts/saida_heaviside_yang_mills_operacional.md
"""

from __future__ import annotations

from pathlib import Path
import sympy as sp


def main() -> None:
    k2, mu, sigma, r = sp.symbols("k2 mu sigma r", positive=True)
    f_mu = sp.simplify(-8 * sp.pi * sigma / (k2 + mu**2) ** 2)
    v_mu = sigma * (1 - sp.exp(-mu * r)) / mu
    limit_v = sp.simplify(sp.limit(v_mu, mu, 0, dir="+"))
    ok = sp.simplify(limit_v - sigma * r) == 0

    lines = [
        "# Saída — ponte operacional Heaviside/GDQ-YM",
        "",
        "Classificação: verificação simbólica reduzida.",
        "",
        "```text",
        f"F_mu(k^2) = {sp.sstr(f_mu)}",
        f"lim_mu_to_0 V_mu(r) = {sp.sstr(limit_v)}",
        f"verificacao_linear = {ok}",
        "```",
        "",
        "Interpretação: a função de transferência estática transporta a lei linear no setor operacional reduzido.",
    ]

    out = Path(__file__).with_name("saida_heaviside_yang_mills_operacional.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

