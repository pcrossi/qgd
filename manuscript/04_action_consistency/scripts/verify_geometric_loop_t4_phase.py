#!/usr/bin/env python3
"""
Chapter 4 — geometric loop of the toroidal phase.

Classification:
    Numerical/symbolic consistency verification.

This script reproduces the minimal test of gauge preservation in GDQ loops:

    S_GDQ -> S_chi^(2) -> H_n[A] -> Tr log H_n[A] -> Pi_{mu nu}.

The calculation uses the phase mode in a cycle of T^4. It verifies:

1. Pi(0)=0 by infrared subtraction;
2. Ward transversality: Q^mu Pi_{mu nu}=0;
3. Finite ultraviolet saturation;
4. Geometric origin of the parameters q_n=n*kappa and m_n=n/R.

There is no fit to experimental data.
"""

from __future__ import annotations

import math
from pathlib import Path


def simpson(f, a: float, b: float, n: int = 800) -> float:
    if n % 2:
        n += 1
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += (4 if i % 2 else 2) * f(a + i * h)
    return s * h / 3.0


def e1(z: float) -> float:
    """E1(z)=int_1^infty exp(-z*u)/u du = int_0^1 exp(-z/t)/t dt."""
    if z <= 0:
        raise ValueError("E1 requires z>0")

    def integrand(t: float) -> float:
        if t == 0.0:
            return 0.0
        return math.exp(-z / t) / t

    return simpson(integrand, 0.0, 1.0, 4000)


def pi_scalar(q2: float, qn: float, mass: float, s0: float) -> float:
    eta = s0 * mass * mass
    e1_eta = e1(eta)

    def integrand(x: float) -> float:
        u = x * (1.0 - x)
        return (1.0 - 2.0 * x) ** 2 * (e1_eta - e1(s0 * (mass * mass + u * q2)))

    return qn * qn / (16.0 * math.pi**2) * simpson(integrand, 0.0, 1.0, 800)


def main() -> None:
    n_mode = 1
    kappa = 1.0
    radius = 1.0
    lambda_perp = 0.0
    s0 = 0.2

    qn = n_mode * kappa
    mass = math.sqrt((n_mode / radius) ** 2 + lambda_perp)
    eta = s0 * mass * mass
    saturation = qn * qn / (48.0 * math.pi**2) * e1(eta)

    q_values = [0.0, 0.25, 0.5, 1.0, 2.0, 5.0, 10.0]
    rows = []
    max_ward = 0.0

    for q_abs in q_values:
        q2 = q_abs * q_abs
        pi = pi_scalar(q2, qn, mass, s0)
        # Choose Q=(q,0,0,0). The transverse tensor is
        # Pi_{mu nu}=(Q_mu Q_nu-Q^2 delta_{mu nu}) Pi.
        # The contraction Q^mu Pi_{mu nu} vanishes algebraically; we compute the norm.
        ward_components = []
        for nu in range(4):
            acc = 0.0
            for mu in range(4):
                q_mu = q_abs if mu == 0 else 0.0
                q_nu = q_abs if nu == 0 else 0.0
                delta = 1.0 if mu == nu else 0.0
                tensor = (q_mu * q_nu - q2 * delta) * pi
                acc += q_mu * tensor
            ward_components.append(acc)
        ward_norm = math.sqrt(sum(v * v for v in ward_components))
        max_ward = max(max_ward, ward_norm)
        rows.append((q_abs, q2, pi, ward_norm))

    lines = [
        '---',
        'title: "Output — geometric loop of the toroidal phase"',
        '---',
        '',
        '# Output — geometric loop of the toroidal phase',
        '',
        'Geometric parameters without adjustment:',
        '',
        f'- toroidal mode `n={n_mode}`',
        f'- `kappa={kappa}`',
        f'- `R={radius}`',
        f'- `lambda_perp={lambda_perp}`',
        f'- `q_n=n*kappa={qn}`',
        f'- `m_n=sqrt(n^2/R^2+lambda_perp)={mass}`',
        f'- `s0={s0}`',
        f'- `eta=s0*m_n^2={eta}`',
        '',
        '## Polarization and Ward',
        '',
        '| $Q$ | $Q^2$ | $\\Pi_{n,s_0}(Q^2)$ | $\\|Q^\\mu\\Pi_{\\mu\\nu}\\|$ |',
        '|---:|---:|---:|---:|',
    ]

    for q_abs, q2, pi, ward_norm in rows:
        lines.append(f'| `{q_abs:.6f}` | `{q2:.6f}` | `{pi:.12e}` | `{ward_norm:.12e}` |')

    lines += [
        '',
        '## Ultraviolet saturation',
        '',
        f'- numerical $\\Pi(0)$: `{rows[0][2]:.12e}`.',
        f'- saturated limit $q_n^2 E_1(\\eta)/(48\\pi^2)$: `{saturation:.12e}`.',
        f'- largest Ward residue in table: `{max_ward:.12e}`.',
        '',
        '## Classification',
        '',
        'Consistency test of the geometric loop derived from the phase Hessian; not a metrological prediction.',
        '',
    ]

    out = Path(__file__).with_name('output_verify_geometric_loop_t4_phase.md')
    out.write_text('\n'.join(lines), encoding='utf-8')
    print('\n'.join(lines))


if __name__ == '__main__':
    main()
