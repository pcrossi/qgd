#!/usr/bin/env python3
"""
GDQ — Capítulo 13 / Aharonov--Bohm simbólico

Objetivo:
    Verificar simbolicamente o representante ideal

        A_harm = (Phi/(2*pi)) dtheta

    no exterior perfurado do solenoide:

        dA_harm = 0,
        integral_gamma A_harm = Phi,
        Hol_gamma = exp(i q Phi/(hbar c)).

Interpretação GDQ:
    O script não introduz nova dinâmica. Ele apenas verifica a parte topológica
    da redução efetiva: o campo exterior é localmente plano, mas a conexão não
    é globalmente exata no domínio perfurado.

Classificação:
    Teste simbólico de consistência da holonomia ideal.

Saída:
    scripts/saida_ab_holonomia_simbolica.md
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_ab_holonomia_simbolica.md"

    r, theta, phi = sp.symbols("r theta phi", positive=True, real=True)
    Phi, q, hbar, c = sp.symbols("Phi q hbar c", nonzero=True, real=True)

    # Em coordenadas cilíndricas no exterior do solenoide, o representante
    # diferencial é A = A_theta dtheta. Como A_theta é constante em r,theta,z
    # neste sistema de 1-formas, dA = d(A_theta) wedge dtheta = 0.
    A_theta = Phi / (2 * sp.pi)
    dA_coeff_dr_dtheta = sp.diff(A_theta, r)
    dA_coeff_dphi_dtheta = sp.diff(A_theta, phi)

    loop_integral = sp.integrate(A_theta, (theta, 0, 2 * sp.pi))
    holonomy = sp.exp(sp.I * q * loop_integral / (hbar * c))

    # Transformação de calibre unívoca: lambda(theta)=a sin(theta). A integral
    # fechada de d lambda deve se anular.
    a = sp.symbols("a", real=True)
    lam = a * sp.sin(theta)
    gauge_loop = sp.integrate(sp.diff(lam, theta), (theta, 0, 2 * sp.pi))

    checks = {
        "dA_dr_dtheta": sp.simplify(dA_coeff_dr_dtheta),
        "dA_dphi_dtheta": sp.simplify(dA_coeff_dphi_dtheta),
        "loop_integral": sp.simplify(loop_integral),
        "gauge_loop_univoca": sp.simplify(gauge_loop),
        "holonomy": holonomy,
    }

    text = f"""# Saída — holonomia AB simbólica

Classificação: teste simbólico de consistência da holonomia ideal.

## Representante

$$
A_{{\\rm harm}}
=
\\frac{{\\Phi}}{{2\\pi}}\\,d\\theta.
$$

## Fechamento exterior

Os coeficientes simbólicos de $dA_{{\\rm harm}}$ verificados são:

| Coeficiente | Resultado |
|---|---:|
| $\\partial_r(\\Phi/2\\pi)$ | ${sp.latex(checks['dA_dr_dtheta'])}$ |
| $\\partial_z(\\Phi/2\\pi)$ | ${sp.latex(checks['dA_dphi_dtheta'])}$ |

Logo, no domínio exterior:

$$
dA_{{\\rm harm}}=0.
$$

## Integral de laço

$$
\\oint_\\gamma A_{{\\rm harm}}
=
\\int_0^{{2\\pi}}
\\frac{{\\Phi}}{{2\\pi}}\\,d\\theta
=
{sp.latex(checks['loop_integral'])}.
$$

## Holonomia

$$
\\operatorname{{Hol}}_\\gamma(A)
=
{sp.latex(checks['holonomy'])}.
$$

## Invariância de calibre unívoca

Para $\\lambda(\\theta)=a\\sin\\theta$:

$$
\\oint_\\gamma d\\lambda
=
{sp.latex(checks['gauge_loop_univoca'])}.
$$

Conclusão: o representante é localmente plano, mas sua integral em laço
perfurado preserva a classe global $\\Phi$.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
