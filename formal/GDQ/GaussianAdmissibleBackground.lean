import GDQ.GaussianOfficialReduction
import GDQ.GeometricInvariants
import Mathlib.Tactic

namespace GDQ

open scoped BigOperators Matrix

/-!
# Controle gaussiano plano sem torção

Este arquivo reúne em um único objeto de controle os dados que antes apareciam
separadamente:

* métrica Hermitiana identidade;
* estrutura complexa padrão em quatro planos reais;
* torção nula;
* potencial gaussiano real;
* densidade constitutiva e kernel oficial.

Por ter `H=0`, este objeto não pertence ao setor material da GDQ. Ele serve
somente como limite Kähler/plano, teste de integrabilidade e controle
analítico. Não pode fundamentar massa, spin, estômato ou a Hessiana física
material.

O testemunho de Bismut continua limitado pela interface abstrata atual de
`BismutWitness`: as propriedades registradas abaixo são identidades
coordenadas concretas disponíveis nesse nível, não uma prova de existência de
atlas suave ou de completude geodésica.
-/

/-- Métrica Hermitiana identidade em dimensão complexa quatro. -/
noncomputable def flatHermitianMetric : HermitianMetricData where
  coeff := fun _ μ ν ↦ if μ = ν then 1 else 0
  hermitian := by
    intro x μ ν
    by_cases h : μ = ν
    · subst ν
      simp
    · have h' : ν ≠ μ := Ne.symm h
      simp [h, h']
  positive := by
    intro x v hv
    simp only [mul_ite, ite_mul, mul_one, mul_zero, zero_mul]
    have hsum :
        0 < ∑ i : Fin 4, Complex.normSq (v i) := by
      rw [Finset.sum_pos_iff_of_nonneg]
      · rcases Function.ne_iff.mp hv with ⟨i, hi⟩
        exact ⟨i, Finset.mem_univ i, Complex.normSq_pos.mpr hi⟩
      · intro i hi
        exact Complex.normSq_nonneg (v i)
    simpa [Complex.mul_re, Complex.normSq_apply] using hsum

/-- Estrutura complexa padrão `J(a,b)=(-b,a)` em `ℝ⁴⊕ℝ⁴`. -/
def flatComplexStructure : ComplexStructureData where
  act := fun _ v ↦
    ![-v 4, -v 5, -v 6, -v 7, v 0, v 1, v 2, v 3]
  square_neg := by
    intro x v
    funext i
    fin_cases i <;> simp

/-- Torção nula do background plano. -/
def zeroTorsion : TorsionData where
  value := fun _ _ _ _ ↦ 0
  swap₁₂ := by simp
  swap₂₃ := by simp

/-- Conexão coordenada nula do background plano. -/
def flatConnection : ConnectionData :=
  fun _ _ _ ↦ 0

/-- Configuração de campos gaussiana antes do certificado de admissibilidade. -/
noncomputable def gaussianFlatFields
    (τ f₀ : ℝ) : GDQFieldConfiguration where
  metric := flatHermitianMetric
  complexStructure := flatComplexStructure
  torsion := zeroTorsion
  potential := fun z ↦ (gaussianPotentialRe τ f₀ z.1 : ℂ)
  density := fun z ↦ gaussianDensity τ f₀ z.1
  density_nonneg := fun z ↦ (gaussianDensity_pos τ f₀ z.1).le
  potential_law := by
    intro z hz
    rfl
  kernel := fun q z ↦
    officialFlowKernel 4 (gaussianDensity τ f₀ z.1) q.zτ

/--
Testemunho coordenado de Bismut disponível no nível abstrato atual.

Cada proposição é uma identidade já demonstrada pelos próprios dados:
`J²=-1`, Hermiticidade da métrica, compatibilidade representada novamente
pela mesma identidade de `J`, e antissimetria da torção nula. Uma futura
camada suave deverá refinar esse testemunho para `∇ᴮg=0`, `∇ᴮJ=0` e
`Tᴮ=H` como equações diferenciais.
-/
noncomputable def gaussianFlatBismutWitness
    (τ f₀ : ℝ) :
    BismutWitness (gaussianFlatFields τ f₀) where
  connection := flatConnection
  complexIntegrable :=
    ∀ x v,
      flatComplexStructure.act x
        (flatComplexStructure.act x v) = -v
  metricCompatible :=
    ∀ x μ ν,
      flatHermitianMetric.coeff x μ ν =
        starRingEnd ℂ (flatHermitianMetric.coeff x ν μ)
  complexCompatible :=
    ∀ x v,
      flatComplexStructure.act x
        (flatComplexStructure.act x v) = -v
  torsionMatchesH :=
    ∀ x i j k,
      zeroTorsion.value x i j k =
        -zeroTorsion.value x j i k
  complexIntegrable_proof := flatComplexStructure.square_neg
  metricCompatible_proof := flatHermitianMetric.hermitian
  complexCompatible_proof := flatComplexStructure.square_neg
  torsionMatchesH_proof := zeroTorsion.swap₁₂

/-- Background gaussiano plano que satisfaz a lei constitutiva do kernel. -/
noncomputable def gaussianFlatAdmissible
    (τ f₀ : ℝ) : AdmissibleConfiguration where
  toGDQFieldConfiguration := gaussianFlatFields τ f₀
  bismut := gaussianFlatBismutWitness τ f₀
  kernel_law := by
    intro q x
    rfl

/-- O controle gaussiano plano não possui torção material não trivial. -/
theorem gaussianFlatAdmissible_not_material
    (τ f₀ : ℝ) :
    ¬(gaussianFlatAdmissible τ f₀).HasNonzeroTorsion := by
  intro h
  rcases h with ⟨x, i, j, k, hH⟩
  exact hH rfl

/-- A densidade do objeto admissível é literalmente a gaussiana definida. -/
@[simp] theorem gaussianFlatAdmissible_rho
    (τ f₀ : ℝ) (z : LocalPoint) :
    (gaussianFlatAdmissible τ f₀).toGDQFieldConfiguration.rho z =
      gaussianDensity τ f₀ z.1 := by
  rfl

/-- O potencial do objeto admissível é o potencial gaussiano real. -/
@[simp] theorem gaussianFlatAdmissible_potential
    (τ f₀ : ℝ) (z : LocalPoint) :
    (gaussianFlatAdmissible τ f₀).potential z =
      (gaussianPotentialRe τ f₀ z.1 : ℂ) := by
  rfl

/-- Todo ponto do background gaussiano pertence ao locus regular. -/
theorem gaussianFlatAdmissible_regular
    (τ f₀ : ℝ) (z : LocalPoint) :
    (gaussianFlatAdmissible τ f₀).RegularAt z := by
  exact gaussianDensity_pos τ f₀ z.1

/-- Invariantes euclidianos explícitos do background plano gaussiano. -/
noncomputable def gaussianFlatInvariants
    (τ : ℝ) : EuclideanGeometricInvariants where
  scalarCurvature := fun _ _ ↦ 0
  gradientNormSq := fun _ z ↦ gaussianGradientNormSq τ z.1
  volumeDensity := fun _ _ ↦ 1
  gradientNormSq_nonneg := by
    intro t z
    unfold gaussianGradientNormSq
    exact Finset.sum_nonneg (fun i hi ↦ sq_nonneg _)
  volumeDensity_pos := by norm_num

@[simp] theorem gaussianFlatInvariants_scalarCurvature
    (τ t : ℝ) (z : LocalPoint) :
    (gaussianFlatInvariants τ).scalarCurvature t z = 0 := by
  rfl

@[simp] theorem gaussianFlatInvariants_gradientNormSq
    (τ t : ℝ) (z : LocalPoint) :
    (gaussianFlatInvariants τ).gradientNormSq t z =
      gaussianGradientNormSq τ z.1 := by
  rfl

@[simp] theorem gaussianFlatInvariants_volumeDensity
    (τ t : ℝ) (z : LocalPoint) :
    (gaussianFlatInvariants τ).volumeDensity t z = 1 := by
  rfl

end GDQ
