#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `relaxacao cp torsional` associada ao capítulo `21_cp_hopf_monopoles`.
Capítulo 21 — relaxação torsional do ângulo CP.

Classificação:
    avaliação direta de fluxo reduzido + comparação fenomenológica.

O script avalia:

1. volume geométrico V_K = 6 pi^5;
2. rigidez proposta f_B = M_Pl^red sqrt(3/sqrt(V_K));
3. massa efetiva m_B = sqrt(chi_top)/f_B se o modo tiver polo;
4. fluxo dtheta/dtau = -kappa chi_dimless sin(theta);
5. tempo de fluxo para ficar abaixo do limite de EDM do nêutron.

O limite experimental do EDM e a escala externa chi_top^(1/4)=75.46 MeV entram
apenas como comparação; não entram na construção do fluxo geométrico.
"""

from __future__ import annotations

import math
from pathlib import Path


def theta_exact(theta0: float, kappa_chi: float, tau: float) -> float:
    """Solução exata de dtheta/dtau = -kappa_chi sin(theta) para 0<theta<pi."""
    return 2.0 * math.atan(math.tan(theta0 / 2.0) * math.exp(-kappa_chi * tau))


def main() -> None:
    pi = math.pi

    # Geometria interna reduzida.
    V_K = 6.0 * pi**5
    chi_dimless = 1.0 / V_K
    kappa_cp = 1.0
    theta0 = 2.5

    # Normalização torsional proposta.
    Mpl_red_GeV = 2.435e18
    f_B_GeV = Mpl_red_GeV * math.sqrt(3.0 / math.sqrt(V_K))

    # Comparação externa para escala axion-like, se houver polo propagante.
    chi_top_quarter_MeV = 75.46
    chi_top_GeV4 = (chi_top_quarter_MeV / 1000.0) ** 4
    m_B_GeV = math.sqrt(chi_top_GeV4) / f_B_GeV
    m_B_eV = m_B_GeV * 1e9

    # Limite de EDM do nêutron usado como comparação.
    d_n_limit = 1.8e-26
    C_n = 3.8e-16
    theta_limit = d_n_limit / C_n

    tau_to_limit = math.log(math.tan(theta0 / 2.0) / math.tan(theta_limit / 2.0)) / (
        kappa_cp * chi_dimless
    )

    tau_samples = [0.0, 0.5 / chi_dimless, 1.0 / chi_dimless, 2.0 / chi_dimless, tau_to_limit]
    rows = []
    for tau in tau_samples:
        theta = theta_exact(theta0, kappa_cp * chi_dimless, tau)
        d_n = C_n * abs(theta)
        rows.append((tau, theta, d_n))

    lines = [
        '---',
        'title: "Saída — relaxação CP torsional"',
        '---',
        '',
        '# Saída — relaxação CP torsional',
        '',
        '## Geometria e normalização',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| $V_K=6\\pi^5$ | `{V_K:.12f}` |',
        f'| $\\chi_{{\\rm dimless}}=1/V_K$ | `{chi_dimless:.12e}` |',
        f'| $f_B$ proposto | `{f_B_GeV:.12e}` GeV |',
        f'| $\\chi_{{\\rm top}}^{{1/4}}$ externo | `{chi_top_quarter_MeV:.6f}` MeV |',
        f'| $m_B$ efetivo se houver polo | `{m_B_eV:.12e}` eV |',
        '',
        '## EDM e limite de ângulo',
        '',
        '| Quantidade | Valor |',
        '|---|---:|',
        f'| limite $|d_n|$ | `{d_n_limit:.12e}` e cm |',
        f'| coeficiente $C_n$ | `{C_n:.12e}` e cm |',
        f'| $\\theta_{{\\rm residual}}$ máximo | `{theta_limit:.12e}` rad |',
        f'| tempo de fluxo até o limite | `{tau_to_limit:.12e}` |',
        '',
        '## Fluxo reduzido',
        '',
        '| $\\tau$ | $\\theta(\\tau)$ | $|d_n|$ [e cm] |',
        '|---:|---:|---:|',
    ]

    for tau, theta, d_n in rows:
        lines.append(f'| `{tau:.12e}` | `{theta:.12e}` | `{d_n:.12e}` |')

    lines += [
        '',
        '## Classificação',
        '',
        'Avaliação direta do fluxo reduzido. O valor experimental do EDM entra apenas como comparação final.',
        'A massa efetiva $m_B$ só deve ser lida como massa de partícula se o modo torsional tiver polo propagante.',
        '',
    ]

    out = Path(__file__).with_name('saida_relaxacao_cp_torsional.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
