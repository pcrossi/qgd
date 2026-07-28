import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.Complex.Basic

namespace GDQ

/-!
# Contorno causal

O contorno é parametrizado por uma variável real `t`, mas não identificamos
`t` automaticamente com o tempo físico. A estrutura guarda a curva complexa,
sua derivada e a condição de que ela não atravesse a origem.
-/

/-- Contorno causal regular no plano complexo do parâmetro de fluxo. -/
structure CausalContour where
  z : ℝ → ℂ
  dz : ℝ → ℂ
  nonzero : ∀ t, z t ≠ 0
  hasDeriv : ∀ t, HasDerivAt z (dz t) t

/-- Coeficiente do pullback da forma logarítmica `dτ/τ`. -/
noncomputable def CausalContour.dlog (γ : CausalContour) (t : ℝ) : ℂ :=
  γ.dz t / γ.z t

/-- O denominador do pullback logarítmico é sempre admissível. -/
theorem CausalContour.dlog_denominator_ne_zero
    (γ : CausalContour) (t : ℝ) :
    γ.z t ≠ 0 := by
  exact γ.nonzero t

/--
Se a derivada do contorno não se anula, o coeficiente logarítmico também não
se anula.
-/
theorem CausalContour.dlog_ne_zero
    (γ : CausalContour) (t : ℝ) (h : γ.dz t ≠ 0) :
    γ.dlog t ≠ 0 := by
  exact div_ne_zero h (γ.nonzero t)

end GDQ
