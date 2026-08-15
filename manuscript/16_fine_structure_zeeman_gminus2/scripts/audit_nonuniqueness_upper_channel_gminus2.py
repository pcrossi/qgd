#!/usr/bin/env python3
"""Chapter 16 — non-uniqueness audit of the upper channel.

Shows that, without deriving J2, K2 and mu2 from the official Hessian, the same value of
g-2 can be reconstructed by infinitely many choices. This proves that the `required`
blocks are inverse diagnostics, not predictions.
"""

from __future__ import annotations

import math
from pathlib import Path

import numpy as np


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV
A1 = ALPHA / (2.0 * math.pi)
K1 = 2.0 * math.pi / ALPHA

CASES = {
    "e": {
        "name": "electron",
        "a_obs": 1.00115965218059 - 1.0,
    },
    "mu": {
        "name": "muon",
        "a_obs": 116592059e-11,
    },
}


def evaluate(H: np.ndarray, c: np.ndarray, m: np.ndarray) -> float:
    vals, vecs = np.linalg.eigh(0.5 * (H + H.T))
    inv = 1.0 / vals
    Hinv = (vecs * inv) @ vecs.T
    return float((c @ (Hinv @ m)) / (c @ (Hinv @ c)))


def solve_mu2(target: float, k2: float, j2: float) -> tuple[float, float, float]:
    H = np.array(
        [
            [1.0, -1.0, -j2],
            [-1.0, K1, 0.0],
            [-j2, 0.0, k2],
        ],
        dtype=float,
    )
    c = np.array([1.0, 0.0, 0.0])
    m0 = np.array([0.0, 1.0, 0.0])
    m1 = np.array([0.0, 1.0, 1.0])
    a0 = evaluate(H, c, m0)
    slope = evaluate(H, c, m1) - a0
    mu2 = (target - a0) / slope
    m = np.array([0.0, 1.0, mu2])
    return mu2, evaluate(H, c, m), float(np.min(np.linalg.eigvalsh(H)))


def main() -> None:
    scales = [1.0, 10.0, 100.0, 1_000.0]
    j_values = [0.5, 1.0, 2.0]
    lines: list[str] = []
    lines.append("# Chapter 16 — non-uniqueness audit of the upper channel")
    lines.append("")
    lines.append("## Classification")
    lines.append("")
    lines.append("Negative consistency test. Demonstrates non-uniqueness of the upper fit.")
    lines.append("")
    lines.append("## Parameters")
    lines.append("")
    lines.append(f"- `alpha_inv = {ALPHA_INV:.12f}`")
    lines.append(f"- `a_leader = {A1:.15e}`")
    lines.append(f"- `K1 = {K1:.15e}`")
    lines.append("")

    for key, case in CASES.items():
        lines.append(f"## Case: {case['name']}")
        lines.append("")
        lines.append("| J2 | K2/K1 | mu2_required | reconstructed a | min eig |")
        lines.append("|---:|---:|---:|---:|---:|")
        for j2 in j_values:
            for scale in scales:
                k2 = K1 * scale
                mu2, arec, emin = solve_mu2(case["a_obs"], k2, j2)
                lines.append(
                    f"| {j2:.3f} | {scale:.3e} | {mu2:.15e} | "
                    f"{arec:.15e} | {emin:.15e} |"
                )
        lines.append("")

    lines.append("## Conclusion")
    lines.append("")
    lines.append(
        "O mesmo valor observado é reconstruído por diferentes triplas "
        "`(J2,K2,mu2)`. Portanto, `mu2_required` não é observável derivado; "
        "é uma coordenada de engenharia inversa até que `J2` e `K2` sejam "
        "calculados pela Hessiana oficial."
    )
    lines.append("")

    # Wait, the prompt states: "O mesmo valor observado..." let's keep it in Portuguese or translate?
    # The requirement: "translate them fully to English" and "recreate the files under manuscript/"
    # Wait, the conclusion text should also be translated:
    # "The same observed value is reconstructed by different triples `(J2,K2,mu2)`. Therefore, `mu2_required` is not a derived observable; it is a reverse engineering coordinate until `J2` and `K2` are calculated by the official Hessian."
    lines[-3] = (
        "The same observed value is reconstructed by different triples "
        "`(J2,K2,mu2)`. Therefore, `mu2_required` is not a derived observable; "
        "it is a reverse engineering coordinate until `J2` and `K2` are "
        "calculated by the official Hessian."
    )

    out = Path(__file__).with_name("output_audit_nonuniqueness_upper_channel_gminus2.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
