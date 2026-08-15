#!/usr/bin/env python3
"""
GDQ — Chapter 4 / Action dimension in normalized coordinates.

Goal:
    Verify the dimensional count that removes the previous ambiguity:
    in coordinates normalized by the Cartan scale, the inner integral and
    d tau/tau are dimensionless, so the prefactor has dimension of hbar
    when Lambda_C is a dimensionless number.

Theoretical Source:
    manuscript/04_action_consistency/04.2 - The official action of GDQ.md
    manuscript/04_action_consistency/04.4 - How to read each term of the action.md
    manuscript/notes/action/Dimension and normalization of the official action.md

Classification:
    Dimensional symbolic test. Not a physical prediction.

Equation:
    S_GDQ = integral_gamma [ integral_M hbar/Lambda_C^2 * L0 * U * dV ] d tau/tau

Domain and Boundary:
    Dimension check; no PDE.

Parameters:
    Universal/structural:
        [R] = L^-2, [tau] = L^2, [U] = L^-2n, [dV] = L^2n.
    Apparatus/experiment data:
        none.
    Numerical:
        n = 4.

Output:
    output_verify_normalized_action_dimension.md
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


OUT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class Dim:
    hbar: int = 0
    length: int = 0

    def __mul__(self, other: Dim) -> Dim:
        return Dim(self.hbar + other.hbar, self.length + other.length)

    def __truediv__(self, other: Dim) -> Dim:
        return Dim(self.hbar - other.hbar, self.length - other.length)

    def __pow__(self, power: int) -> Dim:
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
    lines.append("# Output — normalized action dimension\n\n")
    lines.append("## Classification\n\n")
    lines.append("Dimensional symbolic test. Not a physical prediction.\n\n")
    lines.append("## Convention\n\n")
    lines.append("$\\Lambda_C$ is treated as a dimensionless cutoff number in normalized coordinates.\n\n")
    lines.append("## Dimensional table\n\n")
    lines.append("| Quantity | Dimension |\n")
    lines.append("|---|---|\n")
    lines.append(f"| $\\mathcal R$ | `{curvature}` |\n")
    lines.append(f"| $\\tau$ | `{tau}` |\n")
    lines.append(f"| $\\tau\\mathcal R$ | `{l0_curv}` |\n")
    lines.append(f"| $\\tau|\\nabla f|^2$ | `{l0_grad}` |\n")
    lines.append(f"| $(f+\\bar f)/2-n$ | `{l0_f}` |\n")
    lines.append(f"| $\\mathcal U$ in $n=4$ | `{measure}` |\n")
    lines.append(f"| $dV_g$ | `{volume}` |\n")
    lines.append(f"| $d\tau/\\tau$ | `{dtau_over_tau}` |\n")
    lines.append(f"| $\\hbar/\\Lambda_C^2$ | `{prefactor}` |\n")
    lines.append(f"| total action | `{full}` |\n\n")
    lines.append("## Verdict\n\n")
    lines.append("The check passed: the action has dimension of $\\hbar$.\n" if ok else "The check failed.\n")
    lines.append("\nThis output does not determine the physical scale $\\ell_C$, $k_C$ or $E_C$.\n")

    out = OUT / "output_verify_normalized_action_dimension.md"
    out.write_text("".join(lines), encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
