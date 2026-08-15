#!/usr/bin/env python3
"""Chapter 16 — reduced derivation of H1 by geometric mixture of harmonics.

Context:
    The direct linear upper magnetic source is zero for a uniform field.
    The next place where a universal correction can arise is the Hessian:

        H_C(alpha) = H_0 + alpha H_1 + ...

    This script calculates the first mixing term allowed by symmetry,
    without using experimental values of g_e or g_mu.

Idea:
    The angular leading mode u1(theta)=cos(theta) has local quadratic energy.
    The non-linearity of the weighted density of the official action allows the
    product u1^2 to contain a cos(2 theta) component, coupling to the first
    upper mode u2(theta)=cos(2 theta).

    The dimensionless geometric coefficient is the normalized overlap:

        beta_12 = <u2, u1^2 - <u1^2>> / sqrt(<u2,u2>) .

    The constant term is removed because it belongs to the already normalized sector of
    mass/volume. The absolute physical sign depends on the complete third variation
    of the official action; here we calculate the magnitude and the selection rule.

Classification:
    calculation of selection rule and reduced geometric magnitude of H1; it is not a
    complete metrological prediction.
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


def normed(mode: np.ndarray, dtheta: float) -> np.ndarray:
    norm = math.sqrt(inner(mode, mode, dtheta))
    return mode / norm


def evaluate(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(0.5 * (H + H.T))
    Hinv = (vecs * (1.0 / vals)) @ vecs.T
    return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))


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


def build_block(ratio: float, beta12: float, sign: float = 1.0) -> tuple[np.ndarray, np.ndarray, np.ndarray, dict[str, float]]:
    k2 = K1 * max(1.0, ratio)

    # H0: leading block + stable upper channel.
    H0 = np.array(
        [
            [1.0, -1.0, 0.0],
            [-1.0, K1, 0.0],
            [0.0, 0.0, k2],
        ],
        dtype=float,
    )

    # Reduced H1: the non-linearity of the leading channel mixes e1<->e2.
    # The natural stiffness scale is sqrt(K1*K2); alpha*H1 generates a small
    # relative correction, while beta12 fixes only the angular geometric part.
    H1 = np.zeros_like(H0)
    mix = sign * beta12 * math.sqrt(K1 * k2)
    H1[1, 2] = H1[2, 1] = mix
    H = H0 + ALPHA * H1
    c = np.array([1.0, 0.0, 0.0], dtype=float)
    m = np.array([0.0, 1.0, 0.0], dtype=float)
    meta = {
        "mass_ratio": ratio,
        "K2": k2,
        "mix_H1": mix,
        "eig_min_H": float(np.linalg.eigvalsh(H)[0]),
    }
    return H, c, m, meta


def main() -> None:
    theta, dtheta = grid()
    u1 = normed(np.cos(theta), dtheta)
    u2 = normed(np.cos(2.0 * theta), dtheta)
    u3 = normed(np.cos(3.0 * theta), dtheta)

    u1_sq = u1 * u1
    u1_sq_centered = u1_sq - inner(u1_sq, np.ones_like(theta), dtheta) / (2.0 * math.pi)

    beta12 = inner(u2, u1_sq_centered, dtheta)
    beta13 = inner(u3, u1_sq_centered, dtheta)
    beta11 = inner(u1, u1_sq_centered, dtheta)

    r_mu = r_mu_intrinsic()
    lepton_map = {
        "e": ("primary torsion", 1.0),
        "mu": ("transverse/bispatial torsion", r_mu),
        "tau": ("three-dimensional saturation", r_tau_from_q(r_mu)),
    }
    rows = []
    for symbol, (role, ratio) in lepton_map.items():
        H, c, m, meta = build_block(ratio, beta12, sign=1.0)
        a = evaluate(H, c, m)
        out = BASE / f"leptonic_h1mix_background_{symbol}_gminus2.npz"
        np.savez(
            out,
            H=H,
            c=c,
            m_perp=m,
            gamma0=np.array([1.0]),
            role_q39=np.array([role]),
            ratio_q39=np.array([ratio]),
            beta12=np.array([beta12]),
            mix_H1=np.array([meta["mix_H1"]]),
        )
        rows.append((symbol, role, meta["mass_ratio"], meta["K2"], meta["mix_H1"], meta["eig_min_H"], a, out.name))

    lines = [
        r"# Chapter 16 — reduced derivation of $H_1$ by harmonic mixture",
        "",
        "## Classification",
        "",
        "Calculation of selection rule and reduced geometric magnitude for the",
        r"Hessian mixture $H_1$. Does not use experimental values of $g_e$ or",
        r"$g_\mu-2$.",
        "",
        "## 1. Mechanism",
        "",
        "The direct upper source is zero for a uniform field. The first possible",
        "universal correction comes from the Hessian: the quadratic product of the leading mode",
        "contains a component in the first upper harmonic.",
        "",
        "$$",
        "\\cos^2\\vartheta",
        "=",
        "\\frac12\\left(1+\\cos2\\vartheta\\right).",
        "$$",
        "",
        "Removing the constant mode already absorbed in the normalization, there remains a",
        "component proportional to $\\cos2\\vartheta$.",
        "",
        "## 2. Normalized overlaps",
        "",
        "| quantity | overlap |",
        "|---|---:|",
        f"| `beta12 = <u2, u1^2 - mean>` | {beta12:.15e} |",
        f"| `beta11 = <u1, u1^2 - mean>` | {beta11:.15e} |",
        f"| `beta13 = <u3, u1^2 - mean>` | {beta13:.15e} |",
        "",
        "The selection is specific: the square of the leading mode couples to mode 2, but",
        "not to mode 1 or to mode 3 within numerical precision.",
        "",
        r"## 3. Block $H_C=H_0+\alpha H_1$",
        "",
        "There was used:",
        "",
        "$$",
        "(H_1)_{12}=(H_1)_{21}=\\beta_{12}\\sqrt{K_1K_2}.",
        "$$",
        "",
        "This is the mixing term allowed by symmetry. The absolute sign and",
        "any third variation factors depend on the complete 8D Hessian;",
        "here the minimal geometric magnitude was fixed.",
        "",
        "| lepton | Q39 role | M_l/M_e | K2 | H1_mix | eig_min | obtained a | file |",
        "|---|---|---:|---:|---:|---:|---:|---|",
    ]
    for row in rows:
        symbol, role, ratio, k2, mix, eig_min, a, name = row
        lines.append(f"| {symbol} | {role} | {ratio:.15e} | {k2:.15e} | {mix:.15e} | {eig_min:.15e} | {a:.15e} | `{name}` |")

    lines.extend(
        [
            "",
            "## 4. Verdict",
            "",
            r"The Hessian mixing route exists: $H_1$ is not forbidden by symmetry",
            "and its first angular magnitude is determined by $\\beta_{12}$.",
            "",
            r"However, in the minimal block with $m_\\perp=(0,1,0)$, this mixing alone",
            r"does not alter $a$ in a metrological way, because the upper channel",
            "does not yet possess its own source and there is no diagonal correction/normalization",
            "derived from the complete third variation.",
            "",
            "Conclusion: the next universal coefficient is not a new direct source",
            "and is also not closed only by angular mixing. It remains to evaluate the",
            "third/fourth variation of the official action on the 8D background to obtain",
            r"the tensorial factor that accompanies $\\beta_{12}$ and the diagonal",
            r"corrections of $H_1$.",
            "",
        ]
    )
    report = BASE / "output_h1_mixture_gminus2.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
