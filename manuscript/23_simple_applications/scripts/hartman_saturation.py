#!/usr/bin/env python3
"""
Objective:
    Self-contained verification of `hartman saturation` associated with chapter `23_simple_applications`.
    Chapter 23 — geometric saturation of the Hartman effect.

Classification:
    Direct evaluation of reduced formula. No experimental target is used.

Equation:
    D(L)=sqrt(g0)/kappa * (1-exp(-kappa L)).
"""

from __future__ import annotations

from pathlib import Path
import math


OUT = Path(__file__).with_name("output_hartman_saturation.md")


def main() -> None:
    kappa = 1.0
    g0 = 1.0
    v0 = 1.0
    limit = math.sqrt(g0) / kappa
    lengths = [0.1, 0.5, 1.0, 2.0, 4.0, 8.0]

    lines = [
        "---",
        'title: "Output — Reduced Hartman"',
        "---",
        "",
        "# Output — Reduced Hartman",
        "",
        "- reduced parameters: $\\kappa=1$, $g_0=1$, $v_0=1$;",
        f"- proper limit: `{limit:.12f}`;",
        "- classification: direct evaluation of reduced formula.",
        "",
        "| $L$ | $D_{\\rm prop}(L)$ | $\\tau_{\\rm GDQ}(L)$ | fraction of limit |",
        "|---:|---:|---:|---:|",
    ]
    for length in lengths:
        dprop = math.sqrt(g0) / kappa * (1.0 - math.exp(-kappa * length))
        tau = dprop / v0
        lines.append(f"| `{length:.1f}` | `{dprop:.12f}` | `{tau:.12f}` | `{dprop/limit:.12f}` |")

    lines += [
        "",
        "Interpretation: the proper length saturates; this is not superluminal front",
        "velocity.",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
