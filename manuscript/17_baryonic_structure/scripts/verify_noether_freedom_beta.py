#!/usr/bin/env python3
"""GDQ — Chapter 17 / Remaining transverse freedom of Noether."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def spin_norm(c_s: complex, c_t: complex) -> float:
    return 2.0 * abs(c_s) ** 2 + 6.0 * abs(c_t) ** 2


def main() -> None:
    c_s = 0.8 - 0.3j
    c_t = -0.2 + 0.5j
    lam = 1.7 * np.exp(0.4j)
    before = spin_norm(c_s, c_t)
    after = spin_norm(lam * c_s, lam * c_t)
    predicted = abs(lam) ** 2
    residual = abs(after / before - predicted)
    charges = np.array([0, 1, -1, 0])

    lines = [
        "# Output — residual Noether freedom in beta decay",
        "",
        "Classification: algebraic consistency test; not a physical model.",
        "",
        f"- sum of external charges: `{charges.sum()}`",
        f"- predicted rate factor by complex scaling: `{predicted:.12f}`",
        f"- calculated rate factor: `{after / before:.12f}`",
        f"- residue: `{residual:.3e}`",
        "",
        "Conclusion: charge conservation and isotropy do not fix the transverse normalization of the coefficients.",
        "",
    ]
    out = Path(__file__).with_name("output_verify_noether_freedom_beta.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
