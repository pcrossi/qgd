#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `zemach hyperfine hydrogen` verification associated with chapter `22_hydrogen_atom`.
Chapter 22 — hyperfine structure, leading anomaly and Zemach.

Classification:
    phenomenological comparison when using experimental magnetic moment
    of the proton; direct evaluation of the reduced corrections.
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
        ("Leading Fermi", nu_F),
        ("with $a_e=\\alpha/(2\\pi)$", nu_ae),
        ("with shell Zemach", nu_z),
        ("with fine kinematic recoil", nu_rec),
    ]

    lines = [
        '---',
        'title: "Output — hyperfine and Zemach of hydrogen"',
        '---',
        '',
        '# Output — hyperfine and Zemach of hydrogen',
        '',
        f'- 21 cm reference: `{nu_obs:.6f}` Hz',
        f'- $r_Z=4r_p/3={r_Z_fm:.12f}$ fm',
        f'- $\\delta_Z={delta_Z:.15e}$',
        '',
        '| approximation | frequency [Hz] | relative error |',
        '|---|---:|---:|',
    ]
    for label, val in rows:
        lines.append(f'| {label} | `{val:.6f}` | `{(val/nu_obs-1.0):+.12e}` |')
    lines += [
        '',
        f'- shift still required by the higher magnetic Hessian: `{req:.6f}` Hz.',
        '',
    ]

    out = Path(__file__).with_name('output_zemach_hyperfine_hydrogen.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
