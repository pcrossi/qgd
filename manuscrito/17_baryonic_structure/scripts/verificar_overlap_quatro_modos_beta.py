#!/usr/bin/env python3
"""GDQ — Capítulo 17 / Overlap angular de quatro modos."""

from __future__ import annotations

from pathlib import Path

import numpy as np


IDENTITY = np.eye(2, dtype=complex)
PAULI = (
    np.array([[0.0, 1.0], [1.0, 0.0]], dtype=complex),
    np.array([[0.0, -1j], [1j, 0.0]], dtype=complex),
    np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex),
)


def amplitudes() -> tuple[np.ndarray, np.ndarray]:
    scalar = np.einsum("pn,ev->pevn", IDENTITY, IDENTITY)
    torsional = sum(np.einsum("pn,ev->pevn", sigma, sigma) for sigma in PAULI)
    return scalar, torsional


def spin_averaged_inner(left: np.ndarray, right: np.ndarray) -> complex:
    return np.vdot(left, right) / 2.0


def main() -> None:
    scalar, torsional = amplitudes()
    gram = np.array(
        [
            [spin_averaged_inner(scalar, scalar), spin_averaged_inner(scalar, torsional)],
            [spin_averaged_inner(torsional, scalar), spin_averaged_inner(torsional, torsional)],
        ]
    )
    expected = np.diag([2.0, 6.0])
    residual_gram = float(np.linalg.norm(gram - expected))

    exchanged = 2.0 * np.einsum("pv,en->pevn", IDENTITY, IDENTITY) - scalar
    fierz_residual = float(np.linalg.norm(torsional - exchanged))

    lines = [
        "# Saída — overlap angular de quatro modos beta",
        "",
        "Classificação: avaliação direta da álgebra SU(2) dos quatro modos.",
        "",
        "```text",
        "S = (p† n)(e† nu)",
        "T = sum_i (p† sigma_i n)(e† sigma_i nu)",
        "```",
        "",
        "## Gram com média no spin inicial",
        "",
        "```text",
        np.array2string(gram.real, precision=12),
        "```",
        "",
        f"- resíduo contra diag(2,6): `{residual_gram:.3e}`",
        f"- resíduo de Fierz: `{fierz_residual:.3e}`",
        "",
        "Conclusão: a soma não polarizada é `2|C_S|^2 + 6|C_T|^2`; os coeficientes ainda devem vir da ação projetada.",
        "",
    ]
    out = Path(__file__).with_name("saida_verificar_overlap_quatro_modos_beta.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
