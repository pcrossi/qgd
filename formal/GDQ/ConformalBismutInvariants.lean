import GDQ.ConformalBismutBackground
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators Matrix

/-!
# Curvatura e invariantes oficiais do background torsional

As contrações abaixo usam a conexão de Bismut já verificada. Como seus
coeficientes são constantes no ansatz linear, a curvatura provém dos produtos
quadráticos `ΓΓ`; não se reutiliza a curvatura do controle plano `H=0`.
-/

/-- Diagonal de Ricci da conexão torsional, antes do fator `a²`. -/
def conformalBismutRicciWeight (i : Index8) : ℝ :=
  if i = 0 then 0 else
  if i = 4 then -12 else -8

/-- A conexão do ansatz é homogênea de grau um em `a`. -/
theorem conformalBismutConnectionConstant_homogeneous
    (a : ℝ) (k i j : Index8) :
    conformalBismutConnectionConstant a k i j =
      a * conformalBismutConnectionConstant 1 k i j := by
  unfold conformalBismutConnectionConstant
    conformalLeviCivitaConnection conformalPhiGradient
    conformalTorsionNormalized conformalDOmegaNormalized
  split_ifs <;> ring

/-- Contração puramente numérica que multiplica `a²` em Ricci. -/
noncomputable def conformalBismutRicciCoefficient
    (i j : Index8) : ℝ :=
  ∑ l, ∑ m,
    (conformalBismutConnectionConstant 1 l l m *
        conformalBismutConnectionConstant 1 m j i -
      conformalBismutConnectionConstant 1 l j m *
        conformalBismutConnectionConstant 1 m l i)

/-- A curvatura de Ricci separa exatamente o fator `a²`. -/
theorem conformalCoordinate_ricci_factor
    (a τ f₀ : ℝ) (x : LocalPoint) (i j : Index8) :
    (conformalCoordinateBismutBackground a τ f₀).ricci x i j =
      a ^ 2 * conformalBismutRicciCoefficient i j := by
  unfold CoordinateBismutBackground.ricci
    CoordinateBismutBackground.riemann
    conformalBismutRicciCoefficient
  simp only [conformalCoordinateBismutBackground, zero_sub]
  simp only [neg_zero, zero_add]
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro l hl
  rw [Finset.mul_sum]
  apply Finset.sum_congr rfl
  intro m hm
  rw [conformalBismutConnectionConstant_homogeneous a,
    conformalBismutConnectionConstant_homogeneous a,
    conformalBismutConnectionConstant_homogeneous a,
    conformalBismutConnectionConstant_homogeneous a]
  ring

set_option maxHeartbeats 1000000
set_option maxRecDepth 100000

/-- A contração diagonal puramente numérica vale `-60`. -/
theorem conformalBismutRicciCoefficient_trace :
    ∑ i : Index8, conformalBismutRicciCoefficient i i = -60 := by
  simp only [conformalBismutRicciCoefficient, Fin.sum_univ_succ]
  norm_num [conformalBismutConnectionConstant,
    conformalLeviCivitaConnection,
    conformalTorsionNormalized, conformalDOmegaNormalized,
    conformalPhiGradient, delta8,
    standardFundamentalForm, standardJPartner, standardJSign,
    Fin.ext_iff]
set_option maxHeartbeats 200000
set_option maxRecDepth 1000

/-- Curvatura escalar exata da conexão de Bismut conformal. -/
theorem conformalCoordinate_scalarCurvature
    (a τ f₀ : ℝ) (x : LocalPoint) :
    (conformalCoordinateBismutBackground a τ f₀).scalarCurvature x =
      -60 * a ^ 2 * (conformalScale a x)⁻¹ := by
  change
    (∑ i, ∑ j,
      conformalRealInverseMetric a x i j *
        (conformalCoordinateBismutBackground a τ f₀).ricci x i j) =
      -60 * a ^ 2 * (conformalScale a x)⁻¹
  simp only [conformalRealInverseMetric]
  rw [show
      (∑ i, ∑ j,
        ((conformalScale a x)⁻¹ * delta8 i j) *
          (conformalCoordinateBismutBackground a τ f₀).ricci x i j) =
        ∑ i,
          (conformalScale a x)⁻¹ *
            (conformalCoordinateBismutBackground a τ f₀).ricci x i i by
      apply Finset.sum_congr rfl
      intro i hi
      classical
      simp [delta8]]
  rw [show
      (∑ i,
        (conformalScale a x)⁻¹ *
          (conformalCoordinateBismutBackground a τ f₀).ricci x i i) =
        (conformalScale a x)⁻¹ *
          ∑ i, a ^ 2 * conformalBismutRicciCoefficient i i by
      rw [Finset.mul_sum]
      apply Finset.sum_congr rfl
      intro i hi
      rw [conformalCoordinate_ricci_factor]]
  rw [← Finset.mul_sum, conformalBismutRicciCoefficient_trace]
  ring

/-- Norma do gradiente gaussiano na métrica real conformal. -/
theorem conformalCoordinate_gradientNormSq
    (a τ f₀ : ℝ) (x : LocalPoint) :
    (conformalCoordinateBismutBackground a τ f₀).gradientNormSq x =
      (conformalScale a x)⁻¹ * gaussianGradientNormSq τ x.1 := by
  unfold CoordinateBismutBackground.gradientNormSq
    conformalCoordinateBismutBackground
    conformalRealInverseMetric
  classical
  simp only [delta8]
  simp
  unfold gaussianGradientNormSq
  simp only [Fin.sum_univ_succ]
  norm_num [conformalGaussianPotentialDerivative,
    gaussianPotentialGradient, Fin.ext_iff]
  ring

/-- Invariantes oficiais produzidos diretamente pelo background torsional. -/
noncomputable def conformalBismutInvariants
    (a τ f₀ : ℝ) : EuclideanGeometricInvariants :=
  (conformalCoordinateBismutBackground a τ f₀).toGeometricInvariants

@[simp] theorem conformalBismutInvariants_scalarCurvature
    (a τ f₀ t : ℝ) (x : LocalPoint) :
    (conformalBismutInvariants a τ f₀).scalarCurvature t x =
      -60 * a ^ 2 * (conformalScale a x)⁻¹ := by
  exact conformalCoordinate_scalarCurvature a τ f₀ x

@[simp] theorem conformalBismutInvariants_volumeDensity
    (a τ f₀ t : ℝ) (x : LocalPoint) :
    (conformalBismutInvariants a τ f₀).volumeDensity t x =
      (conformalScale a x) ^ 4 := by
  exact conformalCoordinate_volumeDensity a τ f₀ x

@[simp] theorem conformalBismutInvariants_gradientNormSq
    (a τ f₀ t : ℝ) (x : LocalPoint) :
    (conformalBismutInvariants a τ f₀).gradientNormSq t x =
      (conformalScale a x)⁻¹ * gaussianGradientNormSq τ x.1 := by
  exact conformalCoordinate_gradientNormSq a τ f₀ x

end GDQ
