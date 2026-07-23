#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / Hipercargas por Z6 e anomalias

Objetivo:
    Verificar a busca diofantina das hipercargas inteiras y=6Y.

Construção testada:
    1. O quociente global impõe congruências módulo 6.
    2. As anomalias impõem quatro equações inteiras.
    3. A primitividade seleciona a solução mínima.

Classificação:
    Verificação simbólico-numérica exata. Não é ajuste experimental.

Saída:
    scripts/saida_hipercargas_z6.md
"""

from __future__ import annotations

from math import gcd
from pathlib import Path


def primitive(values: tuple[int, ...]) -> bool:
    """Return True when the integer charge vector has no common divisor."""

    divisor = 0
    for value in values:
        divisor = gcd(divisor, abs(value))
    return divisor == 1


def anomaly_free(q: int, u: int, d: int, ell: int, e: int) -> bool:
    """Check the four anomaly cancellation equations for one generation."""

    return (
        2 * q + u + d == 0
        and 3 * q + ell == 0
        and 6 * q + 3 * u + 3 * d + 2 * ell + e == 0
        and 6 * q**3 + 3 * u**3 + 3 * d**3 + 2 * ell**3 + e**3 == 0
    )


def quotient_allowed(q: int, u: int, d: int, ell: int, e: int) -> bool:
    """Check the Z6 descent congruences for the five multiplets."""

    return (
        q % 6 == 1
        and u % 6 == 2
        and d % 6 == 2
        and ell % 6 == 3
        and e % 6 == 0
    )


def search(bound: int = 42) -> list[tuple[int, int, int, int, int]]:
    """Search all primitive solutions within an integer box."""

    solutions: list[tuple[int, int, int, int, int]] = []
    for q in range(-bound, bound + 1):
        if q % 6 != 1:
            continue
        ell = -3 * q
        e = 6 * q
        if max(abs(ell), abs(e)) > bound:
            continue
        for u in range(-bound, bound + 1):
            d = -2 * q - u
            values = (q, u, d, ell, e)
            if max(map(abs, values)) > bound:
                continue
            if quotient_allowed(*values) and anomaly_free(*values) and primitive(values):
                solutions.append(values)
    return sorted(set(solutions))


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_hipercargas_z6.md"
    bound = 42
    solutions = search(bound)

    rows = "\n".join(
        f"| {q} | {u} | {d} | {ell} | {e} | "
        f"{q/6:.12g} | {u/6:.12g} | {d/6:.12g} | {ell/6:.12g} | {e/6:.12g} |"
        for q, u, d, ell, e in solutions
    )

    text = f"""# Saída — hipercargas por Z6

Classificação: verificação simbólico-numérica exata.

Faixa pesquisada:

$$
|y_i|\\le {bound}.
$$

| q | u | d | ell | e | Y_Q | Y_uc | Y_dc | Y_L | Y_ec |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
{rows}

Número de soluções primitivas encontradas: {len(solutions)}.

Interpretação: a solução orientada mínima contém

$$
(q,u,d,\\ell,e)=(1,-4,2,-3,6),
$$

isto é,

$$
(Y_Q,Y_{{u^c}},Y_{{d^c}},Y_L,Y_{{e^c}})
=
\\left(\\frac16,-\\frac23,\\frac13,-\\frac12,1\\right).
$$

As demais soluções dentro da caixa representam a troca dos singletos de cor ou
orientações equivalentes permitidas pela escolha global.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
