#!/usr/bin/env python3
"""
Q30 — integração direta do disco transversal Ricci--Bohm.

Objetivo:
    Reavaliar sigma_GDQ sem tratar kappa_sigma=pi como fator colocado à mão.
    O fator pi deve sair da integral radial da densidade transversal reduzida.

Escopo:
    - GDQ reduzida do pescoço Ricci--Bohm;
    - não usa QCD/Yang--Mills como ação;
    - não ajusta ao valor hadrônico;
    - não substitui a integração completa de R^B[g,H] no perfil 8D geral.

Modelo transversal reduzido:
    O primeiro quantum transversal do pescoço estabilizado tem escala

        Delta = hbar c / r_perp.

    Como o tubo homogêneo possui célula longitudinal natural de ordem r_perp,
    a densidade de tensão por área no disco é

        eps_sigma = hbar c / r_perp^4.

    Integrando no disco D_{r_perp},

        sigma = int_D eps_sigma dA
              = int_0^{r_perp} 2 pi s ds * hbar c / r_perp^4
              = pi hbar c / r_perp^2.

    Portanto, pi é a integral direta da seção circular, não calibração.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
R_PERP_FM = 0.86
SIGMA_HAD_GEV_PER_FM = 0.89

# Dados do funcional homogêneo de garganta já presente no corpus.
R_HOM = 1.03707435228632
TAU_HOM = 0.274900522513626
Q_T = 1.0


@dataclass(frozen=True)
class DirectIntegralResult:
    r_perp_fm: float
    area_fm2: float
    eps_sigma_gev_per_fm3: float
    sigma_analytic_gev_per_fm: float
    sigma_numeric_gev_per_fm: float
    sigma_gev2: float
    sqrt_sigma_gev: float
    delta_gev: float
    err_sigma_percent: float
    err_sqrt_sigma_percent: float
    w_hom: float
    sigma_hom_gev_per_fm: float
    err_sigma_hom_percent: float


def integrate_midpoint(r: float, n: int = 2_000_000) -> float:
    """Midpoint quadrature of int_0^r 2*pi*s*(HBARC/r^4) ds."""
    dr = r / n
    eps = HBARC_GEV_FM / r**4
    total = 0.0
    for i in range(n):
        s = (i + 0.5) * dr
        total += 2.0 * math.pi * s * eps * dr
    return total


def homogeneous_throat_functional(R: float = R_HOM, tau: float = TAU_HOM, Q: float = Q_T) -> float:
    """Dimensionless W_Q(R) from hessiana_vinculada_garganta_torcional.md."""
    return tau * (6.0 / R**2 - Q**2 / (2.0 * math.pi**2 * R**6)) + 3.0 * math.log(R)


def evaluate() -> DirectIntegralResult:
    r = R_PERP_FM
    area = math.pi * r**2
    eps_sigma = HBARC_GEV_FM / r**4
    sigma_analytic = math.pi * HBARC_GEV_FM / r**2
    sigma_numeric = integrate_midpoint(r)
    sigma_gev2 = sigma_analytic * HBARC_GEV_FM
    sqrt_sigma = math.sqrt(sigma_gev2)
    delta = HBARC_GEV_FM / r

    sigma_had_gev2 = SIGMA_HAD_GEV_PER_FM * HBARC_GEV_FM
    sqrt_sigma_had = math.sqrt(sigma_had_gev2)

    err_sigma = 100.0 * (sigma_analytic - SIGMA_HAD_GEV_PER_FM) / SIGMA_HAD_GEV_PER_FM
    err_sqrt = 100.0 * (sqrt_sigma - sqrt_sigma_had) / sqrt_sigma_had

    w_hom = homogeneous_throat_functional()
    sigma_hom = w_hom * HBARC_GEV_FM / r**2
    err_sigma_hom = 100.0 * (sigma_hom - SIGMA_HAD_GEV_PER_FM) / SIGMA_HAD_GEV_PER_FM

    return DirectIntegralResult(
        r_perp_fm=r,
        area_fm2=area,
        eps_sigma_gev_per_fm3=eps_sigma,
        sigma_analytic_gev_per_fm=sigma_analytic,
        sigma_numeric_gev_per_fm=sigma_numeric,
        sigma_gev2=sigma_gev2,
        sqrt_sigma_gev=sqrt_sigma,
        delta_gev=delta,
        err_sigma_percent=err_sigma,
        err_sqrt_sigma_percent=err_sqrt,
        w_hom=w_hom,
        sigma_hom_gev_per_fm=sigma_hom,
        err_sigma_hom_percent=err_sigma_hom,
    )


def render_markdown(result: DirectIntegralResult) -> str:
    numeric_error = (
        result.sigma_numeric_gev_per_fm - result.sigma_analytic_gev_per_fm
    ) / result.sigma_analytic_gev_per_fm

    return f"""# Q30 — integração direta do disco Ricci--Bohm

## Objetivo

Reavaliar a tensão do tubo sem tratar $\\kappa_\\sigma=\\pi$ como constante
externa. O fator $\\pi$ deve sair da integração direta da seção transversal
circular estabilizada.

## Densidade transversal reduzida

Para o pescoço Ricci--Bohm estabilizado:

$$
r_\\perp={result.r_perp_fm:.12f}\\,\\mathrm{{fm}}.
$$

O primeiro quantum transversal é:

$$
\\Delta_{{\\rm GDQ}}=\\frac{{\\hbar c}}{{r_\\perp}}.
$$

Como o tubo homogêneo possui célula longitudinal natural de ordem
$r_\\perp$, a densidade de tensão por área usada no fechamento reduzido é:

$$
\\varepsilon_\\sigma
=\\frac{{\\hbar c}}{{r_\\perp^4}}
={result.eps_sigma_gev_per_fm3:.12f}\\,\\mathrm{{GeV/fm^3}}.
$$

## Integração direta

$$
\\sigma_{{\\rm GDQ}}
=\\int_{{D_{{r_\\perp}}}}\\varepsilon_\\sigma\\,dA.
$$

Com $dA=2\\pi s\\,ds$:

$$
\\sigma_{{\\rm GDQ}}
=\\int_0^{{r_\\perp}}
2\\pi s\\,ds\\,
\\frac{{\\hbar c}}{{r_\\perp^4}}
=\\pi\\frac{{\\hbar c}}{{r_\\perp^2}}.
$$

Portanto, o fator $\\pi$ é a integral da seção circular; não é ajuste.

## Verificação numérica

| quantidade | valor |
|---|---:|
| $\\mathcal A_0$ | {result.area_fm2:.12f} fm$^2$ |
| $\\Delta_{{\\rm GDQ}}$ | {result.delta_gev:.12f} GeV |
| $\\sigma$ analítico | {result.sigma_analytic_gev_per_fm:.12f} GeV/fm |
| $\\sigma$ quadratura direta | {result.sigma_numeric_gev_per_fm:.12f} GeV/fm |
| erro relativo da quadratura | {numeric_error:.3e} |
| $\\sigma$ | {result.sigma_gev2:.12f} GeV$^2$ |
| $\\sqrt{{\\sigma}}$ | {result.sqrt_sigma_gev:.12f} GeV |

## Comparação posterior

Usando apenas como referência fenomenológica posterior:

$$
\\sigma_{{\\rm had}}\\simeq {SIGMA_HAD_GEV_PER_FM:.6f}\\,\\mathrm{{GeV/fm}}.
$$

O desvio é:

$$
\\frac{{\\sigma_{{\\rm GDQ}}-\\sigma_{{\\rm had}}}}{{\\sigma_{{\\rm had}}}}
={result.err_sigma_percent:+.6f}\\%.
$$

Em $\\sqrt{{\\sigma}}$, o desvio é:

$$
{result.err_sqrt_sigma_percent:+.6f}\\%.
$$

## Auditoria: por que não usar diretamente $\\mathcal W_Q(R)$ como tensão?

O funcional homogêneo de garganta já derivado é:

$$
\\mathcal W_Q(R)
=\\tau\\left(
\\frac6{{R^2}}-\\frac{{Q_T^2}}{{2\\pi^2R^6}}
\\right)+3\\log R.
$$

Com os valores do setor homogêneo vigente:

$$
\\mathcal W_Q={result.w_hom:.12f}.
$$

Se ele fosse usado diretamente como coeficiente de tensão tubular, produziria:

$$
\\sigma_{{\\mathcal W}}
={result.sigma_hom_gev_per_fm:.12f}\\,\\mathrm{{GeV/fm}},
$$

com desvio:

$$
{result.err_sigma_hom_percent:+.6f}\\%.
$$

Isso mostra que $\\mathcal W_Q(R)$ não é a tensão tubular completa. Ele mede o
setor homogêneo de garganta normalizado; a tensão do tubo exige a integral
transversal do pescoço Ricci--Bohm ou, no refinamento final, a integral
completa de $\\mathcal S_\\perp[q_*]-\\mathcal S_\\perp[q_{{\\rm vac}}]$.

## Status

A integração direta da seção reduzida confirma:

$$
\\boxed{{
\\sigma_{{\\rm GDQ}}
={result.sigma_analytic_gev_per_fm:.12f}\\,\\mathrm{{GeV/fm}}
}}
$$

e preserva o acordo de escala com o confinamento hadrônico.

A metrologia final ainda requer resolver o perfil 8D completo para substituir
a densidade reduzida uniforme por:

$$
\\sigma_{{\\rm GDQ}}
=\\mathcal S_\\perp[q_*]-\\mathcal S_\\perp[q_{{\\rm vac}}].
$$
"""


def main() -> None:
    result = evaluate()
    output = Path(__file__).with_name("saida_integracao_direta_tubo_ricci_bohm_q30.md")
    output.write_text(render_markdown(result), encoding="utf-8")
    print(f"r_perp_fm={result.r_perp_fm:.12f}")
    print(f"area_fm2={result.area_fm2:.12f}")
    print(f"Delta_GDQ_GeV={result.delta_gev:.12f}")
    print(f"eps_sigma_GeV_per_fm3={result.eps_sigma_gev_per_fm3:.12f}")
    print(f"sigma_analytic_GeV_per_fm={result.sigma_analytic_gev_per_fm:.12f}")
    print(f"sigma_numeric_GeV_per_fm={result.sigma_numeric_gev_per_fm:.12f}")
    print(f"sigma_GeV2={result.sigma_gev2:.12f}")
    print(f"sqrt_sigma_GeV={result.sqrt_sigma_gev:.12f}")
    print(f"err_sigma_percent={result.err_sigma_percent:+.6f}")
    print(f"err_sqrt_sigma_percent={result.err_sqrt_sigma_percent:+.6f}")
    print(f"W_hom={result.w_hom:.12f}")
    print(f"sigma_from_W_hom_GeV_per_fm={result.sigma_hom_gev_per_fm:.12f}")
    print(f"err_sigma_from_W_hom_percent={result.err_sigma_hom_percent:+.6f}")
    print(f"wrote={output}")


if __name__ == "__main__":
    main()
