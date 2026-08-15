#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `dirac hydrogen spectrum` verification associated with chapter `22_hydrogen_atom`.
Chapter 22 — Sommerfeld--Dirac spectrum of hydrogen.

Classification:
    direct evaluation of the external spinor reduction.

Does not use spectroscopic data as input; uses only fixed physical
constants to calculate reduced-mass Coulomb--Dirac levels.
"""

from __future__ import annotations

import math
from pathlib import Path


def dirac_energy(mass_energy_eV: float, alpha: float, n: int, kappa: int, z: int = 1) -> float:
    za = z * alpha
    gamma = math.sqrt(kappa * kappa - za * za)
    denom = n - abs(kappa) + gamma
    return mass_energy_eV / math.sqrt(1.0 + (za / denom) ** 2)


def main() -> None:
    alpha = 7.2973525693e-3
    c = 299_792_458.0
    e = 1.602_176_634e-19
    m_e = 9.109_383_7015e-31
    m_p = 1.672_621_92369e-27

    mu = m_e * m_p / (m_e + m_p)
    mu_c2_eV = mu * c**2 / e

    levels = [
        ("1s1/2", 1, -1),
        ("2s1/2", 2, -1),
        ("2p1/2", 2, +1),
        ("2p3/2", 2, -2),
        ("3s1/2", 3, -1),
        ("3p1/2", 3, +1),
        ("3p3/2", 3, -2),
        ("3d3/2", 3, +2),
        ("3d5/2", 3, -3),
    ]

    rows = []
    for label, n, kappa in levels:
        j = abs(kappa) - 0.5
        deg = int(2 * j + 1)
        bind = dirac_energy(mu_c2_eV, alpha, n, kappa) - mu_c2_eV
        rows.append((label, n, kappa, j, deg, bind))

    bind = {label: val for label, *_rest, val in rows}
    fs = bind["2p3/2"] - bind["2p1/2"]
    lamb_pure = bind["2s1/2"] - bind["2p1/2"]

    lines = [
        '---',
        'title: "Output — Dirac hydrogen spectrum"',
        '---',
        '',
        '# Output — Dirac hydrogen spectrum',
        '',
        f'- $\\alpha={alpha:.13e}$',
        f'- $\\mu_{{ep}}c^2={mu_c2_eV:.12f}$ eV',
        '',
        '| level | n | kappa | j | degeneracy | binding energy [eV] |',
        '|---|---:|---:|---:|---:|---:|',
    ]
    for label, n, kappa, j, deg, bind_eV in rows:
        lines.append(f'| {label} | {n} | {kappa} | {j:.1f} | {deg} | `{bind_eV:.12f}` |')

    lines += [
        '',
        '## Checks',
        '',
        f'- $E(2p_{{3/2}})-E(2p_{{1/2}})={fs:.12e}$ eV.',
        f'- $E(2s_{{1/2}})-E(2p_{{1/2}})={lamb_pure:.12e}$ eV in the pure Coulomb--Dirac operator.',
        '',
    ]

    out = Path(__file__).with_name('output_dirac_hydrogen_spectrum.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
