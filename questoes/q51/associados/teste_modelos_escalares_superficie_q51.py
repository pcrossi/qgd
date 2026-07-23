#!/usr/bin/env python3
"""Q51 — teste de modelos escalares simples para a energia de superfície.

Classificação:
    - teste de consistência / engenharia inversa diagnóstica;
    - os coeficientes ajustados aqui NÃO são parâmetros da GDQ;
    - objetivo: verificar se um escalar simples de geometria de superfície
      poderia substituir o operador Schur/DtN completo.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path

import numpy as np


HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark_alpha_q51.py"
OUT = HERE / "saida_teste_modelos_escalares_superficie_q51.md"


def load_benchmark():
    spec = importlib.util.spec_from_file_location("q51_benchmark", BENCH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def fit_linear(X: np.ndarray, y: np.ndarray):
    beta, *_ = np.linalg.lstsq(X, y, rcond=None)
    pred = X @ beta
    rms = float(np.sqrt(np.mean((pred - y) ** 2)))
    return beta, pred, rms


def main() -> None:
    q = load_benchmark()

    rows = []
    for c in q.CASES:
        w = q.action_w(c, geometric=False)
        nu = q.internal_attempt_frequency(c)
        w_req = math.log(c.half_life_s * nu / math.log(2.0))
        delta_w = w_req - w
        e_req = max(delta_w, 0.0)
        radius_parent = 1.20 * c.A_parent ** (1.0 / 3.0)
        radius_touch = q.nuclear_radius_fm(c.A_parent)
        delta_touch = (radius_touch - radius_parent) / radius_parent
        x_barrier = q.coulomb_mev_fm(c.Z_parent) / (radius_touch * c.q_alpha_mev) - 1.0
        curvature_softness = delta_touch * delta_touch / x_barrier
        fissility = (c.Z_parent ** 2) / c.A_parent
        daughter_magic_pb208 = 1.0 if (c.A_parent - 4 == 208 and c.Z_parent - 2 == 82) else 0.0
        rows.append(
            {
                "name": c.name,
                "e_req": e_req,
                "delta_touch": delta_touch,
                "x_barrier": x_barrier,
                "curvature_softness": curvature_softness,
                "fissility": fissility,
                "magic": daughter_magic_pb208,
            }
        )

    y = np.array([r["e_req"] for r in rows], dtype=float)
    one = np.ones_like(y)
    curv = np.array([r["curvature_softness"] for r in rows])
    fiss = np.array([r["fissility"] for r in rows])
    magic = np.array([r["magic"] for r in rows])

    models = {
        "constante": np.column_stack([one]),
        "curvatura": np.column_stack([one, curv]),
        "curvatura+fissilidade": np.column_stack([one, curv, fiss]),
        "curvatura+magic": np.column_stack([one, curv, magic]),
        "curvatura+fissilidade+magic": np.column_stack([one, curv, fiss, magic]),
    }

    results = {}
    for name, X in models.items():
        beta, pred, rms = fit_linear(X, y)
        results[name] = (beta, pred, rms)

    lines = []
    lines.append("# Saída — teste de modelos escalares de superfície Q51\n\n")
    lines.append("Classificação: engenharia inversa diagnóstica, não previsão.\n\n")
    lines.append(
        "Objetivo: verificar se a energia de superfície requerida poderia ser "
        "representada por poucos escalares geométricos simples. Se isso falhar "
        "ou depender de indicador de camada, o operador Schur/DtN completo é "
        "necessário.\n\n"
    )
    lines.append("| Núcleo | E_req | delta_touch | x_barrier | chi_curv=delta^2/x | Z^2/A | magic208 |\n")
    lines.append("| --- | ---: | ---: | ---: | ---: | ---: | ---: |\n")
    for r in rows:
        lines.append(
            f"| {r['name']} | {r['e_req']:.6f} | {r['delta_touch']:.6f} | "
            f"{r['x_barrier']:.6f} | {r['curvature_softness']:.6f} | "
            f"{r['fissility']:.6f} | {r['magic']:.0f} |\n"
        )

    lines.append("\n")
    lines.append("| Modelo diagnóstico | RMS em E_req | Coeficientes |\n")
    lines.append("| --- | ---: | --- |\n")
    for name, (beta, _pred, rms) in results.items():
        coeff = ", ".join(f"{b:.6g}" for b in beta)
        lines.append(f"| {name} | {rms:.6f} | `{coeff}` |\n")

    lines.append("\n")
    lines.append("## Veredito\n\n")
    lines.append(
        "Modelos escalares globais são diagnósticos, não derivação. A presença "
        "do indicador `magic208` melhora a descrição apenas porque codifica "
        "informação estrutural de camada. Na GDQ essa informação não deve ser "
        "inserida como etiqueta; ela deve emergir do espectro de "
        "`R_partial^GDQ`.\n\n"
    )
    lines.append(
        "Portanto, a rota correta permanece calcular o operador de superfície "
        "e seu projetor físico, não ajustar escalares.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

