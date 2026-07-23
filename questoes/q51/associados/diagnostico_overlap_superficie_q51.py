#!/usr/bin/env python3
"""Q51 — diagnóstico do overlap/preformação alfa de superfície.

Classificação:
    - diagnóstico inverso de escala;
    - NÃO é previsão;
    - NÃO ajusta parâmetro para reproduzir dados;
    - calcula o termo de superfície que a Hessiana GDQ deve produzir.
"""

from __future__ import annotations

import importlib.util
import math
import sys
from pathlib import Path


HERE = Path(__file__).resolve().parent
BENCH = HERE / "benchmark_alpha_q51.py"
OUT = HERE / "saida_diagnostico_overlap_superficie_q51.md"


def load_benchmark():
    spec = importlib.util.spec_from_file_location("q51_benchmark", BENCH)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    assert spec.loader is not None
    spec.loader.exec_module(module)
    return module


def main() -> None:
    q = load_benchmark()

    lines = []
    lines.append("# Saída — diagnóstico do overlap de superfície Q51\n\n")
    lines.append("Classificação: diagnóstico inverso de escala, não previsão.\n\n")
    lines.append(
        "Usa Gamow com `nu_int` como base radial e calcula o termo de "
        "superfície que falta para coincidir com o dado experimental.\n\n"
    )
    lines.append("Definições:\n\n")
    lines.append("$$\n")
    lines.append("W_{\\rm req}=\\ln\\left(T_{1/2}^{\\rm exp}\\nu_{\\rm int}/\\ln2\\right)\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("\\Delta W_{\\rm req}=W_{\\rm req}-W_{\\rm Gamow}\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("S_\\alpha^{\\rm eff}=e^{-\\Delta W_{\\rm req}}\n")
    lines.append("$$\n\n")
    lines.append("$$\n")
    lines.append("E_{\\partial}^{\\rm req}=\\max(\\Delta W_{\\rm req},0)\n")
    lines.append("$$\n\n")
    lines.append(
        "| Núcleo | Delta W_req | S_alpha_eff | E_surface_req | "
        "Classificação |\n"
    )
    lines.append("| --- | ---: | ---: | ---: | --- |\n")

    positive = []
    for c in q.CASES:
        w = q.action_w(c, geometric=False)
        nu = q.internal_attempt_frequency(c)
        w_req = math.log(c.half_life_s * nu / math.log(2.0))
        delta = w_req - w
        s_eff = math.exp(-delta)
        e_surface = max(delta, 0.0)
        if delta > 0:
            label = "overlap/preformação reduz taxa"
            positive.append(e_surface)
        else:
            label = "radial já lento; refinar raio/frequência/dados"
        lines.append(
            f"| {c.name} | {delta:.6f} | {s_eff:.6f} | "
            f"{e_surface:.6f} | {label} |\n"
        )

    if positive:
        mean_pos = sum(positive) / len(positive)
        rms_pos = math.sqrt(sum(x * x for x in positive) / len(positive))
    else:
        mean_pos = float("nan")
        rms_pos = float("nan")

    lines.append("\n")
    lines.append("Resumo dos casos com correção positiva:\n\n")
    lines.append(f"- média de `E_surface_req` = `{mean_pos:.6f}`\n")
    lines.append(f"- RMS de `E_surface_req` = `{rms_pos:.6f}`\n\n")
    lines.append("Interpretação GDQ:\n\n")
    lines.append(
        "O termo a derivar é uma energia quadrática de superfície, não uma "
        "constante universal de barreira:\n\n"
    )
    lines.append("$$\n")
    lines.append(
        "E_{\\partial}^{\\rm GDQ}[\\alpha]\n"
        "=\n"
        "\\langle P_\\perp\\Phi_{4N},"
        "\\mathsf R_{\\partial}^{\\rm GDQ}"
        "P_\\perp\\Phi_{4N}\\rangle_{\\partial}\n"
    )
    lines.append("$$\n\n")
    lines.append("com:\n\n")
    lines.append("$$\n")
    lines.append(
        "\\mathsf R_{\\partial}^{\\rm GDQ}"
        "=K_{\\partial\\partial}-K_{\\partial I}K_{II}^{-1}K_{I\\partial}.\n"
    )
    lines.append("$$\n\n")
    lines.append(
        "O próximo passo preditivo é calcular esse operador de superfície no "
        "background nuclear, em vez de usar `E_surface_req` como entrada.\n"
    )

    report = "".join(lines)
    OUT.write_text(report, encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()

