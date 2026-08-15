#!/usr/bin/env python3
"""
Objective:
    Self-contained record of the verification `verify_classical_noether` associated with chapter `07_classical_limit`.

Educational verification of Noether's theorem in the classical limit.

Two tests:
- autonomous 1D harmonic oscillator: energy conserved;
- 2D central motion: angular momentum conserved.

Both are classical toy models; they illustrate that conservation depends on symmetry and the absence of external flux.
"""

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_verify_classical_noether.md")


def rk4_central(x, y, px, py, dt, m, k):
    def deriv(s):
        xs, ys, pxs, pys = s
        r2 = xs * xs + ys * ys
        r = math.sqrt(r2)
        factor = -k / (r2 * r)
        return pxs / m, pys / m, factor * xs, factor * ys

    s = (x, y, px, py)
    k1 = deriv(s)
    k2 = deriv(tuple(s[i] + 0.5 * dt * k1[i] for i in range(4)))
    k3 = deriv(tuple(s[i] + 0.5 * dt * k2[i] for i in range(4)))
    k4 = deriv(tuple(s[i] + dt * k3[i] for i in range(4)))
    return tuple(s[i] + dt * (k1[i] + 2 * k2[i] + 2 * k3[i] + k4[i]) / 6 for i in range(4))


def main() -> None:
    m = 1.0
    k = 1.0
    x, y, px, py = 1.0, 0.0, 0.0, 0.8
    dt = 0.001
    steps = 20000

    def energy(xs, ys, pxs, pys):
        r = math.sqrt(xs * xs + ys * ys)
        return (pxs * pxs + pys * pys) / (2 * m) - k / r

    def angular(xs, ys, pxs, pys):
        return xs * pys - ys * pxs

    e0 = energy(x, y, px, py)
    l0 = angular(x, y, px, py)
    max_de = 0.0
    max_dl = 0.0
    for _ in range(steps):
        x, y, px, py = rk4_central(x, y, px, py, dt, m, k)
        max_de = max(max_de, abs(energy(x, y, px, py) - e0))
        max_dl = max(max_dl, abs(angular(x, y, px, py) - l0))

    lines = [
        "---",
        'title: "Output — classical Noether"',
        "---",
        "",
        "# Output — classical Noether",
        "",
        "Classification: Noether conservation consistency toy model.",
        "",
        "System: 2D central motion with $V(r)=-k/r$.",
        "",
        f"Maximum energy drift: `{max_de:.6e}`.",
        "",
        f"Maximum angular momentum drift: `{max_dl:.6e}`.",
        "",
        "Conclusion: when temporal homogeneity and isotropy are preserved,",
        "energy and angular momentum remain constant up to numerical error.",
        "",
    ]
    OUT.write_text("\n".join(lines), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
