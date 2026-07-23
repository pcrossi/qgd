#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `integrar tubo ricci bohm confinamento` associada ao capítulo `18_confinement_signal_problem`.

GDQ — Capítulo 18 / integração direta do tubo Ricci--Bohm.

Calcula:

    sigma = ∫_0^r 2*pi*s ds * hbarc/r^4 = pi*hbarc/r^2
    Delta = hbarc/r

Classificação: avaliação direta da tensão reduzida.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_integrar_tubo_ricci_bohm_confinamento.md"

    hbarc = 0.1973269804
    r = 0.86
    area = math.pi * r * r
    delta = hbarc / r
    sigma = math.pi * hbarc / (r * r)
    gev2 = sigma * hbarc

    text = f"""# Saída — tubo Ricci-Bohm

Classificação: avaliação direta da tensão reduzida.

| quantidade | valor |
|---|---:|
| r_perp fm | {r:.12f} |
| área fm^2 | {area:.12f} |
| Delta GeV | {delta:.12f} |
| sigma GeV/fm | {sigma:.12f} |
| sigma GeV^2 | {gev2:.12f} |
| sqrt(sigma GeV^2) GeV | {math.sqrt(gev2):.12f} |

Interpretação: o fator pi vem da integral circular transversal.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
