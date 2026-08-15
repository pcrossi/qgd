#!/usr/bin/env python3
"""Chapter 16 — contraction of the upper channel mediated by density.

Objective:
    Implement the consequence of the upper variations calculation:

        T123 ~= -2*pi

    The direct leading² -> upper term is zero in the reduced truncation; the robust
    upper channel is mediated by the density Re(f). If the physical leptonic
    background has a stationary amplitude eta_l in the density mode, the
    effective Hessian receives:

        (H_eff)12 = (H0)12 + eta_l T123.

    This script calculates the resulting response without using experimental values.

Classification:
    conditional evaluation of a derived channel. With eta_l=0, it is a consistency test
    of current effective backgrounds; with eta_l coming from an 8D saddle,
    it becomes a direct evaluation of the derived quantity.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np


BASE = Path(__file__).resolve().parent
ALPHA = 1.0 / 137.035999177
T123_REDUCED = -6.283174869281538


def load_block(path: Path) -> tuple[np.ndarray, np.ndarray, np.ndarray, float, dict[str, str | float]]:
    data = np.load(path, allow_pickle=True)
    H = np.asarray(data["H"], dtype=float)
    c = np.asarray(data["c"], dtype=float).reshape(-1)
    m = np.asarray(data["m_perp"], dtype=float).reshape(-1)
    gamma0 = float(np.asarray(data["gamma0"]).reshape(-1)[0]) if "gamma0" in data else 1.0
    meta: dict[str, str | float] = {}
    if "ratio_q39" in data:
        meta["ratio_q39"] = float(np.asarray(data["ratio_q39"]).reshape(-1)[0])
    if "role_q39" in data:
        meta["role_q39"] = str(np.asarray(data["role_q39"]).reshape(-1)[0])
    return H, c, m, gamma0, meta


def anomaly(H: np.ndarray, c: np.ndarray, m: np.ndarray, gamma0: float) -> float:
    Hh = 0.5 * (H + H.T)
    vals, vecs = np.linalg.eigh(Hh)
    if np.min(vals) <= 0.0:
        raise ValueError(f"Hessian not positive: min eig = {np.min(vals):.6e}")
    Hinv = (vecs * (1.0 / vals)) @ vecs.T
    return float((c @ (Hinv @ m)) / (gamma0 * (c @ (Hinv @ c))))


def apply_density_channel(H: np.ndarray, eta_density: float, t123: float) -> np.ndarray:
    """Adds the density-mediated correction to the leading-upper block.

    Effective block convention:
        index 0: protected circulation;
        index 1: leading harmonic;
        index 2: upper harmonic.

    By expansion:
        S = S0 + 1/2 H_ij dx_i dx_j + 1/6 T_ijk dx_i dx_j dx_k + ...

    if x3 = eta is a stationary amplitude of the background, then:
        d²S/dx1dx2 = H12 + T123 eta.

    Since the reduced three-mode block does not explicitly contain x3, this
    contribution is projected onto H[1,2].
    """
    H_eff = np.array(H, dtype=float, copy=True)
    if H_eff.shape[0] < 3:
        raise ValueError("the block must contain circulation, leading, and upper modes")
    delta = eta_density * t123
    H_eff[1, 2] += delta
    H_eff[2, 1] += delta
    return 0.5 * (H_eff + H_eff.T)


def default_blocks() -> list[Path]:
    return [
        BASE / "leptonic_stable_background_e_gminus2.npz",
        BASE / "leptonic_stable_background_mu_gminus2.npz",
        BASE / "leptonic_stable_background_tau_gminus2.npz",
    ]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--eta-density",
        type=float,
        default=0.0,
        help="stationary amplitude of the density mode Re(f) in the background",
    )
    parser.add_argument(
        "--t123",
        type=float,
        default=T123_REDUCED,
        help="reduced cubic coefficient T123",
    )
    args = parser.parse_args()

    rows = []
    for path in default_blocks():
        H, c, m, gamma0, meta = load_block(path)
        a0 = anomaly(H, c, m, gamma0)
        H_eff = apply_density_channel(H, args.eta_density, args.t123)
        eig_min = float(np.min(np.linalg.eigvalsh(H_eff)))
        a_eff = anomaly(H_eff, c, m, gamma0)
        rows.append(
            {
                "file": path.name,
                "role": meta.get("role_q39", ""),
                "ratio": meta.get("ratio_q39", float("nan")),
                "a0": a0,
                "a_eff": a_eff,
                "delta_a": a_eff - a0,
                "eig_min": eig_min,
            }
        )

    lines = [
        "# Chapter 16 — contraction of the upper channel mediated by density",
        "",
        "## Classification",
        "",
        "Conditional evaluation of a derived channel from the reduced action. Does not use",
        "experimental values of `g-2`.",
        "",
        "## 1. Input",
        "",
        f"- `eta_density = {args.eta_density:.15e}`",
        f"- `T123 = {args.t123:.15e}`",
        f"- `alpha/(2*pi) = {ALPHA/(2.0*math.pi):.15e}`",
        "",
        "The applied channel is:",
        "",
        "$$",
        "\\Delta H_{12}",
        "=",
        "\\eta_\\ell T_{123}.",
        "$$",
        "",
        "Here $\\eta_\\ell$ must come from an admissible saddle. The normalized",
        "reduced angular saddle was calculated separately and provides",
        "$\\eta_\\ell=0$. A non-zero value would require the non-homogeneous,",
        "warped, or mixed 8D background.",
        "",
        "## 2. Results",
        "",
        "| block | Q39 role | M_l/M_e | eig_min | a0 | a_eff | delta_a |",
        "|---|---|---:|---:|---:|---:|---:|",
    ]
    for row in rows:
        lines.append(
            f"| `{row['file']}` | {row['role']} | {row['ratio']:.15e} | "
            f"{row['eig_min']:.15e} | {row['a0']:.15e} | "
            f"{row['a_eff']:.15e} | {row['delta_a']:.15e} |"
        )

    lines.extend(
        [
            "",
            "## 3. Reading",
            "",
            "For the value reported above, the table directly shows the response",
            "of the density-mediated channel. The canonical execution uses",
            "$\\eta_\\ell=0$, the value of the normalized reduced angular saddle; in this",
            "case, the contraction does not alter the leading response.",
            "",
            "Therefore, the next physical datum needed for metrology is not",
            "`mu2_required`; it is $\\eta_\\ell$ or, more generally, the complete",
            "stationary profile of $\\operatorname{Re}f$ in the 8D leptonic saddle.",
            "Once this background is provided, this same operator calculates",
            "the correction without experimental adjustment.",
            "",
        ]
    )

    out = BASE / "output_contract_density_channel_gminus2.md"
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
