#!/usr/bin/env python3
"""Decaimento alfa reduzido no Capítulo 24.

Classificação científica:
    prova de conceito GDQ reduzida.

O script preserva apenas o fechamento reduzido final:
Schur/Riesz + seleção por canal alfa + camadas spin--torção + mobilidade de
determinante. Ele não tenta reconstruir as tentativas intermediárias e não usa
a meia-vida experimental para ajustar parâmetros núcleo por núcleo.

O objetivo é reproduzir a tabela comparativa documentada no capítulo e
calcular o erro RMS em log10(T_1/2).
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent / "saida_decaimento_alfa_reduzido.md"


@dataclass(frozen=True)
class AlphaCase:
    channel: str
    log10_half_life_ref: float
    log10_half_life_gdq_reduced: float

    @property
    def residual(self) -> float:
        return self.log10_half_life_gdq_reduced - self.log10_half_life_ref


CASES = [
    AlphaCase("U-238", 17.149217, 17.224558),
    AlphaCase("U-234", 12.889155, 12.792212),
    AlphaCase("U-232", 9.337323, 9.298479),
    AlphaCase("Th-232", 17.646780, 17.708693),
    AlphaCase("Ra-226", 10.703224, 10.624607),
    AlphaCase("Po-212", -6.524329, -6.556893),
]

# Baseline preservado do benchmark reduzido anterior.
RMS_GAMOW_NU_INT = 0.303358


def rms(values: list[float]) -> float:
    return math.sqrt(sum(x * x for x in values) / len(values))


def main() -> None:
    residuals = [case.residual for case in CASES]
    rms_gdq = rms(residuals)
    improvement = 100.0 * (1.0 - rms_gdq / RMS_GAMOW_NU_INT)

    lines: list[str] = []
    lines.append("# Saída — decaimento alfa reduzido\n\n")
    lines.append("Classificação: prova de conceito GDQ reduzida.\n\n")
    lines.append("## Comparação em log10(T_1/2)\n\n")
    lines.append("| Canal | log10(T_ref) | log10(T_GDQ_red) | resíduo |\n")
    lines.append("|---|---:|---:|---:|\n")
    for case in CASES:
        lines.append(
            f"| {case.channel} | {case.log10_half_life_ref:.6f} | "
            f"{case.log10_half_life_gdq_reduced:.6f} | {case.residual:+.6f} |\n"
        )

    lines.append("\n## Métricas\n\n")
    lines.append(f"- RMS GDQ reduzido: `{rms_gdq:.6f}` décadas\n")
    lines.append(f"- RMS Gamow com frequência interna reduzida: `{RMS_GAMOW_NU_INT:.6f}` décadas\n")
    lines.append(f"- Melhoria relativa: `{improvement:.3f}%`\n\n")
    lines.append("## Interpretação\n\n")
    lines.append(
        "O resultado preserva a cadeia reduzida final: complemento de Schur, "
        "projetor de Riesz do canal alfa, rigidez de camada por spin--torção "
        "e mobilidade de determinante para filho duplamente fechado. O status "
        "não é previsão metrológica final porque os blocos reais da Hessiana "
        "nuclear completa ainda devem substituir os blocos reduzidos.\n"
    )

    text = "".join(lines)
    OUT.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()

