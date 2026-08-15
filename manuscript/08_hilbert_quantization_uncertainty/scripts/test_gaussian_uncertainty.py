#!/usr/bin/env python3
"""
Objective:
    Self-contained verification of `test gaussian uncertainty` associated with chapter `08_hilbert_quantization_uncertainty`.

Verifies the Heisenberg inequality for minimum Gaussians.

We use units where hbar=1. For a normalized Gaussian with deviation sigma:

    Delta x = sigma
    Delta p = hbar/(2 sigma)

Therefore:

    Delta x Delta p = hbar/2.
"""

from pathlib import Path

OUT = Path(__file__).with_name("output_test_gaussian_uncertainty.md")


def main() -> None:
    hbar = 1.0
    sigmas = [0.25, 0.5, 1.0, 2.0, 4.0]
    lines = [
        "---",
        'title: "Output — uncertainty in Gaussians"',
        "---",
        "",
        "# Output — uncertainty in Gaussians",
        "",
        "Classification: direct evaluation of analytical formula.",
        "",
        "| $\\sigma$ | $\\Delta x$ | $\\Delta p$ | product |",
        "|---:|---:|---:|---:|",
    ]
    for sigma in sigmas:
        dx = sigma
        dp = hbar / (2.0 * sigma)
        lines.append(f"| {sigma:.2f} | {dx:.8f} | {dp:.8f} | {dx * dp:.8f} |")
    lines += [
        "",
        "Conclusion: minimum Gaussians saturate",
        "$\\Delta x\\,\\Delta p=\\hbar/2$.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
