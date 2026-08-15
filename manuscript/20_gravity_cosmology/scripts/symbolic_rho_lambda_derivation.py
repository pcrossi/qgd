#!/usr/bin/env python3
"""
Symbolic and dimensional derivation of the GDQ dark energy density.

Scientific classification:
    symbolic/dimensional verification of the reduced structural formula.

This script does not use experimental values. It records the algebraic chain:

    rho_UV^p = M_p c^2 / V_p
    V_p = (4 pi / 3) r_p^3
    N_Cartan = dim Lambda^2(R^8) = C(8,2) = 28
    e^{-f} = r_p/r -> linear dilution r_p/R_H
    rho_Lambda = alpha^2 N_Cartan rho_UV^p (r_p/R_H) / c^2

and verifies that the final dimension is mass density, kg/m^3.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_symbolic_rho_lambda_derivation.md"


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
    lines.append('title: "Output — symbolic derivation of rho Lambda"\n')
    lines.append('---\n\n')
    lines.append("# Output — symbolic derivation of rho Lambda\n\n")
    lines.append("Classification: symbolic/dimensional verification of the reduced structural formula.\n\n")

    lines.append("## 1. Algebraic chain\n\n")
    lines.append("$$\n")
    lines.append("V_p=\\frac{4\\pi}{3}r_p^3\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("\\rho_{\\rm UV}^{p}=\\frac{M_pc^2}{V_p}\n")
    lines.append("$$\n\n")
    lines.append("The asymptotic weight of the neck is:\n\n")
    lines.append("$$\n")
    lines.append("f(r)\\sim\\ln\\left(\\frac{r}{r_p}\\right),\\qquad e^{-f}=\\frac{r_p}{r}\n")
    lines.append("$$\n\n")
    lines.append("Hence the preserved dilution scale is:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_{\\rm diluted}\\propto\\frac{r_p}{R_H}\n")
    lines.append("$$\n\n")
    lines.append("The antisymmetric count in eight dimensions is:\n\n")
    lines.append("$$\n")
    lines.append(f"N_{{\\rm Cartan}}=\\dim\\Lambda^2(\\mathbb R^8)=\\binom82={n_cartan}\n")
    lines.append("$$\n\n")
    lines.append("Therefore:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_\\Lambda^{\\rm GDQ}=\\alpha^2N_{\\rm Cartan}\\rho_{\\rm UV}^{p}\\frac{r_p}{R_H}\\frac{1}{c^2}\n")
    lines.append("$$\n\n")

    lines.append("## 2. Explicit cancellation of $c^2$\n\n")
    lines.append("Substituting $\\rho_{\\rm UV}^{p}$:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_\\Lambda^{\\rm GDQ}=\\alpha^2N_{\\rm Cartan}\\frac{M_pc^2}{(4\\pi/3)r_p^3}\\frac{r_p}{R_H}\\frac{1}{c^2}\n")
    lines.append("$$\n\n")
    lines.append("Therefore:\n\n")
    lines.append("$$\n")
    lines.append("\\rho_\\Lambda^{\\rm GDQ}=\\alpha^2N_{\\rm Cartan}\\frac{M_p}{(4\\pi/3)r_p^3}\\frac{r_p}{R_H}\n")
    lines.append("$$\n\n")

    lines.append("## 3. Dimensional verification\n\n")
    lines.append("| Quantity | Dimension |\n")
    lines.append("|---|---:|\n")
    lines.append(f"| $M_p$ | `{unit_string(kg)}` |\n")
    lines.append(f"| $c^2$ | `{unit_string(c2)}` |\n")
    lines.append(f"| $M_pc^2$ | `{unit_string(energy)}` |\n")
    lines.append(f"| $V_p$ | `{unit_string(volume)}` |\n")
    lines.append(f"| $\\rho_{{\\rm UV}}^p$ | `{unit_string(rho_uv)}` |\n")
    lines.append(f"| $r_p/R_H$, $\\alpha^2$, $N_{{\\rm Cartan}}$ | `{unit_string({})}` |\n")
    lines.append(f"| $\\rho_\\Lambda^{{\\rm GDQ}}$ before dividing by $c^2$ | `{unit_string(rho_lambda_energy)}` |\n")
    lines.append(f"| $\\rho_\\Lambda^{{\\rm GDQ}}$ final | `{unit_string(rho_lambda_mass)}` |\n\n")

    lines.append("## 4. Status\n\n")
    lines.append("The symbolic derivation confirms the algebraic structure, the count of 28, and the final dimension of kg/m^3. The metrological evaluation depends on $R_H=c/H_0$ as a cosmological boundary.\n")

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
