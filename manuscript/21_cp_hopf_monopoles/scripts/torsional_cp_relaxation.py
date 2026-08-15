#!/usr/bin/env python3
"""
Objective:
    Self-contained log of the `torsional cp relaxation` verification associated with chapter `21_cp_hopf_monopoles`.
Chapter 21 — torsional relaxation of the CP angle.

Classification:
    direct evaluation of reduced flow + phenomenological comparison.

The script evaluates:

1. geometric volume V_K = 6 pi^5;
2. proposed rigidity f_B = M_Pl^red sqrt(3/sqrt(V_K));
3. effective mass m_B = sqrt(chi_top)/f_B if the mode has a pole;
4. flow dtheta/dtau = -kappa chi_dimless sin(theta);
5. flow time to fall below the neutron EDM limit.

The experimental EDM limit and the external scale chi_top^(1/4)=75.46 MeV enter
only as a comparison; they do not enter the construction of the geometric flow.
"""

from __future__ import annotations

import math
from pathlib import Path


def theta_exact(theta0: float, kappa_chi: float, tau: float) -> float:
    """Exact solution of dtheta/dtau = -kappa_chi sin(theta) for 0<theta<pi."""
    return 2.0 * math.atan(math.tan(theta0 / 2.0) * math.exp(-kappa_chi * tau))


def main() -> None:
    pi = math.pi

    # Reduced internal geometry.
    V_K = 6.0 * pi**5
    chi_dimless = 1.0 / V_K
    kappa_cp = 1.0
    theta0 = 2.5

    # Proposed torsional normalization.
    Mpl_red_GeV = 2.435e18
    f_B_GeV = Mpl_red_GeV * math.sqrt(3.0 / math.sqrt(V_K))

    # External comparison for axion-like scale, if there is a propagating pole.
    chi_top_quarter_MeV = 75.46
    chi_top_GeV4 = (chi_top_quarter_MeV / 1000.0) ** 4
    m_B_GeV = math.sqrt(chi_top_GeV4) / f_B_GeV
    m_B_eV = m_B_GeV * 1e9

    # Neutron EDM limit used as comparison.
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
        'title: "Output — torsional CP relaxation"',
        '---',
        '',
        '# Output — torsional CP relaxation',
        '',
        '## Geometry and normalization',
        '',
        '| Quantity | Value |',
        '|---|---:|',
        f'| $V_K=6\\pi^5$ | `{V_K:.12f}` |',
        f'| $\\chi_{{\\rm dimless}}=1/V_K$ | `{chi_dimless:.12e}` |',
        f'| proposed $f_B$ | `{f_B_GeV:.12e}` GeV |',
        f'| external $\\chi_{{\\rm top}}^{{1/4}}$ | `{chi_top_quarter_MeV:.6f}` MeV |',
        f'| effective $m_B$ if there is a pole | `{m_B_eV:.12e}` eV |',
        '',
        '## EDM and angle limit',
        '',
        '| Quantity | Value |',
        '|---|---:|',
        f'| limit $|d_n|$ | `{d_n_limit:.12e}` e cm |',
        f'| coefficient $C_n$ | `{C_n:.12e}` e cm |',
        f'| maximum $\\theta_{{\\rm residual}}$ | `{theta_limit:.12e}` rad |',
        f'| flow time to the limit | `{tau_to_limit:.12e}` |',
        '',
        '## Reduced flow',
        '',
        '| $\\tau$ | $\\theta(\\tau)$ | $|d_n|$ [e cm] |',
        '|---:|---:|---:|',
    ]

    for tau, theta, d_n in rows:
        lines.append(f'| `{tau:.12e}` | `{theta:.12e}` | `{d_n:.12e}` |')

    lines += [
        '',
        '## Classification',
        '',
        'Direct evaluation of the reduced flow. The experimental EDM value enters only as a final comparison.',
        'The effective mass $m_B$ should only be read as a particle mass if the torsional mode has a propagating pole.',
        '',
    ]

    out = Path(__file__).with_name('output_torsional_cp_relaxation.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
