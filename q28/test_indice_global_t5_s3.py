#!/usr/bin/env python3
"""Álgebra de cohomologia mínima para o índice em T5 x S3."""

from __future__ import annotations

from pathlib import Path


def su2_index(pairing: int) -> float:
    return pairing / 6.0


def render() -> str:
    pairings = [0, 6, 12, 18, 24, 30]
    lines = [
        "# Q28 — Índice global em $T^5\\times S^3$",
        "",
        "Para $c_2=a_4+b_1u_3$:",
        "",
        "$$",
        "\\operatorname{Ind}D^+=\\frac16\\langle a_4b_1,[T^5]\\rangle.",
        "$$",
        "",
        "| $N_{ab}$ | índice |",
        "|---:|---:|",
    ]
    for pairing in pairings:
        lines.append(f"| {pairing} | {su2_index(pairing):.0f} |")
    lines += [
        "",
        "O índice três requer $N_{ab}=18$.",
        "",
        "Para uma linha puxada apenas de $T^5$, $c_1^4=0$ por dimensão e o",
        "índice global é zero.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    report = render()
    output = Path(__file__).with_name("resultado_indice_global_t5_s3.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
