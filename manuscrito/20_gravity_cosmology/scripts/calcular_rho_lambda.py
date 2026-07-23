#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `calcular rho lambda` associada ao capítulo `20_gravity_cosmology`.
Capítulo 20 — avaliação da densidade de energia escura.

Classificação:
    avaliação direta de fórmula estrutural reduzida, condicionada ao contorno
    cosmológico global.

Fórmula:

    rho_Lambda = alpha^2 * 28 * rho_UV^p * (r_p/R_H) / c^2

com

    rho_UV^p = M_p c^2 / ((4/3) pi r_p^3)
    R_H = c/H0.

O valor observacional entra apenas como comparação final via
rho_obs = Omega_Lambda * 3 H0^2/(8 pi G).
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    c = 299_792_458.0
    G = 6.674_30e-11
    alpha_inv = 137.035_999_084
    alpha = 1.0 / alpha_inv
    m_p = 1.672_621_925_95e-27
    r_p = 0.840_778_765_450e-15
    mpc = 3.085_677_581_491_367_3e22

    H0_km_s_mpc = 67.4
    Omega_Lambda = 0.6847

    H0 = H0_km_s_mpc * 1000.0 / mpc
    R_H = c / H0
    n_cartan = 28

    volume_p = (4.0 / 3.0) * math.pi * r_p**3
    rho_uv_j = m_p * c**2 / volume_p
    dilution = r_p / R_H
    rho_eff_j = n_cartan * rho_uv_j * dilution
    rho_lambda_j = alpha**2 * rho_eff_j
    rho_lambda_kg = rho_lambda_j / c**2

    rho_crit = 3.0 * H0**2 / (8.0 * math.pi * G)
    rho_obs = Omega_Lambda * rho_crit
    omega_pred = rho_lambda_kg / rho_crit
    rel_err = (rho_lambda_kg - rho_obs) / rho_obs

    lines = [
        '---',
        'title: "Saída — densidade de energia escura"',
        '---',
        '',
        '# Saída — densidade de energia escura',
        '',
        '## Entradas',
        '',
        f'- $\\alpha^{{-1}}={alpha_inv:.12f}$',
        f'- $r_p={r_p:.12e}\\,{{\\rm m}}$',
        f'- $M_p={m_p:.12e}\\,{{\\rm kg}}$',
        f'- $H_0={H0_km_s_mpc:.6f}\\,{{\\rm km\\,s^{{-1}}\\,Mpc^{{-1}}}}$',
        f'- $\\Omega_\\Lambda={Omega_Lambda:.8f}$',
        f'- $R_H=c/H_0={R_H:.12e}\\,{{\\rm m}}$',
        '',
        '## Cadeia GDQ',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| $N_{{\\rm Cartan}}$ | `{n_cartan}` |',
        f'| $\\rho_{{\\rm UV}}^p$ | `{rho_uv_j:.12e}` J/m³ |',
        f'| $r_p/R_H$ | `{dilution:.12e}` |',
        f'| $\\rho_{{\\rm eff}}$ | `{rho_eff_j:.12e}` J/m³ |',
        f'| $\\alpha^2\\rho_{{\\rm eff}}$ | `{rho_lambda_j:.12e}` J/m³ |',
        f'| $\\rho_\\Lambda^{{\\rm GDQ}}$ | `{rho_lambda_kg:.12e}` kg/m³ |',
        '',
        '## Comparação',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| $\\rho_{{\\rm crit}}$ | `{rho_crit:.12e}` kg/m³ |',
        f'| $\\rho_\\Lambda^{{\\rm obs}}$ | `{rho_obs:.12e}` kg/m³ |',
        f'| $\\Omega_\\Lambda^{{\\rm GDQ}}$ | `{omega_pred:.12f}` |',
        f'| erro relativo | `{rel_err:+.6%}` |',
        '',
        '## Classificação',
        '',
        'Avaliação direta de fórmula estrutural reduzida. O resultado depende de $H_0$ como dado de contorno cosmológico.',
        '',
    ]

    out = Path(__file__).with_name('saida_calculo_rho_lambda.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
