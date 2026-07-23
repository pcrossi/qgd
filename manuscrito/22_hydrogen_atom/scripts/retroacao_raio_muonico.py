#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `retroacao raio muonico` associada ao capítulo `22_hydrogen_atom`.
Capítulo 22 — amplificação de contato no hidrogênio muônico.

Classificação:
    avaliação direta da escala reduzida por massa reduzida.
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
    # Constantes CODATA usadas nesta verificação. Mantemos os valores
    # explicitamente no script para que ele permaneça autocontido.
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
        'title: "Saída — retroação leptônica e hidrogênio muônico"',
        '---',
        '',
        '# Saída — retroação leptônica e hidrogênio muônico',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| $(\\mu_{{ep}}/\\mu_{{\\mu p}})^3$ | `{ratio:.15e}` |',
        f'| $\\Delta E_{{\\rm fs}}^H(2s)$ | `{de_H:.12e}` eV |',
        f'| $\\Delta E_{{\\rm fs}}^{{\\mu H}}(2s)$ | `{de_muH*1e3:.12f}` meV |',
        f'| amplificação $\\mu H/H$ | `{de_muH/de_H:.12e}` |',
        '',
        '## Tabela diagnóstica de retroação do raio',
        '',
        'A tabela abaixo não fixa a contração absoluta do próton. Ela apenas',
        'propaga a razão variacional de contato entre sonda eletrônica e sonda',
        'muônica:',
        '',
        '$$',
        '\\frac{\\delta r_p[e]}{\\delta r_p[\\mu]}',
        '=',
        '\\left(\\frac{\\mu_{ep}}{\\mu_{\\mu p}}\\right)^3.',
        '$$',
        '',
        '| contração muônica assumida | contração eletrônica estimada |',
        '|---:|---:|',
    ]
    for dr_mu in trial_mu_shifts_fm:
        lines.append(f'| `{dr_mu:.6f}` fm | `{dr_mu * ratio:.12e}` fm |')
    lines += [
        '',
        'O valor absoluto de $\\delta r_p[\\mu]$ exige a Hessiana de superfície',
        'do próton, isto é, $H_p^{\\rm surf}$ e a fonte $J_\\mu$ calculadas',
        'diretamente da ação oficial.',
        '',
        'Conclusão: a retroação eletrônica existe, mas é cerca de sete ordens de grandeza menor que a muônica.',
        '',
    ]
    out = Path(__file__).with_name('saida_retroacao_raio_muonico.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
