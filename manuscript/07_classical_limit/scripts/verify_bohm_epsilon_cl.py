#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `verify_bohm_epsilon_cl` associated with chapter `07_classical_limit`.

Verifies the scale of the Bohm term.

For R(x)=exp(-x^2/(2L^2)) in 1D:

    Q_B = -(hbar^2/2m) R''/R.

At point x=0, |R''/R|=1/L^2. With T=p^2/(2m):

    |Q_B|/T = hbar^2/(p^2 L^2) = epsilon_cl^2.

This is a direct test of the estimate used in Chapter 7.
"""

from pathlib import Path


OUT = Path(__file__).with_name("output_verify_bohm_epsilon_cl.md")


def main() -> None:
    hbar = 1.0
    m = 1.0
    p = 10.0
    rows = []
    for L in [2, 4, 8, 16, 32, 64]:
        epsilon = hbar / (p * L)
        qb_abs = hbar * hbar / (2 * m * L * L)
        t_cl = p * p / (2 * m)
        ratio = qb_abs / t_cl
        rows.append((L, epsilon, ratio, ratio / (epsilon * epsilon)))

    lines = [
        "---",
        'title: "Output — scale of the Bohm term"',
        "---",
        "",
        "# Output — scale of the Bohm term",
        "",
        "Classification: direct evaluation of an analytical estimate in a toy model.",
        "",
        "| $L_\\rho$ | $\\varepsilon_{\\rm cl}$ | $|Q_B|/T_{\\rm cl}$ | ratio by $\\varepsilon_{\\rm cl}^2$ |",
        "|---:|---:|---:|---:|",
    ]
    for L, eps, ratio, scaled in rows:
        lines.append(f"| {L} | {eps:.8e} | {ratio:.8e} | {scaled:.8f} |")

    lines += [
        "",
        "Conclusion: in this Gaussian profile, the ratio is exactly",
        "$|Q_B|/T_{\\rm cl}=\\varepsilon_{\\rm cl}^2$ at the center of the packet.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
