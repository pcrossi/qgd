import GDQ.KoideGeometry
import GDQ.ConformalTorsionConstraintTangent
import GDQ.PerelmanProductReduction
import Mathlib.LinearAlgebra.Dimension.Finite
import Mathlib.Tactic

namespace GDQ

/-!
# Hierarquia leptônica reduzida e herança por Schur

Este módulo certifica a álgebra da rota intrínseca reduzida usada no
Capítulo 15:

* composição da razão do múon a partir dos três termos geométricos já
  identificados no modelo reduzido;
* construção do ramo pesado da saturação tridimensional;
* impossibilidade de quatro direções linearmente independentes em dimensão
  três;
* preservação das razões no background produto quando o bloco misto de
  Schur se anula;
* critério subcrítico de estabilidade no setor warped/misto.

O módulo não deriva os coeficientes `2/3`, `6/5` e `2 α` da ação oficial
completa. Eles são os dados geométricos do modelo reduzido documentado no
manuscrito. Também não converte razões adimensionais em massas absolutas.
-/

/-- Fração de suporte biespacial usada no setor reduzido do múon. -/
noncomputable def biespatialSupportFraction : ℝ := 2 / 3

/-- Contribuição de interface reduzida. -/
noncomputable def reducedBoundaryImpedance : ℝ := 6 / 5

/-- Contribuição de duas circulações ortogonais. -/
def reducedCirculationSelfEnergy (alpha : ℝ) : ℝ := 2 * alpha

/-- Termo líder da razão do múon. -/
noncomputable def reducedMuonLeadingRatio (alpha : ℝ) : ℝ :=
  1 / (biespatialSupportFraction * alpha)

/-- Razão reduzida completa do múon. -/
noncomputable def reducedMuonRatio (alpha : ℝ) : ℝ :=
  3 / (2 * alpha) + 6 / 5 + 2 * alpha

/-- A decomposição geométrica reduzida reproduz a fórmula compacta. -/
theorem reducedMuonRatio_decomposition
    {alpha : ℝ} (halpha : alpha ≠ 0) :
    reducedMuonLeadingRatio alpha +
        reducedBoundaryImpedance +
        reducedCirculationSelfEnergy alpha =
      reducedMuonRatio alpha := by
  unfold reducedMuonLeadingRatio biespatialSupportFraction
    reducedBoundaryImpedance reducedCirculationSelfEnergy reducedMuonRatio
  field_simp [halpha]

/-- Para estrutura fina positiva, a razão reduzida do múon é positiva. -/
theorem reducedMuonRatio_pos
    {alpha : ℝ} (halpha : 0 < alpha) :
    0 < reducedMuonRatio alpha := by
  unfold reducedMuonRatio
  positivity

/-- Discriminante da equação de saturação escrito em amplitudes. -/
def koideBranchDiscriminant (a b : ℝ) : ℝ :=
  3 * a ^ 2 + 12 * a * b + 3 * b ^ 2

/-- Amplitude do ramo leve. -/
noncomputable def koideLightAmplitude (a b : ℝ) : ℝ :=
  2 * (a + b) - Real.sqrt (koideBranchDiscriminant a b)

/-- Amplitude do ramo pesado. -/
noncomputable def koideHeavyAmplitude (a b : ℝ) : ℝ :=
  2 * (a + b) + Real.sqrt (koideBranchDiscriminant a b)

/-- Razão pesada associada às duas primeiras razões não negativas. -/
noncomputable def heavyLeptonicRatio (r₁ r₂ : ℝ) : ℝ :=
  (koideHeavyAmplitude (Real.sqrt r₁) (Real.sqrt r₂)) ^ 2

/-- O ramo pesado satisfaz exatamente a equação polinomial de Koide. -/
theorem koideHeavyAmplitude_satisfies
    {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    3 * koideQuadratic a b (koideHeavyAmplitude a b) =
      2 * (a + b + koideHeavyAmplitude a b) ^ 2 := by
  simpa [koideHeavyAmplitude, koideBranchDiscriminant] using
    (koide_heavy_branch_satisfies ha hb)

/-- O quadrado do ramo pesado não é menor que o do ramo leve. -/
theorem koide_heavy_ratio_ge_light
    {a b : ℝ} (ha : 0 ≤ a) (hb : 0 ≤ b) :
    (koideLightAmplitude a b) ^ 2 ≤
      (koideHeavyAmplitude a b) ^ 2 := by
  have hdisc : 0 ≤ koideBranchDiscriminant a b := by
    unfold koideBranchDiscriminant
    positivity
  have hsqrt : 0 ≤ Real.sqrt (koideBranchDiscriminant a b) :=
    Real.sqrt_nonneg _
  unfold koideLightAmplitude koideHeavyAmplitude
  nlinarith

/--
Não existem quatro direções linearmente independentes no suporte real
tridimensional.
-/
theorem no_four_independent_directions_in_three_space
    (v : Fin 4 → (Fin 3 → ℝ)) :
    ¬LinearIndependent ℝ v := by
  intro h
  have hcard := h.fintype_card_le_finrank
  norm_num at hcard

/-- Autovalor efetivo depois da eliminação de um bloco transversal escalar. -/
noncomputable def scalarSchurEigenvalue
    (base mixed transverse : ℝ) : ℝ :=
  base - mixed ^ 2 / transverse

/-- No background produto, o bloco misto nulo não desloca o autovalor. -/
theorem scalarSchurEigenvalue_eq_base_of_mixed_zero
    (base mixed transverse : ℝ)
    (hmixed : mixed = 0) :
    scalarSchurEigenvalue base mixed transverse = base := by
  simp [scalarSchurEigenvalue, hmixed]

/-- Razão de dois autovalores físicos corrigidos por Schur. -/
noncomputable def schurCorrectedRatio
    (lambdaRef lambdaMode mixedRef mixedMode
      transverseRef transverseMode : ℝ) : ℝ :=
  scalarSchurEigenvalue lambdaMode mixedMode transverseMode /
    scalarSchurEigenvalue lambdaRef mixedRef transverseRef

/-- Blocos mistos nulos preservam exatamente a razão reduzida. -/
theorem schurCorrectedRatio_eq_reduced_of_product
    (lambdaRef lambdaMode mixedRef mixedMode
      transverseRef transverseMode : ℝ)
    (hRef : mixedRef = 0)
    (hMode : mixedMode = 0) :
    schurCorrectedRatio lambdaRef lambdaMode mixedRef mixedMode
        transverseRef transverseMode =
      lambdaMode / lambdaRef := by
  simp [schurCorrectedRatio,
    scalarSchurEigenvalue_eq_base_of_mixed_zero _ _ _ hRef,
    scalarSchurEigenvalue_eq_base_of_mixed_zero _ _ _ hMode]

/--
Critério escalar subcrítico: se a correção de Schur é menor que o gap de
base, o autovalor efetivo permanece positivo.
-/
theorem scalarSchurEigenvalue_pos_of_subcritical
    {base mixed transverse : ℝ}
    (_htransverse : 0 < transverse)
    (hsubcritical : mixed ^ 2 / transverse < base) :
    0 < scalarSchurEigenvalue base mixed transverse := by
  unfold scalarSchurEigenvalue
  linarith

end GDQ
