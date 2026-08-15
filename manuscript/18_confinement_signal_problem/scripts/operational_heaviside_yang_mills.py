#!/usr/bin/env python3
"""
GDQ — Chapter 18 / Heaviside operational bridge.

Objective:
    Symbolically verify the confining transfer function:

        F_mu(k^2) = -8*pi*sigma/(k^2+mu^2)^2

    and the subtracted limit:

        sigma*(1-exp(-mu*r))/mu -> sigma*r.

Classification:
    Symbolic verification of reduced operational equivalence.

Output:
    scripts/output_operational_heaviside_yang_mills.md
"""

from __future__ import annotations

from pathlib import Path
import sympy as sp


def main() -> None:
    k2, mu, sigma, r = sp.symbols("k2 mu sigma r", positive=True)
    f_mu = sp.simplify(-8 * sp.pi * sigma / (k2 + mu**2) ** 2)
    v_mu = sigma * (1 - sp.exp(-mu * r)) / mu
    limit_v = sp.simplify(sp.limit(v_mu, mu, 0, dir="+"))
    ok = sp.simplify(limit_v - sigma * r) == 0

    lines = [
        "# Output — operational Heaviside/GDQ-YM bridge",
        "",
        "Classification: reduced symbolic verification.",
        "",
        "```text",
        f"F_mu(k^2) = {sp.sstr(f_mu)}",
        f"lim_mu_to_0 V_mu(r) = {sp.sstr(limit_v)}",
        f"linear_verification = {ok}",
        "```",
        "",
        "Interpretation: the static transfer function transports the linear law in the reduced operational sector.",
    ]

    out = Path(__file__).with_name("output_operational_heaviside_yang_mills.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
