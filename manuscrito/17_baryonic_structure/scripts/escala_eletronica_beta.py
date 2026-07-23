#!/usr/bin/env python3
"""Escala eletrônica por endpoint beta.

Classificação:
    determinação metrológica / consequência analítica reduzida.

O script mostra que, uma vez derivado:

    delta_B = ln(2*pi^2) * 3*sqrt(2)/5,

o endpoint beta:

    Q_beta = M_n - M_p - M_e

implica:

    Q_beta = (delta_B - 1) M_e c^2

e portanto:

    M_e c^2 = Q_beta/(delta_B - 1).

O endpoint Q_beta é dado experimental de contorno/metrologia. Ele não é usado
para ajustar delta_B.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_escala_eletronica_beta.md"


def main() -> None:
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)

    q_beta_mev = 0.782333559310
    me_ref_mev = 0.51099895000
    me_beta_mev = q_beta_mev / (delta_b - 1.0)
    abs_err = me_beta_mev - me_ref_mev
    rel_err = abs_err / me_ref_mev

    # Inversão alternativa pela vida média total reduzida, menos precisa porque
    # depende do fechamento de taxa total e não apenas do endpoint cinemático.
    alpha_inv = 137.035999177
    hbar_gev_s = 6.582119569e-25
    tau_ref_s = 878.3
    me_tau_gev = (32.0 / 15.0) * (alpha_inv**11) * hbar_gev_s / tau_ref_s
    me_tau_mev = 1000.0 * me_tau_gev
    rel_tau = (me_tau_mev - me_ref_mev) / me_ref_mev

    text = f"""# Saída — escala eletrônica por beta

Classificação: determinação metrológica / consequência analítica reduzida.

## Fórmula

$$
Q_\\beta=(\\delta_B-1)M_ec^2.
$$

Logo:

$$
M_ec^2=\\frac{{Q_\\beta}}{{\\delta_B-1}}.
$$

## Avaliação por endpoint

| quantidade | valor |
|---|---:|
| delta_B | {delta_b:.12f} |
| Q_beta MeV | {q_beta_mev:.12f} |
| M_e c^2 por beta MeV | {me_beta_mev:.12f} |
| M_e c^2 referência MeV | {me_ref_mev:.12f} |
| erro absoluto MeV | {abs_err:.12e} |
| erro relativo | {rel_err:.12e} |

## Inversão alternativa por vida média

| quantidade | valor |
|---|---:|
| tau_n referência s | {tau_ref_s:.12f} |
| M_e c^2 por tau_n MeV | {me_tau_mev:.12f} |
| erro relativo por tau_n | {rel_tau:.12e} |

## Veredito

A rota por endpoint beta fornece uma determinação metrológica da escala
eletrônica com erro relativo de ordem $10^{{-4}}$. A rota por vida média é
menos precisa no estágio reduzido atual, pois carrega as aproximações da taxa
total.
"""

    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
