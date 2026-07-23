#!/usr/bin/env python3
"""Q76 — toy parametrizado tipo NV/NESS.

Classificação:
    estimativa parametrizada / diagnóstico físico.

Este script mostra a diferença entre dois critérios:
    1. equilíbrio térmico por Boltzmann: exp(-h f/kBT);
    2. estabilidade operacional por tempos efetivos T1/T2 em um sistema
       preparado e medido fora do equilíbrio (NESS).

Leitura GDQ:
    - T1/T2 efetivos devem vir futuramente de K_phys, R_bath e R_app;
    - aqui eles são parâmetros de aparelho, não previsão da ação oficial.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "saida_estimar_nv_ness_parametrico.md"

KB_OVER_H_GHZ_PER_K = 20.836619123


@dataclass(frozen=True)
class NVScenario:
    name: str
    f_gap_ghz: float
    temperature_k: float
    t_op_us: float
    t1_ms: float
    t2_us: float
    j_over_delta: float
    eps_nonad: float
    eps_read: float


def calc(s: NVScenario) -> dict[str, float]:
    beta = s.f_gap_ghz / (KB_OVER_H_GHZ_PER_K * s.temperature_k)
    boltz_exc = math.exp(-beta)
    # Polarização térmica de dois níveis: tanh(beta/2). Pequena se beta << 1.
    thermal_pol = math.tanh(beta / 2.0)
    t_op_s = s.t_op_us * 1e-6
    t1_s = s.t1_ms * 1e-3
    t2_s = s.t2_us * 1e-6
    eps_t1 = 1.0 - math.exp(-t_op_s / t1_s)
    eps_t2 = 1.0 - math.exp(-t_op_s / t2_s)
    eps_leak = s.j_over_delta**2
    eps_total = eps_t1 + eps_t2 + eps_leak + s.eps_nonad + s.eps_read
    return {
        "beta": beta,
        "boltz_exc": boltz_exc,
        "thermal_pol": thermal_pol,
        "eps_t1": eps_t1,
        "eps_t2": eps_t2,
        "eps_leak": eps_leak,
        "eps_total": eps_total,
        "fidelity": max(0.0, 1.0 - eps_total),
    }


def main() -> None:
    scenarios = [
        NVScenario(
            name="NV_room_temp_fast_gate",
            f_gap_ghz=2.87,
            temperature_k=300.0,
            t_op_us=0.05,
            t1_ms=5.0,
            t2_us=500.0,
            j_over_delta=0.003,
            eps_nonad=1.0e-4,
            eps_read=2.0e-2,
        ),
        NVScenario(
            name="NV_room_temp_improved_readout",
            f_gap_ghz=2.87,
            temperature_k=300.0,
            t_op_us=0.05,
            t1_ms=5.0,
            t2_us=500.0,
            j_over_delta=0.003,
            eps_nonad=1.0e-4,
            eps_read=1.0e-3,
        ),
        NVScenario(
            name="NV_cryo_long_coherence",
            f_gap_ghz=2.87,
            temperature_k=4.0,
            t_op_us=0.05,
            t1_ms=1000.0,
            t2_us=10_000.0,
            j_over_delta=0.001,
            eps_nonad=1.0e-5,
            eps_read=1.0e-3,
        ),
        NVScenario(
            name="GDQ_hypothetical_topological_suppression",
            f_gap_ghz=2.87,
            temperature_k=300.0,
            t_op_us=0.05,
            t1_ms=1000.0,
            t2_us=100_000.0,
            j_over_delta=1.0e-4,
            eps_nonad=1.0e-6,
            eps_read=1.0e-4,
        ),
    ]

    lines = [
        "# Saída — Q76 toy tipo NV/NESS",
        "",
        "Classificação: estimativa parametrizada / diagnóstico físico.",
        "",
        "O ponto do cálculo é separar equilíbrio térmico de estabilidade",
        "operacional fora do equilíbrio. Em temperatura ambiente, um gap de GHz",
        "não polariza termicamente o qubit; a estabilidade exige acoplamento fraco",
        "ao banho, preparação ativa e readout controlado.",
        "",
        "## Cenários",
        "",
        "| cenário | f_gap GHz | T K | beta=hf/kBT | polarização térmica tanh(beta/2) | t_op us | T1 ms | T2 us | leak | eps_T1 | eps_T2 | nonad | readout | erro op total | fidelidade op |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for s in scenarios:
        r = calc(s)
        lines.append(
            f"| {s.name} | {s.f_gap_ghz:.3g} | {s.temperature_k:.3g} | "
            f"{r['beta']:.6e} | {r['thermal_pol']:.6e} | {s.t_op_us:.3g} | "
            f"{s.t1_ms:.3g} | {s.t2_us:.3g} | {r['eps_leak']:.3e} | "
            f"{r['eps_t1']:.3e} | {r['eps_t2']:.3e} | {s.eps_nonad:.3e} | "
            f"{s.eps_read:.3e} | {r['eps_total']:.3e} | {r['fidelity']:.9f} |"
        )

    lines += [
        "",
        "## Interpretação",
        "",
        "1. Para $f_{\\rm gap}=2.87\\,{\\rm GHz}$ e $T=300\\,{\\rm K}$,",
        "   $\\beta=hf/k_BT\\simeq4.59\\times10^{-4}$, então a polarização térmica",
        "   de equilíbrio é praticamente nula.",
        "2. Se o qubit funciona nesse regime, ele não funciona porque",
        "   $hf\\gg k_BT$; ele funciona porque é preparado, controlado e lido fora",
        "   do equilíbrio térmico simples.",
        "3. A versão GDQ da melhora possível é reduzir $J_{\\rm th}^{\\rm eff}$ e",
        "   aumentar $T_1,T_2$ por geometria/contorno, além de melhorar",
        "   $\\mathsf R_{\\rm app}$ no readout.",
        "",
        "$$",
        "\\boxed{",
        "\\text{limitação física: gap de GHz em 300 K não basta; é preciso NESS e acoplamento térmico efetivo fraco.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

