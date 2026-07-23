#!/usr/bin/env python3
"""
GDQ — Capítulo 15 / critério de estabilidade para backgrounds warped/mistos.

Classificação:
    teste de consistência do complemento de Schur.

Calcula:

    m_perp^2 = C_gamma*tau/R_max^2 - sum(c_i a_i^2),
    j_mix = sum(b_i a_i),
    Delta_Schur = j_mix^2 / m_perp^2.

Os valores padrão são normalizados e ilustrativos. Não usam dados
experimentais e não fecham backgrounds warped/mistos reais; eles exibem o
critério que deve ser aplicado quando tal background for obtido.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import math


@dataclass(frozen=True)
class MixedInput:
    a_warp: float
    a_dilaton: float
    a_torsion: float
    eps_metric: float
    lambda_b_gap: float = 1.0
    c_gamma: float = 1.0
    tau: float = 1.0
    r_max: float = 1.0
    c_warp: float = 1.0
    c_dilaton: float = 1.0
    c_torsion: float = 1.0
    c_metric: float = 1.0
    b_warp: float = 1.0
    b_dilaton: float = 1.0
    b_torsion: float = 1.0
    b_metric: float = 1.0


def evaluate(inp: MixedInput) -> dict[str, float | str]:
    if inp.lambda_b_gap <= 0:
        raise ValueError("lambda_b_gap deve ser positivo")
    if inp.c_gamma <= 0 or inp.tau <= 0 or inp.r_max <= 0:
        raise ValueError("c_gamma, tau e r_max devem ser positivos")

    loss = (
        inp.c_warp * inp.a_warp**2
        + inp.c_dilaton * inp.a_dilaton**2
        + inp.c_torsion * inp.a_torsion**2
        + inp.c_metric * inp.eps_metric**2
    )
    m_perp2 = inp.c_gamma * inp.tau / (inp.r_max**2) - loss
    j_mix = (
        inp.b_warp * inp.a_warp
        + inp.b_dilaton * inp.a_dilaton
        + inp.b_torsion * inp.a_torsion
        + inp.b_metric * inp.eps_metric
    )

    if m_perp2 <= 0:
        return {
            "m_perp2": m_perp2,
            "j_mix": j_mix,
            "schur": math.inf,
            "ratio": math.inf,
            "status": "nao-coercivo",
        }

    schur_value = (j_mix * j_mix) / m_perp2
    ratio = schur_value / inp.lambda_b_gap
    if schur_value < inp.lambda_b_gap:
        status = "subcritico"
    elif math.isclose(schur_value, inp.lambda_b_gap, rel_tol=1e-12, abs_tol=1e-12):
        status = "critico"
    else:
        status = "supercritico"
    return {
        "m_perp2": m_perp2,
        "j_mix": j_mix,
        "schur": schur_value,
        "ratio": ratio,
        "status": status,
    }


def one_channel_threshold(lambda_b_gap: float) -> float:
    if lambda_b_gap <= 0:
        raise ValueError("lambda_b_gap deve ser positivo")
    return math.sqrt(lambda_b_gap / (1.0 + lambda_b_gap))


def main() -> None:
    scenarios = [
        ("produto", MixedInput(0.0, 0.0, 0.0, 0.0)),
        ("fraco_um_canal_0p1", MixedInput(0.1, 0.0, 0.0, 0.0)),
        ("quatro_canais_0p1", MixedInput(0.1, 0.1, 0.1, 0.1)),
        ("um_canal_critico_lambda1", MixedInput(one_channel_threshold(1.0), 0.0, 0.0, 0.0)),
        ("um_canal_supercritico_0p8", MixedInput(0.8, 0.0, 0.0, 0.0)),
    ]

    lines = [
        "---",
        'title: "Saída — critério warped/misto"',
        "---",
        "",
        "# Saída — critério warped/misto",
        "",
        "## Fórmulas",
        "",
        "$$",
        "m_\\perp^2",
        "=",
        "C_\\gamma\\tau R_{\\max}^{-2}",
        "-",
        "\\sum_i c_i a_i^2.",
        "$$",
        "",
        "$$",
        "j_{\\rm mix}=\\sum_i b_i a_i.",
        "$$",
        "",
        "$$",
        "\\Delta_{\\rm Schur}",
        "=",
        "\\frac{j_{\\rm mix}^2}{m_\\perp^2}.",
        "$$",
        "",
        "Estável/subcrítico se:",
        "",
        "$$",
        "\\Delta_{\\rm Schur}<\\lambda_B^{\\rm gap}.",
        "$$",
        "",
        "## Cenários normalizados",
        "",
        "| cenário | $m_\\perp^2$ | $j_{\\rm mix}$ | $\\Delta_{\\rm Schur}$ | razão/gap | status |",
        "|---|---:|---:|---:|---:|---|",
    ]

    for name, inp in scenarios:
        out = evaluate(inp)
        lines.append(
            f"| {name} | {out['m_perp2']:.12g} | {out['j_mix']:.12g} | "
            f"{out['schur']:.12g} | {out['ratio']:.12g} | {out['status']} |"
        )

    lines.extend(
        [
            "",
            "## Limiar de um canal",
            "",
            "Para um único canal misto ativo com $\\lambda_B^{\\rm gap}=1$:",
            "",
            "$$",
            "a_{\\rm crit}=\\frac1{\\sqrt2}\\simeq0.707106781187.",
            "$$",
            "",
            "Abaixo desse valor, a mistura warped/mista não altera o índice crítico.",
            "Acima dele, o background pode gerar modo adicional, que deve ser",
            "classificado como ressonância, estado de contorno ou estado composto",
            "até prova de carga primitiva e estabilidade assintótica.",
            "",
        ]
    )

    out = Path(__file__).with_name("saida_criterio_warped_misto.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
