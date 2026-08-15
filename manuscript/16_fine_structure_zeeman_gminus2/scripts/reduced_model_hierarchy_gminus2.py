#!/usr/bin/env python3
"""GDQ — Reduced model Q39 -> Chapter 16.

Objective:
    Use the Q39 intrinsic leptonic hierarchy as a reduced background
    to test how much it explains, on its own, the upper residuals of g-2.

Classification:
    consistency test + inverse diagnostic.

This script is NOT a blind prediction of g-2. It separates:
    1. the universal leading term alpha/(2*pi), already structurally derived;
    2. the diagonal scalar susceptibility inherited from Q39;
    3. the remaining transverse source m_perp,l of the physical Hessian.

Expected conclusion:
    the leptonic hierarchy provides the background, but does not replace the
    calculation of the transverse operator H_C^{-1} m_perp.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV


@dataclass(frozen=True)
class Lepton:
    name: str
    symbol: str
    q39_role: str
    anomaly_obs: float | None
    sigma_anomaly: float | None
    source: str


LEPTONS = [
    Lepton(
        name="electron",
        symbol="e",
        q39_role="primary torsion",
        anomaly_obs=1.00115965218059 - 1.0,
        sigma_anomaly=1.3e-13,
        source="Fan et al. 2022/2023, g/2",
    ),
    Lepton(
        name="muon",
        symbol="mu",
        q39_role="transverse/bispatial torsion",
        anomaly_obs=116592059e-11,
        sigma_anomaly=22e-11,
        source="Muon g-2 world average 2023",
    ),
    Lepton(
        name="tau",
        symbol="tau",
        q39_role="three-dimensional saturation",
        anomaly_obs=None,
        sigma_anomaly=None,
        source="no metrological use in this test",
    ),
]


def r_mu_intrinsic(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0:
        raise ValueError("no real root for Q=2/3")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def main() -> None:
    a1 = ALPHA / (2.0 * math.pi)
    x2 = (ALPHA / math.pi) ** 2

    ratios = {
        "e": 1.0,
        "mu": r_mu_intrinsic(),
        "tau": r_tau_from_q(r_mu_intrinsic()),
    }
    chi_rel = {symbol: 1.0 / value for symbol, value in ratios.items()}

    # Diagnostic: if the upper residual scaled only with the diagonal scalar susceptibility
    # 1/R_l, calibrating on the electron, the muon/tau would follow this curve.
    # This tests whether the hierarchy alone replaces the transverse magnetic operator.
    # The answer should be negative.
    electron_residual = LEPTONS[0].anomaly_obs - a1

    lines: list[str] = []
    lines.append("# Output — Reduced model Q39→Chapter 16")
    lines.append("")
    lines.append("## Classification")
    lines.append("")
    lines.append(
        "Consistency test and inverse diagnostic. This calculation is not a "
        r"blind prediction of $g-2$."
    )
    lines.append("")
    lines.append("## Parameters used")
    lines.append("")
    lines.append(f"- `alpha_inv = {ALPHA_INV:.12f}`")
    lines.append(f"- `alpha = {ALPHA:.15e}`")
    lines.append(f"- `a1 = alpha/(2*pi) = {a1:.15e}`")
    lines.append(f"- `R_mu_Q39 = {ratios['mu']:.15e}`")
    lines.append(f"- `R_tau_Q39 = {ratios['tau']:.15e}`")
    lines.append("")
    lines.append("## Q39 hierarchy used as reduced background")
    lines.append("")
    lines.append("| lepton | Q39 role | R_l=M_l/M_e | chi_rel=1/R_l |")
    lines.append("|---|---|---:|---:|")
    for lep in LEPTONS:
        lines.append(
            f"| {lep.name} | {lep.q39_role} | {ratios[lep.symbol]:.15e} | "
            f"{chi_rel[lep.symbol]:.15e} |"
        )
    lines.append("")
    lines.append("## Observed upper residuals")
    lines.append("")
    lines.append(
        r"The residual is $a_{\rm obs}-\alpha/(2\pi)$. "
        "The aggregated coefficient is only diagnostic:"
    )
    lines.append("")
    lines.append("| lepton | a_obs | residual | aggregated_C2 = residual/(alpha/pi)^2 | source |")
    lines.append("|---|---:|---:|---:|---|")
    for lep in LEPTONS:
        if lep.anomaly_obs is None:
            lines.append(f"| {lep.name} | — | — | — | {lep.source} |")
            continue
        residual = lep.anomaly_obs - a1
        c2 = residual / x2
        lines.append(
            f"| {lep.name} | {lep.anomaly_obs:.15e} | "
            f"{residual:.15e} | {c2:.12f} | {lep.source} |"
        )
    lines.append("")
    lines.append("## Test: does the hierarchy alone explain the residual?")
    lines.append("")
    lines.append(
        "Hypothesis tested: the upper residual scales only with the diagonal "
        r"scalar susceptibility $\chi_\ell\propto1/R_\ell$, "
        "normalized on the electron."
    )
    lines.append("")
    lines.append("| lepton | residual predicted by chi_rel | observed residual | verdict |")
    lines.append("|---|---:|---:|---|")
    for lep in LEPTONS:
        pred = electron_residual * chi_rel[lep.symbol]
        if lep.anomaly_obs is None:
            lines.append(
                f"| {lep.name} | {pred:.15e} | — | no metrological comparison |"
            )
            continue
        obs = lep.anomaly_obs - a1
        ratio = pred / obs if obs != 0 else float("nan")
        verdict = (
            "reference calibration"
            if lep.symbol == "e"
            else f"failure by factor {ratio:.3e}"
        )
        lines.append(f"| {lep.name} | {pred:.15e} | {obs:.15e} | {verdict} |")
    lines.append("")
    lines.append("## Minimal inverse diagnostic")
    lines.append("")
    lines.append(
        r"If one writes $a_\ell-a_1=\mathcal R_\ell$, then the physical "
        r"transverse operator must produce exactly $\mathcal R_\ell$:"
    )
    lines.append("")
    lines.append("$$")
    lines.append(
        "\\mathcal R_\\ell="
        "\\frac{1}{\\gamma_{0,\\ell}}"
        "\\frac{\\langle c_\\ell,H_{C,\\ell}^{+}m_{\\perp,\\ell}\\rangle}"
        "{\\langle c_\\ell,H_{C,\\ell}^{+}c_\\ell\\rangle}"
        "-\\frac{\\alpha}{2\\pi}."
    )
    lines.append("$$")
    lines.append("")
    lines.append(
        "In the reduced diagonal model, the mass/hierarchy does not determine this "
        r"contraction. The missing information is $m_{\perp,\ell}$ and the physical "
        r"transverse block of $H_{C,\ell}$."
    )
    lines.append("")
    lines.append("## Conclusion")
    lines.append("")
    lines.append(
        "The Q39 hierarchy is necessary as a leptonic background, but is "
        r"insufficient to close $g-2$. The mass hierarchy cannot be "
        "used as a substitute for the Zeeman/anomaly calculation. O next physical "
        r"link is to construct $H_{C,\ell}$, $c_\ell$, and $m_{\perp,\ell}$ "
        "directly from the official Hessian on each leptonic background."
    )
    lines.append("")

    out = Path(__file__).with_name("output_reduced_model_hierarchy_gminus2.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
