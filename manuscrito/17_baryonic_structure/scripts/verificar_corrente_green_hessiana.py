#!/usr/bin/env python3
"""
GDQ — Capítulo 17 / Corrente de Green da Hessiana

Verifica simbolicamente a identidade:

    d_x j(phi, psi) = U (psi L phi - phi L psi)

para o bloco reduzido

    L y = - U^{-1} d_x (U A d_x y) + V y.

Esse é o protótipo unidimensional da corrente bilinear conservada usada para
normalizar modos físicos da Hessiana. O script não usa dados experimentais e
não ajusta parâmetros.
"""

from __future__ import annotations

from pathlib import Path

import sympy as sp


def main() -> None:
    x = sp.symbols("x")
    U = sp.exp(-x**2)
    A = 1 + x**2 / 5
    V = 2 + x / 7

    phi = sp.sin(x) + x**2 / 3
    psi = sp.cos(2 * x) + x / 5

    def L(y: sp.Expr) -> sp.Expr:
        return -sp.diff(U * A * sp.diff(y, x), x) / U + V * y

    j = U * A * (phi * sp.diff(psi, x) - psi * sp.diff(phi, x))
    lhs = sp.simplify(sp.diff(j, x))
    rhs = sp.simplify(U * (psi * L(phi) - phi * L(psi)))
    residual = sp.simplify(lhs - rhs)

    lines = [
        "# Saída — corrente de Green da Hessiana",
        "",
        "## Operador testado",
        "",
        "```text",
        "L y = - U^{-1} d_x(U A d_x y) + V y",
        f"U = {sp.sstr(U)}",
        f"A = {sp.sstr(A)}",
        f"V = {sp.sstr(V)}",
        "```",
        "",
        "## Funções teste",
        "",
        "```text",
        f"phi = {sp.sstr(phi)}",
        f"psi = {sp.sstr(psi)}",
        "```",
        "",
        "## Identidade",
        "",
        "```text",
        "d_x j(phi, psi) - U(psi L phi - phi L psi) =",
        sp.sstr(residual),
        "```",
        "",
        f"Resultado: `residual == 0` é `{residual == 0}`.",
        "",
        "Conclusão: a corrente bilinear de Green é conservada para modos no kernel do operador físico.",
        "",
    ]

    out = Path(__file__).with_name("saida_verificar_corrente_green_hessiana.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
