#!/usr/bin/env python3
"""
Q30 — fator de forma a partir do raio efetivo já presente no corpus.

Fonte do raio efetivo:
    pt-br/notas/27/nota_27.4_raio_do_proton.md
    r_eff = r_{p(mu)} = 0.8354 fm

Uso:
    O cap primitivo usava r_perp = 0.86 fm e C_GDQ = pi.
    Se a solução transversal efetiva contrai o raio para r_eff, então:

        F_shape = (r_perp / r_eff)^2

    e

        sigma = F_shape * pi * hbar c / r_perp^2
              = pi * hbar c / r_eff^2.

Classificação:
    Reavaliação com raio efetivo legado da GDQ. Não ajusta F_shape usando
    sigma_had, mas o raio efetivo legado tem origem fenomenológica/setorial e
    deve ser tratado como entrada condicionada até ser rederivado da ação
    oficial no mesmo background transversal.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


HBARC_GEV_FM = 0.1973269804
R_PRIMITIVE_FM = 0.86
R_EFFECTIVE_FM = 0.8354
SIGMA_HAD_GEV_PER_FM = 0.89


@dataclass(frozen=True)
class ShapeResult:
    r_primitive_fm: float
    r_effective_fm: float
    f_shape: float
    c_effective: float
    sigma_gev_per_fm: float
    sigma_gev2: float
    sqrt_sigma_gev: float
    delta_gev: float
    err_sigma_percent: float
    err_sqrt_sigma_percent: float


def evaluate() -> ShapeResult:
    f_shape = (R_PRIMITIVE_FM / R_EFFECTIVE_FM) ** 2
    c_effective = math.pi * f_shape
    sigma = c_effective * HBARC_GEV_FM / R_PRIMITIVE_FM**2
    sigma_gev2 = sigma * HBARC_GEV_FM
    sqrt_sigma = math.sqrt(sigma_gev2)
    delta = HBARC_GEV_FM / R_EFFECTIVE_FM

    sigma_had_gev2 = SIGMA_HAD_GEV_PER_FM * HBARC_GEV_FM
    sqrt_sigma_had = math.sqrt(sigma_had_gev2)
    err_sigma = 100.0 * (sigma - SIGMA_HAD_GEV_PER_FM) / SIGMA_HAD_GEV_PER_FM
    err_sqrt = 100.0 * (sqrt_sigma - sqrt_sigma_had) / sqrt_sigma_had

    return ShapeResult(
        r_primitive_fm=R_PRIMITIVE_FM,
        r_effective_fm=R_EFFECTIVE_FM,
        f_shape=f_shape,
        c_effective=c_effective,
        sigma_gev_per_fm=sigma,
        sigma_gev2=sigma_gev2,
        sqrt_sigma_gev=sqrt_sigma,
        delta_gev=delta,
        err_sigma_percent=err_sigma,
        err_sqrt_sigma_percent=err_sqrt,
    )


def render_markdown(result: ShapeResult) -> str:
    r_primitive_pt = f"{result.r_primitive_fm:.2f}".replace(".", ",")
    r_effective_pt = f"{result.r_effective_fm:.4f}".replace(".", ",")
    sigma_pt = f"{result.sigma_gev_per_fm:.12f}".replace(".", ",")
    return f"""# Q30 — fator de forma pelo raio efetivo legado

## Enunciado

O cap Ricci--Bohm primitivo com $r_\\perp={r_primitive_pt}\\,\\mathrm{{fm}}$
gera:

$$
C_{{\\rm GDQ}}=\\pi.
$$

Mas esse cap não bate metrologicamente com a escala hadrônica de tensão. O
corpus legado já contém um raio efetivo contraído:

$$
r_{{\\rm eff}}={r_effective_pt}\\,\\mathrm{{fm}},
$$

registrado em `pt-br/notas/27/nota_27.4_raio_do_proton.md` como raio efetivo
do próton sob compressão muônica.

## Cálculo do fator de forma

Se a contração efetiva atua na seção transversal do tubo, então:

$$
F_{{\\rm shape}}
=\\left(\\frac{{r_\\perp}}{{r_{{\\rm eff}}}}\\right)^2.
$$

Logo:

$$
F_{{\\rm shape}}
={result.f_shape:.12f}.
$$

O coeficiente efetivo é:

$$
C_{{\\rm eff}}
=\\pi F_{{\\rm shape}}
={result.c_effective:.12f}.
$$

E a tensão corrigida fica:

$$
\\sigma_{{\\rm GDQ}}^{{\\rm eff}}
=F_{{\\rm shape}}\\pi\\frac{{\\hbar c}}{{r_\\perp^2}}
=\\pi\\frac{{\\hbar c}}{{r_{{\\rm eff}}^2}}.
$$

## Resultado

| quantidade | valor |
|---|---:|
| $r_\\perp$ primitivo | {result.r_primitive_fm:.12f} fm |
| $r_{{\\rm eff}}$ | {result.r_effective_fm:.12f} fm |
| $F_{{\\rm shape}}$ | {result.f_shape:.12f} |
| $C_{{\\rm eff}}$ | {result.c_effective:.12f} |
| $\\Delta_{{\\rm eff}}=\\hbar c/r_{{\\rm eff}}$ | {result.delta_gev:.12f} GeV |
| $\\sigma_{{\\rm GDQ}}^{{\\rm eff}}$ | {result.sigma_gev_per_fm:.12f} GeV/fm |
| $\\sigma_{{\\rm GDQ}}^{{\\rm eff}}$ | {result.sigma_gev2:.12f} GeV$^2$ |
| $\\sqrt{{\\sigma_{{\\rm GDQ}}^{{\\rm eff}}}}$ | {result.sqrt_sigma_gev:.12f} GeV |

## Comparação posterior

Com:

$$
\\sigma_{{\\rm had}}\\simeq{SIGMA_HAD_GEV_PER_FM:.6f}\\,\\mathrm{{GeV/fm}},
$$

o desvio fica:

$$
{result.err_sigma_percent:+.6f}\\%.
$$

Em $\\sqrt{{\\sigma}}$:

$$
{result.err_sqrt_sigma_percent:+.6f}\\%.
$$

## Status conservador

O fator de forma calculado a partir do raio efetivo legado praticamente fecha a
escala de tensão:

$$
\\sigma_{{\\rm GDQ}}^{{\\rm eff}}
={sigma_pt}\\,\\mathrm{{GeV/fm}}.
$$

Isso ainda deve ser classificado como fechamento condicionado ao raio efetivo
setorial $r_{{\\rm eff}}={r_effective_pt}\\,\\mathrm{{fm}}$.
Para virar previsão metrológica final da Q30, o mesmo $r_{{\\rm eff}}$ precisa
ser rederivado no background transversal da ação oficial, e não apenas
importado do setor legado de raio do próton.
"""


def main() -> None:
    result = evaluate()
    output = Path(__file__).with_name("saida_fator_forma_raio_efetivo_q30.md")
    output.write_text(render_markdown(result), encoding="utf-8")
    print(f"r_primitive_fm={result.r_primitive_fm:.12f}")
    print(f"r_effective_fm={result.r_effective_fm:.12f}")
    print(f"F_shape={result.f_shape:.12f}")
    print(f"C_effective={result.c_effective:.12f}")
    print(f"Delta_eff_GeV={result.delta_gev:.12f}")
    print(f"sigma_eff_GeV_per_fm={result.sigma_gev_per_fm:.12f}")
    print(f"sigma_eff_GeV2={result.sigma_gev2:.12f}")
    print(f"sqrt_sigma_eff_GeV={result.sqrt_sigma_gev:.12f}")
    print(f"err_sigma_percent={result.err_sigma_percent:+.6f}")
    print(f"err_sqrt_sigma_percent={result.err_sqrt_sigma_percent:+.6f}")
    print(f"wrote={output}")


if __name__ == "__main__":
    main()
