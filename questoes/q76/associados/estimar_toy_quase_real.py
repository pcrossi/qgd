#!/usr/bin/env python3
"""Q76 — toy quase real de estabilidade de qubit GDQ.

Classificação:
    estimativa fenomenológica parametrizada / engenharia reduzida.

Este script estima termos de erro para cenários de qubit com parâmetros
explícitos:

    epsilon_total ~ leak + thermal + nonadiabatic + axis + dephasing + readout.

Leitura GDQ:
    - leak vem de ||J||^2/Delta_gap^2;
    - thermal vem do banho/aparelho;
    - nonadiabatic vem do transporte de contorno;
    - axis vem da imperfeição do eixo clássico;
    - dephasing/readout vêm da impedância de aparelho.

O script NÃO deriva K_phys de um dispositivo real. Ele prepara uma régua
numérica para saber quais escalas a Hessiana GDQ precisaria produzir.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "saida_estimar_toy_quase_real.md"

KB_OVER_H_GHZ_PER_K = 20.836619123  # k_B/h in GHz/K


@dataclass(frozen=True)
class Scenario:
    name: str
    f_gap_ghz: float
    temperature_k: float
    j_over_delta: float
    t_gate_ns: float
    t2_us: float
    axis_error_mrad: float
    readout_error: float


def estimate(s: Scenario) -> dict[str, float]:
    beta_gap = s.f_gap_ghz / (KB_OVER_H_GHZ_PER_K * s.temperature_k)
    eps_th = math.exp(-beta_gap) if beta_gap < 745 else 0.0
    eps_leak = s.j_over_delta**2
    t_gate_s = s.t_gate_ns * 1e-9
    f_gap_hz = s.f_gap_ghz * 1e9
    eps_nonad = (1.0 / (2.0 * math.pi * f_gap_hz * t_gate_s)) ** 2
    delta_theta = s.axis_error_mrad * 1e-3
    eps_axis = delta_theta**2 / 6.0
    t2_s = s.t2_us * 1e-6
    eps_phi = 1.0 - math.exp(-t_gate_s / t2_s)
    eps_total = eps_leak + eps_th + eps_nonad + eps_axis + eps_phi + s.readout_error
    fidelity = max(0.0, 1.0 - eps_total)
    return {
        "beta_gap": beta_gap,
        "eps_th": eps_th,
        "eps_leak": eps_leak,
        "eps_nonad": eps_nonad,
        "eps_axis": eps_axis,
        "eps_phi": eps_phi,
        "eps_read": s.readout_error,
        "eps_total": eps_total,
        "fidelity": fidelity,
    }


def main() -> None:
    scenarios = [
        Scenario(
            name="criogenico_controlado",
            f_gap_ghz=5.0,
            temperature_k=0.015,
            j_over_delta=0.010,
            t_gate_ns=40.0,
            t2_us=50.0,
            axis_error_mrad=5.0,
            readout_error=1.0e-3,
        ),
        Scenario(
            name="spin_frio_gap_maior",
            f_gap_ghz=20.0,
            temperature_k=0.100,
            j_over_delta=0.003,
            t_gate_ns=100.0,
            t2_us=1000.0,
            axis_error_mrad=2.0,
            readout_error=5.0e-4,
        ),
        Scenario(
            name="temperatura_4K_gap_alto",
            f_gap_ghz=500.0,
            temperature_k=4.0,
            j_over_delta=0.001,
            t_gate_ns=5.0,
            t2_us=100.0,
            axis_error_mrad=1.0,
            readout_error=1.0e-4,
        ),
        Scenario(
            name="ambiente_exigente_gap_THz",
            f_gap_ghz=50_000.0,
            temperature_k=300.0,
            j_over_delta=1.0e-4,
            t_gate_ns=1.0,
            t2_us=1_000_000.0,
            axis_error_mrad=0.5,
            readout_error=1.0e-5,
        ),
    ]

    lines = [
        "# Saída — Q76 toy quase real de estabilidade",
        "",
        "Classificação: estimativa fenomenológica parametrizada / engenharia reduzida.",
        "",
        "O cálculo não deriva um hardware real. Ele estima quais escalas a Hessiana",
        "GDQ teria que produzir para que o qubit geométrico fosse competitivo.",
        "",
        "## Fórmulas usadas",
        "",
        "$$",
        "\\epsilon_{\\rm leak}\\simeq\\left(\\frac{\\|J\\|}{\\Delta_{\\rm gap}}\\right)^2,",
        "\\qquad",
        "\\epsilon_{\\rm th}\\simeq e^{-hf_{\\rm gap}/k_BT},",
        "$$",
        "",
        "$$",
        "\\epsilon_{\\rm nonad}\\simeq",
        "\\left(",
        "\\frac{1}{2\\pi f_{\\rm gap}t_{\\rm gate}}",
        "\\right)^2,",
        "\\qquad",
        "\\epsilon_{\\rm axis}\\simeq\\frac{\\delta\\theta^2}{6}.",
        "$$",
        "",
        "$$",
        "\\epsilon_\\phi\\simeq1-e^{-t_{\\rm gate}/T_2}.",
        "$$",
        "",
        "## Cenários",
        "",
        "| cenário | f_gap GHz | T K | J/Delta | gate ns | T2 us | beta_gap | leak | thermal | nonad | axis | dephase | readout | erro total | fidelidade |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for s in scenarios:
        r = estimate(s)
        lines.append(
            f"| {s.name} | {s.f_gap_ghz:.3g} | {s.temperature_k:.3g} | "
            f"{s.j_over_delta:.3g} | {s.t_gate_ns:.3g} | {s.t2_us:.3g} | "
            f"{r['beta_gap']:.6g} | {r['eps_leak']:.3e} | {r['eps_th']:.3e} | "
            f"{r['eps_nonad']:.3e} | {r['eps_axis']:.3e} | {r['eps_phi']:.3e} | "
            f"{r['eps_read']:.3e} | {r['eps_total']:.3e} | {r['fidelity']:.9f} |"
        )

    lines += [
        "",
        "## Leitura dos resultados",
        "",
        "1. Em regime criogênico, o erro térmico já pode ser muito pequeno se",
        "   $hf_{\\rm gap}\\gg k_BT$; os termos dominantes passam a ser readout,",
        "   dephasing e vazamento.",
        "2. Em $4\\,{\\rm K}$, é necessário gap de centenas de GHz para tornar o termo",
        "   térmico pequeno.",
        "3. Em temperatura ambiente, a escala térmica é aproximadamente",
        "   $k_BT/h\\simeq6251\\,{\\rm GHz}$; por isso o toy exige gap em dezenas de THz",
        "   ou uma proteção topológica que reduza o acoplamento térmico efetivo.",
        "4. O caminho GDQ a testar é produzir grande $\\Delta_{\\rm gap}$ e pequeno",
        "   $J$ pela Hessiana/contorno, não declarar estabilidade absoluta.",
        "",
        "$$",
        "\\boxed{",
        "\\text{toy quase real: promissor se }\\Delta_{\\rm gap}\\text{ cresce e }J/\\Delta\\text{ cai; não prova hardware ainda.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

