import GDQ.GaussianContourReduction
import GDQ.ControlledIntegrability
import Mathlib.Analysis.SpecialFunctions.Gaussian.FourierTransform
import Mathlib.MeasureTheory.Integral.Prod
import Mathlib.Tactic

namespace GDQ

open MeasureTheory
open scoped BigOperators

/-!
# Dominação gaussiana explícita no bulk local

Este arquivo constrói uma envolvente integrável concreta em
`ℝ⁴ × T⁴`. O decaimento ocorre nas quatro direções não compactas; a parte
toroidal contribui apenas com sua medida de Haar finita.

O resultado não declara que toda densidade oficial é dominada por essa
gaussiana. Em cada aplicação, a desigualdade de dominação continua sendo uma
obrigação matemática explícita.
-/

/-- A medida de Haar do toro compacto é finita. -/
noncomputable instance torusHaarFiniteMeasure (n : Nat) :
    IsFiniteMeasure (torusHaarMeasure n) := by
  unfold torusHaarMeasure
  infer_instance

/--
Gaussiana complexa positiva nas quatro coordenadas não compactas.

Escrevemos a soma coordenada na mesma forma usada pelo teorema gaussiano da
biblioteca, evitando uma identificação implícita entre normas distintas.
-/
noncomputable def euclidean4GaussianEnvelope
    (b : ℝ) (x : Euclidean4) : ℂ :=
  Complex.exp
    (-((b : ℂ) * ∑ i, (x i : ℂ) ^ 2) +
      ∑ i, (0 : ℂ) * (x i : ℂ))

/-- A envolvente complexa é exatamente a gaussiana real coordenada. -/
theorem euclidean4GaussianEnvelope_eq_real
    (b : ℝ) (x : Euclidean4) :
    euclidean4GaussianEnvelope b x =
      (Real.exp (-b * gaussianRadiusSq x) : ℂ) := by
  unfold euclidean4GaussianEnvelope gaussianRadiusSq
  rw [Complex.ofReal_exp]
  congr 1
  norm_num

/--
A densidade constitutiva do shrinker gaussiano é a envolvente anterior
multiplicada somente pela normalização constante `exp(-f₀)`.
-/
theorem gaussianDensity_eq_envelope
    {τ : ℝ} (hτ : τ ≠ 0) (f₀ : ℝ) (x : Euclidean4) :
    (gaussianDensity τ f₀ x : ℂ) =
      (Real.exp (-f₀) : ℂ) *
        euclidean4GaussianEnvelope (1 / (4 * τ)) x := by
  rw [euclidean4GaussianEnvelope_eq_real]
  rw [← Complex.ofReal_mul]
  congr 1
  rw [← Real.exp_add]
  unfold gaussianDensity gaussianPotentialRe
  congr 1
  field_simp
  ring

/-- Para `b>0`, a gaussiana de `ℝ⁴` é integrável. -/
theorem euclidean4GaussianEnvelope_integrable
    {b : ℝ} (hb : 0 < b) :
    Integrable (euclidean4GaussianEnvelope b)
      (MeasureTheory.volume : Measure Euclidean4) := by
  change
    Integrable
      (fun x : Euclidean4 ↦
        Complex.exp
          (-((b : ℂ) * ∑ i, (x i : ℂ) ^ 2) +
            ∑ i, (0 : ℂ) * (x i : ℂ)))
      (MeasureTheory.volume : Measure Euclidean4)
  have hbComplex : 0 < ((b : ℂ).re) := by
    simpa using hb
  simpa using
    (GaussianFourier.integrable_cexp_neg_mul_sum_add
      (b := (b : ℂ)) hbComplex (fun _ : Fin 4 ↦ (0 : ℂ)))

/-- Envolvente gaussiana no produto local, constante ao longo de `T⁴`. -/
noncomputable def localBulkGaussianEnvelope
    (b : ℝ) (z : LocalPoint) : ℂ :=
  euclidean4GaussianEnvelope b z.1

/--
A envolvente gaussiana é integrável na medida concreta
`Lebesgue(ℝ⁴) × Haar(T⁴)`.
-/
theorem localBulkGaussianEnvelope_integrable
    {b : ℝ} (hb : 0 < b) :
    Integrable (localBulkGaussianEnvelope b)
      localBulkReferenceMeasure := by
  unfold localBulkGaussianEnvelope localBulkReferenceMeasure
  exact
    (euclidean4GaussianEnvelope_integrable hb).comp_fst
      (torusHaarMeasure 4)

/-- Uma constante vezes a envolvente gaussiana também é integrável. -/
theorem localBulkGaussianEnvelope_const_mul_integrable
    {b : ℝ} (hb : 0 < b) (C : ℂ) :
    Integrable (fun z : LocalPoint ↦ C * localBulkGaussianEnvelope b z)
      localBulkReferenceMeasure :=
  (localBulkGaussianEnvelope_integrable hb).const_mul C

/--
Uma potência quadrática multiplicada por uma gaussiana é dominada por uma
gaussiana de taxa pela metade. Esta é a estimativa elementar que permite
absorver os coeficientes afins em `|x|²` produzidos pelo colchete oficial.
-/
theorem radius_mul_exp_neg_le_half_rate
    {b r : ℝ} (hb : 0 < b) (hr : 0 ≤ r) :
    r * Real.exp (-b * r) ≤
      (2 / b) * Real.exp (-(b / 2) * r) := by
  have hu : 0 ≤ b * r / 2 := by positivity
  have hexp : b * r / 2 ≤ Real.exp (b * r / 2) := by
    exact le_trans (le_add_of_nonneg_right zero_le_one)
      (Real.add_one_le_exp (b * r / 2))
  have hc : 0 ≤ 2 / b := by positivity
  have hscaled :=
    mul_le_mul_of_nonneg_left hexp hc
  have hgauss : 0 ≤ Real.exp (-b * r) :=
    (Real.exp_pos _).le
  have hmul :=
    mul_le_mul_of_nonneg_right hscaled hgauss
  calc
    r * Real.exp (-b * r) =
        ((2 / b) * (b * r / 2)) * Real.exp (-b * r) := by
          field_simp
    _ ≤ ((2 / b) * Real.exp (b * r / 2)) *
          Real.exp (-b * r) := by
          simpa [mul_assoc] using hmul
    _ = (2 / b) * Real.exp (-(b / 2) * r) := by
          rw [mul_assoc, ← Real.exp_add]
          congr 1
          ring_nf

/-- A gaussiana de taxa `b` é menor que a gaussiana de taxa `b/2`. -/
theorem exp_neg_le_half_rate
    {b r : ℝ} (hb : 0 < b) (hr : 0 ≤ r) :
    Real.exp (-b * r) ≤ Real.exp (-(b / 2) * r) := by
  apply Real.exp_le_exp.mpr
  nlinarith

/--
Envolvente afim universal:

`(1+r)e^{-br} ≤ (1+2/b)e^{-(b/2)r}` para `b>0`, `r≥0`.
-/
theorem one_add_radius_mul_exp_neg_le
    {b r : ℝ} (hb : 0 < b) (hr : 0 ≤ r) :
    (1 + r) * Real.exp (-b * r) ≤
      (1 + 2 / b) * Real.exp (-(b / 2) * r) := by
  rw [add_mul, one_mul, add_mul, one_mul]
  exact add_le_add
    (exp_neg_le_half_rate hb hr)
    (radius_mul_exp_neg_le_half_rate hb hr)

/--
Versão no bulk local: o fator `1+|x|²` é absorvido por uma gaussiana
integrável de taxa reduzida.
-/
theorem local_one_add_radius_gaussian_bound
    {b : ℝ} (hb : 0 < b) (z : LocalPoint) :
    (1 + gaussianRadiusSq z.1) *
        Real.exp (-b * gaussianRadiusSq z.1) ≤
      (1 + 2 / b) *
        Real.exp (-(b / 2) * gaussianRadiusSq z.1) := by
  exact one_add_radius_mul_exp_neg_le hb
    (Finset.sum_nonneg (fun i hi ↦ sq_nonneg _))

/--
O bloco espacial `(1+|x|²)e^{-b|x|²}` é integrável em `ℝ⁴×T⁴`.
-/
theorem local_one_add_radius_gaussian_integrable
    {b : ℝ} (hb : 0 < b) :
    Integrable
      (fun z : LocalPoint ↦
        ((1 + gaussianRadiusSq z.1) *
          Real.exp (-b * gaussianRadiusSq z.1) : ℝ))
      localBulkReferenceMeasure := by
  have henv :
      Integrable
        (fun z : LocalPoint ↦
          (1 + 2 / b) *
            Real.exp (-(b / 2) * gaussianRadiusSq z.1))
        localBulkReferenceMeasure := by
    have hb2 : 0 < b / 2 := by positivity
    have hcomplex :=
      localBulkGaussianEnvelope_const_mul_integrable hb2
        ((1 + 2 / b : ℝ) : ℂ)
    apply hcomplex.re.congr
    filter_upwards with z
    change
      (((1 + 2 / b : ℝ) : ℂ) *
        euclidean4GaussianEnvelope (b / 2) z.1).re =
          (1 + 2 / b) *
            Real.exp (-(b / 2) * gaussianRadiusSq z.1)
    rw [euclidean4GaussianEnvelope_eq_real]
    rw [Complex.mul_re, Complex.ofReal_re, Complex.ofReal_re,
      Complex.ofReal_im, Complex.ofReal_im]
    ring
  apply henv.mono'
  · unfold gaussianRadiusSq
    fun_prop
  · filter_upwards with z
    rw [Real.norm_eq_abs, abs_of_nonneg]
    · exact local_one_add_radius_gaussian_bound hb z
    · exact mul_nonneg
        (add_nonneg zero_le_one
          (Finset.sum_nonneg (fun i hi ↦ sq_nonneg _)))
        (Real.exp_pos _).le

/-- O momento radial quadrático da gaussiana também é integrável. -/
theorem local_radius_gaussian_integrable
    {b : ℝ} (hb : 0 < b) :
    Integrable
      (fun z : LocalPoint ↦
        gaussianRadiusSq z.1 *
          Real.exp (-b * gaussianRadiusSq z.1))
      localBulkReferenceMeasure := by
  have hmajor :=
    local_one_add_radius_gaussian_integrable hb
  apply hmajor.mono'
  · unfold gaussianRadiusSq
    fun_prop
  · filter_upwards with z
    rw [Real.norm_eq_abs, abs_of_nonneg]
    · have hr :
          0 ≤ gaussianRadiusSq z.1 :=
        Finset.sum_nonneg (fun i hi ↦ sq_nonneg _)
      exact mul_le_mul_of_nonneg_right
        (le_add_of_nonneg_left zero_le_one)
        (Real.exp_pos _).le
    · change
        0 ≤ gaussianRadiusSq z.1 *
          Real.exp (-b * gaussianRadiusSq z.1)
      exact mul_nonneg
        (Finset.sum_nonneg (fun i hi ↦ sq_nonneg _))
        (Real.exp_pos _).le

/--
O momento `|x|² ρ_*` da densidade constitutiva gaussiana é integrável no
bulk local para `τ>0`.
-/
theorem localGaussianRadiusDensity_integrable
    {τ : ℝ} (hτ : 0 < τ) (f₀ : ℝ) :
    Integrable
      (fun z : LocalPoint ↦
        (gaussianRadiusSq z.1 : ℂ) *
          (gaussianDensity τ f₀ z.1 : ℂ))
      localBulkReferenceMeasure := by
  have hb : 0 < 1 / (4 * τ) := by positivity
  have hmoment :=
    (local_radius_gaussian_integrable hb).ofReal.const_mul
      (Real.exp (-f₀) : ℂ)
  apply hmoment.congr
  filter_upwards with z
  unfold gaussianDensity gaussianPotentialRe
  have hreal :
      Real.exp (-f₀) *
          (gaussianRadiusSq z.1 *
            Real.exp (-(1 / (4 * τ)) * gaussianRadiusSq z.1)) =
        gaussianRadiusSq z.1 *
          Real.exp (-(gaussianRadiusSq z.1 / (4 * τ) + f₀)) := by
    rw [show
      Real.exp (-f₀) *
          (gaussianRadiusSq z.1 *
            Real.exp (-(1 / (4 * τ)) * gaussianRadiusSq z.1)) =
        gaussianRadiusSq z.1 *
          (Real.exp (-f₀) *
            Real.exp (-(1 / (4 * τ)) * gaussianRadiusSq z.1)) by ring]
    rw [← Real.exp_add]
    congr 2
    field_simp
    ring
  exact
    (Complex.ofReal_mul
      (Real.exp (-f₀))
      (gaussianRadiusSq z.1 *
        Real.exp (-(1 / (4 * τ)) *
          gaussianRadiusSq z.1))).symm.trans
      ((congrArg (fun r : ℝ ↦ (r : ℂ)) hreal).trans
        (Complex.ofReal_mul
          (gaussianRadiusSq z.1)
          (Real.exp
            (-(gaussianRadiusSq z.1 / (4 * τ) + f₀)))))

/--
Para `τ>0`, a densidade constitutiva gaussiana, estendida trivialmente no
toro, é integrável na medida local concreta.
-/
theorem localGaussianDensity_integrable
    {τ : ℝ} (hτ : 0 < τ) (f₀ : ℝ) :
    Integrable
      (fun z : LocalPoint ↦ (gaussianDensity τ f₀ z.1 : ℂ))
      localBulkReferenceMeasure := by
  have hb : 0 < 1 / (4 * τ) := by positivity
  have henv :=
    localBulkGaussianEnvelope_const_mul_integrable hb
      (Real.exp (-f₀) : ℂ)
  apply henv.congr
  filter_upwards with z
  symm
  exact gaussianDensity_eq_envelope (ne_of_gt hτ) f₀ z.1

/--
Certificado concreto de dominação para a própria densidade constitutiva
gaussiana do background.
-/
noncomputable def localGaussianDensityDomination
    {τ : ℝ} (hτ : 0 < τ) (f₀ : ℝ) :
    IntegrableDomination localBulkReferenceMeasure
      (fun z : LocalPoint ↦ (gaussianDensity τ f₀ z.1 : ℂ)) where
  stronglyMeasurable :=
    (localGaussianDensity_integrable hτ f₀).aestronglyMeasurable
  envelope := fun z ↦ (gaussianDensity τ f₀ z.1 : ℂ)
  envelope_integrable := localGaussianDensity_integrable hτ f₀
  norm_le := Filter.Eventually.of_forall (fun _ ↦ le_rfl)

/--
O bloco de fase com coeficiente espacial constante é uma constante vezes a
densidade gaussiana e, portanto, possui certificado explícito de
integrabilidade.
-/
noncomputable def localGaussianConstantBlockDomination
    {τ : ℝ} (hτ : 0 < τ) (f₀ : ℝ) (C : ℂ) :
    IntegrableDomination localBulkReferenceMeasure
      (fun z : LocalPoint ↦
        C * (gaussianDensity τ f₀ z.1 : ℂ)) where
  stronglyMeasurable :=
    ((localGaussianDensity_integrable hτ f₀).const_mul C).aestronglyMeasurable
  envelope := fun z ↦ C * (gaussianDensity τ f₀ z.1 : ℂ)
  envelope_integrable :=
    (localGaussianDensity_integrable hτ f₀).const_mul C
  norm_le := Filter.Eventually.of_forall (fun _ ↦ le_rfl)

/--
Construtor reutilizável de certificado: uma densidade mensurável dominada
por uma gaussiana explícita possui integral finita no bulk local.
-/
noncomputable def gaussianBulkDomination
    (f : LocalPoint → ℂ)
    (b : ℝ) (C : ℂ)
    (hb : 0 < b)
    (hf : AEStronglyMeasurable f localBulkReferenceMeasure)
    (hbound :
      ∀ᵐ z ∂localBulkReferenceMeasure,
        ‖f z‖ ≤ ‖C * localBulkGaussianEnvelope b z‖) :
    IntegrableDomination localBulkReferenceMeasure f where
  stronglyMeasurable := hf
  envelope := fun z ↦ C * localBulkGaussianEnvelope b z
  envelope_integrable :=
    localBulkGaussianEnvelope_const_mul_integrable hb C
  norm_le := hbound

/--
Corolário operacional: a desigualdade gaussiana explícita implica
integrabilidade da densidade alvo.
-/
theorem integrable_of_gaussianBulk_bound
    (f : LocalPoint → ℂ)
    (b : ℝ) (C : ℂ)
    (hb : 0 < b)
    (hf : AEStronglyMeasurable f localBulkReferenceMeasure)
    (hbound :
      ∀ᵐ z ∂localBulkReferenceMeasure,
        ‖f z‖ ≤ ‖C * localBulkGaussianEnvelope b z‖) :
    Integrable f localBulkReferenceMeasure :=
  (gaussianBulkDomination f b C hb hf hbound).integrable

end GDQ
