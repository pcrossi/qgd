#!/usr/bin/env python3
"""
GDQ — Capítulo 19 / Transporte espectral do ângulo de Weinberg

Objetivo:
    Registrar os cálculos algébricos e numéricos reduzidos da rota de
    transporte eletrofraco: condição Z_W/Z_Y=10/21, escala do cruzamento
    espectral e comparação W/Z.

Classificação:
    Diagnóstico reduzido/condicional. O script não usa m_W ou m_Z para construir
    os parâmetros; esses valores entram somente no final como comparação.

Saída:
    scripts/saida_transporte_weinberg_condicional.md
"""

from pathlib import Path
import math


def masses(v: float, alpha_inv: float, sin2: float) -> tuple[float, float, float, float]:
    alpha = 1.0 / alpha_inv
    e = math.sqrt(4.0 * math.pi * alpha)
    s = math.sqrt(sin2)
    c = math.sqrt(1.0 - sin2)
    g = e / s
    gp = e / c
    mw = 0.5 * g * v
    mz = 0.5 * math.sqrt(g * g + gp * gp) * v
    return g, gp, mw, mz


def main() -> None:
    i2 = 2.0
    iy = 10.0 / 3.0
    ratio_match = i2 / iy
    sin2_match = ratio_match / (1.0 + ratio_match)

    sin2_operational = 2.0 / 9.0
    ratio_operational = sin2_operational / (1.0 - sin2_operational)
    z_w_over_z_y = ratio_operational / ratio_match

    s_star = 5.9090386e6
    lambda0 = 126354.3162
    q_over_lambda0 = 1.0 / math.sqrt(s_star)
    q_star = lambda0 * q_over_lambda0

    v = 246.111195996
    alpha_inv_cond = 132.457669
    mw_ref = 80.379
    mz_ref = 91.1876
    g, gp, mw, mz = masses(v, alpha_inv_cond, sin2_operational)
    err_w = (mw - mw_ref) / mw_ref
    err_z = (mz - mz_ref) / mz_ref

    lines = [
        "# Saída — transporte de Weinberg condicional",
        "",
        "Classificação: diagnóstico reduzido/condicional; comparação posterior.",
        "",
        "| quantidade | valor |",
        "|---|---:|",
        f"| I2 | {i2:.12f} |",
        f"| IY | {iy:.12f} |",
        f"| g_prime^2/g^2 no ponto comum | {ratio_match:.12f} |",
        f"| sin2 ponto comum | {sin2_match:.12f} |",
        f"| sin2 operacional | {sin2_operational:.12f} |",
        f"| Z_W/Z_Y requerido | {z_w_over_z_y:.12f} |",
        f"| s_star | {s_star:.6e} |",
        f"| Q_star/Lambda0 | {q_over_lambda0:.12e} |",
        f"| Lambda0 GeV | {lambda0:.6f} |",
        f"| Q_star GeV | {q_star:.6f} |",
        f"| alpha_EW_inv condicional | {alpha_inv_cond:.6f} |",
        f"| g | {g:.12f} |",
        f"| g_prime | {gp:.12f} |",
        f"| m_W GeV | {mw:.6f} |",
        f"| erro W | {err_w:.6%} |",
        f"| m_Z GeV | {mz:.6f} |",
        f"| erro Z | {err_z:.6%} |",
        "",
        "Interpretação: a rota 2/9 + alpha_EW condicional aproxima W/Z; o cálculo forte restante é derivar Z_W/Z_Y e alpha_EW pela Hessiana global de contorno.",
    ]

    out = Path(__file__).with_name("saida_transporte_weinberg_condicional.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
