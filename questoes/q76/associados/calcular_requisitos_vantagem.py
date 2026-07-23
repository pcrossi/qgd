#!/usr/bin/env python3
"""Q76 — requisitos invertidos para vantagem GDQ em qubits.

Classificação:
    ferramenta de engenharia reduzida / requisitos de fechamento.

Entrada:
    fidelidade alvo e tempo de porta.

Saída:
    requisitos mínimos sobre:
        - J/Delta;
        - T1;
        - T2;
        - f_gap para adiabaticidade;
        - erro angular de contorno;
        - readout.

Isso não prova hardware GDQ. Ele define o alvo quantitativo que a Hessiana e
os contornos reais precisam satisfazer.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


ROOT = Path(__file__).resolve().parent
OUT = ROOT / "saida_calcular_requisitos_vantagem.md"


@dataclass(frozen=True)
class Target:
    name: str
    fidelity: float
    gate_ns: float


@dataclass(frozen=True)
class Budget:
    leak: float = 0.20
    t1: float = 0.15
    t2: float = 0.20
    nonad: float = 0.15
    axis: float = 0.10
    readout: float = 0.20

    def total(self) -> float:
        return self.leak + self.t1 + self.t2 + self.nonad + self.axis + self.readout


def reqs(target: Target, budget: Budget) -> dict[str, float]:
    eps = 1.0 - target.fidelity
    t_gate_s = target.gate_ns * 1e-9
    j_over_delta = math.sqrt(budget.leak * eps)
    t1_s = t_gate_s / (budget.t1 * eps)
    t2_s = t_gate_s / (budget.t2 * eps)
    f_gap_hz = 1.0 / (2.0 * math.pi * t_gate_s * math.sqrt(budget.nonad * eps))
    axis_rad = math.sqrt(6.0 * budget.axis * eps)
    readout = budget.readout * eps
    return {
        "eps": eps,
        "j_over_delta": j_over_delta,
        "t1_s": t1_s,
        "t2_s": t2_s,
        "f_gap_hz": f_gap_hz,
        "axis_rad": axis_rad,
        "readout": readout,
    }


def main() -> None:
    budget = Budget()
    if abs(budget.total() - 1.0) > 1e-12:
        raise RuntimeError("error budget weights must sum to one")

    targets = [
        Target("NISQ_bom_99p9", 0.999, 50.0),
        Target("fault_tolerance_99p99", 0.9999, 50.0),
        Target("alto_99p999", 0.99999, 50.0),
        Target("ultra_99p9999", 0.999999, 50.0),
        Target("porta_rapida_99p99", 0.9999, 5.0),
    ]

    lines = [
        "# Saída — Q76 requisitos para vantagem GDQ",
        "",
        "Classificação: ferramenta de engenharia reduzida / requisitos de fechamento.",
        "",
        "Orçamento de erro usado:",
        "",
        "| canal | peso |",
        "|---|---:|",
        f"| vazamento | {budget.leak:.2f} |",
        f"| T1 | {budget.t1:.2f} |",
        f"| T2 | {budget.t2:.2f} |",
        f"| não adiabático | {budget.nonad:.2f} |",
        f"| eixo/contorno | {budget.axis:.2f} |",
        f"| readout | {budget.readout:.2f} |",
        "",
        "## Requisitos",
        "",
        "| alvo | gate ns | erro alvo | max J/Delta | min T1 | min T2 | min f_gap | max eixo mrad | max readout |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for t in targets:
        r = reqs(t, budget)
        lines.append(
            f"| {t.name} | {t.gate_ns:.3g} | {r['eps']:.1e} | "
            f"{r['j_over_delta']:.3e} | {r['t1_s']*1e6:.3f} us | "
            f"{r['t2_s']*1e6:.3f} us | {r['f_gap_hz']/1e9:.3f} GHz | "
            f"{r['axis_rad']*1e3:.3f} | {r['readout']:.3e} |"
        )

    lines += [
        "",
        "## Leitura GDQ",
        "",
        "Esses requisitos são os alvos que a construção GDQ precisa atingir pela",
        "Hessiana e pelo contorno:",
        "",
        "$$",
        "K_{\\rm phys}",
        "\\to",
        "\\Delta_{\\rm gap},",
        "\\qquad",
        "P_\\perp\\delta K P_Q",
        "\\to",
        "J,",
        "\\qquad",
        "\\mathsf R_{\\rm app}",
        "\\to",
        "p_{\\rm read}.",
        "$$",
        "",
        "Se a GDQ reduzir $J/\\Delta$ e melhorar $T_1,T_2$ sem piorar readout, ela",
        "pode reduzir overhead. Se não conseguir, fica apenas como reinterpretação",
        "geométrica do qubit operacional.",
        "",
        "$$",
        "\\boxed{",
        "\\text{a próxima prova física da Q76 é calcular esses requisitos, não postulá-los.}",
        "}",
        "$$",
        "",
    ]

    OUT.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()

