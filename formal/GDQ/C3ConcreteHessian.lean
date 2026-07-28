import GDQ.C3Application
import Mathlib.Data.Fin.VecNotation
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators

/-!
# Hessiana concreta do setor reduzido `C₃`

O objetivo é retirar do certificado abstrato as identidades algébricas do
junction de três centros. O único dado dimensional deste bloco é a magnitude
primitiva `T`; nenhum valor experimental entra no cálculo.
-/

/--
Jacobiano do vínculo
`C = Σₐ T (cos θₐ, sin θₐ)` no equilíbrio
`(0, 2π/3, 4π/3)`.
-/
noncomputable def c3ClosureJacobian
    (T : ℝ) (v : ThreeCenterMode) : Fin 2 → ℝ :=
  ![
    T * (-(Real.sqrt 3 / 2) * v 1 + (Real.sqrt 3 / 2) * v 2),
    T * (v 0 - v 1 / 2 - v 2 / 2)
  ]

/-- Norma quadrática euclidiana em três componentes. -/
noncomputable def threeCenterNormSq (v : ThreeCenterMode) : ℝ :=
  ∑ i, v i ^ 2

/-- Norma quadrática do Jacobiano do fechamento. -/
noncomputable def closureJacobianNormSq
    (T : ℝ) (v : ThreeCenterMode) : ℝ :=
  ∑ i, c3ClosureJacobian T v i ^ 2

/--
Identidade de Gram do triângulo equilátero:
`D C† D C = (3/2) T² P_rel`.
-/
theorem c3ClosureJacobian_gram_identity
    (T : ℝ) (v : ThreeCenterMode) :
    closureJacobianNormSq T v =
      (3 / 2 : ℝ) * T ^ 2 *
        threeCenterNormSq (relativeThreeCenterProjector v) := by
  have hsqrt : (Real.sqrt 3) ^ 2 = (3 : ℝ) := by
    norm_num
  simp [closureJacobianNormSq, c3ClosureJacobian,
    threeCenterNormSq, relativeThreeCenterProjector, threeCenterMean,
    Fin.sum_univ_succ]
  ring_nf
  rw [hsqrt]
  ring

/-- O modo comum pertence ao kernel do Jacobiano do fechamento. -/
theorem c3ClosureJacobian_kills_common
    (T a : ℝ) :
    c3ClosureJacobian T (fun _ => a) = (fun _ => 0) := by
  funext i
  fin_cases i
  · change
      T * (-(Real.sqrt 3 / 2) * a + (Real.sqrt 3 / 2) * a) = 0
    ring
  · change T * (a - a / 2 - a / 2) = 0
    ring

/-- Num modo relativo, o projetor físico age como a identidade. -/
theorem relativeThreeCenterProjector_eq_self
    (v : ThreeCenterMode) (hv : ∑ i, v i = 0) :
    relativeThreeCenterProjector v = v := by
  funext i
  simp [relativeThreeCenterProjector, threeCenterMean, hv]

/-- Forma angular vinculada, incluindo a rigidez positiva `κ_rel`. -/
noncomputable def c3AngularEnergy
    (κ T : ℝ) (v : ThreeCenterMode) : ℝ :=
  κ * closureJacobianNormSq T v

/-- No setor relativo, a energia angular tem autovalor duplo `3κT²/2`. -/
theorem c3AngularEnergy_on_relative
    (κ T : ℝ) (v : ThreeCenterMode)
    (hv : ∑ i, v i = 0) :
    c3AngularEnergy κ T v =
      ((3 / 2 : ℝ) * κ * T ^ 2) * threeCenterNormSq v := by
  rw [c3AngularEnergy, c3ClosureJacobian_gram_identity,
    relativeThreeCenterProjector_eq_self v hv]
  ring

/-- A forma angular é estritamente positiva em todo modo relativo não nulo. -/
theorem c3AngularEnergy_pos
    {κ T : ℝ} (hκ : 0 < κ) (hT : T ≠ 0)
    {v : ThreeCenterMode}
    (hvrel : ∑ i, v i = 0) (hv : v ≠ 0) :
    0 < c3AngularEnergy κ T v := by
  rw [c3AngularEnergy_on_relative κ T v hvrel]
  have hnorm : 0 < threeCenterNormSq v := by
    classical
    have : ∃ i, v i ≠ 0 := by
      by_contra h
      apply hv
      funext i
      by_contra hi
      exact h ⟨i, hi⟩
    obtain ⟨i, hi⟩ := this
    rw [threeCenterNormSq]
    simpa using Finset.sum_pos'
      (s := Finset.univ)
      (fun j _ => sq_nonneg (v j))
      ⟨i, Finset.mem_univ i, sq_pos_of_ne_zero hi⟩
  positivity

/-- Autovalor do operador de Ornstein--Uhlenbeck ponderado. -/
noncomputable def ouEigenvalue (τ : ℝ) (m : Nat) : ℝ :=
  (m : ℝ) / (2 * τ)

/-- Depois de remover `m=0`, todo nível OU é limitado por `1/(2τ)`. -/
theorem ouEigenvalue_lower_bound
    {τ : ℝ} (hτ : 0 < τ) {m : Nat} (hm : 1 ≤ m) :
    1 / (2 * τ) ≤ ouEigenvalue τ m := by
  unfold ouEigenvalue
  apply div_le_div_of_nonneg_right
  · exact_mod_cast hm
  · positivity

/-- Todo nível OU físico é positivo. -/
theorem ouEigenvalue_pos
    {τ : ℝ} (hτ : 0 < τ) {m : Nat} (hm : 1 ≤ m) :
    0 < ouEigenvalue τ m := by
  unfold ouEigenvalue
  positivity

/-- Gap radial homogêneo derivado para o fundo gaussiano. -/
noncomputable def c3RadialHomogeneousGap (τ : ℝ) : ℝ :=
  3 / (2 * τ)

theorem c3RadialHomogeneousGap_pos
    {τ : ℝ} (hτ : 0 < τ) :
    0 < c3RadialHomogeneousGap τ := by
  unfold c3RadialHomogeneousGap
  positivity

/--
O bloco misto nulo deixa o complemento de Schur igual ao bloco angular.
-/
theorem schur_eq_angular_of_mixed_zero
    (angular correction : ℝ) (hcorrection : correction = 0) :
    angular - correction = angular := by
  simp [hcorrection]

/--
O menor dos blocos angular, radial, fase e métrico é a fórmula já usada no
gap `C₃`. O bloco radial `3/(2τ)` e o bloco de fase `1/τ` são maiores que o
primeiro nível métrico/dilatônico `1/(2τ)`.
-/
theorem c3_reduced_gap_formula
    {κT2 τ : ℝ} (_hκ : 0 < κT2) (hτ : 0 < τ) :
    min
      (min ((3 / 2 : ℝ) * κT2) (3 / (2 * τ)))
      (min (1 / τ) (1 / (2 * τ))) =
      c3PhysicalGap κT2 τ := by
  have hden : 0 < 2 * τ := by positivity
  rw [c3PhysicalGap]
  have hrad : 1 / (2 * τ) ≤ 3 / (2 * τ) := by
    apply div_le_div_of_nonneg_right
    · norm_num
    · positivity
  have hphase : 1 / (2 * τ) ≤ 1 / τ := by
    have htwo : τ ≤ 2 * τ := by linarith
    exact one_div_le_one_div_of_le hτ htwo
  rw [min_eq_right hphase]
  rw [min_assoc, min_eq_right hrad]

end GDQ
