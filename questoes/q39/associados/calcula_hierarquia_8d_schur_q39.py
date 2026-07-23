#!/usr/bin/env python3
"""Q39 — hierarquia leptônica expandida para 8D por Schur.

O script avalia:

    R_mu^(0) = 3/(2 alpha)+6/5+2 alpha
    R_tau^(0) por Q=2/3
    correções 8D por sigma_mu, sigma_tau
    fator de resposta dR_tau/dR_mu sob Q fixo

Não usa alvos experimentais para construir os números.
"""

from __future__ import annotations

from pathlib import Path
import math


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV


def r_mu_reduced(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0:
        raise ValueError("sem raiz real")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def q_value(r_mu: float, r_tau: float) -> float:
    return (1.0 + r_mu + r_tau) / (1.0 + math.sqrt(r_mu) + math.sqrt(r_tau)) ** 2


def partials_q(r_mu: float, r_tau: float) -> tuple[float, float]:
    s = 1.0 + math.sqrt(r_mu) + math.sqrt(r_tau)
    n = 1.0 + r_mu + r_tau
    dq_mu = 1.0 / (s * s) - n / (s**3 * math.sqrt(r_mu))
    dq_tau = 1.0 / (s * s) - n / (s**3 * math.sqrt(r_tau))
    return dq_mu, dq_tau


def schur_bound(j_mix: float, m_perp2: float) -> float:
    if m_perp2 <= 0:
        return math.inf
    return (j_mix * j_mix) / m_perp2


def main() -> None:
    base = Path(__file__).resolve().parent
    rmu0 = r_mu_reduced()
    rtau0 = r_tau_from_q(rmu0)
    dq_mu, dq_tau = partials_q(rmu0, rtau0)
    amp_tau_mu = -dq_mu / dq_tau

    scenarios = [
        ("produto", 0.0, 1.0),
        ("subcritico_fraco", 0.1, 0.99),
        ("subcritico_4canais", 0.4, 0.96),
    ]

    lines = [
        "# Q39 — saída da hierarquia 8D por Schur",
        "",
        "## Valores reduzidos",
        "",
        f"- `R_mu_0 = {rmu0:.15f}`",
        f"- `R_tau_0 = {rtau0:.15f}`",
        f"- `Q(R_mu_0,R_tau_0) = {q_value(rmu0, rtau0):.15f}`",
        "",
        "## Resposta linear da saturação",
        "",
        f"- `dQ/dR_mu = {dq_mu:.15e}`",
        f"- `dQ/dR_tau = {dq_tau:.15e}`",
        f"- `dR_tau/dR_mu | Q = {amp_tau_mu:.15f}`",
        "",
        "## Cotas de Schur",
        "",
        "| cenário | j_mix | m_perp^2 | Delta_Schur | |delta R_mu| max | |delta R_tau direto| max |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for name, j_mix, m_perp2 in scenarios:
        delta = schur_bound(j_mix, m_perp2)
        lines.append(
            f"| {name} | {j_mix:.12g} | {m_perp2:.12g} | {delta:.12g} | "
            f"{delta:.12g} | {delta:.12g} |"
        )

    lines.extend(
        [
            "",
            "## Fórmula 8D",
            "",
            "$$",
            "R_\\mu^{(8)}",
            "=",
            "R_\\mu^{(0)}-\\sigma_\\mu.",
            "$$",
            "",
            "$$",
            "|\\sigma_\\ell|\\le\\Delta_{\\rm Schur}.",
            "$$",
            "",
            "Mantendo a saturação $Q=2/3$:",
            "",
            "$$",
            "dR_\\tau",
            "=",
            "-\\frac{\\partial_\\mu Q}{\\partial_\\tau Q}dR_\\mu.",
            "$$",
            "",
        ]
    )

    report = base / "saida_hierarquia_8d_schur_q39.md"
    report.write_text("\n".join(lines), encoding="utf-8")
    print(report)


if __name__ == "__main__":
    main()
