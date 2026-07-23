#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `hiperfina zemach hidrogenio` associada ao capítulo `22_hydrogen_atom`.
Capítulo 22 — hiperfina, anomalia líder e Zemach.

Classificação:
    comparação fenomenológica quando usa momento magnético experimental do
    próton; avaliação direta das correções reduzidas.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    alpha = 7.2973525693e-3
    c = 299_792_458.0
    hbar = 1.054_571_817e-34
    m_e = 9.109_383_7015e-31
    m_p = 1.672_621_92369e-27
    Rinf = 10_973_731.568_160
    mu_p_over_mu_B = 1.521_032_202_30e-3
    nu_obs = 1_420_405_751.768
    r_p_fm = 0.840_778_765_45

    mu = m_e * m_p / (m_e + m_p)
    nu_F = (16.0 / 3.0) * alpha**2 * c * Rinf * (mu / m_e) ** 3 * mu_p_over_mu_B
    ae = alpha / (2.0 * math.pi)
    nu_ae = nu_F * (1.0 + ae)

    r_Z_fm = 4.0 * r_p_fm / 3.0
    delta_Z = -2.0 * alpha * (mu * c / hbar) * (r_Z_fm * 1e-15)
    nu_z = nu_ae * (1.0 + delta_Z)

    delta_rec = -0.5 * alpha**2 * (mu / m_p)
    nu_rec = nu_z * (1.0 + delta_rec)
    req = nu_obs - nu_rec

    rows = [
        ("Fermi líder", nu_F),
        ("com $a_e=\\alpha/(2\\pi)$", nu_ae),
        ("com Zemach de casca", nu_z),
        ("com recuo cinemático fino", nu_rec),
    ]

    lines = [
        '---',
        'title: "Saída — hiperfina e Zemach do hidrogênio"',
        '---',
        '',
        '# Saída — hiperfina e Zemach do hidrogênio',
        '',
        f'- referência 21 cm: `{nu_obs:.6f}` Hz',
        f'- $r_Z=4r_p/3={r_Z_fm:.12f}$ fm',
        f'- $\\delta_Z={delta_Z:.15e}$',
        '',
        '| aproximação | frequência [Hz] | erro relativo |',
        '|---|---:|---:|',
    ]
    for label, val in rows:
        lines.append(f'| {label} | `{val:.6f}` | `{(val/nu_obs-1.0):+.12e}` |')
    lines += [
        '',
        f'- deslocamento ainda requerido pela Hessiana magnética superior: `{req:.6f}` Hz.',
        '',
    ]

    out = Path(__file__).with_name('saida_hiperfina_zemach_hidrogenio.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
