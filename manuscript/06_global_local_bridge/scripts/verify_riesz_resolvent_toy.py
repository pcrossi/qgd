#!/usr/bin/env python3
"""
Objective:
    Self-contained verification record of `verify_riesz_resolvent_toy` associated with chapter `06_global_local_bridge`.

Toy model of resolvent and Riesz projector.

We create a symmetric matrix K0 with an isolated cluster of dimension 2. We perturb
by eps*V and compare the spectral projectors of the cluster. The stable object is
the projector, not each individual eigenvector.
"""

from pathlib import Path
import numpy as np


OUT = Path(__file__).with_name("output_verify_riesz_resolvent_toy.md")


def projector(K: np.ndarray, rank: int = 2) -> np.ndarray:
    vals, vecs = np.linalg.eigh(K)
    U = vecs[:, :rank]
    return U @ U.T


def main() -> None:
    rng = np.random.default_rng(12345)
    K0 = np.diag([1.0, 1.2, 5.0, 6.0, 8.0, 10.0])
    A = rng.normal(size=(6, 6))
    V = (A + A.T) / 2.0
    P0 = projector(K0)

    z = 3.0
    R0 = np.linalg.inv(K0 - z * np.eye(6))

    rows = []
    for eps in [0.2, 0.1, 0.05, 0.02, 0.01]:
        Ke = K0 + eps * V
        Pe = projector(Ke)
        Re = np.linalg.inv(Ke - z * np.eye(6))
        proj_err = np.linalg.norm(Pe - P0, ord=2)
        res_err = np.linalg.norm(Re - R0, ord=2)
        vals = np.linalg.eigvalsh(Ke)
        cluster_gap = min(vals[2] - vals[1], vals[0] - (-np.inf))
        rows.append((eps, proj_err, res_err, vals[0], vals[1], vals[2], cluster_gap))

    lines = [
        "---",
        'title: "Output — toy resolvent and Riesz"',
        "---",
        "",
        "# Output — toy resolvent and Riesz",
        "",
        "Classification: spectral toy model / consistency verification.",
        "",
        "| $\\varepsilon$ | projector error | resolvent error at $z=3$ | $\\lambda_1$ | $\\lambda_2$ | $\\lambda_3$ | cluster gap |",
        "|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for eps, proj_err, res_err, l1, l2, l3, gap in rows:
        lines.append(
            f"| {eps:.3f} | {proj_err:.6e} | {res_err:.6e} | {l1:.6f} | {l2:.6f} | {l3:.6f} | {gap:.6f} |"
        )

    lines += [
        "",
        "Conclusion: when the cluster remains separated, the spectral projectors",
        "converge with the perturbation. This is the finite form of the inheritance",
        "argument by resolvents and Riesz projectors.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
