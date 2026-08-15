#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `signal variance autocorrelation` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / autocorrelation scaling.

Fits power laws to the preserved reduced data:

    tau_corr ~ N^p
    1/gap ~ N^p_gap

Classification: reduced numerical scaling test.
"""

from __future__ import annotations

from pathlib import Path
import math


def fit_power(xs: list[float], ys: list[float]) -> tuple[float, float]:
    lx = [math.log(x) for x in xs]
    ly = [math.log(y) for y in ys]
    mx = sum(lx) / len(lx)
    my = sum(ly) / len(ly)
    p = sum((x - mx) * (y - my) for x, y in zip(lx, ly)) / sum((x - mx) ** 2 for x in lx)
    c = math.exp(my - p * mx)
    return c, p


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_signal_variance_autocorrelation.md"

    n = [16, 36, 64]
    tau = [8.241905, 17.523244, 30.118337]
    c_tau, p_tau = fit_power(n, tau)

    n2 = [4, 8, 16, 32, 64]
    inv_gap = [2.222222, 7.587141, 29.193492, 115.652077, 461.494514]
    c_gap, p_gap = fit_power(n2, inv_gap)

    text = f"""# Output — autocorrelation and variance of the signal problem

Classification: reduced numerical scaling test.

| fit | C | exponent |
|---|---:|---:|
| tau_corr ~ C N^p | {c_tau:.12e} | {p_tau:.6f} |
| 1/gap ~ C N^p | {c_gap:.12e} | {p_gap:.6f} |

Interpretation: the reduced data indicate polynomial scaling in the interval
tested. This is not a general asymptotic proof.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
