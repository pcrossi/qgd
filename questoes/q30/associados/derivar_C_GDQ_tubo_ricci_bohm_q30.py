#!/usr/bin/env python3
"""
Q30 — derivação reduzida de C_GDQ no pescoço Ricci--Bohm.

Ideia:
    O coeficiente adimensional da tensão não deve ser escolhido pelo alvo.
    No setor transversal reduzido da GDQ, o pescoço estabilizado é representado
    pelo cap Ricci--Bohm primitivo: uma 2-seção compacta com bordo geodésico.

    Na redução on-shell, o termo transversal relevante é o índice de curvatura

        C_GDQ = (1/4) int_cap R_2 dA.

    Para o cap primitivo hemisférico de raio r:

        R_2 = 2/r^2,
        Area(cap) = 2*pi*r^2,
        C_GDQ = (1/4) * (2/r^2) * (2*pi*r^2) = pi.

    O resultado é topológico/geometrico: pelo Gauss--Bonnet, o cap com bordo
    geodésico tem int K dA = 2*pi e R_2=2K.

Classificação:
    Derivação reduzida no setor Ricci--Bohm transversal. Não é solução 8D
    geral do perfil q_*; é o fechamento do coeficiente usado na avaliação
    reduzida da Q30.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
R_PERP_FM = 0.86
SIGMA_HAD_GEV_PER_FM = 0.89


@dataclass(frozen=True)
class CGDQResult:
    r_perp_fm: float
    cap_area_fm2: float
    projected_area_fm2: float
    scalar_curvature_fm_inv2: float
    int_R_dA: float
    c_gdq: float
    sigma_gev_per_fm: float
    sigma_gev2: float
    sqrt_sigma_gev: float
    delta_gev: float
    err_sigma_percent: float
    err_sqrt_sigma_percent: float
    c_required: float
    f_shape_required: float
    r_required_fm: float
    cap_angle_required_deg: float


def evaluate(r: float = R_PERP_FM) -> CGDQResult:
    cap_area = 2.0 * math.pi * r**2
    projected_area = math.pi * r**2
    scalar_curvature = 2.0 / r**2
    int_R_dA = scalar_curvature * cap_area
    c_gdq = 0.25 * int_R_dA

    sigma = c_gdq * HBARC_GEV_FM / r**2
    sigma_gev2 = sigma * HBARC_GEV_FM
    sqrt_sigma = math.sqrt(sigma_gev2)
    delta = HBARC_GEV_FM / r

    sigma_had_gev2 = SIGMA_HAD_GEV_PER_FM * HBARC_GEV_FM
    sqrt_sigma_had = math.sqrt(sigma_had_gev2)
    err_sigma = 100.0 * (sigma - SIGMA_HAD_GEV_PER_FM) / SIGMA_HAD_GEV_PER_FM
    err_sqrt = 100.0 * (sqrt_sigma - sqrt_sigma_had) / sqrt_sigma_had
    c_required = SIGMA_HAD_GEV_PER_FM * r**2 / HBARC_GEV_FM
    f_shape_required = c_required / c_gdq
    r_required_fm = math.sqrt(c_gdq * HBARC_GEV_FM / SIGMA_HAD_GEV_PER_FM)
    cap_angle_required_deg = math.degrees(math.acos(1.0 - f_shape_required))

    return CGDQResult(
        r_perp_fm=r,
        cap_area_fm2=cap_area,
        projected_area_fm2=projected_area,
        scalar_curvature_fm_inv2=scalar_curvature,
        int_R_dA=int_R_dA,
        c_gdq=c_gdq,
        sigma_gev_per_fm=sigma,
        sigma_gev2=sigma_gev2,
        sqrt_sigma_gev=sqrt_sigma,
        delta_gev=delta,
        err_sigma_percent=err_sigma,
        err_sqrt_sigma_percent=err_sqrt,
        c_required=c_required,
        f_shape_required=f_shape_required,
        r_required_fm=r_required_fm,
        cap_angle_required_deg=cap_angle_required_deg,
    )


def render_markdown(result: CGDQResult) -> str:
    return rf"""# Q30 — derivação reduzida de $C_{{\\rm GDQ}}$ no tubo Ricci--Bohm

## Enunciado

Queremos remover a ambiguidade do coeficiente na fórmula reduzida:

$$
\\sigma_{{\\rm GDQ}}
=C_{{\\rm GDQ}}\\frac{{\\hbar c}}{{r_\\perp^2}}.
$$

A pergunta é se $C_{{\\rm GDQ}}$ foi ajustado ou se sai da geometria
transversal da ação oficial reduzida.

## Setor usado

Usamos o setor transversal Ricci--Bohm já adotado na Q30. Ele é uma redução da
ação oficial na seção normal ao tubo, não uma ação Yang--Mills/QCD.

O cap transversal primitivo é uma 2-seção compacta com bordo geodésico. Em
coordenadas internas:

$$
ds_\\perp^2
=r_\\perp^2(d\\chi^2+\\sin^2\\chi\\,d\\theta^2),
\\qquad
0\\le\\chi\\le\\frac\\pi2.
$$

O bordo em $\\chi=\\pi/2$ é geodésico. Assim, pelo Gauss--Bonnet:

$$
\\int_{{\\rm cap}}K\\,dA=2\\pi.
$$

Como em duas dimensões $R_2=2K$:

$$
\\int_{{\\rm cap}}R_2\,dA=4\\pi.
$$

## Coeficiente on-shell

Na equação transversal Ricci--Bohm da GDQ, o balanço entre curvatura e pressão
de Bohm deixa, no setor on-shell primitivo, o índice reduzido:

$$
C_{{\\rm GDQ}}
=\\frac14\\int_{{\\rm cap}}R_2\,dA.
$$

Logo:

$$
C_{{\\rm GDQ}}
=\\frac14(4\\pi)
=\\boxed{{\\pi}}.
$$

Portanto, o fator $\\pi$ não vem do dado hadrônico. Ele é a carga geométrica do
cap Ricci--Bohm primitivo.

## Avaliação numérica

Com:

$$
r_\\perp={result.r_perp_fm:.12f}\\,\\mathrm{{fm}},
\\qquad
\\hbar c={HBARC_GEV_FM:.10f}\\,\\mathrm{{GeV\\,fm}},
$$

temos:

| quantidade | valor |
|---|---:|
| área intrínseca do cap | {result.cap_area_fm2:.12f} fm$^2$ |
| área projetada do disco | {result.projected_area_fm2:.12f} fm$^2$ |
| $R_2$ | {result.scalar_curvature_fm_inv2:.12f} fm$^{{-2}}$ |
| $\\int R_2 dA$ | {result.int_R_dA:.12f} |
| $C_{{\\rm GDQ}}$ | {result.c_gdq:.12f} |
| $\\Delta_{{\\rm GDQ}}$ | {result.delta_gev:.12f} GeV |
| $\\sigma_{{\\rm GDQ}}$ | {result.sigma_gev_per_fm:.12f} GeV/fm |
| $\\sigma_{{\\rm GDQ}}$ | {result.sigma_gev2:.12f} GeV$^2$ |
| $\\sqrt{{\\sigma_{{\\rm GDQ}}}}$ | {result.sqrt_sigma_gev:.12f} GeV |

Comparação posterior com
$\\sigma_{{\\rm had}}\\simeq{SIGMA_HAD_GEV_PER_FM:.6f}\\,\\mathrm{{GeV/fm}}$:

$$
\\frac{{\\sigma_{{\\rm GDQ}}-\\sigma_{{\\rm had}}}}{{\\sigma_{{\\rm had}}}}
={result.err_sigma_percent:+.6f}\\%.
$$

Em $\\sqrt{{\\sigma}}$:

$$
{result.err_sqrt_sigma_percent:+.6f}\\%.
$$

## Relação com a integração do disco

A integração anterior do disco usava:

$$
\\varepsilon_\\sigma=\\frac{{\\hbar c}}{{r_\\perp^4}}.
$$

Agora essa densidade reduzida fica interpretada como a representação projetada
do índice de curvatura do cap Ricci--Bohm. Integrando no disco projetado:

$$
\\int_0^{{r_\\perp}}2\\pi s\,ds\\,
\\frac{{\\hbar c}}{{r_\\perp^4}}
=\\pi\\frac{{\\hbar c}}{{r_\\perp^2}},
$$

que coincide com $C_{{\\rm GDQ}}\\hbar c/r_\\perp^2$.

## Limite de validade

Este fechamento é forte no setor transversal reduzido. Ele ainda não equivale
à solução 8D geral de:

$$
\\sigma_{{\\rm GDQ}}
=\\mathcal S_\\perp[q_*]-\\mathcal S_\\perp[q_{{\\rm vac}}],
$$

com todos os modos de $g$, $J$, $H$, $f$ e os contornos da ação oficial. A
integração 8D completa pode corrigir o valor por um fator de forma:

$$
\\sigma_{{\\rm full}}
=F_{{\\rm shape}}\\,\\pi\\frac{{\\hbar c}}{{r_\\perp^2}}.
$$

No setor primitivo Ricci--Bohm:

$$
F_{{\\rm shape}}=1.
$$

## Auditoria de discrepância

O cap primitivo não bate metrologicamente com a escala hadrônica de referência.
O desvio em tensão é:

$$
{result.err_sigma_percent:+.6f}\\%.
$$

Mantendo $r_\\perp={result.r_perp_fm:.12f}\\,\\mathrm{{fm}}$, o coeficiente
necessário para igualar
$\\sigma_{{\\rm had}}\\simeq{SIGMA_HAD_GEV_PER_FM:.6f}\\,\\mathrm{{GeV/fm}}$
seria:

$$
C_{{\\rm req}}={result.c_required:.12f}.
$$

Logo, o fator de forma requerido é:

$$
F_{{\\rm shape,req}}
=\\frac{{C_{{\\rm req}}}}{{\\pi}}
={result.f_shape_required:.12f}.
$$

Isto equivale a uma correção de forma de
${100.0 * (result.f_shape_required - 1.0):.6f}\\%$ sobre o cap primitivo.

Se mantivermos $F_{{\\rm shape}}=1$, o raio efetivo necessário seria:

$$
r_{{\\rm req}}={result.r_required_fm:.12f}\\,\\mathrm{{fm}}.
$$

Na parametrização por cap esférico, $C=\\pi(1-\\cos\\chi_0)$. O coeficiente
requerido corresponderia a:

$$
\\chi_0={result.cap_angle_required_deg:.6f}^\\circ,
$$

isto é, cerca de
${result.cap_angle_required_deg - 90.0:.6f}^\\circ$ acima do hemisfério.

## Status

O coeficiente do cap primitivo fica derivado:

$$
\\boxed{{
C_{{\\rm GDQ}}=\\pi
}}
$$

e a tensão reduzida do cap primitivo permanece:

$$
\\boxed{{
\\sigma_{{\\rm GDQ}}
={result.sigma_gev_per_fm:.12f}\\,\\mathrm{{GeV/fm}}.
}}
$$

Status conservador: não fechado metrologicamente. O que está fechado é o cap
Ricci--Bohm primitivo. O valor físico final exige derivar
$F_{{\\rm shape}}$ ou $r_{{\\rm eff}}$ a partir do perfil transversal completo.
""".replace("\\\\", "\\")


def main() -> None:
    result = evaluate()
    output = Path(__file__).with_name("derivacao_C_GDQ_tubo_ricci_bohm_q30.md")
    output.write_text(render_markdown(result), encoding="utf-8")
    print(f"C_GDQ={result.c_gdq:.12f}")
    print(f"int_R_dA={result.int_R_dA:.12f}")
    print(f"sigma_GDQ_GeV_per_fm={result.sigma_gev_per_fm:.12f}")
    print(f"sigma_GDQ_GeV2={result.sigma_gev2:.12f}")
    print(f"sqrt_sigma_GDQ_GeV={result.sqrt_sigma_gev:.12f}")
    print(f"Delta_GDQ_GeV={result.delta_gev:.12f}")
    print(f"err_sigma_percent={result.err_sigma_percent:+.6f}")
    print(f"err_sqrt_sigma_percent={result.err_sqrt_sigma_percent:+.6f}")
    print(f"C_required={result.c_required:.12f}")
    print(f"F_shape_required={result.f_shape_required:.12f}")
    print(f"r_required_fm={result.r_required_fm:.12f}")
    print(f"cap_angle_required_deg={result.cap_angle_required_deg:.6f}")
    print(f"wrote={output}")


if __name__ == "__main__":
    main()
