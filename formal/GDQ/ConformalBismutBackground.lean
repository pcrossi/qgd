import GDQ.ConformalBismutConnection
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators Matrix

/-!
# Background coordenado material com torção

Este módulo reúne a métrica conformal, a estrutura complexa padrão, a
conexão de Bismut e o potencial gaussiano num
`CoordinateBismutBackground`.

O objeto resultante satisfaz diretamente:

* positividade e inversibilidade da métrica;
* `J²=-1` e integrabilidade do `J` constante;
* `∇ᴮg=0`;
* `∇ᴮJ=0`;
* `Tᴮ=H=d_J^cω`;
* positividade da norma do gradiente do potencial.

A construção é local no bulk `ℝ⁴×T⁴`. Não prova, por si só, completude
geodésica nem condições globais no toro.
-/

/-- Gradiente real do potencial gaussiano inserido nos oito eixos reais. -/
noncomputable def conformalGaussianPotentialDerivative
    (τ : ℝ) (x : LocalPoint) (i : Index8) : ℝ :=
  match i.1 with
  | 0 => gaussianPotentialGradient τ x.1 0
  | 1 => gaussianPotentialGradient τ x.1 1
  | 2 => gaussianPotentialGradient τ x.1 2
  | 3 => gaussianPotentialGradient τ x.1 (Fin.succ 2)
  | _ => 0

/-- A norma quadrática diagonal do gradiente é não negativa. -/
theorem conformalGaussianGradientNorm_nonneg
    (a τ : ℝ) (x : LocalPoint) :
    0 ≤
      ∑ i, ∑ j,
        conformalRealInverseMetric a x i j *
          (conformalGaussianPotentialDerivative τ x i *
              conformalGaussianPotentialDerivative τ x j +
            0 * 0) := by
  classical
  simp only [conformalRealInverseMetric, delta8]
  simp
  apply Finset.sum_nonneg
  intro i hi
  exact mul_nonneg
    (le_of_lt (inv_pos.mpr (conformalScale_pos a x)))
    (by
      simpa [pow_two] using
        sq_nonneg (conformalGaussianPotentialDerivative τ x i))

/--
Background coordenado de Bismut associado à configuração material conformal.

As derivadas da conexão são nulas porque
`conformalBismutConnection_eq_constant` prova que todos os seus coeficientes
são independentes da posição para `φ=a x⁰`.
-/
noncomputable def conformalCoordinateBismutBackground
    (a τ f₀ : ℝ) :
    CoordinateBismutBackground (conformalMaterialAdmissible a τ f₀) where
  metric := fun x i j ↦ conformalRealMetric a x i j
  inverseMetric := fun x i j ↦ conformalRealInverseMetric a x i j
  metricDerivative :=
    fun x p i j ↦ conformalRealMetricDerivative a x p i j
  connection := fun _ k i j ↦
    conformalBismutConnectionConstant a k i j
  connectionDerivative := fun _ _ _ _ _ ↦ 0
  complexCoeff := fun _ i j ↦ standardComplexCoeff i j
  complexDerivative := fun _ _ _ _ ↦ 0
  potentialDerivativeRe :=
    fun x i ↦ conformalGaussianPotentialDerivative τ x i
  potentialDerivativeIm := fun _ _ ↦ 0
  metric_symmetric := by
    intro x i j
    exact conformalRealMetric_symmetric a x i j
  metric_positive := by
    intro x v hv
    exact conformalRealMetric_positive a x v hv
  metric_det_pos := by
    intro x
    exact conformalRealMetric_det_pos a x
  inverse_law := by
    intro x i j
    exact conformalRealInverse_law a x i j
  complex_square_neg := by
    intro x i j
    exact standardComplexCoeff_square_neg i j
  complex_integrable := by
    intro x i j k
    simp
  metric_compatible := by
    intro x p i j
    simpa [conformalBismutConnection_eq_constant] using
      conformalBismutConnection_metricCompatible a x p i j
  complex_compatible := by
    intro x p i j
    simpa [conformalBismutConnection_eq_constant] using
      conformalBismutConnection_complexCompatible a x p i j
  torsion_matches := by
    intro x i j k
    change
      (∑ m,
        conformalRealMetric a x k m *
          (conformalBismutConnectionConstant a m i j -
            conformalBismutConnectionConstant a m j i)) =
        (conformalBismutTorsion a).value x i j k
    simpa [conformalBismutConnection_eq_constant] using
      conformalBismutConnection_torsion a x i j k
  gradientNormSq_nonneg := by
    intro x
    exact conformalGaussianGradientNorm_nonneg a τ x

/-- O volume real do background torsional é `e^{8φ}`. -/
theorem conformalCoordinate_volumeDensity
    (a τ f₀ : ℝ) (x : LocalPoint) :
    (conformalCoordinateBismutBackground a τ f₀).volumeDensity x =
      (conformalScale a x) ^ 4 := by
  unfold CoordinateBismutBackground.volumeDensity
  change
    Real.sqrt
      (Matrix.det (fun i j ↦ conformalRealMetric a x i j)) =
      (conformalScale a x) ^ 4
  rw [conformalRealMetric_det]
  rw [show
      conformalScale a x ^ 8 =
        (conformalScale a x ^ 4) ^ 2 by ring]
  rw [Real.sqrt_sq_eq_abs]
  rw [abs_of_nonneg]
  positivity

end GDQ
