#!/usr/bin/env python3
"""Q51 — pipeline numérico para taxa alfa GDQ.

Este script não fabrica a Hessiana nuclear. Ele executa a etapa algébrica
final quando os blocos reais são fornecidos em um arquivo NPZ.

Arquivo NPZ esperado:
    K_II              matriz interior
    K_Ib              acoplamento interior-bordo
    K_bb              matriz de bordo
    phi_alpha         vetor do canal alfa bruto
    phi_parent        vetor/traco do pai, opcional
    P_daughter        projetor do subespaco filho, opcional
    alpha_window_min  escalar, opcional
    alpha_window_max  escalar, opcional
    nu_gdq            escalar, opcional
    W_rad_gdq         escalar, opcional

Classificacao: infraestrutura/pipeline. Se rodado sem NPZ, executa apenas um
fixture algebraico auto-contido para validar Schur, projetor e forma
quadratica.
"""

from __future__ import annotations

import argparse
import math
from pathlib import Path

import numpy as np

from riesz_projector_utils_q51 import (
    Window,
    projection_weight,
    schur_boundary,
    spectral_projector,
)


OUT = Path(__file__).resolve().parent / "saida_calcular_taxa_alpha_gdq_q51.md"


def _as_scalar(value: np.ndarray | float, default: float) -> float:
    if value is None:
        return default
    arr = np.asarray(value)
    if arr.size == 0:
        return default
    return float(arr.reshape(-1)[0])


def _load_npz(path: Path) -> dict[str, np.ndarray]:
    with np.load(path) as data:
        return {key: data[key] for key in data.files}


def _fixture() -> dict[str, np.ndarray]:
    """Fixture positivo simples que não usa dado experimental."""
    K_II = np.diag([3.0, 5.0])
    K_Ib = np.array(
        [
            [0.20, 0.05, 0.00],
            [0.00, 0.15, 0.04],
        ],
        dtype=float,
    )
    K_bb = np.diag([0.40, 1.20, 2.50])
    phi_alpha = np.array([1.0, 0.0, 0.0], dtype=float)
    P_daughter = np.zeros((3, 3), dtype=float)
    return {
        "K_II": K_II,
        "K_Ib": K_Ib,
        "K_bb": K_bb,
        "phi_alpha": phi_alpha,
        "P_daughter": P_daughter,
        "alpha_window_min": np.array([0.0]),
        "alpha_window_max": np.array([0.8]),
        "nu_gdq": np.array([1.0e21]),
        "W_rad_gdq": np.array([80.0]),
    }


def compute(payload: dict[str, np.ndarray]) -> dict[str, float | np.ndarray]:
    K_II = np.asarray(payload["K_II"], dtype=float)
    K_Ib = np.asarray(payload["K_Ib"], dtype=float)
    K_bb = np.asarray(payload["K_bb"], dtype=float)
    phi_alpha = np.asarray(payload["phi_alpha"], dtype=float).reshape(-1)

    K_partial = schur_boundary(K_II, K_Ib, K_bb)
    eigvals = np.linalg.eigvalsh(K_partial)

    w_min = _as_scalar(payload.get("alpha_window_min"), float(eigvals[0] - 1e-9))
    w_max = _as_scalar(payload.get("alpha_window_max"), float(eigvals[0] + 1e-6))
    window_center = 0.5 * (w_min + w_max)
    window_radius = 0.5 * abs(w_max - w_min)
    P_alpha = spectral_projector(K_partial, Window(window_center, window_radius))

    P_daughter = np.asarray(
        payload.get("P_daughter", np.zeros_like(K_partial)),
        dtype=float,
    )

    P_perp = P_alpha @ (np.eye(K_partial.shape[0]) - P_daughter)
    projected = P_perp @ phi_alpha
    E_partial = float(projected.T @ K_partial @ projected)
    p_weight = projection_weight(P_perp, phi_alpha)

    nu_gdq = _as_scalar(payload.get("nu_gdq"), 1.0)
    W_rad_gdq = _as_scalar(payload.get("W_rad_gdq"), 0.0)
    gamma = nu_gdq * math.exp(-E_partial) * math.exp(-W_rad_gdq)
    half_life = math.log(2.0) / gamma if gamma > 0.0 else math.inf

    return {
        "K_partial": K_partial,
        "eigvals": eigvals,
        "P_alpha": P_alpha,
        "P_perp": P_perp,
        "E_partial": E_partial,
        "p_weight": p_weight,
        "nu_gdq": nu_gdq,
        "W_rad_gdq": W_rad_gdq,
        "Gamma_gdq": gamma,
        "T_half_gdq": half_life,
        "window_min": w_min,
        "window_max": w_max,
        "window_center": window_center,
        "window_radius": window_radius,
    }


def render(result: dict[str, float | np.ndarray], source: str) -> str:
    eigvals = np.asarray(result["eigvals"])
    lines: list[str] = []
    lines.append("# Saída — pipeline preditivo alfa GDQ Q51\n\n")
    lines.append(f"- fonte: `{source}`\n")
    lines.append("- classificação: infraestrutura algébrica/pipeline\n\n")
    lines.append("## Janela espectral\n\n")
    lines.append(f"- mínimo: `{result['window_min']:.12e}`\n")
    lines.append(f"- máximo: `{result['window_max']:.12e}`\n\n")
    lines.append(f"- centro usado pelo projetor: `{result['window_center']:.12e}`\n")
    lines.append(f"- raio usado pelo projetor: `{result['window_radius']:.12e}`\n\n")
    lines.append("## Espectro de K_partial\n\n")
    lines.append("| índice | autovalor |\n")
    lines.append("| ---: | ---: |\n")
    for idx, val in enumerate(eigvals):
        lines.append(f"| {idx} | `{val:.12e}` |\n")
    lines.append("\n")
    lines.append("## Observáveis algébricos\n\n")
    lines.append(f"- peso projetado: `{result['p_weight']:.12e}`\n")
    lines.append(f"- E_partial_GDQ: `{result['E_partial']:.12e}`\n")
    lines.append(f"- nu_GDQ: `{result['nu_gdq']:.12e}` s^-1\n")
    lines.append(f"- W_rad_GDQ: `{result['W_rad_gdq']:.12e}`\n")
    lines.append(f"- Gamma_GDQ: `{result['Gamma_gdq']:.12e}` s^-1\n")
    lines.append(f"- T_half_GDQ: `{result['T_half_gdq']:.12e}` s\n\n")
    lines.append("## Interpretação\n\n")
    if source == "fixture":
        lines.append(
            "Esta saída valida apenas a etapa algébrica Schur/Riesz/taxa. "
            "Ela não é previsão física, pois não usa a Hessiana nuclear real.\n"
        )
    else:
        lines.append(
            "Esta saída deve ser classificada conforme a origem do NPZ. Se os "
            "blocos vierem da Hessiana física GDQ com parâmetros congelados, "
            "a comparação posterior pode ser tratada como avaliação direta.\n"
        )
    return "".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--npz", type=Path, default=None)
    args = parser.parse_args()

    if args.npz is None:
        payload = _fixture()
        source = "fixture"
    else:
        payload = _load_npz(args.npz)
        source = str(args.npz)

    result = compute(payload)
    OUT.write_text(render(result, source), encoding="utf-8")
    print(OUT)


if __name__ == "__main__":
    main()
