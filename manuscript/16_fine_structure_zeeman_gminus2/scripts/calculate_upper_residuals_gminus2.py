#!/usr/bin/env python3
"""Chapter 16 — upper residuals of g-2.

Calculates what remains after the leading QGD term:

    a1 = alpha/(2*pi)

for electron and muon. These residuals are NOT derived by QGD in this script.
They are metrological diagnostics: they indicate the size that the contraction
H_C^{-1} m_perp must produce in upper orders.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


ALPHA_INV_CODATA_2022 = 137.035999177


@dataclass(frozen=True)
class Case:
    name: str
    anomaly: float
    uncertainty: float | None
    source: str


def evaluate(case: Case, alpha: float) -> dict[str, float | str | None]:
    x = alpha / math.pi
    a1 = x / 2.0
    residual = case.anomaly - a1
    c2_aggregate = residual / (x * x)
    c3_aggregate = residual / (x * x * x)
    g = 2.0 * (1.0 + case.anomaly)
    g_leader = 2.0 * (1.0 + a1)
    return {
        "name": case.name,
        "a_obs": case.anomaly,
        "sigma": case.uncertainty,
        "a1": a1,
        "residual_a": residual,
        "g_obs": g,
        "g_leader": g_leader,
        "residual_g": 2.0 * residual,
        "c2_aggregate": c2_aggregate,
        "c3_aggregate": c3_aggregate,
        "source": case.source,
    }


def fmt(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{x:.15e}"


def main() -> None:
    alpha = 1.0 / ALPHA_INV_CODATA_2022

    # Electron: Fan et al. quote -mu/mu_B = g/2.
    # The anomaly magnitude is g/2 - 1.
    electron = Case(
        name="electron Fan 2022",
        anomaly=1.00115965218059 - 1.0,
        uncertainty=0.00000000000013,
        source="Fan et al. arXiv:2209.13084",
    )

    # Muon: 2023 Fermilab + BNL world average from arXiv:2308.06230.
    muon_2023 = Case(
        name="muon world avg 2023",
        anomaly=116_592_059e-11,
        uncertainty=22e-11,
        source="Aguillard et al. arXiv:2308.06230",
    )

    rows = [evaluate(electron, alpha), evaluate(muon_2023, alpha)]

    lines = [
        "# Chapter 16 — upper residuals after the leading term",
        "",
        "Classification: external metrological comparison and size diagnostic. It is not a derivation of the upper QGD terms.",
        "",
        f"- alpha^-1 used: `{ALPHA_INV_CODATA_2022:.12f}`",
        f"- x = alpha/pi: `{alpha / math.pi:.15e}`",
        f"- leading term: `a1 = alpha/(2*pi) = {alpha/(2*math.pi):.15e}`",
        "",
        "| case | a_obs | sigma | a_obs-a1 | g_obs | g_leader | g_obs-g_leader | aggregated C2 | source |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        sigma_text = fmt(r["sigma"] if isinstance(r["sigma"], float) else None)
        r_fmt = dict(r)
        r_fmt["sigma_text"] = sigma_text
        lines.append(
            "| {name} | {a_obs:.15e} | {sigma_text} | {residual_a:.15e} | "
            "{g_obs:.15f} | {g_leader:.15f} | {residual_g:.15e} | "
            "{c2_aggregate:.12f} | {source} |".format(
                **r_fmt,
            )
        )

    lines.extend(
        [
            "",
            "## QGD Reading",
            "",
            "For each lepton, the residual must be produced by:",
            "",
            "$$",
            "\\Delta\\gamma_{\\rm geom}^{\\rm upper}",
            "=",
            "\\frac{\\langle c,H_C^{-1}m_\\perp\\rangle}",
            "{\\langle c,H_C^{-1}c\\rangle}",
            "-\\gamma_0\\frac{\\alpha}{2\\pi}.",
            "$$",
            "",
            "The `aggregated C2` is only the effective coefficient that would appear if the entire",
            "residual were put into `(alpha/pi)^2`. It is not a derivation.",
            "",
            "For the electron, the aggregated coefficient is of the order of negative unity,",
            "as expected for a small upper correction. For the muon, the aggregated",
            "coefficient changes significantly, showing that the heavy leptonic background",
            "cannot be replaced by the electron background.",
            "",
        ]
    )

    out = Path(__file__).with_name("output_calculate_upper_residuals_gminus2.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
