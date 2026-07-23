#!/usr/bin/env python3
"""
GDQ — Capítulo 4 / Dimensão da ação em coordenadas normalizadas.

Objetivo:
    Verificar a contagem dimensional que remove a ambiguidade anterior:
    em coordenadas normalizadas pela escala de Cartan, a integral interna e
    d tau/tau são adimensionais, de modo que o prefator tem dimensão hbar
    quando Lambda_C é um número adimensional.

Fonte teórica:
    manuscrito/04_action_consistency/04.2 - A ação oficial da GDQ.md
    manuscrito/04_action_consistency/04.4 - Como ler cada termo da ação.md
    manuscrito/notes/action/Dimensão e normalização da ação oficial.md

Classificação:
    Teste simbólico dimensional. Não é previsão física.

Equação:
    S_GDQ = integral_gamma [ integral_M hbar/Lambda_C^2 * L0 * U * dV ] d tau/tau

Domínio e contorno:
    Checagem de dimensão; sem EDP.

Parâmetros:
    Universais/estruturais:
        [R] = L^-2, [tau] = L^2, [U] = L^-2n, [dV] = L^2n.
    Dados de aparelho/experimento:
        nenhum.
    Numéricos:
        n = 4.

Saída:
    saida_verificar_dimensao_acao_normalizada.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Dim:
    hbar: int = 0
    length: int = 0

    def __mul__(self, other: "Dim") -> "Dim":
        return Dim(self.hbar + other.hbar, self.length + other.length)

    def __truediv__(self, other: "Dim") -> "Dim":
        return Dim(self.hbar - other.hbar, self.length - other.length)

    def __pow__(self, power: int) -> "Dim":
        return Dim(self.hbar * power, self.length * power)

    def __str__(self) -> str:
        parts = []
        if self.hbar:
            parts.append(f"hbar^{self.hbar}")
        if self.length:
            parts.append(f"L^{self.length}")
        return " ".join(parts) if parts else "1"


def main() -> None:
    n = 4
    curvature = Dim(length=-2)
    tau = Dim(length=2)
    f = Dim()
    grad_f_sq = Dim(length=-2)
    l0_curv = tau * curvature
    l0_grad = tau * grad_f_sq
    l0_f = f
    measure = Dim(length=-2 * n)
    volume = Dim(length=2 * n)
    dtau_over_tau = Dim()
    lambda_c = Dim()  # dimensionless cutoff number in normalized coordinates
    prefactor = Dim(hbar=1) / (lambda_c**2)
    full = prefactor * l0_curv * measure * volume * dtau_over_tau
    ok = l0_curv == Dim() and l0_grad == Dim() and l0_f == Dim() and full == Dim(hbar=1)

    lines: list[str] = []
    lines.append("# Saída — dimensão da ação normalizada\n\n")
    lines.append("## Classificação\n\n")
    lines.append("Teste simbólico dimensional. Não é previsão física.\n\n")
    lines.append("## Convenção\n\n")
    lines.append("$\\Lambda_C$ é tratado como número de corte adimensional nas coordenadas normalizadas.\n\n")
    lines.append("## Tabela dimensional\n\n")
    lines.append("| Quantidade | Dimensão |\n")
    lines.append("|---|---|\n")
    lines.append(f"| $\\mathcal R$ | `{curvature}` |\n")
    lines.append(f"| $\\tau$ | `{tau}` |\n")
    lines.append(f"| $\\tau\\mathcal R$ | `{l0_curv}` |\n")
    lines.append(f"| $\\tau|\\nabla f|^2$ | `{l0_grad}` |\n")
    lines.append(f"| $(f+\\bar f)/2-n$ | `{l0_f}` |\n")
    lines.append(f"| $\\mathcal U$ em $n=4$ | `{measure}` |\n")
    lines.append(f"| $dV_g$ | `{volume}` |\n")
    lines.append(f"| $d\\tau/\\tau$ | `{dtau_over_tau}` |\n")
    lines.append(f"| $\\hbar/\\Lambda_C^2$ | `{prefactor}` |\n")
    lines.append(f"| ação total | `{full}` |\n\n")
    lines.append("## Veredito\n\n")
    lines.append("A checagem passou: a ação tem dimensão de $\\hbar$.\n" if ok else "A checagem falhou.\n")
    lines.append("\nEsta saída não determina a escala física $\\ell_C$, $k_C$ ou $E_C$.\n")

    out = OUT / "saida_verificar_dimensao_acao_normalizada.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()

