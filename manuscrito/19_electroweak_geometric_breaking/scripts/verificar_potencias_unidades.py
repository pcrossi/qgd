#!/usr/bin/env python3
"""
GDQ — Capítulo 19 / verificação editorial-dimensional.

Objetivo:
    Demonstrar de forma autocontida a diferença entre:

        125 GeV^2

    e:

        (125 GeV)^2.

Classificação:
    teste simbólico/dimensional editorial.

Esta verificação não é uma previsão física e não altera a ação oficial. Ela
apenas protege a escrita do manuscrito contra ambiguidade entre:

    1. número linear multiplicado por unidade quadrática;
    2. quadrado de uma escala linear de massa.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_verificar_potencias_unidades.md"

    mass_h_gev = 125.0
    linear_times_unit_squared = mass_h_gev
    squared_mass_value = mass_h_gev**2

    delta_m2_mev2 = 0.68
    wrongly_squared_delta = delta_m2_mev2**2

    text = f"""---
title: "Saída — potências e unidades"
---

# Saída — potências e unidades

Classificação: teste simbólico/dimensional editorial.

## Massa linear ao quadrado

| Escrita | valor numérico na unidade quadrática |
|---|---:|
| $125\\,{{\\rm GeV}}^2$ | `{linear_times_unit_squared:.6f}` GeV² |
| $(125\\,{{\\rm GeV}})^2$ | `{squared_mass_value:.6f}` GeV² |

Razão entre as duas leituras:

$$
\\frac{{(125\\,{{\\rm GeV}})^2}}{{125\\,{{\\rm GeV}}^2}}
=
{squared_mass_value / linear_times_unit_squared:.6f}.
$$

Portanto, se o significado físico for massa do Higgs ao quadrado, a escrita
segura é:

$$
M_H^2\\simeq(125\\,{{\\rm GeV}})^2.
$$

## Valor quadrático já calculado

Se um cálculo fornece diretamente:

$$
\\Delta M_H^2\\simeq0.68\\,{{\\rm MeV}}^2,
$$

então o número `0.68` já é o valor da grandeza quadrática. Escrever
$(0.68\\,{{\\rm MeV}})^2$ mudaria o valor para:

$$
{wrongly_squared_delta:.6f}\\,{{\\rm MeV}}^2.
$$

## Conclusão

- Use $(M\\,{{\\rm GeV}})^2$ quando o número linear também deve ser elevado ao
  quadrado.
- Use $X\\,{{\\rm GeV}}^2$ quando $X$ já é o valor de uma quantidade
  quadrática.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
