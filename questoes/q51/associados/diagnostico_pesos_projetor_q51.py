#!/usr/bin/env python3
"""Q51 — diagnóstico dos pesos requeridos do projetor P_perp."""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark_alpha_q51.py"
OUT = HERE / "saida_diagnostico_pesos_projetor_q51.md"

J0 = 1.712091781054
J1 = 1.341454657186
J2 = 1.063840998206


def load_benchmark():
    spec = importlib.util.spec_from_file_location("q51_benchmark", BENCH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def impedance_q40_base(x: float) -> float:
    return (
        J0 * J0 * x * x / (1.0 + x)
        + J1 * J1 * x * x / (1.0 + x) ** 2
        + J2 * J2 * x ** 3 / (1.0 + x) ** 2
    )


def main() -> None:
    q = load_benchmark()
    scale = 4.0 / q.ALPHA

    lines = []
    lines.append("# Saída — pesos requeridos do projetor Q51\n\n")
    lines.append("Classificação: diagnóstico inverso, não previsão.\n\n")
    lines.append("Define:\n\n")
    lines.append("$$\n")
    lines.append("p_{\\rm req}=E_{\\partial}^{\\rm req}/E_{\\partial}^{\\rm spec}.\n")
    lines.append("$$\n\n")
    lines.append("| Núcleo | E_req | E_spec | p_req | sqrt(p_req) | Status |\n")
    lines.append("| --- | ---: | ---: | ---: | ---: | --- |\n")

    all_in_range = True
    for c in q.CASES:
        radius_touch = q.nuclear_radius_fm(c.A_parent)
        radius_parent = 1.20 * c.A_parent ** (1.0 / 3.0)
        x_barrier = q.coulomb_mev_fm(c.Z_parent) / (radius_touch * c.q_alpha_mev) - 1.0
        delta_touch = (radius_touch - radius_parent) / radius_parent
        chi = delta_touch * delta_touch / x_barrier
        e_spec = scale * impedance_q40_base(chi)

        w = q.action_w(c, geometric=False)
        nu = q.internal_attempt_frequency(c)
        w_req = math.log(c.half_life_s * nu / math.log(2.0))
        e_req = max(w_req - w, 0.0)
        p_req = e_req / e_spec if e_spec > 0 else 0.0
        amp = math.sqrt(max(p_req, 0.0))
        ok = 0.0 <= p_req <= 1.0
        all_in_range = all_in_range and ok
        status = "compatível com projetor" if ok else "fora do intervalo"
        lines.append(
            f"| {c.name} | {e_req:.6f} | {e_spec:.6f} | "
            f"{p_req:.6f} | {amp:.6f} | {status} |\n"
        )

    lines.append("\n")
    lines.append("Verificação global:\n\n")
    lines.append("$$\n")
    lines.append(f"0\\le p_{{\\rm req}}\\le1\\quad\\text{{para todos}} = {str(all_in_range).lower()}.\n")
    lines.append("$$\n\n")
    lines.append(
        "Interpretação: a impedância média pode ser mantida; o que falta é "
        "o projetor espectral de canal que preserva apenas a componente alfa "
        "admissível.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

