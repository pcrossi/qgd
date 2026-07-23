#!/usr/bin/env python3
"""
Q30 — avaliação reduzida do tubo Ricci--Bohm da GDQ.

Este script não usa ação de Yang--Mills/QCD nem ajusta parâmetros ao valor
fenomenológico da tensão de corda. Ele avalia a escala transversal reduzida já
registrada no manuscrito legado da GDQ:

    r_perp = 0.86 fm

e aplica as fórmulas estruturais da rota Ricci--Bohm:

    A0 = pi r_perp^2
    Delta_GDQ = hbar c / r_perp
    sigma_GDQ = kappa_sigma hbar c / r_perp^2

com kappa_sigma = pi como fechamento geométrico reduzido do primeiro quantum
transversal distribuído na seção circular estabilizada.

Classificação: avaliação quantitativa reduzida / comparação fenomenológica.
Não é previsão metrológica final até que S_perp[q_*] seja integrada
diretamente a partir da ação oficial no perfil estacionário completo.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
R_PERP_FM = 0.86
KAPPA_SIGMA = math.pi

# Referência fenomenológica usual para a tensão de corda hadrônica.
# Usada apenas para comparação posterior, não na construção.
SIGMA_HAD_GEV_PER_FM = 0.89


@dataclass(frozen=True)
class TubeResult:
    r_perp_fm: float
    area_fm2: float
    delta_gev: float
    sigma_gev_per_fm: float
    sigma_gev2: float
    sqrt_sigma_gev: float
    sigma_had_gev_per_fm: float
    sigma_had_gev2: float
    sqrt_sigma_had_gev: float
    err_sigma_percent: float
    err_sqrt_sigma_percent: float


def evaluate(
    r_perp_fm: float = R_PERP_FM,
    kappa_sigma: float = KAPPA_SIGMA,
    sigma_had_gev_per_fm: float = SIGMA_HAD_GEV_PER_FM,
) -> TubeResult:
    area_fm2 = math.pi * r_perp_fm**2
    delta_gev = HBARC_GEV_FM / r_perp_fm
    sigma_gev_per_fm = kappa_sigma * HBARC_GEV_FM / r_perp_fm**2
    sigma_gev2 = sigma_gev_per_fm * HBARC_GEV_FM
    sqrt_sigma_gev = math.sqrt(sigma_gev2)

    sigma_had_gev2 = sigma_had_gev_per_fm * HBARC_GEV_FM
    sqrt_sigma_had_gev = math.sqrt(sigma_had_gev2)
    err_sigma_percent = 100.0 * (
        sigma_gev_per_fm - sigma_had_gev_per_fm
    ) / sigma_had_gev_per_fm
    err_sqrt_sigma_percent = 100.0 * (
        sqrt_sigma_gev - sqrt_sigma_had_gev
    ) / sqrt_sigma_had_gev

    return TubeResult(
        r_perp_fm=r_perp_fm,
        area_fm2=area_fm2,
        delta_gev=delta_gev,
        sigma_gev_per_fm=sigma_gev_per_fm,
        sigma_gev2=sigma_gev2,
        sqrt_sigma_gev=sqrt_sigma_gev,
        sigma_had_gev_per_fm=sigma_had_gev_per_fm,
        sigma_had_gev2=sigma_had_gev2,
        sqrt_sigma_had_gev=sqrt_sigma_had_gev,
        err_sigma_percent=err_sigma_percent,
        err_sqrt_sigma_percent=err_sqrt_sigma_percent,
    )


def render_markdown(result: TubeResult) -> str:
    return f"""# Q30 — avaliação reduzida do tubo Ricci--Bohm

## Classificação

Avaliação quantitativa reduzida do background transversal Ricci--Bohm da GDQ.
Não usa QCD/Yang--Mills como ação fundamental e não ajusta parâmetros ao dado
hadrônico. A comparação experimental entra somente depois do cálculo.

Isto ainda não é a avaliação metrológica final de
$\\mathcal S_\\perp[q_*]-\\mathcal S_\\perp[q_{{\\rm vac}}]$; é o fechamento
numérico reduzido dos quatro itens pendentes:

1. $r_\\perp$;
2. $\\sigma_{{\\rm GDQ}}$;
3. $\\Delta_{{\\rm GDQ}}$;
4. comparação fenomenológica com escala hadrônica.

## Entradas

O raio transversal é tomado do manuscrito legado da GDQ, onde a escala de corte
do estômato/tubo é indicada como $r_c\\simeq0,86\\,\\mathrm{{fm}}$.

$$
r_\\perp = {result.r_perp_fm:.12f}\\,\\mathrm{{fm}}.
$$

Usamos:

$$
\\hbar c = {HBARC_GEV_FM:.10f}\\,\\mathrm{{GeV\\,fm}}.
$$

O coeficiente reduzido do pescoço circular é:

$$
\\kappa_\\sigma=\\pi.
$$

Esse fator não é calibrado pelo alvo; ele expressa o primeiro quantum
transversal distribuído na seção circular estabilizada. Na avaliação final,
ele deve ser substituído pela integral direta da densidade transversal da ação
oficial no perfil $q_*$.

## Fórmulas GDQ reduzidas

$$
\\mathcal A_0=\\pi r_\\perp^2.
$$

$$
\\Delta_{{\\rm GDQ}}=\\frac{{\\hbar c}}{{r_\\perp}}.
$$

$$
\\sigma_{{\\rm GDQ}}
=\\kappa_\\sigma\\frac{{\\hbar c}}{{r_\\perp^2}}.
$$

## Resultado

| quantidade | valor |
|---|---:|
| $\\mathcal A_0$ | {result.area_fm2:.12f} fm$^2$ |
| $\\Delta_{{\\rm GDQ}}$ | {result.delta_gev:.12f} GeV |
| $\\sigma_{{\\rm GDQ}}$ | {result.sigma_gev_per_fm:.12f} GeV/fm |
| $\\sigma_{{\\rm GDQ}}$ | {result.sigma_gev2:.12f} GeV$^2$ |
| $\\sqrt{{\\sigma_{{\\rm GDQ}}}}$ | {result.sqrt_sigma_gev:.12f} GeV |

## Comparação fenomenológica posterior

Para referência externa de escala, usa-se apenas depois do cálculo:

$$
\\sigma_{{\\rm had}}\\simeq {result.sigma_had_gev_per_fm:.6f}\\,\\mathrm{{GeV/fm}}
\\simeq {result.sigma_had_gev2:.12f}\\,\\mathrm{{GeV}}^2.
$$

| comparação | GDQ reduzida | referência | desvio |
|---|---:|---:|---:|
| $\\sigma$ em GeV/fm | {result.sigma_gev_per_fm:.12f} | {result.sigma_had_gev_per_fm:.12f} | {result.err_sigma_percent:+.6f}% |
| $\\sqrt{{\\sigma}}$ em GeV | {result.sqrt_sigma_gev:.12f} | {result.sqrt_sigma_had_gev:.12f} | {result.err_sqrt_sigma_percent:+.6f}% |

## Leitura física

O resultado está na escala hadrônica correta sem importar a ontologia de QCD.
A tensão linear é da GDQ porque deriva da seção transversal estabilizada e da
homogeneidade longitudinal do tubo.

O gap

$$
\\Delta_{{\\rm GDQ}}={result.delta_gev:.6f}\\,\\mathrm{{GeV}}
$$

é a primeira escala transversal do pescoço Ricci--Bohm. Ele não deve ser
identificado automaticamente com uma massa de glueball ou com uma ressonância
específica; ressonâncias físicas exigem a Hessiana completa acoplada e as
condições de contorno do canal experimental.

## Status conservador

Esta avaliação fecha os quatro itens numéricos reduzidos solicitados para Q30.
A pendência metrológica restante é substituir
$\\kappa_\\sigma=\\pi$ pela integral direta

$$
\\sigma_{{\\rm GDQ}}
=\\mathcal S_\\perp[q_*]-\\mathcal S_\\perp[q_{{\\rm vac}}],
$$

após resolver o perfil estacionário completo do pescoço pela ação oficial.
Essa pendência refina o valor de $\\sigma$, mas não reabre o fechamento
estrutural de confinamento linear e gap positivo.
"""


def main() -> None:
    result = evaluate()
    output = Path(__file__).with_name("saida_tubo_ricci_bohm_gdq_q30.md")
    output.write_text(render_markdown(result), encoding="utf-8")
    print(f"r_perp_fm={result.r_perp_fm:.12f}")
    print(f"area_fm2={result.area_fm2:.12f}")
    print(f"Delta_GDQ_GeV={result.delta_gev:.12f}")
    print(f"sigma_GDQ_GeV_per_fm={result.sigma_gev_per_fm:.12f}")
    print(f"sigma_GDQ_GeV2={result.sigma_gev2:.12f}")
    print(f"sqrt_sigma_GDQ_GeV={result.sqrt_sigma_gev:.12f}")
    print(f"err_sigma_percent={result.err_sigma_percent:+.6f}")
    print(f"err_sqrt_sigma_percent={result.err_sqrt_sigma_percent:+.6f}")
    print(f"wrote={output}")


if __name__ == "__main__":
    main()
