import Mathlib.Tactic

namespace GDQ

/-!
# Identidade off-shell de Noether

Este arquivo certifica o núcleo algébrico da identidade de Noether usada na
GDQ. A primeira variação é decomposta em termo de Euler--Lagrange e divergência
de potencial simplético. Para uma simetria, a mesma variação é uma divergência
de bordo. A subtração fornece a corrente de Noether.

O arquivo não postula uma nova ação e não substitui a análise funcional da
ação oficial: as duas fórmulas de primeira variação entram como hipóteses
tipadas, a serem verificadas no domínio e contorno considerados.
-/

/--
Identidade off-shell: se a primeira variação admite simultaneamente as
decomposições

`δL = E·δΦ + div Θ` e `δL = div B`,

então a divergência da corrente `J = Θ - B` é `-E·δΦ`.
-/
theorem noether_off_shell_identity
    (variation eulerPair divTheta divBoundary : ℝ)
    (hFirstVariation : variation = eulerPair + divTheta)
    (hSymmetry : variation = divBoundary) :
    divTheta - divBoundary = -eulerPair := by
  linarith

/-- No setor on-shell, a corrente de Noether é conservada. -/
theorem noether_on_shell_conservation
    (variation eulerPair divTheta divBoundary : ℝ)
    (hFirstVariation : variation = eulerPair + divTheta)
    (hSymmetry : variation = divBoundary)
    (hOnShell : eulerPair = 0) :
    divTheta - divBoundary = 0 := by
  rw [noether_off_shell_identity variation eulerPair divTheta divBoundary
    hFirstVariation hSymmetry, hOnShell, neg_zero]

/--
Forma integrada: a carga é constante quando sua derivada é a divergência
integrada da corrente e esta se anula pelo domínio/contorno físico.
-/
theorem noether_charge_constant
    (chargeDerivative integratedDivergence : ℝ)
    (hBalance : chargeDerivative = -integratedDivergence)
    (hBoundary : integratedDivergence = 0) :
    chargeDerivative = 0 := by
  linarith

end GDQ
