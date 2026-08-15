#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `verify_monokinetic_liouville` associated with chapter `07_classical_limit`.

Verifies norm conservation for the transported density before caustics.

Free 1D model with constant velocity v:

    rho(x,t)=rho0(x-vt).

Thus:

    partial_t rho + v partial_x rho = 0.

We integrate the norm over a wide window to confirm conservation.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_verify_monokinetic_liouville.md")


def rho0(x: float) -> float:
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def integrate(func, lo: float, hi: float, n: int = 200000) -> float:
    h = (hi - lo) / n
    total = 0.5 * (func(lo) + func(hi))
    for i in range(1, n):
        total += func(lo + i * h)
    return total * h


def main() -> None:
    v = 1.7
    rows = []
    for t in [0, 1, 2, 4, 6]:
        norm = integrate(lambda x: rho0(x - v * t), -20, 20)
        rows.append((t, norm, abs(norm - 1.0)))

    lines = [
        "---",
        'title: "Output — Monokinetic Liouville"',
        "---",
        "",
        "# Output — Monokinetic Liouville",
        "",
        "Classification: classical transport toy model before caustics.",
        "",
        "| $t$ | transported norm | error against 1 |",
        "|---:|---:|---:|",
    ]
    for t, norm, err in rows:
        lines.append(f"| {t} | {norm:.12f} | {err:.3e} |")

    lines += [
        "",
        "Conclusion: before caustics and without flux leakage, continuity",
        "transports the density and conserves the ensemble norm.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
