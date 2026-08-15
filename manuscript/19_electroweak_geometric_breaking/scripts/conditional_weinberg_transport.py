#!/usr/bin/env python3
"""
GDQ — Chapter 19 / Spectral transport of the Weinberg angle

Objective:
    Record the reduced algebraic and numerical calculations of the electroweak
    transport path: condition Z_W/Z_Y=10/21, spectral crossing scale, and W/Z
    comparison.

Classification:
    Reduced/conditional diagnostic. The script does not use m_W or m_Z to construct
    the parameters; these values enter only at the end for comparison.

Output:
    scripts/output_conditional_weinberg_transport.md
"""

from pathlib import Path
import math


def masses(v: float, alpha_inv: float, sin2: float) -> tuple[float, float, float, float]:
    alpha = 1.0 / alpha_inv
    e = math.sqrt(4.0 * math.pi * alpha)
    s = math.sqrt(sin2)
    c = math.sqrt(1.0 - sin2)
    g = e / s
    gp = e / c
    mw = 0.5 * g * v
    mz = 0.5 * math.sqrt(g * g + gp * gp) * v
    return g, gp, mw, mz


def main() -> None:
    i2 = 2.0
    iy = 10.0 / 3.0
    ratio_match = i2 / iy
    sin2_match = ratio_match / (1.0 + ratio_match)

    sin2_operational = 2.0 / 9.0
    ratio_operational = sin2_operational / (1.0 - sin2_operational)
    z_w_over_z_y = ratio_operational / ratio_match

    s_star = 5.9090386e6
    lambda0 = 126354.3162
    q_over_lambda0 = 1.0 / math.sqrt(s_star)
    q_star = lambda0 * q_over_lambda0

    v = 246.111195996
    alpha_inv_cond = 132.457669
    mw_ref = 80.379
    mz_ref = 91.1876
    g, gp, mw, mz = masses(v, alpha_inv_cond, sin2_operational)
    err_w = (mw - mw_ref) / mw_ref
    err_z = (mz - mz_ref) / mz_ref

    lines = [
        "# Output — conditional Weinberg transport",
        "",
        "Classification: reduced/conditional diagnostic; posterior comparison.",
        "",
        "| quantity | value |",
        "|---|---:|",
        f"| I2 | {i2:.12f} |",
        f"| IY | {iy:.12f} |",
        f"| g_prime^2/g^2 at common point | {ratio_match:.12f} |",
        f"| sin2 common point | {sin2_match:.12f} |",
        f"| sin2 operational | {sin2_operational:.12f} |",
        f"| Z_W/Z_Y required | {z_w_over_z_y:.12f} |",
        f"| s_star | {s_star:.6e} |",
        f"| Q_star/Lambda0 | {q_over_lambda0:.12e} |",
        f"| Lambda0 GeV | {lambda0:.6f} |",
        f"| Q_star GeV | {q_star:.6f} |",
        f"| conditional alpha_EW_inv | {alpha_inv_cond:.6f} |",
        f"| g | {g:.12f} |",
        f"| g_prime | {gp:.12f} |",
        f"| m_W GeV | {mw:.6f} |",
        f"| W error | {err_w:.6%} |",
        f"| m_Z GeV | {mz:.6f} |",
        f"| Z error | {err_z:.6%} |",
        "",
        "Interpretation: the conditional 2/9 + alpha_EW route approximates W/Z; the remaining strong calculation is to derive Z_W/Z_Y and alpha_EW from the global boundary Hessian.",
    ]

    out = Path(__file__).with_name("output_conditional_weinberg_transport.md")
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
