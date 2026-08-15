#!/usr/bin/env python3
"""
GDQ — Chapter 17 / leading spectrum and baryonic stability.

Classification:
    direct evaluation of reduced stability formulas.

The script records:

1. surface moment of inertia:
       I_rot = 3 M_p r_p^2 / 10;
2. leading rotational scale:
       E_rot = 5 (hbar c)^2 / (M_p r_p^2);
3. qualitative test of proximity to Delta(1232);
4. topological stability of the proton as a sector with preserved Cauchy charge/residue
   integer preserved.
"""

from __future__ import annotations

import math
from pathlib import Path


def main() -> None:
    hbarc = 197.3269804  # MeV fm
    alpha = 1.0 / 137.035999177
    me = 0.51099895000
    mp_ratio = 6.0 * math.pi**5 + alpha * (3.0 * math.pi / 2.0 + 3.0 / (4.0 * math.pi**3))
    mp = mp_ratio * me
    r_p = 0.840778765432
    i_rot = 0.3 * mp * r_p * r_p
    e_rot = 5.0 * hbarc * hbarc / (mp * r_p * r_p)
    m_delta_pred = mp + e_rot
    m_delta_ref = 1232.0
    rel_delta = (m_delta_pred - m_delta_ref) / m_delta_ref

    lines = [
        "---",
        'title: "Output — baryon spectrum and stability"',
        "---",
        "",
        "# Output — baryon spectrum and stability",
        "",
        "## Reduced moment of inertia",
        "",
        "$$",
        "I_{\\rm rot}",
        "=",
        "\\frac12 M_p\\frac35r_p^2",
        "=",
        "\\frac{3}{10}M_pr_p^2.",
        "$$",
        "",
        "## Leading rotational scale",
        "",
        "$$",
        "E_{\\rm rot}",
        "=",
        "\\frac{5(\\hbar c)^2}{M_pr_p^2}.",
        "$$",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| reduced $M_p$ | `{mp:.9f}` MeV |",
        f"| $r_p$ | `{r_p:.12f}` fm |",
        f"| $I_{{\\rm rot}}$ | `{i_rot:.9f}` MeV fm$^2$ |",
        f"| $E_{{\\rm rot}}$ | `{e_rot:.9f}` MeV |",
        f"| $M_p+E_{{\\rm rot}}$ | `{m_delta_pred:.9f}` MeV |",
        f"| $\\Delta(1232)$ reference | `{m_delta_ref:.9f}` MeV |",
        f"| relative error | `{rel_delta:.12e}` |",
        "",
        "## Structural stability",
        "",
        "In the sector that preserves Cauchy charge, Noether flux, and topological class,",
        "the proton does not continuously decay to the vacuum. The neutron preserves baryon",
        "number, but possesses antiparallel torsional shear and therefore opens a",
        "dynamic beta decay channel.",
        "",
        "## Classification",
        "",
        "The rotational scale is a leading approximation. The complete spectrum of radial,",
        "torsional, and throat modes requires full diagonalization of the physical",
        "baryonic Hessian.",
        "",
    ]

    out = Path(__file__).with_name("output_baryon_stability_spectrum.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
