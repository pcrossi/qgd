#!/usr/bin/env python3
"""Q51 — diagnóstico espectral do projetor alfa.

Classificação:
    - diagnóstico matemático;
    - não previsão;
    - converte p_req em ângulo espectral e em razão gap/largura para orientar
      a construção de K_partial^phys.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark_alpha_q51.py"
OUT = HERE / "saida_diagnostico_espectral_projetor_q51.md"

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
    lines.append("# Saída — diagnóstico espectral do projetor Q51\n\n")
    lines.append("Classificação: diagnóstico matemático, não previsão.\n\n")
    lines.append("Partimos de:\n\n")
    lines.append("$$\n")
    lines.append("p_{\\rm req}=E_{\\partial}^{\\rm req}/E_{\\partial}^{\\rm spec}.\n")
    lines.append("$$\n\n")
    lines.append("Se $p_{\\rm req}$ é norma quadrática de projeção, então:\n\n")
    lines.append("$$\n")
    lines.append("\\sqrt{p_{\\rm req}}=\\cos\\theta_\\alpha.\n")
    lines.append("$$\n\n")
    lines.append("Num modelo de janela espectral Lorentziana:\n\n")
    lines.append("$$\n")
    lines.append("p_{\\rm req}=\\frac{1}{1+(\\Delta/\\Gamma)^2}.\n")
    lines.append("$$\n\n")
    lines.append("| Núcleo | p_req | theta_alpha (graus) | Delta/Gamma |\n")
    lines.append("| --- | ---: | ---: | ---: |\n")

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
        p_req = min(max(p_req, 0.0), 1.0)
        theta = math.degrees(math.acos(math.sqrt(p_req)))
        if p_req == 0.0:
            gap_ratio = float("inf")
        else:
            gap_ratio = math.sqrt(1.0 / p_req - 1.0)
        gap_text = "inf" if math.isinf(gap_ratio) else f"{gap_ratio:.6f}"
        lines.append(f"| {c.name} | {p_req:.6f} | {theta:.6f} | {gap_text} |\n")

    lines.append("\n")
    lines.append("## Interpretação\n\n")
    lines.append(
        "Casos com $p\\simeq0$ exigem que o modo $4N$ esteja quase ortogonal "
        "à janela alfa selecionada. Casos com $p\\simeq1$ exigem alinhamento "
        "quase completo. Valores intermediários correspondem a mistura "
        "espectral parcial.\n\n"
    )
    lines.append(
        "Isso define o que o operador $K_\\partial^{\\rm phys}$ precisa "
        "produzir: separações espectrais distintas por núcleo, não uma "
        "constante universal.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
