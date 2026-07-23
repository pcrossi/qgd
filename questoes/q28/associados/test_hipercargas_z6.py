#!/usr/bin/env python3
"""Busca diofantina das hipercargas inteiras y=6Y."""

from __future__ import annotations

from math import gcd
from pathlib import Path


def primitive(values: tuple[int, ...]) -> bool:
    divisor = 0
    for value in values:
        divisor = gcd(divisor, abs(value))
    return divisor == 1


def anomaly_free(q: int, u: int, d: int, ell: int, e: int) -> bool:
    return (
        2 * q + u + d == 0
        and 3 * q + ell == 0
        and 6 * q + 3 * u + 3 * d + 2 * ell + e == 0
        and 6 * q**3 + 3 * u**3 + 3 * d**3 + 2 * ell**3 + e**3 == 0
    )


def quotient_allowed(q: int, u: int, d: int, ell: int, e: int) -> bool:
    return (
        q % 6 == 1
        and u % 6 == 2
        and d % 6 == 2
        and ell % 6 == 3
        and e % 6 == 0
    )


def search(bound: int = 30) -> list[tuple[int, int, int, int, int]]:
    solutions: list[tuple[int, int, int, int, int]] = []
    for q in range(-bound, bound + 1):
        if q % 6 != 1:
            continue
        ell = -3 * q
        e = 6 * q
        if abs(ell) > bound or abs(e) > bound:
            continue
        for u in range(-bound, bound + 1):
            d = -2 * q - u
            values = (q, u, d, ell, e)
            if max(map(abs, values)) > bound:
                continue
            if quotient_allowed(*values) and anomaly_free(*values) and primitive(values):
                solutions.append(values)
    return sorted(set(solutions))


def render(bound: int = 30) -> str:
    solutions = search(bound)
    lines = [
        "# Q28 — Busca diofantina das hipercargas",
        "",
        f"Faixa pesquisada: $|y_i|\\leq {bound}$.",
        "",
        "| $q$ | $u$ | $d$ | $\\ell$ | $e$ |",
        "|---:|---:|---:|---:|---:|",
    ]
    for solution in solutions:
        lines.append("| " + " | ".join(map(str, solution)) + " |")
    lines += [
        "",
        f"Número de soluções primitivas: ${len(solutions)}$.",
        "",
        "As duas soluções esperadas diferem apenas pela troca dos dois singletos",
        "de cor. A conjugação global corresponde à orientação oposta do gerador",
        "$U(1)$ e pode ser escrita usando a escolha conjugada do gerador de",
        "$\\mathbb Z_6$.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    report = render()
    output = Path(__file__).with_name("resultado_hipercargas_z6.md")
    output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
