#!/usr/bin/env python3
"""GDQ — Capítulo 17 / Liberdade transversal remanescente de Noether."""

from __future__ import annotations

from pathlib import Path

import numpy as np


def spin_norm(c_s: complex, c_t: complex) -> float:
    return 2.0 * abs(c_s) ** 2 + 6.0 * abs(c_t) ** 2


def main() -> None:
    c_s = 0.8 - 0.3j
    c_t = -0.2 + 0.5j
    lam = 1.7 * np.exp(0.4j)
    before = spin_norm(c_s, c_t)
    after = spin_norm(lam * c_s, lam * c_t)
    predicted = abs(lam) ** 2
    residual = abs(after / before - predicted)
    charges = np.array([0, 1, -1, 0])

    lines = [
        "# Saída — liberdade residual de Noether no beta",
        "",
        "Classificação: teste algébrico de consistência; não é modelo físico.",
        "",
        f"- soma das cargas externas: `{charges.sum()}`",
        f"- fator previsto na taxa por escala complexa: `{predicted:.12f}`",
        f"- fator calculado na taxa: `{after / before:.12f}`",
        f"- resíduo: `{residual:.3e}`",
        "",
        "Conclusão: conservação de carga e isotropia não fixam a normalização transversal dos coeficientes.",
        "",
    ]
    out = Path(__file__).with_name("saida_verificar_liberdade_noether_beta.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
