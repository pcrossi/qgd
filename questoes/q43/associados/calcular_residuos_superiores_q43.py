#!/usr/bin/env python3
"""Q43 — resíduos superiores de g-2.

Calcula o que resta depois do termo GDQ líder

    a1 = alpha/(2*pi)

para elétron e múon. Esses resíduos NÃO são derivados pela GDQ neste script.
Eles são diagnósticos metrológicos: indicam o tamanho que a contração
H_C^{-1} m_perp deve produzir nas ordens superiores.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


ALPHA_INV_CODATA_2022 = 137.035999177


@dataclass(frozen=True)
class Case:
    name: str
    anomaly: float
    uncertainty: float | None
    source: str


def evaluate(case: Case, alpha: float) -> dict[str, float | str | None]:
    x = alpha / math.pi
    a1 = x / 2.0
    residual = case.anomaly - a1
    c2_aggregate = residual / (x * x)
    c3_aggregate = residual / (x * x * x)
    g = 2.0 * (1.0 + case.anomaly)
    g_leader = 2.0 * (1.0 + a1)
    return {
        "name": case.name,
        "a_obs": case.anomaly,
        "sigma": case.uncertainty,
        "a1": a1,
        "residual_a": residual,
        "g_obs": g,
        "g_leader": g_leader,
        "residual_g": 2.0 * residual,
        "c2_aggregate": c2_aggregate,
        "c3_aggregate": c3_aggregate,
        "source": case.source,
    }


def fmt(x: float | None) -> str:
    if x is None:
        return "—"
    return f"{x:.15e}"


def main() -> None:
    alpha = 1.0 / ALPHA_INV_CODATA_2022

    # Electron: Fan et al. quote -mu/mu_B = g/2.
    # The anomaly magnitude is g/2 - 1.
    electron = Case(
        name="electron Fan 2022",
        anomaly=1.00115965218059 - 1.0,
        uncertainty=0.00000000000013,
        source="Fan et al. arXiv:2209.13084",
    )

    # Muon: 2023 Fermilab + BNL world average from arXiv:2308.06230.
    muon_2023 = Case(
        name="muon world avg 2023",
        anomaly=116_592_059e-11,
        uncertainty=22e-11,
        source="Aguillard et al. arXiv:2308.06230",
    )

    rows = [evaluate(electron, alpha), evaluate(muon_2023, alpha)]

    lines = [
        "# Q43 — resíduos superiores depois do termo líder",
        "",
        "Classificação: comparação metrológica externa e diagnóstico de tamanho.",
        "Não é derivação dos termos superiores da GDQ.",
        "",
        f"- alpha^-1 usado: `{ALPHA_INV_CODATA_2022:.12f}`",
        f"- x = alpha/pi: `{alpha / math.pi:.15e}`",
        f"- termo líder: `a1 = alpha/(2*pi) = {alpha/(2*math.pi):.15e}`",
        "",
        "| caso | a_obs | sigma | a_obs-a1 | g_obs | g_lider | g_obs-g_lider | C2 agregado | fonte |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---|",
    ]
    for r in rows:
        sigma_text = fmt(r["sigma"] if isinstance(r["sigma"], float) else None)
        r_fmt = dict(r)
        r_fmt["sigma_text"] = sigma_text
        lines.append(
            "| {name} | {a_obs:.15e} | {sigma_text} | {residual_a:.15e} | "
            "{g_obs:.15f} | {g_leader:.15f} | {residual_g:.15e} | "
            "{c2_aggregate:.12f} | {source} |".format(
                **r_fmt,
            )
        )

    lines.extend(
        [
            "",
            "## Leitura GDQ",
            "",
            "Para cada lépton, o resíduo deve ser produzido por:",
            "",
            "$$",
            "\\Delta\\gamma_{\\rm geom}^{\\rm sup}",
            "=",
            "\\frac{\\langle c,H_C^{-1}m_\\perp\\rangle}",
            "{\\langle c,H_C^{-1}c\\rangle}",
            "-\\gamma_0\\frac{\\alpha}{2\\pi}.",
            "$$",
            "",
            "O `C2 agregado` é apenas o coeficiente efetivo que apareceria se todo",
            "o resíduo fosse colocado em `(alpha/pi)^2`. Ele não é uma derivação.",
            "",
            "Para o elétron, o coeficiente agregado é da ordem de unidade negativa,",
            "como esperado para uma correção superior pequena. Para o múon, o",
            "coeficiente agregado muda de modo significativo, mostrando que o",
            "background leptônico pesado não pode ser substituído pelo background",
            "do elétron.",
            "",
        ]
    )

    out = Path(__file__).with_name("saida_residuos_superiores_q43.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)
    print("\n".join(lines))


if __name__ == "__main__":
    main()
