#!/usr/bin/env python3
"""Chapter 16 — derivation of the physical upper channel of magnetic source.

Objective:
    Determine whether the first upper channel can appear as a new direct linear source
    M_perp^(2)[Phi;B] for a uniform magnetic field.

Expected result by symmetry:
    For a uniform field on the Noether cycle, only the Hodge harmonic component
    couples linearly. Upper exact modes have zero integral.
    Hence mu_{2,l}^{direct}=0.

Classification:
    direct evaluation of a selection rule of the magnetic map; does not use an
    experimental target.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parent
ALPHA = 1.0 / 137.035999177
K1 = 2.0 * math.pi / ALPHA


def grid(n: int = 65536) -> tuple[np.ndarray, float]:
    theta = np.linspace(0.0, 2.0 * math.pi, n, endpoint=False)
    return theta, theta[1] - theta[0]


def inner(a: np.ndarray, b: np.ndarray, dtheta: float) -> float:
    return float(np.sum(a * b) * dtheta)


def normalized_constant_one_form(theta: np.ndarray) -> np.ndarray:
    # h=dtheta/(2pi). We represent only the angular coefficient.
    return np.ones_like(theta) / (2.0 * math.pi)


def exact_mode(theta: np.ndarray, k: int) -> np.ndarray:
    # d(sin(k theta))/(2pi) = k cos(k theta)/(2pi).
    return k * np.cos(k * theta) / (2.0 * math.pi)


def normalized_exact_mode(theta: np.ndarray, dtheta: float, k: int) -> np.ndarray:
    mode = exact_mode(theta, k)
    norm = math.sqrt(inner(mode, mode, dtheta))
    return mode / norm


def r_mu_intrinsic(alpha_inv: float = 137.035999177) -> float:
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


def stable_block_with_selection(ratio: float) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float]]:
    k2 = K1 * max(1.0, ratio)

    # e0: circulation; e1: leading harmonic channel; e2: first upper exact mode.
    # Selection rule: direct mu2 = 0 for uniform B.
    H = np.array(
        [
            [1.0, -1.0, 0.0],
            [-1.0, K1, 0.0],
            [0.0, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0], dtype=float)
    m_perp = np.array([0.0, 1.0, 0.0], dtype=float)
    meta = {"mass_ratio": ratio, "K2": k2}
    return H, c, m_perp, meta


def evaluate_anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(0.5 * (H + H.T))
    Hinv = (vecs * (1.0 / vals)) @ vecs.T
    return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))


def main() -> None:
    theta, dtheta = grid()
    h = normalized_constant_one_form(theta)
    mode1 = normalized_exact_mode(theta, dtheta, 1)
    mode2 = normalized_exact_mode(theta, dtheta, 2)

    h_norm2 = inner(h, h, dtheta)
    overlap_h_mode1 = inner(h, mode1, dtheta)
    overlap_h_mode2 = inner(h, mode2, dtheta)
    overlap_mode1_mode2 = inner(mode1, mode2, dtheta)

    r_mu = r_mu_intrinsic()
    lepton_map = {
        "e": ("primary torsion", 1.0),
        "mu": ("transverse/bispatial torsion", r_mu),
        "tau": ("three-dimensional saturation", r_tau_from_q(r_mu)),
    }
    rows = []
    for symbol, (role, ratio) in lepton_map.items():
        H, c, m, meta = stable_block_with_selection(ratio)
        a = evaluate_anomaly(H, c, m)
        out = BASE / f"leptonic_selection_background_{symbol}_gminus2.npz"
        np.savez(
            out,
            H=H,
            c=c,
            m_perp=m,
            gamma0=np.array([1.0]),
            role_q39=np.array([role]),
            ratio_q39=np.array([ratio]),
            mu2_direct=np.array([0.0]),
        )
        rows.append((symbol, role, meta["mass_ratio"], meta["K2"], 0.0, a, out.name))

    lines = [
        "# Chapter 16 — derivation of the physical upper channel",
        "",
        "## Classification",
        "",
        "Direct evaluation of the selection rule of the linear magnetic map. Does not use",
        "the experimental value of `g_e` or `g_mu-2`.",
        "",
        "## 1. Linear magnetic map",
        "",
        "For a uniform magnetic field on the Noether cycle, the linear coupling",
        "selects only the Hodge harmonic component:",
        "",
        "$$",
        "M[\\Phi;B]",
        "=",
        "B\\left(\\gamma_0\\mathcal C[\\Phi]+M_\\perp[\\Phi]\\right).",
        "$$",
        "",
        r"The direct upper channel would be a projection of $M_\perp$ onto upper",
        r"exact modes $d\sin(k\vartheta)$.",
        "",
        "## 2. Selection rule",
        "",
        "$$",
        "h=\\frac{d\\vartheta}{2\\pi},",
        "\\qquad",
        "e_k\\propto d\\sin(k\\vartheta).",
        "$$",
        "",
        "Since the uniform field is constant on the cycle,",
        "",
        "$$",
        "\\langle h,e_k\\rangle=0",
        "\\qquad",
        "(k\\ge1).",
        "$$",
        "",
        "Numerically:",
        "",
        f"- `||h||^2 = {h_norm2:.15e}`",
        f"- `<h,e_1> = {overlap_h_mode1:.15e}`",
        f"- `<h,e_2> = {overlap_h_mode2:.15e}`",
        f"- `<e_1,e_2> = {overlap_mode1_mode2:.15e}`",
        "",
        "Therefore:",
        "",
        "$$",
        "\\boxed{\\mu_{2,\\ell}^{\\rm direct}=0.}",
        "$$",
        "",
        "## 3. Stable blocks with selection rule",
        "",
        "| lepton | Q39 role | M_l/M_e | K2 | direct mu2 | obtained a | file |",
        "|---|---|---:|---:|---:|---:|---|",
    ]
    for symbol, role, ratio, k2, mu2, a, name in rows:
        lines.append(f"| {symbol} | {role} | {ratio:.15e} | {k2:.15e} | {mu2:.1f} | {a:.15e} | `{name}` |")

    lines.extend(
        [
            "",
            "## 4. Consequence",
            "",
            "The first upper channel is not a new direct linear source for a uniform",
            "magnetic field. Thus, replacing the `required` blocks with a",
            "derived direct source gives `mu2=0`, not the observed metrological value.",
            "",
            "Therefore, the upper residuals of `g-2` must come from another internal link:",
            "",
            "1. correction of the physical Hessian `H_C=H_0+alpha H_1+...`;",
            "2. Hessian mixture between the leading channel and upper modes;",
            "3. non-uniform internal electrogeometric map, if derived from the bulk;",
            "4. or non-uniform apparatus source, which is not universal.",
            "",
            "For the universal anomaly of a uniform field, the correct route is the",
            "Hessian correction, not a new direct `mu2`.",
            "",
        ]
    )
    report = BASE / "output_physical_upper_channel_gminus2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
