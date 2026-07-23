#!/usr/bin/env python3
"""
GDQ — Capítulo 14 / Seleção do junction N=3

Objetivo:
    Verificar o argumento reduzido de seleção:
        - N=2 fecha apenas colinearmente;
        - N=3 é o primeiro fechamento não colinear isolado;
        - N>3 possui N-3 modos internos nulos no modelo horizontal reduzido.

Classificação:
    Teste de consistência da prova de seleção. Não substitui a ação oficial.

Saída:
    scripts/saida_selecao_junction_N.md
"""

from __future__ import annotations

from pathlib import Path

import numpy as np


def closure_hessian_spectrum(n: int) -> np.ndarray:
    """Return eigenvalues of H = (D C)^T(D C) at equally spaced closure."""

    angles = 2.0 * np.pi * np.arange(n) / float(n)
    d_constraint = np.vstack((-np.sin(angles), np.cos(angles)))
    return np.linalg.eigvalsh(d_constraint.T @ d_constraint)


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_selecao_junction_N.md"

    rows = []
    for n in range(2, 9):
        eig = closure_hessian_spectrum(n)
        zero_modes = int(np.sum(np.abs(eig) < 1.0e-10))
        # One zero is the common rotation. Additional zeros are internal.
        internal_zeros = max(0, zero_modes - 1)
        nonzero = [x for x in eig if x > 1.0e-10]
        rows.append((n, zero_modes, internal_zeros, nonzero))

    table = "\n".join(
        f"| {n} | {zero_modes} | {internal_zeros} | "
        f"{', '.join(f'{x:.6f}' for x in nonzero)} |"
        for n, zero_modes, internal_zeros, nonzero in rows
    )

    text = f"""# Saída — seleção do junction N

Classificação: teste de consistência da prova de seleção.

| N | modos zero totais | zeros internos além da rotação | autovalores não nulos |
|---:|---:|---:|---|
{table}

Interpretação: $N=3$ é o primeiro fechamento não colinear isolado. Para
$N>3$, aparecem $N-3$ modos internos nulos além da rotação global. Isso
implementa a condição usada no texto: fechamento, não colinearidade e
isolamento selecionam $N=3$.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
