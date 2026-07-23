#!/usr/bin/env python3
"""
Q30/Q40 — derivação do raio efetivo de superfície e fator de forma.

Cadeia usada:
    Q39: epsilon_eff = 5 alpha/pi - [(4/9) alpha^2 - (pi/2) alpha^3]
    Q40: r_p = C_r epsilon_eff R_B
         C_r = (1/8)(1 + alpha/4)
         R_B = (3/2) Lambda_C

Esse é o raio de superfície/projeção Hopf canônico já consolidado em Q40.
Depois calculamos, para Q30:

    F_shape = (r_perp / r_p)^2
    sigma = F_shape pi hbar c / r_perp^2 = pi hbar c / r_p^2

Classificação:
    Derivação condicional cruzada Q39/Q40 aplicada à Q30. Não usa a tensão
    hadrônica como entrada.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


ALPHA_INV = 137.03599907
LAMBDA_C_FM = 386.159268
HBARC_GEV_FM = 0.1973269804
R_PRIMITIVE_FM = 0.86
SIGMA_HAD_GEV_PER_FM = 0.89

# Raio legado de compressão/probe, mantido apenas para auditoria comparativa.
R_LEGACY_COMPRESSED_FM = 0.8354


@dataclass(frozen=True)
class RadiusResult:
    alpha: float
    epsilon_classic: float
    delta_epsilon: float
    epsilon_eff: float
    c_r: float
    r_b_fm: float
    r_surface_fm: float
    f_shape_surface: float
    sigma_surface_gev_per_fm: float
    sigma_surface_gev2: float
    sqrt_sigma_surface_gev: float
    delta_surface_gev: float
    err_sigma_surface_percent: float
    f_shape_legacy: float
    sigma_legacy_gev_per_fm: float
    err_sigma_legacy_percent: float


def evaluate() -> RadiusResult:
    alpha = 1.0 / ALPHA_INV
    epsilon_classic = 5.0 * alpha / math.pi
    delta_epsilon = (4.0 / 9.0) * alpha**2 - (math.pi / 2.0) * alpha**3
    epsilon_eff = epsilon_classic - delta_epsilon
    c_r = 0.125 * (1.0 + alpha / 4.0)
    r_b = 1.5 * LAMBDA_C_FM
    r_surface = c_r * epsilon_eff * r_b

    f_shape_surface = (R_PRIMITIVE_FM / r_surface) ** 2
    sigma_surface = math.pi * HBARC_GEV_FM / r_surface**2
    sigma_surface_gev2 = sigma_surface * HBARC_GEV_FM
    sqrt_sigma_surface = math.sqrt(sigma_surface_gev2)
    delta_surface = HBARC_GEV_FM / r_surface
    err_sigma_surface = 100.0 * (
        sigma_surface - SIGMA_HAD_GEV_PER_FM
    ) / SIGMA_HAD_GEV_PER_FM

    f_shape_legacy = (R_PRIMITIVE_FM / R_LEGACY_COMPRESSED_FM) ** 2
    sigma_legacy = math.pi * HBARC_GEV_FM / R_LEGACY_COMPRESSED_FM**2
    err_sigma_legacy = 100.0 * (
        sigma_legacy - SIGMA_HAD_GEV_PER_FM
    ) / SIGMA_HAD_GEV_PER_FM

    return RadiusResult(
        alpha=alpha,
        epsilon_classic=epsilon_classic,
        delta_epsilon=delta_epsilon,
        epsilon_eff=epsilon_eff,
        c_r=c_r,
        r_b_fm=r_b,
        r_surface_fm=r_surface,
        f_shape_surface=f_shape_surface,
        sigma_surface_gev_per_fm=sigma_surface,
        sigma_surface_gev2=sigma_surface_gev2,
        sqrt_sigma_surface_gev=sqrt_sigma_surface,
        delta_surface_gev=delta_surface,
        err_sigma_surface_percent=err_sigma_surface,
        f_shape_legacy=f_shape_legacy,
        sigma_legacy_gev_per_fm=sigma_legacy,
        err_sigma_legacy_percent=err_sigma_legacy,
    )


def render_markdown(result: RadiusResult) -> str:
    legacy_pt = f"{R_LEGACY_COMPRESSED_FM:.4f}".replace(".", ",")
    return f"""# Q30/Q40 — derivação do raio efetivo de superfície

## Enunciado

Queremos obter o raio usado no fator de forma da Q30 sem ajustá-lo pela tensão
hadrônica.

O raio canônico já consolidado na Q40 é um raio eletromagnético de superfície,
não uma média volumétrica do bulk:

$$
r_p=C_r\\epsilon_{{\\rm eff}}R_B.
$$

## Cadeia dedutiva

Da Q39, o raio angular efetivo do estômato é:

$$
\\epsilon_{{\\rm eff}}
=\\frac{{5\\alpha}}{{\\pi}}
-\\left(
\\frac49\\alpha^2-\\frac\\pi2\\alpha^3
\\right).
$$

Numericamente:

$$
\\epsilon_{{\\rm eff}}
={result.epsilon_eff:.12f}.
$$

Da Q40, a projeção Hopf de superfície fornece:

$$
C_r=\\frac18\\left(1+\\frac\\alpha4\\right).
$$

Numericamente:

$$
C_r={result.c_r:.12f}.
$$

A escala bariônica é:

$$
R_B=\\frac32\\Lambda_C.
$$

Com:

$$
\\Lambda_C={LAMBDA_C_FM:.6f}\\,\\mathrm{{fm}},
$$

obtemos:

$$
R_B={result.r_b_fm:.12f}\\,\\mathrm{{fm}}.
$$

Portanto:

$$
r_p
=C_r\\epsilon_{{\\rm eff}}R_B
={result.r_surface_fm:.12f}\\,\\mathrm{{fm}}.
$$

## Aplicação à Q30

O cap primitivo da Q30 usava:

$$
r_\\perp={R_PRIMITIVE_FM:.12f}\\,\\mathrm{{fm}}.
$$

O fator de forma induzido pelo raio de superfície derivado é:

$$
F_{{\\rm shape}}
=\\left(\\frac{{r_\\perp}}{{r_p}}\\right)^2
={result.f_shape_surface:.12f}.
$$

A tensão correspondente é:

$$
\\sigma_{{\\rm GDQ}}
=F_{{\\rm shape}}\\pi\\frac{{\\hbar c}}{{r_\\perp^2}}
=\\pi\\frac{{\\hbar c}}{{r_p^2}}
={result.sigma_surface_gev_per_fm:.12f}\\,\\mathrm{{GeV/fm}}.
$$

Em unidades de $\\mathrm{{GeV}}^2$:

$$
\\sigma_{{\\rm GDQ}}
={result.sigma_surface_gev2:.12f}\\,\\mathrm{{GeV}}^2.
$$

E:

$$
\\sqrt{{\\sigma_{{\\rm GDQ}}}}
={result.sqrt_sigma_surface_gev:.12f}\\,\\mathrm{{GeV}}.
$$

Comparação posterior com
$\\sigma_{{\\rm had}}\\simeq{SIGMA_HAD_GEV_PER_FM:.6f}\\,\\mathrm{{GeV/fm}}$:

$$
{result.err_sigma_surface_percent:+.6f}\\%.
$$

## Auditoria do raio legado comprimido

O raio antigo:

$$
r_{{\\rm legacy}}={R_LEGACY_COMPRESSED_FM:.12f}\\,\\mathrm{{fm}}
$$

não é o raio canônico derivado pela Q40. Ele representa uma compressão de
sonda/probe registrada historicamente. Se usado, produz:

$$
F_{{\\rm shape,legacy}}
={result.f_shape_legacy:.12f},
$$

e:

$$
\\sigma_{{\\rm legacy}}
={result.sigma_legacy_gev_per_fm:.12f}\\,\\mathrm{{GeV/fm}},
$$

com desvio:

$$
{result.err_sigma_legacy_percent:+.6f}\\%.
$$

## Status

O raio derivado pela cadeia Q39/Q40 é:

$$
\\boxed{{
r_p={result.r_surface_fm:.12f}\\,\\mathrm{{fm}}
}}
$$

Esse raio não usa a tensão hadrônica como entrada. A Q30, usando esse raio,
fica com:

$$
\\boxed{{
F_{{\\rm shape}}={result.f_shape_surface:.12f}
}}
$$

e:

$$
\\boxed{{
\\sigma_{{\\rm GDQ}}
={result.sigma_surface_gev_per_fm:.12f}\\,\\mathrm{{GeV/fm}}.
}}
$$

O fechamento com ${legacy_pt}\\,\\mathrm{{fm}}$ permanece
como cenário de compressão de sonda, não como raio canônico de superfície.
"""


def main() -> None:
    result = evaluate()
    output = Path(__file__).with_name("derivacao_raio_efetivo_q30_q40.md")
    output.write_text(render_markdown(result), encoding="utf-8")
    print(f"alpha={result.alpha:.15f}")
    print(f"epsilon_eff={result.epsilon_eff:.12f}")
    print(f"C_r={result.c_r:.12f}")
    print(f"R_B_fm={result.r_b_fm:.12f}")
    print(f"r_surface_fm={result.r_surface_fm:.12f}")
    print(f"F_shape_surface={result.f_shape_surface:.12f}")
    print(f"sigma_surface_GeV_per_fm={result.sigma_surface_gev_per_fm:.12f}")
    print(f"sigma_surface_GeV2={result.sigma_surface_gev2:.12f}")
    print(f"err_sigma_surface_percent={result.err_sigma_surface_percent:+.6f}")
    print(f"F_shape_legacy={result.f_shape_legacy:.12f}")
    print(f"sigma_legacy_GeV_per_fm={result.sigma_legacy_gev_per_fm:.12f}")
    print(f"err_sigma_legacy_percent={result.err_sigma_legacy_percent:+.6f}")
    print(f"wrote={output}")


if __name__ == "__main__":
    main()
