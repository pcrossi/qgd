#!/usr/bin/env python3
"""
GDQ — Chapter 15 / stability criterion for warped/mixed backgrounds.

Classification:
    consistency test of the Schur complement.

Calculates:

    m_perp^2 = C_gamma*tau/R_max^2 - sum(c_i a_i^2),
    j_mix = sum(b_i a_i),
    Delta_Schur = j_mix^2 / m_perp^2.

The default values are normalized and illustrative. They do not use experimental
data and do not close real warped/mixed backgrounds; they display the criterion
that must be applied when such a background is obtained.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


@dataclass(frozen=True)
class MixedInput:
    a_warp: float
    a_dilaton: float
    a_torsion: float
    eps_metric: float
    lambda_b_gap: float = 1.0
    c_gamma: float = 1.0
    tau: float = 1.0
    r_max: float = 1.0
    c_warp: float = 1.0
    c_dilaton: float = 1.0
    c_torsion: float = 1.0
    c_metric: float = 1.0
    b_warp: float = 1.0
    b_dilaton: float = 1.0
    b_torsion: float = 1.0
    b_metric: float = 1.0


def evaluate(inp: MixedInput) -> dict[str, float | str]:
    if inp.lambda_b_gap <= 0:
        raise ValueError("lambda_b_gap must be positive")
    if inp.c_gamma <= 0 or inp.tau <= 0 or inp.r_max <= 0:
        raise ValueError("c_gamma, tau and r_max must be positive")

    loss = (
        inp.c_warp * inp.a_warp**2
        + inp.c_dilaton * inp.a_dilaton**2
        + inp.c_torsion * inp.a_torsion**2
        + inp.c_metric * inp.eps_metric**2
    )
    m_perp2 = inp.c_gamma * inp.tau / (inp.r_max**2) - loss
    j_mix = (
        inp.b_warp * inp.a_warp
        + inp.b_dilaton * inp.a_dilaton
        + inp.b_torsion * inp.a_torsion
        + inp.b_metric * inp.eps_metric
    )

    if m_perp2 <= 0:
        return {
            "m_perp2": m_perp2,
            "j_mix": j_mix,
            "schur": math.inf,
            "ratio": math.inf,
            "status": "non-coercive",
        }

    schur_value = (j_mix * j_mix) / m_perp2
    ratio = schur_value / inp.lambda_b_gap
    if schur_value < inp.lambda_b_gap:
        status = "subcritical"
    elif math.isclose(schur_value, inp.lambda_b_gap, rel_tol=1e-12, abs_tol=1e-12):
        status = "critical"
    else:
        status = "supercritical"
    return {
        "m_perp2": m_perp2,
        "j_mix": j_mix,
        "schur": schur_value,
        "ratio": ratio,
        "status": status,
    }


def one_channel_threshold(lambda_b_gap: float) -> float:
    if lambda_b_gap <= 0:
        raise ValueError("lambda_b_gap must be positive")
    return math.sqrt(lambda_b_gap / (1.0 + lambda_b_gap))


def main() -> None:
    scenarios = [
        ("product", MixedInput(0.0, 0.0, 0.0, 0.0)),
        ("weak_one_channel_0p1", MixedInput(0.1, 0.0, 0.0, 0.0)),
        ("four_channels_0p1", MixedInput(0.1, 0.1, 0.1, 0.1)),
        ("one_channel_critical_lambda1", MixedInput(one_channel_threshold(1.0), 0.0, 0.0, 0.0)),
        ("one_channel_supercritical_0p8", MixedInput(0.8, 0.0, 0.0, 0.0)),
    ]

    lines = [
        "---",
        'title: "Output — warped/mixed criterion"',
        "---",
        "",
        "# Output — warped/mixed criterion",
        "",
        "## Formulas",
        "",
        "$$",
        "m_\\perp^2",
        "=",
        "C_\\gamma\\tau R_{\\max}^{-2}",
        "-",
        "\\sum_i c_i a_i^2.",
        "$$",
        "",
        "$$",
        "j_{\\rm mix}=\\sum_i b_i a_i.",
        "$$",
        "",
        "$$",
        "\\Delta_{\\rm Schur}",
        "=",
        "\\frac{j_{\\rm mix}^2}{m_\\perp^2}.",
        "$$",
        "",
        "Stable/subcritical if:",
        "",
        "$$",
        "\\Delta_{\\rm Schur}<\\lambda_B^{\\rm gap}.",
        "$$",
        "",
        "## Normalized Scenarios",
        "",
        "| scenario | $m_\\perp^2$ | $j_{\\rm mix}$ | $\\Delta_{\\rm Schur}$ | ratio/gap | status |",
        "|---|---:|---:|---:|---:|---|",
    ]

    for name, inp in scenarios:
        out = evaluate(inp)
        lines.append(
            f"| {name} | {out['m_perp2']:.12g} | {out['j_mix']:.12g} | "
            f"{out['schur']:.12g} | {out['ratio']:.12g} | {out['status']} |"
        )

    lines.extend(
        [
            "",
            "## One-channel Threshold",
            "",
            "For a single active mixed channel with $\\lambda_B^{\\rm gap}=1$:",
            "",
            "$$",
            "a_{\\rm crit}=\\frac1{\\sqrt2}\\simeq0.707106781187.",
            "$$",
            "",
            "Below this value, the warped/mixed mixture does not alter the critical index.",
            "Above it, the background may generate an additional mode, which must be",
            "classified as a resonance, boundary state, or composite state",
            "until proof of primitive charge and asymptotic stability.",
            "",
        ]
    )

    out = Path(__file__).with_name("output_warped_mixed_criterion.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
