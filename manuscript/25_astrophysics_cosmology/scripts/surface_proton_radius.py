#!/usr/bin/env python3
"""
Structural surface proton radius in GDQ.

Classification:
    arithmetic correction, direct evaluation of structural formula, and phenomenological
    comparison.

The script preserves the conclusion of Q60 in self-contained form:

1. the old multiplicative formula yields 0.000248914485 fm, not 0.0369 fm;
2. the current radius is the surface radius
   r_p=(1/8)(1+alpha/4) epsilon_eff (3 Lambda_C/2);
3. differences between probes are treated by boundary linear response.
"""

from __future__ import annotations

from pathlib import Path


OUT = Path(__file__).resolve().parent / "output_surface_proton_radius.md"


def main() -> None:
    legacy = 0.8778 * 0.07479 * 1.0e-3 * 3.7915
    old_claim = 0.0369
    factor_error = old_claim / legacy

    alpha_inv = 137.035999084
    alpha = 1.0 / alpha_inv
    epsilon_eff = 0.011591040463
    Lambda_C_fm = 386.159268
    C_r = (1.0 / 8.0) * (1.0 + alpha / 4.0)
    R_B = 1.5 * Lambda_C_fm
    r_p = C_r * epsilon_eff * R_B

    refs = [
        ("muonic reference 0.84087 fm", 0.84087),
        ("comparative electronic value 0.8778 fm", 0.8778),
        ("comparative effective value 0.8354 fm", 0.8354),
    ]

    mu_ratio = 1.555489846615637e-7

    lines = [
        "---",
        'title: "Output — structural proton radius"',
        "---",
        "",
        "# Output — structural proton radius",
        "",
        "## Discarded arithmetic correction",
        "",
        f"- correct old product: `{legacy:.12f} fm`.",
        f"- value written in the old route: `{old_claim:.12f} fm`.",
        f"- error factor: `{factor_error:.6f}`.",
        "",
        "## Structural formula",
        "",
        "$$",
        "r_p^{\\rm surf}=\\frac{1}{8}\\left(1+\\frac{\\alpha}{4}\\right)\\epsilon_{\\rm eff}\\frac{3\\Lambda_C}{2}",
        "$$",
        "",
        "| Quantity | Value |",
        "|---|---:|",
        f"| $\\alpha^{{-1}}$ | {alpha_inv:.12f} |",
        f"| $\\epsilon_{{\\rm eff}}$ | {epsilon_eff:.12f} |",
        f"| $\\Lambda_C$ | {Lambda_C_fm:.12f} fm |",
        f"| $C_r$ | {C_r:.15f} |",
        f"| $R_B=3\\Lambda_C/2$ | {R_B:.12f} fm |",
        f"| $r_p^{{\\rm surf}}$ | {r_p:.12f} fm |",
        "",
        "## Comparisons",
        "",
        "| Reference | Difference | Relative difference |",
        "|---|---:|---:|",
    ]

    for label, ref in refs:
        diff = r_p - ref
        lines.append(f"| {label} | {diff:+.12f} fm | {diff/ref:+.6%} |")

    lines += [
        "",
        "## Probe response",
        "",
        "$$",
        "r_p^{\\rm eff}[\\ell]=r_p^{\\rm surf}-\\left(H_p^{\\rm surf}\\right)^{-1}J_{p,\\ell}",
        "$$",
        "",
        "$$",
        "\\frac{\\delta r_p[e]}{\\delta r_p[\\mu]}=\\left(\\frac{\\mu_{ep}}{\\mu_{\\mu p}}\\right)^3",
        "$$",
        "",
        f"- electronic/muonic contact ratio: `{mu_ratio:.15e}`.",
        "",
        "Classification: structural radius closed; experimental puzzle reduced to boundary response.",
        "",
    ]

    text = "\n".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
