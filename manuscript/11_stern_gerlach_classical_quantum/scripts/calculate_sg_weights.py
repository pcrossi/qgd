#!/usr/bin/env python3
"""
GDQ — Chapter 11 / Stern--Gerlach Weights

Goal:
    Calculate p_±=(1±a·n)/2 for various angles between preparation and apparatus.

Theoretical source:
    manuscript/11_stern_gerlach_classical_quantum/notes/born_weights_sg.md

Classification:
    Operational consistency test. Not a metrological prediction.

Output:
    scripts/output_calculate_sg_weights.md
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "output_calculate_sg_weights.md"

    angles = [0, 30, 60, 90, 120, 180]
    rows = []
    for deg in angles:
        theta = math.radians(deg)
        p_plus = math.cos(theta / 2) ** 2
        p_minus = math.sin(theta / 2) ** 2
        rows.append((deg, p_plus, p_minus, p_plus + p_minus))

    table = "\n".join(
        f"| {deg} | {pp:.12f} | {pm:.12f} | {s:.12f} |"
        for deg, pp, pm, s in rows
    )

    text = f"""# Output — Stern--Gerlach angular weights

Classification: operational consistency test.

| theta degrees | p_plus | p_minus | sum |
|---:|---:|---:|---:|
{table}

Interpretation: the weights depend on the angle between preparation and apparatus axis;
two channels do not imply equal weights.
"""
    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
