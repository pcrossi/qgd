#!/usr/bin/env python3
"""Q48 — cálculo direto do raio de Zemach por fatores de forma Q40.

Usa a fórmula:

    r_Z = -(4/pi) int_0^inf dq/q^2 [G_E(q) G_M(q)/G_M(0) - 1]

Para o fechamento líder Q40:

    G_E^p(q) = j0(q r_E)
    G_M^p(q)/mu_p = j0(q r_M)

com r_E=r_M=r_p no primeiro fechamento geométrico.
"""

from __future__ import annotations

from math import pi
from pathlib import Path
import warnings

import numpy as np
from scipy.integrate import IntegrationWarning, quad


OUT = Path(__file__).with_name("saida_calculo_direto_zemach_q48.md")

r_p = 0.84077876545  # fm


def j0(x: float) -> float:
    if abs(x) < 1.0e-8:
        return 1.0 - x * x / 6.0 + x**4 / 120.0
    return np.sin(x) / x


def normalized_product(q: float, r_e: float, r_m: float) -> float:
    return j0(q * r_e) * j0(q * r_m)


def integrand(q: float, r_e: float, r_m: float) -> float:
    if q < 1.0e-7:
        # product = 1 - q^2(r_e^2+r_m^2)/6 + O(q^4)
        return -(r_e * r_e + r_m * r_m) / 6.0
    return (normalized_product(q, r_e, r_m) - 1.0) / (q * q)


def zemach_numeric(r_e: float, r_m: float) -> tuple[float, float]:
    # Evita a integração direta em [0, infinito), que é correta mas pode emitir
    # aviso de roundoff por causa do termo oscilatório de j0(q r_E) j0(q r_M).
    # Para q grande:
    #
    #   [j0(q r_E) j0(q r_M)-1]/q^2 = -1/q^2 + O(q^-4).
    #
    # Integramos o trecho finito e somamos analiticamente a cauda dominante
    # int_Q^inf -dq/q^2 = -1/Q. A cauda oscilatória restante é O(Q^-3).
    q_max = 1000.0 / min(r_e, r_m)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", IntegrationWarning)
        val_finite, err = quad(
            lambda q: integrand(q, r_e, r_m),
            0.0,
            q_max,
            epsabs=1e-10,
            epsrel=1e-10,
            limit=2000,
        )
    tail = -1.0 / q_max
    val = val_finite + tail
    tail_err_bound = 1.0 / (3.0 * r_e * r_m * q_max**3)
    return -(4.0 / pi) * val, (4.0 / pi) * (err + tail_err_bound)


def main() -> None:
    cases = [
        ("casca coincidente Q40", r_p, r_p, 4.0 * r_p / 3.0),
        ("teste rM 5% maior", r_p, 1.05 * r_p, None),
        ("teste rM 5% menor", r_p, 0.95 * r_p, None),
    ]

    text = [
        "# Saída — cálculo direto do raio de Zemach Q48",
        "",
        "Classificação: avaliação direta do modelo de fatores de forma de superfície Q40.",
        "",
        "Fórmula:",
        "",
        "$$",
        "r_Z=-\\frac4\\pi\\int_0^\\infty\\frac{dq}{q^2}",
        "\\left[\\frac{G_E(q)G_M(q)}{G_M(0)}-1\\right].",
        "$$",
        "",
        "| caso | r_E (fm) | r_M (fm) | r_Z numérico (fm) | erro quad | referência analítica |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for name, r_e, r_m, ref in cases:
        rz, err = zemach_numeric(r_e, r_m)
        ref_txt = "" if ref is None else f"{ref:.12f}"
        text.append(f"| {name} | {r_e:.12f} | {r_m:.12f} | {rz:.12f} | {err:.3e} | {ref_txt} |")

    text += [
        "",
        "Conclusão: o valor usado na hiperfina, $r_Z=4r_p/3$, é confirmado",
        "diretamente pela integral de fatores de forma quando $r_E=r_M=r_p$.",
        "Separar $r_M$ de $r_E$ é exatamente o próximo refinamento da Hessiana",
        "magnética superior do próton.",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()
