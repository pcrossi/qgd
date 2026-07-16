#!/usr/bin/env python3
r"""Varredura multiespécie da condição sem polo das Q34/Q35.

Calcula

  Pi_inf = alpha0/(3*pi) sum_f Nc_f Q_f^2 E1(m_f^2/Lambda_EM^2)

e localiza Pi_inf=1 em log10(Lambda_EM/m_e). Nenhuma escala é ajustada a
dados de running. O cenário de quarks é um benchmark externo configurável,
pois suas massas não foram derivadas no setor canônico da GDQ.
"""

from __future__ import annotations

import argparse
import math
from dataclasses import dataclass
from pathlib import Path

import numpy as np
from scipy.optimize import brentq
from scipy.special import exp1


EULER_GAMMA = 0.5772156649015329
ALPHA0 = 1.0 / 137.035999084


@dataclass(frozen=True)
class Species:
    name: str
    mass_over_me: float
    charge: float
    colors: int = 1
    provenance: str = ""

    @property
    def weight(self) -> float:
        return self.colors * self.charge**2


def leptons_gdq() -> list[Species]:
    return [
        Species("e", 1.0, -1.0, 1, "unidade metrológica"),
        Species("mu", 206.767399, -1.0, 1, "razão espectral Q39"),
        Species("tau", 3477.131776, -1.0, 1, "razão espectral Q39"),
    ]


def charged_fermion_benchmark() -> list[Species]:
    """Benchmark externo; massas de quarks são limiares ilustrativos."""
    me_mev = 0.51099895
    rows = [
        ("e", 0.51099895, -1.0, 1, "referência externa"),
        ("mu", 105.6583755, -1.0, 1, "referência externa"),
        ("tau", 1776.86, -1.0, 1, "referência externa"),
        ("u", 2.16, 2.0 / 3.0, 3, "massa de quark dependente de esquema"),
        ("d", 4.67, -1.0 / 3.0, 3, "massa de quark dependente de esquema"),
        ("s", 93.0, -1.0 / 3.0, 3, "massa de quark dependente de esquema"),
        ("c", 1270.0, 2.0 / 3.0, 3, "massa de quark dependente de esquema"),
        ("b", 4180.0, -1.0 / 3.0, 3, "massa de quark dependente de esquema"),
        ("t", 172760.0, 2.0 / 3.0, 3, "massa de quark dependente de esquema"),
    ]
    return [Species(n, m / me_mev, q, nc, p) for n, m, q, nc, p in rows]


def exp1_log(log_z: float) -> float:
    """E1(exp(log_z)) sem underflow para escalas extremamente grandes."""
    if log_z < -35.0:
        return -EULER_GAMMA - log_z + math.exp(log_z)
    if log_z > 700.0:
        return 0.0
    return float(exp1(math.exp(log_z)))


def pi_infinity(log10_lambda_over_me: float, species: list[Species], alpha0: float = ALPHA0) -> float:
    log_lambda = log10_lambda_over_me * math.log(10.0)
    total = 0.0
    for item in species:
        log_z = 2.0 * math.log(item.mass_over_me) - 2.0 * log_lambda
        total += item.weight * exp1_log(log_z)
    return alpha0 * total / (3.0 * math.pi)


def critical_scale(species: list[Species], low: float = -3.0, high: float = 200.0) -> float:
    f = lambda x: pi_infinity(x, species) - 1.0
    if f(low) >= 0.0 or f(high) <= 0.0:
        raise RuntimeError("intervalo não contém uma única fronteira Pi_inf=1")
    return float(brentq(f, low, high, xtol=1e-12, rtol=1e-12))


def audit_scenario(name: str, species: list[Species]) -> dict[str, object]:
    critical = critical_scale(species)
    grid = np.linspace(-3.0, 120.0, 493)
    values = np.array([pi_infinity(float(x), species) for x in grid])
    return {
        "name": name,
        "species": species,
        "critical": critical,
        "critical_pi": pi_infinity(critical, species),
        "monotone": bool(np.all(np.diff(values) >= -1e-13)),
        "below": pi_infinity(critical - 1.0, species),
        "above": pi_infinity(critical + 1.0, species),
        "weight": sum(item.weight for item in species),
    }


def write_report(results: list[dict[str, object]], output: Path) -> None:
    lines = [
        "# Varredura multiespécie $U(1)$ — Q34/Q35",
        "",
        "## Classificação",
        "",
        "**Avaliação direta e teste de consistência.** A fronteira calculada não",
        "prediz $\\Lambda_{\\rm EM}$; informa apenas que condição uma derivação",
        "geométrica posterior precisa satisfazer.",
        "",
        "## Fórmula",
        "",
        "$$",
        "\\Pi_{\\rm EM}(\\infty)=\\frac{\\alpha_0}{3\\pi}",
        "\\sum_f N_c^{(f)}Q_f^2",
        "E_1\\!\\left(\\frac{m_f^2}{\\Lambda_{\\rm EM}^2}\\right).",
        "$$",
        "",
        "A fronteira é definida por $\\Pi_{\\rm EM}(\\infty)=1$.",
        "",
        "## Resultados",
        "",
        "| cenário | espécies | $\\sum N_cQ^2$ | $\\log_{10}(\\Lambda_{\\rm crit}/m_e)$ | $\\Pi$ na raiz |",
        "|:---|---:|---:|---:|---:|",
    ]
    for row in results:
        lines.append(
            f"| {row['name']} | {len(row['species'])} | {row['weight']:.6f} | "
            f"{row['critical']:.9f} | {row['critical_pi']:.12f} |"
        )
    lines += [
        "",
        "Uma década abaixo e acima da raiz:",
        "",
        "| cenário | $\\Pi(\\Lambda_{\\rm crit}/10)$ | $\\Pi(10\\Lambda_{\\rm crit})$ | monotônica |",
        "|:---|---:|---:|:---:|",
    ]
    for row in results:
        lines.append(
            f"| {row['name']} | {row['below']:.9f} | {row['above']:.9f} | {row['monotone']} |"
        )
    for row in results:
        lines += ["", f"## Espectro: {row['name']}", ""]
        lines += [
            "| espécie | $m_f/m_e$ | $Q_f$ | $N_c$ | peso | proveniência |",
            "|:---|---:|---:|---:|---:|:---|",
        ]
        for item in row["species"]:
            lines.append(
                f"| {item.name} | {item.mass_over_me:.9g} | {item.charge:.6g} | "
                f"{item.colors} | {item.weight:.6g} | {item.provenance} |"
            )
    lines += [
        "",
        "## Limitações",
        "",
        "- O cenário léptons GDQ usa as razões espectrais registradas na Q39.",
        "- O cenário com quarks é benchmark externo: massas de quarks dependem de",
        "  esquema e escala e não foram derivadas neste cálculo.",
        "- A raiz extremamente alta é consequência matemática da extrapolação",
        "  efetiva; não deve ser chamada de escala GDQ prevista.",
        "- A próxima etapa estrutural continua sendo obter $\\Lambda_{\\rm EM}$ da",
        "  Hessiana e do espectro eletromagnético.",
        "",
    ]
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", type=Path,
        default=Path(__file__).with_name("saida_sweep_especies_u1.md"),
    )
    args = parser.parse_args()
    results = [
        audit_scenario("léptons GDQ", leptons_gdq()),
        audit_scenario("férmions carregados — benchmark", charged_fermion_benchmark()),
    ]
    write_report(results, args.output)
    for row in results:
        print(f"{row['name']}: log10(Lambda_crit/m_e)={row['critical']:.9f}")
    print(f"Relatório: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
