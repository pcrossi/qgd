#!/usr/bin/env python3
"""Números de Betti de T^5 x S^3 pelo produto de Poincaré."""

from __future__ import annotations

from math import comb
from pathlib import Path


def betti_numbers() -> list[int]:
    torus = [comb(5, k) for k in range(6)]
    sphere = [1, 0, 0, 1]
    result = [0] * (len(torus) + len(sphere) - 1)
    for i, left in enumerate(torus):
        for j, right in enumerate(sphere):
            result[i + j] += left * right
    return result


def render() -> str:
    betti = betti_numbers()
    euler = sum(((-1) ** degree) * value for degree, value in enumerate(betti))
    lines = [
        "# Q28 — Cohomologia de $T^5\\times S^3$",
        "",
        "| grau $k$ | " + " | ".join(map(str, range(len(betti)))) + " |",
        "|---:|" + "---:|" * len(betti),
        "| $b_k$ | " + " | ".join(map(str, betti)) + " |",
        "",
        f"Característica de Euler: $\\chi={euler}$.",
        "",
        "A topologia real não fornece automaticamente o número três e não",
        "determina números de Hodge sem uma estrutura complexa concreta.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    report = render()
    output = Path(__file__).with_name("resultado_betti_t5_s3.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
