#!/usr/bin/env python3
"""
Objetivo:
    Registrar de forma autocontida a verificação `comparar tau neutron` associada ao capítulo `17_baryonic_structure`.

GDQ — Capítulo 17 / vida média do nêutron.

Calcula:

    tau_n = (32/15) alpha^-11 hbar/(m_e c^2)

usando hbar em GeV*s e m_e c^2 em GeV.

Classificação: comparação fenomenológica da taxa total reduzida.
"""

from __future__ import annotations

from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parent
    out = root / "saida_comparar_tau_neutron.md"

    alpha_inv = 137.035999177
    hbar_gev_s = 6.582119569e-25
    me_gev = 0.00051099895000
    tau = (32.0 / 15.0) * (alpha_inv**11) * hbar_gev_s / me_gev
    half_life = tau * 0.6931471805599453
    ref = 878.3
    diff = tau - ref
    rel = diff / ref

    text = f"""# Saída — vida média do nêutron

Classificação: comparação fenomenológica da taxa total reduzida.

| quantidade | valor |
|---|---:|
| alpha^-1 | {alpha_inv:.12f} |
| tau_n GDQ s | {tau:.12f} |
| T_1/2 GDQ s | {half_life:.12f} |
| tau_ref s | {ref:.12f} |
| diferença s | {diff:.12f} |
| diferença relativa | {rel:.12e} |

Interpretação: a taxa total reduzida fica no nível $10^{{-3}}$ da referência.
Forma diferencial, correlações angulares e recoil permanecem extensões.
"""

    out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
