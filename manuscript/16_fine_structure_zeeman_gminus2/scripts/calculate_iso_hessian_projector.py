#!/usr/bin/env python3
"""GDQ — Chapter 16: isotropic projector of the electrical channel.

Classification:
    direct evaluation of derived quantity.

The script evaluates the factor

    P_iso = pi^-4 * <(n.u)^4>_{S^3} * (Tr_CS 1_3)^2

which appears when the mean physical Hessian of the Einstein ensemble is scalar
in the physical subspace of four directions. The calculation does not use the experimental
value of alpha.
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

    text = f"""# Output — isotropic projector of the Hessian

Classification: direct evaluation of derived quantity; does not use CODATA.

| quantity | value |
|---|---:|
| angular normalization $\\pi^{{-4}}$ | {angular_normalization:.15e} |
| Haar moment $\\langle(n\\cdot u)^4\\rangle_{{S^3}}$ | {hopf_haar_fourth_moment:.15e} |
| coherent Cartan-Schouten trace squared | {cartan_schouten_trace_squared:.15e} |
| calculated $\\mathcal P_{{\\rm iso}}$ | {p_iso:.15e} |
| $9/(8\\pi^4)$ | {p_iso_closed:.15e} |
| difference | {p_iso - p_iso_closed:.3e} |
| $\\alpha_E^{{\\rm mean}}$ | {alpha_mean:.15e} |
| $(\\alpha_E^{{\\rm mean}})^{{-1}}$ | {1.0 / alpha_mean:.12f} |
| $Z_Q^E=1/(4\\pi\\alpha_E^{{\\rm mean}})$ | {z_q:.12f} |

Interpretation: the mean Hessian cancels in the projective ratio due to Schur isotropy. The remaining factor is the angular/torsional contraction of the electrical channel.
"""

    assert abs(p_iso - p_iso_closed) < 1e-15
    out = Path(__file__).resolve().parent / "output_calculate_iso_hessian_projector.md"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
