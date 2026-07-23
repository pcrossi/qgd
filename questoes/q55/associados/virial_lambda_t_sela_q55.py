#!/usr/bin/env python3
"""
Q55 — identidade de virial da sela radial e papel de lambda_T.

Classificação:
    teste de consistência / diagnóstico variacional.

Para o funcional radial reduzido:

    E[u] = K + U_T + W

com:

    K   = 1/2 ∫ |∇u|² dV
    U_T = lambda_T/2 ∫ u⁴ dV
    W   = 1/2 ∫ phi u² dV

a variação de escala u_a(r)=a^{3/2}u(ar), preservando massa, implica a
identidade de virial em 3D:

    2 K + 3 U_T + W = 0

até termos de bordo por truncamento em R.

Esta identidade não fixa lambda_T universalmente. Ela audita se a sela
numérica está de fato estacionária sob escala e prepara a fórmula que deve
receber lambda_T da Hessiana oficial.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.integrate import trapezoid

import solve_sela_densidade_bohm_q55 as radial


OUT = Path(__file__).with_name("saida_virial_lambda_t_sela_q55.md")


@dataclass(frozen=True)
class Config:
    r_min: float = 1.0e-4
    r_max: float = 25.0
    n_eval: int = 40000
    lambdas: tuple[float, ...] = (0.0, 0.5, 1.0, 3.0, 8.0, 21.0)


def compute_for_lambda(lambda_T: float, cfg: Config):
    rcfg = radial.RunConfig(r_min=cfg.r_min, r_max=cfg.r_max, lambda_T=lambda_T)
    sol = radial.solve_reduced(rcfg)
    r = np.linspace(cfg.r_min, cfg.r_max, cfg.n_eval)
    u, v, phi, mass = sol.sol(r)

    dV = 4.0 * np.pi * r**2
    K = 0.5 * trapezoid(v**2 * dV, r)
    U = 0.5 * lambda_T * trapezoid(u**4 * dV, r)
    W = 0.5 * trapezoid(phi * u**2 * dV, r)
    N = trapezoid(u**2 * dV, r)
    virial = 2.0 * K + 3.0 * U + W
    scale = abs(2.0 * K) + abs(3.0 * U) + abs(W)
    rel = virial / scale if scale else np.nan

    fit = (r > 5.0e-4) & (r < 8.0e-2)
    m_power = np.polyfit(
        np.log(r[fit]),
        np.log(np.maximum(mass[fit], 1e-300)),
        1,
    )[0]

    return {
        "lambda_T": lambda_T,
        "success": sol.success,
        "mu": float(sol.p[0]),
        "nodes": int(sol.x.size),
        "N": float(N),
        "K": float(K),
        "U": float(U),
        "W": float(W),
        "virial": float(virial),
        "virial_rel": float(rel),
        "m_power": float(m_power),
    }


def main() -> None:
    cfg = Config()
    rows = [compute_for_lambda(lam, cfg) for lam in cfg.lambdas]

    lines = []
    lines.append("# Saída — Q55 virial da sela radial e lambda_T\n")
    lines.append("Classificação: teste de consistência / diagnóstico variacional.\n")
    lines.append("## Identidade testada\n")
    lines.append("")
    lines.append("$$")
    lines.append("2K+3U_T+W=0")
    lines.append("$$")
    lines.append("")
    lines.append("com:")
    lines.append("")
    lines.append("$$")
    lines.append("K=\\frac12\\int |\\nabla u|^2dV,")
    lines.append("\\quad")
    lines.append("U_T=\\frac{\\lambda_T}{2}\\int u^4dV,")
    lines.append("\\quad")
    lines.append("W=\\frac12\\int \\phi u^2dV.")
    lines.append("$$")
    lines.append("")
    lines.append("## Varredura\n")
    lines.append("")
    lines.append("| lambda_T | success | mu | K | U_T | W | virial relativo | M power |")
    lines.append("|---:|:---:|---:|---:|---:|---:|---:|---:|")
    for row in rows:
        lines.append(
            "| {lambda_T:.6g} | {success} | {mu:.6e} | {K:.6e} | "
            "{U:.6e} | {W:.6e} | {virial_rel:.6e} | {m_power:.8f} |".format(**row)
        )
    lines.append("")
    lines.append("## Leitura\n")
    lines.append("")
    lines.append(
        "A identidade de virial audita a estacionariedade sob reescala de massa "
        "preservada. Como o domínio é truncado por `u(R)=0`, o resíduo inclui "
        "termos de bordo finitos."
    )
    lines.append("")
    lines.append(
        "O teste mostra que `lambda_T` parametriza uma família de selas reduzidas. "
        "Portanto, a virial não determina sozinha o valor universal de "
        "`lambda_T`; ela fornece a equação de balanço que o valor derivado da "
        "Hessiana oficial deve satisfazer."
    )
    lines.append("")
    lines.append("## Status\n")
    lines.append("")
    lines.append("$$")
    lines.append("\\boxed{")
    lines.append("\\text{lambda_T ainda depende da projeção torsional da Hessiana oficial.}")
    lines.append("}")
    lines.append("$$")
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(OUT)
    for row in rows:
        print(row)


if __name__ == "__main__":
    main()
