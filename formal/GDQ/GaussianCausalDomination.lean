import GDQ.GaussianBulkDomination
import GDQ.ComplexContourAction
import Mathlib.Analysis.SpecialFunctions.Gaussian.GaussianIntegral
import Mathlib.MeasureTheory.Integral.IntegrableOn
import Mathlib.MeasureTheory.Measure.Lebesgue.Basic
import Mathlib.Tactic

namespace GDQ

open MeasureTheory

/-!
# Controle gaussiano na direção causal

No relógio exponencial, `γ*(dτ/τ)=κ dt` é constante. Portanto a finitude da
integral externa em toda a reta não segue do relógio: ela requer decaimento
do background integrado, ou outra especificação legítima do domínio causal.

Este arquivo formaliza um critério suficiente por decaimento gaussiano e
prova a obstrução elementar para um integrando temporal constante não nulo.
-/

/-- Envolvente temporal gaussiana complexificada a partir de uma função real. -/
noncomputable def causalGaussianEnvelope
    (a : ℝ) (t : ℝ) : ℂ :=
  (Real.exp (-a * t ^ 2) : ℂ)

/-- Para `a>0`, a envolvente temporal é integrável em toda a reta. -/
theorem causalGaussianEnvelope_integrable
    {a : ℝ} (ha : 0 < a) :
    Integrable (causalGaussianEnvelope a)
      (MeasureTheory.volume : Measure ℝ) := by
  exact (integrable_exp_neg_mul_sq ha).ofReal

/-- Uma constante vezes a envolvente temporal continua integrável. -/
theorem causalGaussianEnvelope_const_mul_integrable
    {a : ℝ} (ha : 0 < a) (C : ℂ) :
    Integrable (fun t ↦ C * causalGaussianEnvelope a t)
      (MeasureTheory.volume : Measure ℝ) :=
  (causalGaussianEnvelope_integrable ha).const_mul C

/--
Certificado reutilizável de integrabilidade causal por dominação gaussiana.
-/
noncomputable def causalGaussianDomination
    (f : ℝ → ℂ)
    (a : ℝ) (C : ℂ)
    (ha : 0 < a)
    (hf :
      AEStronglyMeasurable f
        (MeasureTheory.volume : Measure ℝ))
    (hbound :
      ∀ᵐ t ∂(MeasureTheory.volume : Measure ℝ),
        ‖f t‖ ≤ ‖C * causalGaussianEnvelope a t‖) :
    IntegrableDomination (MeasureTheory.volume : Measure ℝ) f where
  stronglyMeasurable := hf
  envelope := fun t ↦ C * causalGaussianEnvelope a t
  envelope_integrable :=
    causalGaussianEnvelope_const_mul_integrable ha C
  norm_le := hbound

/-- A medida de Lebesgue de toda a reta não é finita. -/
theorem realVolume_not_finite :
    ¬ IsFiniteMeasure (MeasureTheory.volume : Measure ℝ) := by
  intro hfinite
  letI := hfinite
  have hlt :
      (MeasureTheory.volume : Measure ℝ) Set.univ < ⊤ :=
    IsFiniteMeasure.measure_univ_lt_top
  rw [Real.volume_univ] at hlt
  exact (lt_irrefl ⊤) hlt

/--
Um integrando temporal constante não nulo não é integrável em toda a reta.
Assim, `dτ/τ=κ dt` constante não pode, sozinho, fechar a ação externa.
-/
theorem constant_nonzero_not_integrable_on_real
    {c : ℂ} (hc : c ≠ 0) :
    ¬ Integrable (fun _ : ℝ ↦ c)
      (MeasureTheory.volume : Measure ℝ) := by
  rw [integrable_const_iff]
  exact not_or_intro hc realVolume_not_finite

/--
Janela indicadora de um segmento causal finito. Ela representa uma
parametrização definida em `[t₀,t₁]` e estendida por zero fora do segmento;
não acrescenta termo à ação.
-/
noncomputable def finiteCausalWindow
    (t₀ t₁ : ℝ) (t : ℝ) : ℂ :=
  Set.indicator (Set.Icc t₀ t₁) (fun _ ↦ (1 : ℂ)) t

/-- A janela de um segmento causal finito é integrável. -/
theorem finiteCausalWindow_integrable
    (t₀ t₁ : ℝ) :
    Integrable (finiteCausalWindow t₀ t₁)
      (MeasureTheory.volume : Measure ℝ) := by
  unfold finiteCausalWindow
  have hconst :
      IntegrableOn (fun _ : ℝ ↦ (1 : ℂ)) (Set.Icc t₀ t₁)
        (MeasureTheory.volume : Measure ℝ) :=
    integrableOn_const measure_Icc_lt_top.ne
  exact hconst.integrable_indicator measurableSet_Icc

/-- Uma amplitude constante restrita ao segmento causal também é integrável. -/
theorem finiteCausalWindow_const_mul_integrable
    (t₀ t₁ : ℝ) (C : ℂ) :
    Integrable (fun t ↦ C * finiteCausalWindow t₀ t₁ t)
      (MeasureTheory.volume : Measure ℝ) :=
  (finiteCausalWindow_integrable t₀ t₁).const_mul C

/--
Certificado alternativo para um segmento causal finito. A extensão por zero
faz explícito que a integração física ocorre somente naquele segmento.
-/
noncomputable def finiteCausalWindowDomination
    (f : ℝ → ℂ)
    (t₀ t₁ : ℝ) (C : ℂ)
    (hf :
      AEStronglyMeasurable f
        (MeasureTheory.volume : Measure ℝ))
    (hbound :
      ∀ᵐ t ∂(MeasureTheory.volume : Measure ℝ),
        ‖f t‖ ≤ ‖C * finiteCausalWindow t₀ t₁ t‖) :
    IntegrableDomination (MeasureTheory.volume : Measure ℝ) f where
  stronglyMeasurable := hf
  envelope := fun t ↦ C * finiteCausalWindow t₀ t₁ t
  envelope_integrable :=
    finiteCausalWindow_const_mul_integrable t₀ t₁ C
  norm_le := hbound

/--
Dados de bounds gaussianos suficientes para construir uma instância
controlada da ação oficial complexa.

As desigualdades `bulkBound` e `contourBound` são as obrigações analíticas
específicas do background; o construtor não as inventa.
-/
structure GaussianControlledComplexContourBounds
    (fields : AdmissibleConfiguration)
    (contour : CausalContour)
    (geometry : EuclideanGeometricInvariants)
    (ℏ ΛC : ℝ) where
  bulkRate : ℝ → ℝ
  bulkRate_pos : ∀ t, 0 < bulkRate t
  bulkConstant : ℝ → ℂ
  bulkMeasurable :
    ∀ t,
      AEStronglyMeasurable
        (complexContourPointDensity ℏ ΛC fields geometry contour t)
        localBulkReferenceMeasure
  bulkBound :
    ∀ t,
      ∀ᵐ z ∂localBulkReferenceMeasure,
        ‖complexContourPointDensity
            ℏ ΛC fields geometry contour t z‖ ≤
          ‖bulkConstant t *
            localBulkGaussianEnvelope (bulkRate t) z‖
  contourRate : ℝ
  contourRate_pos : 0 < contourRate
  contourConstant : ℂ
  contourMeasurable :
    AEStronglyMeasurable
      (fun t ↦
        (∫ z,
          complexContourPointDensity
            ℏ ΛC fields geometry contour t z
          ∂localBulkReferenceMeasure) *
          contour.dlog t)
      (MeasureTheory.volume : Measure ℝ)
  contourBound :
    ∀ᵐ t ∂(MeasureTheory.volume : Measure ℝ),
      ‖(∫ z,
          complexContourPointDensity
            ℏ ΛC fields geometry contour t z
          ∂localBulkReferenceMeasure) *
          contour.dlog t‖ ≤
        ‖contourConstant *
          causalGaussianEnvelope contourRate t‖

/--
Os bounds explícitos constroem os dois certificados de dominação exigidos
por `ControlledComplexContourActionData`.
-/
noncomputable def
    GaussianControlledComplexContourBounds.toControlledAction
    (fields : AdmissibleConfiguration)
    (contour : CausalContour)
    (geometry : EuclideanGeometricInvariants)
    (ℏ ΛC : ℝ) (hΛC : ΛC ≠ 0)
    (B :
      GaussianControlledComplexContourBounds
        fields contour geometry ℏ ΛC) :
    ControlledComplexContourActionData where
  fields := fields
  contour := contour
  geometry := geometry
  ℏ := ℏ
  ΛC := ΛC
  ΛC_ne_zero := hΛC
  bulkControl := fun t ↦
    gaussianBulkDomination
      (complexContourPointDensity ℏ ΛC fields geometry contour t)
      (B.bulkRate t) (B.bulkConstant t)
      (B.bulkRate_pos t) (B.bulkMeasurable t) (B.bulkBound t)
  contourControl :=
    causalGaussianDomination
      (fun t ↦
        (∫ z,
          complexContourPointDensity
            ℏ ΛC fields geometry contour t z
          ∂localBulkReferenceMeasure) *
          contour.dlog t)
      B.contourRate B.contourConstant B.contourRate_pos
      B.contourMeasurable B.contourBound

end GDQ
