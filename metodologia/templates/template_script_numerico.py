#!/usr/bin/env python3
"""Template numérico GDQ.

Copiar este arquivo para a pasta da questão e preencher os blocos marcados.
Todo script deve gerar uma saída Markdown auditável.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Params:
    # Parâmetros universais ou normalizados.
    hbar: float = 1.0

    # Parâmetros de aparelho/contorno.
    app_strength: float = 0.0

    # Parâmetros numéricos.
    n: int = 1000


def build_domain(p: Params):
    """Construir domínio/malha."""
    x = np.linspace(-1.0, 1.0, p.n)
    return x


def build_operator(p: Params, x: np.ndarray):
    """Montar operador K ou K_phys."""
    # Exemplo: Laplaciano 1D com Dirichlet simples.
    dx = x[1] - x[0]
    main = 2.0 * np.ones(p.n)
    off = -1.0 * np.ones(p.n - 1)
    k = (np.diag(main) + np.diag(off, 1) + np.diag(off, -1)) / dx**2
    return k


def build_source(p: Params, x: np.ndarray):
    """Montar fonte clássica J_app."""
    return p.app_strength * np.exp(-x**2 / 0.1)


def solve_response(k: np.ndarray, j: np.ndarray):
    """Resolver deltaPhi = K^{-1}J."""
    # Regularização mínima para template; trocar por solver adequado.
    return np.linalg.solve(k + 1e-12 * np.eye(k.shape[0]), j)


def extract_observable(p: Params, x: np.ndarray, response: np.ndarray):
    """Extrair observável."""
    return float(np.trapezoid(response**2, x))


def run(p: Params):
    x = build_domain(p)
    k = build_operator(p, x)
    j = build_source(p, x)
    response = solve_response(k, j)
    obs = extract_observable(p, x, response)
    return {
        "n": p.n,
        "app_strength": p.app_strength,
        "observable": obs,
    }


def main() -> None:
    rows = [run(Params(n=n, app_strength=1.0)) for n in (500, 1000, 2000)]

    lines = []
    lines.append("# Saída numérica GDQ\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Definir: cálculo direto, teste de convergência, comparação, etc.\n\n")
    lines.append("## Resultados\n\n")
    lines.append("| N | app_strength | observável |\n")
    lines.append("|---:|---:|---:|\n")
    for r in rows:
        lines.append(f"| {r['n']} | {r['app_strength']:.6g} | {r['observable']:.12g} |\n")

    (OUT / "saida_template.md").write_text("".join(lines), encoding="utf-8")
    print(OUT / "saida_template.md")


if __name__ == "__main__":
    main()
