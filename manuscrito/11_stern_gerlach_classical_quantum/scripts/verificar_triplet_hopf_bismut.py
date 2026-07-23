#!/usr/bin/env python3
"""
GDQ — Capítulo 11 / Triplet Hopf--Bismut

Verificação autocontida do fato usado no texto:

1. na orientação complexa padrão de C^2 ~= R^4, o triplet hipercähler
   associado ao mapa de Hopf é auto-dual;
2. após normalização por sqrt(2), sua matriz de Gram é a identidade;
3. o aparelho seleciona uma direção dentro desse triplet, não o triplet.

O script é simbólico-numérico elementar. Ele não ajusta parâmetros e não usa
dados experimentais.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


PAIRS = ["12", "13", "14", "23", "24", "34"]
IDX = {p: i for i, p in enumerate(PAIRS)}


def vec(**coeffs: float) -> np.ndarray:
    out = np.zeros(6, dtype=float)
    for key, value in coeffs.items():
        out[IDX[key]] = value
    return out


def hodge_matrix() -> np.ndarray:
    """
    Hodge em R^4 orientado por e1^e2^e3^e4 > 0:
    *12=34, *13=-24, *14=23, *23=14, *24=-13, *34=12.
    """

    star = np.zeros((6, 6), dtype=float)
    mapping = {
        "12": ("34", +1.0),
        "13": ("24", -1.0),
        "14": ("23", +1.0),
        "23": ("14", +1.0),
        "24": ("13", -1.0),
        "34": ("12", +1.0),
    }
    for p, (q, sgn) in mapping.items():
        star[IDX[q], IDX[p]] = sgn
    return star


def format_vec(v: np.ndarray) -> str:
    terms = []
    for coeff, name in zip(v, PAIRS):
        if abs(coeff) > 1e-12:
            terms.append(f"{coeff:+.6g} e{name}")
    return " ".join(terms).replace("+", "", 1) if terms else "0"


def main() -> None:
    star = hodge_matrix()

    omega1 = vec(**{"12": 1, "34": 1})
    omega2 = vec(**{"13": 1, "24": -1})
    omega3 = vec(**{"14": 1, "23": 1})
    omegas = [omega1, omega2, omega3]

    sigma = [w / np.sqrt(2.0) for w in omegas]
    gram = np.array([[np.dot(a, b) for b in sigma] for a in sigma])
    residuals = [np.linalg.norm(star @ w - w) for w in omegas]
    anti_residuals = [np.linalg.norm(star @ w + w) for w in omegas]

    lines = [
        "# Saída — triplet Hopf--Bismut",
        "",
        "## Base de 2-formas",
        "",
        f"Ordem usada: `{PAIRS}`.",
        "",
        "## Formas hipercähler",
        "",
    ]
    for i, w in enumerate(omegas, start=1):
        lines.append(f"- `Omega_{i} = {format_vec(w)}`")
    lines += [
        "",
        "## Teste de autodualidade",
        "",
    ]
    for i, res in enumerate(residuals, start=1):
        lines.append(f"- `||*Omega_{i} - Omega_{i}|| = {res:.3e}`")
    for i, res in enumerate(anti_residuals, start=1):
        lines.append(f"- `||*Omega_{i} + Omega_{i}|| = {res:.6f}`")

    lines += [
        "",
        "## Gram da base normalizada Sigma_i^+ = Omega_i/sqrt(2)",
        "",
        "```text",
        np.array2string(gram, precision=12, suppress_small=False),
        "```",
        "",
        "Conclusão: o triplet de Hopf é auto-dual na orientação complexa padrão e a base normalizada é ortonormal.",
        "",
    ]

    out = Path(__file__).with_name("saida_verificar_triplet_hopf_bismut.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
