import GDQ.GaussianAdmissibleBackground
import GDQ.GaussianBulkDomination
import GDQ.ComplexContourAction
import Mathlib.Tactic

namespace GDQ

open MeasureTheory

/-!
# Integrabilidade espacial da densidade oficial gaussiana

O colchete oficial do background plano é afim em `|x|²`, enquanto o kernel
contém a densidade gaussiana. Este arquivo prova que a densidade pontual
completa — prefator, colchete, kernel e volume — é integrável no bulk local
para cada ponto regular do contorno causal.
-/

/-- Perfil espacial afim multiplicando a densidade gaussiana constitutiva. -/
noncomputable def gaussianComplexAffineProfile
    (τ f₀ : ℝ) (A B : ℂ) (z : LocalPoint) : ℂ :=
  (A * (gaussianRadiusSq z.1 : ℂ) + B) *
    (gaussianDensity τ f₀ z.1 : ℂ)

/-- Todo perfil afim-gaussiano é integrável para `τ>0`. -/
theorem gaussianComplexAffineProfile_integrable
    {τ : ℝ} (hτ : 0 < τ) (f₀ : ℝ) (A B : ℂ) :
    Integrable
      (gaussianComplexAffineProfile τ f₀ A B)
      localBulkReferenceMeasure := by
  have hr :=
    (localGaussianRadiusDensity_integrable hτ f₀).const_mul A
  have hρ :=
    (localGaussianDensity_integrable hτ f₀).const_mul B
  have hadd := hr.add hρ
  apply hadd.congr
  filter_upwards with z
  simp [gaussianComplexAffineProfile]
  ring

/-- Coeficiente comum produzido pelo prefator e pelo denominador do kernel. -/
noncomputable def gaussianOfficialCommonCoefficient
    (ℏ ΛC : ℝ) (zτ : ℂ) : ℂ :=
  ((ℏ / ΛC ^ 2 : ℝ) : ℂ) /
    ((((4 * Real.pi : ℝ) : ℂ) * zτ) ^ 4)

/-- Coeficiente de `|x|²` na densidade oficial gaussiana. -/
noncomputable def gaussianOfficialRadialCoefficient
    (τ ℏ ΛC : ℝ) (zτ : ℂ) : ℂ :=
  gaussianOfficialCommonCoefficient ℏ ΛC zτ *
    (zτ / (4 * (τ : ℂ) ^ 2) +
      1 / (4 * (τ : ℂ)))

/-- Coeficiente constante na densidade oficial gaussiana. -/
noncomputable def gaussianOfficialConstantCoefficient
    (f₀ ℏ ΛC : ℝ) (zτ : ℂ) : ℂ :=
  gaussianOfficialCommonCoefficient ℏ ΛC zτ *
    ((f₀ - 4 : ℝ) : ℂ)

/--
Redução literal da densidade oficial completa a um perfil afim-gaussiano.

Não há ansatz adicional: os dois coeficientes são apenas o resultado de
agrupar o prefator, o denominador do kernel e as parcelas de `|x|²`.
-/
theorem complexContourPointDensity_gaussian_eq_affine
    {τ : ℝ} (hτ : τ ≠ 0)
    (f₀ ℏ ΛC : ℝ)
    (γ : CausalContour) (t : ℝ) (z : LocalPoint) :
    complexContourPointDensity ℏ ΛC
        (gaussianFlatAdmissible τ f₀)
        (gaussianFlatInvariants τ) γ t z =
      gaussianComplexAffineProfile τ f₀
        (gaussianOfficialRadialCoefficient τ ℏ ΛC (γ.z t))
        (gaussianOfficialConstantCoefficient f₀ ℏ ΛC (γ.z t))
        z := by
  unfold complexContourPointDensity
    complexContourOfficialDensity complexOfficialBracket
    gaussianComplexAffineProfile
    gaussianOfficialRadialCoefficient
    gaussianOfficialConstantCoefficient
    gaussianOfficialCommonCoefficient officialFlowKernel
  simp only [gaussianFlatInvariants_scalarCurvature,
    gaussianFlatInvariants_gradientNormSq,
    gaussianFlatInvariants_volumeDensity,
    gaussianFlatAdmissible_potential,
    gaussianFlatAdmissible_rho,
    Complex.ofReal_re, zero_add,
    Complex.ofReal_one, mul_one]
  rw [gaussianGradientNormSq_eq hτ]
  rw [gaussianPotentialRe]
  push_cast
  field_simp [hτ, γ.nonzero t, Real.pi_ne_zero]
  ring

/--
Para todo instante do contorno, a densidade oficial do background gaussiano
é integrável em `ℝ⁴×T⁴`.
-/
theorem complexContourPointDensity_gaussian_integrable
    {τ : ℝ} (hτ : 0 < τ)
    (f₀ ℏ ΛC : ℝ)
    (γ : CausalContour) (t : ℝ) :
    Integrable
      (complexContourPointDensity ℏ ΛC
        (gaussianFlatAdmissible τ f₀)
        (gaussianFlatInvariants τ) γ t)
      localBulkReferenceMeasure := by
  apply
    (gaussianComplexAffineProfile_integrable hτ f₀
      (gaussianOfficialRadialCoefficient τ ℏ ΛC (γ.z t))
      (gaussianOfficialConstantCoefficient f₀ ℏ ΛC (γ.z t))).congr
  filter_upwards with z
  exact
    (complexContourPointDensity_gaussian_eq_affine
      (ne_of_gt hτ) f₀ ℏ ΛC γ t z).symm

/-- Certificado espacial concreto exigido pela ação controlada. -/
noncomputable def gaussianOfficialBulkControl
    {τ : ℝ} (hτ : 0 < τ)
    (f₀ ℏ ΛC : ℝ)
    (γ : CausalContour) (t : ℝ) :
    IntegrableDomination localBulkReferenceMeasure
      (complexContourPointDensity ℏ ΛC
        (gaussianFlatAdmissible τ f₀)
        (gaussianFlatInvariants τ) γ t) where
  stronglyMeasurable :=
    (complexContourPointDensity_gaussian_integrable
      hτ f₀ ℏ ΛC γ t).aestronglyMeasurable
  envelope :=
    complexContourPointDensity ℏ ΛC
      (gaussianFlatAdmissible τ f₀)
      (gaussianFlatInvariants τ) γ t
  envelope_integrable :=
    complexContourPointDensity_gaussian_integrable
      hτ f₀ ℏ ΛC γ t
  norm_le := Filter.Eventually.of_forall (fun _ ↦ le_rfl)

/--
Controle externo de um segmento causal finito.

O bound é uma obrigação específica do contorno/background. A estrutura não
o ajusta nem o deduz de dados experimentais.
-/
structure GaussianFiniteSegmentContourBound
    (τ f₀ ℏ ΛC : ℝ) (γ : CausalContour) where
  t₀ : ℝ
  t₁ : ℝ
  constant : ℂ
  stronglyMeasurable :
    AEStronglyMeasurable
      (fun t ↦
        (∫ z,
          complexContourPointDensity ℏ ΛC
            (gaussianFlatAdmissible τ f₀)
            (gaussianFlatInvariants τ) γ t z
          ∂localBulkReferenceMeasure) *
          γ.dlog t)
      ((MeasureTheory.volume : Measure ℝ).restrict
        (Set.Icc t₀ t₁))
  norm_le :
    ∀ᵐ t ∂((MeasureTheory.volume : Measure ℝ).restrict
      (Set.Icc t₀ t₁)),
      ‖(∫ z,
          complexContourPointDensity ℏ ΛC
            (gaussianFlatAdmissible τ f₀)
            (gaussianFlatInvariants τ) γ t z
          ∂localBulkReferenceMeasure) *
          γ.dlog t‖ ≤ ‖constant‖

/-- Uma constante é integrável na medida de um segmento finito. -/
theorem constant_integrable_on_finite_segment
    (t₀ t₁ : ℝ) (C : ℂ) :
    Integrable (fun _ : ℝ ↦ C)
      ((MeasureTheory.volume : Measure ℝ).restrict
        (Set.Icc t₀ t₁)) := by
  exact integrableOn_const measure_Icc_lt_top.ne

/--
O background gaussiano e um bound causal explícito constroem uma ação
oficial bem definida sobre o segmento `[t₀,t₁]`.

A restrição está na medida do domínio externo; o integrando oficial não é
alterado.
-/
noncomputable def gaussianFiniteSegmentAction
    {τ : ℝ} (hτ : 0 < τ)
    (f₀ ℏ ΛC : ℝ)
    (γ : CausalContour)
    (B : GaussianFiniteSegmentContourBound τ f₀ ℏ ΛC γ) :
    PulledBackActionCandidate where
  bulkMeasure := localBulkReferenceMeasure
  contourMeasure :=
    (MeasureTheory.volume : Measure ℝ).restrict
      (Set.Icc B.t₀ B.t₁)
  fields := gaussianFlatAdmissible τ f₀
  contour := γ
  pointDensity :=
    complexContourPointDensity ℏ ΛC
      (gaussianFlatAdmissible τ f₀)
      (gaussianFlatInvariants τ) γ
  bulkIntegrable :=
    complexContourPointDensity_gaussian_integrable
      hτ f₀ ℏ ΛC γ
  contourIntegrable := by
    apply
      (constant_integrable_on_finite_segment
        B.t₀ B.t₁ B.constant).mono
        B.stronglyMeasurable
    filter_upwards [B.norm_le] with t ht
    simpa using ht

/-- O valor do segmento usa literalmente a densidade e o pullback oficiais. -/
theorem gaussianFiniteSegmentAction_value
    {τ : ℝ} (hτ : 0 < τ)
    (f₀ ℏ ΛC : ℝ)
    (γ : CausalContour)
    (B : GaussianFiniteSegmentContourBound τ f₀ ℏ ΛC γ) :
    (gaussianFiniteSegmentAction hτ f₀ ℏ ΛC γ B).value =
      ∫ t in Set.Icc B.t₀ B.t₁,
        (∫ z,
          complexContourPointDensity ℏ ΛC
            (gaussianFlatAdmissible τ f₀)
            (gaussianFlatInvariants τ) γ t z
          ∂localBulkReferenceMeasure) *
          γ.dlog t := by
  rfl

end GDQ
