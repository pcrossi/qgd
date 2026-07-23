#!/usr/bin/env python3
"""Q51 — primeira aproximação espectral de R_partial^GDQ.

Classificação:
    - teste de consistência;
    - não é previsão final;
    - reaproveita a base variacional de superfície da Q40 e troca a variável
      de sonda por um mismatch geométrico do canal alfa.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark_alpha_q51.py"
OUT = HERE / "saida_aproximacao_espectral_Rpartial_q51.md"

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
    lines.append("# Saída — aproximação espectral de R_partial Q51\n\n")
    lines.append("Classificação: teste de consistência, não previsão final.\n\n")
    lines.append("Base herdada da Q40:\n\n")
    lines.append("$$\n")
    lines.append(
        "\\mathcal I_\\Sigma(x)=\n"
        "j_0^2\\frac{x^2}{1+x}\n"
        "+j_1^2\\frac{x^2}{(1+x)^2}\n"
        "+j_2^2\\frac{x^3}{(1+x)^2}\n"
    )
    lines.append("$$\n\n")
    lines.append("com:\n\n")
    lines.append("$$\n")
    lines.append(f"j_0={J0:.12f},\\quad j_1={J1:.12f},\\quad j_2={J2:.12f}.\n")
    lines.append("$$\n\n")
    lines.append("Variável de canal alfa testada:\n\n")
    lines.append("$$\n")
    lines.append("\\chi_{\\rm curv}=\\frac{\\delta_{\\rm touch}^2}{x_{\\rm barrier}}.\n")
    lines.append("$$\n\n")
    lines.append("Escala geométrica testada:\n\n")
    lines.append("$$\n")
    lines.append("E_{\\partial}^{\\rm spec}=\\frac{4}{\\alpha}\\mathcal I_\\Sigma(\\chi_{\\rm curv}).\n")
    lines.append("$$\n\n")
    lines.append(
        "O fator 4 representa os quatro nucleons do cluster alfa; "
        "1/alpha representa a complacência eletrogeométrica global. "
        "Esta é uma hipótese reduzida de escala, não fechamento.\n\n"
    )
    lines.append("| Núcleo | E_req | chi_curv | E_spec | Diferença |\n")
    lines.append("| --- | ---: | ---: | ---: | ---: |\n")

    sq = []
    sq_pos = []
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
        diff = e_spec - e_req
        sq.append(diff * diff)
        if e_req > 0:
            sq_pos.append(diff * diff)
        lines.append(f"| {c.name} | {e_req:.6f} | {chi:.6f} | {e_spec:.6f} | {diff:.6f} |\n")

    rms_all = math.sqrt(sum(sq) / len(sq))
    rms_pos = math.sqrt(sum(sq_pos) / len(sq_pos))
    lines.append("\n")
    lines.append(f"- RMS total = `{rms_all:.6f}`\n")
    lines.append(f"- RMS nos casos positivos = `{rms_pos:.6f}`\n\n")
    lines.append("## Veredito\n\n")
    lines.append(
        "A base espectral herdada da Q40 acerta a escala de alguns actinídeos, "
        "mas falha como previsão universal: gera energia positiva onde o "
        "diagnóstico pede quase zero e superestima Po-212.\n\n"
    )
    lines.append(
        "Conclusão: é necessário o projetor físico de canal `P_perp` e o "
        "espectro real de camada/superfície. A impedância média não basta.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

