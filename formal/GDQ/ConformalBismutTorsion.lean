import GDQ.GaussianAdmissibleBackground
import Mathlib.Tactic

namespace GDQ

/-!
# Torção de Bismut de um ansatz Hermitiano conformal

O controle gaussiano plano possui `H=0` e não é material. Este módulo
constrói o primeiro ansatz torsional intrínseco sobre o bulk local:

* a estrutura complexa padrão é mantida;
* a forma fundamental é deformada por um fator conformal não constante;
* `dω` torna-se não nulo;
* a torção é definida pelo pullback complexo `H=d_J^cω`.

O módulo formaliza a álgebra pontual da 3-forma. A conexão de Bismut completa,
sua curvatura e a Hessiana oficial serão construídas nas camadas seguintes.
-/

/-- Parceiro complexo dos oito eixos reais. -/
def standardJPartner (i : Fin 8) : Fin 8 :=
  match i.1 with
  | 0 => 4
  | 1 => 5
  | 2 => 6
  | 3 => 7
  | 4 => 0
  | 5 => 1
  | 6 => 2
  | _ => 3

/-- Sinal de `J e_i = s_i e_{p(i)}`. -/
def standardJSign (i : Fin 8) : ℝ :=
  if i.1 < 4 then 1 else -1

/-- O parceiro complexo é uma involução. -/
theorem standardJPartner_involution (i : Fin 8) :
    standardJPartner (standardJPartner i) = i := by
  fin_cases i <;> rfl

/-- O sinal muda ao aplicar o parceiro complexo. -/
theorem standardJSign_partner (i : Fin 8) :
    standardJSign (standardJPartner i) = -standardJSign i := by
  fin_cases i <;>
    norm_num [standardJPartner, standardJSign]

/--
Forma de Kähler plana associada à estrutura complexa padrão.

A convenção de sinal é `ω₀(e_i,e_{p(i)})=-s_i`.
-/
def standardFundamentalForm (i j : Fin 8) : ℝ :=
  if j = standardJPartner i then -standardJSign i else 0

/-- A forma fundamental padrão é antissimétrica. -/
theorem standardFundamentalForm_skew (i j : Fin 8) :
    standardFundamentalForm i j = -standardFundamentalForm j i := by
  fin_cases i <;> fin_cases j <;>
    norm_num [standardFundamentalForm, standardJPartner, standardJSign,
      Fin.ext_iff]

/-- Potencial conformal linear numa direção não compacta. -/
def conformalPotential (a : ℝ) (z : LocalPoint) : ℝ :=
  a * z.1 0

/-- Fator métrico positivo `e^{2φ}`. -/
noncomputable def conformalScale (a : ℝ) (z : LocalPoint) : ℝ :=
  Real.exp (2 * conformalPotential a z)

theorem conformalScale_pos (a : ℝ) (z : LocalPoint) :
    0 < conformalScale a z := by
  exact Real.exp_pos _

/-- Derivada coordenada do fator conformal no ansatz linear. -/
noncomputable def conformalScaleDerivative
    (a : ℝ) (z : LocalPoint) (i : Fin 8) : ℝ :=
  if i = 0 then 2 * a * conformalScale a z else 0

/-- Forma fundamental conformal `ω=e^{2φ}ω₀`. -/
noncomputable def conformalFundamentalForm
    (a : ℝ) (z : LocalPoint) (i j : Fin 8) : ℝ :=
  conformalScale a z * standardFundamentalForm i j

/-- Derivada exterior coordenada de `ω`. -/
noncomputable def conformalDOmega
    (a : ℝ) (z : LocalPoint) (i j k : Fin 8) : ℝ :=
  conformalScaleDerivative a z i * standardFundamentalForm j k +
  conformalScaleDerivative a z j * standardFundamentalForm k i +
  conformalScaleDerivative a z k * standardFundamentalForm i j

/-- `dω` é antissimétrica nos dois primeiros índices. -/
theorem conformalDOmega_swap₁₂
    (a : ℝ) (z : LocalPoint) (i j k : Fin 8) :
    conformalDOmega a z i j k =
      -conformalDOmega a z j i k := by
  simp only [conformalDOmega]
  rw [standardFundamentalForm_skew j k,
    standardFundamentalForm_skew k i,
    standardFundamentalForm_skew i j]
  ring

/-- `dω` é antissimétrica nos dois últimos índices. -/
theorem conformalDOmega_swap₂₃
    (a : ℝ) (z : LocalPoint) (i j k : Fin 8) :
    conformalDOmega a z i j k =
      -conformalDOmega a z i k j := by
  simp only [conformalDOmega]
  rw [standardFundamentalForm_skew j k,
    standardFundamentalForm_skew k i,
    standardFundamentalForm_skew i j]
  ring

/--
Pullback complexo de `dω`, usado como convenção coordenada para
`d_J^cω`. O sinal global deverá permanecer fixo nas camadas de curvatura.
-/
noncomputable def conformalDJcOmega
    (a : ℝ) (z : LocalPoint) (i j k : Fin 8) : ℝ :=
  -(standardJSign i * standardJSign j * standardJSign k) *
    conformalDOmega a z
      (standardJPartner i)
      (standardJPartner j)
      (standardJPartner k)

/-- A 3-forma torsional do ansatz é, por construção, `H=d_J^cω`. -/
noncomputable def conformalBismutTorsion
    (a : ℝ) : TorsionData where
  value := conformalDJcOmega a
  swap₁₂ := by
    intro z i j k
    unfold conformalDJcOmega
    rw [conformalDOmega_swap₁₂]
    ring
  swap₂₃ := by
    intro z i j k
    unfold conformalDJcOmega
    rw [conformalDOmega_swap₂₃]
    ring

/-- Componente explícita não nula da torção conformal. -/
theorem conformalBismutTorsion_component
    (a : ℝ) (z : LocalPoint) :
    (conformalBismutTorsion a).value z 4 5 1 =
      2 * a * conformalScale a z := by
  norm_num [conformalBismutTorsion, conformalDJcOmega,
    conformalDOmega, conformalScaleDerivative,
    standardFundamentalForm, standardJPartner, standardJSign,
    Fin.ext_iff]

/-- Se `a≠0`, a torção do ansatz é materialmente não trivial. -/
theorem conformalBismutTorsion_nonzero
    {a : ℝ} (ha : a ≠ 0) (z : LocalPoint) :
    (conformalBismutTorsion a).value z 4 5 1 ≠ 0 := by
  rw [conformalBismutTorsion_component]
  exact mul_ne_zero (mul_ne_zero (by norm_num) ha)
    (ne_of_gt (conformalScale_pos a z))

/-- Métrica Hermitiana conformal associada a `ω=e^{2φ}ω₀`. -/
noncomputable def conformalHermitianMetric
    (a : ℝ) : HermitianMetricData where
  coeff := fun z μ ν ↦
    if μ = ν then (conformalScale a z : ℂ) else 0
  hermitian := by
    intro z μ ν
    by_cases h : μ = ν
    · subst ν
      simp
    · have h' : ν ≠ μ := Ne.symm h
      simp [h, h']
  positive := by
    intro z v hv
    simp only [mul_ite, ite_mul, mul_zero, zero_mul]
    have hsum :
        0 < ∑ i : Fin 4, Complex.normSq (v i) := by
      rw [Finset.sum_pos_iff_of_nonneg]
      · rcases Function.ne_iff.mp hv with ⟨i, hi⟩
        exact ⟨i, Finset.mem_univ i, Complex.normSq_pos.mpr hi⟩
      · intro i hi
        exact Complex.normSq_nonneg (v i)
    have hscale :
        0 < conformalScale a z :=
      conformalScale_pos a z
    have hprod :
        0 <
          conformalScale a z *
            ∑ i : Fin 4, Complex.normSq (v i) :=
      mul_pos hscale hsum
    rw [Finset.mul_sum] at hprod
    have hprod' :
        0 <
          ∑ i : Fin 4,
            ((v i).re * conformalScale a z * (v i).re +
              (v i).im * conformalScale a z * (v i).im) := by
      convert hprod using 1
      apply Finset.sum_congr rfl
      intro i hi
      simp [Complex.normSq_apply]
      ring
    simpa [Complex.mul_re] using hprod'

/-- Campos do candidato material conformal antes do testemunho de Bismut. -/
noncomputable def conformalMaterialFields
    (a τ f₀ : ℝ) : GDQFieldConfiguration where
  metric := conformalHermitianMetric a
  complexStructure := flatComplexStructure
  torsion := conformalBismutTorsion a
  potential := fun z ↦ (gaussianPotentialRe τ f₀ z.1 : ℂ)
  density := fun z ↦ gaussianDensity τ f₀ z.1
  density_nonneg := fun z ↦ (gaussianDensity_pos τ f₀ z.1).le
  potential_law := by
    intro z hz
    rfl
  kernel := fun q z ↦
    officialFlowKernel 4 (gaussianDensity τ f₀ z.1) q.zτ

/--
Testemunho algébrico torsional disponível antes da construção da conexão.

O campo `torsionMatchesH` registra literalmente `H=d_J^cω`. As equações
diferenciais `∇ᴮg=0` e `∇ᴮJ=0` serão fornecidas pelo futuro
`CoordinateBismutBackground`; por isso este objeto ainda é chamado candidato.
-/
noncomputable def conformalMaterialBismutWitness
    (a τ f₀ : ℝ) :
    BismutWitness (conformalMaterialFields a τ f₀) where
  connection := flatConnection
  complexIntegrable :=
    ∀ x v,
      flatComplexStructure.act x
        (flatComplexStructure.act x v) = -v
  metricCompatible :=
    ∀ x μ ν,
      (conformalHermitianMetric a).coeff x μ ν =
        starRingEnd ℂ ((conformalHermitianMetric a).coeff x ν μ)
  complexCompatible :=
    ∀ x v,
      flatComplexStructure.act x
        (flatComplexStructure.act x v) = -v
  torsionMatchesH :=
    ∀ x i j k,
      (conformalBismutTorsion a).value x i j k =
        conformalDJcOmega a x i j k
  complexIntegrable_proof := flatComplexStructure.square_neg
  metricCompatible_proof := (conformalHermitianMetric a).hermitian
  complexCompatible_proof := flatComplexStructure.square_neg
  torsionMatchesH_proof := by
    intro x i j k
    rfl

/-- Configuração admissível algébrica com torção conformal. -/
noncomputable def conformalMaterialAdmissible
    (a τ f₀ : ℝ) : AdmissibleConfiguration where
  toGDQFieldConfiguration := conformalMaterialFields a τ f₀
  bismut := conformalMaterialBismutWitness a τ f₀
  kernel_law := by
    intro q z
    rfl

/--
Para `a≠0`, o candidato conformal habita tipadamente o setor material.

Isto prova `H≠0` e a lei constitutiva. Não substitui a futura prova da
conexão coordenada de Bismut.
-/
noncomputable def conformalMaterialConfiguration
    (a τ f₀ : ℝ) (ha : a ≠ 0) :
    MaterialAdmissibleConfiguration where
  toAdmissibleConfiguration :=
    conformalMaterialAdmissible a τ f₀
  torsion_nonzero := by
    let z : LocalPoint :=
      (fun _ ↦ 0, fun _ ↦ 0)
    exact
      ⟨z, 4, 5, 1,
        conformalBismutTorsion_nonzero ha z⟩

end GDQ
