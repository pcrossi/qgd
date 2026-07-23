#!/usr/bin/env python3
"""Fluxo espectral do protótipo APS U(1) da Q28."""

from __future__ import annotations

import argparse
import importlib.util
from pathlib import Path

import numpy as np


def load_eta_module():
    path = Path(__file__).with_name("test_eta_s3_hopf.py")
    spec = importlib.util.spec_from_file_location("eta_s3", path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def crossings(charge: int, beta_final: float, two_j_max: int) -> list[tuple[float, int, str]]:
    eta = load_eta_module()
    initial = eta.spectrum(two_j_max, float(charge), 0.0, 1.0)
    unique, counts = np.unique(np.round(initial, 12), return_counts=True)
    result: list[tuple[float, int, str]] = []
    low, high = sorted((0.0, beta_final))
    for value, multiplicity in zip(unique, counts):
        beta_cross = -float(value)
        if low < beta_cross < high:
            direction = "positivo→negativo" if beta_final < 0 else "negativo→positivo"
            result.append((beta_cross, int(multiplicity), direction))
    return sorted(result)


def render(charge: int, beta_final: float, two_j_max: int) -> str:
    eta = load_eta_module()
    events = crossings(charge, beta_final, two_j_max)
    final_values = eta.spectrum(two_j_max, float(charge), beta_final, 1.0)
    kernel = int(np.count_nonzero(np.abs(final_values) < 1.0e-10))
    sf = 0
    for _, multiplicity, direction in events:
        sf += multiplicity if direction == "negativo→positivo" else -multiplicity
    index_initial = 0
    index_final = index_initial - sf

    lines = [
        "# Q28 — Fluxo espectral do protótipo $U(1)$",
        "",
        f"- carga de Hopf: $m={charge}$;",
        f"- deslocamento final: $\\beta={beta_final:g}$;",
        f"- cutoff: $2j_{{\\max}}={two_j_max}$.",
        "",
        "| $\\beta$ do cruzamento | multiplicidade | direção |",
        "|---:|---:|:---|",
    ]
    for beta, multiplicity, direction in events:
        lines.append(f"| {beta:.12f} | {multiplicity} | {direction} |")
    if not events:
        lines.append("| — | 0 | nenhum cruzamento interior |")

    lines += [
        "",
        "## Resultado",
        "",
        f"- fluxo espectral assinado: ${sf}$;",
        f"- dimensão do kernel no endpoint: $h={kernel}$;",
        f"- índice APS inicial: ${index_initial}$;",
        f"- índice APS final: ${index_final}$.",
        "",
        "A convenção conta cruzamentos negativo→positivo como positivos e usa",
        "$\\Delta\\operatorname{ind}_{\\rm APS}=-\\operatorname{SF}$.",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--charge", type=int, default=1)
    parser.add_argument("--beta-final", type=float, default=-1.5)
    parser.add_argument("--two-j-max", type=int, default=30)
    parser.add_argument(
        "--output",
        type=Path,
        default=Path(__file__).with_name("resultado_fluxo_espectral_u1.md"),
    )
    args = parser.parse_args()
    report = render(args.charge, args.beta_final, args.two_j_max)
    args.output.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
