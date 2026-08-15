#!/usr/bin/env python3
"""
Chapter 4 — verification of GDQ scale separation.

Classification:
    Numerical/symbolic consistency test.

This script does not make a metrological prediction. It verifies the conceptual thesis of the
note "Cartan scale, flow resolution and sectorial scales":

1. Lambda_C in the normalized action is dimensionless.
2. The scale of the heat kernel is Lambda_hat_tau = tau^{-1/2}.
3. Masses shift the spectrum p^2 + m_i^2, but are not universal cutoffs.
4. Using m_e or 1 GeV as a universal hard Gaussian cutoff would destroy processes
   in GeV/TeV, so this reading is forbidden.

The mass/energy numbers below are used only as reference scales to
demonstrate the order of magnitude of the inconsistency.
"""

from __future__ import annotations

import math
from pathlib import Path


def log10_gaussian_suppression(energy_gev: float, cutoff_gev: float) -> float:
    """Returns log10(exp[-(E/Lambda)^2]) without underflow."""
    return -((energy_gev / cutoff_gev) ** 2) / math.log(10.0)


def main() -> None:
    # Reference scales in GeV.
    electron_mass_gev = 0.00051099895
    one_gev = 1.0

    # Illustrative external energies, not used as fit.
    energies_gev = [electron_mass_gev, 0.01, 1.0, 100.0, 13000.0]

    # Illustrative flow scales.
    tau_values = [1.0, 0.25, 0.01, 1.0e-4]

    # Example of mass shifting spectrum, not defining cutoff.
    p_gev = 10.0
    sector_masses = {
        "electron": electron_mass_gev,
        "hadronic_1GeV": 1.0,
        "electroweak_100GeV": 100.0,
    }

    lines = [
        '---',
        'title: "Output — scale separation"',
        '---',
        '',
        '# Output — scale separation',
        '',
        '## 1. Heat kernel scale',
        '',
        '| $\\tau$ | $\\widehat\\Lambda_\\tau=\\tau^{-1/2}$ |',
        '|---:|---:|',
    ]

    for tau in tau_values:
        print(tau)
        lam = tau ** -0.5
        lines.append(f'| `{tau:.6e}` | `{lam:.12e}` |')

    lines += [
        '',
        '## 2. Why $m_e$ cannot be a hard universal cutoff',
        '',
        'The table shows $\\log_{10}\\{\\exp[-(E/\\Lambda)^2]\\}$.',
        '',
        '| external energy $E$ [GeV] | $m_e$ cutoff | $1$ GeV cutoff |',
        '|---:|---:|---:|',
    ]

    for energy in energies_gev:
        log_me = log10_gaussian_suppression(energy, electron_mass_gev)
        log_one = log10_gaussian_suppression(energy, one_gev)
        lines.append(f'| `{energy:.9e}` | `{log_me:.6e}` | `{log_one:.6e}` |')

    lines += [
        '',
        'Very negative values mean effectively zero suppression.',
        'Thus, $m_e$ or $1$ GeV cannot be read as a universal wall of external energy.',
        '',
        '## 3. Mass as a spectral shift',
        '',
        f'For $p_E={p_gev}$ GeV, with $\\lambda_i=p_E^2+m_i^2$:',
        '',
        '| sector | $m_i$ [GeV] | $p_E^2$ | $m_i^2$ | $\\lambda_i$ | fraction $m_i^2/\\lambda_i$ |',
        '|---|---:|---:|---:|---:|---:|',
    ]

    p2 = p_gev * p_gev
    for name, mass in sector_masses.items():
        m2 = mass * mass
        lam = p2 + m2
        frac = m2 / lam
        lines.append(f'| `{name}` | `{mass:.9e}` | `{p2:.9e}` | `{m2:.9e}` | `{lam:.9e}` | `{frac:.9e}` |')

    lines += [
        '',
        '## Conclusion',
        '',
        '\\Lambda_C, \\widehat\\Lambda_\\tau and $m_i$ have distinct functions.',
        'The mass alters the spectrum of the sector; the resolution comes from $\\tau$; the action uses $\\Lambda_C$ as a normalized dimensionless number.',
        '',
    ]

    out = Path(__file__).with_name('output_verify_scale_separation.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
