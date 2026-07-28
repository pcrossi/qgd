import Mathlib.Analysis.Calculus.Deriv.Basic
import Mathlib.Analysis.SpecialFunctions.ExpDeriv

namespace GDQ

/-!
# Identidade diferencial de Bohm no setor regular unidimensional

Este módulo formaliza a identidade local usada nos Capítulos 1 e 5. Ele não
postula a equação de Schrödinger nem modifica a ação oficial. Parte de uma
densidade positiva escrita como `ρ = exp q` e calcula as duas derivadas da
amplitude `sqrt ρ = exp (q / 2)`.

A versão riemanniana substitui as derivadas ordinárias por `∇` e `Δ_g`; sua
formalização requer a infraestrutura de cálculo em variedades e permanece uma
extensão posterior. A identidade abaixo certifica exatamente o núcleo
diferencial local já usado no manuscrito.
-/

/-- Amplitude positiva associada à log-densidade `q = log ρ`. -/
noncomputable def densityAmplitude (q : ℝ → ℝ) (x : ℝ) : ℝ :=
  Real.exp (q x / 2)

/-- Expressão local que será identificada com `R'' / R`. -/
noncomputable def bohmLogExpression (q₁ q₂ : ℝ) : ℝ :=
  q₂ / 2 + q₁ ^ 2 / 4

/--
Primeira derivada de `R = exp(q/2)`.
-/
theorem densityAmplitude_hasDerivAt
    {q : ℝ → ℝ} {x q₁ : ℝ}
    (hq : HasDerivAt q q₁ x) :
    HasDerivAt (densityAmplitude q)
      (densityAmplitude q x * (q₁ / 2)) x := by
  change HasDerivAt (fun y => Real.exp (q y / 2))
    (Real.exp (q x / 2) * (q₁ / 2)) x
  exact (hq.div_const 2).exp

/--
Derivada da expressão da primeira derivada. Sob `q' = q₁` e `q₁' = q₂`,
ela vale `R (q₂/2 + q₁²/4)`.
-/
theorem densityAmplitude_firstDerivative_hasDerivAt
    {q qPrime : ℝ → ℝ} {x q₁ q₂ : ℝ}
    (hq : HasDerivAt q q₁ x)
    (hqPrime : HasDerivAt qPrime q₂ x)
    (hqPrimeValue : qPrime x = q₁) :
    HasDerivAt
      (fun y => densityAmplitude q y * (qPrime y / 2))
      (densityAmplitude q x * bohmLogExpression q₁ q₂) x := by
  have hAmp := densityAmplitude_hasDerivAt hq
  have hHalfPrime := hqPrime.div_const 2
  convert hAmp.mul hHalfPrime using 1 <;> try rfl
  rw [hqPrimeValue]
  simp only [bohmLogExpression]
  ring

/--
Como `R = exp(q/2)` é não nula, a razão entre a segunda derivada local e a
amplitude reduz-se à expressão de Bohm em termos da log-densidade.
-/
theorem densityAmplitude_second_ratio
    (q₁ q₂ : ℝ) :
    (Real.exp (q₁ / 2) * bohmLogExpression q₁ q₂) /
        Real.exp (q₁ / 2)
      = bohmLogExpression q₁ q₂ := by
  field_simp [Real.exp_ne_zero]

/--
Forma algébrica usada na variação de Fisher:
`-2 Δq - |∇q|² = -4 Δsqrt(ρ)/sqrt(ρ)`.
-/
theorem fisherVariation_eq_bohmExpression
    (gradSq laplacian : ℝ) :
    -2 * laplacian - gradSq
      = -4 * (laplacian / 2 + gradSq / 4) := by
  ring

end GDQ
