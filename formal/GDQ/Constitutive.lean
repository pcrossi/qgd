import Mathlib.Analysis.SpecialFunctions.Exp
import Mathlib.Data.Complex.Basic

namespace GDQ

/-!
# Relações constitutivas elementares

Este arquivo formaliza somente identidades pontuais. Ainda não introduz
variedades, campos suaves ou a medida integral da ação.
-/

/--
Densidade constitutiva associada ao potencial complexo.

Como `(f + conj f) / 2 = Re f`, a definição oficial
`ρ = exp (-(f + conj f)/2)` reduz-se pontualmente à exponencial real abaixo.
-/
noncomputable def densityFromPotential (f : ℂ) : ℝ :=
  Real.exp (-f.re)

/-- A densidade constitutiva é estritamente positiva. -/
theorem densityFromPotential_pos (f : ℂ) :
    0 < densityFromPotential f := by
  exact Real.exp_pos (-f.re)

/-- A média de um número complexo e seu conjugado é sua parte real. -/
theorem conjugate_average_eq_real (f : ℂ) :
    (f + starRingEnd ℂ f) / 2 = (f.re : ℂ) := by
  apply Complex.ext
  · simp
  · simp

/-- A diferença de `f` e seu conjugado não possui parte real. -/
theorem conjugate_difference_re (f : ℂ) :
    (f - starRingEnd ℂ f).re = 0 := by
  simp

/-- A diferença contém duas vezes a parte imaginária de `f`. -/
theorem conjugate_difference_im (f : ℂ) :
    (f - starRingEnd ℂ f).im = 2 * f.im := by
  simp [two_mul]

/-- Forma real da fase constitutiva `S_R = ℏ Im f`. -/
def phaseFromPotential (ℏ : ℝ) (f : ℂ) : ℝ :=
  ℏ * f.im

end GDQ
