#!/usr/bin/env python3
"""
Objective:
    Register in a self-contained way the verification `compare tension confinement radii` associated with chapter `18_confinement_signal_problem`.

GDQ — Chapter 18 / comparison of tension by radii.

Compares the reduced tension sigma=pi*hbarc/r^2 for three radii:
0.86 fm, radius of the leptonic hierarchy/baryonic structure, and effective compressed radius.
"""

from __future__ import annotations

from pathlib import Path
import math


def sigma(hbarc: float, r: float) -> float:
    return math.pi * hbarc / (r * r)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_compare_tension_confinement_radii.md"

    hbarc = 0.1973269804
    ref = 0.89
    radii = [
        ("initial radius 0.86 fm", 0.86),
        ("leptonic hierarchy and baryonic structure", 0.84077876545),
        ("compressed effective", 0.8354),
    ]

    lines = [
        "# Output — comparison of tension by radii",
        "",
        "Classification: posterior phenomenological comparison.",
        "",
        "| case | r fm | sigma GeV/fm | deviation vs 0.89 |",
        "|---|---:|---:|---:|",
    ]
    for label, r in radii:
        sig = sigma(hbarc, r)
        lines.append(f"| {label} | {r:.12f} | {sig:.12f} | {(sig-ref)/ref:.6%} |")
    lines += [
        "",
        "Interpretation: the compressed effective radius practically closes the scale of",
        "tension, but remains sectorial until re-derived in the same background of the tube.",
    ]
    text = "\n".join(lines) + "\n"
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
