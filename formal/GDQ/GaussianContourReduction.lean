import GDQ.GaussianOfficialReduction
import GDQ.EuclideanOfficialAction
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic

namespace GDQ

open MeasureTheory

/-!
# Transporte da variação gaussiana pelo contorno causal

`GaussianOfficialReduction` provou que a variação pura de fase é exatamente
quadrática antes e depois da integral no bulk. Este arquivo inclui a
dependência no parâmetro real `t` do contorno e executa a segunda integral,
com o pullback explícito `γ*(dτ/τ)`.

O resultado é algébrico e não pressupõe que todo contorno seja exponencial.
Integrabilidade no bulk e no contorno continua sendo uma obrigação explícita.
-/

section IteratedPhaseVariation

variable {α : Type*} [MeasurableSpace α]

/-- Termo base pontual, agora dependente do parâmetro do contorno. -/
noncomputable def contourPhaseBaseTerm
    (prefactor base : ℝ → α → ℝ) (t : ℝ) (x : α) : ℝ :=
  prefactor t x * base t x

/-- Coeficiente quadrático pontual ao longo do contorno. -/
noncomputable def contourPhaseQuadraticTerm
    (τ : ℝ → ℝ)
    (prefactor phaseGradientNormSq : ℝ → α → ℝ)
    (t : ℝ) (x : α) : ℝ :=
  prefactor t x * τ t * phaseGradientNormSq t x

/--
Família de fase da ação iterada. O integrando é real no bulk e torna-se
complexo somente ao ser multiplicado pelo pullback causal `dτ/τ`.
-/
noncomputable def iteratedOfficialPhaseVariation
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (contour : CausalContour)
    (τ : ℝ → ℝ)
    (prefactor base phaseGradientNormSq : ℝ → α → ℝ)
    (s : ℝ) : ℂ :=
  ∫ t,
    (∫ x,
      (officialPhaseVariationDensity
        (prefactor t x) (τ t) (base t x)
        (phaseGradientNormSq t x) s : ℂ)
      ∂bulkMeasure) *
      contour.dlog t
    ∂contourMeasure

/-- Integral de contorno do termo independente da variação. -/
noncomputable def contourIntegratedPhaseBase
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (contour : CausalContour)
    (prefactor base : ℝ → α → ℝ) : ℂ :=
  ∫ t,
    (∫ x, (contourPhaseBaseTerm prefactor base t x : ℂ)
      ∂bulkMeasure) *
      contour.dlog t
    ∂contourMeasure

/-- Integral de contorno do coeficiente quadrático da fase. -/
noncomputable def contourIntegratedPhaseQuadratic
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (contour : CausalContour)
    (τ : ℝ → ℝ)
    (prefactor phaseGradientNormSq : ℝ → α → ℝ) : ℂ :=
  ∫ t,
    (∫ x,
      (contourPhaseQuadraticTerm τ prefactor
        phaseGradientNormSq t x : ℂ)
      ∂bulkMeasure) *
      contour.dlog t
    ∂contourMeasure

/--
Sob as quatro condições explícitas de integrabilidade, as integrais no bulk
e no contorno preservam exatamente a dependência quadrática em `s`.
-/
theorem iteratedOfficialPhaseVariation_eq_quadratic
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (contour : CausalContour)
    (τ : ℝ → ℝ)
    (prefactor base phaseGradientNormSq : ℝ → α → ℝ)
    (s : ℝ)
    (hbulkBase :
      ∀ t,
        Integrable
          (fun x ↦
            (contourPhaseBaseTerm prefactor base t x : ℂ))
          bulkMeasure)
    (hbulkQuad :
      ∀ t,
        Integrable
          (fun x ↦
            (contourPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq t x : ℂ))
          bulkMeasure)
    (hcontourBase :
      Integrable
        (fun t ↦
          (∫ x, (contourPhaseBaseTerm prefactor base t x : ℂ)
            ∂bulkMeasure) *
            contour.dlog t)
        contourMeasure)
    (hcontourQuad :
      Integrable
        (fun t ↦
          (∫ x,
            (contourPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq t x : ℂ)
            ∂bulkMeasure) *
            contour.dlog t)
        contourMeasure) :
    iteratedOfficialPhaseVariation bulkMeasure contourMeasure contour
        τ prefactor base phaseGradientNormSq s =
      contourIntegratedPhaseBase bulkMeasure contourMeasure contour
          prefactor base +
        (s ^ 2 : ℂ) *
          contourIntegratedPhaseQuadratic bulkMeasure contourMeasure contour
            τ prefactor phaseGradientNormSq := by
  unfold iteratedOfficialPhaseVariation
    contourIntegratedPhaseBase contourIntegratedPhaseQuadratic
  conv_lhs =>
    enter [2, t, 1, 2, x]
    rw [show
      (officialPhaseVariationDensity
        (prefactor t x) (τ t) (base t x)
          (phaseGradientNormSq t x) s : ℂ) =
        (contourPhaseBaseTerm prefactor base t x : ℂ) +
          (s ^ 2 : ℂ) *
            (contourPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq t x : ℂ) by
        norm_num [officialPhaseVariationDensity,
          contourPhaseBaseTerm, contourPhaseQuadraticTerm]
        ring]
  have hinner :
      ∀ t,
        (∫ x,
          ((contourPhaseBaseTerm prefactor base t x : ℂ) +
            (s ^ 2 : ℂ) *
              (contourPhaseQuadraticTerm τ prefactor
                phaseGradientNormSq t x : ℂ))
          ∂bulkMeasure) =
        (∫ x, (contourPhaseBaseTerm prefactor base t x : ℂ)
          ∂bulkMeasure) +
          (s ^ 2 : ℂ) *
            (∫ x,
              (contourPhaseQuadraticTerm τ prefactor
                phaseGradientNormSq t x : ℂ)
              ∂bulkMeasure) := by
    intro t
    rw [integral_add (hbulkBase t) ((hbulkQuad t).const_mul (s ^ 2))]
    rw [integral_const_mul]
  simp_rw [hinner]
  have hpoint :
      ∀ t,
        ((∫ x, (contourPhaseBaseTerm prefactor base t x : ℂ)
            ∂bulkMeasure) +
          (s ^ 2 : ℂ) *
            (∫ x,
              (contourPhaseQuadraticTerm τ prefactor
                phaseGradientNormSq t x : ℂ)
              ∂bulkMeasure)) *
            contour.dlog t =
        ((∫ x, (contourPhaseBaseTerm prefactor base t x : ℂ)
            ∂bulkMeasure) *
          contour.dlog t) +
          (s ^ 2 : ℂ) *
            ((∫ x,
              (contourPhaseQuadraticTerm τ prefactor
                phaseGradientNormSq t x : ℂ)
              ∂bulkMeasure) *
              contour.dlog t) := by
    intro t
    ring
  simp_rw [hpoint]
  rw [integral_add hcontourBase (hcontourQuad.const_mul (s ^ 2))]
  rw [integral_const_mul]

/-- Parte real da ação iterada, isto é, o funcional variacional físico. -/
noncomputable def realIteratedOfficialPhaseVariation
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (contour : CausalContour)
    (τ : ℝ → ℝ)
    (prefactor base phaseGradientNormSq : ℝ → α → ℝ)
    (s : ℝ) : ℝ :=
  (iteratedOfficialPhaseVariation bulkMeasure contourMeasure contour
    τ prefactor base phaseGradientNormSq s).re

/--
A segunda variação da parte real da ação completa é duas vezes a parte real
do coeficiente quadrático integrado no contorno.
-/
theorem realIteratedOfficialPhaseVariation_second
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (contour : CausalContour)
    (τ : ℝ → ℝ)
    (prefactor base phaseGradientNormSq : ℝ → α → ℝ)
    (h : ℝ) (hh : h ≠ 0)
    (hbulkBase :
      ∀ t,
        Integrable
          (fun x ↦
            (contourPhaseBaseTerm prefactor base t x : ℂ))
          bulkMeasure)
    (hbulkQuad :
      ∀ t,
        Integrable
          (fun x ↦
            (contourPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq t x : ℂ))
          bulkMeasure)
    (hcontourBase :
      Integrable
        (fun t ↦
          (∫ x, (contourPhaseBaseTerm prefactor base t x : ℂ)
            ∂bulkMeasure) *
            contour.dlog t)
        contourMeasure)
    (hcontourQuad :
      Integrable
        (fun t ↦
          (∫ x,
            (contourPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq t x : ℂ)
            ∂bulkMeasure) *
            contour.dlog t)
        contourMeasure) :
    symmetricSecondQuotient
      (realIteratedOfficialPhaseVariation bulkMeasure contourMeasure contour
        τ prefactor base phaseGradientNormSq) h =
      2 *
        (contourIntegratedPhaseQuadratic bulkMeasure contourMeasure contour
          τ prefactor phaseGradientNormSq).re := by
  rw [show
    realIteratedOfficialPhaseVariation bulkMeasure contourMeasure contour
        τ prefactor base phaseGradientNormSq =
      fun s ↦
        (contourIntegratedPhaseBase bulkMeasure contourMeasure contour
          prefactor base).re +
          (contourIntegratedPhaseQuadratic bulkMeasure contourMeasure contour
            τ prefactor phaseGradientNormSq).re * s ^ 2 by
      funext s
      unfold realIteratedOfficialPhaseVariation
      rw [iteratedOfficialPhaseVariation_eq_quadratic
        bulkMeasure contourMeasure contour τ prefactor base
        phaseGradientNormSq s hbulkBase hbulkQuad
        hcontourBase hcontourQuad]
      simp [Complex.mul_re, pow_two]
      ring]
  exact symmetricSecondQuotient_quadratic _ _ h hh

end IteratedPhaseVariation

section ExponentialClock

/-- Coeficiente quadrático integrado sem o peso causal `dτ/τ`. -/
noncomputable def unweightedContourPhaseQuadratic
    {α : Type*} [MeasurableSpace α]
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (τ : ℝ → ℝ)
    (prefactor phaseGradientNormSq : ℝ → α → ℝ) : ℂ :=
  ∫ t,
    (∫ x,
      (contourPhaseQuadraticTerm τ prefactor
        phaseGradientNormSq t x : ℂ)
      ∂bulkMeasure)
    ∂contourMeasure

/--
No relógio causal exponencial, o peso logarítmico do contorno é exatamente
o gerador constante `κ`; não se trata de uma aproximação assintótica.
-/
theorem exponentialContour_phaseWeight
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀)
    (bulkCoefficient : ℝ → ℂ) (t : ℝ) :
    bulkCoefficient t *
        (exponentialCausalContour τ₀ κ hτ₀).dlog t =
      bulkCoefficient t * (κ : ℂ) := by
  rw [exponentialPositiveRealSection_dlog]

/--
Consequentemente, o coeficiente Hessiano integrado no contorno exponencial é
o coeficiente sem peso multiplicado exatamente por `κ`.
-/
theorem contourIntegratedPhaseQuadratic_exponential_eq
    {α : Type*} [MeasurableSpace α]
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀)
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (τ : ℝ → ℝ)
    (prefactor phaseGradientNormSq : ℝ → α → ℝ) :
    contourIntegratedPhaseQuadratic bulkMeasure contourMeasure
        (exponentialCausalContour τ₀ κ hτ₀)
        τ prefactor phaseGradientNormSq =
      unweightedContourPhaseQuadratic bulkMeasure contourMeasure
        τ prefactor phaseGradientNormSq * (κ : ℂ) := by
  unfold contourIntegratedPhaseQuadratic unweightedContourPhaseQuadratic
  simp_rw [exponentialPositiveRealSection_dlog]
  rw [integral_mul_const]

/--
Se `κ>0` e o coeficiente sem peso é real e positivo, o bloco Hessiano de
fase permanece positivo depois do pullback causal exponencial.
-/
theorem contourIntegratedPhaseQuadratic_exponential_re_pos
    {α : Type*} [MeasurableSpace α]
    (τ₀ κ : ℝ) (hτ₀ : 0 < τ₀) (hκ : 0 < κ)
    (bulkMeasure : Measure α)
    (contourMeasure : Measure ℝ)
    (τ : ℝ → ℝ)
    (prefactor phaseGradientNormSq : ℝ → α → ℝ)
    (hreal :
      0 <
        (unweightedContourPhaseQuadratic bulkMeasure contourMeasure
          τ prefactor phaseGradientNormSq).re)
    (him :
      (unweightedContourPhaseQuadratic bulkMeasure contourMeasure
        τ prefactor phaseGradientNormSq).im = 0) :
    0 <
      (contourIntegratedPhaseQuadratic bulkMeasure contourMeasure
        (exponentialCausalContour τ₀ κ hτ₀)
        τ prefactor phaseGradientNormSq).re := by
  rw [contourIntegratedPhaseQuadratic_exponential_eq]
  simp [Complex.mul_re, him]
  exact mul_pos hreal hκ

end ExponentialClock

end GDQ
