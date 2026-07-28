#!/usr/bin/env python3
"""
GDQ — Capítulo 17 / derivação reduzida de delta_B.

Objetivo:
    Verificar de forma autocontida a dedução reduzida

        delta_B = ln(2*pi^2) * (3*sqrt(2)/5)

    a partir de:

    1. volume unitário da fronteira S^3: Vol(S^3)=2*pi^2;
    2. configuração torsional do próton t_p=(1,1,1);
    3. configuração estacionária do nêutron t_n=(1,1,-2);
    4. invariante de cisalhamento par-a-par
       I_sh^2=sum_{a<b}(t_a-t_b)^2;
    5. hipótese pitagórica 3-4-5 da projeção Fredholm-Fano:
       n=3 canais torsionais, D=4 contínuo local, cos(theta)=3/5;
    6. norma complexa elementar ||1+i||=sqrt(2).

Classificação:
    Avaliação direta de derivação reduzida condicional. Não usa massas
    experimentais como alvo; apenas calcula o invariante geométrico usado no
    capítulo.
"""

from __future__ import annotations

from itertools import combinations
import math
from pathlib import Path


def pairwise_shear_squared(tensions: tuple[float, float, float]) -> float:
    """Calcula I_sh^2=sum_{a<b}(t_a-t_b)^2."""
    return sum((tensions[i] - tensions[j]) ** 2 for i, j in combinations(range(3), 2))


def main() -> None:
    out = Path(__file__).resolve().parent / "saida_derivar_delta_barioes.md"

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

    text = f"""# Saída — derivação reduzida de delta_B

Classificação: avaliação direta de derivação reduzida condicional.

## Entradas geométricas

| item | valor |
|---|---:|
| Vol(S^3) | {vol_s3:.12f} |
| ln Vol(S^3) | {entropy_surface:.12f} |
| t_p | {proton} |
| t_n | {neutron} |
| soma t_n | {sum(neutron):.12f} |
| canais torsionais n | {n_channels:.0f} |
| dimensão local D | {continuum_dim:.0f} |
| hipotenusa sqrt(n^2+D^2) | {hyp:.12f} |

## Invariante de cisalhamento

| quantidade | valor |
|---|---:|
| I_sh^2(t_p) | {shear_p2:.12f} |
| I_sh^2(t_n) | {shear_n2:.12f} |
| I_sh(t_n) | {shear_n:.12f} |

## Projeção pitagórica 3-4-5

| quantidade | valor |
|---|---:|
| tan(theta_c)=D/n | {tan_theta:.12f} |
| cos(theta_c)=n/sqrt(n^2+D^2) | {cos_theta:.12f} |
| ||1+i|| | {complex_norm:.12f} |
| chi_B=sqrt(2) cos(theta_c) | {chi_b:.12f} |
| delta_B | {delta_b:.12f} |

## Fórmula avaliada

$$
\\delta_B
=
\\ln(2\\pi^2)\\frac{{3\\sqrt2}}{{5}}
=
{delta_b:.12f}.
$$

Interpretação: a configuração do nêutron satisfaz conservação torsional local
e possui cisalhamento relativo não nulo. O próton alinhado tem cisalhamento
par-a-par nulo. A conversão desse invariante em diferença de massa é
condicional à hipótese Fredholm--Fano 3--4--5.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
