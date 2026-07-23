#!/usr/bin/env python3
"""
GDQ — Capítulo 3 / Homogeneidade dimensional de z_tau.

Objetivo:
    Verificar de modo autocontido que a variável causal complexa
    z_tau = tau + i nu_0 t é dimensionalmente homogênea se tau tem dimensão
    L^2, t tem dimensão T e nu_0 tem dimensão L^2/T.

Fonte teórica:
    manuscrito/03_complex_causality/03.2 - Três variáveis que não devem ser confundidas.md
    manuscrito/notes/causality/Variável causal complexa - dimensão, simetrias e unicidade condicional.md

Classificação:
    Teste simbólico dimensional. Não é previsão física.

Equação:
    z_tau = tau + i nu_0 t

Domínio e contorno:
    Checagem algébrica de unidades; sem EDP e sem contorno.

Parâmetros:
    Universais/constitutivos:
        [tau] = L^2
        [t] = T
        [nu_0] = L^2/T
    Dados de aparelho/experimento:
        nenhum
    Numéricos:
        nenhum

Saída:
    saida_verificar_z_tau_dimensional.md

Observação:
    Nenhum alvo experimental é usado.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Dim:
    """Dimensão monomial L^a T^b."""

    length: int = 0
    time: int = 0

    def __mul__(self, other: "Dim") -> "Dim":
        return Dim(self.length + other.length, self.time + other.time)

    def __truediv__(self, other: "Dim") -> "Dim":
        return Dim(self.length - other.length, self.time - other.time)

    def __str__(self) -> str:
        parts = []
        if self.length:
            parts.append(f"L^{self.length}")
        if self.time:
            parts.append(f"T^{self.time}")
        return " ".join(parts) if parts else "1"


def main() -> None:
    tau = Dim(length=2)
    t = Dim(time=1)
    nu0 = Dim(length=2, time=-1)
    imaginary_part = nu0 * t
    ok = tau == imaginary_part

    lines: list[str] = []
    lines.append("# Saída — homogeneidade dimensional de $z_\\tau$\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico dimensional. Não é previsão física.\n\n")
    lines.append("## Fórmula\n\n")
    lines.append("$$\n")
    lines.append("z_\\tau=\\tau+i\\nu_0t.\n")
    lines.append("$$\n\n")
    lines.append("## Unidades\n\n")
    lines.append("| Quantidade | Dimensão |\n")
    lines.append("|---|---|\n")
    lines.append(f"| $\\tau$ | `{tau}` |\n")
    lines.append(f"| $t$ | `{t}` |\n")
    lines.append(f"| $\\nu_0$ | `{nu0}` |\n")
    lines.append(f"| $\\nu_0 t$ | `{imaginary_part}` |\n\n")
    lines.append("## Veredito\n\n")
    lines.append("A checagem passou: $\\tau$ e $\\nu_0t$ possuem a mesma dimensão.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída não determina o valor de $\\nu_0$; apenas verifica a homogeneidade dimensional.\n")

    out = OUT / "saida_verificar_z_tau_dimensional.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

