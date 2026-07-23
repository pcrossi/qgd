#!/usr/bin/env python3
"""Q76 — avaliador autocontido de protótipo de qubit.

Classificação:
    comparação fenomenológica / protocolo de fechamento.

Este script recebe quantidades que, em um fechamento GDQ completo, deveriam
vir da Hessiana física e da impedância de contorno:

    Delta_gap_hz      -> isolamento espectral do operador K_phys;
    J_over_Delta      -> razão ||P_perp dK P_Q|| / Delta_gap;
    T1, T2            -> taxas efetivas calculadas do contorno/bath;
    f_gap_hz          -> frequência mínima de adiabaticidade;
    axis_mrad         -> erro angular efetivo de eixo de contorno;
    readout           -> erro de leitura.

Aqui usamos cenários fixos para verificar a contabilidade de erro. Não há
ajuste ao alvo experimental.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "saida_avaliar_prototipo_qubit.md"


@dataclass(frozen=True)
class Prototype:
    name: str
    gate_ns: float
    j_over_delta: float
    t1_us: float
    t2_us: float
    f_gap_ghz: float
    axis_mrad: float
    readout: float


def evaluate(p: Prototype) -> dict[str, float]:
    t_gate = p.gate_ns * 1e-9
    t1 = p.t1_us * 1e-6
    t2 = p.t2_us * 1e-6
    f_gap = p.f_gap_ghz * 1e9
    axis = p.axis_mrad * 1e-3

    eps_leak = p.j_over_delta**2
    eps_t1 = 1.0 - math.exp(-t_gate / t1)
    eps_t2 = 1.0 - math.exp(-t_gate / t2)
    eps_nonad = (1.0 / (2.0 * math.pi * f_gap * t_gate)) ** 2
    eps_axis = axis**2 / 6.0
    eps_total = eps_leak + eps_t1 + eps_t2 + eps_nonad + eps_axis + p.readout
    fidelity = max(0.0, 1.0 - eps_total)

    return {
        "leak": eps_leak,
        "t1": eps_t1,
        "t2": eps_t2,
        "nonad": eps_nonad,
        "axis": eps_axis,
        "readout": p.readout,
        "total": eps_total,
        "fidelity": fidelity,
    }


def main() -> None:
    scenarios = [
        Prototype(
            name="baseline_convencional_bom",
            gate_ns=50.0,
            j_over_delta=1.0e-2,
            t1_us=500.0,
            t2_us=300.0,
            f_gap_ghz=1.0,
            axis_mrad=10.0,
            readout=1.0e-3,
        ),
        Prototype(
            name="gdq_gap_contorno_moderado",
            gate_ns=50.0,
            j_over_delta=3.0e-3,
            t1_us=5000.0,
            t2_us=3000.0,
            f_gap_ghz=2.0,
            axis_mrad=5.0,
            readout=2.0e-4,
        ),
        Prototype(
            name="gdq_meta_forte",
            gate_ns=50.0,
            j_over_delta=5.0e-4,
            t1_us=300000.0,
            t2_us=200000.0,
            f_gap_ghz=10.0,
            axis_mrad=0.8,
            readout=2.0e-7,
        ),
    ]

    lines = [
        "# Saída — Q76 avaliador de protótipo de qubit",
        "",
        "Classificação: comparação fenomenológica / protocolo de fechamento.",
        "",
        "Os cenários são fixos. Em uma aplicação GDQ real, `J/Delta`, `T1`, `T2`,",
        "`f_gap`, erro de eixo e readout devem vir de `K_phys` e `R_app`.",
        "",
        "| cenário | leak | T1 | T2 | nonad | eixo | readout | erro total | fidelidade |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for p in scenarios:
        r = evaluate(p)
        lines.append(
            f"| {p.name} | {r['leak']:.3e} | {r['t1']:.3e} | "
            f"{r['t2']:.3e} | {r['nonad']:.3e} | {r['axis']:.3e} | "
            f"{r['readout']:.3e} | {r['total']:.3e} | {r['fidelity']:.9f} |"
        )

    lines += [
        "",
        "## Leitura",
        "",
        "O caso `baseline_convencional_bom` ilustra um qubit bom, mas ainda com",
        "readout e coerência limitantes. O caso `gdq_gap_contorno_moderado` mostra",
        "que reduzir `J/Delta` e aumentar coerência já empurra a fidelidade para",
        "a faixa `99.96%`. O caso `gdq_meta_forte` mostra o regime que seria",
        "compatível com erro `~1e-6` por porta.",
        "",
        "$$",
        "\\boxed{",
        "\\text{o fechamento real exige substituir esses números pela Hessiana e pelo contorno calculados.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
