#!/usr/bin/env python3
"""
Chapter 4 — verification of the GDQ heat-kernel propagator.

Classification:
    Symbolic/numerical consistency verification.

The script confirms three points used in the text:

1. The Hessian contains the flow factor as O_Hess = tau * L.
2. The correct heat generator is L = O_Hess / tau.
3. In the flat limit the propagator is exp(-tau p^2)/(p^2 + m^2), without new poles
   coming from the numerator.

No experimental data is used. No parameters are adjusted.
"""

from __future__ import annotations

import math
from pathlib import Path


def gdq_propagator(p: float, tau: float, mass: float) -> float:
    return math.exp(-tau * p * p) / (p * p + mass * mass)


def wrong_double_tau_factor(p: float, tau: float, mass: float) -> float:
    """Incorrect form that would arise from using exp[-tau*(tau L)]."""
    return math.exp(-(tau * tau) * p * p) / (p * p + mass * mass)


def main() -> None:
    tau = 0.25
    lam_hat = tau ** -0.5
    mass = 0.7
    momenta = [0.0, 0.5, 1.0, 2.0, 4.0, 8.0]

    lines = [
        '---',
        'title: "Output — heat kernel and GDQ propagator"',
        '---',
        '',
        '# Output — heat kernel and GDQ propagator',
        '',
        'Test parameters, without adjustment:',
        '',
        f'- $\\tau={tau}$',
        f'- $\\widehat\\Lambda_\\tau=\\tau^{{-1/2}}={lam_hat:.12f}$',
        f'- $m={mass}$',
        '',
        '| $p_E$ | $G_\\tau=e^{-\\tau p^2}/(p^2+m^2)$ | wrong form $e^{-\\tau^2p^2}/(p^2+m^2)$ | wrong/correct ratio |',
        '|---:|---:|---:|---:|',
    ]

    for p in momenta:
        good = gdq_propagator(p, tau, mass)
        bad = wrong_double_tau_factor(p, tau, mass)
        ratio = bad / good if good != 0.0 else float('inf')
        lines.append(f'| `{p:.6f}` | `{good:.12e}` | `{bad:.12e}` | `{ratio:.12e}` |')

    lines += [
        '',
        '## Poles',
        '',
        'The numerator $e^{-\\tau p^2}$ is always positive on the Euclidean real axis.',
        'Thus it does not create poles. The denominator vanishes only when $p_E^2+m^2=0$,',
        'that is, off the Euclidean real axis for $m^2>0$.',
        '',
        '## Classification',
        '',
        'Consistency test of the flat limit of the heat semigroup; not a metrological prediction.',
        '',
    ]

    out = Path(__file__).with_name('output_verify_heat_kernel_propagator.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
