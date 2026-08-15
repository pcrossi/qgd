#!/usr/bin/env python3
"""
Chapter 21 — Angular Hessian and topological susceptibility.

Classification:
    symbolic/numerical consistency verification.

For:

    V(theta) = chi * (1 - cos(theta)),

we have:

    d2V/dtheta2 = chi * cos(theta).

At the minimum theta=0, the Hessian is +chi. At the point theta=pi, it is -chi.
This verifies that the positivity of chi_top^GDQ selects theta=0 mod 2*pi
as the stable attractor and theta=pi mod 2*pi as the unstable maximum.
"""

from __future__ import annotations

import math
from pathlib import Path


def potential(theta: float, chi: float) -> float:
    return chi * (1.0 - math.cos(theta))


def second_derivative_central(theta: float, chi: float, h: float) -> float:
    return (potential(theta + h, chi) - 2.0 * potential(theta, chi) + potential(theta - h, chi)) / h**2


def main() -> None:
    chi = 1.0
    h = 1.0e-4
    points = [0.0, math.pi / 2.0, math.pi, 2.0 * math.pi]

    lines = [
        '---',
        'title: "Output — CP Hessian and susceptibility"',
        '---',
        '',
        '# Output — CP Hessian and susceptibility',
        '',
        'Reduced potential:',
        '',
        '$$',
        'V(\\theta)=\\chi(1-\\cos\\theta).',
        '$$',
        '',
        f'Used $\\chi=1$ and finite difference step `h={h:.1e}` only to verify the identity.',
        '',
        '| $\\theta$ | Analytical Hessian | Numerical Hessian | Classification |',
        '|---:|---:|---:|---|',
    ]

    for theta in points:
        analytic = chi * math.cos(theta)
        numeric = second_derivative_central(theta, chi, h)
        if analytic > 1e-8:
            status = 'stable minimum'
        elif analytic < -1e-8:
            status = 'unstable maximum'
        else:
            status = 'flat point of the angular projection'
        lines.append(f'| `{theta:.12f}` | `{analytic:.12f}` | `{numeric:.12f}` | {status} |')

    lines += [
        '',
        'Conclusion: in the torsional channel, $\\chi_{\\rm top}^{\\rm GDQ}>0$ is exactly the positive curvature of the CP minimum.',
        '',
    ]

    out = Path(__file__).with_name('output_hessian_cp_susceptibility.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
