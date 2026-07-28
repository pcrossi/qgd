import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.Tactic

namespace GDQ

/-!
# Projetores espectrais e pesos angulares de Stern--Gerlach

Este módulo formaliza o núcleo algébrico dos dois canais. Um observável
normalizado de Clifford satisfaz `s² = 1`; seus projetores espectrais são os
polinômios `(1 ± s)/2`. A realização matricial/Hopf, a Hessiana de interface
e a dinâmica do aparelho pertencem a módulos posteriores.
-/

/-- Projetor espectral escalar associado ao autovalor `+1`. -/
noncomputable def cliffordProjectorPlus (s : ℝ) : ℝ :=
  (1 + s) / 2

/-- Projetor espectral escalar associado ao autovalor `-1`. -/
noncomputable def cliffordProjectorMinus (s : ℝ) : ℝ :=
  (1 - s) / 2

/-- O projetor positivo é idempotente no espectro de uma involução. -/
theorem cliffordProjectorPlus_idempotent
    (s : ℝ) (hs : s ^ 2 = 1) :
    cliffordProjectorPlus s ^ 2 = cliffordProjectorPlus s := by
  unfold cliffordProjectorPlus
  nlinarith

/-- O projetor negativo é idempotente no espectro de uma involução. -/
theorem cliffordProjectorMinus_idempotent
    (s : ℝ) (hs : s ^ 2 = 1) :
    cliffordProjectorMinus s ^ 2 = cliffordProjectorMinus s := by
  unfold cliffordProjectorMinus
  nlinarith

/-- Os dois projetores são ortogonais. -/
theorem cliffordProjectors_orthogonal
    (s : ℝ) (hs : s ^ 2 = 1) :
    cliffordProjectorPlus s * cliffordProjectorMinus s = 0 := by
  unfold cliffordProjectorPlus cliffordProjectorMinus
  nlinarith

/-- Os dois canais formam uma decomposição completa. -/
theorem cliffordProjectors_complete (s : ℝ) :
    cliffordProjectorPlus s + cliffordProjectorMinus s = 1 := by
  unfold cliffordProjectorPlus cliffordProjectorMinus
  ring

/-- Peso do canal alinhado para eixos separados por `θ`. -/
noncomputable def sternGerlachPlusWeight (θ : ℝ) : ℝ :=
  (1 + Real.cos θ) / 2

/-- Peso do canal antialinhado para eixos separados por `θ`. -/
noncomputable def sternGerlachMinusWeight (θ : ℝ) : ℝ :=
  (1 - Real.cos θ) / 2

/-- Forma de meia-ângulo do peso alinhado. -/
theorem sternGerlachPlusWeight_eq_cos_sq_half (θ : ℝ) :
    sternGerlachPlusWeight θ = Real.cos (θ / 2) ^ 2 := by
  unfold sternGerlachPlusWeight
  rw [show θ = 2 * (θ / 2) by ring, Real.cos_two_mul]
  ring_nf

/-- Forma de meia-ângulo do peso antialinhado. -/
theorem sternGerlachMinusWeight_eq_sin_sq_half (θ : ℝ) :
    sternGerlachMinusWeight θ = Real.sin (θ / 2) ^ 2 := by
  unfold sternGerlachMinusWeight
  rw [show θ = 2 * (θ / 2) by ring, Real.cos_two_mul]
  rw [← Real.sin_sq_add_cos_sq (θ / 2)]
  ring_nf

/-- Normalização dos dois pesos. -/
theorem sternGerlachWeights_sum_one (θ : ℝ) :
    sternGerlachPlusWeight θ + sternGerlachMinusWeight θ = 1 := by
  unfold sternGerlachPlusWeight sternGerlachMinusWeight
  ring

/-- Positividade do peso alinhado. -/
theorem sternGerlachPlusWeight_nonneg (θ : ℝ) :
    0 ≤ sternGerlachPlusWeight θ := by
  rw [sternGerlachPlusWeight_eq_cos_sq_half]
  positivity

/-- Positividade do peso antialinhado. -/
theorem sternGerlachMinusWeight_nonneg (θ : ℝ) :
    0 ≤ sternGerlachMinusWeight θ := by
  rw [sternGerlachMinusWeight_eq_sin_sq_half]
  positivity

end GDQ
