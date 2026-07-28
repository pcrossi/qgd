import GDQ.ConformalTorsionHessian
import GDQ.PhysicalProjector
import Mathlib.Tactic

namespace GDQ

/-!
# Hessiana torsional projetada no setor reduzido

Este módulo fortalece somente o resultado autorizado pela ação reduzida:

* deriva a segunda variação exata na amplitude geométrica `a`;
* constrói o setor físico de dois modos já depois dos vínculos e do gauge;
* fornece uma cota explícita de gap sob dominância diagonal verificável.

Os coeficientes do modo adicional não são escolhidos aqui. Em particular,
o módulo não afirma estabilidade da Hessiana 8D completa.
-/

/-- Segunda variação da ação reduzida em relação à amplitude `a`. -/
noncomputable def normalizedTorsionHessianA
    (q τ a : ℝ) : ℝ :=
  2 * τ * normalizedTorsionSlope q (τ * a ^ 2) +
    (2 * τ * a) *
      (normalizedTorsionSlopeDerivative q (τ * a ^ 2) *
        (τ * (a + a)))

/-- A fórmula acima é de fato a derivada da primeira variação em `a`. -/
theorem normalizedTorsionFirstVariationInA_hasDerivAt
    (q τ a : ℝ) :
    HasDerivAt (normalizedTorsionFirstVariationInA q τ)
      (normalizedTorsionHessianA q τ a) a := by
  have hu := (hasDerivAt_pow 2 a).const_mul τ
  have hs :=
    (normalizedTorsionSlope_hasDerivAt q (τ * a ^ 2)).comp a hu
  have hp := ((hasDerivAt_id a).const_mul (2 * τ)).mul hs
  apply (hp.congr_of_eventuallyEq ?_).congr_deriv
  · simp only [id_eq, mul_one]
    unfold normalizedTorsionHessianA
    simp only [Function.comp_apply]
    ring
  · exact Filter.Eventually.of_forall (fun x ↦ by
      change
        2 * τ * x * normalizedTorsionSlope q (τ * x ^ 2) =
          normalizedTorsionFirstVariationInA q τ x
      rfl)

/-- Na sela não nula, desaparece o termo proporcional à primeira variação. -/
theorem normalizedTorsionHessianA_at_saddle
    {q τ a : ℝ}
    (hroot : normalizedTorsionSlope q (τ * a ^ 2) = 0) :
    normalizedTorsionHessianA q τ a =
      4 * τ * (τ * a ^ 2) *
        normalizedTorsionSlopeDerivative q (τ * a ^ 2) := by
  simp [normalizedTorsionHessianA, hroot]
  ring

/-- A Hessiana em `a` é positiva no ramo torsional físico. -/
theorem normalizedTorsionHessianA_pos_at_saddle
    {q τ a : ℝ}
    (hq : 0 < q) (hτ : 0 < τ)
    (ha : a ≠ 0)
    (huU : τ * a ^ 2 < 5 / 42)
    (hroot : normalizedTorsionSlope q (τ * a ^ 2) = 0) :
    0 < normalizedTorsionHessianA q τ a := by
  rw [normalizedTorsionHessianA_at_saddle hroot]
  have hu0 : 0 < τ * a ^ 2 := mul_pos hτ (sq_pos_of_ne_zero ha)
  exact normalizedTorsionSaddle_secondCoefficient_pos
    hq hτ hu0 huU

/-- Espaço dos dois modos físicos reduzidos: amplitude torsional e um modo adicional. -/
abbrev TorsionTwoMode := EuclideanSpace ℝ (Fin 2)

/--
Depois de impor os vínculos e remover gauge, o espaço reduzido de dois modos
é todo físico. O projetor é construído pelo mecanismo geral.
-/
noncomputable def torsionTwoModePhysicalSector :
    OrthogonalPhysicalSector TorsionTwoMode :=
  finiteDimensionalOrthogonalPhysicalSector ⊤ ⊥

/-- No setor já reduzido, o projetor físico age como a identidade. -/
theorem torsionTwoModePhysicalProjector_eq_self
    (v : TorsionTwoMode) :
    torsionTwoModePhysicalSector.projector v = v := by
  rw [torsionTwoModePhysicalSector.projector_eq_self_iff]
  change
    v ∈ (⊤ : Submodule ℝ TorsionTwoMode) ∧
      v ∈ (⊥ : Submodule ℝ TorsionTwoMode)ᗮ
  refine ⟨Submodule.mem_top, ?_⟩
  rw [Submodule.mem_orthogonal]
  intro w hw
  have : w = 0 := by simpa using hw
  subst w
  simp

/-- Norma quadrática coordenada do setor de dois modos. -/
def torsionTwoModeNormSq (x y : ℝ) : ℝ :=
  x ^ 2 + y ^ 2

/-- Cota inferior universal do termo cruzado. -/
theorem coupled_crossTerm_lower_bound
    (kab x y : ℝ) :
    -|kab| * (x ^ 2 + y ^ 2) ≤ 2 * kab * x * y := by
  by_cases hkab : 0 ≤ kab
  · rw [abs_of_nonneg hkab]
    have hs : 0 ≤ (x + y) ^ 2 := sq_nonneg _
    have hm : 0 ≤ kab * (x + y) ^ 2 := mul_nonneg hkab hs
    nlinarith
  · have hkabNeg : kab < 0 := lt_of_not_ge hkab
    rw [abs_of_neg hkabNeg]
    have hs : 0 ≤ (x - y) ^ 2 := sq_nonneg _
    have hm : 0 ≤ (-kab) * (x - y) ^ 2 :=
      mul_nonneg (neg_nonneg.mpr hkabNeg.le) hs
    nlinarith

/-- Gap explícito fornecido por dominância diagonal. -/
noncomputable def coupledDiagonalGap
    (kaa kab kbb : ℝ) : ℝ :=
  min (kaa - |kab|) (kbb - |kab|)

/-- A dominância diagonal estrita torna a cota de gap positiva. -/
theorem coupledDiagonalGap_pos
    {kaa kab kbb : ℝ}
    (ha : |kab| < kaa) (hb : |kab| < kbb) :
    0 < coupledDiagonalGap kaa kab kbb := by
  rw [coupledDiagonalGap, lt_min_iff]
  exact ⟨sub_pos.mpr ha, sub_pos.mpr hb⟩

/-- A forma Hessiana domina o gap explícito vezes a norma coordenada. -/
theorem coupledHessianQuadratic_ge_diagonalGap
    (kaa kab kbb x y : ℝ) :
    coupledDiagonalGap kaa kab kbb * torsionTwoModeNormSq x y ≤
      coupledHessianQuadratic kaa kab kbb x y := by
  have hcross := coupled_crossTerm_lower_bound kab x y
  have hga :
      coupledDiagonalGap kaa kab kbb ≤ kaa - |kab| :=
    min_le_left _ _
  have hgb :
      coupledDiagonalGap kaa kab kbb ≤ kbb - |kab| :=
    min_le_right _ _
  have hx : 0 ≤ x ^ 2 := sq_nonneg x
  have hy : 0 ≤ y ^ 2 := sq_nonneg y
  have hgax :
      coupledDiagonalGap kaa kab kbb * x ^ 2 ≤
        (kaa - |kab|) * x ^ 2 :=
    mul_le_mul_of_nonneg_right hga hx
  have hgay :
      coupledDiagonalGap kaa kab kbb * y ^ 2 ≤
        (kbb - |kab|) * y ^ 2 :=
    mul_le_mul_of_nonneg_right hgb hy
  unfold torsionTwoModeNormSq coupledHessianQuadratic
  nlinarith

/--
Aplicação ao bloco conformal derivado. Os coeficientes `kab` e `kbb`
continuam dados a calcular na Hessiana dos modos adicionais.
-/
theorem torsionReducedProjectedGap
    {q τ a kab kbb : ℝ}
    (hq : 0 < q) (hτ : 0 < τ)
    (ha : a ≠ 0)
    (huU : τ * a ^ 2 < 5 / 42)
    (hroot : normalizedTorsionSlope q (τ * a ^ 2) = 0)
    (hdomA : |kab| < normalizedTorsionHessianA q τ a)
    (hdomB : |kab| < kbb) :
    0 < coupledDiagonalGap
        (normalizedTorsionHessianA q τ a) kab kbb ∧
      ∀ x y,
        coupledDiagonalGap
            (normalizedTorsionHessianA q τ a) kab kbb *
            torsionTwoModeNormSq x y ≤
          coupledHessianQuadratic
            (normalizedTorsionHessianA q τ a) kab kbb x y := by
  have _hkaa :
      0 < normalizedTorsionHessianA q τ a :=
    normalizedTorsionHessianA_pos_at_saddle
      hq hτ ha huU hroot
  exact
    ⟨coupledDiagonalGap_pos hdomA hdomB,
      fun x y ↦ coupledHessianQuadratic_ge_diagonalGap _ _ _ x y⟩

end GDQ
