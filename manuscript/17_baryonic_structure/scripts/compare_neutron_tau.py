#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `compare_neutron_tau` associated with chapter `17_baryonic_structure`.

GDQ — Chapter 17 / neutron lifetime.

Calculates:

    tau_n = (32/15) alpha^-11 hbar/(m_e c^2)

using hbar in GeV*s and m_e c^2 in GeV.

Classification: phenomenological comparison of the reduced total rate.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_compare_neutron_tau.md"

    alpha_inv = 137.035999177
    hbar_gev_s = 6.582119569e-25
    me_gev = 0.00051099895000
    tau = (32.0 / 15.0) * (alpha_inv**11) * hbar_gev_s / me_gev
    half_life = tau * 0.6931471805599453
    ref = 878.3
    diff = tau - ref
    rel = diff / ref

    text = f"""# Output — neutron lifetime

Classification: phenomenological comparison of the reduced total rate.

| quantity | value |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| tau_n GDQ s | {tau:.12f} |
| T_1/2 GDQ s | {half_life:.12f} |
| tau_ref s | {ref:.12f} |
| difference s | {diff:.12f} |
| relative difference | {rel:.12e} |

Interpretation: the reduced total rate lies at the $10^{{-3}}$ level of the reference.
Differential shape, angular correlations, and recoil remain extensions.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
