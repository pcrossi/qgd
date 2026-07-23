#!/usr/bin/env python3
"""Utilitários numéricos para projetores espectrais da Q51.

Classificação:
    - infraestrutura numérica;
    - não contém dados físicos;
    - pode ser reutilizada quando K_partial^phys real estiver disponível.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import numpy as np


OUT = Path(__file__).resolve().parent / "saida_riesz_projector_utils_q51.md"


@dataclass(frozen=True)
class Window:
    center: float
    radius: float


def spectral_projector(K: np.ndarray, window: Window) -> np.ndarray:
    """Orthogonal spectral projector for Hermitian/symmetric K.

    This is the finite-dimensional equivalent of the Riesz projector.
    """
    vals, vecs = np.linalg.eigh(K)
    mask = np.abs(vals - window.center) <= window.radius
    if not np.any(mask):
        return np.zeros_like(K)
    V = vecs[:, mask]
    return V @ V.T


def schur_boundary(K_II: np.ndarray, K_Ib: np.ndarray, K_bb: np.ndarray) -> np.ndarray:
    """Compute K_bb - K_bI K_II^{-1} K_Ib."""
    return K_bb - K_Ib.T @ np.linalg.solve(K_II, K_Ib)


def projection_weight(P: np.ndarray, vector: np.ndarray) -> float:
    projected = P @ vector
    denom = float(vector @ vector)
    if denom == 0.0:
        return 0.0
    return float(projected @ projected) / denom


def demo() -> str:
    # Fixture only: verifies projector algebra.
    p = 0.63
    v_alpha = np.array([np.sqrt(p), np.sqrt(1.0 - p), 0.0])
    v_orth = np.array([np.sqrt(1.0 - p), -np.sqrt(p), 0.0])
    v_res = np.array([0.0, 0.0, 1.0])
    V = np.column_stack([v_alpha, v_orth, v_res])
    K = V @ np.diag([0.0, 1.0, 3.0]) @ V.T
    P = spectral_projector(K, Window(center=0.0, radius=0.1))
    e0 = np.array([1.0, 0.0, 0.0])
    w = projection_weight(P, e0)

    lines = []
    lines.append("# Saída — utilitários de projetor de Riesz Q51\n\n")
    lines.append("Classificação: infraestrutura numérica / fixture algébrico.\n\n")
    lines.append(f"- peso-alvo do fixture = `{p:.6f}`\n")
    lines.append(f"- peso recuperado = `{w:.6f}`\n")
    lines.append(f"- erro absoluto = `{abs(w-p):.6e}`\n\n")
    lines.append("Funções disponíveis:\n\n")
    lines.append("1. `spectral_projector(K, Window)`;\n")
    lines.append("2. `schur_boundary(K_II, K_Ib, K_bb)`;\n")
    lines.append("3. `projection_weight(P, vector)`.\n")
    return "".join(lines)


def main() -> None:
    report = demo()
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

