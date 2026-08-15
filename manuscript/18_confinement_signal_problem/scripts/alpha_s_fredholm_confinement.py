#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `alpha s fredholm confinement` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / effective alpha_s by Fredholm.

Evaluates:

    alpha_s_eff = (1/2)*(3/(4*pi)) = 3/(8*pi)

Classification: direct evaluation of sectorial proposal; not a full running.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_alpha_s_fredholm_confinement.md"

    t = 0.5
    alpha_s = t * 3.0 / (4.0 * math.pi)

    text = f"""# Output — effective alpha_s by Fredholm

Classification: direct evaluation of the sectorial proposal.

| quantity | value |
|---|---:|
| T_transm | {t:.12f} |
| 3/(4*pi) | {3.0/(4.0*math.pi):.12f} |
| alpha_s_eff = 3/(8*pi) | {alpha_s:.12f} |

Interpretation: effective coupling of specific hadronic scale/topology;
it is not a full running of QCD.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
