#!/usr/bin/env python3
"""
GDQ — Chapter 17 / reduced derivation of delta_B.

Objective:
    Self-contained verification of the reduced deduction:

        delta_B = ln(2*pi^2) * (3*sqrt(2)/5)

    from:

    1. unit volume of the boundary S^3: Vol(S^3)=2*pi^2;
    2. proton torsional configuration t_p=(1,1,1);
    3. neutron stationary configuration t_n=(1,1,-2);
    4. pairwise shear invariant
       I_sh^2=sum_{a<b}(t_a-t_b)^2;
    5. Pythagorean 3-4-5 attractor of the Fredholm-Fano projection:
       n=3 torsional channels, D=4 local continuum, cos(theta)=3/5;
    6. elementary complex norm ||1+i||=sqrt(2).

Classification:
    Direct evaluation of conditional reduced derivation. Does not use experimental
    masses as a target; only calculates the geometric invariant used in the
    chapter.
"""

from __future__ import annotations

from itertools import combinations
import math
from pathlib import Path


def pairwise_shear_squared(tensions: tuple[float, float, float]) -> float:
    """Calculates I_sh^2=sum_{a<b}(t_a-t_b)^2."""
    return sum((tensions[i] - tensions[j]) ** 2 for i, j in combinations(range(3), 2))


def main() -> None:
    out = Path(__file__).resolve().parent / "output_derive_baryon_deltas.md"

    proton = (1.0, 1.0, 1.0)
    neutron = (1.0, 1.0, -2.0)
    n_channels = 3.0
    continuum_dim = 4.0

    vol_s3 = 2.0 * math.pi**2
    entropy_surface = math.log(vol_s3)

    shear_p2 = pairwise_shear_squared(proton)
    shear_n2 = pairwise_shear_squared(neutron)
    shear_n = math.sqrt(shear_n2)
    hyp = math.sqrt(n_channels**2 + continuum_dim**2)
    tan_theta = continuum_dim / n_channels
    cos_theta = n_channels / hyp
    complex_norm = math.sqrt(2.0)
    chi_b = complex_norm * cos_theta
    delta_b = entropy_surface * chi_b

    text = f"""# Output — reduced derivation of delta_B

Classification: direct evaluation of conditional reduced derivation.

## Geometric Inputs

| item | value |
|---|---:|
| Vol(S^3) | {vol_s3:.12f} |
| ln Vol(S^3) | {entropy_surface:.12f} |
| t_p | {proton} |
| t_n | {neutron} |
| sum t_n | {sum(neutron):.12f} |
| torsional channels n | {n_channels:.0f} |
| local dimension D | {continuum_dim:.0f} |
| hypotenuse sqrt(n^2+D^2) | {hyp:.12f} |

## Shear Invariant

| quantity | value |
|---|---:|
| I_sh^2(t_p) | {shear_p2:.12f} |
| I_sh^2(t_n) | {shear_n2:.12f} |
| I_sh(t_n) | {shear_n:.12f} |

## Pythagorean attractor 3-4-5

| quantity | value |
|---|---:|
| tan(theta_c)=D/n | {tan_theta:.12f} |
| cos(theta_c)=n/sqrt(n^2+D^2) | {cos_theta:.12f} |
| ||1+i|| | {complex_norm:.12f} |
| chi_B=sqrt(2) cos(theta_c) | {chi_b:.12f} |
| delta_B | {delta_b:.12f} |

## Formula Evaluated

$$
\\delta_B
=
\\ln(2\\pi^2)\\frac{{3\\sqrt2}}{{5}}
=
{delta_b:.12f}.
$$

Interpretation: the neutron configuration satisfies local torsional current conservation
and possesses non-zero relative shear. The aligned proton has zero pairwise
shear. The reduced mass difference comes from the surface entropic energy
multiplied by the Fredholm-Fano admittance of the 3-4-5 projection.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
