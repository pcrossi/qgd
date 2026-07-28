import GDQ.C3ConcreteHessian
import GDQ.ActionDensity
import Mathlib.MeasureTheory.Integral.Bochner.Basic
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators

/-!
# Redução gaussiana direta da densidade oficial

Esta camada calcula somente identidades que seguem literalmente do integrando
oficial num fundo plano gaussiano. Ela não substitui a integral por um
funcional auxiliar e não declara que o setor métrico gauge-fixado já foi
construído.
-/

/-- Norma quadrática das quatro coordenadas não compactas. -/
def gaussianRadiusSq (x : Euclidean4) : ℝ :=
  ∑ i, x i ^ 2

/-- Parte real do potencial do shrinker gaussiano. -/
noncomputable def gaussianPotentialRe
    (τ f₀ : ℝ) (x : Euclidean4) : ℝ :=
  gaussianRadiusSq x / (4 * τ) + f₀

/-- Densidade constitutiva do background gaussiano. -/
noncomputable def gaussianDensity
    (τ f₀ : ℝ) (x : Euclidean4) : ℝ :=
  Real.exp (-gaussianPotentialRe τ f₀ x)

/-- A densidade gaussiana é estritamente positiva para todo ponto. -/
theorem gaussianDensity_pos
    (τ f₀ : ℝ) (x : Euclidean4) :
    0 < gaussianDensity τ f₀ x := by
  exact Real.exp_pos _

/-- Gradiente coordenado da parte real do potencial gaussiano. -/
noncomputable def gaussianPotentialGradient
    (τ : ℝ) (x : Euclidean4) : Euclidean4 :=
  fun i => x i / (2 * τ)

/-- Norma quadrática do gradiente gaussiano na métrica plana. -/
noncomputable def gaussianGradientNormSq
    (τ : ℝ) (x : Euclidean4) : ℝ :=
  ∑ i, gaussianPotentialGradient τ x i ^ 2

/-- Fórmula explícita da norma do gradiente. -/
theorem gaussianGradientNormSq_eq
    {τ : ℝ} (hτ : τ ≠ 0) (x : Euclidean4) :
    gaussianGradientNormSq τ x =
      gaussianRadiusSq x / (4 * τ ^ 2) := by
  unfold gaussianGradientNormSq gaussianPotentialGradient gaussianRadiusSq
  rw [Finset.sum_div]
  apply Finset.sum_congr rfl
  intro i _
  field_simp
  ring

/-- Colchete oficial pontual no fundo plano gaussiano. -/
noncomputable def gaussianOfficialBracket
    (τ f₀ : ℝ) (x : Euclidean4) : ℝ :=
  officialBracket 4 τ 0
    (gaussianGradientNormSq τ x)
    (gaussianPotentialRe τ f₀ x)

/-- Expansão literal do colchete gaussiano. -/
theorem gaussianOfficialBracket_eq
    {τ : ℝ} (hτ : τ ≠ 0) (f₀ : ℝ) (x : Euclidean4) :
    gaussianOfficialBracket τ f₀ x =
      gaussianRadiusSq x / (2 * τ) + f₀ - 4 := by
  rw [gaussianOfficialBracket, officialBracket,
    gaussianGradientNormSq_eq hτ]
  simp [gaussianPotentialRe]
  field_simp
  ring

/--
Quociente central exato usado para identificar uma segunda variação sem
introduzir aproximação em diferenças finitas.
-/
noncomputable def symmetricSecondQuotient
    (F : ℝ → ℝ) (h : ℝ) : ℝ :=
  (F h - 2 * F 0 + F (-h)) / h ^ 2

/-- O quociente central de uma função quadrática é exatamente `2b`. -/
theorem symmetricSecondQuotient_quadratic
    (a b h : ℝ) (hh : h ≠ 0) :
    symmetricSecondQuotient (fun s => a + b * s ^ 2) h =
      2 * b := by
  unfold symmetricSecondQuotient
  field_simp
  ring

/--
Densidade oficial quando somente a parte imaginária de `f` varia como
`Im f_s = s v`. `phaseGradientNormSq` representa `|∇v|²`.

A densidade e `Re f` permanecem fixas nessa variação.
-/
noncomputable def officialPhaseVariationDensity
    (prefactor τ base phaseGradientNormSq s : ℝ) : ℝ :=
  prefactor * (base + τ * s ^ 2 * phaseGradientNormSq)

/--
Segunda variação pontual exata do setor de fase, extraída do integrando
oficial.
-/
theorem officialPhaseVariation_second
    (prefactor τ base phaseGradientNormSq h : ℝ)
    (hh : h ≠ 0) :
    symmetricSecondQuotient
      (officialPhaseVariationDensity
        prefactor τ base phaseGradientNormSq) h =
      2 * prefactor * τ * phaseGradientNormSq := by
  rw [show
      officialPhaseVariationDensity
          prefactor τ base phaseGradientNormSq =
        fun s =>
          prefactor * base +
            (prefactor * τ * phaseGradientNormSq) * s ^ 2 by
        funext s
        simp [officialPhaseVariationDensity]
        ring]
  rw [symmetricSecondQuotient_quadratic _ _ h hh]
  ring

/-- A primeira variação simétrica da fase em `s=0` se anula exatamente. -/
theorem officialPhaseVariation_stationary_at_zero
    (prefactor τ base phaseGradientNormSq h : ℝ) :
    officialPhaseVariationDensity
        prefactor τ base phaseGradientNormSq h -
      officialPhaseVariationDensity
        prefactor τ base phaseGradientNormSq (-h) = 0 := by
  simp [officialPhaseVariationDensity]

/-- Quociente simétrico de primeira variação em torno de `s`. -/
noncomputable def symmetricFirstQuotientAt
    (F : ℝ → ℝ) (s h : ℝ) : ℝ :=
  (F (s + h) - F (s - h)) / (2 * h)

/--
Primeira variação exata da família de fase. Como a família é quadrática,
nenhum limite numérico ou resto assintótico é necessário.
-/
theorem officialPhaseVariation_first_exact
    (prefactor τ base phaseGradientNormSq s h : ℝ)
    (hh : h ≠ 0) :
    symmetricFirstQuotientAt
      (officialPhaseVariationDensity
        prefactor τ base phaseGradientNormSq) s h =
      2 * prefactor * τ * phaseGradientNormSq * s := by
  unfold symmetricFirstQuotientAt officialPhaseVariationDensity
  field_simp
  ring

/-- Em `s=0`, a primeira variação exata se anula. -/
theorem officialPhaseVariation_first_at_zero
    (prefactor τ base phaseGradientNormSq h : ℝ)
    (hh : h ≠ 0) :
    symmetricFirstQuotientAt
      (officialPhaseVariationDensity
        prefactor τ base phaseGradientNormSq) 0 h = 0 := by
  rw [officialPhaseVariation_first_exact _ _ _ _ _ h hh]
  ring

/--
Com prefator, fluxo e norma de gradiente positivos, a segunda variação da
fase é positiva.
-/
theorem officialPhaseVariation_second_pos
    {prefactor τ phaseGradientNormSq : ℝ}
    (hp : 0 < prefactor) (hτ : 0 < τ)
    (hv : 0 < phaseGradientNormSq) :
    0 < 2 * prefactor * τ * phaseGradientNormSq := by
  positivity

section IntegratedPhaseBlock

open MeasureTheory

variable {α : Type*} [MeasurableSpace α]

/-- Parcela independente da amplitude na variação de fase. -/
noncomputable def officialPhaseBaseTerm
    (prefactor base : α → ℝ) (x : α) : ℝ :=
  prefactor x * base x

/-- Coeficiente quadrático pontual da variação de fase. -/
noncomputable def officialPhaseQuadraticTerm
    (τ : ℝ) (prefactor phaseGradientNormSq : α → ℝ)
    (x : α) : ℝ :=
  prefactor x * τ * phaseGradientNormSq x

omit [MeasurableSpace α] in
/-- A densidade variável separa-se exatamente em termo base e termo quadrático. -/
theorem officialPhaseVariationDensity_split
    (τ s : ℝ) (prefactor base phaseGradientNormSq : α → ℝ)
    (x : α) :
    officialPhaseVariationDensity
        (prefactor x) τ (base x) (phaseGradientNormSq x) s =
      officialPhaseBaseTerm prefactor base x +
        s ^ 2 *
          officialPhaseQuadraticTerm τ prefactor
            phaseGradientNormSq x := by
  simp [officialPhaseVariationDensity, officialPhaseBaseTerm,
    officialPhaseQuadraticTerm]
  ring

/-- A família de fase integrada sobre uma medida arbitrária do bulk. -/
noncomputable def integratedOfficialPhaseVariation
    (μ : Measure α) (τ : ℝ)
    (prefactor base phaseGradientNormSq : α → ℝ)
    (s : ℝ) : ℝ :=
  ∫ x,
    officialPhaseVariationDensity
      (prefactor x) τ (base x) (phaseGradientNormSq x) s
    ∂μ

/--
Sob integrabilidade explícita, a integral preserva exatamente a estrutura
quadrática da variação.
-/
theorem integratedOfficialPhaseVariation_eq_quadratic
    (μ : Measure α) (τ s : ℝ)
    (prefactor base phaseGradientNormSq : α → ℝ)
    (hbase : Integrable (officialPhaseBaseTerm prefactor base) μ)
    (hquad :
      Integrable
        (officialPhaseQuadraticTerm τ prefactor phaseGradientNormSq) μ) :
    integratedOfficialPhaseVariation μ τ prefactor base
        phaseGradientNormSq s =
      (∫ x, officialPhaseBaseTerm prefactor base x ∂μ) +
        s ^ 2 *
          (∫ x,
            officialPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq x ∂μ) := by
  unfold integratedOfficialPhaseVariation
  conv_lhs =>
    enter [2, x]
    rw [officialPhaseVariationDensity_split]
  rw [integral_add hbase (hquad.const_mul (s ^ 2))]
  rw [integral_const_mul]

/--
A segunda variação da ação integrada é a integral do coeficiente Hessiano
pontual. Não há troca informal de limite com integral: a dependência é
quadrática exata antes e depois da integração.
-/
theorem integratedOfficialPhaseVariation_second
    (μ : Measure α) (τ h : ℝ)
    (prefactor base phaseGradientNormSq : α → ℝ)
    (hh : h ≠ 0)
    (hbase : Integrable (officialPhaseBaseTerm prefactor base) μ)
    (hquad :
      Integrable
        (officialPhaseQuadraticTerm τ prefactor phaseGradientNormSq) μ) :
    symmetricSecondQuotient
      (integratedOfficialPhaseVariation μ τ prefactor base
        phaseGradientNormSq) h =
      2 *
        (∫ x,
          officialPhaseQuadraticTerm τ prefactor
            phaseGradientNormSq x ∂μ) := by
  rw [show
    integratedOfficialPhaseVariation μ τ prefactor base
        phaseGradientNormSq =
      fun s =>
        (∫ x, officialPhaseBaseTerm prefactor base x ∂μ) +
          s ^ 2 *
            (∫ x,
              officialPhaseQuadraticTerm τ prefactor
                phaseGradientNormSq x ∂μ) by
      funext s
      exact integratedOfficialPhaseVariation_eq_quadratic
        μ τ s prefactor base phaseGradientNormSq hbase hquad]
  rw [show
    (fun s =>
      (∫ x, officialPhaseBaseTerm prefactor base x ∂μ) +
        s ^ 2 *
          (∫ x,
            officialPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq x ∂μ)) =
      (fun s =>
        (∫ x, officialPhaseBaseTerm prefactor base x ∂μ) +
          (∫ x,
            officialPhaseQuadraticTerm τ prefactor
              phaseGradientNormSq x ∂μ) * s ^ 2) by
      funext s
      ring]
  exact symmetricSecondQuotient_quadratic _ _ h hh

end IntegratedPhaseBlock

/--
Bloco reduzido já extraído diretamente da ação.

`metricDilatonMatchesOU` permanece obrigação porque exige a construção do
gauge Hermitiano--DeTurck e o complemento de Schur no espaço de campos.
-/
structure GaussianOfficialBlockCertificate where
  τ : ℝ
  τ_pos : 0 < τ
  phaseBlockIsTwiceOU : Prop
  phaseBlockIsTwiceOU_proof : phaseBlockIsTwiceOU
  radialHomogeneousFromOfficialAction : Prop
  radialHomogeneousFromOfficialAction_proof :
    radialHomogeneousFromOfficialAction
  mixedAngularRadialVanishesByFluxConservation : Prop
  mixedAngularRadialVanishesByFluxConservation_proof :
    mixedAngularRadialVanishesByFluxConservation
  metricDilatonMatchesOU : Prop
  metricDilatonMatchesOU_proof : metricDilatonMatchesOU

/--
O certificado completo, combinado com a álgebra concreta `C₃`, fornece a
fórmula reduzida do gap sem pós-ajuste.
-/
theorem gaussian_c3_gap_from_official_blocks
    (G : GaussianOfficialBlockCertificate)
    {κT2 : ℝ} (hκ : 0 < κT2) :
    0 < c3PhysicalGap κT2 G.τ :=
  c3PhysicalGap_pos hκ G.τ_pos

end GDQ
