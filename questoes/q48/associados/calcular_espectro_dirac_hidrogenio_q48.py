#!/usr/bin/env python3
"""Q48 — avaliação direta do espectro Sommerfeld--Dirac.

Classificação: avaliação direta de fórmula derivada como redução espinorial
efetiva da GDQ no limite coulombiano externo.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import sqrt
from pathlib import Path

from scipy import constants as C


OUT = Path(__file__).with_name("saida_espectro_dirac_hidrogenio_q48.md")


alpha = C.alpha
c = C.c
e = C.e
m_e = C.m_e
m_p = C.m_p

mec2_eV = m_e * c**2 / e
mu_ep = m_e * m_p / (m_e + m_p)
mu_c2_eV = mu_ep * c**2 / e


@dataclass(frozen=True)
class Level:
    n: int
    kappa: int
    label: str

    @property
    def j(self) -> float:
        return abs(self.kappa) - 0.5

    @property
    def degeneracy(self) -> int:
        return int(2 * self.j + 1)


def dirac_energy_eV(n: int, kappa: int, z: int = 1, mass_energy_eV: float = mec2_eV) -> float:
    za = z * alpha
    gamma = sqrt(kappa * kappa - za * za)
    denom = n - abs(kappa) + gamma
    return mass_energy_eV / sqrt(1.0 + (za / denom) ** 2)


def binding_eV(n: int, kappa: int, mass_energy_eV: float) -> float:
    return dirac_energy_eV(n, kappa, mass_energy_eV=mass_energy_eV) - mass_energy_eV


def main() -> None:
    levels = [
        Level(1, -1, "1s1/2"),
        Level(2, -1, "2s1/2"),
        Level(2, +1, "2p1/2"),
        Level(2, -2, "2p3/2"),
        Level(3, -1, "3s1/2"),
        Level(3, +1, "3p1/2"),
        Level(3, -2, "3p3/2"),
        Level(3, +2, "3d3/2"),
        Level(3, -3, "3d5/2"),
    ]

    rows = []
    for lev in levels:
        rows.append(
            (
                lev.label,
                lev.n,
                lev.kappa,
                lev.j,
                lev.degeneracy,
                binding_eV(lev.n, lev.kappa, mec2_eV),
                binding_eV(lev.n, lev.kappa, mu_c2_eV),
            )
        )

    fs_2p = binding_eV(2, -2, mu_c2_eV) - binding_eV(2, +1, mu_c2_eV)
    lamb_dirac = binding_eV(2, -1, mu_c2_eV) - binding_eV(2, +1, mu_c2_eV)

    text = [
        "# Saída — espectro Dirac do hidrogênio (Q48)",
        "",
        "Classificação: avaliação direta de fórmula derivada no limite espinorial",
        "Coulomb--Dirac efetivo da GDQ.",
        "",
        "## Constantes",
        "",
        f"- alpha = {alpha:.15g}",
        f"- m_e c^2 = {mec2_eV:.9f} eV",
        f"- mu_ep c^2 = {mu_c2_eV:.9f} eV",
        "",
        "## Níveis",
        "",
        "| nível | n | kappa | j | deg | E_bind sem recuo (eV) | E_bind com massa reduzida (eV) |",
        "|---|---:|---:|---:|---:|---:|---:|",
    ]
    for label, n, kappa, j, deg, be, be_mu in rows:
        text.append(f"| {label} | {n} | {kappa} | {j:.1f} | {deg} | {be:.12f} | {be_mu:.12f} |")

    text += [
        "",
        "## Checagens",
        "",
        f"- Estrutura fina Dirac 2p3/2 - 2p1/2 = {fs_2p:.12e} eV",
        f"- Degenerescência Coulomb--Dirac 2s1/2 - 2p1/2 = {lamb_dirac:.12e} eV",
        "",
        "A segunda diferença deve ser zero até erro numérico: Lamb shift não aparece",
        "no operador Coulomb--Dirac puro; exige campo próximo/DtN/Hessiana.",
        "",
    ]

    OUT.write_text("\n".join(text), encoding="utf-8")
    print("\n".join(text))


if __name__ == "__main__":
    main()
