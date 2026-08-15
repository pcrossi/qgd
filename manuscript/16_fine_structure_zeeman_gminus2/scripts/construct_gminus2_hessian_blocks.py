#!/usr/bin/env python3
"""Chapter 16 — operational block builder of H_C, c, m_perp.

Generates two types of block:

1. leading:
   H = [[1, -1], [-1, 2*pi/alpha]]
   c = [1, 0]
   m_perp = [0, 1]

   This block implements the derived identity
   <c,H^+m>/<c,H^+c> = alpha/(2*pi).

2. upper_required:
   adds an extra transverse channel and chooses the amplitude of this channel to
   reproduce the observed residual. It is an inverse diagnostic, not a prediction.

The script saves the NPZs and a Markdown report.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
A1 = ALPHA / (2.0 * math.pi)
K1 = 2.0 * math.pi / ALPHA


@dataclass(frozen=True)
class Case:
    symbol: str
    name: str
    role_q39: str
    ratio_q39: float
    anomaly_obs: float | None
    source: str


CASES = [
    Case("e", "electron", "primary torsion", 1.0, 1.00115965218059 - 1.0, "Fan et al. 2022/2023"),
    Case("mu", "muon", "transverse/bispatial torsion", 0.0, 116592059e-11, "Muon g-2 world average 2023"),
    Case("tau", "tau", "three-dimensional saturation", 0.0, None, "no metrological target used"),
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
    if disc < 0.0:
        raise ValueError("no real root for Q=2/3")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def cases_with_ratios() -> list[Case]:
    r_mu = r_mu_intrinsic()
    return [
        CASES[0],
        Case("mu", "muon", "transverse/bispatial torsion", r_mu, 116592059e-11, "Muon g-2 world average 2023"),
        Case("tau", "tau", "three-dimensional saturation", r_tau_from_q(r_mu), None, "no metrological target used"),
    ]


def evaluate(H: np.ndarray, c: np.ndarray, m_perp: np.ndarray, gamma0: float = 1.0) -> dict[str, float]:
    Hh = 0.5 * (H + H.T)
    vals, vecs = np.linalg.eigh(Hh)
    inv = 1.0 / vals
    Hinv = (vecs * inv) @ vecs.T
    den = float(c @ (Hinv @ c))
    num = float(c @ (Hinv @ m_perp))
    a = num / (den * gamma0)
    return {
        "eig_min": float(vals[0]),
        "eig_max": float(vals[-1]),
        "den": den,
        "num": num,
        "a_geom": a,
        "g_total": 2.0 * (1.0 + a),
    }


def leading_block() -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    H = np.array([[1.0, -1.0], [-1.0, K1]], dtype=float)
    c = np.array([1.0, 0.0], dtype=float)
    m = np.array([0.0, 1.0], dtype=float)
    return H, c, m


def required_block(target_a: float, k2: float, j2: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, float]:
    """Constructs 3x3 block and solves mu2 amplitude to reach target_a."""
    H = np.array(
        [
            [1.0, -1.0, -j2],
            [-1.0, K1, 0.0],
            [-j2, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0], dtype=float)

    # Linear response in mu2: a(mu2) = a(mu2=0) + slope * mu2.
    m0 = np.array([0.0, 1.0, 0.0], dtype=float)
    m1 = np.array([0.0, 1.0, 1.0], dtype=float)
    a0 = evaluate(H, c, m0)["a_geom"]
    a1 = evaluate(H, c, m1)["a_geom"]
    slope = a1 - a0
    if abs(slope) < 1e-30:
        raise ValueError("Upper channel decoupled: zero slope.")
    mu2 = (target_a - a0) / slope
    m = np.array([0.0, 1.0, mu2], dtype=float)
    return H, c, m, mu2


def save_npz(path: Path, H: np.ndarray, c: np.ndarray, m: np.ndarray) -> None:
    np.savez(path, H=H, c=c, m_perp=m, gamma0=np.array([1.0]))


def main() -> None:
    base = Path(__file__).resolve().parent
    cases = cases_with_ratios()

    lines: list[str] = []
    lines.append("# Chapter 16 — output of the Hessian blocks builder")
    lines.append("")
    lines.append("## Classification")
    lines.append("")
    lines.append("- Leading blocks: direct evaluation of already derived quantity.")
    lines.append("- Blocks `required`: inverse diagnostic of the missing upper channel.")
    lines.append("")
    lines.append("## Parameters")
    lines.append("")
    lines.append(f"- `alpha_inv = {ALPHA_INV:.12f}`")
    lines.append(f"- `alpha = {ALPHA:.15e}`")
    lines.append(f"- `K1 = 2*pi/alpha = {K1:.15e}`")
    lines.append(f"- `a_leader = alpha/(2*pi) = {A1:.15e}`")
    lines.append("")

    Hlead, clead, mlead = leading_block()
    lead_path = base / "leading_hessian_gminus2.npz"
    save_npz(lead_path, Hlead, clead, mlead)
    lead_eval = evaluate(Hlead, clead, mlead)

    lines.append("## Universal leading block")
    lines.append("")
    lines.append(f"- file: `{lead_path.name}`")
    lines.append(f"- `a_geom = {lead_eval['a_geom']:.15e}`")
    lines.append(f"- `g_total = {lead_eval['g_total']:.15e}`")
    lines.append(f"- `eig_min = {lead_eval['eig_min']:.15e}`")
    lines.append("")

    lines.append("## Q39 hierarchy used for diagnostic stiffness")
    lines.append("")
    lines.append("| case | Q39 role | M_l/M_e | K2 used |")
    lines.append("|---|---|---:|---:|")
    for case in cases:
        ratio = case.ratio_q39
        # Positive K2 scaled by relative mass stiffness. This is a
        # diagnostic choice to measure the required amplitude; it is not a prediction.
        k2 = K1 * max(1.0, ratio)
        lines.append(f"| {case.name} | {case.role_q39} | {ratio:.15e} | {k2:.15e} |")
    lines.append("")

    lines.append("## Required upper blocks")
    lines.append("")
    lines.append(
        "In these blocks the amplitude `mu2_required` is chosen to reach "
        "`a_obs`. Therefore, they are diagnostic reverse engineering."
    )
    lines.append("")
    lines.append("| case | a_obs | residual a_obs-a_leader | mu2_required | reconstructed a | file |")
    lines.append("|---|---:|---:|---:|---:|---|")
    for case in cases:
        if case.anomaly_obs is None:
            lines.append(f"| {case.name} | — | — | — | — | — |")
            continue
        ratio = case.ratio_q39
        k2 = K1 * max(1.0, ratio)
        H, c, m, mu2 = required_block(case.anomaly_obs, k2=k2)
        out = base / f"required_hessian_{case.symbol}_gminus2.npz"
        save_npz(out, H, c, m)
        ev = evaluate(H, c, m)
        lines.append(
            f"| {case.name} | {case.anomaly_obs:.15e} | "
            f"{case.anomaly_obs - A1:.15e} | {mu2:.15e} | "
            f"{ev['a_geom']:.15e} | `{out.name}` |"
        )
    lines.append("")

    lines.append("## Verdict")
    lines.append("")
    lines.append(
        r"The leading block constructs $H_C,c,m_\perp$ without an experimental target and "
        r"reproduces exactly $\alpha/(2\pi)$."
    )
    lines.append("")
    lines.append(
        "The `required` blocks numerically show the size of the upper transverse "
        "response that remains to be derived. They do not metrologically close "
        r"$g-2$, but they transform the pending task into a precise "
        "quantity: to derive from the official action the channel that will replace "
        "`mu2_required`."
    )
    lines.append("")

    report = base / "output_gminus2_hessian_blocks.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
