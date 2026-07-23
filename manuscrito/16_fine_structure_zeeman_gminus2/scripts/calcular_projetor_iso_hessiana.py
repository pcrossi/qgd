#!/usr/bin/env python3
"""GDQ — Capítulo 16: projetor isotrópico do canal elétrico.

Classificação:
    avaliação direta de quantidade derivada.

O script avalia o fator

    P_iso = pi^-4 * <(n.u)^4>_{S^3} * (Tr_CS 1_3)^2

que aparece quando a Hessiana física média do ensemble de Einstein é escalar
no subespaço físico de quatro direções. O cálculo não usa o valor experimental
de alpha.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    angular_normalization = 1.0 / math.pi**4
    hopf_haar_fourth_moment = 1.0 / 8.0
    cartan_schouten_trace_squared = 3.0**2

    p_iso = (
        angular_normalization
        * hopf_haar_fourth_moment
        * cartan_schouten_trace_squared
    )
    p_iso_closed = 9.0 / (8.0 * math.pi**4)

    c_e = (math.pi**5 / 1920.0) ** 0.25
    alpha_mean = p_iso * c_e
    z_q = 1.0 / (4.0 * math.pi * alpha_mean)

    text = f"""# Saída — projetor isotrópico da Hessiana

Classificação: avaliação direta de quantidade derivada; não usa CODATA.

| quantidade | valor |
|---|---:|
| normalização angular $\\pi^{{-4}}$ | {angular_normalization:.15e} |
| momento de Haar $\\langle(n\\cdot u)^4\\rangle_{{S^3}}$ | {hopf_haar_fourth_moment:.15e} |
| traço coerente Cartan--Schouten ao quadrado | {cartan_schouten_trace_squared:.15e} |
| $\\mathcal P_{{\\rm iso}}$ calculado | {p_iso:.15e} |
| $9/(8\\pi^4)$ | {p_iso_closed:.15e} |
| diferença | {p_iso - p_iso_closed:.3e} |
| $\\alpha_E^{{\\rm mean}}$ | {alpha_mean:.15e} |
| $(\\alpha_E^{{\\rm mean}})^{{-1}}$ | {1.0 / alpha_mean:.12f} |
| $Z_Q^E=1/(4\\pi\\alpha_E^{{\\rm mean}})$ | {z_q:.12f} |

Interpretação: a Hessiana média cancela na razão projetiva por isotropia de
Schur. O fator remanescente é a contração angular/torsional do canal elétrico.
"""

    assert abs(p_iso - p_iso_closed) < 1e-15
    out = Path(__file__).resolve().parent / "saida_calcular_projetor_iso_hessiana.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
