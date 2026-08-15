#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the `muonic radius backreaction` verification associated with chapter `22_hydrogen_atom`.
Chapter 22 — contact amplification in muonic hydrogen.

Classification:
    direct evaluation of the reduced scale by reduced mass.
"""

from __future__ import annotations

import math
from pathlib import Path


def finite_size_eV(alpha: float, mu: float, c: float, hbar: float, e: float, r_fm: float, n: int = 2) -> float:
    r = r_fm * 1e-15
    return (2.0 / 3.0) * alpha**4 * mu**3 * c**4 * r**2 / hbar**2 / n**3 / e


def main() -> None:
    alpha = 7.2973525693e-3
    c = 299_792_458.0
    hbar = 1.054_571_817e-34
    e = 1.602_176_634e-19
    # CODATA constants used in this verification. We keep the values
    # explicitly in the script so that it remains self-contained.
    m_e = 9.109_383_7139e-31
    m_p = 1.672_621_92595e-27
    m_mu = 1.883_531_627e-28
    r_p_fm = 0.840_778_765_45

    mu_ep = m_e * m_p / (m_e + m_p)
    mu_mup = m_mu * m_p / (m_mu + m_p)
    ratio = (mu_ep / mu_mup) ** 3

    de_H = finite_size_eV(alpha, mu_ep, c, hbar, e, r_p_fm)
    de_muH = finite_size_eV(alpha, mu_mup, c, hbar, e, r_p_fm)
    trial_mu_shifts_fm = [-0.01, -0.03, -0.034]

    lines = [
        '---',
        'title: "Output — leptonic backreaction and muonic hydrogen"',
        '---',
        '',
        '# Output — leptonic backreaction and muonic hydrogen',
        '',
        '| Quantity | Value |',
        '|---|---:|',
        f'| $(\\mu_{{ep}}/\\mu_{{\\mu p}})^3$ | `{ratio:.15e}` |',
        f'| $\\Delta E_{{\\rm fs}}^H(2s)$ | `{de_H:.12e}` eV |',
        f'| $\\Delta E_{{\\rm fs}}^{{\\mu H}}(2s)$ | `{de_muH*1e3:.12f}` meV |',
        f'| amplification $\\mu H/H$ | `{de_muH/de_H:.12e}` |',
        '',
        '## Diagnostic table of radius backreaction',
        '',
        'The table below does not fix the absolute contraction of the proton. It only',
        'propagates the contact variational ratio between the electronic probe and the',
        'muonic probe:',
        '',
        '$$',
        '\\frac{\\delta r_p[e]}{\\delta r_p[\\mu]}',
        '=',
        '\\left(\\frac{\\mu_{ep}}{\\mu_{\\mu p}}\\right)^3.',
        '$$',
        '',
        '| assumed muonic contraction | estimated electronic contraction |',
        '|---:|---:|',
    ]
    for dr_mu in trial_mu_shifts_fm:
        lines.append(f'| `{dr_mu:.6f}` fm | `{dr_mu * ratio:.12e}` fm |')
    lines += [
        '',
        'The absolute value of $\\delta r_p[\\mu]$ requires the surface Hessian',
        'of the proton, i.e., $H_p^{\\rm surf}$ and the source $J_\\mu$ calculated',
        'directly from the official action.',
        '',
        'Conclusion: electronic backreaction exists, but it is about seven orders of magnitude smaller than the muonic one.',
        '',
    ]
    out = Path(__file__).with_name('output_muonic_radius_backreaction.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
