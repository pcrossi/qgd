#!/usr/bin/env python3
"""
GDQ — Modelo reduzido Q39 -> Q43.

Objetivo:
    Usar a hierarquia leptônica intrínseca da Q39 como background reduzido
    para testar o quanto ela explica, sozinha, os resíduos superiores de g-2.

Classificação:
    teste de consistência + diagnóstico inverso.

Este script NÃO é uma predição cega de g-2. Ele separa:
    1. o termo universal líder alpha/(2*pi), já derivado estruturalmente;
    2. a susceptibilidade escalar diagonal herdada da Q39;
    3. a fonte transversal ainda faltante m_perp,l da Hessiana física.

Conclusão esperada:
    a hierarquia leptônica fornece o background, mas não substitui o cálculo
    do operador transversal H_C^{-1} m_perp.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


ALPHA_INV = 137.035999177
ALPHA = 1.0 / ALPHA_INV


@dataclass(frozen=True)
class Lepton:
    name: str
    symbol: str
    q39_role: str
    anomaly_obs: float | None
    sigma_anomaly: float | None
    source: str


LEPTONS = [
    Lepton(
        name="elétron",
        symbol="e",
        q39_role="torção primária",
        anomaly_obs=1.00115965218059 - 1.0,
        sigma_anomaly=1.3e-13,
        source="Fan et al. 2022/2023, g/2",
    ),
    Lepton(
        name="múon",
        symbol="mu",
        q39_role="torção transversal/biespacial",
        anomaly_obs=116592059e-11,
        sigma_anomaly=22e-11,
        source="Muon g-2 world average 2023",
    ),
    Lepton(
        name="tau",
        symbol="tau",
        q39_role="saturação tridimensional",
        anomaly_obs=None,
        sigma_anomaly=None,
        source="sem uso metrológico neste teste",
    ),
]


def r_mu_intrinsic(alpha_inv: float = ALPHA_INV) -> float:
    alpha = 1.0 / alpha_inv
    return 1.5 * alpha_inv + 6.0 / 5.0 + 2.0 * alpha


def r_tau_from_q(r_mu: float, q: float = 2.0 / 3.0) -> float:
    a = math.sqrt(r_mu)
    A = 1.0 - q
    B = -2.0 * q * (1.0 + a)
    C = 1.0 + r_mu - q * (1.0 + a) ** 2
    disc = B * B - 4.0 * A * C
    if disc < 0:
        raise ValueError("sem raiz real para Q=2/3")
    y1 = (-B - math.sqrt(disc)) / (2.0 * A)
    y2 = (-B + math.sqrt(disc)) / (2.0 * A)
    return max(y1 * y1, y2 * y2)


def main() -> None:
    a1 = ALPHA / (2.0 * math.pi)
    x2 = (ALPHA / math.pi) ** 2

    ratios = {
        "e": 1.0,
        "mu": r_mu_intrinsic(),
        "tau": r_tau_from_q(r_mu_intrinsic()),
    }
    chi_rel = {symbol: 1.0 / value for symbol, value in ratios.items()}

    # Diagnóstico: se o resíduo superior escalasse somente com a susceptibilidade
    # escalar diagonal 1/R_l, calibrando no elétron, o múon/tau seguiriam esta
    # curva. Isso testa se a hierarquia sozinha substitui o operador
    # transversal magnético. A resposta deve ser negativa.
    electron_residual = LEPTONS[0].anomaly_obs - a1

    lines: list[str] = []
    lines.append("# Saída — Modelo reduzido Q39→Q43")
    lines.append("")
    lines.append("## Classificação")
    lines.append("")
    lines.append(
        "Teste de consistência e diagnóstico inverso. Este cálculo não é "
        r"predição cega de \(g-2\)."
    )
    lines.append("")
    lines.append("## Parâmetros usados")
    lines.append("")
    lines.append(f"- `alpha_inv = {ALPHA_INV:.12f}`")
    lines.append(f"- `alpha = {ALPHA:.15e}`")
    lines.append(f"- `a1 = alpha/(2*pi) = {a1:.15e}`")
    lines.append(f"- `R_mu_Q39 = {ratios['mu']:.15e}`")
    lines.append(f"- `R_tau_Q39 = {ratios['tau']:.15e}`")
    lines.append("")
    lines.append("## Hierarquia Q39 usada como background reduzido")
    lines.append("")
    lines.append("| lépton | papel Q39 | R_l=M_l/M_e | chi_rel=1/R_l |")
    lines.append("|---|---|---:|---:|")
    for lep in LEPTONS:
        lines.append(
            f"| {lep.name} | {lep.q39_role} | {ratios[lep.symbol]:.15e} | "
            f"{chi_rel[lep.symbol]:.15e} |"
        )
    lines.append("")
    lines.append("## Resíduos superiores observados")
    lines.append("")
    lines.append(
        r"O resíduo é \(a_{\rm obs}-\alpha/(2\pi)\). "
        "O coeficiente agregado é apenas diagnóstico:"
    )
    lines.append("")
    lines.append("| lépton | a_obs | resíduo | C2_agregado = residuo/(alpha/pi)^2 | fonte |")
    lines.append("|---|---:|---:|---:|---|")
    for lep in LEPTONS:
        if lep.anomaly_obs is None:
            lines.append(f"| {lep.name} | — | — | — | {lep.source} |")
            continue
        residual = lep.anomaly_obs - a1
        c2 = residual / x2
        lines.append(
            f"| {lep.name} | {lep.anomaly_obs:.15e} | "
            f"{residual:.15e} | {c2:.12f} | {lep.source} |"
        )
    lines.append("")
    lines.append("## Teste: a hierarquia sozinha explica o resíduo?")
    lines.append("")
    lines.append(
        "Hipótese testada: o resíduo superior escala apenas com a "
        r"susceptibilidade escalar diagonal \(\chi_\ell\propto1/R_\ell\), "
        "normalizada no elétron."
    )
    lines.append("")
    lines.append("| lépton | resíduo previsto por chi_rel | resíduo observado | veredito |")
    lines.append("|---|---:|---:|---|")
    for lep in LEPTONS:
        pred = electron_residual * chi_rel[lep.symbol]
        if lep.anomaly_obs is None:
            lines.append(
                f"| {lep.name} | {pred:.15e} | — | sem comparação metrológica |"
            )
            continue
        obs = lep.anomaly_obs - a1
        ratio = pred / obs if obs != 0 else float("nan")
        verdict = (
            "calibração de referência"
            if lep.symbol == "e"
            else f"falha por fator {ratio:.3e}"
        )
        lines.append(f"| {lep.name} | {pred:.15e} | {obs:.15e} | {verdict} |")
    lines.append("")
    lines.append("## Diagnóstico inverso mínimo")
    lines.append("")
    lines.append(
        r"Se se escreve \(a_\ell-a_1=\mathcal R_\ell\), então o operador "
        r"transversal físico deve produzir exatamente \(\mathcal R_\ell\):"
    )
    lines.append("")
    lines.append("$$")
    lines.append(
        "\\mathcal R_\\ell="
        "\\frac{1}{\\gamma_{0,\\ell}}"
        "\\frac{\\langle c_\\ell,H_{C,\\ell}^{+}m_{\\perp,\\ell}\\rangle}"
        "{\\langle c_\\ell,H_{C,\\ell}^{+}c_\\ell\\rangle}"
        "-\\frac{\\alpha}{2\\pi}."
    )
    lines.append("$$")
    lines.append("")
    lines.append(
        "No modelo diagonal reduzido, a massa/hierarquia não determina essa "
        r"contração. A informação faltante é \(m_{\perp,\ell}\) e o bloco "
        r"transversal físico de \(H_{C,\ell}\)."
    )
    lines.append("")
    lines.append("## Conclusão")
    lines.append("")
    lines.append(
        "A hierarquia Q39 é necessária como background leptônico, mas é "
        r"insuficiente para fechar \(g-2\). A hierarquia de massas não pode ser "
        "usada como substituto do cálculo Zeeman/anomalia. O próximo elo "
        r"físico é construir \(H_{C,\ell}\), \(c_\ell\) e \(m_{\perp,\ell}\) "
        "diretamente da Hessiana oficial em cada background leptônico."
    )
    lines.append("")

    out = Path(__file__).with_name("saida_modelo_reduzido_q39_q43.md")
    out.write_text("\n".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
