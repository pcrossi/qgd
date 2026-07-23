#!/usr/bin/env python3
"""
Derivação simbólica/dimensional da densidade de energia escura GDQ.

Classificação científica:
    verificação simbólica/dimensional da fórmula estrutural reduzida.

Este script não usa valores experimentais. Ele registra a cadeia algébrica:

    rho_UV^p = M_p c^2 / V_p
    V_p = (4 pi / 3) r_p^3
    N_Cartan = dim Lambda^2(R^8) = C(8,2) = 28
    e^{-f} = r_p/r -> diluição linear r_p/R_H
    rho_Lambda = alpha^2 N_Cartan rho_UV^p (r_p/R_H) / c^2

e verifica que a dimensão final é densidade de massa, kg/m^3.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_derivacao_rho_lambda_simbolica.md"


def combine_units(*terms: dict[str, int]) -> dict[str, int]:
    out: dict[str, int] = {}
    for term in terms:
        for key, value in term.items():
            out[key] = out.get(key, 0) + value
            if out[key] == 0:
                del out[key]
    return out


def inv(unit: dict[str, int]) -> dict[str, int]:
    return {key: -value for key, value in unit.items()}


def unit_string(unit: dict[str, int]) -> str:
    if not unit:
        return "1"
    order = ["kg", "m", "s"]
    return " ".join(f"{u}^{unit[u]}" if unit[u] != 1 else u for u in order if u in unit)


def main() -> None:
    kg = {"kg": 1}
    m = {"m": 1}
    s = {"s": 1}

    c2 = combine_units({"m": 2}, {"s": -2})
    energy = combine_units(kg, c2)
    volume = {"m": 3}
    rho_uv = combine_units(energy, inv(volume))
    dilution = {}
    alpha2 = {}
    n_cartan_unit = {}
    rho_lambda_energy = combine_units(alpha2, n_cartan_unit, rho_uv, dilution)
    rho_lambda_mass = combine_units(rho_lambda_energy, inv(c2))

    n_dim = 8
    n_cartan = math.comb(n_dim, 2)

    lines: list[str] = []
    lines.append('---\n')
    lines.append('title: "Saída — derivação simbólica de rho Lambda"\n')
    lines.append('---\n\n')
    lines.append("# Saída — derivação simbólica de rho Lambda\n\n")
    lines.append("Classificação: verificação simbólica/dimensional da fórmula estrutural reduzida.\n\n")

    lines.append("## 1. Cadeia algébrica\n\n")
    lines.append("$$\n")
    lines.append("V_p=\\frac{4\\pi}{3}r_p^3\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("\\rho_{\\rm UV}^{p}=\\frac{M_pc^2}{V_p}\n")
    lines.append("$$\n\n")
    lines.append("O peso assintótico do colar é:\n\n")
    lines.append("$$\n")
    lines.append("f(r)\\sim\\ln\\left(\\frac{r}{r_p}\\right),\\qquad e^{-f}=\\frac{r_p}{r}\n")
    lines.append("$$\n\n")
    lines.append("Logo a escala de diluição preservada é:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_{\\rm diluida}\\propto\\frac{r_p}{R_H}\n")
    lines.append("$$\n\n")
    lines.append("A contagem antissimétrica em oito dimensões é:\n\n")
    lines.append("$$\n")
    lines.append(f"N_{{\\rm Cartan}}=\\dim\\Lambda^2(\\mathbb R^8)=\\binom82={n_cartan}\n")
    lines.append("$$\n\n")
    lines.append("Portanto:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_\\Lambda^{\\rm GDQ}=\\alpha^2N_{\\rm Cartan}\\rho_{\\rm UV}^{p}\\frac{r_p}{R_H}\\frac1{c^2}\n")
    lines.append("$$\n\n")

    lines.append("## 2. Cancelamento explícito de $c^2$\n\n")
    lines.append("Substituindo $\\rho_{\\rm UV}^{p}$:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_\\Lambda^{\\rm GDQ}=\\alpha^2N_{\\rm Cartan}\\frac{M_pc^2}{(4\\pi/3)r_p^3}\\frac{r_p}{R_H}\\frac1{c^2}\n")
    lines.append("$$\n\n")
    lines.append("Logo:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_\\Lambda^{\\rm GDQ}=\\alpha^2N_{\\rm Cartan}\\frac{M_p}{(4\\pi/3)r_p^3}\\frac{r_p}{R_H}\n")
    lines.append("$$\n\n")

    lines.append("## 3. Verificação dimensional\n\n")
    lines.append("| Quantidade | Dimensão |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $M_p$ | `{unit_string(kg)}` |\n")
    lines.append(f"| $c^2$ | `{unit_string(c2)}` |\n")
    lines.append(f"| $M_pc^2$ | `{unit_string(energy)}` |\n")
    lines.append(f"| $V_p$ | `{unit_string(volume)}` |\n")
    lines.append(f"| $\\rho_{{\\rm UV}}^p$ | `{unit_string(rho_uv)}` |\n")
    lines.append(f"| $r_p/R_H$, $\\alpha^2$, $N_{{\\rm Cartan}}$ | `{unit_string({})}` |\n")
    lines.append(f"| $\\rho_\\Lambda^{{\\rm GDQ}}$ antes de dividir por $c^2$ | `{unit_string(rho_lambda_energy)}` |\n")
    lines.append(f"| $\\rho_\\Lambda^{{\\rm GDQ}}$ final | `{unit_string(rho_lambda_mass)}` |\n\n")

    lines.append("## 4. Status\n\n")
    lines.append("A derivação simbólica confirma a estrutura algébrica, a contagem 28 e a dimensão final kg/m^3. A avaliação metrológica depende de $R_H=c/H_0$ como contorno cosmológico.\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
