#!/usr/bin/env python3
"""
Objective:
    Self-contained verification script for `zeeman linear response` associated with chapter `16_fine_structure_zeeman_gminus2`.

QGD — Chapter 16 / linear Zeeman response.

Verifies the reduced form:

    E_pm = E0 ∓ gamma_eff (hbar/2) |B|
    F_pm = ± gamma_eff (hbar/2) grad |B|

The script uses reduced units hbar=1 and gamma_eff=1 to demonstrate the
sign structure. B and gradB are apparatus data.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_zeeman_linear_response.md"

    hbar = 1.0
    gamma_eff = 1.0
    e0 = 0.0
    b_abs = 0.25
    grad_b = 0.03

    e_plus = e0 - gamma_eff * 0.5 * hbar * b_abs
    e_minus = e0 + gamma_eff * 0.5 * hbar * b_abs
    f_plus = gamma_eff * 0.5 * hbar * grad_b
    f_minus = -gamma_eff * 0.5 * hbar * grad_b

    text = f"""# Output — linear Zeeman response

Classification: reduced symbolic-numerical test.

Reduced units: $\\hbar=1$, $\\gamma_{{\\rm eff}}=1$.

| quantity | value |
|---|---:|
| magnitude of B | {b_abs:.12f} |
| gradient of the magnitude of B | {grad_b:.12f} |
| E_+ | {e_plus:.12f} |
| E_- | {e_minus:.12f} |
| E_+-E_- | {e_plus-e_minus:.12f} |
| F_+ | {f_plus:.12f} |
| F_- | {f_minus:.12f} |

Interpretation: the two channels have opposing energies and forces because the apparatus
selects the two stable orientations of the circulation.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
