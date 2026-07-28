import GDQ.FlowKernel

namespace GDQ

/-!
# Densidade pontual da ação oficial

Este arquivo formaliza o colchete e o prefator pontuais da ação. Não declara
que a integral existe. A integração será introduzida somente depois de fixar
medida, domínio, regularidade e integrabilidade.
-/

/-- Colchete real da ação oficial em um ponto. -/
def officialBracket
    (n : Nat) (τ scalarCurvature gradientNormSq realPotential : ℝ) : ℝ :=
  τ * (scalarCurvature + gradientNormSq) + realPotential - n

/--
Densidade pontual real na seção euclidiana.

`volumeDensity` representa `sqrt(det g)` e permanece um dado explícito.
-/
noncomputable def officialPointDensity
    (n : Nat)
    (ℏ ΛC τ scalarCurvature gradientNormSq realPotential kernel
      volumeDensity : ℝ) : ℝ :=
  (ℏ / ΛC ^ 2) *
    officialBracket n τ scalarCurvature gradientNormSq realPotential *
    kernel * volumeDensity

/-- A definição não contém termo adicional além dos fatores oficiais. -/
theorem officialPointDensity_unfold
    (n : Nat)
    (ℏ ΛC τ scalarCurvature gradientNormSq realPotential kernel
      volumeDensity : ℝ) :
    officialPointDensity n ℏ ΛC τ scalarCurvature gradientNormSq
        realPotential kernel volumeDensity =
      (ℏ / ΛC ^ 2) *
        (τ * (scalarCurvature + gradientNormSq) + realPotential - n) *
        kernel * volumeDensity := by
  rfl

end GDQ
