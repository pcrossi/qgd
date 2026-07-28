import Mathlib.Algebra.Lie.Basic

namespace GDQ

/-!
# Potenciais de Killing como representação de Lie

No setor local onde os potenciais Hamiltonianos existem, o mapa que envia um
gerador geométrico ao seu potencial é um homomorfismo de Lie. O colchete no
alvo representa o colchete de Poisson.

A existência global dos potenciais e sua colagem no fibrado não é inferida
por este módulo; ela permanece hipótese geométrica explícita.
-/

variable {R 𝔤 P : Type*}
  [CommRing R]
  [LieRing 𝔤] [LieAlgebra R 𝔤]
  [LieRing P] [LieAlgebra R P]

/-- Realização local dos geradores por potenciais de Killing/Poisson. -/
structure KillingPotentialRealization where
  potential : 𝔤 →ₗ⁅R⁆ P

/-- O mapa de potenciais preserva exatamente o colchete de Lie/Poisson. -/
theorem killingPotential_preserves_bracket
    (K : KillingPotentialRealization (R := R) (𝔤 := 𝔤) (P := P))
    (x y : 𝔤) :
    K.potential ⁅x, y⁆ = ⁅K.potential x, K.potential y⁆ :=
  K.potential.map_lie x y

/--
Se o mapa local é injetivo, uma relação entre potenciais reflete uma relação
entre os geradores geométricos.
-/
theorem killingPotential_reflects_bracket
    (K : KillingPotentialRealization (R := R) (𝔤 := 𝔤) (P := P))
    (hinj : Function.Injective K.potential)
    (x y z : 𝔤)
    (hP : ⁅K.potential x, K.potential y⁆ = K.potential z) :
    ⁅x, y⁆ = z := by
  apply hinj
  rw [K.potential.map_lie]
  exact hP

end GDQ
