#!/usr/bin/env python3
"""
GDQ — Chapter 19 / editorial-dimensional verification.

Objective:
    Demonstrate in a self-contained way the difference between:

        125 GeV^2

    and:

        (125 GeV)^2.

Classification:
    editorial symbolic/dimensional test.

This verification is not a physical prediction and does not alter the official
action. It only protects the writing of the manuscript against ambiguity between:

    1. linear number multiplied by a quadratic unit;
    2. square of a linear mass scale.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_verify_powers_units.md"

    mass_h_gev = 125.0
    linear_times_unit_squared = mass_h_gev
    squared_mass_value = mass_h_gev**2

    delta_m2_mev2 = 0.68
    wrongly_squared_delta = delta_m2_mev2**2

    text = f"""---
title: "Output — powers and units"
---

# Output — powers and units

Classification: editorial symbolic/dimensional test.

## Linear mass squared

| Writing | numerical value in the quadratic unit |
|---|---:|
| $125\\,{{\\rm GeV}}^2$ | `{linear_times_unit_squared:.6f}` GeV² |
| $(125\\,{{\\rm GeV}})^2$ | `{squared_mass_value:.6f}` GeV² |

Ratio between the two readings:

$$
\\frac{{(125\\,{{\\rm GeV}})^2}}{{125\\,{{\\rm GeV}}^2}}
=
{squared_mass_value / linear_times_unit_squared:.6f}.
$$

Therefore, if the physical meaning is Higgs mass squared, the safe writing is:

$$
M_H^2\\simeq(125\\,{{\\rm GeV}})^2.
$$

## Already calculated quadratic value

If a calculation directly yields:

$$
\\Delta M_H^2\\simeq0.68\\,{{\\rm MeV}}^2,
$$

then the number `0.68` is already the value of the quadratic quantity. Writing
$(0.68\\,{{\\rm MeV}})^2$ would change the value to:

$$
{wrongly_squared_delta:.6f}\\,{{\\rm MeV}}^2.
$$

## Conclusion

- Use $(M\\,{{\\rm GeV}})^2$ when the linear number must also be squared.
- Use $X\\,{{\\rm GeV}}^2$ when $X$ is already the value of a quadratic quantity.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
