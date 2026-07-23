#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `auditar vk` associada ao capítulo `19_electroweak_geometric_breaking`.

GDQ — Capítulo 19 / auditoria da escala auxiliar v_K.

Calcula:

    v_K = M_e/alpha * (1 - 3/(4*pi^2))^{-1/2}

para demonstrar que essa expressão fornece escala de MeV, não 246 GeV.

Classificação: auditoria numérica/dimensional.
"""

from __future__ import annotations

from pathlib import Path
import math


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_auditar_vk.md"

    me_mev = 0.51099895
    alpha_inv = 137.035999
    alpha = 1.0 / alpha_inv
    factor = (1.0 - 3.0 / (4.0 * math.pi**2)) ** -0.5
    vk_mev = me_mev / alpha * factor
    vk_gev = vk_mev / 1000.0
    v_ew = 246.111195996

    text = f"""# Saída — auditoria de v_K

Classificação: auditoria numérica/dimensional.

| quantidade | valor |
|---|---:|
| M_e MeV | {me_mev:.8f} |
| alpha_inv | {alpha_inv:.6f} |
| fator geométrico | {factor:.12f} |
| v_K MeV | {vk_mev:.6f} |
| v_K GeV | {vk_gev:.9f} |
| v_EW usado GeV | {v_ew:.12f} |

Interpretação: $v_K$ é escala auxiliar de baixa energia; não é a escala
eletrofraca.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
