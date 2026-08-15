#!/usr/bin/env python3
"""Electronic scale by beta endpoint.

Classification:
    metrological determination / reduced analytical consequence.

The script shows that, once derived:

    delta_B = ln(2*pi^2) * 3*sqrt(2)/5,

the beta endpoint:

    Q_beta = M_n - M_p - M_e

implies:

    Q_beta = (delta_B - 1) M_e c^2

and therefore:

    M_e c^2 = Q_beta/(delta_B - 1).

The endpoint Q_beta is a metrological boundary condition datum. It is not used
to fit delta_B.
"""

from __future__ import annotations

import math
from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_electronic_scale_beta.md"


def main() -> None:
    delta_b = math.log(2.0 * math.pi**2) * (3.0 * math.sqrt(2.0) / 5.0)

    q_beta_mev = 0.782333559310
    me_ref_mev = 0.51099895000
    me_beta_mev = q_beta_mev / (delta_b - 1.0)
    abs_err = me_beta_mev - me_ref_mev
    rel_err = abs_err / me_ref_mev

    # Alternative inversion by total reduced lifetime, less precise because it
    # depends on the total rate closure and not just the kinematic endpoint.
    alpha_inv = 137.035999177
    hbar_gev_s = 6.582119569e-25
    tau_ref_s = 878.3
    me_tau_gev = (32.0 / 15.0) * (alpha_inv**11) * hbar_gev_s / tau_ref_s
    me_tau_mev = 1000.0 * me_tau_gev
    rel_tau = (me_tau_mev - me_ref_mev) / me_ref_mev

    text = f"""# Output — electronic scale by beta

Classification: metrological determination / reduced analytical consequence.

## Formula

$$
Q_\\beta=(\\delta_B-1)M_ec^2.
$$

Hence:

$$
M_ec^2=\\frac{{Q_\\beta}}{{\\delta_B-1}}.
$$

## Evaluation by endpoint

| quantity | value |
|---|---:|
| delta_B | {delta_b:.12f} |
| Q_beta MeV | {q_beta_mev:.12f} |
| M_e c^2 by beta MeV | {me_beta_mev:.12f} |
| M_e c^2 reference MeV | {me_ref_mev:.12f} |
| absolute error MeV | {abs_err:.12e} |
| relative error | {rel_err:.12e} |

## Alternative inversion by lifetime

| quantity | value |
|---|---:|
| tau_n reference s | {tau_ref_s:.12f} |
| M_e c^2 by tau_n MeV | {me_tau_mev:.12f} |
| relative error by tau_n | {rel_tau:.12e} |

## Verdict

The route by beta endpoint provides a metrological determination of the scale
electronic with relative error of order $10^{{-4}}$. The route by lifetime is
less precise at the current reduced stage, as it carries the approximations of
the total rate.
"""

    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
